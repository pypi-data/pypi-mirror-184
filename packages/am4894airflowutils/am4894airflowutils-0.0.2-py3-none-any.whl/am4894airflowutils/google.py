import json
import logging
from typing import List, Any

import pendulum
from airflow.hooks.base import BaseHook
from airflow.models.baseoperator import BaseOperator
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook
from airflow.providers.google.cloud.hooks.secret_manager import SecretsManagerHook
from googleapiclient.discovery import build
from google.oauth2 import service_account
from am4894airflowutils.utils import dest_dict
from am4894airflowutils import GCP_PROJECTS


def gcp_get_secrets(secret_id: str, secret_version: str = 'latest',
                    project_id: str = GCP_PROJECTS.MY_PROJECT.id, gcp_conn_id="google_cloud_default"):
    return SecretsManagerHook(gcp_conn_id=gcp_conn_id).get_secret(
        secret_id=secret_id, secret_version=secret_version, project_id=project_id
    )


class SearchConsoleSearchAnalyticsOperator(BaseOperator):
    template_fields = ["site_urls", "request"]
    template_fields_renderers = {"site_urls": "md", "request": "json"}

    def __init__(self, site_urls: List[str] = None, start_date: str = None, end_date: str = None, **kwargs):
        super(SearchConsoleSearchAnalyticsOperator, self).__init__(**kwargs)
        self.site_urls = site_urls
        self.request = {
            'startDate': start_date,
            'endDate': end_date,
            'dimensions': ['date', 'page', 'query'],
            # max number of rows
            'rowLimit': 25000
        }

    def execute(self, context: Any):
        bq_hook = BigQueryHook(gcp_conn_id='google_cloud_default')
        credentials = service_account.Credentials.from_service_account_info(
            json.loads(
                json.loads(
                    BaseHook.get_connection('google_cloud_default').extra
                ).get('extra__google_cloud_platform__keyfile_dict')
            )
        )

        service = build('searchconsole', 'v1', credentials=credentials, cache_discovery=False)

        if not self.site_urls:
            site_list = service.sites().list().execute()
            self.site_urls = [s['siteUrl'] for s in site_list['siteEntry']
                              if s['permissionLevel'] != 'siteUnverifiedUser'
                              and s['siteUrl'][:4] == 'http']

        sa = service.searchanalytics()

        destination_dict = dest_dict(f'{GCP_PROJECTS.MY_PROJECT.id}.searchconsole.searchanalytics_daily',
                                     ignore_env=context['params'].get('ignore_env'))

        for site_url in self.site_urls:
            rows = [
                {'page': row['keys'][self.request['dimensions'].index('page')], 'date': pendulum.parse(row['keys'][self.request['dimensions'].index('date')]),
                 'query': row['keys'][self.request['dimensions'].index('query')],
                 'clicks': row['clicks'],
                 'impressions': row['impressions'],
                 'ctr': row['ctr'],
                 'position': row['position'],
                 }
                for row in sa.query(siteUrl=site_url, body=self.request).execute().get('rows', [])
            ]

            if rows:
                logging.info(f'{len(rows)} for {site_url}')
                bq_hook.insert_all(project_id=destination_dict['projectId'], dataset_id=destination_dict['datasetId'],
                                   table_id=destination_dict['tableId'], rows=rows,
                                   ignore_unknown_values=True, fail_on_error=True)
            else:
                logging.warning(f'no data for {site_url}')

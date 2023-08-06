import json
import logging
from typing import Any

import pandas as pd
import requests
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook
from jinja2 import Template
from am4894airflowutils import GCP_PROJECTS, google
from am4894airflowutils.bigquery import MyBigQueryBaseOperator
from requests.adapters import HTTPAdapter, Retry
from . import airflow

GAINSIGHT_API_URL: str = "https://api.aptrinsic.com/v1/users"
DATASET_ID: str = "gainsight"


def update_gainsight_user(
        session_: requests.Session, user_id: str, custom_attributes: str
) -> int:
    json_payload = {
        k: int(v) if isinstance(v, str) and v.isdigit() and k != 'terms_version' else v
        for k, v in json.loads(custom_attributes).items()
    }
    if 'active_user' in json_payload:
        json_payload['active_user'] = json_payload['active_user'] in ('true', 1, '1', 't')
    r = session_.request(
        "PUT",
        f"{GAINSIGHT_API_URL}/{user_id}",
        json={"customAttributes": json_payload},
    )
    if r.status_code not in (204, 404):
        logging.error(
            f"Status code: {r.status_code} for: {user_id} {json_payload} {r.text} | response body: {r.text}")
    return r.status_code


class GainsightUserAttrOperator(MyBigQueryBaseOperator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open(self.sql_filepath, 'r') as f:
            self.query = Template(f.read()).render(ds='{{ ds }}', n_max=self.n_max)
        self.project_id = GCP_PROJECTS.MY_PROJECT.id
        self.dataset_id = DATASET_ID
        self.table_id = 'user_attributes_processed'
        self.destination_table = f"{self.project_id}.{self.dataset_id}.{self.table_id}${{{{ ds_nodash }}}}"

    def execute(self, context: Any):
        bq_hook = BigQueryHook(gcp_conn_id='google_cloud_default')
        df_users_updates = bq_hook.get_pandas_df(self.query, dialect='standard', progress_bar_type=None)

        if not len(df_users_updates):
            logging.warning("No data to process")
            return

        logging.info(f"{len(df_users_updates)} need update")

        retry_strategy = Retry(
            total=4,
            status_forcelist=[502],
            allowed_methods=["PUT"],
            backoff_factor=5  # 0s, 10s, 20s, 40s
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        session.headers.update(
            {
                "X-APTRINSIC-API-KEY": google.gcp_get_secrets("gainsight_api_key", "1")
            }
        )
        df_users_updates = df_users_updates.set_index('email').reset_index()

        updates_processed = {}

        for _, row in df_users_updates.iterrows():
            status_code = update_gainsight_user(session, row.account_id, row.custom_attributes)
            if status_code == 404:
                updates_processed[row.email] = ''
                logging.debug(f'non-existing: {row.email} {row.account_id} {row.custom_attributes}')
            elif status_code == 204:
                updates_processed[row.email] = row.custom_attributes
                logging.debug(f'updated: {row.email} {row.account_id} {row.custom_attributes}')
            else:
                logging.error(f"failed to update: {row.email} {row.account_id} {row.custom_attributes}")
                continue

        df_contact_updates_processed = df_users_updates.join(
            pd.DataFrame.from_dict(updates_processed, orient='index'), on=["email"], how='outer'
        ).reset_index()[['email', 'diff_date', 'custom_attributes_farm_fingerprint']]
        df_contact_updates_processed['diff_date'] = pd.to_datetime(df_contact_updates_processed['diff_date'])
        df_contact_updates_processed.dropna(inplace=True)
        logging.debug(
            f"{len(df_contact_updates_processed)} rows to send to {self.destination_table}")
        bq_hook.insert_all(project_id=GCP_PROJECTS.MY_PROJECT.id, dataset_id=DATASET_ID,
                           table_id='user_attributes_processed', rows=df_contact_updates_processed.to_dict('records'),
                           ignore_unknown_values=True, fail_on_error=True)

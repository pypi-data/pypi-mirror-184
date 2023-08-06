import os
from datetime import timedelta
from typing import Dict, Any, Callable

from airflow.exceptions import AirflowSkipException
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from .utils import dest, dest_dict, sched, valid_label

DEFAULT_GCP_CONN_ID: str = "google_cloud_default"


def default_args_builder(email_env_var: str = 'AIRFLOW_FAILURE_EMAILS', ignore_env: bool = False,
                         gcp_conn_id: str = DEFAULT_GCP_CONN_ID) -> Dict[str, Any]:
    """Default args builder for an Airflow DAG.
    """
    airflow_failure_emails = os.getenv(email_env_var, 'your_email@example.com').split(',')
    return {
        "owner": "Airflow",
        'email_on_failure': True,
        'email_on_retry': False,
        'email': airflow_failure_emails,
        'retries': 1,
        'retry_delay': timedelta(seconds=90),
        'use_legacy_sql': False,
        'gcp_conn_id': gcp_conn_id,
        'on_failure_callback': None,
        'on_success_callback': None,
        'params': {
            'backfill': False,
            'ignore_env': ignore_env,
        }
    }


def user_defined_macros_builder(macros: Dict[str, Callable] = None) -> Dict[str, Callable]:
    if macros is None:
        macros = {
            'sched': sched,
            'dest': dest,
            'dest_dict': dest_dict,
            'valid_label': valid_label
        }
    return macros


class TriggerDagSkipBackfillRunOperator(TriggerDagRunOperator):
    """Skip TriggerDagRun when context.params.backfill is true.
    """
    def execute(self, context: Dict):
        if context.get('params', {}).get('backfill') is True:
            raise AirflowSkipException
        return super(TriggerDagSkipBackfillRunOperator, self).execute(context=context)

from abc import ABC
from typing import List, Dict, Type

from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryUpdateTableSchemaOperator, BigQueryUpdateTableOperator,
    BigQueryInsertJobOperator, BigQueryCheckOperator
)
from airflow.utils.task_group import TaskGroup
from airflow.models.baseoperator import BaseOperator

from .utils import dest_dict, dest


def make_table_desc_op(destination_table: str, description: str,
                       task_id: str = None, ignore_env: bool = False) -> BigQueryUpdateTableOperator:
    """Creates an `BigQueryUpdateTableOperator` in order to update table's description."""
    if task_id is None:
        task_id = f"description__{'.'.join(destination_table.split('.')[-2:])}"

    return BigQueryUpdateTableOperator(
        task_id=task_id,
        dataset_id=dest_dict(destination_table, ignore_env=ignore_env)['datasetId'],
        table_id=dest_dict(destination_table, ignore_env=ignore_env)['tableId'],
        table_resource={
            "description": description,
        },
    )


def make_table_schema_update_op(destination_table: str, schema: List[List[str]],
                                task_id: str = None, ignore_env: bool = False) -> BigQueryUpdateTableSchemaOperator:
    """Creates an `BigQueryUpdateTableSchemaOperator` in order to update schema's fields"""
    if task_id is None:
        task_id = f"schema__{'.'.join(destination_table.split('.')[-2:])}"

    return BigQueryUpdateTableSchemaOperator(
        task_id=task_id,
        dataset_id=dest_dict(destination_table, ignore_env=ignore_env)['datasetId'],
        table_id=dest_dict(destination_table, ignore_env=ignore_env)['tableId'],
        schema_fields_updates=[{'name': s[0], 'description': s[1]} for s in schema]
    )


def make_bq_job_labels(**kwargs) -> Dict[str, str]:
    """Create bigquery job labels using the current run, task and dag id.

    :param kwargs: extra labels.
    :return: a dictionary of labels.
    """
    return dict(
        task_instance_key_str="{{ valid_label(task_instance_key_str) }}",
        run_id="{{ valid_label(ti.run_id) }}", task_id="{{ valid_label(ti.task_id) }}",
        dag_id="{{ valid_label(ti.dag_id) }}", **kwargs
    )


def make_table_info_task_group(destination_table, description=None, schema=None, ignore_env=False):

    table_name = '.'.join(destination_table.split('.')[-2:])

    with TaskGroup(group_id=f"table_info_{table_name.replace('.','_')}") as table_info_task_group:

        # table description
        if description:
            description_op = make_table_desc_op(
                destination_table=destination_table,
                description=description,
                ignore_env=ignore_env
            )

        # schema description
        if schema:
            schema_op = make_table_schema_update_op(
                destination_table=destination_table,
                schema=schema,
                ignore_env=ignore_env
            )

    return table_info_task_group


def make_bq_insert_task_group(destination_table, params=None, ignore_env=False, write_desposition='WRITE_TRUNCATE',
                              validate=False, partition_field=None, sql_filename: str = None,
                              custom_task: Type[BaseOperator] = None, custom_task_op_kwargs: dict = {}):

    if params is None:
        params = {}

    table_name = '.'.join(destination_table.split('$')[0].split('.')[-2:])
    table_yyyymmdd = None
    if '$' in destination_table:
        table_yyyymmdd = destination_table.split('$')[-1]

    configuration = {
        "query": {
            "query": f"{{% include 'sql/{sql_filename or table_name}.sql' %}}",
            "useLegacySql": False,
            "destinationTable": {**dest_dict(destination_table, ignore_env=ignore_env)},
            "writeDisposition": write_desposition,
        },
        "labels": make_bq_job_labels()
    }

    if table_yyyymmdd or partition_field:
        configuration['query']['timePartitioning'] = {"type": "DAY", "require_partition_filter": True}
        if partition_field:
            configuration['query']['timePartitioning']['field'] = partition_field
        configuration['query']['schemaUpdateOptions'] = ["ALLOW_FIELD_ADDITION", "ALLOW_FIELD_RELAXATION"]

    with TaskGroup(group_id=table_name.replace('.', '_')) as bigquery_insert_task_group:

        bigquery_insert_job_op = custom_task(params=params, **custom_task_op_kwargs) if custom_task else \
            BigQueryInsertJobOperator(
                task_id=table_name,
                configuration=configuration,
                params=params
            )

        if validate:
            validate_op = BigQueryCheckOperator(
                task_id=f'validate__{table_name}',
                sql=f'sql/validate__{sql_filename or table_name}.sql',
                params={**params, 'table_id': dest(destination_table.split('$')[0], ignore_env=ignore_env)}
            )

            bigquery_insert_job_op >> validate_op

    return bigquery_insert_task_group


class MyBigQueryBaseOperator(BaseOperator, ABC):
    template_fields = ["sql_filepath", "query", "destination_table", "n_max"]
    template_fields_renderers = {"sql_filepath": "md", "query": "sql", "destination_table": "md", "n_max": "md"}

    def __init__(self, sql_filepath: str = None, n_max: int = 10000, **kwargs):
        super().__init__(**kwargs)
        self.sql_filepath = sql_filepath
        self.n_max = n_max
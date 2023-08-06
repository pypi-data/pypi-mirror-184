import collections
import datetime
import json
import logging
from typing import List

import pandas as pd
import numpy as np
from airflow.models.baseoperator import BaseOperator
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook

from .hooks import GainsightHook, Filter


class GainsightToBigQueryOperator(BaseOperator):
    template_fields = ('gainsight_conn_id', 'gcp_conn_id', 'action', 'parameter_id', 'page_size', 'page_number',
                       'filters', 'sort', 'max_results', 'project_id', 'dataset_id', 'table_id', 'ingestion_timestamp',
                       'ingestion_column_name', 'array_as_str', 'bool_as_str', 'all_fields_as_str',
                       'keep_nested_fields')

    def __init__(self, gainsight_conn_id: str = None, gcp_conn_id: str = None, action: str = None,
                 parameter_id: str = None, page_size: int = 100, page_number: int = 0,
                 filters: str = None, sort: List[str] = None, max_results: int = None,
                 project_id: str = None, dataset_id: str = None, table_id: str = None,
                 ingestion_timestamp: bool = False, ingestion_column_name: str = 'bq_ingested_at',
                 arrays_as_str: bool = True, bool_as_str: bool = True, all_fields_as_str: bool = False,
                 keep_nested_fields: List[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.gainsight_conn_id: str = gainsight_conn_id
        self.gcp_conn_id: str = gcp_conn_id
        self.action = action
        self.parameter_id = parameter_id
        self.page_size = page_size
        self.page_number = page_number
        self.filters = filters
        self.sort = sort
        self.max_results = max_results
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id
        self.ingestion_timestamp = ingestion_timestamp
        self.ingestion_column_name = ingestion_column_name
        self.array_as_str = arrays_as_str
        self.bool_as_str = bool_as_str
        self.all_fields_as_str = all_fields_as_str
        self.keep_nested_fields = keep_nested_fields or []

    @staticmethod
    def flatten(d, parent_key='', sep='_', ignore: List[str] = None):
        items = []
        ignore = ignore or []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, collections.MutableMapping) and k not in ignore:
                items.extend(GainsightToBigQueryOperator.flatten(v, new_key, sep=sep, ignore=ignore).items())
            else:
                items.append((new_key, v))
        return dict(items)

    @staticmethod
    def batch(lst, batch_size):
        """Yields batch of specified size
        """
        for i in range(0, len(lst), batch_size):
            yield lst[i: i + batch_size]

    def execute(self, context):
        gainsight_client = GainsightHook(gainsight_conn_id=self.gainsight_conn_id)
        bigquery_client = BigQueryHook(gcp_conn_id=self.gcp_conn_id)

        if not self.action:
            raise ValueError('You have to provide an action')

        if not self.action.startswith('get'):
            raise ValueError('Only get actions are supported by this operator')

        try:
            clb = getattr(gainsight_client, self.action)
        except AttributeError:
            raise ValueError(f'`{self.action}` is not supported')

        args = (self.parameter_id,) if self.parameter_id else tuple()

        kwargs = {
            'page_size': self.page_size, 'page_number': self.page_number, 'sort': self.sort
        }
        if isinstance(self.filters, str) and self.filters.strip():
            kwargs.update(filters=[Filter(raw=self.filters.strip())])

        if self.max_results:
            kwargs['max_results'] = self.max_results
        logging.info(f'Gainsight args: {args}')
        logging.info(f'Gainsight kwargs: {kwargs}')
        data = [self.flatten(item, ignore=self.keep_nested_fields) for item in clb(*args, **kwargs)]

        for i in range(len(data)):
            for k, v in data[i].items():
                if isinstance(v, int) and len(str(v)) == 13:
                    data[i][k] = datetime.datetime.fromtimestamp(v / 1000, tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                if k == 'createDate' and v == 0:
                    data[i][k] = None
                elif isinstance(v, list):
                    data[i][k] = str(v) if self.array_as_str or self.all_fields_as_str else json.dumps(v)
                elif isinstance(v, bool):
                    data[i][k] = str(v) if self.bool_as_str or self.all_fields_as_str else json.dumps(v)
                elif isinstance(v, dict) and k in self.keep_nested_fields:
                    data[i][k] = json.dumps(v)
            if self.ingestion_timestamp:
                data[i][self.ingestion_column_name] = context['ts']
            data[i].pop('', None)

        complete_row = {k: v for i in data for k, v in i.items() if v is not None}
        logging.info(complete_row)

        if data:
            for batch_data in self.batch(data, 1000):
                bigquery_client.insert_all(
                    project_id=self.project_id, dataset_id=self.dataset_id, table_id=f'{self.table_id}',
                    rows=batch_data, ignore_unknown_values=False, skip_invalid_rows=False, fail_on_error=True
                )
        logging.info(f'Number of inserted rows: {len(data)}')


class GainsightPandasToBigQueryOperator(BaseOperator):
    template_fields = ('gainsight_conn_id', 'gcp_conn_id', 'action', 'parameter_id', 'page_size', 'page_number',
                       'sort', 'max_results', 'project_id', 'dataset_id', 'table_id', 'ingestion_timestamp',
                       'ingestion_column_name', 'array_as_str', 'bool_as_str', 'all_fields_as_str', 'if_exists')

    def __init__(self, gainsight_conn_id: str = None, gcp_conn_id: str = None, action: str = None,
                 parameter_id: str = None, page_size: int = 100, page_number: int = 1, filters: List[Filter] = None,
                 sort: List[str] = None, max_results: int = None, project_id: str = None, dataset_id: str = None,
                 table_id: str = None, ingestion_timestamp: bool = False, ingestion_column_name: str = 'bq_ingested_at',
                 arrays_as_str: bool = True, bool_as_str: bool = True, all_fields_as_str: bool = False,
                 if_exists: str = 'append', **kwargs):
        super().__init__(**kwargs)
        self.gainsight_conn_id: str = gainsight_conn_id
        self.gcp_conn_id: str = gcp_conn_id
        self.action = action
        self.parameter_id = parameter_id
        self.page_size = page_size
        self.page_number = page_number
        self.filters = filters
        self.sort = sort
        self.max_results = max_results
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id
        self.ingestion_timestamp = ingestion_timestamp
        self.ingestion_column_name = ingestion_column_name
        self.array_as_str = arrays_as_str
        self.bool_as_str = bool_as_str
        self.all_fields_as_str = all_fields_as_str
        self.if_exists = if_exists

    @staticmethod
    def flatten(d, parent_key='', sep='_'):
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, collections.MutableMapping):
                items.extend(GainsightToBigQueryOperator.flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def execute(self, context):
        gainsight_client = GainsightHook(gainsight_conn_id=self.gainsight_conn_id)
        bigquery_client = BigQueryHook(gcp_conn_id=self.gcp_conn_id).get_client()

        if not self.action:
            raise ValueError('You have to provide an action')

        if not self.action.startswith('get'):
            raise ValueError('Only get actions are supported by this operator')

        try:
            clb = getattr(gainsight_client, self.action)
        except AttributeError:
            raise ValueError(f'`{self.action}` is not supported')

        args = (self.parameter_id,) if self.parameter_id else tuple()
        kwargs = {
            'page_size': self.page_size, 'page_number': self.page_number, 'filters': self.filters, 'sort': self.sort
        }
        if self.max_results:
            kwargs['max_results'] = self.max_results
        data = [self.flatten(item) for item in clb(*args, **kwargs)]

        for i in range(len(data)):
            for k, v in data[i].items():
                if isinstance(v, list) and (self.array_as_str or self.all_fields_as_str):
                    data[i][k] = str(v)
                elif isinstance(v, bool) and (self.bool_as_str or self.all_fields_as_str):
                    data[i][k] = str(v)

        df = pd.DataFrame.from_records(data)

        if self.ingestion_timestamp:
            df[self.ingestion_column_name] = context['ts']

        if self.all_fields_as_str:
            df = df.astype(str)

        df.replace(['N/A', np.nan], value=None, inplace=True)

        print(dir(bigquery_client))

        df.to_gbq(
            destination_table=f"{self.dataset_id}.{self.table_id}",
            project_id=self.project_id,
            if_exists=self.if_exists,
            credentials=bigquery_client._credentials
        )

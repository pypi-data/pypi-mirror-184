import warnings
from enum import Enum
from typing import Generator
from typing import Type, Any, List

import requests
from airflow.hooks.base import BaseHook
from requests.adapters import HTTPAdapter, Retry

ACTIONS = {
    'get': 'GET',
    'update': 'PUT',
    'delete': 'DELETE',
    'create': 'POST',
    'set': 'PUT',
    'export': 'GET',
    'import': 'POST',
    'request': 'POST'
}
RESOURCES = {
    'accounts': {
        'actions': ('get', 'create', 'update', 'delete'),
        'endpoint': '/accounts',
        'allow_parameter_id': True,
    },
    'admin/model/user/attributes': {
        'actions': ('get',),
        'endpoint': '/admin/model/user/attributes',
        'single_result': True
    },
    'admin/model/account/attributes': {
        'actions': ('get',),
        'endpoint': '/admin/model/account/attributes',
        'single_result': True
    },
    'admin/subscription': {
        'actions': ('get',),
        'endpoint': '/admin/subscription',
        'single_result': True
    },
    'engagement': {
        'actions': ('get',),
        'allow_parameter_id': True,
        'endpoint': '/engagement',
        'result_key': 'engagements'
    },
    'engagement/env': {
        'actions': ('set',),
        'endpoint': '/engagement/env'
    },
    'engagement/envs': {
        'actions': ('set',),
        'endpoint': '/engagement/envs'
    },
    'engagement/extended': {
        'actions': ('get',),
        'endpoint': '/engagement/extended',
        'result_key': 'engagements'
    },
    # 'engagement/metadata/survey': {
    #     'actions': ('get',),
    #     'endpoint': '/engagement/metadata/survey',
    #     'allow_parameter_id': True
    # },
    'engagement/state': {
        'actions': ('set',),
        'endpoint': '/engagement/state'
    },
    'events/custom': {
        'actions': ('create', 'get'),
        'endpoint': '/events/custom',
        'result_key': 'customEvents'
    },
    'events/email': {
        'actions': ('get',),
        'endpoint': '/events/email',
    },
    'events/engagementView': {
        'actions': ('get',),
        'endpoint': '/events/engagementView'
    },
    'events/feature_match': {
        'actions': ('get',),
        'endpoint': '/events/feature_match',
        'result_key': 'featureMatchEvents'
    },
    'events/formSubmit': {
        'actions': ('get',),
        'endpoint': '/events/formSubmit'
    },
    'events/identify': {
        'actions': ('get',),
        'endpoint': '/events/identify',
        'result_key': 'identifyEvents'
    },
    'events/lead': {
        'actions': ('get',),
        'endpoint': '/events/lead'
    },
    'events/pageView': {
        'actions': ('get',),
        'endpoint': '/events/pageView'
    },
    'events/segment_match': {
        'actions': ('get',),
        'endpoint': '/events/segment_match',
        'result_key': 'featureMatchEvents'
    },
    'events/session': {
        'actions': ('get',),
        'endpoint': '/events/session',
        'result_key': 'sessionInitializedEvents'
    },
    'feature': {
        'actions': ('get', 'update'),
        'endpoint': '/feature',
        'allow_parameter_id': True,
        'result_key': 'features'
    },
    'feature/backfill': {
        'actions': ('request',),
        'allow_parameter_id': True,
        'endpoint': '/feature/backfill'
    },
    # 'localization/export': {
    #     'actions': ('export',),
    #     'endpoint': '/localization/export'
    # },
    # 'localization/import': {
    #     'actions': ('import',),
    #     'endpoint': '/localization/import'
    # },
    'segment': {
        'actions': ('get',),
        'endpoint': '/segment',
        'allow_parameter_id': True,
        'result_key': 'segments'
    },
    'survey/responses': {
        'actions': ('get',),
        'endpoint': '/survey/responses'
    },
    # 'user/preferences': {
    #     'actions': ('get', 'update'),
    #     'allow_parameter_id': True,
    #     'endpoint': '/user/preferences'
    # },
    'users': {
        'actions': ('get', 'create', 'update', 'delete'),
        'endpoint': '/users',
        'allow_parameter_id': True
    },
    'users/denylist': {
        'actions': ('get', 'update'),
        'allow_parameter_id': True,
        'endpoint': '/users/denylist'
    },
}


class Operator(Enum):
    """Gainsight-supported operators"""
    EXACT_MATCH = '=='
    NOT_EQUAL = '!='
    LT = '<'
    LTE = '<='
    GT = '>'
    GTE = '>='
    STRING_MATCH = '~'
    STRING_NOT_MATCH = '!~'


class Filter:
    """This class represents a filter"""
    def __init__(self, field: str = None, operator: Type[Operator] = None, value: Any = None, raw: str = None):
        self.field = field
        self.operator = operator.value if operator is not None else None
        self.value = value
        self.raw = raw

    def get(self) -> str:
        return self.raw or f'{self.field}{self.operator}{self.value}'


class _GainsightRequest:
    """The low-level gainsight request class."""
    def __init__(self, session: requests.Session, action: str, url: str, allow_parameter_id: bool = False,
                 result_key: str = None, single_result: bool = False, resource_id: str = None):
        self.session = session
        self.action = action
        self.method = ACTIONS.get(action, action.upper())
        self.url = url
        self.allow_parameter_id = allow_parameter_id
        self.resource_id = resource_id
        self.result_key = result_key or resource_id
        self.single_result = single_result

    def __call__(self, *args, page_size: int = 100, page_number: int = 1, filters: List[Filter] = None,
                 sort: List[str] = None, body: dict = None, max_results: int = None, **kwargs):
        params = {}
        if args:
            if not self.allow_parameter_id:
                raise ValueError(f'Parameter id is not supported for endpoint: {self.url}.')
            url = '/'.join((self.url.strip('/'), args[0].strip('/')))
            if max_results:
                warnings.warn('max_results is ignored when parameter id is provided')
        else:
            if self.action in ('update', 'delete'):
                raise ValueError('You have to provide a parameter id.')
            url = self.url[:]
            params.update(pageSize=page_size, pageNumber=page_number)

        if filters:
            params.update(filter=';'.join(filter_.get() for filter_ in filters))
        if sort:
            if args:
                warnings.warn('sorting is ignored when parameter id is provided')
            else:
                params.update(sort=f'-{";".join(sort)}')

        results = []
        while True:  # iterate based on scrollId
            r = self.session.request(self.method, url, json=body, params=params)
            try:
                resp = r.json()
            except Exception as e:
                raise ValueError(e)
            if 'externalapierror' in resp:
                raise ValueError(resp['externalapierror'])
            if args or self.single_result or self.action in ('update', 'delete', 'request'):
                return resp

            if self.result_key not in resp and 'results' not in resp:
                raise ValueError(f'Cannot extract {self.result_key} from {resp.keys()}')

            current_results = resp['results'] if 'results' in resp else resp[self.result_key]
            results.extend(current_results)
            will_break = True
            if resp.get('scrollId'):
                params.update(scrollId=resp['scrollId'])
                will_break = False
            if resp.get('isLastPage') is False:
                params.update(pageNumber=params['pageNumber'] + 1)
                will_break = False
            if max_results and len(results) >= max_results:
                return results[:max_results]
            if will_break or not current_results:
                break

        return results


class GainsightHook(BaseHook):
    default_conn_name = 'gainsight_default'
    URL_BASE: str

    def __init__(self, gainsight_conn_id: str = default_conn_name) -> None:
        super().__init__()
        self.gainsight_conn_id = gainsight_conn_id or self.default_conn_name
        self.session = self._init_session()
        for resource_id, details in RESOURCES.items():
            endpoint = details.pop("endpoint")
            for action in details.pop('actions', []):
                method_name = f'{self._slugify(action)}_{self._slugify(resource_id)}'
                setattr(
                    self,
                    method_name,
                    _GainsightRequest(
                        self.session, action, f'{self.URL_BASE}{endpoint}', resource_id=resource_id, **details
                    )
                )

    def __dir__(self):
        return dir(type(self)) + list(self.__dict__.keys()) + list(self._iter_method_names())

    @staticmethod
    def _slugify(input_txt: str) -> str:
        return input_txt.lower().replace('/', '_')

    def _init_session(self, retry_total: int = 3, retry_backoff_factor: int = 20) -> requests.Session:
        # TODO: allow high level api to adjust retry_total and retry_backoff_factor
        conn = self.get_connection(self.gainsight_conn_id)
        self.URL_BASE = conn.host.strip('/')
        adapter = HTTPAdapter(
            max_retries=Retry(
                total=retry_total,
                backoff_factor=retry_backoff_factor
            )
        )
        session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        session.headers.update(
            {
                "X-APTRINSIC-API-KEY": conn.password
            }
        )
        return session

    def _iter_method_names(self) -> Generator:
        for k, v in RESOURCES.items():
            for action in v.get('actions', []):
                yield f'{self._slugify(action)}_{self._slugify(k)}'

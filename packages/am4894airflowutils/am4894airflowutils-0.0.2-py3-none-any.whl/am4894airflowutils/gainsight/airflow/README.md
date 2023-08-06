# Gainsight Provider

This folder aims to implement the gainsight provider.

## Gainsight Hook

Initially, a basic gainsight hook has been implemented. This hook support any kind of supported request on 
every endpoint. The methods are dynamically defined using a static dictionary (`airflow.hooks.RESOURCES`)

The default connection name is `gainsight_default`, this connection can be ssh for now.

### Usage example

```shell
$ cd airflow
$ export AIRFLOW_CONN_GAINSIGHT_DEFAULT=ssh://foo:<API_KEY>@https%3A%2F%2Fapi.aptrinsic.com%2Fv1%2F
```

#### Get by id
```python
>>> from am4894airflowutils.gainsight.airflow.hooks import GainsightHook
>>> from am4894airflowutils.gainsight.airflow.utils import Filter, Operator
>>> gainsight_client = GainsightHook()
>>> filters = [Filter('name', Operator.EXACT_MATCH, 'foo.com')]
>>> gainsight_client.get_accounts('1234')
{'id': '1234',
 'name': 'foo.com',
 'trackedSubscriptionId': '',
 'sfdcId': '',
 'lastSeenDate': 1600791393136,
 'dunsNumber': '',
 'industry': '',
 'numberOfEmployees': 0,
 'sicCode': '',
 'website': '',
 'naicsCode': '',
 'plan': '',
 'location': {'countryName': '',
  'countryCode': '',
  'stateName': '',
  'stateCode': '',
  'city': '',
  'street': '',
  'postalCode': '',
  'continent': '',
  'regionName': '',
  'timeZone': '',
  'coordinates': {'latitude': 0.0, 'longitude': 0.0}},
 'numberOfUsers': 1,
 'propertyKeys': ['AP-XXX-2-1'],
 'createDate': 1600724133259,
 'lastModifiedDate': 1600791393136,
 'customAttributes': None,
 'parentGroupId': ''}
```

#### Filtering and sorting
```python
>>> from am4894airflowutils.gainsight.airflow.hooks import GainsightHook
>>> from am4894airflowutils.gainsight.airflow.utils import Filter, Operator
>>> gainsight_client = GainsightHook()
>>> filters = [Filter('name', Operator.EXACT_MATCH, 'foo.com')]
>>> gainsight_client.get_accounts(filters=filters, sort=['lastModifiedDate'])
[{'id': '1234',
  'name': 'foo.com',
  'trackedSubscriptionId': '',
  'sfdcId': '',
  'lastSeenDate': 1600791393136,
  'dunsNumber': '',
  'industry': '',
  'numberOfEmployees': 0,
  'sicCode': '',
  'website': '',
  'naicsCode': '',
  'plan': '',
  'location': {'countryName': '',
   'countryCode': '',
   'stateName': '',
   'stateCode': '',
   'city': '',
   'street': '',
   'postalCode': '',
   'continent': '',
   'regionName': '',
   'timeZone': '',
   'coordinates': {'latitude': 0.0, 'longitude': 0.0}},
  'numberOfUsers': 1,
  'propertyKeys': ['AP-XXX-2-1'],
  'createDate': 1600724133259,
  'lastModifiedDate': 1600791393136,
  'customAttributes': None,
  'parentGroupId': ''}]
```
# DependenciesApi

## PureCloudPlatformClientV2.DependenciesApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_dependencies_type_entity_type_id_entity_id_connections_requiredby**](#get_dependencies_type_entity_type_id_entity_id_connections_requiredby) | Get entities that require the given entity|
|[**get_dependencies_type_entity_type_id_entity_id_connections_requiredbycounts**](#get_dependencies_type_entity_type_id_entity_id_connections_requiredbycounts) | An estimated count of entities that depend on this entity, including indirect dependencies.|
|[**get_dependencies_type_entity_type_id_entity_id_connections_requires**](#get_dependencies_type_entity_type_id_entity_id_connections_requires) | Get entities that the given entity requires|



## get_dependencies_type_entity_type_id_entity_id_connections_requiredby

> [**DependencyEntityListing**](DependencyEntityListing) get_dependencies_type_entity_type_id_entity_id_connections_requiredby(entity_type, entity_id, page_size=page_size, before_source_type=before_source_type, before_source_id=before_source_id, after_source_type=after_source_type, after_source_id=after_source_id)


Get entities that require the given entity

Wraps GET /api/v2/dependencies/type/{entityType}/id/{entityId}/connections/requiredby 

Requires ANY permissions: 

* dependencies:dependency:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.DependenciesApi()
entity_type = 'entity_type_example' # str | Entity type
entity_id = 'entity_id_example' # str | Entity ID
page_size = ''25'' # str | Page size (max 100) (optional) (default to '25')
before_source_type = 'before_source_type_example' # str | Cursor for previous page (optional)
before_source_id = 'before_source_id_example' # str | Cursor for previous page (optional)
after_source_type = 'after_source_type_example' # str | Cursor for next page (optional)
after_source_id = 'after_source_id_example' # str | Cursor for next page (optional)

try:
    # Get entities that require the given entity
    api_response = api_instance.get_dependencies_type_entity_type_id_entity_id_connections_requiredby(entity_type, entity_id, page_size=page_size, before_source_type=before_source_type, before_source_id=before_source_id, after_source_type=after_source_type, after_source_id=after_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DependenciesApi->get_dependencies_type_entity_type_id_entity_id_connections_requiredby: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str**| Entity type | <br />**Values**: Integration, DataAction, Credential |
| **entity_id** | **str**| Entity ID |  |
| **page_size** | **str**| Page size (max 100) | [optional] [default to &#39;25&#39;] |
| **before_source_type** | **str**| Cursor for previous page | [optional]  |
| **before_source_id** | **str**| Cursor for previous page | [optional]  |
| **after_source_type** | **str**| Cursor for next page | [optional]  |
| **after_source_id** | **str**| Cursor for next page | [optional]  |

### Return type

[**DependencyEntityListing**](DependencyEntityListing)


## get_dependencies_type_entity_type_id_entity_id_connections_requiredbycounts

> [**DependencyCount**](DependencyCount) get_dependencies_type_entity_type_id_entity_id_connections_requiredbycounts(entity_type, entity_id)


An estimated count of entities that depend on this entity, including indirect dependencies.

Wraps GET /api/v2/dependencies/type/{entityType}/id/{entityId}/connections/requiredbycounts 

Requires ANY permissions: 

* dependencies:dependency:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.DependenciesApi()
entity_type = 'entity_type_example' # str | Entity type
entity_id = 'entity_id_example' # str | Entity ID

try:
    # An estimated count of entities that depend on this entity, including indirect dependencies.
    api_response = api_instance.get_dependencies_type_entity_type_id_entity_id_connections_requiredbycounts(entity_type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DependenciesApi->get_dependencies_type_entity_type_id_entity_id_connections_requiredbycounts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str**| Entity type | <br />**Values**: Integration, DataAction, Credential |
| **entity_id** | **str**| Entity ID |  |

### Return type

[**DependencyCount**](DependencyCount)


## get_dependencies_type_entity_type_id_entity_id_connections_requires

> [**DependencyEntityListing**](DependencyEntityListing) get_dependencies_type_entity_type_id_entity_id_connections_requires(entity_type, entity_id, page_size=page_size, before_source_type=before_source_type, before_source_id=before_source_id, after_source_type=after_source_type, after_source_id=after_source_id)


Get entities that the given entity requires

Wraps GET /api/v2/dependencies/type/{entityType}/id/{entityId}/connections/requires 

Requires ANY permissions: 

* dependencies:dependency:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.DependenciesApi()
entity_type = 'entity_type_example' # str | Entity type
entity_id = 'entity_id_example' # str | Entity ID
page_size = ''25'' # str | Page size (max 100) (optional) (default to '25')
before_source_type = 'before_source_type_example' # str | Cursor for previous page (optional)
before_source_id = 'before_source_id_example' # str | Cursor for previous page (optional)
after_source_type = 'after_source_type_example' # str | Cursor for next page (optional)
after_source_id = 'after_source_id_example' # str | Cursor for next page (optional)

try:
    # Get entities that the given entity requires
    api_response = api_instance.get_dependencies_type_entity_type_id_entity_id_connections_requires(entity_type, entity_id, page_size=page_size, before_source_type=before_source_type, before_source_id=before_source_id, after_source_type=after_source_type, after_source_id=after_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DependenciesApi->get_dependencies_type_entity_type_id_entity_id_connections_requires: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str**| Entity type | <br />**Values**: Integration, DataAction, Credential |
| **entity_id** | **str**| Entity ID |  |
| **page_size** | **str**| Page size (max 100) | [optional] [default to &#39;25&#39;] |
| **before_source_type** | **str**| Cursor for previous page | [optional]  |
| **before_source_id** | **str**| Cursor for previous page | [optional]  |
| **after_source_type** | **str**| Cursor for next page | [optional]  |
| **after_source_id** | **str**| Cursor for next page | [optional]  |

### Return type

[**DependencyEntityListing**](DependencyEntityListing)


_PureCloudPlatformClientV2 265.0.0_

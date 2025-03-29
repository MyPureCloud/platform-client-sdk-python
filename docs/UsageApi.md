# UsageApi

## PureCloudPlatformClientV2.UsageApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_oauth_client_usage_query_result**](#get_oauth_client_usage_query_result) | Get the results of a usage query|
|[**get_oauth_client_usage_summary**](#get_oauth_client_usage_summary) | Get a summary of OAuth client API usage|
|[**get_usage_query_execution_id_results**](#get_usage_query_execution_id_results) | Get the results of a usage query|
|[**get_usage_simplesearch_execution_id_results**](#get_usage_simplesearch_execution_id_results) | Get the results of a usage search. Number of records to be returned is limited to 20,000 results.|
|[**post_oauth_client_usage_query**](#post_oauth_client_usage_query) | Query for OAuth client API usage|
|[**post_usage_query**](#post_usage_query) | Query organization API Usage - |
|[**post_usage_simplesearch**](#post_usage_simplesearch) | Search organization API Usage|



## get_oauth_client_usage_query_result

> [**ApiUsageQueryResult**](ApiUsageQueryResult) get_oauth_client_usage_query_result(execution_id, client_id)


Get the results of a usage query

Wraps GET /api/v2/oauth/clients/{clientId}/usage/query/results/{executionId} 

Requires ANY permissions: 

* oauth:client:view
* usage:client:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsageApi()
execution_id = 'execution_id_example' # str | ID of the query execution
client_id = 'client_id_example' # str | Client ID

try:
    # Get the results of a usage query
    api_response = api_instance.get_oauth_client_usage_query_result(execution_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_oauth_client_usage_query_result: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **execution_id** | **str**| ID of the query execution |  |
| **client_id** | **str**| Client ID |  |

### Return type

[**ApiUsageQueryResult**](ApiUsageQueryResult)


## get_oauth_client_usage_summary

> [**UsageExecutionResult**](UsageExecutionResult) get_oauth_client_usage_summary(client_id, days=days)


Get a summary of OAuth client API usage

After calling this method, you will then need to poll for the query results based on the returned execution Id

Wraps GET /api/v2/oauth/clients/{clientId}/usage/summary 

Requires ANY permissions: 

* oauth:client:view
* usage:client:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsageApi()
client_id = 'client_id_example' # str | Client ID
days = ''7'' # str | Previous number of days to query (optional) (default to '7')

try:
    # Get a summary of OAuth client API usage
    api_response = api_instance.get_oauth_client_usage_summary(client_id, days=days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_oauth_client_usage_summary: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client_id** | **str**| Client ID |  |
| **days** | **str**| Previous number of days to query | [optional] [default to &#39;7&#39;] |

### Return type

[**UsageExecutionResult**](UsageExecutionResult)


## get_usage_query_execution_id_results

> [**ApiUsageQueryResult**](ApiUsageQueryResult) get_usage_query_execution_id_results(execution_id)


Get the results of a usage query

Wraps GET /api/v2/usage/query/{executionId}/results 

Requires ANY permissions: 

* oauth:client:view
* usage:organization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsageApi()
execution_id = 'execution_id_example' # str | ID of the query execution

try:
    # Get the results of a usage query
    api_response = api_instance.get_usage_query_execution_id_results(execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_usage_query_execution_id_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **execution_id** | **str**| ID of the query execution |  |

### Return type

[**ApiUsageQueryResult**](ApiUsageQueryResult)


## get_usage_simplesearch_execution_id_results

> [**ApiUsageQueryResult**](ApiUsageQueryResult) get_usage_simplesearch_execution_id_results(execution_id, after=after, page_size=page_size)


Get the results of a usage search. Number of records to be returned is limited to 20,000 results.

Wraps GET /api/v2/usage/simplesearch/{executionId}/results 

Requires ANY permissions: 

* oauth:client:view
* usage:simpleSearch:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsageApi()
execution_id = 'execution_id_example' # str | ID of the search execution
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned (optional)
page_size = 56 # int | The max number of entities to be returned per request. Maximum page size of 1000 (optional)

try:
    # Get the results of a usage search. Number of records to be returned is limited to 20,000 results.
    api_response = api_instance.get_usage_simplesearch_execution_id_results(execution_id, after=after, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_usage_simplesearch_execution_id_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **execution_id** | **str**| ID of the search execution |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned | [optional]  |
| **page_size** | **int**| The max number of entities to be returned per request. Maximum page size of 1000 | [optional]  |

### Return type

[**ApiUsageQueryResult**](ApiUsageQueryResult)


## post_oauth_client_usage_query

> [**UsageExecutionResult**](UsageExecutionResult) post_oauth_client_usage_query(client_id, body)


Query for OAuth client API usage

After calling this method, you will then need to poll for the query results based on the returned execution Id

Wraps POST /api/v2/oauth/clients/{clientId}/usage/query 

Requires ANY permissions: 

* oauth:client:view
* usage:client:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsageApi()
client_id = 'client_id_example' # str | Client ID
body = PureCloudPlatformClientV2.ApiUsageClientQuery() # ApiUsageClientQuery | Query

try:
    # Query for OAuth client API usage
    api_response = api_instance.post_oauth_client_usage_query(client_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->post_oauth_client_usage_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client_id** | **str**| Client ID |  |
| **body** | [**ApiUsageClientQuery**](ApiUsageClientQuery)| Query |  |

### Return type

[**UsageExecutionResult**](UsageExecutionResult)


## post_usage_query

> [**UsageExecutionResult**](UsageExecutionResult) post_usage_query(body)


Query organization API Usage - 

After calling this method, you will then need to poll for the query results based on the returned execution Id

Wraps POST /api/v2/usage/query 

Requires ANY permissions: 

* oauth:client:view
* usage:organization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsageApi()
body = PureCloudPlatformClientV2.ApiUsageOrganizationQuery() # ApiUsageOrganizationQuery | Query

try:
    # Query organization API Usage - 
    api_response = api_instance.post_usage_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->post_usage_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ApiUsageOrganizationQuery**](ApiUsageOrganizationQuery)| Query |  |

### Return type

[**UsageExecutionResult**](UsageExecutionResult)


## post_usage_simplesearch

> [**UsageExecutionResult**](UsageExecutionResult) post_usage_simplesearch(body)


Search organization API Usage

After calling this method, you will then need to poll for the query results based on the returned execution Id. The number of records is limited to 20,000 results

Wraps POST /api/v2/usage/simplesearch 

Requires ANY permissions: 

* oauth:client:view
* usage:simpleSearch:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsageApi()
body = PureCloudPlatformClientV2.ApiUsageSimpleSearch() # ApiUsageSimpleSearch | SimpleSearch

try:
    # Search organization API Usage
    api_response = api_instance.post_usage_simplesearch(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->post_usage_simplesearch: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ApiUsageSimpleSearch**](ApiUsageSimpleSearch)| SimpleSearch |  |

### Return type

[**UsageExecutionResult**](UsageExecutionResult)


_PureCloudPlatformClientV2 224.1.0_

# AuditApi

## PureCloudPlatformClientV2.AuditApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_audits_query_realtime_servicemapping**](#get_audits_query_realtime_servicemapping) | Get service mapping information used in realtime audits.|
|[**get_audits_query_servicemapping**](#get_audits_query_servicemapping) | Get service mapping information used in audits.|
|[**get_audits_query_transaction_id**](#get_audits_query_transaction_id) | Get status of audit query execution|
|[**get_audits_query_transaction_id_results**](#get_audits_query_transaction_id_results) | Get results of audit query|
|[**post_audits_query**](#post_audits_query) | Create audit query execution|
|[**post_audits_query_realtime**](#post_audits_query_realtime) | This endpoint will only retrieve 14 days worth of audits for certain services. Please use /query to get a full list and older audits.|
|[**post_audits_query_realtime_related**](#post_audits_query_realtime_related) | Often a single action results in multiple audits. The endpoint retrieves all audits created by the same action as the given audit id.|



## get_audits_query_realtime_servicemapping

> [**AuditQueryServiceMapping**](AuditQueryServiceMapping) get_audits_query_realtime_servicemapping()


Get service mapping information used in realtime audits.

Wraps GET /api/v2/audits/query/realtime/servicemapping 

Requires ALL permissions: 

* audits:audit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuditApi()

try:
    # Get service mapping information used in realtime audits.
    api_response = api_instance.get_audits_query_realtime_servicemapping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_audits_query_realtime_servicemapping: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**AuditQueryServiceMapping**](AuditQueryServiceMapping)


## get_audits_query_servicemapping

> [**AuditQueryServiceMapping**](AuditQueryServiceMapping) get_audits_query_servicemapping()


Get service mapping information used in audits.

Wraps GET /api/v2/audits/query/servicemapping 

Requires ALL permissions: 

* audits:audit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuditApi()

try:
    # Get service mapping information used in audits.
    api_response = api_instance.get_audits_query_servicemapping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_audits_query_servicemapping: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**AuditQueryServiceMapping**](AuditQueryServiceMapping)


## get_audits_query_transaction_id

> [**AuditQueryExecutionStatusResponse**](AuditQueryExecutionStatusResponse) get_audits_query_transaction_id(transaction_id)


Get status of audit query execution

Wraps GET /api/v2/audits/query/{transactionId} 

Requires ALL permissions: 

* audits:audit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuditApi()
transaction_id = 'transaction_id_example' # str | Transaction ID

try:
    # Get status of audit query execution
    api_response = api_instance.get_audits_query_transaction_id(transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_audits_query_transaction_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **transaction_id** | **str**| Transaction ID |  |

### Return type

[**AuditQueryExecutionStatusResponse**](AuditQueryExecutionStatusResponse)


## get_audits_query_transaction_id_results

> [**AuditQueryExecutionResultsResponse**](AuditQueryExecutionResultsResponse) get_audits_query_transaction_id_results(transaction_id, cursor=cursor, page_size=page_size, expand=expand, allow_redirect=allow_redirect)


Get results of audit query

Wraps GET /api/v2/audits/query/{transactionId}/results 

Requires ALL permissions: 

* audits:audit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuditApi()
transaction_id = 'transaction_id_example' # str | Transaction ID
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page) (optional)
page_size = 25 # int | Indicates maximum number of results in response. Default page size is 25 results. The maximum page size is 500. (optional) (default to 25)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
allow_redirect = True # bool | Result sets with large amounts of data will respond with a download url (optional)

try:
    # Get results of audit query
    api_response = api_instance.get_audits_query_transaction_id_results(transaction_id, cursor=cursor, page_size=page_size, expand=expand, allow_redirect=allow_redirect)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_audits_query_transaction_id_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **transaction_id** | **str**| Transaction ID |  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page) | [optional]  |
| **page_size** | **int**| Indicates maximum number of results in response. Default page size is 25 results. The maximum page size is 500. | [optional] [default to 25] |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: user |
| **allow_redirect** | **bool**| Result sets with large amounts of data will respond with a download url | [optional]  |

### Return type

[**AuditQueryExecutionResultsResponse**](AuditQueryExecutionResultsResponse)


## post_audits_query

> [**AuditQueryExecutionStatusResponse**](AuditQueryExecutionStatusResponse) post_audits_query(body)


Create audit query execution

Use /api/v2/audits/query/servicemapping endpoint for a list of valid values

Wraps POST /api/v2/audits/query 

Requires ALL permissions: 

* audits:audit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuditApi()
body = PureCloudPlatformClientV2.AuditQueryRequest() # AuditQueryRequest | query

try:
    # Create audit query execution
    api_response = api_instance.post_audits_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->post_audits_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AuditQueryRequest**](AuditQueryRequest)| query |  |

### Return type

[**AuditQueryExecutionStatusResponse**](AuditQueryExecutionStatusResponse)


## post_audits_query_realtime

> [**AuditRealtimeQueryResultsResponse**](AuditRealtimeQueryResultsResponse) post_audits_query_realtime(body, expand=expand)


This endpoint will only retrieve 14 days worth of audits for certain services. Please use /query to get a full list and older audits.

Use /api/v2/audits/query/realtime/servicemapping endpoint for a list of valid values

Wraps POST /api/v2/audits/query/realtime 

Requires ALL permissions: 

* audits:audit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuditApi()
body = PureCloudPlatformClientV2.AuditRealtimeQueryRequest() # AuditRealtimeQueryRequest | query
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # This endpoint will only retrieve 14 days worth of audits for certain services. Please use /query to get a full list and older audits.
    api_response = api_instance.post_audits_query_realtime(body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->post_audits_query_realtime: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AuditRealtimeQueryRequest**](AuditRealtimeQueryRequest)| query |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: user |

### Return type

[**AuditRealtimeQueryResultsResponse**](AuditRealtimeQueryResultsResponse)


## post_audits_query_realtime_related

> [**AuditRealtimeRelatedResultsResponse**](AuditRealtimeRelatedResultsResponse) post_audits_query_realtime_related(body, expand=expand)


Often a single action results in multiple audits. The endpoint retrieves all audits created by the same action as the given audit id.

Wraps POST /api/v2/audits/query/realtime/related 

Requires ALL permissions: 

* audits:audit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuditApi()
body = PureCloudPlatformClientV2.AuditRealtimeRelatedRequest() # AuditRealtimeRelatedRequest | query
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Often a single action results in multiple audits. The endpoint retrieves all audits created by the same action as the given audit id.
    api_response = api_instance.post_audits_query_realtime_related(body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->post_audits_query_realtime_related: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AuditRealtimeRelatedRequest**](AuditRealtimeRelatedRequest)| query |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: user |

### Return type

[**AuditRealtimeRelatedResultsResponse**](AuditRealtimeRelatedResultsResponse)


_PureCloudPlatformClientV2 242.0.0_

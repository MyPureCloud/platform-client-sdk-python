---
title: AuditApi
---

## PureCloudPlatformClientV2.AuditApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_audits_query_realtime_servicemapping**](AuditApi.html#get_audits_query_realtime_servicemapping) | Get service mapping information used in realtime audits.|
|[**get_audits_query_servicemapping**](AuditApi.html#get_audits_query_servicemapping) | Get service mapping information used in audits.|
|[**get_audits_query_transaction_id**](AuditApi.html#get_audits_query_transaction_id) | Get status of audit query execution|
|[**get_audits_query_transaction_id_results**](AuditApi.html#get_audits_query_transaction_id_results) | Get results of audit query|
|[**post_audits_query**](AuditApi.html#post_audits_query) | Create audit query execution|
|[**post_audits_query_realtime**](AuditApi.html#post_audits_query_realtime) | This endpoint will only retrieve 14 days worth of audits for certain services. Please use /query to get a full list and older audits.|
{: class="table table-striped"}

<a name="get_audits_query_realtime_servicemapping"></a>

## [**AuditQueryServiceMapping**](AuditQueryServiceMapping.html) get_audits_query_realtime_servicemapping()



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

[**AuditQueryServiceMapping**](AuditQueryServiceMapping.html)

<a name="get_audits_query_servicemapping"></a>

## [**AuditQueryServiceMapping**](AuditQueryServiceMapping.html) get_audits_query_servicemapping()



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

[**AuditQueryServiceMapping**](AuditQueryServiceMapping.html)

<a name="get_audits_query_transaction_id"></a>

## [**AuditQueryExecutionStatusResponse**](AuditQueryExecutionStatusResponse.html) get_audits_query_transaction_id(transaction_id)



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
{: class="table table-striped"}

### Return type

[**AuditQueryExecutionStatusResponse**](AuditQueryExecutionStatusResponse.html)

<a name="get_audits_query_transaction_id_results"></a>

## [**AuditQueryExecutionResultsResponse**](AuditQueryExecutionResultsResponse.html) get_audits_query_transaction_id_results(transaction_id, cursor=cursor, page_size=page_size, expand=expand)



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

try:
    # Get results of audit query
    api_response = api_instance.get_audits_query_transaction_id_results(transaction_id, cursor=cursor, page_size=page_size, expand=expand)
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
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: user |
{: class="table table-striped"}

### Return type

[**AuditQueryExecutionResultsResponse**](AuditQueryExecutionResultsResponse.html)

<a name="post_audits_query"></a>

## [**AuditQueryExecutionStatusResponse**](AuditQueryExecutionStatusResponse.html) post_audits_query(body)



Create audit query execution



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
| **body** | [**AuditQueryRequest**](AuditQueryRequest.html)| query |  |
{: class="table table-striped"}

### Return type

[**AuditQueryExecutionStatusResponse**](AuditQueryExecutionStatusResponse.html)

<a name="post_audits_query_realtime"></a>

## [**AuditRealtimeQueryResultsResponse**](AuditRealtimeQueryResultsResponse.html) post_audits_query_realtime(body, expand=expand)



This endpoint will only retrieve 14 days worth of audits for certain services. Please use /query to get a full list and older audits.



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
| **body** | [**AuditRealtimeQueryRequest**](AuditRealtimeQueryRequest.html)| query |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: user |
{: class="table table-striped"}

### Return type

[**AuditRealtimeQueryResultsResponse**](AuditRealtimeQueryResultsResponse.html)


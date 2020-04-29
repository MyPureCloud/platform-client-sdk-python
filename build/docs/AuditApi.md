---
title: AuditApi
---

## PureCloudPlatformClientV2.AuditApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_audits_query_transaction_id**](AuditApi.html#get_audits_query_transaction_id) | Get status of audit query execution|
|[**get_audits_query_transaction_id_results**](AuditApi.html#get_audits_query_transaction_id_results) | Get results of audit query|
|[**post_audits_query**](AuditApi.html#post_audits_query) | Create audit query execution|
{: class="table table-striped"}

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
    print "Exception when calling AuditApi->get_audits_query_transaction_id: %s\n" % e
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
page_size = 25 # int | Page size (optional) (default to 25)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get results of audit query
    api_response = api_instance.get_audits_query_transaction_id_results(transaction_id, cursor=cursor, page_size=page_size, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditApi->get_audits_query_transaction_id_results: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **transaction_id** | **str**| Transaction ID |  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page) | [optional]  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
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
    print "Exception when calling AuditApi->post_audits_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AuditQueryRequest**](AuditQueryRequest.html)| query |  |
{: class="table table-striped"}

### Return type

[**AuditQueryExecutionStatusResponse**](AuditQueryExecutionStatusResponse.html)


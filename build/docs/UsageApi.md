---
title: UsageApi
---

## PureCloudPlatformClientV2.UsageApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_usage_query_execution_id_results**](UsageApi.html#get_usage_query_execution_id_results) | Get the results of a usage query|
|[**post_usage_query**](UsageApi.html#post_usage_query) | Query organization API Usage - |
{: class="table table-striped"}

<a name="get_usage_query_execution_id_results"></a>

## [**ApiUsageQueryResult**](ApiUsageQueryResult.html) get_usage_query_execution_id_results(execution_id)



Get the results of a usage query



Wraps GET /api/v2/usage/query/{executionId}/results 

Requires ANY permissions: 

* oauth:client:view

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
{: class="table table-striped"}

### Return type

[**ApiUsageQueryResult**](ApiUsageQueryResult.html)

<a name="post_usage_query"></a>

## [**UsageExecutionResult**](UsageExecutionResult.html) post_usage_query(body)



Query organization API Usage - 

After calling this method, you will then need to poll for the query results based on the returned execution Id



Wraps POST /api/v2/usage/query 

Requires ANY permissions: 

* oauth:client:view

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
body = PureCloudPlatformClientV2.ApiUsageQuery() # ApiUsageQuery | Query

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
| **body** | [**ApiUsageQuery**](ApiUsageQuery.html)| Query |  |
{: class="table table-striped"}

### Return type

[**UsageExecutionResult**](UsageExecutionResult.html)


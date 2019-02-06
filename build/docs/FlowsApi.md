---
title: FlowsApi
---

## PureCloudPlatformClientV2.FlowsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**post_analytics_flows_aggregates_query**](FlowsApi.html#post_analytics_flows_aggregates_query) | Query for flow aggregates|
{: class="table table-striped"}

<a name="post_analytics_flows_aggregates_query"></a>

## [**AggregateQueryResponse**](AggregateQueryResponse.html) post_analytics_flows_aggregates_query(body)



Query for flow aggregates



Wraps POST /api/v2/analytics/flows/aggregates/query 

Requires ANY permissions: 

* analytics:flowAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.FlowsApi()
body = PureCloudPlatformClientV2.AggregationQuery() # AggregationQuery | query

try:
    # Query for flow aggregates
    api_response = api_instance.post_analytics_flows_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FlowsApi->post_analytics_flows_aggregates_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AggregationQuery**](AggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AggregateQueryResponse**](AggregateQueryResponse.html)


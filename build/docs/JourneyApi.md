---
title: JourneyApi
---

## PureCloudPlatformClientV2.JourneyApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**post_analytics_journeys_aggregates_query**](JourneyApi.html#post_analytics_journeys_aggregates_query) | Query for journey aggregates|
{: class="table table-striped"}

<a name="post_analytics_journeys_aggregates_query"></a>

## [**JourneyAggregateQueryResponse**](JourneyAggregateQueryResponse.html) post_analytics_journeys_aggregates_query(body)



Query for journey aggregates



Wraps POST /api/v2/analytics/journeys/aggregates/query 

Requires ANY permissions: 

* analytics:journeyAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.JourneyApi()
body = PureCloudPlatformClientV2.JourneyAggregationQuery() # JourneyAggregationQuery | query

try:
    # Query for journey aggregates
    api_response = api_instance.post_analytics_journeys_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JourneyApi->post_analytics_journeys_aggregates_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**JourneyAggregationQuery**](JourneyAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**JourneyAggregateQueryResponse**](JourneyAggregateQueryResponse.html)


---
title: JourneyApi
---

## PureCloudPlatformClientV2.JourneyApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_journey_actiontarget**](JourneyApi.html#get_journey_actiontarget) | Retrieve a single action target.|
|[**get_journey_actiontargets**](JourneyApi.html#get_journey_actiontargets) | Retrieve all action targets.|
|[**patch_journey_actiontarget**](JourneyApi.html#patch_journey_actiontarget) | Update a single action target.|
|[**post_analytics_journeys_aggregates_query**](JourneyApi.html#post_analytics_journeys_aggregates_query) | Query for journey aggregates|
{: class="table table-striped"}

<a name="get_journey_actiontarget"></a>

## [**ActionTarget**](ActionTarget.html) get_journey_actiontarget(action_target_id)



Retrieve a single action target.



Wraps GET /api/v2/journey/actiontargets/{actionTargetId} 

Requires ANY permissions: 

* journey:actiontarget:view

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
action_target_id = 'action_target_id_example' # str | ID of the action target.

try:
    # Retrieve a single action target.
    api_response = api_instance.get_journey_actiontarget(action_target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_actiontarget: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_target_id** | **str**| ID of the action target. |  |
{: class="table table-striped"}

### Return type

[**ActionTarget**](ActionTarget.html)

<a name="get_journey_actiontargets"></a>

## [**ActionTargetListing**](ActionTargetListing.html) get_journey_actiontargets(page_number=page_number, page_size=page_size)



Retrieve all action targets.



Wraps GET /api/v2/journey/actiontargets 

Requires ANY permissions: 

* journey:actiontarget:view

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
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Retrieve all action targets.
    api_response = api_instance.get_journey_actiontargets(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_actiontargets: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**ActionTargetListing**](ActionTargetListing.html)

<a name="patch_journey_actiontarget"></a>

## [**ActionTarget**](ActionTarget.html) patch_journey_actiontarget(action_target_id, body=body)



Update a single action target.



Wraps PATCH /api/v2/journey/actiontargets/{actionTargetId} 

Requires ANY permissions: 

* journey:actiontarget:edit

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
action_target_id = 'action_target_id_example' # str | ID of the action target.
body = PureCloudPlatformClientV2.PatchActionTarget() # PatchActionTarget |  (optional)

try:
    # Update a single action target.
    api_response = api_instance.patch_journey_actiontarget(action_target_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->patch_journey_actiontarget: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_target_id** | **str**| ID of the action target. |  |
| **body** | [**PatchActionTarget**](PatchActionTarget.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**ActionTarget**](ActionTarget.html)

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
    print("Exception when calling JourneyApi->post_analytics_journeys_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**JourneyAggregationQuery**](JourneyAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**JourneyAggregateQueryResponse**](JourneyAggregateQueryResponse.html)


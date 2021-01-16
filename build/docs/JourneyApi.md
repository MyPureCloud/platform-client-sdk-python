---
title: JourneyApi
---

## PureCloudPlatformClientV2.JourneyApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_journey_segment**](JourneyApi.html#delete_journey_segment) | Delete a segment.|
|[**get_journey_actiontarget**](JourneyApi.html#get_journey_actiontarget) | Retrieve a single action target.|
|[**get_journey_actiontargets**](JourneyApi.html#get_journey_actiontargets) | Retrieve all action targets.|
|[**get_journey_segment**](JourneyApi.html#get_journey_segment) | Retrieve a single segment.|
|[**get_journey_segments**](JourneyApi.html#get_journey_segments) | Retrieve all segments.|
|[**patch_journey_actiontarget**](JourneyApi.html#patch_journey_actiontarget) | Update a single action target.|
|[**patch_journey_segment**](JourneyApi.html#patch_journey_segment) | Update a segment.|
|[**post_analytics_journeys_aggregates_query**](JourneyApi.html#post_analytics_journeys_aggregates_query) | Query for journey aggregates|
|[**post_journey_segments**](JourneyApi.html#post_journey_segments) | Create a segment.|
{: class="table table-striped"}

<a name="delete_journey_segment"></a>

##  delete_journey_segment(segment_id)



Delete a segment.



Wraps DELETE /api/v2/journey/segments/{segmentId} 

Requires ANY permissions: 

* journey:segment:delete

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
segment_id = 'segment_id_example' # str | ID of the segment.

try:
    # Delete a segment.
    api_instance.delete_journey_segment(segment_id)
except ApiException as e:
    print("Exception when calling JourneyApi->delete_journey_segment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **segment_id** | **str**| ID of the segment. |  |
{: class="table table-striped"}

### Return type

void (empty response body)

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

<a name="get_journey_segment"></a>

## [**JourneySegment**](JourneySegment.html) get_journey_segment(segment_id)



Retrieve a single segment.



Wraps GET /api/v2/journey/segments/{segmentId} 

Requires ANY permissions: 

* journey:segment:view

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
segment_id = 'segment_id_example' # str | ID of the segment.

try:
    # Retrieve a single segment.
    api_response = api_instance.get_journey_segment(segment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_segment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **segment_id** | **str**| ID of the segment. |  |
{: class="table table-striped"}

### Return type

[**JourneySegment**](JourneySegment.html)

<a name="get_journey_segments"></a>

## [**SegmentListing**](SegmentListing.html) get_journey_segments(sort_by=sort_by, page_size=page_size, page_number=page_number, is_active=is_active)



Retrieve all segments.



Wraps GET /api/v2/journey/segments 

Requires ANY permissions: 

* journey:segment:view

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
sort_by = 'sort_by_example' # str | Field(s) to sort by. The response can be sorted by any first level property on the Outcome response. Prefix with '-' for descending (e.g. sortBy=displayName,-createdDate). (optional)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
is_active = true # bool | Determines whether or not to show only active segments. (optional)

try:
    # Retrieve all segments.
    api_response = api_instance.get_journey_segments(sort_by=sort_by, page_size=page_size, page_number=page_number, is_active=is_active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_segments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sort_by** | **str**| Field(s) to sort by. The response can be sorted by any first level property on the Outcome response. Prefix with &#39;-&#39; for descending (e.g. sortBy=displayName,-createdDate). | [optional]  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **is_active** | **bool**| Determines whether or not to show only active segments. | [optional]  |
{: class="table table-striped"}

### Return type

[**SegmentListing**](SegmentListing.html)

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

<a name="patch_journey_segment"></a>

## [**JourneySegment**](JourneySegment.html) patch_journey_segment(segment_id, body=body)



Update a segment.



Wraps PATCH /api/v2/journey/segments/{segmentId} 

Requires ANY permissions: 

* journey:segment:edit

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
segment_id = 'segment_id_example' # str | ID of the segment.
body = PureCloudPlatformClientV2.PatchSegment() # PatchSegment |  (optional)

try:
    # Update a segment.
    api_response = api_instance.patch_journey_segment(segment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->patch_journey_segment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **segment_id** | **str**| ID of the segment. |  |
| **body** | [**PatchSegment**](PatchSegment.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**JourneySegment**](JourneySegment.html)

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

<a name="post_journey_segments"></a>

## [**JourneySegment**](JourneySegment.html) post_journey_segments(body=body)



Create a segment.



Wraps POST /api/v2/journey/segments 

Requires ANY permissions: 

* journey:segment:add

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
body = PureCloudPlatformClientV2.JourneySegment() # JourneySegment |  (optional)

try:
    # Create a segment.
    api_response = api_instance.post_journey_segments(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_segments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**JourneySegment**](JourneySegment.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**JourneySegment**](JourneySegment.html)


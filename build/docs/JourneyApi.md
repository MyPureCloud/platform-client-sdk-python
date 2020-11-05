---
title: JourneyApi
---

## PureCloudPlatformClientV2.JourneyApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_journey_actiontarget**](JourneyApi.html#get_journey_actiontarget) | Retrieve a single action target.|
|[**get_journey_actiontargets**](JourneyApi.html#get_journey_actiontargets) | Retrieve all action targets.|
|[**get_journey_customer_customer_id_segments**](JourneyApi.html#get_journey_customer_customer_id_segments) | Retrieve segment assignments by customer ID.|
|[**get_journey_externalcontact_segments**](JourneyApi.html#get_journey_externalcontact_segments) | Retrieve segment assignments by external contact ID.|
|[**get_journey_session_segments**](JourneyApi.html#get_journey_session_segments) | Retrieve segment assignments by session ID.|
|[**patch_journey_actiontarget**](JourneyApi.html#patch_journey_actiontarget) | Update a single action target.|
|[**post_analytics_journeys_aggregates_query**](JourneyApi.html#post_analytics_journeys_aggregates_query) | Query for journey aggregates|
|[**post_journey_externalcontact_segments**](JourneyApi.html#post_journey_externalcontact_segments) | Assign/Unassign a segment to/from an external contact or, if a segment is already assigned, update the expiry date of the segment assignment.|
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
    print "Exception when calling JourneyApi->get_journey_actiontarget: %s\n" % e
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
    print "Exception when calling JourneyApi->get_journey_actiontargets: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**ActionTargetListing**](ActionTargetListing.html)

<a name="get_journey_customer_customer_id_segments"></a>

## [**SegmentAssignmentListing**](SegmentAssignmentListing.html) get_journey_customer_customer_id_segments(customer_id_type, customer_id, page_size=page_size, after=after, segment_scope=segment_scope, assignment_state=assignment_state)



Retrieve segment assignments by customer ID.



Wraps GET /api/v2/journey/customers/{customerIdType}/{customerId}/segments 

Requires ANY permissions: 

* journey:segmentassignment:view

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
customer_id_type = 'customer_id_type_example' # str | Type of ID used to identify customer (e.g. email, cookie, and phone).
customer_id = 'customer_id_example' # str | Primary identifier of the customer to query for segment assignments.
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
segment_scope = 'segment_scope_example' # str | Scope to filter on. If not specified, both session-scoped and customer-scoped assignments are returned. (optional)
assignment_state = 'assignment_state_example' # str | Assignment state to filter on. If not specified, both assigned and unassigned assignments are returned. (optional)

try:
    # Retrieve segment assignments by customer ID.
    api_response = api_instance.get_journey_customer_customer_id_segments(customer_id_type, customer_id, page_size=page_size, after=after, segment_scope=segment_scope, assignment_state=assignment_state)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JourneyApi->get_journey_customer_customer_id_segments: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **customer_id_type** | **str**| Type of ID used to identify customer (e.g. email, cookie, and phone). |  |
| **customer_id** | **str**| Primary identifier of the customer to query for segment assignments. |  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **segment_scope** | **str**| Scope to filter on. If not specified, both session-scoped and customer-scoped assignments are returned. | [optional] <br />**Values**: Session, Customer |
| **assignment_state** | **str**| Assignment state to filter on. If not specified, both assigned and unassigned assignments are returned. | [optional] <br />**Values**: Assigned, Unassigned |
{: class="table table-striped"}

### Return type

[**SegmentAssignmentListing**](SegmentAssignmentListing.html)

<a name="get_journey_externalcontact_segments"></a>

## [**SegmentAssignmentListing**](SegmentAssignmentListing.html) get_journey_externalcontact_segments(external_contact_id, page_size=page_size, after=after, segment_scope=segment_scope, assignment_state=assignment_state)



Retrieve segment assignments by external contact ID.



Wraps GET /api/v2/journey/externalcontacts/{externalContactId}/segments 

Requires ANY permissions: 

* journey:segmentassignment:view

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
external_contact_id = 'external_contact_id_example' # str | ID of the external contact to query for segment assignments.
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
segment_scope = 'segment_scope_example' # str | Scope to filter on. If not specified, both session-scoped and customer-scoped assignments are returned. (optional)
assignment_state = 'assignment_state_example' # str | Assignment state to filter on. If not specified, both assigned and unassigned assignments are returned. (optional)

try:
    # Retrieve segment assignments by external contact ID.
    api_response = api_instance.get_journey_externalcontact_segments(external_contact_id, page_size=page_size, after=after, segment_scope=segment_scope, assignment_state=assignment_state)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JourneyApi->get_journey_externalcontact_segments: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_contact_id** | **str**| ID of the external contact to query for segment assignments. |  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **segment_scope** | **str**| Scope to filter on. If not specified, both session-scoped and customer-scoped assignments are returned. | [optional] <br />**Values**: Session, Customer |
| **assignment_state** | **str**| Assignment state to filter on. If not specified, both assigned and unassigned assignments are returned. | [optional] <br />**Values**: Assigned, Unassigned |
{: class="table table-striped"}

### Return type

[**SegmentAssignmentListing**](SegmentAssignmentListing.html)

<a name="get_journey_session_segments"></a>

## [**SegmentAssignmentListing**](SegmentAssignmentListing.html) get_journey_session_segments(session_id, page_size=page_size, after=after, segment_scope=segment_scope, assignment_state=assignment_state)



Retrieve segment assignments by session ID.



Wraps GET /api/v2/journey/sessions/{sessionId}/segments 

Requires ANY permissions: 

* journey:segmentassignment:view

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
session_id = 'session_id_example' # str | ID of the session to query for segment assignments.
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
segment_scope = 'segment_scope_example' # str | Scope to filter on. If not specified, both session-scoped and customer-scoped assignments are returned. (optional)
assignment_state = 'assignment_state_example' # str | Assignment state to filter on. If not specified, both assigned and unassigned assignments are returned. (optional)

try:
    # Retrieve segment assignments by session ID.
    api_response = api_instance.get_journey_session_segments(session_id, page_size=page_size, after=after, segment_scope=segment_scope, assignment_state=assignment_state)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JourneyApi->get_journey_session_segments: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| ID of the session to query for segment assignments. |  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **segment_scope** | **str**| Scope to filter on. If not specified, both session-scoped and customer-scoped assignments are returned. | [optional] <br />**Values**: Session, Customer |
| **assignment_state** | **str**| Assignment state to filter on. If not specified, both assigned and unassigned assignments are returned. | [optional] <br />**Values**: Assigned, Unassigned |
{: class="table table-striped"}

### Return type

[**SegmentAssignmentListing**](SegmentAssignmentListing.html)

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
    print "Exception when calling JourneyApi->patch_journey_actiontarget: %s\n" % e
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
    print "Exception when calling JourneyApi->post_analytics_journeys_aggregates_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**JourneyAggregationQuery**](JourneyAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**JourneyAggregateQueryResponse**](JourneyAggregateQueryResponse.html)

<a name="post_journey_externalcontact_segments"></a>

##  post_journey_externalcontact_segments(external_contact_id, body=body)



Assign/Unassign a segment to/from an external contact or, if a segment is already assigned, update the expiry date of the segment assignment.



Wraps POST /api/v2/journey/externalcontacts/{externalContactId}/segments 

Requires ANY permissions: 

* journey:segmentassignment:add
* journey:segmentassignment:delete

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
external_contact_id = 'external_contact_id_example' # str | ID of the external contact to query for segment assignments.
body = [PureCloudPlatformClientV2.SegmentAssignmentsUpdate()] # list[SegmentAssignmentsUpdate] |  (optional)

try:
    # Assign/Unassign a segment to/from an external contact or, if a segment is already assigned, update the expiry date of the segment assignment.
    api_instance.post_journey_externalcontact_segments(external_contact_id, body=body)
except ApiException as e:
    print "Exception when calling JourneyApi->post_journey_externalcontact_segments: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **external_contact_id** | **str**| ID of the external contact to query for segment assignments. |  |
| **body** | [**list[SegmentAssignmentsUpdate]**](SegmentAssignmentsUpdate.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)


---
title: JourneyApi
---

## PureCloudPlatformClientV2.JourneyApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_journey_actionmap**](JourneyApi.html#delete_journey_actionmap) | Delete single action map.|
|[**delete_journey_actiontemplate**](JourneyApi.html#delete_journey_actiontemplate) | Delete a single action template.|
|[**delete_journey_outcome**](JourneyApi.html#delete_journey_outcome) | Delete an outcome.|
|[**delete_journey_outcomes_predictor**](JourneyApi.html#delete_journey_outcomes_predictor) | Delete an outcome predictor.|
|[**delete_journey_segment**](JourneyApi.html#delete_journey_segment) | Delete a segment.|
|[**delete_journey_view**](JourneyApi.html#delete_journey_view) | Delete a Journey View by ID|
|[**get_analytics_journeys_aggregates_job**](JourneyApi.html#get_analytics_journeys_aggregates_job) | Get status for async query for journey aggregates|
|[**get_analytics_journeys_aggregates_job_results**](JourneyApi.html#get_analytics_journeys_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_externalcontacts_contact_journey_sessions**](JourneyApi.html#get_externalcontacts_contact_journey_sessions) | Retrieve all sessions for a given external contact.|
|[**get_journey_actionmap**](JourneyApi.html#get_journey_actionmap) | Retrieve a single action map.|
|[**get_journey_actionmaps**](JourneyApi.html#get_journey_actionmaps) | Retrieve all action maps.|
|[**get_journey_actionmaps_estimates_job**](JourneyApi.html#get_journey_actionmaps_estimates_job) | Get status of job.|
|[**get_journey_actionmaps_estimates_job_results**](JourneyApi.html#get_journey_actionmaps_estimates_job_results) | Get estimates from completed job.|
|[**get_journey_actiontarget**](JourneyApi.html#get_journey_actiontarget) | Retrieve a single action target.|
|[**get_journey_actiontargets**](JourneyApi.html#get_journey_actiontargets) | Retrieve all action targets.|
|[**get_journey_actiontemplate**](JourneyApi.html#get_journey_actiontemplate) | Retrieve a single action template.|
|[**get_journey_actiontemplates**](JourneyApi.html#get_journey_actiontemplates) | Retrieve all action templates.|
|[**get_journey_deployment_customer_ping**](JourneyApi.html#get_journey_deployment_customer_ping) | Send a ping.|
|[**get_journey_outcome**](JourneyApi.html#get_journey_outcome) | Retrieve a single outcome.|
|[**get_journey_outcomes**](JourneyApi.html#get_journey_outcomes) | Retrieve all outcomes.|
|[**get_journey_outcomes_attributions_job**](JourneyApi.html#get_journey_outcomes_attributions_job) | Get job status.|
|[**get_journey_outcomes_attributions_job_results**](JourneyApi.html#get_journey_outcomes_attributions_job_results) | Get outcome attribution entities from completed job.|
|[**get_journey_outcomes_predictor**](JourneyApi.html#get_journey_outcomes_predictor) | Retrieve a single outcome predictor.|
|[**get_journey_outcomes_predictors**](JourneyApi.html#get_journey_outcomes_predictors) | Retrieve all outcome predictors.|
|[**get_journey_segment**](JourneyApi.html#get_journey_segment) | Retrieve a single segment.|
|[**get_journey_segments**](JourneyApi.html#get_journey_segments) | Retrieve all segments.|
|[**get_journey_session**](JourneyApi.html#get_journey_session) | Retrieve a single session.|
|[**get_journey_session_events**](JourneyApi.html#get_journey_session_events) | Retrieve all events for a given session.|
|[**get_journey_session_outcomescores**](JourneyApi.html#get_journey_session_outcomescores) | Retrieve latest outcome score associated with a session for all outcomes.|
|[**get_journey_view**](JourneyApi.html#get_journey_view) | Get a Journey View by ID|
|[**get_journey_view_version**](JourneyApi.html#get_journey_view_version) | Get a Journey View by ID and version|
|[**get_journey_views**](JourneyApi.html#get_journey_views) | Get a list of Journey Views|
|[**patch_journey_actionmap**](JourneyApi.html#patch_journey_actionmap) | Update single action map.|
|[**patch_journey_actiontarget**](JourneyApi.html#patch_journey_actiontarget) | Update a single action target.|
|[**patch_journey_actiontemplate**](JourneyApi.html#patch_journey_actiontemplate) | Update a single action template.|
|[**patch_journey_outcome**](JourneyApi.html#patch_journey_outcome) | Update an outcome.|
|[**patch_journey_segment**](JourneyApi.html#patch_journey_segment) | Update a segment.|
|[**post_analytics_journeys_aggregates_jobs**](JourneyApi.html#post_analytics_journeys_aggregates_jobs) | Query for journey aggregates asynchronously|
|[**post_analytics_journeys_aggregates_query**](JourneyApi.html#post_analytics_journeys_aggregates_query) | Query for journey aggregates|
|[**post_journey_actionmaps**](JourneyApi.html#post_journey_actionmaps) | Create an action map.|
|[**post_journey_actionmaps_estimates_jobs**](JourneyApi.html#post_journey_actionmaps_estimates_jobs) | Query for estimates|
|[**post_journey_actiontemplates**](JourneyApi.html#post_journey_actiontemplates) | Create a single action template.|
|[**post_journey_deployment_actionevent**](JourneyApi.html#post_journey_deployment_actionevent) | Sends an action event, which is used for changing the state of actions that have been offered to the user.|
|[**post_journey_deployment_appevents**](JourneyApi.html#post_journey_deployment_appevents) | Send a journey app event, used for tracking customer activity on an application.|
|[**post_journey_flows_paths_query**](JourneyApi.html#post_journey_flows_paths_query) | Query for flow paths.|
|[**post_journey_outcomes**](JourneyApi.html#post_journey_outcomes) | Create an outcome.|
|[**post_journey_outcomes_attributions_jobs**](JourneyApi.html#post_journey_outcomes_attributions_jobs) | Create Outcome Attributions|
|[**post_journey_outcomes_predictors**](JourneyApi.html#post_journey_outcomes_predictors) | Create an outcome predictor.|
|[**post_journey_segments**](JourneyApi.html#post_journey_segments) | Create a segment.|
|[**post_journey_view_versions**](JourneyApi.html#post_journey_view_versions) | Update a Journey View by ID|
|[**post_journey_views**](JourneyApi.html#post_journey_views) | Create a new Journey View|
{: class="table table-striped"}

<a name="delete_journey_actionmap"></a>

##  delete_journey_actionmap(action_map_id)



Delete single action map.

Wraps DELETE /api/v2/journey/actionmaps/{actionMapId} 

Requires ANY permissions: 

* journey:actionmap:delete

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
action_map_id = 'action_map_id_example' # str | ID of the action map.

try:
    # Delete single action map.
    api_instance.delete_journey_actionmap(action_map_id)
except ApiException as e:
    print("Exception when calling JourneyApi->delete_journey_actionmap: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_map_id** | **str**| ID of the action map. |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_journey_actiontemplate"></a>

##  delete_journey_actiontemplate(action_template_id, hard_delete=hard_delete)



Delete a single action template.

Wraps DELETE /api/v2/journey/actiontemplates/{actionTemplateId} 

Requires ANY permissions: 

* journey:actiontemplate:delete

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
action_template_id = 'action_template_id_example' # str | ID of the action template.
hard_delete = True # bool | Determines whether Action Template should be soft-deleted (have it's state set to deleted) or hard-deleted (permanently removed). Set to false (soft-delete) by default. (optional)

try:
    # Delete a single action template.
    api_instance.delete_journey_actiontemplate(action_template_id, hard_delete=hard_delete)
except ApiException as e:
    print("Exception when calling JourneyApi->delete_journey_actiontemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_template_id** | **str**| ID of the action template. |  |
| **hard_delete** | **bool**| Determines whether Action Template should be soft-deleted (have it&#39;s state set to deleted) or hard-deleted (permanently removed). Set to false (soft-delete) by default. | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_journey_outcome"></a>

##  delete_journey_outcome(outcome_id)



Delete an outcome.

Wraps DELETE /api/v2/journey/outcomes/{outcomeId} 

Requires ANY permissions: 

* journey:outcome:delete

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
outcome_id = 'outcome_id_example' # str | ID of the outcome.

try:
    # Delete an outcome.
    api_instance.delete_journey_outcome(outcome_id)
except ApiException as e:
    print("Exception when calling JourneyApi->delete_journey_outcome: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **outcome_id** | **str**| ID of the outcome. |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_journey_outcomes_predictor"></a>

##  delete_journey_outcomes_predictor(predictor_id)



Delete an outcome predictor.

Wraps DELETE /api/v2/journey/outcomes/predictors/{predictorId} 

Requires ANY permissions: 

* journey:outcomepredictor:delete

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
predictor_id = 'predictor_id_example' # str | ID of predictor

try:
    # Delete an outcome predictor.
    api_instance.delete_journey_outcomes_predictor(predictor_id)
except ApiException as e:
    print("Exception when calling JourneyApi->delete_journey_outcomes_predictor: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **predictor_id** | **str**| ID of predictor |  |
{: class="table table-striped"}

### Return type

void (empty response body)

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

<a name="delete_journey_view"></a>

##  delete_journey_view(view_id)



Delete a Journey View by ID

deletes all versions

delete_journey_view is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/journey/views/{viewId} 

Requires ALL permissions: 

* journey:views:delete

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
view_id = 'view_id_example' # str | viewId

try:
    # Delete a Journey View by ID
    api_instance.delete_journey_view(view_id)
except ApiException as e:
    print("Exception when calling JourneyApi->delete_journey_view: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| viewId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_analytics_journeys_aggregates_job"></a>

## [**AsyncQueryStatus**](AsyncQueryStatus.html) get_analytics_journeys_aggregates_job(job_id)



Get status for async query for journey aggregates

get_analytics_journeys_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/journeys/aggregates/jobs/{jobId} 

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
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for journey aggregates
    api_response = api_instance.get_analytics_journeys_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_analytics_journeys_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus.html)

<a name="get_analytics_journeys_aggregates_job_results"></a>

## [**JourneyAsyncAggregateQueryResponse**](JourneyAsyncAggregateQueryResponse.html) get_analytics_journeys_aggregates_job_results(job_id, cursor=cursor)



Fetch a page of results for an async aggregates query

get_analytics_journeys_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/journeys/aggregates/jobs/{jobId}/results 

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
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_journeys_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_analytics_journeys_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |
{: class="table table-striped"}

### Return type

[**JourneyAsyncAggregateQueryResponse**](JourneyAsyncAggregateQueryResponse.html)

<a name="get_externalcontacts_contact_journey_sessions"></a>

## [**SessionListing**](SessionListing.html) get_externalcontacts_contact_journey_sessions(contact_id, page_size=page_size, after=after, include_merged=include_merged)



Retrieve all sessions for a given external contact.

Wraps GET /api/v2/externalcontacts/contacts/{contactId}/journey/sessions 

Requires ANY permissions: 

* externalContacts:session:view

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
contact_id = 'contact_id_example' # str | ExternalContact ID
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
include_merged = True # bool | Indicates whether to return sessions from all external contacts in the merge-set of the given one. (optional)

try:
    # Retrieve all sessions for a given external contact.
    api_response = api_instance.get_externalcontacts_contact_journey_sessions(contact_id, page_size=page_size, after=after, include_merged=include_merged)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_externalcontacts_contact_journey_sessions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **include_merged** | **bool**| Indicates whether to return sessions from all external contacts in the merge-set of the given one. | [optional]  |
{: class="table table-striped"}

### Return type

[**SessionListing**](SessionListing.html)

<a name="get_journey_actionmap"></a>

## [**ActionMap**](ActionMap.html) get_journey_actionmap(action_map_id)



Retrieve a single action map.

Wraps GET /api/v2/journey/actionmaps/{actionMapId} 

Requires ANY permissions: 

* journey:actionmap:view

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
action_map_id = 'action_map_id_example' # str | ID of the action map.

try:
    # Retrieve a single action map.
    api_response = api_instance.get_journey_actionmap(action_map_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_actionmap: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_map_id** | **str**| ID of the action map. |  |
{: class="table table-striped"}

### Return type

[**ActionMap**](ActionMap.html)

<a name="get_journey_actionmaps"></a>

## [**ActionMapListing**](ActionMapListing.html) get_journey_actionmaps(page_number=page_number, page_size=page_size, sort_by=sort_by, filter_field=filter_field, filter_value=filter_value, action_map_ids=action_map_ids, query_fields=query_fields, query_value=query_value)



Retrieve all action maps.

Wraps GET /api/v2/journey/actionmaps 

Requires ANY permissions: 

* journey:actionmap:view

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
sort_by = 'sort_by_example' # str | Field(s) to sort by. Prefix with '-' for descending (e.g. sortBy=displayName,-createdDate). (optional)
filter_field = 'filter_field_example' # str | Field to filter by (e.g. filterField=weight or filterField=action.actionTemplate.id). Requires 'filterField' to also be set. (optional)
filter_value = 'filter_value_example' # str | Value to filter by. Requires 'filterValue' to also be set. (optional)
action_map_ids = ['action_map_ids_example'] # list[str] | IDs of action maps to return. Use of this parameter is not compatible with pagination, filtering, sorting or querying. A maximum of 100 action maps are allowed per request. (optional)
query_fields = ['query_fields_example'] # list[str] | Action Map field(s) to query on. Requires 'queryValue' to also be set. (optional)
query_value = 'query_value_example' # str | Value to query on. Requires 'queryFields' to also be set. (optional)

try:
    # Retrieve all action maps.
    api_response = api_instance.get_journey_actionmaps(page_number=page_number, page_size=page_size, sort_by=sort_by, filter_field=filter_field, filter_value=filter_value, action_map_ids=action_map_ids, query_fields=query_fields, query_value=query_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_actionmaps: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Field(s) to sort by. Prefix with &#39;-&#39; for descending (e.g. sortBy&#x3D;displayName,-createdDate). | [optional]  |
| **filter_field** | **str**| Field to filter by (e.g. filterField&#x3D;weight or filterField&#x3D;action.actionTemplate.id). Requires &#39;filterField&#39; to also be set. | [optional]  |
| **filter_value** | **str**| Value to filter by. Requires &#39;filterValue&#39; to also be set. | [optional]  |
| **action_map_ids** | [**list[str]**](str.html)| IDs of action maps to return. Use of this parameter is not compatible with pagination, filtering, sorting or querying. A maximum of 100 action maps are allowed per request. | [optional]  |
| **query_fields** | [**list[str]**](str.html)| Action Map field(s) to query on. Requires &#39;queryValue&#39; to also be set. | [optional]  |
| **query_value** | **str**| Value to query on. Requires &#39;queryFields&#39; to also be set. | [optional]  |
{: class="table table-striped"}

### Return type

[**ActionMapListing**](ActionMapListing.html)

<a name="get_journey_actionmaps_estimates_job"></a>

## str** get_journey_actionmaps_estimates_job(job_id)



Get status of job.

Wraps GET /api/v2/journey/actionmaps/estimates/jobs/{jobId} 

Requires ALL permissions: 

* journey:actionmapEstimateJob:view

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
job_id = 'job_id_example' # str | ID of the job.

try:
    # Get status of job.
    api_response = api_instance.get_journey_actionmaps_estimates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_actionmaps_estimates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| ID of the job. |  |
{: class="table table-striped"}

### Return type

**str**

<a name="get_journey_actionmaps_estimates_job_results"></a>

## [**ActionMapEstimateResult**](ActionMapEstimateResult.html) get_journey_actionmaps_estimates_job_results(job_id)



Get estimates from completed job.

Wraps GET /api/v2/journey/actionmaps/estimates/jobs/{jobId}/results 

Requires ALL permissions: 

* journey:actionmapEstimate:view

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
job_id = 'job_id_example' # str | ID of the job.

try:
    # Get estimates from completed job.
    api_response = api_instance.get_journey_actionmaps_estimates_job_results(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_actionmaps_estimates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| ID of the job. |  |
{: class="table table-striped"}

### Return type

[**ActionMapEstimateResult**](ActionMapEstimateResult.html)

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

<a name="get_journey_actiontemplate"></a>

## [**ActionTemplate**](ActionTemplate.html) get_journey_actiontemplate(action_template_id)



Retrieve a single action template.

Wraps GET /api/v2/journey/actiontemplates/{actionTemplateId} 

Requires ANY permissions: 

* journey:actiontemplate:view

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
action_template_id = 'action_template_id_example' # str | ID of the action template.

try:
    # Retrieve a single action template.
    api_response = api_instance.get_journey_actiontemplate(action_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_actiontemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_template_id** | **str**| ID of the action template. |  |
{: class="table table-striped"}

### Return type

[**ActionTemplate**](ActionTemplate.html)

<a name="get_journey_actiontemplates"></a>

## [**ActionTemplateListing**](ActionTemplateListing.html) get_journey_actiontemplates(page_number=page_number, page_size=page_size, sort_by=sort_by, media_type=media_type, state=state, query_fields=query_fields, query_value=query_value)



Retrieve all action templates.

Wraps GET /api/v2/journey/actiontemplates 

Requires ANY permissions: 

* journey:actiontemplate:view

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
sort_by = 'sort_by_example' # str | Field(s) to sort by. Prefix with '-' for descending (e.g. sortBy=name,-createdDate). (optional)
media_type = 'media_type_example' # str | Media type (optional)
state = 'state_example' # str | Action template state. (optional)
query_fields = ['query_fields_example'] # list[str] | ActionTemplate field(s) to query on. Requires 'queryValue' to also be set. (optional)
query_value = 'query_value_example' # str | Value to query on. Requires 'queryFields' to also be set. (optional)

try:
    # Retrieve all action templates.
    api_response = api_instance.get_journey_actiontemplates(page_number=page_number, page_size=page_size, sort_by=sort_by, media_type=media_type, state=state, query_fields=query_fields, query_value=query_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_actiontemplates: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Field(s) to sort by. Prefix with &#39;-&#39; for descending (e.g. sortBy&#x3D;name,-createdDate). | [optional]  |
| **media_type** | **str**| Media type | [optional] <br />**Values**: webchat, webMessagingOffer, contentOffer, integrationAction, architectFlow, openAction |
| **state** | **str**| Action template state. | [optional] <br />**Values**: Active, Inactive, Deleted |
| **query_fields** | [**list[str]**](str.html)| ActionTemplate field(s) to query on. Requires &#39;queryValue&#39; to also be set. | [optional]  |
| **query_value** | **str**| Value to query on. Requires &#39;queryFields&#39; to also be set. | [optional]  |
{: class="table table-striped"}

### Return type

[**ActionTemplateListing**](ActionTemplateListing.html)

<a name="get_journey_deployment_customer_ping"></a>

## [**DeploymentPing**](DeploymentPing.html) get_journey_deployment_customer_ping(deployment_id, customer_cookie_id, dl=dl, dt=dt, app_namespace=app_namespace, session_id=session_id, since_last_beacon_milliseconds=since_last_beacon_milliseconds)



Send a ping.

Wraps GET /api/v2/journey/deployments/{deploymentId}/customers/{customerCookieId}/ping 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.JourneyApi()
deployment_id = 'deployment_id_example' # str | The ID of the deployment sending the ping.
customer_cookie_id = 'customer_cookie_id_example' # str | ID of the customer associated with the ping.
dl = 'dl_example' # str | Document Location: 1) Web Page URL if overridden or URL fragment identifier (window.location.hash). OR  2) Application screen name that the ping request was sent from in the app. e.g. 'home' or 'help. Pings without this parameter will not return actions. (optional)
dt = 'dt_example' # str | Document Title.  A human readable name for the page or screen (optional)
app_namespace = 'app_namespace_example' # str | Namespace of the application (e.g. com.genesys.bancodinero). Used for domain filtering in application sessions (optional)
session_id = 'session_id_example' # str | UUID of the customer session. Use the same Session Id for all pings, AppEvents and ActionEvents in the session (optional)
since_last_beacon_milliseconds = 56 # int | How long (milliseconds) since the last app event or beacon was sent. The response may return a pollInternvalMilliseconds to reduce the frequency of pings. (optional)

try:
    # Send a ping.
    api_response = api_instance.get_journey_deployment_customer_ping(deployment_id, customer_cookie_id, dl=dl, dt=dt, app_namespace=app_namespace, session_id=session_id, since_last_beacon_milliseconds=since_last_beacon_milliseconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_deployment_customer_ping: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| The ID of the deployment sending the ping. |  |
| **customer_cookie_id** | **str**| ID of the customer associated with the ping. |  |
| **dl** | **str**| Document Location: 1) Web Page URL if overridden or URL fragment identifier (window.location.hash). OR  2) Application screen name that the ping request was sent from in the app. e.g. &#39;home&#39; or &#39;help. Pings without this parameter will not return actions. | [optional]  |
| **dt** | **str**| Document Title.  A human readable name for the page or screen | [optional]  |
| **app_namespace** | **str**| Namespace of the application (e.g. com.genesys.bancodinero). Used for domain filtering in application sessions | [optional]  |
| **session_id** | **str**| UUID of the customer session. Use the same Session Id for all pings, AppEvents and ActionEvents in the session | [optional]  |
| **since_last_beacon_milliseconds** | **int**| How long (milliseconds) since the last app event or beacon was sent. The response may return a pollInternvalMilliseconds to reduce the frequency of pings. | [optional]  |
{: class="table table-striped"}

### Return type

[**DeploymentPing**](DeploymentPing.html)

<a name="get_journey_outcome"></a>

## [**Outcome**](Outcome.html) get_journey_outcome(outcome_id)



Retrieve a single outcome.

Wraps GET /api/v2/journey/outcomes/{outcomeId} 

Requires ANY permissions: 

* journey:outcome:view

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
outcome_id = 'outcome_id_example' # str | ID of the outcome.

try:
    # Retrieve a single outcome.
    api_response = api_instance.get_journey_outcome(outcome_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_outcome: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **outcome_id** | **str**| ID of the outcome. |  |
{: class="table table-striped"}

### Return type

[**Outcome**](Outcome.html)

<a name="get_journey_outcomes"></a>

## [**OutcomeListing**](OutcomeListing.html) get_journey_outcomes(page_number=page_number, page_size=page_size, sort_by=sort_by, outcome_ids=outcome_ids, query_fields=query_fields, query_value=query_value)



Retrieve all outcomes.

Wraps GET /api/v2/journey/outcomes 

Requires ANY permissions: 

* journey:outcome:view

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
sort_by = 'sort_by_example' # str | Field(s) to sort by. The response can be sorted by any first level property on the Outcome response. Prefix with '-' for descending (e.g. sortBy=displayName,-createdDate). (optional)
outcome_ids = ['outcome_ids_example'] # list[str] | IDs of outcomes to return. Use of this parameter is not compatible with pagination, sorting or querying. A maximum of 20 outcomes are allowed per request. (optional)
query_fields = ['query_fields_example'] # list[str] | Outcome field(s) to query on. Requires 'queryValue' to also be set. (optional)
query_value = 'query_value_example' # str | Value to query on. Requires 'queryFields' to also be set. (optional)

try:
    # Retrieve all outcomes.
    api_response = api_instance.get_journey_outcomes(page_number=page_number, page_size=page_size, sort_by=sort_by, outcome_ids=outcome_ids, query_fields=query_fields, query_value=query_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_outcomes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **sort_by** | **str**| Field(s) to sort by. The response can be sorted by any first level property on the Outcome response. Prefix with &#39;-&#39; for descending (e.g. sortBy&#x3D;displayName,-createdDate). | [optional]  |
| **outcome_ids** | [**list[str]**](str.html)| IDs of outcomes to return. Use of this parameter is not compatible with pagination, sorting or querying. A maximum of 20 outcomes are allowed per request. | [optional]  |
| **query_fields** | [**list[str]**](str.html)| Outcome field(s) to query on. Requires &#39;queryValue&#39; to also be set. | [optional]  |
| **query_value** | **str**| Value to query on. Requires &#39;queryFields&#39; to also be set. | [optional]  |
{: class="table table-striped"}

### Return type

[**OutcomeListing**](OutcomeListing.html)

<a name="get_journey_outcomes_attributions_job"></a>

## [**OutcomeAttributionJobStateResponse**](OutcomeAttributionJobStateResponse.html) get_journey_outcomes_attributions_job(job_id)



Get job status.

get_journey_outcomes_attributions_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/journey/outcomes/attributions/jobs/{jobId} 

Requires ALL permissions: 

* journey:outcomeAttributionJob:view

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
job_id = 'job_id_example' # str | ID of the job.

try:
    # Get job status.
    api_response = api_instance.get_journey_outcomes_attributions_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_outcomes_attributions_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| ID of the job. |  |
{: class="table table-striped"}

### Return type

[**OutcomeAttributionJobStateResponse**](OutcomeAttributionJobStateResponse.html)

<a name="get_journey_outcomes_attributions_job_results"></a>

## [**OutcomeAttributionResponseListing**](OutcomeAttributionResponseListing.html) get_journey_outcomes_attributions_job_results(job_id)



Get outcome attribution entities from completed job.

get_journey_outcomes_attributions_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/journey/outcomes/attributions/jobs/{jobId}/results 

Requires ALL permissions: 

* journey:outcomeAttribution:view

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
job_id = 'job_id_example' # str | ID of the job.

try:
    # Get outcome attribution entities from completed job.
    api_response = api_instance.get_journey_outcomes_attributions_job_results(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_outcomes_attributions_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| ID of the job. |  |
{: class="table table-striped"}

### Return type

[**OutcomeAttributionResponseListing**](OutcomeAttributionResponseListing.html)

<a name="get_journey_outcomes_predictor"></a>

## [**OutcomePredictor**](OutcomePredictor.html) get_journey_outcomes_predictor(predictor_id)



Retrieve a single outcome predictor.

Wraps GET /api/v2/journey/outcomes/predictors/{predictorId} 

Requires ANY permissions: 

* journey:outcomepredictor:view

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
predictor_id = 'predictor_id_example' # str | ID of predictor

try:
    # Retrieve a single outcome predictor.
    api_response = api_instance.get_journey_outcomes_predictor(predictor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_outcomes_predictor: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **predictor_id** | **str**| ID of predictor |  |
{: class="table table-striped"}

### Return type

[**OutcomePredictor**](OutcomePredictor.html)

<a name="get_journey_outcomes_predictors"></a>

## [**OutcomePredictorListing**](OutcomePredictorListing.html) get_journey_outcomes_predictors()



Retrieve all outcome predictors.

Wraps GET /api/v2/journey/outcomes/predictors 

Requires ANY permissions: 

* journey:outcomepredictor:view

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

try:
    # Retrieve all outcome predictors.
    api_response = api_instance.get_journey_outcomes_predictors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_outcomes_predictors: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**OutcomePredictorListing**](OutcomePredictorListing.html)

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

## [**SegmentListing**](SegmentListing.html) get_journey_segments(sort_by=sort_by, page_size=page_size, page_number=page_number, is_active=is_active, segment_ids=segment_ids, query_fields=query_fields, query_value=query_value)



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
is_active = True # bool | Determines whether or not to show only active segments. (optional)
segment_ids = ['segment_ids_example'] # list[str] | IDs of segments to return. Use of this parameter is not compatible with pagination, sorting or querying. A maximum of 100 segments are allowed per request. (optional)
query_fields = ['query_fields_example'] # list[str] | Segment field(s) to query on. Requires 'queryValue' to also be set. (optional)
query_value = 'query_value_example' # str | Value to query on. Requires 'queryFields' to also be set. (optional)

try:
    # Retrieve all segments.
    api_response = api_instance.get_journey_segments(sort_by=sort_by, page_size=page_size, page_number=page_number, is_active=is_active, segment_ids=segment_ids, query_fields=query_fields, query_value=query_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_segments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sort_by** | **str**| Field(s) to sort by. The response can be sorted by any first level property on the Outcome response. Prefix with &#39;-&#39; for descending (e.g. sortBy&#x3D;displayName,-createdDate). | [optional]  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **is_active** | **bool**| Determines whether or not to show only active segments. | [optional]  |
| **segment_ids** | [**list[str]**](str.html)| IDs of segments to return. Use of this parameter is not compatible with pagination, sorting or querying. A maximum of 100 segments are allowed per request. | [optional]  |
| **query_fields** | [**list[str]**](str.html)| Segment field(s) to query on. Requires &#39;queryValue&#39; to also be set. | [optional]  |
| **query_value** | **str**| Value to query on. Requires &#39;queryFields&#39; to also be set. | [optional]  |
{: class="table table-striped"}

### Return type

[**SegmentListing**](SegmentListing.html)

<a name="get_journey_session"></a>

## [**Session**](Session.html) get_journey_session(session_id)



Retrieve a single session.

Wraps GET /api/v2/journey/sessions/{sessionId} 

Requires ANY permissions: 

* journey:session:view
* externalContacts:session:view

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
session_id = 'session_id_example' # str | ID of the session.

try:
    # Retrieve a single session.
    api_response = api_instance.get_journey_session(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_session: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| ID of the session. |  |
{: class="table table-striped"}

### Return type

[**Session**](Session.html)

<a name="get_journey_session_events"></a>

## [**EventListing**](EventListing.html) get_journey_session_events(session_id, page_size=page_size, after=after)



Retrieve all events for a given session.

get_journey_session_events is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/journey/sessions/{sessionId}/events 

Requires ANY permissions: 

* journey:event:view

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
session_id = 'session_id_example' # str | System-generated UUID that represents the session the event is a part of.
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)

try:
    # Retrieve all events for a given session.
    api_response = api_instance.get_journey_session_events(session_id, page_size=page_size, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_session_events: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| System-generated UUID that represents the session the event is a part of. |  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
{: class="table table-striped"}

### Return type

[**EventListing**](EventListing.html)

<a name="get_journey_session_outcomescores"></a>

## [**OutcomeScoresResult**](OutcomeScoresResult.html) get_journey_session_outcomescores(session_id)



Retrieve latest outcome score associated with a session for all outcomes.

Wraps GET /api/v2/journey/sessions/{sessionId}/outcomescores 

Requires ANY permissions: 

* journey:outcomescores:view

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
session_id = 'session_id_example' # str | ID of the session.

try:
    # Retrieve latest outcome score associated with a session for all outcomes.
    api_response = api_instance.get_journey_session_outcomescores(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_session_outcomescores: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| ID of the session. |  |
{: class="table table-striped"}

### Return type

[**OutcomeScoresResult**](OutcomeScoresResult.html)

<a name="get_journey_view"></a>

## [**JourneyView**](JourneyView.html) get_journey_view(view_id)



Get a Journey View by ID

returns the latest version

get_journey_view is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/journey/views/{viewId} 

Requires ALL permissions: 

* journey:views:view

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
view_id = 'view_id_example' # str | viewId

try:
    # Get a Journey View by ID
    api_response = api_instance.get_journey_view(view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_view: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| viewId |  |
{: class="table table-striped"}

### Return type

[**JourneyView**](JourneyView.html)

<a name="get_journey_view_version"></a>

## [**JourneyView**](JourneyView.html) get_journey_view_version(view_id, version_id)



Get a Journey View by ID and version

get_journey_view_version is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/journey/views/{viewId}/versions/{versionId} 

Requires ALL permissions: 

* journey:views:view

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
view_id = 'view_id_example' # str | viewId
version_id = 'version_id_example' # str | versionId

try:
    # Get a Journey View by ID and version
    api_response = api_instance.get_journey_view_version(view_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_view_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| viewId |  |
| **version_id** | **str**| versionId |  |
{: class="table table-striped"}

### Return type

[**JourneyView**](JourneyView.html)

<a name="get_journey_views"></a>

## [**AddressableEntityListing**](AddressableEntityListing.html) get_journey_views()



Get a list of Journey Views

get_journey_views is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/journey/views 

Requires ALL permissions: 

* journey:views:view

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

try:
    # Get a list of Journey Views
    api_response = api_instance.get_journey_views()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_views: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**AddressableEntityListing**](AddressableEntityListing.html)

<a name="patch_journey_actionmap"></a>

## [**ActionMap**](ActionMap.html) patch_journey_actionmap(action_map_id, body=body)



Update single action map.

Wraps PATCH /api/v2/journey/actionmaps/{actionMapId} 

Requires ANY permissions: 

* journey:actionmap:edit

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
action_map_id = 'action_map_id_example' # str | ID of the action map.
body = PureCloudPlatformClientV2.PatchActionMap() # PatchActionMap |  (optional)

try:
    # Update single action map.
    api_response = api_instance.patch_journey_actionmap(action_map_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->patch_journey_actionmap: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_map_id** | **str**| ID of the action map. |  |
| **body** | [**PatchActionMap**](PatchActionMap.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**ActionMap**](ActionMap.html)

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

<a name="patch_journey_actiontemplate"></a>

## [**ActionTemplate**](ActionTemplate.html) patch_journey_actiontemplate(action_template_id, body=body)



Update a single action template.

Wraps PATCH /api/v2/journey/actiontemplates/{actionTemplateId} 

Requires ANY permissions: 

* journey:actiontemplate:edit

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
action_template_id = 'action_template_id_example' # str | ID of the action template.
body = PureCloudPlatformClientV2.PatchActionTemplate() # PatchActionTemplate |  (optional)

try:
    # Update a single action template.
    api_response = api_instance.patch_journey_actiontemplate(action_template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->patch_journey_actiontemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_template_id** | **str**| ID of the action template. |  |
| **body** | [**PatchActionTemplate**](PatchActionTemplate.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**ActionTemplate**](ActionTemplate.html)

<a name="patch_journey_outcome"></a>

## [**Outcome**](Outcome.html) patch_journey_outcome(outcome_id, body=body)



Update an outcome.

Wraps PATCH /api/v2/journey/outcomes/{outcomeId} 

Requires ANY permissions: 

* journey:outcome:edit

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
outcome_id = 'outcome_id_example' # str | ID of the outcome.
body = PureCloudPlatformClientV2.PatchOutcome() # PatchOutcome |  (optional)

try:
    # Update an outcome.
    api_response = api_instance.patch_journey_outcome(outcome_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->patch_journey_outcome: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **outcome_id** | **str**| ID of the outcome. |  |
| **body** | [**PatchOutcome**](PatchOutcome.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**Outcome**](Outcome.html)

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

<a name="post_analytics_journeys_aggregates_jobs"></a>

## [**AsyncQueryResponse**](AsyncQueryResponse.html) post_analytics_journeys_aggregates_jobs(body)



Query for journey aggregates asynchronously

post_analytics_journeys_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/journeys/aggregates/jobs 

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
body = PureCloudPlatformClientV2.JourneyAsyncAggregationQuery() # JourneyAsyncAggregationQuery | query

try:
    # Query for journey aggregates asynchronously
    api_response = api_instance.post_analytics_journeys_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_analytics_journeys_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**JourneyAsyncAggregationQuery**](JourneyAsyncAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse.html)

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

<a name="post_journey_actionmaps"></a>

## [**ActionMap**](ActionMap.html) post_journey_actionmaps(body=body)



Create an action map.

Wraps POST /api/v2/journey/actionmaps 

Requires ANY permissions: 

* journey:actionmap:add

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
body = PureCloudPlatformClientV2.ActionMap() # ActionMap |  (optional)

try:
    # Create an action map.
    api_response = api_instance.post_journey_actionmaps(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_actionmaps: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ActionMap**](ActionMap.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**ActionMap**](ActionMap.html)

<a name="post_journey_actionmaps_estimates_jobs"></a>

## [**EstimateJobAsyncResponse**](EstimateJobAsyncResponse.html) post_journey_actionmaps_estimates_jobs(body)



Query for estimates

Wraps POST /api/v2/journey/actionmaps/estimates/jobs 

Requires ANY permissions: 

* journey:actionmapEstimateJob:add

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
body = PureCloudPlatformClientV2.ActionMapEstimateRequest() # ActionMapEstimateRequest | audience estimator request

try:
    # Query for estimates
    api_response = api_instance.post_journey_actionmaps_estimates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_actionmaps_estimates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ActionMapEstimateRequest**](ActionMapEstimateRequest.html)| audience estimator request |  |
{: class="table table-striped"}

### Return type

[**EstimateJobAsyncResponse**](EstimateJobAsyncResponse.html)

<a name="post_journey_actiontemplates"></a>

## [**ActionTemplate**](ActionTemplate.html) post_journey_actiontemplates(body=body)



Create a single action template.

Wraps POST /api/v2/journey/actiontemplates 

Requires ANY permissions: 

* journey:actiontemplate:add

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
body = PureCloudPlatformClientV2.ActionTemplate() # ActionTemplate |  (optional)

try:
    # Create a single action template.
    api_response = api_instance.post_journey_actiontemplates(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_actiontemplates: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ActionTemplate**](ActionTemplate.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**ActionTemplate**](ActionTemplate.html)

<a name="post_journey_deployment_actionevent"></a>

##  post_journey_deployment_actionevent(deployment_id, body)



Sends an action event, which is used for changing the state of actions that have been offered to the user.

Wraps POST /api/v2/journey/deployments/{deploymentId}/actionevent 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.JourneyApi()
deployment_id = 'deployment_id_example' # str | The ID of the deployment sending the beacon.
body = PureCloudPlatformClientV2.ActionEventRequest() # ActionEventRequest | 

try:
    # Sends an action event, which is used for changing the state of actions that have been offered to the user.
    api_instance.post_journey_deployment_actionevent(deployment_id, body)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_deployment_actionevent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| The ID of the deployment sending the beacon. |  |
| **body** | [**ActionEventRequest**](ActionEventRequest.html)|  |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_journey_deployment_appevents"></a>

## [**AppEventResponse**](AppEventResponse.html) post_journey_deployment_appevents(deployment_id, body=body)



Send a journey app event, used for tracking customer activity on an application.

Wraps POST /api/v2/journey/deployments/{deploymentId}/appevents 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.JourneyApi()
deployment_id = 'deployment_id_example' # str | The ID of the deployment sending the app event.
body = PureCloudPlatformClientV2.AppEventRequest() # AppEventRequest |  (optional)

try:
    # Send a journey app event, used for tracking customer activity on an application.
    api_response = api_instance.post_journey_deployment_appevents(deployment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_deployment_appevents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| The ID of the deployment sending the app event. |  |
| **body** | [**AppEventRequest**](AppEventRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**AppEventResponse**](AppEventResponse.html)

<a name="post_journey_flows_paths_query"></a>

## [**FlowPaths**](FlowPaths.html) post_journey_flows_paths_query(body=body)



Query for flow paths.

post_journey_flows_paths_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/journey/flows/paths/query 

Requires ALL permissions: 

* journey:flowpaths:view

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
body = PureCloudPlatformClientV2.FlowPathsQuery() # FlowPathsQuery |  (optional)

try:
    # Query for flow paths.
    api_response = api_instance.post_journey_flows_paths_query(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_flows_paths_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowPathsQuery**](FlowPathsQuery.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**FlowPaths**](FlowPaths.html)

<a name="post_journey_outcomes"></a>

## [**Outcome**](Outcome.html) post_journey_outcomes(body=body)



Create an outcome.

Wraps POST /api/v2/journey/outcomes 

Requires ANY permissions: 

* journey:outcome:add

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
body = PureCloudPlatformClientV2.OutcomeRequest() # OutcomeRequest |  (optional)

try:
    # Create an outcome.
    api_response = api_instance.post_journey_outcomes(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_outcomes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OutcomeRequest**](OutcomeRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**Outcome**](Outcome.html)

<a name="post_journey_outcomes_attributions_jobs"></a>

## [**OutcomeAttributionAsyncResponse**](OutcomeAttributionAsyncResponse.html) post_journey_outcomes_attributions_jobs(body=body)



Create Outcome Attributions

post_journey_outcomes_attributions_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/journey/outcomes/attributions/jobs 

Requires ANY permissions: 

* journey:outcomeAttributionJob:add

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
body = PureCloudPlatformClientV2.OutcomeAttributionListing() # OutcomeAttributionListing | outcome attribution request (optional)

try:
    # Create Outcome Attributions
    api_response = api_instance.post_journey_outcomes_attributions_jobs(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_outcomes_attributions_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OutcomeAttributionListing**](OutcomeAttributionListing.html)| outcome attribution request | [optional]  |
{: class="table table-striped"}

### Return type

[**OutcomeAttributionAsyncResponse**](OutcomeAttributionAsyncResponse.html)

<a name="post_journey_outcomes_predictors"></a>

## [**OutcomePredictor**](OutcomePredictor.html) post_journey_outcomes_predictors(body=body)



Create an outcome predictor.

Wraps POST /api/v2/journey/outcomes/predictors 

Requires ANY permissions: 

* journey:outcomepredictor:add

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
body = PureCloudPlatformClientV2.OutcomePredictorRequest() # OutcomePredictorRequest |  (optional)

try:
    # Create an outcome predictor.
    api_response = api_instance.post_journey_outcomes_predictors(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_outcomes_predictors: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OutcomePredictorRequest**](OutcomePredictorRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**OutcomePredictor**](OutcomePredictor.html)

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
body = PureCloudPlatformClientV2.JourneySegmentRequest() # JourneySegmentRequest |  (optional)

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
| **body** | [**JourneySegmentRequest**](JourneySegmentRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**JourneySegment**](JourneySegment.html)

<a name="post_journey_view_versions"></a>

## [**JourneyView**](JourneyView.html) post_journey_view_versions(view_id, body)



Update a Journey View by ID

creates a new version

post_journey_view_versions is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/journey/views/{viewId}/versions 

Requires ALL permissions: 

* journey:views:edit

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
view_id = 'view_id_example' # str | viewId
body = PureCloudPlatformClientV2.JourneyView() # JourneyView | JourneyView

try:
    # Update a Journey View by ID
    api_response = api_instance.post_journey_view_versions(view_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_view_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| viewId |  |
| **body** | [**JourneyView**](JourneyView.html)| JourneyView |  |
{: class="table table-striped"}

### Return type

[**JourneyView**](JourneyView.html)

<a name="post_journey_views"></a>

## [**JourneyView**](JourneyView.html) post_journey_views(body)



Create a new Journey View

post_journey_views is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/journey/views 

Requires ALL permissions: 

* journey:views:add

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
body = PureCloudPlatformClientV2.JourneyView() # JourneyView | JourneyView

try:
    # Create a new Journey View
    api_response = api_instance.post_journey_views(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_views: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**JourneyView**](JourneyView.html)| JourneyView |  |
{: class="table table-striped"}

### Return type

[**JourneyView**](JourneyView.html)


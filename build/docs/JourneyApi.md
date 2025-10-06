# JourneyApi

## PureCloudPlatformClientV2.JourneyApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_analytics_journeys_aggregates_job**](#delete_analytics_journeys_aggregates_job) | Delete/cancel an async request for journey aggregates|
|[**delete_journey_actionmap**](#delete_journey_actionmap) | Delete single action map.|
|[**delete_journey_actiontemplate**](#delete_journey_actiontemplate) | Delete a single action template.|
|[**delete_journey_outcome**](#delete_journey_outcome) | Delete an outcome.|
|[**delete_journey_outcomes_predictor**](#delete_journey_outcomes_predictor) | Delete an outcome predictor.|
|[**delete_journey_segment**](#delete_journey_segment) | Delete a segment.|
|[**delete_journey_view**](#delete_journey_view) | Delete a Journey View by ID|
|[**delete_journey_view_schedules**](#delete_journey_view_schedules) | Delete the Schedule of a JourneyView|
|[**get_analytics_journeys_aggregates_job**](#get_analytics_journeys_aggregates_job) | Get status for async query for journey aggregates|
|[**get_analytics_journeys_aggregates_job_results**](#get_analytics_journeys_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_externalcontacts_contact_journey_segments**](#get_externalcontacts_contact_journey_segments) | Retrieve segment assignments by external contact ID.|
|[**get_externalcontacts_contact_journey_sessions**](#get_externalcontacts_contact_journey_sessions) | Retrieve all sessions for a given external contact.|
|[**get_journey_actionmap**](#get_journey_actionmap) | Retrieve a single action map.|
|[**get_journey_actionmaps**](#get_journey_actionmaps) | Retrieve all action maps.|
|[**get_journey_actionmaps_estimates_job**](#get_journey_actionmaps_estimates_job) | Get status of job.|
|[**get_journey_actionmaps_estimates_job_results**](#get_journey_actionmaps_estimates_job_results) | Get estimates from completed job.|
|[**get_journey_actiontarget**](#get_journey_actiontarget) | Retrieve a single action target.|
|[**get_journey_actiontargets**](#get_journey_actiontargets) | Retrieve all action targets.|
|[**get_journey_actiontemplate**](#get_journey_actiontemplate) | Retrieve a single action template.|
|[**get_journey_actiontemplates**](#get_journey_actiontemplates) | Retrieve all action templates.|
|[**get_journey_deployment_customer_ping**](#get_journey_deployment_customer_ping) | Send a ping.|
|[**get_journey_outcome**](#get_journey_outcome) | Retrieve a single outcome.|
|[**get_journey_outcomes**](#get_journey_outcomes) | Retrieve all outcomes.|
|[**get_journey_outcomes_attributions_job**](#get_journey_outcomes_attributions_job) | Get job status.|
|[**get_journey_outcomes_attributions_job_results**](#get_journey_outcomes_attributions_job_results) | Get outcome attribution entities from completed job.|
|[**get_journey_outcomes_predictor**](#get_journey_outcomes_predictor) | Retrieve a single outcome predictor.|
|[**get_journey_outcomes_predictors**](#get_journey_outcomes_predictors) | Retrieve all outcome predictors.|
|[**get_journey_segment**](#get_journey_segment) | Retrieve a single segment.|
|[**get_journey_segments**](#get_journey_segments) | Retrieve all segments.|
|[**get_journey_session**](#get_journey_session) | Retrieve a single session.|
|[**get_journey_session_events**](#get_journey_session_events) | Retrieve all events for a given session.|
|[**get_journey_session_outcomescores**](#get_journey_session_outcomescores) | Retrieve latest outcome score associated with a session for all outcomes.|
|[**get_journey_view**](#get_journey_view) | Get a Journey View by ID|
|[**get_journey_view_schedules**](#get_journey_view_schedules) | Get the Schedule for a JourneyView|
|[**get_journey_view_version**](#get_journey_view_version) | Get a Journey View by ID and version|
|[**get_journey_view_version_chart**](#get_journey_view_version_chart) | Get a Chart by ID|
|[**get_journey_view_version_chart_version**](#get_journey_view_version_chart_version) | Get a Chart by ID and version|
|[**get_journey_view_version_job**](#get_journey_view_version_job) | Get the job for a journey view version.|
|[**get_journey_view_version_job_results**](#get_journey_view_version_job_results) | Get the result of a job for a journey view version.|
|[**get_journey_view_version_job_results_chart**](#get_journey_view_version_job_results_chart) | Get the chart result associated with a journey view job.|
|[**get_journey_view_version_jobs_latest**](#get_journey_view_version_jobs_latest) | Get the latest job of a journey view version.|
|[**get_journey_views**](#get_journey_views) | Get a list of Journey Views|
|[**get_journey_views_data_details**](#get_journey_views_data_details) | Get details about the data available for journey queries including oldest and newest event dates|
|[**get_journey_views_eventdefinition**](#get_journey_views_eventdefinition) | Get an Event Definition|
|[**get_journey_views_eventdefinitions**](#get_journey_views_eventdefinitions) | Get a list of Event Definitions|
|[**get_journey_views_jobs**](#get_journey_views_jobs) | Get the jobs for an organization.|
|[**get_journey_views_jobs_me**](#get_journey_views_jobs_me) | Get my jobs|
|[**get_journey_views_schedules**](#get_journey_views_schedules) | Get the journey schedules for an organization.|
|[**patch_journey_actionmap**](#patch_journey_actionmap) | Update single action map.|
|[**patch_journey_actiontarget**](#patch_journey_actiontarget) | Update a single action target.|
|[**patch_journey_actiontemplate**](#patch_journey_actiontemplate) | Update a single action template.|
|[**patch_journey_outcome**](#patch_journey_outcome) | Update an outcome.|
|[**patch_journey_segment**](#patch_journey_segment) | Update a segment.|
|[**patch_journey_view_version_job**](#patch_journey_view_version_job) | Update the job for a journey view version. Only the status can be changed and only to Cancelled|
|[**post_analytics_journeys_aggregates_jobs**](#post_analytics_journeys_aggregates_jobs) | Query for journey aggregates asynchronously|
|[**post_analytics_journeys_aggregates_query**](#post_analytics_journeys_aggregates_query) | Query for journey aggregates|
|[**post_externalcontacts_contact_journey_segments**](#post_externalcontacts_contact_journey_segments) | Assign/Unassign up to 10 segments to/from an external contact or, if a segment is already assigned, update the expiry date of the segment assignment. Any unprocessed segment assignments are returned in the body for the client to retry, in the event of a partial success.|
|[**post_journey_actionmaps**](#post_journey_actionmaps) | Create an action map.|
|[**post_journey_actionmaps_estimates_jobs**](#post_journey_actionmaps_estimates_jobs) | Query for estimates|
|[**post_journey_actiontemplates**](#post_journey_actiontemplates) | Create a single action template.|
|[**post_journey_deployment_actionevent**](#post_journey_deployment_actionevent) | Sends an action event, which is used for changing the state of actions that have been offered to the user.|
|[**post_journey_deployment_appevents**](#post_journey_deployment_appevents) | Send a journey app event, used for tracking customer activity on an application.|
|[**post_journey_deployment_webevents**](#post_journey_deployment_webevents) | Send a journey web event, used for tracking customer activity on a website.|
|[**post_journey_flows_paths_query**](#post_journey_flows_paths_query) | Query for flow paths.|
|[**post_journey_outcomes**](#post_journey_outcomes) | Create an outcome.|
|[**post_journey_outcomes_attributions_jobs**](#post_journey_outcomes_attributions_jobs) | Create Outcome Attributions|
|[**post_journey_outcomes_predictors**](#post_journey_outcomes_predictors) | Create an outcome predictor.|
|[**post_journey_segments**](#post_journey_segments) | Create a segment.|
|[**post_journey_view_schedules**](#post_journey_view_schedules) | Add a new Schedule to a JourneyView|
|[**post_journey_view_version_jobs**](#post_journey_view_version_jobs) | Submit a job request for a journey view version.|
|[**post_journey_view_versions**](#post_journey_view_versions) | Update a Journey View by ID|
|[**post_journey_views**](#post_journey_views) | Create a new Journey View|
|[**post_journey_views_encodings_validate**](#post_journey_views_encodings_validate) | Validate whether an encoding exist for a label/value combination.|
|[**put_journey_view_schedules**](#put_journey_view_schedules) | Update the Schedule for a JourneyView|
|[**put_journey_view_version**](#put_journey_view_version) | Update a Journey View by ID and version|



## delete_analytics_journeys_aggregates_job

>  delete_analytics_journeys_aggregates_job(job_id)


Delete/cancel an async request for journey aggregates

delete_analytics_journeys_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/journeys/aggregates/jobs/{jobId} 

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
    # Delete/cancel an async request for journey aggregates
    api_instance.delete_analytics_journeys_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling JourneyApi->delete_analytics_journeys_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_journey_actionmap

>  delete_journey_actionmap(action_map_id)


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

### Return type

void (empty response body)


## delete_journey_actiontemplate

>  delete_journey_actiontemplate(action_template_id, hard_delete=hard_delete)


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

### Return type

void (empty response body)


## delete_journey_outcome

>  delete_journey_outcome(outcome_id)


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

### Return type

void (empty response body)


## delete_journey_outcomes_predictor

>  delete_journey_outcomes_predictor(predictor_id)


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

### Return type

void (empty response body)


## delete_journey_segment

>  delete_journey_segment(segment_id)


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

### Return type

void (empty response body)


## delete_journey_view

>  delete_journey_view(view_id)


Delete a Journey View by ID

deletes all versions

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

### Return type

void (empty response body)


## delete_journey_view_schedules

> [**JourneyViewSchedule**](JourneyViewSchedule) delete_journey_view_schedules(view_id)


Delete the Schedule of a JourneyView

Wraps DELETE /api/v2/journey/views/{viewId}/schedules 

Requires ALL permissions: 

* journey:viewsSchedule:delete

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
view_id = 'view_id_example' # str | Journey View Id

try:
    # Delete the Schedule of a JourneyView
    api_response = api_instance.delete_journey_view_schedules(view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->delete_journey_view_schedules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| Journey View Id |  |

### Return type

[**JourneyViewSchedule**](JourneyViewSchedule)


## get_analytics_journeys_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_journeys_aggregates_job(job_id)


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

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_journeys_aggregates_job_results

> [**JourneyAsyncAggregateQueryResponse**](JourneyAsyncAggregateQueryResponse) get_analytics_journeys_aggregates_job_results(job_id, cursor=cursor)


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

### Return type

[**JourneyAsyncAggregateQueryResponse**](JourneyAsyncAggregateQueryResponse)


## get_externalcontacts_contact_journey_segments

> [**SegmentAssignmentListing**](SegmentAssignmentListing) get_externalcontacts_contact_journey_segments(contact_id, include_merged=include_merged, limit=limit)


Retrieve segment assignments by external contact ID.

Wraps GET /api/v2/externalcontacts/contacts/{contactId}/journey/segments 

Requires ANY permissions: 

* externalContacts:segmentAssignment:view

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
include_merged = True # bool | Indicates whether to return segment assignments from all external contacts in the merge-set of the given one. (optional)
limit = 56 # int | Number of entities to return. Default of 25, maximum of 500. (optional)

try:
    # Retrieve segment assignments by external contact ID.
    api_response = api_instance.get_externalcontacts_contact_journey_segments(contact_id, include_merged=include_merged, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_externalcontacts_contact_journey_segments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |
| **include_merged** | **bool**| Indicates whether to return segment assignments from all external contacts in the merge-set of the given one. | [optional]  |
| **limit** | **int**| Number of entities to return. Default of 25, maximum of 500. | [optional]  |

### Return type

[**SegmentAssignmentListing**](SegmentAssignmentListing)


## get_externalcontacts_contact_journey_sessions

> [**SessionListing**](SessionListing) get_externalcontacts_contact_journey_sessions(contact_id, page_size=page_size, after=after, include_merged=include_merged)


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

### Return type

[**SessionListing**](SessionListing)


## get_journey_actionmap

> [**ActionMap**](ActionMap) get_journey_actionmap(action_map_id)


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

### Return type

[**ActionMap**](ActionMap)


## get_journey_actionmaps

> [**ActionMapListing**](ActionMapListing) get_journey_actionmaps(page_number=page_number, page_size=page_size, sort_by=sort_by, filter_field=filter_field, filter_value=filter_value, action_map_ids=action_map_ids, query_fields=query_fields, query_value=query_value)


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
| **action_map_ids** | [**list[str]**](str)| IDs of action maps to return. Use of this parameter is not compatible with pagination, filtering, sorting or querying. A maximum of 100 action maps are allowed per request. | [optional]  |
| **query_fields** | [**list[str]**](str)| Action Map field(s) to query on. Requires &#39;queryValue&#39; to also be set. | [optional]  |
| **query_value** | **str**| Value to query on. Requires &#39;queryFields&#39; to also be set. | [optional]  |

### Return type

[**ActionMapListing**](ActionMapListing)


## get_journey_actionmaps_estimates_job

> str** get_journey_actionmaps_estimates_job(job_id)


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

### Return type

**str**


## get_journey_actionmaps_estimates_job_results

> [**ActionMapEstimateResult**](ActionMapEstimateResult) get_journey_actionmaps_estimates_job_results(job_id)


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

### Return type

[**ActionMapEstimateResult**](ActionMapEstimateResult)


## get_journey_actiontarget

> [**ActionTarget**](ActionTarget) get_journey_actiontarget(action_target_id)


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

### Return type

[**ActionTarget**](ActionTarget)


## get_journey_actiontargets

> [**ActionTargetListing**](ActionTargetListing) get_journey_actiontargets(page_number=page_number, page_size=page_size)


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

### Return type

[**ActionTargetListing**](ActionTargetListing)


## get_journey_actiontemplate

> [**ActionTemplate**](ActionTemplate) get_journey_actiontemplate(action_template_id)


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

### Return type

[**ActionTemplate**](ActionTemplate)


## get_journey_actiontemplates

> [**ActionTemplateListing**](ActionTemplateListing) get_journey_actiontemplates(page_number=page_number, page_size=page_size, sort_by=sort_by, media_type=media_type, state=state, query_fields=query_fields, query_value=query_value)


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
| **query_fields** | [**list[str]**](str)| ActionTemplate field(s) to query on. Requires &#39;queryValue&#39; to also be set. | [optional]  |
| **query_value** | **str**| Value to query on. Requires &#39;queryFields&#39; to also be set. | [optional]  |

### Return type

[**ActionTemplateListing**](ActionTemplateListing)


## get_journey_deployment_customer_ping

> [**DeploymentPing**](DeploymentPing) get_journey_deployment_customer_ping(deployment_id, customer_cookie_id, dl=dl, dt=dt, app_namespace=app_namespace, session_id=session_id, since_last_beacon_milliseconds=since_last_beacon_milliseconds)


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

### Return type

[**DeploymentPing**](DeploymentPing)


## get_journey_outcome

> [**Outcome**](Outcome) get_journey_outcome(outcome_id)


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

### Return type

[**Outcome**](Outcome)


## get_journey_outcomes

> [**OutcomeListing**](OutcomeListing) get_journey_outcomes(page_number=page_number, page_size=page_size, sort_by=sort_by, outcome_ids=outcome_ids, query_fields=query_fields, query_value=query_value)


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
| **outcome_ids** | [**list[str]**](str)| IDs of outcomes to return. Use of this parameter is not compatible with pagination, sorting or querying. A maximum of 20 outcomes are allowed per request. | [optional]  |
| **query_fields** | [**list[str]**](str)| Outcome field(s) to query on. Requires &#39;queryValue&#39; to also be set. | [optional]  |
| **query_value** | **str**| Value to query on. Requires &#39;queryFields&#39; to also be set. | [optional]  |

### Return type

[**OutcomeListing**](OutcomeListing)


## get_journey_outcomes_attributions_job

> [**OutcomeAttributionJobStateResponse**](OutcomeAttributionJobStateResponse) get_journey_outcomes_attributions_job(job_id)


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

### Return type

[**OutcomeAttributionJobStateResponse**](OutcomeAttributionJobStateResponse)


## get_journey_outcomes_attributions_job_results

> [**OutcomeAttributionResponseListing**](OutcomeAttributionResponseListing) get_journey_outcomes_attributions_job_results(job_id)


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

### Return type

[**OutcomeAttributionResponseListing**](OutcomeAttributionResponseListing)


## get_journey_outcomes_predictor

> [**OutcomePredictor**](OutcomePredictor) get_journey_outcomes_predictor(predictor_id)


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

### Return type

[**OutcomePredictor**](OutcomePredictor)


## get_journey_outcomes_predictors

> [**OutcomePredictorListing**](OutcomePredictorListing) get_journey_outcomes_predictors()


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

[**OutcomePredictorListing**](OutcomePredictorListing)


## get_journey_segment

> [**JourneySegment**](JourneySegment) get_journey_segment(segment_id)


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

### Return type

[**JourneySegment**](JourneySegment)


## get_journey_segments

> [**SegmentListing**](SegmentListing) get_journey_segments(sort_by=sort_by, page_size=page_size, page_number=page_number, is_active=is_active, segment_ids=segment_ids, query_fields=query_fields, query_value=query_value)


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
| **segment_ids** | [**list[str]**](str)| IDs of segments to return. Use of this parameter is not compatible with pagination, sorting or querying. A maximum of 100 segments are allowed per request. | [optional]  |
| **query_fields** | [**list[str]**](str)| Segment field(s) to query on. Requires &#39;queryValue&#39; to also be set. | [optional]  |
| **query_value** | **str**| Value to query on. Requires &#39;queryFields&#39; to also be set. | [optional]  |

### Return type

[**SegmentListing**](SegmentListing)


## get_journey_session

> [**Session**](Session) get_journey_session(session_id)


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

### Return type

[**Session**](Session)


## get_journey_session_events

> [**EventListing**](EventListing) get_journey_session_events(session_id, page_size=page_size, after=after, event_type=event_type)


Retrieve all events for a given session.

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
event_type = 'event_type_example' # str | A comma separated list of journey event types to include in the results. (optional)

try:
    # Retrieve all events for a given session.
    api_response = api_instance.get_journey_session_events(session_id, page_size=page_size, after=after, event_type=event_type)
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
| **event_type** | **str**| A comma separated list of journey event types to include in the results. | [optional] <br />**Values**: com.genesys.journey.OutcomeAchievedEvent, com.genesys.journey.SegmentAssignmentEvent, com.genesys.journey.WebActionEvent, com.genesys.journey.WebEvent, com.genesys.journey.AppEvent |

### Return type

[**EventListing**](EventListing)


## get_journey_session_outcomescores

> [**OutcomeScoresResult**](OutcomeScoresResult) get_journey_session_outcomescores(session_id)


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

### Return type

[**OutcomeScoresResult**](OutcomeScoresResult)


## get_journey_view

> [**JourneyView**](JourneyView) get_journey_view(view_id)


Get a Journey View by ID

returns the latest version

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

### Return type

[**JourneyView**](JourneyView)


## get_journey_view_schedules

> [**JourneyViewSchedule**](JourneyViewSchedule) get_journey_view_schedules(view_id)


Get the Schedule for a JourneyView

Wraps GET /api/v2/journey/views/{viewId}/schedules 

Requires ALL permissions: 

* journey:viewsSchedule:view

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
view_id = 'view_id_example' # str | Journey View Id

try:
    # Get the Schedule for a JourneyView
    api_response = api_instance.get_journey_view_schedules(view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_view_schedules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| Journey View Id |  |

### Return type

[**JourneyViewSchedule**](JourneyViewSchedule)


## get_journey_view_version

> [**JourneyView**](JourneyView) get_journey_view_version(view_id, version_id)


Get a Journey View by ID and version

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

### Return type

[**JourneyView**](JourneyView)


## get_journey_view_version_chart

> [**JourneyViewChart**](JourneyViewChart) get_journey_view_version_chart(view_id, journey_view_version, chart_id)


Get a Chart by ID

returns the latest version

Wraps GET /api/v2/journey/views/{viewId}/versions/{journeyViewVersion}/charts/{chartId} 

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
journey_view_version = 'journey_view_version_example' # str | Journey View Version
chart_id = 'chart_id_example' # str | chartId

try:
    # Get a Chart by ID
    api_response = api_instance.get_journey_view_version_chart(view_id, journey_view_version, chart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_view_version_chart: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| viewId |  |
| **journey_view_version** | **str**| Journey View Version |  |
| **chart_id** | **str**| chartId |  |

### Return type

[**JourneyViewChart**](JourneyViewChart)


## get_journey_view_version_chart_version

> [**JourneyViewChart**](JourneyViewChart) get_journey_view_version_chart_version(view_id, journey_view_version, chart_id, chart_version)


Get a Chart by ID and version

Wraps GET /api/v2/journey/views/{viewId}/versions/{journeyViewVersion}/charts/{chartId}/versions/{chartVersion} 

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
journey_view_version = 'journey_view_version_example' # str | Journey View Version
chart_id = 'chart_id_example' # str | chartId
chart_version = 'chart_version_example' # str | chartVersion

try:
    # Get a Chart by ID and version
    api_response = api_instance.get_journey_view_version_chart_version(view_id, journey_view_version, chart_id, chart_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_view_version_chart_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| viewId |  |
| **journey_view_version** | **str**| Journey View Version |  |
| **chart_id** | **str**| chartId |  |
| **chart_version** | **str**| chartVersion |  |

### Return type

[**JourneyViewChart**](JourneyViewChart)


## get_journey_view_version_job

> [**JourneyViewJob**](JourneyViewJob) get_journey_view_version_job(view_id, journey_version_id, job_id)


Get the job for a journey view version.

Wraps GET /api/v2/journey/views/{viewId}/versions/{journeyVersionId}/jobs/{jobId} 

Requires ALL permissions: 

* journey:viewsJobs:view

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
view_id = 'view_id_example' # str | Journey View Id
journey_version_id = 'journey_version_id_example' # str | Journey View Version
job_id = 'job_id_example' # str | JobId

try:
    # Get the job for a journey view version.
    api_response = api_instance.get_journey_view_version_job(view_id, journey_version_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_view_version_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| Journey View Id |  |
| **journey_version_id** | **str**| Journey View Version |  |
| **job_id** | **str**| JobId |  |

### Return type

[**JourneyViewJob**](JourneyViewJob)


## get_journey_view_version_job_results

> [**JourneyViewResult**](JourneyViewResult) get_journey_view_version_job_results(view_id, journey_view_version, job_id)


Get the result of a job for a journey view version.

Wraps GET /api/v2/journey/views/{viewId}/versions/{journeyViewVersion}/jobs/{jobId}/results 

Requires ALL permissions: 

* journey:viewsResults:view

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
view_id = 'view_id_example' # str | JourneyViewResult id
journey_view_version = 'journey_view_version_example' # str | Journey View Version
job_id = 'job_id_example' # str | Id of the executing job

try:
    # Get the result of a job for a journey view version.
    api_response = api_instance.get_journey_view_version_job_results(view_id, journey_view_version, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_view_version_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| JourneyViewResult id |  |
| **journey_view_version** | **str**| Journey View Version |  |
| **job_id** | **str**| Id of the executing job |  |

### Return type

[**JourneyViewResult**](JourneyViewResult)


## get_journey_view_version_job_results_chart

> [**JourneyViewChartResult**](JourneyViewChartResult) get_journey_view_version_job_results_chart(view_id, journey_version_id, job_id, chart_id)


Get the chart result associated with a journey view job.

Wraps GET /api/v2/journey/views/{viewId}/versions/{journeyVersionId}/jobs/{jobId}/results/charts/{chartId} 

Requires ALL permissions: 

* journey:viewsResults:view

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
view_id = 'view_id_example' # str | Journey View Id
journey_version_id = 'journey_version_id_example' # str | Journey View Version
job_id = 'job_id_example' # str | JobId
chart_id = 'chart_id_example' # str | ChartId

try:
    # Get the chart result associated with a journey view job.
    api_response = api_instance.get_journey_view_version_job_results_chart(view_id, journey_version_id, job_id, chart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_view_version_job_results_chart: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| Journey View Id |  |
| **journey_version_id** | **str**| Journey View Version |  |
| **job_id** | **str**| JobId |  |
| **chart_id** | **str**| ChartId |  |

### Return type

[**JourneyViewChartResult**](JourneyViewChartResult)


## get_journey_view_version_jobs_latest

> [**JourneyViewJob**](JourneyViewJob) get_journey_view_version_jobs_latest(view_id, journey_version_id)


Get the latest job of a journey view version.

Wraps GET /api/v2/journey/views/{viewId}/versions/{journeyVersionId}/jobs/latest 

Requires ALL permissions: 

* journey:viewsJobs:view

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
view_id = 'view_id_example' # str | Journey View Id
journey_version_id = 'journey_version_id_example' # str | Journey View Version

try:
    # Get the latest job of a journey view version.
    api_response = api_instance.get_journey_view_version_jobs_latest(view_id, journey_version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_view_version_jobs_latest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| Journey View Id |  |
| **journey_version_id** | **str**| Journey View Version |  |

### Return type

[**JourneyViewJob**](JourneyViewJob)


## get_journey_views

> [**JourneyViewListing**](JourneyViewListing) get_journey_views(page_number=page_number, page_size=page_size, name_or_created_by=name_or_created_by, expand=expand, id=id)


Get a list of Journey Views

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
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
name_or_created_by = 'name_or_created_by_example' # str | Journey View Name or Created By (optional)
expand = 'expand_example' # str | Parameter to request additional data to return in Journey payload (optional)
id = 'id_example' # str | Parameter to request a list of Journey Views by id, separated by commas. Limit of 100 items. (optional)

try:
    # Get a list of Journey Views
    api_response = api_instance.get_journey_views(page_number=page_number, page_size=page_size, name_or_created_by=name_or_created_by, expand=expand, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_views: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **name_or_created_by** | **str**| Journey View Name or Created By | [optional]  |
| **expand** | **str**| Parameter to request additional data to return in Journey payload | [optional] <br />**Values**: charts |
| **id** | **str**| Parameter to request a list of Journey Views by id, separated by commas. Limit of 100 items. | [optional]  |

### Return type

[**JourneyViewListing**](JourneyViewListing)


## get_journey_views_data_details

> [**DataRange**](DataRange) get_journey_views_data_details()


Get details about the data available for journey queries including oldest and newest event dates

Wraps GET /api/v2/journey/views/data/details 

Requires ALL permissions: 

* journey:dataDetails:view

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
    # Get details about the data available for journey queries including oldest and newest event dates
    api_response = api_instance.get_journey_views_data_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_views_data_details: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**DataRange**](DataRange)


## get_journey_views_eventdefinition

> [**JourneyEventDefinition**](JourneyEventDefinition) get_journey_views_eventdefinition(event_definition_id)


Get an Event Definition

Wraps GET /api/v2/journey/views/eventdefinitions/{eventDefinitionId} 

Requires ALL permissions: 

* journey:eventDefinition:view

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
event_definition_id = 'event_definition_id_example' # str | Event Definition ID

try:
    # Get an Event Definition
    api_response = api_instance.get_journey_views_eventdefinition(event_definition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_views_eventdefinition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **event_definition_id** | **str**| Event Definition ID |  |

### Return type

[**JourneyEventDefinition**](JourneyEventDefinition)


## get_journey_views_eventdefinitions

> [**JourneyEventDefinitionListing**](JourneyEventDefinitionListing) get_journey_views_eventdefinitions()


Get a list of Event Definitions

Wraps GET /api/v2/journey/views/eventdefinitions 

Requires ALL permissions: 

* journey:eventDefinition:view

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
    # Get a list of Event Definitions
    api_response = api_instance.get_journey_views_eventdefinitions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_views_eventdefinitions: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**JourneyEventDefinitionListing**](JourneyEventDefinitionListing)


## get_journey_views_jobs

> [**JourneyViewJobListing**](JourneyViewJobListing) get_journey_views_jobs(page_number=page_number, page_size=page_size, interval=interval, statuses=statuses)


Get the jobs for an organization.

Wraps GET /api/v2/journey/views/jobs 

Requires ALL permissions: 

* journey:viewsJobs:view

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
page_number = 1 # int | The number of the page to return (optional) (default to 1)
page_size = 25 # int | Max number of entities to return (optional) (default to 25)
interval = '2023-07-17T00:00:00Z/2023-07-18T00:00:00Z' # str | An absolute timeframe for filtering the jobs, expressed as an ISO 8601 interval. (optional)
statuses = 'statuses=Accepted,Executing,Complete,Failed,Scheduled' # str | Job statuses to filter for (optional)

try:
    # Get the jobs for an organization.
    api_response = api_instance.get_journey_views_jobs(page_number=page_number, page_size=page_size, interval=interval, statuses=statuses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_views_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| The number of the page to return | [optional] [default to 1] |
| **page_size** | **int**| Max number of entities to return | [optional] [default to 25] |
| **interval** | **str**| An absolute timeframe for filtering the jobs, expressed as an ISO 8601 interval. | [optional]  |
| **statuses** | **str**| Job statuses to filter for | [optional]  |

### Return type

[**JourneyViewJobListing**](JourneyViewJobListing)


## get_journey_views_jobs_me

> [**JourneyViewJobListing**](JourneyViewJobListing) get_journey_views_jobs_me(page_number=page_number, page_size=page_size, interval=interval, statuses=statuses)


Get my jobs

Wraps GET /api/v2/journey/views/jobs/me 

Requires ALL permissions: 

* journey:viewsJobs:view

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
page_number = 1 # int | The number of the page to return (optional) (default to 1)
page_size = 25 # int | Max number of entities to return (optional) (default to 25)
interval = '2023-07-17T00:00:00Z/2023-07-18T00:00:00Z' # str | An absolute timeframe for filtering the jobs, expressed as an ISO 8601 interval. (optional)
statuses = 'statuses=Accepted,Executing,Complete,Failed,Scheduled' # str | Job statuses to filter for (optional)

try:
    # Get my jobs
    api_response = api_instance.get_journey_views_jobs_me(page_number=page_number, page_size=page_size, interval=interval, statuses=statuses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_views_jobs_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| The number of the page to return | [optional] [default to 1] |
| **page_size** | **int**| Max number of entities to return | [optional] [default to 25] |
| **interval** | **str**| An absolute timeframe for filtering the jobs, expressed as an ISO 8601 interval. | [optional]  |
| **statuses** | **str**| Job statuses to filter for | [optional]  |

### Return type

[**JourneyViewJobListing**](JourneyViewJobListing)


## get_journey_views_schedules

> [**JourneyViewScheduleListing**](JourneyViewScheduleListing) get_journey_views_schedules(page_number=page_number, page_size=page_size)


Get the journey schedules for an organization.

Wraps GET /api/v2/journey/views/schedules 

Requires ALL permissions: 

* journey:viewsSchedule:view

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
page_number = 1 # int | The number of the page to return (optional) (default to 1)
page_size = 25 # int | Max number of entities to return (optional) (default to 25)

try:
    # Get the journey schedules for an organization.
    api_response = api_instance.get_journey_views_schedules(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->get_journey_views_schedules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| The number of the page to return | [optional] [default to 1] |
| **page_size** | **int**| Max number of entities to return | [optional] [default to 25] |

### Return type

[**JourneyViewScheduleListing**](JourneyViewScheduleListing)


## patch_journey_actionmap

> [**ActionMap**](ActionMap) patch_journey_actionmap(action_map_id, body=body)


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
| **body** | [**PatchActionMap**](PatchActionMap)|  | [optional]  |

### Return type

[**ActionMap**](ActionMap)


## patch_journey_actiontarget

> [**ActionTarget**](ActionTarget) patch_journey_actiontarget(action_target_id, body=body)


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
| **body** | [**PatchActionTarget**](PatchActionTarget)|  | [optional]  |

### Return type

[**ActionTarget**](ActionTarget)


## patch_journey_actiontemplate

> [**ActionTemplate**](ActionTemplate) patch_journey_actiontemplate(action_template_id, body=body)


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
| **body** | [**PatchActionTemplate**](PatchActionTemplate)|  | [optional]  |

### Return type

[**ActionTemplate**](ActionTemplate)


## patch_journey_outcome

> [**Outcome**](Outcome) patch_journey_outcome(outcome_id, body=body)


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
| **body** | [**PatchOutcome**](PatchOutcome)|  | [optional]  |

### Return type

[**Outcome**](Outcome)


## patch_journey_segment

> [**JourneySegment**](JourneySegment) patch_journey_segment(segment_id, body=body)


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
| **body** | [**PatchSegment**](PatchSegment)|  | [optional]  |

### Return type

[**JourneySegment**](JourneySegment)


## patch_journey_view_version_job

> [**JourneyViewJob**](JourneyViewJob) patch_journey_view_version_job(view_id, journey_version_id, job_id, body)


Update the job for a journey view version. Only the status can be changed and only to Cancelled

Wraps PATCH /api/v2/journey/views/{viewId}/versions/{journeyVersionId}/jobs/{jobId} 

Requires ALL permissions: 

* journey:viewsJobs:edit

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
view_id = 'view_id_example' # str | Journey View Id
journey_version_id = 'journey_version_id_example' # str | Journey View Version
job_id = 'job_id_example' # str | JobId
body = PureCloudPlatformClientV2.JourneyViewJob() # JourneyViewJob | journeyViewJob

try:
    # Update the job for a journey view version. Only the status can be changed and only to Cancelled
    api_response = api_instance.patch_journey_view_version_job(view_id, journey_version_id, job_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->patch_journey_view_version_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| Journey View Id |  |
| **journey_version_id** | **str**| Journey View Version |  |
| **job_id** | **str**| JobId |  |
| **body** | [**JourneyViewJob**](JourneyViewJob)| journeyViewJob |  |

### Return type

[**JourneyViewJob**](JourneyViewJob)


## post_analytics_journeys_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_journeys_aggregates_jobs(body)


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
| **body** | [**JourneyAsyncAggregationQuery**](JourneyAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_journeys_aggregates_query

> [**JourneyAggregateQueryResponse**](JourneyAggregateQueryResponse) post_analytics_journeys_aggregates_query(body)


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
| **body** | [**JourneyAggregationQuery**](JourneyAggregationQuery)| query |  |

### Return type

[**JourneyAggregateQueryResponse**](JourneyAggregateQueryResponse)


## post_externalcontacts_contact_journey_segments

> [**UpdateSegmentAssignmentResponse**](UpdateSegmentAssignmentResponse) post_externalcontacts_contact_journey_segments(contact_id, body=body)


Assign/Unassign up to 10 segments to/from an external contact or, if a segment is already assigned, update the expiry date of the segment assignment. Any unprocessed segment assignments are returned in the body for the client to retry, in the event of a partial success.

Wraps POST /api/v2/externalcontacts/contacts/{contactId}/journey/segments 

Requires ANY permissions: 

* externalContacts:segmentAssignment:add
* externalContacts:segmentAssignment:delete

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
body = PureCloudPlatformClientV2.UpdateSegmentAssignmentRequest() # UpdateSegmentAssignmentRequest |  (optional)

try:
    # Assign/Unassign up to 10 segments to/from an external contact or, if a segment is already assigned, update the expiry date of the segment assignment. Any unprocessed segment assignments are returned in the body for the client to retry, in the event of a partial success.
    api_response = api_instance.post_externalcontacts_contact_journey_segments(contact_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_externalcontacts_contact_journey_segments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contact_id** | **str**| ExternalContact ID |  |
| **body** | [**UpdateSegmentAssignmentRequest**](UpdateSegmentAssignmentRequest)|  | [optional]  |

### Return type

[**UpdateSegmentAssignmentResponse**](UpdateSegmentAssignmentResponse)


## post_journey_actionmaps

> [**ActionMap**](ActionMap) post_journey_actionmaps(body=body)


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
| **body** | [**ActionMap**](ActionMap)|  | [optional]  |

### Return type

[**ActionMap**](ActionMap)


## post_journey_actionmaps_estimates_jobs

> [**EstimateJobAsyncResponse**](EstimateJobAsyncResponse) post_journey_actionmaps_estimates_jobs(body)


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
| **body** | [**ActionMapEstimateRequest**](ActionMapEstimateRequest)| audience estimator request |  |

### Return type

[**EstimateJobAsyncResponse**](EstimateJobAsyncResponse)


## post_journey_actiontemplates

> [**ActionTemplate**](ActionTemplate) post_journey_actiontemplates(body=body)


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
| **body** | [**ActionTemplate**](ActionTemplate)|  | [optional]  |

### Return type

[**ActionTemplate**](ActionTemplate)


## post_journey_deployment_actionevent

>  post_journey_deployment_actionevent(deployment_id, body)


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
| **body** | [**ActionEventRequest**](ActionEventRequest)|  |  |

### Return type

void (empty response body)


## post_journey_deployment_appevents

> [**AppEventResponse**](AppEventResponse) post_journey_deployment_appevents(deployment_id, body=body)


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
| **body** | [**AppEventRequest**](AppEventRequest)|  | [optional]  |

### Return type

[**AppEventResponse**](AppEventResponse)


## post_journey_deployment_webevents

> [**WebEventResponse**](WebEventResponse) post_journey_deployment_webevents(deployment_id, body=body)


Send a journey web event, used for tracking customer activity on a website.

Wraps POST /api/v2/journey/deployments/{deploymentId}/webevents 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.JourneyApi()
deployment_id = 'deployment_id_example' # str | The ID of the deployment sending the web event.
body = PureCloudPlatformClientV2.WebEventRequest() # WebEventRequest |  (optional)

try:
    # Send a journey web event, used for tracking customer activity on a website.
    api_response = api_instance.post_journey_deployment_webevents(deployment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_deployment_webevents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| The ID of the deployment sending the web event. |  |
| **body** | [**WebEventRequest**](WebEventRequest)|  | [optional]  |

### Return type

[**WebEventResponse**](WebEventResponse)


## post_journey_flows_paths_query

> [**FlowPaths**](FlowPaths) post_journey_flows_paths_query(body=body)


Query for flow paths.

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
| **body** | [**FlowPathsQuery**](FlowPathsQuery)|  | [optional]  |

### Return type

[**FlowPaths**](FlowPaths)


## post_journey_outcomes

> [**Outcome**](Outcome) post_journey_outcomes(body=body)


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
| **body** | [**OutcomeRequest**](OutcomeRequest)|  | [optional]  |

### Return type

[**Outcome**](Outcome)


## post_journey_outcomes_attributions_jobs

> [**OutcomeAttributionAsyncResponse**](OutcomeAttributionAsyncResponse) post_journey_outcomes_attributions_jobs(body=body)


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
| **body** | [**OutcomeAttributionListing**](OutcomeAttributionListing)| outcome attribution request | [optional]  |

### Return type

[**OutcomeAttributionAsyncResponse**](OutcomeAttributionAsyncResponse)


## post_journey_outcomes_predictors

> [**OutcomePredictor**](OutcomePredictor) post_journey_outcomes_predictors(body=body)


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
| **body** | [**OutcomePredictorRequest**](OutcomePredictorRequest)|  | [optional]  |

### Return type

[**OutcomePredictor**](OutcomePredictor)


## post_journey_segments

> [**JourneySegment**](JourneySegment) post_journey_segments(body=body)


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
| **body** | [**JourneySegmentRequest**](JourneySegmentRequest)|  | [optional]  |

### Return type

[**JourneySegment**](JourneySegment)


## post_journey_view_schedules

> [**JourneyViewSchedule**](JourneyViewSchedule) post_journey_view_schedules(view_id, body)


Add a new Schedule to a JourneyView

Wraps POST /api/v2/journey/views/{viewId}/schedules 

Requires ALL permissions: 

* journey:viewsSchedule:add

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
view_id = 'view_id_example' # str | Journey View Id
body = PureCloudPlatformClientV2.JourneyViewSchedule() # JourneyViewSchedule | journeyViewSchedule

try:
    # Add a new Schedule to a JourneyView
    api_response = api_instance.post_journey_view_schedules(view_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_view_schedules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| Journey View Id |  |
| **body** | [**JourneyViewSchedule**](JourneyViewSchedule)| journeyViewSchedule |  |

### Return type

[**JourneyViewSchedule**](JourneyViewSchedule)


## post_journey_view_version_jobs

> [**JourneyViewJob**](JourneyViewJob) post_journey_view_version_jobs(view_id, journey_version_id)


Submit a job request for a journey view version.

Wraps POST /api/v2/journey/views/{viewId}/versions/{journeyVersionId}/jobs 

Requires ALL permissions: 

* journey:viewsJobs:add

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
view_id = 'view_id_example' # str | Journey View Id
journey_version_id = 'journey_version_id_example' # str | Journey View Version

try:
    # Submit a job request for a journey view version.
    api_response = api_instance.post_journey_view_version_jobs(view_id, journey_version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_view_version_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| Journey View Id |  |
| **journey_version_id** | **str**| Journey View Version |  |

### Return type

[**JourneyViewJob**](JourneyViewJob)


## post_journey_view_versions

> [**JourneyView**](JourneyView) post_journey_view_versions(view_id, body)


Update a Journey View by ID

creates a new version

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
| **body** | [**JourneyView**](JourneyView)| JourneyView |  |

### Return type

[**JourneyView**](JourneyView)


## post_journey_views

> [**JourneyView**](JourneyView) post_journey_views(body)


Create a new Journey View

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
| **body** | [**JourneyView**](JourneyView)| JourneyView |  |

### Return type

[**JourneyView**](JourneyView)


## post_journey_views_encodings_validate

> [**EntityListing**](EntityListing) post_journey_views_encodings_validate(body=body)


Validate whether an encoding exist for a label/value combination.

True indicates a valid encoding

Wraps POST /api/v2/journey/views/encodings/validate 

Requires ALL permissions: 

* journey:viewsEncodings:view

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
body = [PureCloudPlatformClientV2.Label()] # list[Label] |  (optional)

try:
    # Validate whether an encoding exist for a label/value combination.
    api_response = api_instance.post_journey_views_encodings_validate(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->post_journey_views_encodings_validate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**list[Label]**](Label)|  | [optional]  |

### Return type

[**EntityListing**](EntityListing)


## put_journey_view_schedules

> [**JourneyViewSchedule**](JourneyViewSchedule) put_journey_view_schedules(view_id, body)


Update the Schedule for a JourneyView

Wraps PUT /api/v2/journey/views/{viewId}/schedules 

Requires ALL permissions: 

* journey:viewsSchedule:edit

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
view_id = 'view_id_example' # str | Journey View Id
body = PureCloudPlatformClientV2.JourneyViewSchedule() # JourneyViewSchedule | journeyViewSchedule

try:
    # Update the Schedule for a JourneyView
    api_response = api_instance.put_journey_view_schedules(view_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->put_journey_view_schedules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| Journey View Id |  |
| **body** | [**JourneyViewSchedule**](JourneyViewSchedule)| journeyViewSchedule |  |

### Return type

[**JourneyViewSchedule**](JourneyViewSchedule)


## put_journey_view_version

> [**JourneyView**](JourneyView) put_journey_view_version(view_id, version_id, body)


Update a Journey View by ID and version

does not create a new version

Wraps PUT /api/v2/journey/views/{viewId}/versions/{versionId} 

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
version_id = 'version_id_example' # str | versionId
body = PureCloudPlatformClientV2.JourneyView() # JourneyView | JourneyView

try:
    # Update a Journey View by ID and version
    api_response = api_instance.put_journey_view_version(view_id, version_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyApi->put_journey_view_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **view_id** | **str**| viewId |  |
| **version_id** | **str**| versionId |  |
| **body** | [**JourneyView**](JourneyView)| JourneyView |  |

### Return type

[**JourneyView**](JourneyView)


_PureCloudPlatformClientV2 240.0.0_

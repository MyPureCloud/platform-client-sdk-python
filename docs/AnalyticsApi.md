# AnalyticsApi

## PureCloudPlatformClientV2.AnalyticsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_analytics_actions_aggregates_job**](#delete_analytics_actions_aggregates_job) | Delete/cancel an async request for action aggregates|
|[**delete_analytics_agentcopilots_aggregates_job**](#delete_analytics_agentcopilots_aggregates_job) | Delete/cancel an async request for agent copilot aggregates|
|[**delete_analytics_bots_aggregates_job**](#delete_analytics_bots_aggregates_job) | Delete/cancel an async request for bot aggregates|
|[**delete_analytics_casemanagement_aggregates_job**](#delete_analytics_casemanagement_aggregates_job) | Delete/cancel an async request for case management aggregates|
|[**delete_analytics_conversations_aggregates_job**](#delete_analytics_conversations_aggregates_job) | Delete/cancel an async request for conversation aggregates|
|[**delete_analytics_conversations_details_job**](#delete_analytics_conversations_details_job) | Delete/cancel an async details job|
|[**delete_analytics_evaluations_aggregates_job**](#delete_analytics_evaluations_aggregates_job) | Delete/cancel an async request for evaluation aggregates|
|[**delete_analytics_flowexecutions_aggregates_job**](#delete_analytics_flowexecutions_aggregates_job) | Delete/cancel an async request for flow execution aggregates|
|[**delete_analytics_flows_aggregates_job**](#delete_analytics_flows_aggregates_job) | Delete/cancel an async request for flow aggregates|
|[**delete_analytics_journeys_aggregates_job**](#delete_analytics_journeys_aggregates_job) | Delete/cancel an async request for journey aggregates|
|[**delete_analytics_knowledge_aggregates_job**](#delete_analytics_knowledge_aggregates_job) | Delete/cancel an async request for knowledge aggregates|
|[**delete_analytics_resolutions_aggregates_job**](#delete_analytics_resolutions_aggregates_job) | Delete/cancel an async request for resolution aggregates|
|[**delete_analytics_summaries_aggregates_job**](#delete_analytics_summaries_aggregates_job) | Delete/cancel an async request for summary aggregates|
|[**delete_analytics_surveys_aggregates_job**](#delete_analytics_surveys_aggregates_job) | Delete/cancel an async request for survey aggregates|
|[**delete_analytics_taskmanagement_aggregates_job**](#delete_analytics_taskmanagement_aggregates_job) | Delete/cancel an async request for task management aggregates|
|[**delete_analytics_transcripts_aggregates_job**](#delete_analytics_transcripts_aggregates_job) | Delete/cancel an async request for transcript aggregates|
|[**delete_analytics_users_aggregates_job**](#delete_analytics_users_aggregates_job) | Delete/cancel an async request for user aggregates|
|[**delete_analytics_users_details_job**](#delete_analytics_users_details_job) | Delete/cancel an async request|
|[**get_analytics_actions_aggregates_job**](#get_analytics_actions_aggregates_job) | Get status for async query for action aggregates|
|[**get_analytics_actions_aggregates_job_results**](#get_analytics_actions_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_agent_status**](#get_analytics_agent_status) | Get an agent and their active sessions by user ID|
|[**get_analytics_agentcopilots_aggregates_job**](#get_analytics_agentcopilots_aggregates_job) | Get status for async query for agent copilot aggregates|
|[**get_analytics_agentcopilots_aggregates_job_results**](#get_analytics_agentcopilots_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_botflow_divisions_reportingturns**](#get_analytics_botflow_divisions_reportingturns) | Get Reporting Turns (division aware).|
|[**get_analytics_botflow_reportingturns**](#get_analytics_botflow_reportingturns) | Get Reporting Turns.|
|[**get_analytics_botflow_sessions**](#get_analytics_botflow_sessions) | Get Bot Flow Sessions.|
|[**get_analytics_bots_aggregates_job**](#get_analytics_bots_aggregates_job) | Get status for async query for bot aggregates|
|[**get_analytics_bots_aggregates_job_results**](#get_analytics_bots_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_casemanagement_aggregates_job**](#get_analytics_casemanagement_aggregates_job) | Get status for async query for case management aggregates|
|[**get_analytics_casemanagement_aggregates_job_results**](#get_analytics_casemanagement_aggregates_job_results) | Fetch a page of results for an async case management query|
|[**get_analytics_conversation_details**](#get_analytics_conversation_details) | Get a conversation by id|
|[**get_analytics_conversations_aggregates_job**](#get_analytics_conversations_aggregates_job) | Get status for async query for conversation aggregates|
|[**get_analytics_conversations_aggregates_job_results**](#get_analytics_conversations_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_conversations_details**](#get_analytics_conversations_details) | Gets multiple conversations by id|
|[**get_analytics_conversations_details_job**](#get_analytics_conversations_details_job) | Get status for async query for conversation details|
|[**get_analytics_conversations_details_job_results**](#get_analytics_conversations_details_job_results) | Fetch a page of results for an async details job|
|[**get_analytics_conversations_details_jobs_availability**](#get_analytics_conversations_details_jobs_availability) | Lookup the datalake availability date and time|
|[**get_analytics_dataextraction_download**](#get_analytics_dataextraction_download) | Get analytics data warehouse file download|
|[**get_analytics_dataextraction_downloads_metadata**](#get_analytics_dataextraction_downloads_metadata) | Get metadata on files available for extraction|
|[**get_analytics_dataretention_settings**](#get_analytics_dataretention_settings) | Get analytics data retention setting|
|[**get_analytics_evaluations_aggregates_job**](#get_analytics_evaluations_aggregates_job) | Get status for async query for evaluation aggregates|
|[**get_analytics_evaluations_aggregates_job_results**](#get_analytics_evaluations_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_flowexecutions_aggregates_job**](#get_analytics_flowexecutions_aggregates_job) | Get status for async query for flow execution aggregates|
|[**get_analytics_flowexecutions_aggregates_job_results**](#get_analytics_flowexecutions_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_flows_aggregates_job**](#get_analytics_flows_aggregates_job) | Get status for async query for Flow aggregates|
|[**get_analytics_flows_aggregates_job_results**](#get_analytics_flows_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_journeys_aggregates_job**](#get_analytics_journeys_aggregates_job) | Get status for async query for journey aggregates|
|[**get_analytics_journeys_aggregates_job_results**](#get_analytics_journeys_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_knowledge_aggregates_job**](#get_analytics_knowledge_aggregates_job) | Get status for async query for knowledge aggregates|
|[**get_analytics_knowledge_aggregates_job_results**](#get_analytics_knowledge_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_reporting_dashboards_user**](#get_analytics_reporting_dashboards_user) | Get dashboards summary for a user|
|[**get_analytics_reporting_dashboards_users**](#get_analytics_reporting_dashboards_users) | Get dashboards summary for users in a org|
|[**get_analytics_reporting_exports**](#get_analytics_reporting_exports) | Get all view export requests for a user|
|[**get_analytics_reporting_exports_metadata**](#get_analytics_reporting_exports_metadata) | Get all export metadata|
|[**get_analytics_reporting_settings**](#get_analytics_reporting_settings) | Get AnalyticsReportingSettings for an organization|
|[**get_analytics_reporting_settings_dashboards_query**](#get_analytics_reporting_settings_dashboards_query) | Get list of dashboard configurations|
|[**get_analytics_reporting_settings_user_dashboards**](#get_analytics_reporting_settings_user_dashboards) | Get list of dashboards for an user|
|[**get_analytics_resolutions_aggregates_job**](#get_analytics_resolutions_aggregates_job) | Get status for async query for resolution aggregates|
|[**get_analytics_resolutions_aggregates_job_results**](#get_analytics_resolutions_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_summaries_aggregates_job**](#get_analytics_summaries_aggregates_job) | Get status for async query for summary aggregates|
|[**get_analytics_summaries_aggregates_job_results**](#get_analytics_summaries_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_surveys_aggregates_job**](#get_analytics_surveys_aggregates_job) | Get status for async query for survey aggregates|
|[**get_analytics_surveys_aggregates_job_results**](#get_analytics_surveys_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_taskmanagement_aggregates_job**](#get_analytics_taskmanagement_aggregates_job) | Get status for async query for task management aggregates|
|[**get_analytics_taskmanagement_aggregates_job_results**](#get_analytics_taskmanagement_aggregates_job_results) | Fetch a page of results for an async task management query|
|[**get_analytics_transcripts_aggregates_job**](#get_analytics_transcripts_aggregates_job) | Get status for async query for transcript aggregates|
|[**get_analytics_transcripts_aggregates_job_results**](#get_analytics_transcripts_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_users_aggregates_job**](#get_analytics_users_aggregates_job) | Get status for async query for user aggregates|
|[**get_analytics_users_aggregates_job_results**](#get_analytics_users_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_users_details_job**](#get_analytics_users_details_job) | Get status for async query for user details|
|[**get_analytics_users_details_job_results**](#get_analytics_users_details_job_results) | Fetch a page of results for an async query|
|[**get_analytics_users_details_jobs_availability**](#get_analytics_users_details_jobs_availability) | Lookup the datalake availability date and time|
|[**patch_analytics_reporting_settings**](#patch_analytics_reporting_settings) | Patch AnalyticsReportingSettings values for an organization|
|[**post_analytics_actions_aggregates_jobs**](#post_analytics_actions_aggregates_jobs) | Query for action aggregates asynchronously|
|[**post_analytics_actions_aggregates_query**](#post_analytics_actions_aggregates_query) | Query for action aggregates|
|[**post_analytics_agentcopilots_aggregates_jobs**](#post_analytics_agentcopilots_aggregates_jobs) | Query for agent copilot aggregates asynchronously|
|[**post_analytics_agentcopilots_aggregates_query**](#post_analytics_agentcopilots_aggregates_query) | Query for agent copilot aggregates|
|[**post_analytics_agents_status_counts**](#post_analytics_agents_status_counts) | Count agents by different groupings|
|[**post_analytics_agents_status_query**](#post_analytics_agents_status_query) | Retrieve the top 50 agents matching the query filters|
|[**post_analytics_bots_aggregates_jobs**](#post_analytics_bots_aggregates_jobs) | Query for bot aggregates asynchronously|
|[**post_analytics_bots_aggregates_query**](#post_analytics_bots_aggregates_query) | Query for bot aggregates|
|[**post_analytics_casemanagement_aggregates_jobs**](#post_analytics_casemanagement_aggregates_jobs) | Query for case management aggregates asynchronously|
|[**post_analytics_casemanagement_aggregates_query**](#post_analytics_casemanagement_aggregates_query) | Query for case management aggregates|
|[**post_analytics_conversation_details_properties**](#post_analytics_conversation_details_properties) | Index conversation properties|
|[**post_analytics_conversations_activity_query**](#post_analytics_conversations_activity_query) | Query for conversation activity observations|
|[**post_analytics_conversations_aggregates_jobs**](#post_analytics_conversations_aggregates_jobs) | Query for conversation aggregates asynchronously|
|[**post_analytics_conversations_aggregates_query**](#post_analytics_conversations_aggregates_query) | Query for conversation aggregates|
|[**post_analytics_conversations_details_jobs**](#post_analytics_conversations_details_jobs) | Query for conversation details asynchronously|
|[**post_analytics_conversations_details_query**](#post_analytics_conversations_details_query) | Query for conversation details|
|[**post_analytics_dataextraction_downloads_bulk**](#post_analytics_dataextraction_downloads_bulk) | Get download URLs for analytics data warehouse files|
|[**post_analytics_evaluations_aggregates_jobs**](#post_analytics_evaluations_aggregates_jobs) | Query for evaluation aggregates asynchronously|
|[**post_analytics_evaluations_aggregates_query**](#post_analytics_evaluations_aggregates_query) | Query for evaluation aggregates|
|[**post_analytics_flowexecutions_aggregates_jobs**](#post_analytics_flowexecutions_aggregates_jobs) | Query for flow execution aggregates asynchronously|
|[**post_analytics_flowexecutions_aggregates_query**](#post_analytics_flowexecutions_aggregates_query) | Query for flow execution aggregates|
|[**post_analytics_flows_activity_query**](#post_analytics_flows_activity_query) | Query for flow activity observations|
|[**post_analytics_flows_aggregates_jobs**](#post_analytics_flows_aggregates_jobs) | Query for flow aggregates asynchronously|
|[**post_analytics_flows_aggregates_query**](#post_analytics_flows_aggregates_query) | Query for flow aggregates|
|[**post_analytics_flows_observations_query**](#post_analytics_flows_observations_query) | Query for flow observations|
|[**post_analytics_journeys_aggregates_jobs**](#post_analytics_journeys_aggregates_jobs) | Query for journey aggregates asynchronously|
|[**post_analytics_journeys_aggregates_query**](#post_analytics_journeys_aggregates_query) | Query for journey aggregates|
|[**post_analytics_knowledge_aggregates_jobs**](#post_analytics_knowledge_aggregates_jobs) | Query for knowledge aggregates asynchronously|
|[**post_analytics_knowledge_aggregates_query**](#post_analytics_knowledge_aggregates_query) | Query for knowledge aggregates|
|[**post_analytics_queues_observations_query**](#post_analytics_queues_observations_query) | Query for queue observations|
|[**post_analytics_ratelimits_aggregates_query**](#post_analytics_ratelimits_aggregates_query) | Query for limits rate limit aggregates. Data populated when limits reach 90% of the maximum. Not a source of truth for limits hit but a best effort estimate.|
|[**post_analytics_reporting_dashboards_users_bulk_remove**](#post_analytics_reporting_dashboards_users_bulk_remove) | Bulk soft delete dashboards owned by other user(s)|
|[**post_analytics_reporting_exports**](#post_analytics_reporting_exports) | Generate a view export request|
|[**post_analytics_reporting_settings_dashboards_bulk_remove**](#post_analytics_reporting_settings_dashboards_bulk_remove) | Bulk soft delete dashboard configurations|
|[**post_analytics_reporting_settings_dashboards_query**](#post_analytics_reporting_settings_dashboards_query) | Query dashboard configurations|
|[**post_analytics_resolutions_aggregates_jobs**](#post_analytics_resolutions_aggregates_jobs) | Query for resolution aggregates asynchronously|
|[**post_analytics_resolutions_aggregates_query**](#post_analytics_resolutions_aggregates_query) | Query for resolution aggregates|
|[**post_analytics_routing_activity_query**](#post_analytics_routing_activity_query) | Query for user activity observations|
|[**post_analytics_summaries_aggregates_jobs**](#post_analytics_summaries_aggregates_jobs) | Query for summary aggregates asynchronously|
|[**post_analytics_summaries_aggregates_query**](#post_analytics_summaries_aggregates_query) | Query for summary aggregates|
|[**post_analytics_surveys_aggregates_jobs**](#post_analytics_surveys_aggregates_jobs) | Query for survey aggregates asynchronously|
|[**post_analytics_surveys_aggregates_query**](#post_analytics_surveys_aggregates_query) | Query for survey aggregates|
|[**post_analytics_taskmanagement_aggregates_jobs**](#post_analytics_taskmanagement_aggregates_jobs) | Query for task management aggregates asynchronously|
|[**post_analytics_taskmanagement_aggregates_query**](#post_analytics_taskmanagement_aggregates_query) | Query for task management aggregates|
|[**post_analytics_teams_activity_query**](#post_analytics_teams_activity_query) | Query for team activity observations|
|[**post_analytics_transcripts_aggregates_jobs**](#post_analytics_transcripts_aggregates_jobs) | Query for transcript aggregates asynchronously|
|[**post_analytics_transcripts_aggregates_query**](#post_analytics_transcripts_aggregates_query) | Query for transcript aggregates|
|[**post_analytics_users_activity_query**](#post_analytics_users_activity_query) | Query for user activity observations|
|[**post_analytics_users_aggregates_jobs**](#post_analytics_users_aggregates_jobs) | Query for user aggregates asynchronously|
|[**post_analytics_users_aggregates_query**](#post_analytics_users_aggregates_query) | Query for user aggregates|
|[**post_analytics_users_details_jobs**](#post_analytics_users_details_jobs) | Query for user details asynchronously|
|[**post_analytics_users_details_query**](#post_analytics_users_details_query) | Query for user details|
|[**post_analytics_users_observations_query**](#post_analytics_users_observations_query) | Query for user observations|
|[**put_analytics_dataretention_settings**](#put_analytics_dataretention_settings) | Update analytics data retention setting|



## delete_analytics_actions_aggregates_job

>  delete_analytics_actions_aggregates_job(job_id)


Delete/cancel an async request for action aggregates

delete_analytics_actions_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/actions/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* integrations:action:view
* bridge:actions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for action aggregates
    api_instance.delete_analytics_actions_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_actions_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_agentcopilots_aggregates_job

>  delete_analytics_agentcopilots_aggregates_job(job_id)


Delete/cancel an async request for agent copilot aggregates

delete_analytics_agentcopilots_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/agentcopilots/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:agentCopilotAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for agent copilot aggregates
    api_instance.delete_analytics_agentcopilots_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_agentcopilots_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_bots_aggregates_job

>  delete_analytics_bots_aggregates_job(job_id)


Delete/cancel an async request for bot aggregates

delete_analytics_bots_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/bots/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:botAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for bot aggregates
    api_instance.delete_analytics_bots_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_bots_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_casemanagement_aggregates_job

>  delete_analytics_casemanagement_aggregates_job(job_id)


Delete/cancel an async request for case management aggregates

delete_analytics_casemanagement_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/casemanagement/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:caseManagementAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for case management aggregates
    api_instance.delete_analytics_casemanagement_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_casemanagement_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_conversations_aggregates_job

>  delete_analytics_conversations_aggregates_job(job_id)


Delete/cancel an async request for conversation aggregates

delete_analytics_conversations_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/conversations/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:conversationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for conversation aggregates
    api_instance.delete_analytics_conversations_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_conversations_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_conversations_details_job

>  delete_analytics_conversations_details_job(job_id)


Delete/cancel an async details job

Wraps DELETE /api/v2/analytics/conversations/details/jobs/{jobId} 

Requires ANY permissions: 

* analytics:conversationDetail:view
* analytics:agentConversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async details job
    api_instance.delete_analytics_conversations_details_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_conversations_details_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_evaluations_aggregates_job

>  delete_analytics_evaluations_aggregates_job(job_id)


Delete/cancel an async request for evaluation aggregates

delete_analytics_evaluations_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/evaluations/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:evaluationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for evaluation aggregates
    api_instance.delete_analytics_evaluations_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_evaluations_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_flowexecutions_aggregates_job

>  delete_analytics_flowexecutions_aggregates_job(job_id)


Delete/cancel an async request for flow execution aggregates

delete_analytics_flowexecutions_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/flowexecutions/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:flowExecutionAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for flow execution aggregates
    api_instance.delete_analytics_flowexecutions_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_flowexecutions_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_flows_aggregates_job

>  delete_analytics_flows_aggregates_job(job_id)


Delete/cancel an async request for flow aggregates

delete_analytics_flows_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/flows/aggregates/jobs/{jobId} 

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
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for flow aggregates
    api_instance.delete_analytics_flows_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_flows_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


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
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for journey aggregates
    api_instance.delete_analytics_journeys_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_journeys_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_knowledge_aggregates_job

>  delete_analytics_knowledge_aggregates_job(job_id)


Delete/cancel an async request for knowledge aggregates

delete_analytics_knowledge_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/knowledge/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:knowledgeAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for knowledge aggregates
    api_instance.delete_analytics_knowledge_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_knowledge_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_resolutions_aggregates_job

>  delete_analytics_resolutions_aggregates_job(job_id)


Delete/cancel an async request for resolution aggregates

delete_analytics_resolutions_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/resolutions/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:resolutionAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for resolution aggregates
    api_instance.delete_analytics_resolutions_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_resolutions_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_summaries_aggregates_job

>  delete_analytics_summaries_aggregates_job(job_id)


Delete/cancel an async request for summary aggregates

delete_analytics_summaries_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/summaries/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:summaryAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for summary aggregates
    api_instance.delete_analytics_summaries_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_summaries_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_surveys_aggregates_job

>  delete_analytics_surveys_aggregates_job(job_id)


Delete/cancel an async request for survey aggregates

delete_analytics_surveys_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/surveys/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:surveyAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for survey aggregates
    api_instance.delete_analytics_surveys_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_surveys_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_taskmanagement_aggregates_job

>  delete_analytics_taskmanagement_aggregates_job(job_id)


Delete/cancel an async request for task management aggregates

delete_analytics_taskmanagement_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/taskmanagement/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:taskManagementAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for task management aggregates
    api_instance.delete_analytics_taskmanagement_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_taskmanagement_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_transcripts_aggregates_job

>  delete_analytics_transcripts_aggregates_job(job_id)


Delete/cancel an async request for transcript aggregates

delete_analytics_transcripts_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/transcripts/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:speechAndTextAnalyticsAggregates:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for transcript aggregates
    api_instance.delete_analytics_transcripts_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_transcripts_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_users_aggregates_job

>  delete_analytics_users_aggregates_job(job_id)


Delete/cancel an async request for user aggregates

delete_analytics_users_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/analytics/users/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:userAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request for user aggregates
    api_instance.delete_analytics_users_aggregates_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_users_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## delete_analytics_users_details_job

>  delete_analytics_users_details_job(job_id)


Delete/cancel an async request

Wraps DELETE /api/v2/analytics/users/details/jobs/{jobId} 

Requires ANY permissions: 

* analytics:userDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request
    api_instance.delete_analytics_users_details_job(job_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->delete_analytics_users_details_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

void (empty response body)


## get_analytics_actions_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_actions_aggregates_job(job_id)


Get status for async query for action aggregates

get_analytics_actions_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/actions/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* integrations:action:view
* bridge:actions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for action aggregates
    api_response = api_instance.get_analytics_actions_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_actions_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_actions_aggregates_job_results

> [**ActionAsyncAggregateQueryResponse**](ActionAsyncAggregateQueryResponse) get_analytics_actions_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async aggregates query

get_analytics_actions_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/actions/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* integrations:action:view
* bridge:actions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_actions_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_actions_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**ActionAsyncAggregateQueryResponse**](ActionAsyncAggregateQueryResponse)


## get_analytics_agent_status

> [**AnalyticsAgentStateAgentResponse**](AnalyticsAgentStateAgentResponse) get_analytics_agent_status(user_id)


Get an agent and their active sessions by user ID

Wraps GET /api/v2/analytics/agents/{userId}/status 

Requires ANY permissions: 

* analytics:agentState:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
user_id = 'user_id_example' # str | userId

try:
    # Get an agent and their active sessions by user ID
    api_response = api_instance.get_analytics_agent_status(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_agent_status: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| userId |  |

### Return type

[**AnalyticsAgentStateAgentResponse**](AnalyticsAgentStateAgentResponse)


## get_analytics_agentcopilots_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_agentcopilots_aggregates_job(job_id)


Get status for async query for agent copilot aggregates

get_analytics_agentcopilots_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/agentcopilots/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:agentCopilotAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for agent copilot aggregates
    api_response = api_instance.get_analytics_agentcopilots_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_agentcopilots_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_agentcopilots_aggregates_job_results

> [**AgentCopilotAsyncAggregateQueryResponse**](AgentCopilotAsyncAggregateQueryResponse) get_analytics_agentcopilots_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async aggregates query

get_analytics_agentcopilots_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/agentcopilots/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:agentCopilotAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_agentcopilots_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_agentcopilots_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**AgentCopilotAsyncAggregateQueryResponse**](AgentCopilotAsyncAggregateQueryResponse)


## get_analytics_botflow_divisions_reportingturns

> [**ReportingTurnsResponse**](ReportingTurnsResponse) get_analytics_botflow_divisions_reportingturns(bot_flow_id, after=after, page_size=page_size, interval=interval, action_id=action_id, session_id=session_id, language=language, ask_action_results=ask_action_results)


Get Reporting Turns (division aware).

Returns the reporting turns for the specified flow, filtered by the clients divisions and grouped by session, in reverse chronological order from the date the session was created, with the reporting turns from the most recent session appearing at the start of the list. It is expected that the client will URL encode the request URI once only. For pagination, clients should keep sending requests using the value of 'nextUri' in the response, until it's no longer present, only then have all items have been returned. The 'nextUri' value in the response is already URL encoded (so it doesn't need to be encoded again). Note: resources returned by this endpoint are not persisted indefinitely, as they are deleted after approximately, but not before, 10 days.

Wraps GET /api/v2/analytics/botflows/{botFlowId}/divisions/reportingturns 

Requires ANY permissions: 

* analytics:botFlowDivisionAwareReportingTurn:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
bot_flow_id = 'bot_flow_id_example' # str | ID of the bot flow.
after = 'after_example' # str | The cursor that points to the ID of the last item in the list of entities that has been returned. (optional)
page_size = ''50'' # str | Max number of entities to return. Maximum of 250 (optional) (default to '50')
interval = '2023-07-17T08:15:44.586Z/2023-07-26T09:22:33.111Z' # str | Date range filter based on the date the individual resources were completed. UTC is the default if no TZ is supplied, however alternate timezones can be used e.g: '2022-11-22T09:11:11.111+08:00/2022-11-30T07:17:44.586-07'. . Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
action_id = 'action_id_example' # str | Optional action ID to get the reporting turns associated to a particular flow action (optional)
session_id = 'session_id_example' # str | Optional session ID to get the reporting turns for a particular session. Specifying a session ID alongside an action ID or a language or any ask action results is not allowed. (optional)
language = 'en-us' # str | Optional language code to get the reporting turns for a particular language (optional)
ask_action_results = 'ask_action_results_example' # str | Optional case-insensitive comma separated list of ask action results to filter the reporting turns. (optional)

try:
    # Get Reporting Turns (division aware).
    api_response = api_instance.get_analytics_botflow_divisions_reportingturns(bot_flow_id, after=after, page_size=page_size, interval=interval, action_id=action_id, session_id=session_id, language=language, ask_action_results=ask_action_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_botflow_divisions_reportingturns: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bot_flow_id** | **str**| ID of the bot flow. |  |
| **after** | **str**| The cursor that points to the ID of the last item in the list of entities that has been returned. | [optional]  |
| **page_size** | **str**| Max number of entities to return. Maximum of 250 | [optional] [default to &#39;50&#39;] |
| **interval** | **str**| Date range filter based on the date the individual resources were completed. UTC is the default if no TZ is supplied, however alternate timezones can be used e.g: &#39;2022-11-22T09:11:11.111+08:00/2022-11-30T07:17:44.586-07&#39;. . Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **action_id** | **str**| Optional action ID to get the reporting turns associated to a particular flow action | [optional]  |
| **session_id** | **str**| Optional session ID to get the reporting turns for a particular session. Specifying a session ID alongside an action ID or a language or any ask action results is not allowed. | [optional]  |
| **language** | **str**| Optional language code to get the reporting turns for a particular language | [optional]  |
| **ask_action_results** | **str**| Optional case-insensitive comma separated list of ask action results to filter the reporting turns. | [optional] <br />**Values**: AgentRequestedByUser, ConfirmationRequired, DisambiguationRequired, Error, ExpressionError, NoInputCollection, NoInputConfirmation, NoInputDisambiguation, NoMatchCollection, NoMatchConfirmation, NoMatchDisambiguation, SuccessCollection, SkippedCollection, SuccessConfirmationNo, SuccessConfirmationYes, SuccessDisambiguation, SuccessDisambiguationNone |

### Return type

[**ReportingTurnsResponse**](ReportingTurnsResponse)


## get_analytics_botflow_reportingturns

> [**ReportingTurnsResponse**](ReportingTurnsResponse) get_analytics_botflow_reportingturns(bot_flow_id, after=after, page_size=page_size, interval=interval, action_id=action_id, session_id=session_id, language=language, ask_action_results=ask_action_results)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get Reporting Turns.

Deprecated: Please use GET /analytics/botflows/{botFlowId}/divisions/reportingturns instead. Returns the reporting turns grouped by session, in reverse chronological order from the date the session was created, with the reporting turns from the most recent session appearing at the start of the list. It is expected that the client will URL encode the request URI once only. For pagination, clients should keep sending requests using the value of 'nextUri' in the response, until it's no longer present, only then have all items have been returned. The 'nextUri' value in the response is already URL encoded (so it doesn't need to be encoded again). Note: resources returned by this endpoint are not persisted indefinitely, as they are deleted after approximately, but not before, 10 days.

Wraps GET /api/v2/analytics/botflows/{botFlowId}/reportingturns 

Requires ANY permissions: 

* analytics:botFlowReportingTurn:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
bot_flow_id = 'bot_flow_id_example' # str | ID of the bot flow.
after = 'after_example' # str | The cursor that points to the ID of the last item in the list of entities that has been returned. (optional)
page_size = ''50'' # str | Max number of entities to return. Maximum of 250 (optional) (default to '50')
interval = '2023-07-17T08:15:44.586Z/2023-07-26T09:22:33.111Z' # str | Date range filter based on the date the individual resources were completed. UTC is the default if no TZ is supplied, however alternate timezones can be used e.g: '2022-11-22T09:11:11.111+08:00/2022-11-30T07:17:44.586-07'. . Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
action_id = 'action_id_example' # str | Optional action ID to get the reporting turns associated to a particular flow action (optional)
session_id = 'session_id_example' # str | Optional session ID to get the reporting turns for a particular session. Specifying a session ID alongside an action ID or a language or any ask action results is not allowed. (optional)
language = 'en-us' # str | Optional language code to get the reporting turns for a particular language (optional)
ask_action_results = 'ask_action_results_example' # str | Optional case-insensitive comma separated list of ask action results to filter the reporting turns. (optional)

try:
    # Get Reporting Turns.
    api_response = api_instance.get_analytics_botflow_reportingturns(bot_flow_id, after=after, page_size=page_size, interval=interval, action_id=action_id, session_id=session_id, language=language, ask_action_results=ask_action_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_botflow_reportingturns: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bot_flow_id** | **str**| ID of the bot flow. |  |
| **after** | **str**| The cursor that points to the ID of the last item in the list of entities that has been returned. | [optional]  |
| **page_size** | **str**| Max number of entities to return. Maximum of 250 | [optional] [default to &#39;50&#39;] |
| **interval** | **str**| Date range filter based on the date the individual resources were completed. UTC is the default if no TZ is supplied, however alternate timezones can be used e.g: &#39;2022-11-22T09:11:11.111+08:00/2022-11-30T07:17:44.586-07&#39;. . Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **action_id** | **str**| Optional action ID to get the reporting turns associated to a particular flow action | [optional]  |
| **session_id** | **str**| Optional session ID to get the reporting turns for a particular session. Specifying a session ID alongside an action ID or a language or any ask action results is not allowed. | [optional]  |
| **language** | **str**| Optional language code to get the reporting turns for a particular language | [optional]  |
| **ask_action_results** | **str**| Optional case-insensitive comma separated list of ask action results to filter the reporting turns. | [optional] <br />**Values**: AgentRequestedByUser, ConfirmationRequired, DisambiguationRequired, Error, ExpressionError, NoInputCollection, NoInputConfirmation, NoInputDisambiguation, NoMatchCollection, NoMatchConfirmation, NoMatchDisambiguation, SuccessCollection, SkippedCollection, SuccessConfirmationNo, SuccessConfirmationYes, SuccessDisambiguation, SuccessDisambiguationNone |

### Return type

[**ReportingTurnsResponse**](ReportingTurnsResponse)


## get_analytics_botflow_sessions

> [**SessionsResponse**](SessionsResponse) get_analytics_botflow_sessions(bot_flow_id, after=after, page_size=page_size, interval=interval, bot_result_categories=bot_result_categories, end_language=end_language)


Get Bot Flow Sessions.

Returns the bot flow sessions in reverse chronological order from the date they were created. It is expected that the client will URL encode the request URI once only. For pagination, clients should keep sending requests using the value of 'nextUri' in the response, until it's no longer present, only then have all items have been returned. The 'nextUri' value in the response is already URL encoded (so it doesn't need to be encoded again). Note: resources returned by this endpoint are not persisted indefinitely, as they are deleted after approximately, but not before, 10 days.

Wraps GET /api/v2/analytics/botflows/{botFlowId}/sessions 

Requires ANY permissions: 

* analytics:botFlowSession:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
bot_flow_id = 'bot_flow_id_example' # str | ID of the bot flow.
after = 'after_example' # str | The cursor that points to the ID of the last item in the list of entities that has been returned. (optional)
page_size = ''50'' # str | Max number of entities to return. Maximum of 250 (optional) (default to '50')
interval = '2023-07-17T08:15:44.586Z/2023-07-26T09:22:33.111Z' # str | Date range filter based on the date the individual resources were completed. UTC is the default if no TZ is supplied, however alternate timezones can be used e.g: '2022-11-22T09:11:11.111+08:00/2022-11-30T07:17:44.586-07'. . Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
bot_result_categories = 'bot_result_categories_example' # str | Optional case-insensitive comma separated list of Bot Result Categories to filter sessions by. (optional)
end_language = 'end_language_example' # str | Optional case-insensitive language code to filter sessions by the language the sessions ended in. (optional)

try:
    # Get Bot Flow Sessions.
    api_response = api_instance.get_analytics_botflow_sessions(bot_flow_id, after=after, page_size=page_size, interval=interval, bot_result_categories=bot_result_categories, end_language=end_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_botflow_sessions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bot_flow_id** | **str**| ID of the bot flow. |  |
| **after** | **str**| The cursor that points to the ID of the last item in the list of entities that has been returned. | [optional]  |
| **page_size** | **str**| Max number of entities to return. Maximum of 250 | [optional] [default to &#39;50&#39;] |
| **interval** | **str**| Date range filter based on the date the individual resources were completed. UTC is the default if no TZ is supplied, however alternate timezones can be used e.g: &#39;2022-11-22T09:11:11.111+08:00/2022-11-30T07:17:44.586-07&#39;. . Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **bot_result_categories** | **str**| Optional case-insensitive comma separated list of Bot Result Categories to filter sessions by. | [optional] <br />**Values**: Unknown, UserExit, BotExit, Error, RecognitionFailure, UserDisconnect, BotDisconnect, SessionExpired, Transfer |
| **end_language** | **str**| Optional case-insensitive language code to filter sessions by the language the sessions ended in. | [optional]  |

### Return type

[**SessionsResponse**](SessionsResponse)


## get_analytics_bots_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_bots_aggregates_job(job_id)


Get status for async query for bot aggregates

get_analytics_bots_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/bots/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:botAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for bot aggregates
    api_response = api_instance.get_analytics_bots_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_bots_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_bots_aggregates_job_results

> [**BotAsyncAggregateQueryResponse**](BotAsyncAggregateQueryResponse) get_analytics_bots_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async aggregates query

get_analytics_bots_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/bots/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:botAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_bots_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_bots_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**BotAsyncAggregateQueryResponse**](BotAsyncAggregateQueryResponse)


## get_analytics_casemanagement_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_casemanagement_aggregates_job(job_id)


Get status for async query for case management aggregates

get_analytics_casemanagement_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/casemanagement/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:caseManagementAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for case management aggregates
    api_response = api_instance.get_analytics_casemanagement_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_casemanagement_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_casemanagement_aggregates_job_results

> [**CaseManagementAsyncAggregateQueryResponse**](CaseManagementAsyncAggregateQueryResponse) get_analytics_casemanagement_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async case management query

get_analytics_casemanagement_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/casemanagement/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:caseManagementAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async case management query
    api_response = api_instance.get_analytics_casemanagement_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_casemanagement_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**CaseManagementAsyncAggregateQueryResponse**](CaseManagementAsyncAggregateQueryResponse)


## get_analytics_conversation_details

> [**AnalyticsConversationWithoutAttributes**](AnalyticsConversationWithoutAttributes) get_analytics_conversation_details(conversation_id)


Get a conversation by id

Wraps GET /api/v2/analytics/conversations/{conversationId}/details 

Requires ANY permissions: 

* analytics:conversationDetail:view
* analytics:agentConversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get a conversation by id
    api_response = api_instance.get_analytics_conversation_details(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_conversation_details: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |

### Return type

[**AnalyticsConversationWithoutAttributes**](AnalyticsConversationWithoutAttributes)


## get_analytics_conversations_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_conversations_aggregates_job(job_id)


Get status for async query for conversation aggregates

get_analytics_conversations_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/conversations/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:conversationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for conversation aggregates
    api_response = api_instance.get_analytics_conversations_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_conversations_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_conversations_aggregates_job_results

> [**ConversationAsyncAggregateQueryResponse**](ConversationAsyncAggregateQueryResponse) get_analytics_conversations_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async aggregates query

get_analytics_conversations_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/conversations/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:conversationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_conversations_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_conversations_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**ConversationAsyncAggregateQueryResponse**](ConversationAsyncAggregateQueryResponse)


## get_analytics_conversations_details

> [**AnalyticsConversationWithoutAttributesMultiGetResponse**](AnalyticsConversationWithoutAttributesMultiGetResponse) get_analytics_conversations_details(id=id)


Gets multiple conversations by id

Wraps GET /api/v2/analytics/conversations/details 

Requires ANY permissions: 

* analytics:conversationDetail:view
* analytics:agentConversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
id = ['id_example'] # list[str] | Comma-separated conversation ids (optional)

try:
    # Gets multiple conversations by id
    api_response = api_instance.get_analytics_conversations_details(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_conversations_details: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str)| Comma-separated conversation ids | [optional]  |

### Return type

[**AnalyticsConversationWithoutAttributesMultiGetResponse**](AnalyticsConversationWithoutAttributesMultiGetResponse)


## get_analytics_conversations_details_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_conversations_details_job(job_id)


Get status for async query for conversation details

Wraps GET /api/v2/analytics/conversations/details/jobs/{jobId} 

Requires ANY permissions: 

* analytics:conversationDetail:view
* analytics:agentConversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for conversation details
    api_response = api_instance.get_analytics_conversations_details_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_conversations_details_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_conversations_details_job_results

> [**AnalyticsConversationAsyncQueryResponse**](AnalyticsConversationAsyncQueryResponse) get_analytics_conversations_details_job_results(job_id, cursor=cursor, page_size=page_size)


Fetch a page of results for an async details job

Wraps GET /api/v2/analytics/conversations/details/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:conversationDetail:view
* analytics:agentConversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page) (optional)
page_size = 56 # int | The desired maximum number of results (optional)

try:
    # Fetch a page of results for an async details job
    api_response = api_instance.get_analytics_conversations_details_job_results(job_id, cursor=cursor, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_conversations_details_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page) | [optional]  |
| **page_size** | **int**| The desired maximum number of results | [optional]  |

### Return type

[**AnalyticsConversationAsyncQueryResponse**](AnalyticsConversationAsyncQueryResponse)


## get_analytics_conversations_details_jobs_availability

> [**DataAvailabilityResponse**](DataAvailabilityResponse) get_analytics_conversations_details_jobs_availability()


Lookup the datalake availability date and time

Wraps GET /api/v2/analytics/conversations/details/jobs/availability 

Requires ANY permissions: 

* analytics:conversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()

try:
    # Lookup the datalake availability date and time
    api_response = api_instance.get_analytics_conversations_details_jobs_availability()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_conversations_details_jobs_availability: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**DataAvailabilityResponse**](DataAvailabilityResponse)


## get_analytics_dataextraction_download

>  get_analytics_dataextraction_download(download_id)


Get analytics data warehouse file download

get_analytics_dataextraction_download is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/dataextraction/downloads/{downloadId} 

Requires ANY permissions: 

* analytics:datawarehouse:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
download_id = 'download_id_example' # str | Unique file Id to download

try:
    # Get analytics data warehouse file download
    api_instance.get_analytics_dataextraction_download(download_id)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_dataextraction_download: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **download_id** | **str**| Unique file Id to download |  |

### Return type

void (empty response body)


## get_analytics_dataextraction_downloads_metadata

> [**DataExtractionFileSchemaListing**](DataExtractionFileSchemaListing) get_analytics_dataextraction_downloads_metadata(before=before, after=after, page_size=page_size, data_schema=data_schema, date_start=date_start, date_end=date_end)


Get metadata on files available for extraction

get_analytics_dataextraction_downloads_metadata is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/dataextraction/downloads/metadata 

Requires ANY permissions: 

* analytics:datawarehouse:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
data_schema = 'data_schema_example' # str | Data schema like conversations (optional)
date_start = '2013-10-20T19:20:30+01:00' # datetime | Start DateTime filter. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z (optional)
date_end = '2013-10-20T19:20:30+01:00' # datetime | End DateTime filter. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z (optional)

try:
    # Get metadata on files available for extraction
    api_response = api_instance.get_analytics_dataextraction_downloads_metadata(before=before, after=after, page_size=page_size, data_schema=data_schema, date_start=date_start, date_end=date_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_dataextraction_downloads_metadata: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **data_schema** | **str**| Data schema like conversations | [optional]  |
| **date_start** | **datetime**| Start DateTime filter. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional]  |
| **date_end** | **datetime**| End DateTime filter. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional]  |

### Return type

[**DataExtractionFileSchemaListing**](DataExtractionFileSchemaListing)


## get_analytics_dataretention_settings

> [**AnalyticsDataRetentionResponse**](AnalyticsDataRetentionResponse) get_analytics_dataretention_settings()


Get analytics data retention setting

Wraps GET /api/v2/analytics/dataretention/settings 

Requires ANY permissions: 

* analytics:dataRetention:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()

try:
    # Get analytics data retention setting
    api_response = api_instance.get_analytics_dataretention_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_dataretention_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**AnalyticsDataRetentionResponse**](AnalyticsDataRetentionResponse)


## get_analytics_evaluations_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_evaluations_aggregates_job(job_id)


Get status for async query for evaluation aggregates

get_analytics_evaluations_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/evaluations/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:evaluationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for evaluation aggregates
    api_response = api_instance.get_analytics_evaluations_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_evaluations_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_evaluations_aggregates_job_results

> [**EvaluationAsyncAggregateQueryResponse**](EvaluationAsyncAggregateQueryResponse) get_analytics_evaluations_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async aggregates query

get_analytics_evaluations_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/evaluations/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:evaluationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_evaluations_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_evaluations_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**EvaluationAsyncAggregateQueryResponse**](EvaluationAsyncAggregateQueryResponse)


## get_analytics_flowexecutions_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_flowexecutions_aggregates_job(job_id)


Get status for async query for flow execution aggregates

get_analytics_flowexecutions_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/flowexecutions/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:flowExecutionAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for flow execution aggregates
    api_response = api_instance.get_analytics_flowexecutions_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_flowexecutions_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_flowexecutions_aggregates_job_results

> [**FlowExecutionAsyncAggregateQueryResponse**](FlowExecutionAsyncAggregateQueryResponse) get_analytics_flowexecutions_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async aggregates query

get_analytics_flowexecutions_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/flowexecutions/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:flowExecutionAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_flowexecutions_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_flowexecutions_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**FlowExecutionAsyncAggregateQueryResponse**](FlowExecutionAsyncAggregateQueryResponse)


## get_analytics_flows_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_flows_aggregates_job(job_id)


Get status for async query for Flow aggregates

get_analytics_flows_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/flows/aggregates/jobs/{jobId} 

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
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for Flow aggregates
    api_response = api_instance.get_analytics_flows_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_flows_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_flows_aggregates_job_results

> [**FlowAsyncAggregateQueryResponse**](FlowAsyncAggregateQueryResponse) get_analytics_flows_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async aggregates query

get_analytics_flows_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/flows/aggregates/jobs/{jobId}/results 

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
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_flows_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_flows_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**FlowAsyncAggregateQueryResponse**](FlowAsyncAggregateQueryResponse)


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
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for journey aggregates
    api_response = api_instance.get_analytics_journeys_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_journeys_aggregates_job: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_journeys_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_journeys_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**JourneyAsyncAggregateQueryResponse**](JourneyAsyncAggregateQueryResponse)


## get_analytics_knowledge_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_knowledge_aggregates_job(job_id)


Get status for async query for knowledge aggregates

get_analytics_knowledge_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/knowledge/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:knowledgeAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for knowledge aggregates
    api_response = api_instance.get_analytics_knowledge_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_knowledge_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_knowledge_aggregates_job_results

> [**KnowledgeAsyncAggregateQueryResponse**](KnowledgeAsyncAggregateQueryResponse) get_analytics_knowledge_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async aggregates query

get_analytics_knowledge_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/knowledge/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:knowledgeAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_knowledge_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_knowledge_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**KnowledgeAsyncAggregateQueryResponse**](KnowledgeAsyncAggregateQueryResponse)


## get_analytics_reporting_dashboards_user

> [**DashboardUser**](DashboardUser) get_analytics_reporting_dashboards_user(user_id)


Get dashboards summary for a user

Wraps GET /api/v2/analytics/reporting/dashboards/users/{userId} 

Requires ALL permissions: 

* analytics:dashboardConfigurations:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
user_id = 'user_id_example' # str | User ID

try:
    # Get dashboards summary for a user
    api_response = api_instance.get_analytics_reporting_dashboards_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_reporting_dashboards_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |

### Return type

[**DashboardUser**](DashboardUser)


## get_analytics_reporting_dashboards_users

> [**DashboardUserListing**](DashboardUserListing) get_analytics_reporting_dashboards_users(sort_by=sort_by, page_number=page_number, page_size=page_size, id=id, state=state, deleted_only=deleted_only)


Get dashboards summary for users in a org

Wraps GET /api/v2/analytics/reporting/dashboards/users 

Requires ALL permissions: 

* analytics:dashboardConfigurations:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
sort_by = ''asc'' # str |  (optional) (default to 'asc')
page_number = 1 # int |  (optional) (default to 1)
page_size = 25 # int |  (optional) (default to 25)
id = ['id_example'] # list[str] | A list of user IDs to fetch by bulk (optional)
state = 'state_example' # str | Only list users of this state (optional)
deleted_only = True # bool | Only list users with deleted dashboards (optional)

try:
    # Get dashboards summary for users in a org
    api_response = api_instance.get_analytics_reporting_dashboards_users(sort_by=sort_by, page_number=page_number, page_size=page_size, id=id, state=state, deleted_only=deleted_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_reporting_dashboards_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sort_by** | **str**|  | [optional] [default to &#39;asc&#39;] |
| **page_number** | **int**|  | [optional] [default to 1] |
| **page_size** | **int**|  | [optional] [default to 25] |
| **id** | [**list[str]**](str)| A list of user IDs to fetch by bulk | [optional]  |
| **state** | **str**| Only list users of this state | [optional] <br />**Values**: active, inactive |
| **deleted_only** | **bool**| Only list users with deleted dashboards | [optional]  |

### Return type

[**DashboardUserListing**](DashboardUserListing)


## get_analytics_reporting_exports

> [**ReportingExportJobListing**](ReportingExportJobListing) get_analytics_reporting_exports(page_number=page_number, page_size=page_size)


Get all view export requests for a user

Wraps GET /api/v2/analytics/reporting/exports 

Requires ALL permissions: 

* analytics:dataExport:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get all view export requests for a user
    api_response = api_instance.get_analytics_reporting_exports(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_reporting_exports: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**ReportingExportJobListing**](ReportingExportJobListing)


## get_analytics_reporting_exports_metadata

> [**ReportingExportMetadataJobListing**](ReportingExportMetadataJobListing) get_analytics_reporting_exports_metadata()


Get all export metadata

Wraps GET /api/v2/analytics/reporting/exports/metadata 

Requires ALL permissions: 

* analytics:dataExport:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()

try:
    # Get all export metadata
    api_response = api_instance.get_analytics_reporting_exports_metadata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_reporting_exports_metadata: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**ReportingExportMetadataJobListing**](ReportingExportMetadataJobListing)


## get_analytics_reporting_settings

> [**AnalyticsReportingSettings**](AnalyticsReportingSettings) get_analytics_reporting_settings()


Get AnalyticsReportingSettings for an organization

Wraps GET /api/v2/analytics/reporting/settings 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()

try:
    # Get AnalyticsReportingSettings for an organization
    api_response = api_instance.get_analytics_reporting_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_reporting_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**AnalyticsReportingSettings**](AnalyticsReportingSettings)


## get_analytics_reporting_settings_dashboards_query

> [**DashboardConfigurationListing**](DashboardConfigurationListing) get_analytics_reporting_settings_dashboards_query(dashboard_type, dashboard_access_filter, name=name, dashboard_state=dashboard_state, sort_by=sort_by, page_number=page_number, page_size=page_size)


Get list of dashboard configurations

Wraps GET /api/v2/analytics/reporting/settings/dashboards/query 

Requires ALL permissions: 

* analytics:dashboardConfigurations:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
dashboard_type = 'dashboard_type_example' # str | List dashboard of given type
dashboard_access_filter = 'dashboard_access_filter_example' # str | Filter dashboard based on the owner of dashboard
name = 'name_example' # str | name of the dashboard (optional)
dashboard_state = ''Active'' # str | List dashboard of given state (optional) (default to 'Active')
sort_by = ''desc'' # str |  (optional) (default to 'desc')
page_number = 1 # int |  (optional) (default to 1)
page_size = 9 # int |  (optional) (default to 9)

try:
    # Get list of dashboard configurations
    api_response = api_instance.get_analytics_reporting_settings_dashboards_query(dashboard_type, dashboard_access_filter, name=name, dashboard_state=dashboard_state, sort_by=sort_by, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_reporting_settings_dashboards_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dashboard_type** | **str**| List dashboard of given type | <br />**Values**: All, Public, Private, Shared, Favorites |
| **dashboard_access_filter** | **str**| Filter dashboard based on the owner of dashboard | <br />**Values**: OwnedByMe, OwnedByAnyone, NotOwnedByMe |
| **name** | **str**| name of the dashboard | [optional]  |
| **dashboard_state** | **str**| List dashboard of given state | [optional] [default to &#39;Active&#39;]<br />**Values**: Active, Deleted |
| **sort_by** | **str**|  | [optional] [default to &#39;desc&#39;] |
| **page_number** | **int**|  | [optional] [default to 1] |
| **page_size** | **int**|  | [optional] [default to 9] |

### Return type

[**DashboardConfigurationListing**](DashboardConfigurationListing)


## get_analytics_reporting_settings_user_dashboards

> [**DashboardConfigurationListing**](DashboardConfigurationListing) get_analytics_reporting_settings_user_dashboards(user_id, sort_by=sort_by, page_number=page_number, page_size=page_size, public_only=public_only, favorite_only=favorite_only, deleted_only=deleted_only, name=name)


Get list of dashboards for an user

Wraps GET /api/v2/analytics/reporting/settings/users/{userId}/dashboards 

Requires ALL permissions: 

* analytics:dashboardConfigurations:viewPrivate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
user_id = 'user_id_example' # str | User ID
sort_by = ''asc'' # str |  (optional) (default to 'asc')
page_number = 1 # int |  (optional) (default to 1)
page_size = 50 # int |  (optional) (default to 50)
public_only = True # bool | If true, retrieve only public dashboards (optional)
favorite_only = True # bool | If true, retrieve only favorite dashboards (optional)
deleted_only = True # bool | If true, retrieve only deleted dashboards that are still recoverable (optional)
name = 'name_example' # str | retrieve dashboards that match with given name (optional)

try:
    # Get list of dashboards for an user
    api_response = api_instance.get_analytics_reporting_settings_user_dashboards(user_id, sort_by=sort_by, page_number=page_number, page_size=page_size, public_only=public_only, favorite_only=favorite_only, deleted_only=deleted_only, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_reporting_settings_user_dashboards: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **sort_by** | **str**|  | [optional] [default to &#39;asc&#39;] |
| **page_number** | **int**|  | [optional] [default to 1] |
| **page_size** | **int**|  | [optional] [default to 50] |
| **public_only** | **bool**| If true, retrieve only public dashboards | [optional]  |
| **favorite_only** | **bool**| If true, retrieve only favorite dashboards | [optional]  |
| **deleted_only** | **bool**| If true, retrieve only deleted dashboards that are still recoverable | [optional]  |
| **name** | **str**| retrieve dashboards that match with given name | [optional]  |

### Return type

[**DashboardConfigurationListing**](DashboardConfigurationListing)


## get_analytics_resolutions_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_resolutions_aggregates_job(job_id)


Get status for async query for resolution aggregates

get_analytics_resolutions_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/resolutions/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:resolutionAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for resolution aggregates
    api_response = api_instance.get_analytics_resolutions_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_resolutions_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_resolutions_aggregates_job_results

> [**ResolutionAsyncAggregateQueryResponse**](ResolutionAsyncAggregateQueryResponse) get_analytics_resolutions_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async aggregates query

get_analytics_resolutions_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/resolutions/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:resolutionAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_resolutions_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_resolutions_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**ResolutionAsyncAggregateQueryResponse**](ResolutionAsyncAggregateQueryResponse)


## get_analytics_summaries_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_summaries_aggregates_job(job_id)


Get status for async query for summary aggregates

get_analytics_summaries_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/summaries/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:summaryAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for summary aggregates
    api_response = api_instance.get_analytics_summaries_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_summaries_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_summaries_aggregates_job_results

> [**SummaryAsyncAggregateQueryResponse**](SummaryAsyncAggregateQueryResponse) get_analytics_summaries_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async aggregates query

get_analytics_summaries_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/summaries/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:summaryAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_summaries_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_summaries_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**SummaryAsyncAggregateQueryResponse**](SummaryAsyncAggregateQueryResponse)


## get_analytics_surveys_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_surveys_aggregates_job(job_id)


Get status for async query for survey aggregates

get_analytics_surveys_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/surveys/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:surveyAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for survey aggregates
    api_response = api_instance.get_analytics_surveys_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_surveys_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_surveys_aggregates_job_results

> [**SurveyAsyncAggregateQueryResponse**](SurveyAsyncAggregateQueryResponse) get_analytics_surveys_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async aggregates query

get_analytics_surveys_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/surveys/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:surveyAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_surveys_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_surveys_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**SurveyAsyncAggregateQueryResponse**](SurveyAsyncAggregateQueryResponse)


## get_analytics_taskmanagement_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_taskmanagement_aggregates_job(job_id)


Get status for async query for task management aggregates

get_analytics_taskmanagement_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/taskmanagement/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:taskManagementAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for task management aggregates
    api_response = api_instance.get_analytics_taskmanagement_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_taskmanagement_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_taskmanagement_aggregates_job_results

> [**TaskManagementAsyncAggregateQueryResponse**](TaskManagementAsyncAggregateQueryResponse) get_analytics_taskmanagement_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async task management query

get_analytics_taskmanagement_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/taskmanagement/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:taskManagementAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async task management query
    api_response = api_instance.get_analytics_taskmanagement_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_taskmanagement_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**TaskManagementAsyncAggregateQueryResponse**](TaskManagementAsyncAggregateQueryResponse)


## get_analytics_transcripts_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_transcripts_aggregates_job(job_id)


Get status for async query for transcript aggregates

get_analytics_transcripts_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/transcripts/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:speechAndTextAnalyticsAggregates:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for transcript aggregates
    api_response = api_instance.get_analytics_transcripts_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_transcripts_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_transcripts_aggregates_job_results

> [**TranscriptAsyncAggregateQueryResponse**](TranscriptAsyncAggregateQueryResponse) get_analytics_transcripts_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async aggregates query

get_analytics_transcripts_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/transcripts/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:speechAndTextAnalyticsAggregates:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_transcripts_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_transcripts_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**TranscriptAsyncAggregateQueryResponse**](TranscriptAsyncAggregateQueryResponse)


## get_analytics_users_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_users_aggregates_job(job_id)


Get status for async query for user aggregates

get_analytics_users_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/users/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:userAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for user aggregates
    api_response = api_instance.get_analytics_users_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_users_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_users_aggregates_job_results

> [**UserAsyncAggregateQueryResponse**](UserAsyncAggregateQueryResponse) get_analytics_users_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async aggregates query

get_analytics_users_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/users/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:userAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_users_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_users_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**UserAsyncAggregateQueryResponse**](UserAsyncAggregateQueryResponse)


## get_analytics_users_details_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_analytics_users_details_job(job_id)


Get status for async query for user details

Wraps GET /api/v2/analytics/users/details/jobs/{jobId} 

Requires ANY permissions: 

* analytics:userDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for user details
    api_response = api_instance.get_analytics_users_details_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_users_details_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_analytics_users_details_job_results

> [**AnalyticsUserDetailsAsyncQueryResponse**](AnalyticsUserDetailsAsyncQueryResponse) get_analytics_users_details_job_results(job_id, cursor=cursor, page_size=page_size)


Fetch a page of results for an async query

Wraps GET /api/v2/analytics/users/details/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:userDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page) (optional)
page_size = 56 # int | The desired maximum number of results (optional)

try:
    # Fetch a page of results for an async query
    api_response = api_instance.get_analytics_users_details_job_results(job_id, cursor=cursor, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_users_details_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page) | [optional]  |
| **page_size** | **int**| The desired maximum number of results | [optional]  |

### Return type

[**AnalyticsUserDetailsAsyncQueryResponse**](AnalyticsUserDetailsAsyncQueryResponse)


## get_analytics_users_details_jobs_availability

> [**DataAvailabilityResponse**](DataAvailabilityResponse) get_analytics_users_details_jobs_availability()


Lookup the datalake availability date and time

Wraps GET /api/v2/analytics/users/details/jobs/availability 

Requires ANY permissions: 

* analytics:userDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()

try:
    # Lookup the datalake availability date and time
    api_response = api_instance.get_analytics_users_details_jobs_availability()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_analytics_users_details_jobs_availability: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**DataAvailabilityResponse**](DataAvailabilityResponse)


## patch_analytics_reporting_settings

> [**AnalyticsReportingSettings**](AnalyticsReportingSettings) patch_analytics_reporting_settings(body)


Patch AnalyticsReportingSettings values for an organization

Wraps PATCH /api/v2/analytics/reporting/settings 

Requires ANY permissions: 

* analytics:reportingSettings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.AnalyticsReportingSettings() # AnalyticsReportingSettings | AnalyticsReportingSettingsRequest

try:
    # Patch AnalyticsReportingSettings values for an organization
    api_response = api_instance.patch_analytics_reporting_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->patch_analytics_reporting_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AnalyticsReportingSettings**](AnalyticsReportingSettings)| AnalyticsReportingSettingsRequest |  |

### Return type

[**AnalyticsReportingSettings**](AnalyticsReportingSettings)


## post_analytics_actions_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_actions_aggregates_jobs(body)


Query for action aggregates asynchronously

post_analytics_actions_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/actions/aggregates/jobs 

Requires ANY permissions: 

* integrations:action:view
* bridge:actions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.ActionAsyncAggregationQuery() # ActionAsyncAggregationQuery | query

try:
    # Query for action aggregates asynchronously
    api_response = api_instance.post_analytics_actions_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_actions_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ActionAsyncAggregationQuery**](ActionAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_actions_aggregates_query

> [**ActionAggregateQueryResponse**](ActionAggregateQueryResponse) post_analytics_actions_aggregates_query(body)


Query for action aggregates

Wraps POST /api/v2/analytics/actions/aggregates/query 

Requires ANY permissions: 

* integrations:action:view
* bridge:actions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.ActionAggregationQuery() # ActionAggregationQuery | query

try:
    # Query for action aggregates
    api_response = api_instance.post_analytics_actions_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_actions_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ActionAggregationQuery**](ActionAggregationQuery)| query |  |

### Return type

[**ActionAggregateQueryResponse**](ActionAggregateQueryResponse)


## post_analytics_agentcopilots_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_agentcopilots_aggregates_jobs(body)


Query for agent copilot aggregates asynchronously

post_analytics_agentcopilots_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/agentcopilots/aggregates/jobs 

Requires ANY permissions: 

* analytics:agentCopilotAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.AgentCopilotAsyncAggregationQuery() # AgentCopilotAsyncAggregationQuery | query

try:
    # Query for agent copilot aggregates asynchronously
    api_response = api_instance.post_analytics_agentcopilots_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_agentcopilots_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AgentCopilotAsyncAggregationQuery**](AgentCopilotAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_agentcopilots_aggregates_query

> [**AgentCopilotAggregateQueryResponse**](AgentCopilotAggregateQueryResponse) post_analytics_agentcopilots_aggregates_query(body)


Query for agent copilot aggregates

Wraps POST /api/v2/analytics/agentcopilots/aggregates/query 

Requires ANY permissions: 

* analytics:agentCopilotAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.AgentCopilotAggregationQuery() # AgentCopilotAggregationQuery | query

try:
    # Query for agent copilot aggregates
    api_response = api_instance.post_analytics_agentcopilots_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_agentcopilots_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AgentCopilotAggregationQuery**](AgentCopilotAggregationQuery)| query |  |

### Return type

[**AgentCopilotAggregateQueryResponse**](AgentCopilotAggregateQueryResponse)


## post_analytics_agents_status_counts

> [**AnalyticsAgentStateCountsResponse**](AnalyticsAgentStateCountsResponse) post_analytics_agents_status_counts(body, group_by=group_by)


Count agents by different groupings

Wraps POST /api/v2/analytics/agents/status/counts 

Requires ANY permissions: 

* analytics:agentState:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.AgentStateCountsRequest() # AgentStateCountsRequest | query
group_by = ['group_by_example'] # list[str] | Include to choose which groupings to count by and return. If not included it will return only counts grouped by segmentType (optional)

try:
    # Count agents by different groupings
    api_response = api_instance.post_analytics_agents_status_counts(body, group_by=group_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_agents_status_counts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AgentStateCountsRequest**](AgentStateCountsRequest)| query |  |
| **group_by** | [**list[str]**](str)| Include to choose which groupings to count by and return. If not included it will return only counts grouped by segmentType | [optional] <br />**Values**: segmentType, presence, routingStatus, isOutOfOffice |

### Return type

[**AnalyticsAgentStateCountsResponse**](AnalyticsAgentStateCountsResponse)


## post_analytics_agents_status_query

> [**AnalyticsAgentStateQueryResponse**](AnalyticsAgentStateQueryResponse) post_analytics_agents_status_query(body)


Retrieve the top 50 agents matching the query filters

Wraps POST /api/v2/analytics/agents/status/query 

Requires ANY permissions: 

* analytics:agentState:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.AgentStateQueryRequest() # AgentStateQueryRequest | query

try:
    # Retrieve the top 50 agents matching the query filters
    api_response = api_instance.post_analytics_agents_status_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_agents_status_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AgentStateQueryRequest**](AgentStateQueryRequest)| query |  |

### Return type

[**AnalyticsAgentStateQueryResponse**](AnalyticsAgentStateQueryResponse)


## post_analytics_bots_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_bots_aggregates_jobs(body)


Query for bot aggregates asynchronously

post_analytics_bots_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/bots/aggregates/jobs 

Requires ANY permissions: 

* analytics:botAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.BotAsyncAggregationQuery() # BotAsyncAggregationQuery | query

try:
    # Query for bot aggregates asynchronously
    api_response = api_instance.post_analytics_bots_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_bots_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BotAsyncAggregationQuery**](BotAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_bots_aggregates_query

> [**BotAggregateQueryResponse**](BotAggregateQueryResponse) post_analytics_bots_aggregates_query(body)


Query for bot aggregates

Wraps POST /api/v2/analytics/bots/aggregates/query 

Requires ANY permissions: 

* analytics:botAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.BotAggregationQuery() # BotAggregationQuery | query

try:
    # Query for bot aggregates
    api_response = api_instance.post_analytics_bots_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_bots_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BotAggregationQuery**](BotAggregationQuery)| query |  |

### Return type

[**BotAggregateQueryResponse**](BotAggregateQueryResponse)


## post_analytics_casemanagement_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_casemanagement_aggregates_jobs(body)


Query for case management aggregates asynchronously

post_analytics_casemanagement_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/casemanagement/aggregates/jobs 

Requires ANY permissions: 

* analytics:caseManagementAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.CaseManagementAsyncAggregationQuery() # CaseManagementAsyncAggregationQuery | query

try:
    # Query for case management aggregates asynchronously
    api_response = api_instance.post_analytics_casemanagement_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_casemanagement_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CaseManagementAsyncAggregationQuery**](CaseManagementAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_casemanagement_aggregates_query

> [**CaseManagementAggregateQueryResponse**](CaseManagementAggregateQueryResponse) post_analytics_casemanagement_aggregates_query(body)


Query for case management aggregates

post_analytics_casemanagement_aggregates_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/casemanagement/aggregates/query 

Requires ANY permissions: 

* analytics:caseManagementAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.CaseManagementAggregationQuery() # CaseManagementAggregationQuery | query

try:
    # Query for case management aggregates
    api_response = api_instance.post_analytics_casemanagement_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_casemanagement_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CaseManagementAggregationQuery**](CaseManagementAggregationQuery)| query |  |

### Return type

[**CaseManagementAggregateQueryResponse**](CaseManagementAggregateQueryResponse)


## post_analytics_conversation_details_properties

> [**PropertyIndexRequest**](PropertyIndexRequest) post_analytics_conversation_details_properties(conversation_id, body)


Index conversation properties

Wraps POST /api/v2/analytics/conversations/{conversationId}/details/properties 

Requires ANY permissions: 

* analytics:conversationProperties:index

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.PropertyIndexRequest() # PropertyIndexRequest | request

try:
    # Index conversation properties
    api_response = api_instance.post_analytics_conversation_details_properties(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_conversation_details_properties: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**PropertyIndexRequest**](PropertyIndexRequest)| request |  |

### Return type

[**PropertyIndexRequest**](PropertyIndexRequest)


## post_analytics_conversations_activity_query

> [**ConversationActivityResponse**](ConversationActivityResponse) post_analytics_conversations_activity_query(body, page_size=page_size, page_number=page_number)


Query for conversation activity observations

Wraps POST /api/v2/analytics/conversations/activity/query 

Requires ANY permissions: 

* analytics:queueObservation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.ConversationActivityQuery() # ConversationActivityQuery | query
page_size = 56 # int | The desired page size (optional)
page_number = 56 # int | The desired page number (optional)

try:
    # Query for conversation activity observations
    api_response = api_instance.post_analytics_conversations_activity_query(body, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_conversations_activity_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationActivityQuery**](ConversationActivityQuery)| query |  |
| **page_size** | **int**| The desired page size | [optional]  |
| **page_number** | **int**| The desired page number | [optional]  |

### Return type

[**ConversationActivityResponse**](ConversationActivityResponse)


## post_analytics_conversations_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_conversations_aggregates_jobs(body)


Query for conversation aggregates asynchronously

post_analytics_conversations_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/conversations/aggregates/jobs 

Requires ANY permissions: 

* analytics:conversationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.ConversationAsyncAggregationQuery() # ConversationAsyncAggregationQuery | query

try:
    # Query for conversation aggregates asynchronously
    api_response = api_instance.post_analytics_conversations_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_conversations_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationAsyncAggregationQuery**](ConversationAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_conversations_aggregates_query

> [**ConversationAggregateQueryResponse**](ConversationAggregateQueryResponse) post_analytics_conversations_aggregates_query(body)


Query for conversation aggregates

Wraps POST /api/v2/analytics/conversations/aggregates/query 

Requires ANY permissions: 

* analytics:conversationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.ConversationAggregationQuery() # ConversationAggregationQuery | query

try:
    # Query for conversation aggregates
    api_response = api_instance.post_analytics_conversations_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_conversations_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationAggregationQuery**](ConversationAggregationQuery)| query |  |

### Return type

[**ConversationAggregateQueryResponse**](ConversationAggregateQueryResponse)


## post_analytics_conversations_details_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_conversations_details_jobs(body)


Query for conversation details asynchronously

Wraps POST /api/v2/analytics/conversations/details/jobs 

Requires ANY permissions: 

* analytics:conversationDetail:view
* analytics:agentConversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.AsyncConversationQuery() # AsyncConversationQuery | query

try:
    # Query for conversation details asynchronously
    api_response = api_instance.post_analytics_conversations_details_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_conversations_details_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AsyncConversationQuery**](AsyncConversationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_conversations_details_query

> [**AnalyticsConversationQueryResponse**](AnalyticsConversationQueryResponse) post_analytics_conversations_details_query(body)


Query for conversation details

Wraps POST /api/v2/analytics/conversations/details/query 

Requires ANY permissions: 

* analytics:conversationDetail:view
* analytics:agentConversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.ConversationQuery() # ConversationQuery | query

try:
    # Query for conversation details
    api_response = api_instance.post_analytics_conversations_details_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_conversations_details_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationQuery**](ConversationQuery)| query |  |

### Return type

[**AnalyticsConversationQueryResponse**](AnalyticsConversationQueryResponse)


## post_analytics_dataextraction_downloads_bulk

> [**DataExtractionFileUrlListing**](DataExtractionFileUrlListing) post_analytics_dataextraction_downloads_bulk(body)


Get download URLs for analytics data warehouse files

post_analytics_dataextraction_downloads_bulk is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/dataextraction/downloads/bulk 

Requires ANY permissions: 

* analytics:datawarehouse:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.DownloadServiceRequest() # DownloadServiceRequest | request

try:
    # Get download URLs for analytics data warehouse files
    api_response = api_instance.post_analytics_dataextraction_downloads_bulk(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_dataextraction_downloads_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DownloadServiceRequest**](DownloadServiceRequest)| request |  |

### Return type

[**DataExtractionFileUrlListing**](DataExtractionFileUrlListing)


## post_analytics_evaluations_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_evaluations_aggregates_jobs(body)


Query for evaluation aggregates asynchronously

post_analytics_evaluations_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/evaluations/aggregates/jobs 

Requires ANY permissions: 

* analytics:evaluationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.EvaluationAsyncAggregationQuery() # EvaluationAsyncAggregationQuery | query

try:
    # Query for evaluation aggregates asynchronously
    api_response = api_instance.post_analytics_evaluations_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_evaluations_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EvaluationAsyncAggregationQuery**](EvaluationAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_evaluations_aggregates_query

> [**EvaluationAggregateQueryResponse**](EvaluationAggregateQueryResponse) post_analytics_evaluations_aggregates_query(body)


Query for evaluation aggregates

Wraps POST /api/v2/analytics/evaluations/aggregates/query 

Requires ANY permissions: 

* analytics:evaluationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.EvaluationAggregationQuery() # EvaluationAggregationQuery | query

try:
    # Query for evaluation aggregates
    api_response = api_instance.post_analytics_evaluations_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_evaluations_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EvaluationAggregationQuery**](EvaluationAggregationQuery)| query |  |

### Return type

[**EvaluationAggregateQueryResponse**](EvaluationAggregateQueryResponse)


## post_analytics_flowexecutions_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_flowexecutions_aggregates_jobs(body)


Query for flow execution aggregates asynchronously

post_analytics_flowexecutions_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/flowexecutions/aggregates/jobs 

Requires ANY permissions: 

* analytics:flowExecutionAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.FlowExecutionAsyncAggregationQuery() # FlowExecutionAsyncAggregationQuery | query

try:
    # Query for flow execution aggregates asynchronously
    api_response = api_instance.post_analytics_flowexecutions_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_flowexecutions_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowExecutionAsyncAggregationQuery**](FlowExecutionAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_flowexecutions_aggregates_query

> [**FlowExecutionAggregateQueryResponse**](FlowExecutionAggregateQueryResponse) post_analytics_flowexecutions_aggregates_query(body)


Query for flow execution aggregates

Wraps POST /api/v2/analytics/flowexecutions/aggregates/query 

Requires ANY permissions: 

* analytics:flowExecutionAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.FlowExecutionAggregationQuery() # FlowExecutionAggregationQuery | query

try:
    # Query for flow execution aggregates
    api_response = api_instance.post_analytics_flowexecutions_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_flowexecutions_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowExecutionAggregationQuery**](FlowExecutionAggregationQuery)| query |  |

### Return type

[**FlowExecutionAggregateQueryResponse**](FlowExecutionAggregateQueryResponse)


## post_analytics_flows_activity_query

> [**FlowActivityResponse**](FlowActivityResponse) post_analytics_flows_activity_query(body, page_size=page_size, page_number=page_number)


Query for flow activity observations

Wraps POST /api/v2/analytics/flows/activity/query 

Requires ANY permissions: 

* analytics:flowObservation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.FlowActivityQuery() # FlowActivityQuery | query
page_size = 56 # int | The desired page size (optional)
page_number = 56 # int | The desired page number (optional)

try:
    # Query for flow activity observations
    api_response = api_instance.post_analytics_flows_activity_query(body, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_flows_activity_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowActivityQuery**](FlowActivityQuery)| query |  |
| **page_size** | **int**| The desired page size | [optional]  |
| **page_number** | **int**| The desired page number | [optional]  |

### Return type

[**FlowActivityResponse**](FlowActivityResponse)


## post_analytics_flows_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_flows_aggregates_jobs(body)


Query for flow aggregates asynchronously

post_analytics_flows_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/flows/aggregates/jobs 

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
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.FlowAsyncAggregationQuery() # FlowAsyncAggregationQuery | query

try:
    # Query for flow aggregates asynchronously
    api_response = api_instance.post_analytics_flows_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_flows_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowAsyncAggregationQuery**](FlowAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_flows_aggregates_query

> [**FlowAggregateQueryResponse**](FlowAggregateQueryResponse) post_analytics_flows_aggregates_query(body)


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
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.FlowAggregationQuery() # FlowAggregationQuery | query

try:
    # Query for flow aggregates
    api_response = api_instance.post_analytics_flows_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_flows_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowAggregationQuery**](FlowAggregationQuery)| query |  |

### Return type

[**FlowAggregateQueryResponse**](FlowAggregateQueryResponse)


## post_analytics_flows_observations_query

> [**FlowObservationQueryResponse**](FlowObservationQueryResponse) post_analytics_flows_observations_query(body)


Query for flow observations

Wraps POST /api/v2/analytics/flows/observations/query 

Requires ANY permissions: 

* analytics:flowObservation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.FlowObservationQuery() # FlowObservationQuery | query

try:
    # Query for flow observations
    api_response = api_instance.post_analytics_flows_observations_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_flows_observations_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowObservationQuery**](FlowObservationQuery)| query |  |

### Return type

[**FlowObservationQueryResponse**](FlowObservationQueryResponse)


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
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.JourneyAsyncAggregationQuery() # JourneyAsyncAggregationQuery | query

try:
    # Query for journey aggregates asynchronously
    api_response = api_instance.post_analytics_journeys_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_journeys_aggregates_jobs: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.JourneyAggregationQuery() # JourneyAggregationQuery | query

try:
    # Query for journey aggregates
    api_response = api_instance.post_analytics_journeys_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_journeys_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**JourneyAggregationQuery**](JourneyAggregationQuery)| query |  |

### Return type

[**JourneyAggregateQueryResponse**](JourneyAggregateQueryResponse)


## post_analytics_knowledge_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_knowledge_aggregates_jobs(body)


Query for knowledge aggregates asynchronously

post_analytics_knowledge_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/knowledge/aggregates/jobs 

Requires ANY permissions: 

* analytics:knowledgeAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.KnowledgeAsyncAggregationQuery() # KnowledgeAsyncAggregationQuery | query

try:
    # Query for knowledge aggregates asynchronously
    api_response = api_instance.post_analytics_knowledge_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_knowledge_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**KnowledgeAsyncAggregationQuery**](KnowledgeAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_knowledge_aggregates_query

> [**KnowledgeAggregateQueryResponse**](KnowledgeAggregateQueryResponse) post_analytics_knowledge_aggregates_query(body)


Query for knowledge aggregates

Wraps POST /api/v2/analytics/knowledge/aggregates/query 

Requires ANY permissions: 

* analytics:knowledgeAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.KnowledgeAggregationQuery() # KnowledgeAggregationQuery | query

try:
    # Query for knowledge aggregates
    api_response = api_instance.post_analytics_knowledge_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_knowledge_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**KnowledgeAggregationQuery**](KnowledgeAggregationQuery)| query |  |

### Return type

[**KnowledgeAggregateQueryResponse**](KnowledgeAggregateQueryResponse)


## post_analytics_queues_observations_query

> [**QueueObservationQueryResponse**](QueueObservationQueryResponse) post_analytics_queues_observations_query(body)


Query for queue observations

Wraps POST /api/v2/analytics/queues/observations/query 

Requires ANY permissions: 

* analytics:queueObservation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.QueueObservationQuery() # QueueObservationQuery | query

try:
    # Query for queue observations
    api_response = api_instance.post_analytics_queues_observations_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_queues_observations_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**QueueObservationQuery**](QueueObservationQuery)| query |  |

### Return type

[**QueueObservationQueryResponse**](QueueObservationQueryResponse)


## post_analytics_ratelimits_aggregates_query

> [**RateLimitAggregateQueryResponse**](RateLimitAggregateQueryResponse) post_analytics_ratelimits_aggregates_query(body)


Query for limits rate limit aggregates. Data populated when limits reach 90% of the maximum. Not a source of truth for limits hit but a best effort estimate.

The 'max' property can be used to determine estimated rate limit value hit. See https://developer.genesys.cloud/organization/organization/limits#available-limits for limits that are trackable (Operational Events Enabled).

Wraps POST /api/v2/analytics/ratelimits/aggregates/query 

Requires ANY permissions: 

* analytics:rateLimitAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.RateLimitAggregationQuery() # RateLimitAggregationQuery | query

try:
    # Query for limits rate limit aggregates. Data populated when limits reach 90% of the maximum. Not a source of truth for limits hit but a best effort estimate.
    api_response = api_instance.post_analytics_ratelimits_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_ratelimits_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RateLimitAggregationQuery**](RateLimitAggregationQuery)| query |  |

### Return type

[**RateLimitAggregateQueryResponse**](RateLimitAggregateQueryResponse)


## post_analytics_reporting_dashboards_users_bulk_remove

>  post_analytics_reporting_dashboards_users_bulk_remove(body)


Bulk soft delete dashboards owned by other user(s)

Wraps POST /api/v2/analytics/reporting/dashboards/users/bulk/remove 

Requires ANY permissions: 

* analytics:dashboardConfigurations:deleteActive
* analytics:dashboardConfigurations:deleteInactive

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = ['body_example'] # list[str] | List of userIds

try:
    # Bulk soft delete dashboards owned by other user(s)
    api_instance.post_analytics_reporting_dashboards_users_bulk_remove(body)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_reporting_dashboards_users_bulk_remove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**list[str]**](str)| List of userIds |  |

### Return type

void (empty response body)


## post_analytics_reporting_exports

> [**ReportingExportJobResponse**](ReportingExportJobResponse) post_analytics_reporting_exports(body)


Generate a view export request

This API creates a reporting export but the desired way to export analytics data is to use the analytics query APIs instead

Wraps POST /api/v2/analytics/reporting/exports 

Requires ALL permissions: 

* analytics:dataExport:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.ReportingExportJobRequest() # ReportingExportJobRequest | ReportingExportJobRequest

try:
    # Generate a view export request
    api_response = api_instance.post_analytics_reporting_exports(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_reporting_exports: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ReportingExportJobRequest**](ReportingExportJobRequest)| ReportingExportJobRequest |  |

### Return type

[**ReportingExportJobResponse**](ReportingExportJobResponse)


## post_analytics_reporting_settings_dashboards_bulk_remove

>  post_analytics_reporting_settings_dashboards_bulk_remove(body)


Bulk soft delete dashboard configurations

Wraps POST /api/v2/analytics/reporting/settings/dashboards/bulk/remove 

Requires ALL permissions: 

* analytics:dashboardConfigurations:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.DashboardConfigurationBulkRequest() # DashboardConfigurationBulkRequest | 

try:
    # Bulk soft delete dashboard configurations
    api_instance.post_analytics_reporting_settings_dashboards_bulk_remove(body)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_reporting_settings_dashboards_bulk_remove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DashboardConfigurationBulkRequest**](DashboardConfigurationBulkRequest)|  |  |

### Return type

void (empty response body)


## post_analytics_reporting_settings_dashboards_query

> [**DashboardConfigurationListing**](DashboardConfigurationListing) post_analytics_reporting_settings_dashboards_query(body)


Query dashboard configurations

Wraps POST /api/v2/analytics/reporting/settings/dashboards/query 

Requires ALL permissions: 

* analytics:dashboardConfigurations:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.DashboardConfigurationQueryRequest() # DashboardConfigurationQueryRequest | 

try:
    # Query dashboard configurations
    api_response = api_instance.post_analytics_reporting_settings_dashboards_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_reporting_settings_dashboards_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DashboardConfigurationQueryRequest**](DashboardConfigurationQueryRequest)|  |  |

### Return type

[**DashboardConfigurationListing**](DashboardConfigurationListing)


## post_analytics_resolutions_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_resolutions_aggregates_jobs(body)


Query for resolution aggregates asynchronously

post_analytics_resolutions_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/resolutions/aggregates/jobs 

Requires ANY permissions: 

* analytics:resolutionAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.ResolutionAsyncAggregationQuery() # ResolutionAsyncAggregationQuery | query

try:
    # Query for resolution aggregates asynchronously
    api_response = api_instance.post_analytics_resolutions_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_resolutions_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ResolutionAsyncAggregationQuery**](ResolutionAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_resolutions_aggregates_query

> [**ResolutionAggregateQueryResponse**](ResolutionAggregateQueryResponse) post_analytics_resolutions_aggregates_query(body)


Query for resolution aggregates

Wraps POST /api/v2/analytics/resolutions/aggregates/query 

Requires ANY permissions: 

* analytics:resolutionAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.ResolutionAggregationQuery() # ResolutionAggregationQuery | query

try:
    # Query for resolution aggregates
    api_response = api_instance.post_analytics_resolutions_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_resolutions_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ResolutionAggregationQuery**](ResolutionAggregationQuery)| query |  |

### Return type

[**ResolutionAggregateQueryResponse**](ResolutionAggregateQueryResponse)


## post_analytics_routing_activity_query

> [**RoutingActivityResponse**](RoutingActivityResponse) post_analytics_routing_activity_query(body, page_size=page_size, page_number=page_number)


Query for user activity observations

Wraps POST /api/v2/analytics/routing/activity/query 

Requires ANY permissions: 

* analytics:queueObservation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.RoutingActivityQuery() # RoutingActivityQuery | query
page_size = 56 # int | The desired page size (optional)
page_number = 56 # int | The desired page number (optional)

try:
    # Query for user activity observations
    api_response = api_instance.post_analytics_routing_activity_query(body, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_routing_activity_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RoutingActivityQuery**](RoutingActivityQuery)| query |  |
| **page_size** | **int**| The desired page size | [optional]  |
| **page_number** | **int**| The desired page number | [optional]  |

### Return type

[**RoutingActivityResponse**](RoutingActivityResponse)


## post_analytics_summaries_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_summaries_aggregates_jobs(body)


Query for summary aggregates asynchronously

post_analytics_summaries_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/summaries/aggregates/jobs 

Requires ANY permissions: 

* analytics:summaryAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.SummaryAsyncAggregationQuery() # SummaryAsyncAggregationQuery | query

try:
    # Query for summary aggregates asynchronously
    api_response = api_instance.post_analytics_summaries_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_summaries_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SummaryAsyncAggregationQuery**](SummaryAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_summaries_aggregates_query

> [**SummaryAggregateQueryResponse**](SummaryAggregateQueryResponse) post_analytics_summaries_aggregates_query(body)


Query for summary aggregates

Wraps POST /api/v2/analytics/summaries/aggregates/query 

Requires ANY permissions: 

* analytics:summaryAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.SummaryAggregationQuery() # SummaryAggregationQuery | query

try:
    # Query for summary aggregates
    api_response = api_instance.post_analytics_summaries_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_summaries_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SummaryAggregationQuery**](SummaryAggregationQuery)| query |  |

### Return type

[**SummaryAggregateQueryResponse**](SummaryAggregateQueryResponse)


## post_analytics_surveys_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_surveys_aggregates_jobs(body)


Query for survey aggregates asynchronously

post_analytics_surveys_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/surveys/aggregates/jobs 

Requires ANY permissions: 

* analytics:surveyAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.SurveyAsyncAggregationQuery() # SurveyAsyncAggregationQuery | query

try:
    # Query for survey aggregates asynchronously
    api_response = api_instance.post_analytics_surveys_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_surveys_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SurveyAsyncAggregationQuery**](SurveyAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_surveys_aggregates_query

> [**SurveyAggregateQueryResponse**](SurveyAggregateQueryResponse) post_analytics_surveys_aggregates_query(body)


Query for survey aggregates

Wraps POST /api/v2/analytics/surveys/aggregates/query 

Requires ANY permissions: 

* analytics:surveyAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.SurveyAggregationQuery() # SurveyAggregationQuery | query

try:
    # Query for survey aggregates
    api_response = api_instance.post_analytics_surveys_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_surveys_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SurveyAggregationQuery**](SurveyAggregationQuery)| query |  |

### Return type

[**SurveyAggregateQueryResponse**](SurveyAggregateQueryResponse)


## post_analytics_taskmanagement_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_taskmanagement_aggregates_jobs(body)


Query for task management aggregates asynchronously

post_analytics_taskmanagement_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/taskmanagement/aggregates/jobs 

Requires ANY permissions: 

* analytics:taskManagementAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.TaskManagementAsyncAggregationQuery() # TaskManagementAsyncAggregationQuery | query

try:
    # Query for task management aggregates asynchronously
    api_response = api_instance.post_analytics_taskmanagement_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_taskmanagement_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TaskManagementAsyncAggregationQuery**](TaskManagementAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_taskmanagement_aggregates_query

> [**TaskManagementAggregateQueryResponse**](TaskManagementAggregateQueryResponse) post_analytics_taskmanagement_aggregates_query(body)


Query for task management aggregates

Wraps POST /api/v2/analytics/taskmanagement/aggregates/query 

Requires ANY permissions: 

* analytics:taskManagementAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.TaskManagementAggregationQuery() # TaskManagementAggregationQuery | query

try:
    # Query for task management aggregates
    api_response = api_instance.post_analytics_taskmanagement_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_taskmanagement_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TaskManagementAggregationQuery**](TaskManagementAggregationQuery)| query |  |

### Return type

[**TaskManagementAggregateQueryResponse**](TaskManagementAggregateQueryResponse)


## post_analytics_teams_activity_query

> [**TeamActivityResponse**](TeamActivityResponse) post_analytics_teams_activity_query(body, page_size=page_size, page_number=page_number)


Query for team activity observations

Wraps POST /api/v2/analytics/teams/activity/query 

Requires ANY permissions: 

* analytics:teamObservation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.TeamActivityQuery() # TeamActivityQuery | query
page_size = 56 # int | The desired page size (optional)
page_number = 56 # int | The desired page number (optional)

try:
    # Query for team activity observations
    api_response = api_instance.post_analytics_teams_activity_query(body, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_teams_activity_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TeamActivityQuery**](TeamActivityQuery)| query |  |
| **page_size** | **int**| The desired page size | [optional]  |
| **page_number** | **int**| The desired page number | [optional]  |

### Return type

[**TeamActivityResponse**](TeamActivityResponse)


## post_analytics_transcripts_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_transcripts_aggregates_jobs(body)


Query for transcript aggregates asynchronously

post_analytics_transcripts_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/transcripts/aggregates/jobs 

Requires ANY permissions: 

* analytics:speechAndTextAnalyticsAggregates:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.TranscriptAsyncAggregationQuery() # TranscriptAsyncAggregationQuery | query

try:
    # Query for transcript aggregates asynchronously
    api_response = api_instance.post_analytics_transcripts_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_transcripts_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TranscriptAsyncAggregationQuery**](TranscriptAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_transcripts_aggregates_query

> [**TranscriptAggregateQueryResponse**](TranscriptAggregateQueryResponse) post_analytics_transcripts_aggregates_query(body)


Query for transcript aggregates

Wraps POST /api/v2/analytics/transcripts/aggregates/query 

Requires ANY permissions: 

* analytics:speechAndTextAnalyticsAggregates:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.TranscriptAggregationQuery() # TranscriptAggregationQuery | query

try:
    # Query for transcript aggregates
    api_response = api_instance.post_analytics_transcripts_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_transcripts_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TranscriptAggregationQuery**](TranscriptAggregationQuery)| query |  |

### Return type

[**TranscriptAggregateQueryResponse**](TranscriptAggregateQueryResponse)


## post_analytics_users_activity_query

> [**UserActivityResponse**](UserActivityResponse) post_analytics_users_activity_query(body, page_size=page_size, page_number=page_number)


Query for user activity observations

Wraps POST /api/v2/analytics/users/activity/query 

Requires ANY permissions: 

* analytics:userObservation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.UserActivityQuery() # UserActivityQuery | query
page_size = 56 # int | The desired page size (optional)
page_number = 56 # int | The desired page number (optional)

try:
    # Query for user activity observations
    api_response = api_instance.post_analytics_users_activity_query(body, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_users_activity_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserActivityQuery**](UserActivityQuery)| query |  |
| **page_size** | **int**| The desired page size | [optional]  |
| **page_number** | **int**| The desired page number | [optional]  |

### Return type

[**UserActivityResponse**](UserActivityResponse)


## post_analytics_users_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_users_aggregates_jobs(body)


Query for user aggregates asynchronously

post_analytics_users_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/users/aggregates/jobs 

Requires ANY permissions: 

* analytics:userAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.UserAsyncAggregationQuery() # UserAsyncAggregationQuery | query

try:
    # Query for user aggregates asynchronously
    api_response = api_instance.post_analytics_users_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_users_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserAsyncAggregationQuery**](UserAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_users_aggregates_query

> [**UserAggregateQueryResponse**](UserAggregateQueryResponse) post_analytics_users_aggregates_query(body)


Query for user aggregates

Wraps POST /api/v2/analytics/users/aggregates/query 

Requires ANY permissions: 

* analytics:userAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.UserAggregationQuery() # UserAggregationQuery | query

try:
    # Query for user aggregates
    api_response = api_instance.post_analytics_users_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_users_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserAggregationQuery**](UserAggregationQuery)| query |  |

### Return type

[**UserAggregateQueryResponse**](UserAggregateQueryResponse)


## post_analytics_users_details_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_analytics_users_details_jobs(body)


Query for user details asynchronously

Wraps POST /api/v2/analytics/users/details/jobs 

Requires ANY permissions: 

* analytics:userDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.AsyncUserDetailsQuery() # AsyncUserDetailsQuery | query

try:
    # Query for user details asynchronously
    api_response = api_instance.post_analytics_users_details_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_users_details_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AsyncUserDetailsQuery**](AsyncUserDetailsQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_analytics_users_details_query

> [**AnalyticsUserDetailsQueryResponse**](AnalyticsUserDetailsQueryResponse) post_analytics_users_details_query(body)


Query for user details

Wraps POST /api/v2/analytics/users/details/query 

Requires ANY permissions: 

* analytics:userDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.UserDetailsQuery() # UserDetailsQuery | query

try:
    # Query for user details
    api_response = api_instance.post_analytics_users_details_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_users_details_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserDetailsQuery**](UserDetailsQuery)| query |  |

### Return type

[**AnalyticsUserDetailsQueryResponse**](AnalyticsUserDetailsQueryResponse)


## post_analytics_users_observations_query

> [**UserObservationQueryResponse**](UserObservationQueryResponse) post_analytics_users_observations_query(body)


Query for user observations

Wraps POST /api/v2/analytics/users/observations/query 

Requires ANY permissions: 

* analytics:userObservation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.UserObservationQuery() # UserObservationQuery | query

try:
    # Query for user observations
    api_response = api_instance.post_analytics_users_observations_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->post_analytics_users_observations_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserObservationQuery**](UserObservationQuery)| query |  |

### Return type

[**UserObservationQueryResponse**](UserObservationQueryResponse)


## put_analytics_dataretention_settings

> [**AnalyticsDataRetentionResponse**](AnalyticsDataRetentionResponse) put_analytics_dataretention_settings(body)


Update analytics data retention setting

Wraps PUT /api/v2/analytics/dataretention/settings 

Requires ANY permissions: 

* analytics:dataRetention:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.UpdateAnalyticsDataRetentionRequest() # UpdateAnalyticsDataRetentionRequest | retentionDays

try:
    # Update analytics data retention setting
    api_response = api_instance.put_analytics_dataretention_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->put_analytics_dataretention_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UpdateAnalyticsDataRetentionRequest**](UpdateAnalyticsDataRetentionRequest)| retentionDays |  |

### Return type

[**AnalyticsDataRetentionResponse**](AnalyticsDataRetentionResponse)


_PureCloudPlatformClientV2 247.0.0_

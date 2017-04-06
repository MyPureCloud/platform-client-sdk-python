---
title: AnalyticsApi
---

## PureCloudPlatformClientV2.AnalyticsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_analytics_reporting_schedule**](AnalyticsApi.html#delete_analytics_reporting_schedule) | Delete a scheduled report job.|
|[**get_analytics_conversation_details**](AnalyticsApi.html#get_analytics_conversation_details) | Get a conversation by id|
|[**get_analytics_reporting_metadata**](AnalyticsApi.html#get_analytics_reporting_metadata) | Get list of reporting metadata.|
|[**get_analytics_reporting_report_id_metadata**](AnalyticsApi.html#get_analytics_reporting_report_id_metadata) | Get a reporting metadata.|
|[**get_analytics_reporting_reportformats**](AnalyticsApi.html#get_analytics_reporting_reportformats) | Get a list of report formats|
|[**get_analytics_reporting_schedule**](AnalyticsApi.html#get_analytics_reporting_schedule) | Get a scheduled report job.|
|[**get_analytics_reporting_schedule_history**](AnalyticsApi.html#get_analytics_reporting_schedule_history) | Get list of completed scheduled report jobs.|
|[**get_analytics_reporting_schedule_history_latest**](AnalyticsApi.html#get_analytics_reporting_schedule_history_latest) | Get most recently completed scheduled report job.|
|[**get_analytics_reporting_schedule_history_run_id**](AnalyticsApi.html#get_analytics_reporting_schedule_history_run_id) | A completed scheduled report job|
|[**get_analytics_reporting_schedules**](AnalyticsApi.html#get_analytics_reporting_schedules) | Get a list of scheduled report jobs|
|[**get_analytics_reporting_timeperiods**](AnalyticsApi.html#get_analytics_reporting_timeperiods) | Get a list of report time periods.|
|[**post_analytics_conversation_details_properties**](AnalyticsApi.html#post_analytics_conversation_details_properties) | Index conversation properties|
|[**post_analytics_conversations_aggregates_query**](AnalyticsApi.html#post_analytics_conversations_aggregates_query) | Query for conversation aggregates|
|[**post_analytics_conversations_details_query**](AnalyticsApi.html#post_analytics_conversations_details_query) | Query for conversation details|
|[**post_analytics_evaluations_aggregates_query**](AnalyticsApi.html#post_analytics_evaluations_aggregates_query) | Query for evaluation aggregates|
|[**post_analytics_queues_observations_query**](AnalyticsApi.html#post_analytics_queues_observations_query) | Query for queue observations|
|[**post_analytics_reporting_schedule_runreport**](AnalyticsApi.html#post_analytics_reporting_schedule_runreport) | Place a scheduled report immediately into the reporting queue|
|[**post_analytics_reporting_schedules**](AnalyticsApi.html#post_analytics_reporting_schedules) | Create a scheduled report job|
|[**post_analytics_users_aggregates_query**](AnalyticsApi.html#post_analytics_users_aggregates_query) | Query for user aggregates|
|[**post_analytics_users_details_query**](AnalyticsApi.html#post_analytics_users_details_query) | Query for user details|
|[**post_analytics_users_observations_query**](AnalyticsApi.html#post_analytics_users_observations_query) | Query for user observations|
|[**put_analytics_reporting_schedule**](AnalyticsApi.html#put_analytics_reporting_schedule) | Update a scheduled report job.|
{: class="table table-striped"}

<a name="delete_analytics_reporting_schedule"></a>

## str**delete_analytics_reporting_schedule(schedule_id)

Delete a scheduled report job.



Wraps DELETE /api/v2/analytics/reporting/schedules/{scheduleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
schedule_id = 'schedule_id_example' # str | Schedule ID

try:
    # Delete a scheduled report job.
    api_response = api_instance.delete_analytics_reporting_schedule(schedule_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->delete_analytics_reporting_schedule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID | |
{: class="table table-striped"}

### Return type

**str**

<a name="get_analytics_conversation_details"></a>

## [**AnalyticsConversation**](AnalyticsConversation.html)get_analytics_conversation_details(conversation_id)

Get a conversation by id



Wraps GET /api/v2/analytics/conversations/{conversationId}/details 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get a conversation by id
    api_response = api_instance.get_analytics_conversation_details(conversation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_conversation_details: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId | |
{: class="table table-striped"}

### Return type

[**AnalyticsConversation**](AnalyticsConversation.html)

<a name="get_analytics_reporting_metadata"></a>

## [**ReportMetaDataEntityListing**](ReportMetaDataEntityListing.html)get_analytics_reporting_metadata(page_number=page_number, page_size=page_size, locale=locale)

Get list of reporting metadata.



Wraps GET /api/v2/analytics/reporting/metadata 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
locale = 'locale_example' # str | Locale (optional)

try:
    # Get list of reporting metadata.
    api_response = api_instance.get_analytics_reporting_metadata(page_number=page_number, page_size=page_size, locale=locale)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_metadata: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **locale** | **str**| Locale | [optional] |
{: class="table table-striped"}

### Return type

[**ReportMetaDataEntityListing**](ReportMetaDataEntityListing.html)

<a name="get_analytics_reporting_report_id_metadata"></a>

## [**ReportMetaData**](ReportMetaData.html)get_analytics_reporting_report_id_metadata(report_id, locale=locale)

Get a reporting metadata.



Wraps GET /api/v2/analytics/reporting/{reportId}/metadata 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
report_id = 'report_id_example' # str | Report ID
locale = 'locale_example' # str | Locale (optional)

try:
    # Get a reporting metadata.
    api_response = api_instance.get_analytics_reporting_report_id_metadata(report_id, locale=locale)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_report_id_metadata: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **report_id** | **str**| Report ID | |
| **locale** | **str**| Locale | [optional] |
{: class="table table-striped"}

### Return type

[**ReportMetaData**](ReportMetaData.html)

<a name="get_analytics_reporting_reportformats"></a>

## list[str]**get_analytics_reporting_reportformats()

Get a list of report formats

Get a list of report formats.

Wraps GET /api/v2/analytics/reporting/reportformats 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()

try:
    # Get a list of report formats
    api_response = api_instance.get_analytics_reporting_reportformats()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_reportformats: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

**list[str]**

<a name="get_analytics_reporting_schedule"></a>

## [**ReportSchedule**](ReportSchedule.html)get_analytics_reporting_schedule(schedule_id)

Get a scheduled report job.



Wraps GET /api/v2/analytics/reporting/schedules/{scheduleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
schedule_id = 'schedule_id_example' # str | Schedule ID

try:
    # Get a scheduled report job.
    api_response = api_instance.get_analytics_reporting_schedule(schedule_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_schedule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID | |
{: class="table table-striped"}

### Return type

[**ReportSchedule**](ReportSchedule.html)

<a name="get_analytics_reporting_schedule_history"></a>

## [**ReportRunEntryEntityDomainListing**](ReportRunEntryEntityDomainListing.html)get_analytics_reporting_schedule_history(schedule_id, page_number=page_number, page_size=page_size)

Get list of completed scheduled report jobs.



Wraps GET /api/v2/analytics/reporting/schedules/{scheduleId}/history 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
schedule_id = 'schedule_id_example' # str | Schedule ID
page_number = 1 # int |  (optional) (default to 1)
page_size = 25 # int |  (optional) (default to 25)

try:
    # Get list of completed scheduled report jobs.
    api_response = api_instance.get_analytics_reporting_schedule_history(schedule_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_schedule_history: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID | |
| **page_number** | **int**|  | [optional] [default to 1]|
| **page_size** | **int**|  | [optional] [default to 25]|
{: class="table table-striped"}

### Return type

[**ReportRunEntryEntityDomainListing**](ReportRunEntryEntityDomainListing.html)

<a name="get_analytics_reporting_schedule_history_latest"></a>

## [**ReportRunEntry**](ReportRunEntry.html)get_analytics_reporting_schedule_history_latest(schedule_id)

Get most recently completed scheduled report job.



Wraps GET /api/v2/analytics/reporting/schedules/{scheduleId}/history/latest 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
schedule_id = 'schedule_id_example' # str | Schedule ID

try:
    # Get most recently completed scheduled report job.
    api_response = api_instance.get_analytics_reporting_schedule_history_latest(schedule_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_schedule_history_latest: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID | |
{: class="table table-striped"}

### Return type

[**ReportRunEntry**](ReportRunEntry.html)

<a name="get_analytics_reporting_schedule_history_run_id"></a>

## [**ReportRunEntry**](ReportRunEntry.html)get_analytics_reporting_schedule_history_run_id(run_id, schedule_id)

A completed scheduled report job

A completed scheduled report job.

Wraps GET /api/v2/analytics/reporting/schedules/{scheduleId}/history/{runId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
run_id = 'run_id_example' # str | Run ID
schedule_id = 'schedule_id_example' # str | Schedule ID

try:
    # A completed scheduled report job
    api_response = api_instance.get_analytics_reporting_schedule_history_run_id(run_id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_schedule_history_run_id: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **run_id** | **str**| Run ID | |
| **schedule_id** | **str**| Schedule ID | |
{: class="table table-striped"}

### Return type

[**ReportRunEntry**](ReportRunEntry.html)

<a name="get_analytics_reporting_schedules"></a>

## [**ReportScheduleEntityListing**](ReportScheduleEntityListing.html)get_analytics_reporting_schedules(page_number=page_number, page_size=page_size)

Get a list of scheduled report jobs

Get a list of scheduled report jobs.

Wraps GET /api/v2/analytics/reporting/schedules 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get a list of scheduled report jobs
    api_response = api_instance.get_analytics_reporting_schedules(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_schedules: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
{: class="table table-striped"}

### Return type

[**ReportScheduleEntityListing**](ReportScheduleEntityListing.html)

<a name="get_analytics_reporting_timeperiods"></a>

## list[str]**get_analytics_reporting_timeperiods()

Get a list of report time periods.



Wraps GET /api/v2/analytics/reporting/timeperiods 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()

try:
    # Get a list of report time periods.
    api_response = api_instance.get_analytics_reporting_timeperiods()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_timeperiods: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

**list[str]**

<a name="post_analytics_conversation_details_properties"></a>

## [**PropertyIndexRequest**](PropertyIndexRequest.html)post_analytics_conversation_details_properties(conversation_id, body)

Index conversation properties



Wraps POST /api/v2/analytics/conversations/{conversationId}/details/properties 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling AnalyticsApi->post_analytics_conversation_details_properties: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId | |
| **body** | [**PropertyIndexRequest**](PropertyIndexRequest.html)| request | |
{: class="table table-striped"}

### Return type

[**PropertyIndexRequest**](PropertyIndexRequest.html)

<a name="post_analytics_conversations_aggregates_query"></a>

## [**AggregateQueryResponse**](AggregateQueryResponse.html)post_analytics_conversations_aggregates_query(body)

Query for conversation aggregates



Wraps POST /api/v2/analytics/conversations/aggregates/query 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.AggregationQuery() # AggregationQuery | query

try:
    # Query for conversation aggregates
    api_response = api_instance.post_analytics_conversations_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->post_analytics_conversations_aggregates_query: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AggregationQuery**](AggregationQuery.html)| query | |
{: class="table table-striped"}

### Return type

[**AggregateQueryResponse**](AggregateQueryResponse.html)

<a name="post_analytics_conversations_details_query"></a>

## [**AnalyticsConversationQueryResponse**](AnalyticsConversationQueryResponse.html)post_analytics_conversations_details_query(body)

Query for conversation details



Wraps POST /api/v2/analytics/conversations/details/query 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.ConversationQuery() # ConversationQuery | query

try:
    # Query for conversation details
    api_response = api_instance.post_analytics_conversations_details_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->post_analytics_conversations_details_query: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationQuery**](ConversationQuery.html)| query | |
{: class="table table-striped"}

### Return type

[**AnalyticsConversationQueryResponse**](AnalyticsConversationQueryResponse.html)

<a name="post_analytics_evaluations_aggregates_query"></a>

## [**AggregateQueryResponse**](AggregateQueryResponse.html)post_analytics_evaluations_aggregates_query(body)

Query for evaluation aggregates



Wraps POST /api/v2/analytics/evaluations/aggregates/query 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.AggregationQuery() # AggregationQuery | query

try:
    # Query for evaluation aggregates
    api_response = api_instance.post_analytics_evaluations_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->post_analytics_evaluations_aggregates_query: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AggregationQuery**](AggregationQuery.html)| query | |
{: class="table table-striped"}

### Return type

[**AggregateQueryResponse**](AggregateQueryResponse.html)

<a name="post_analytics_queues_observations_query"></a>

## [**QualifierMappingObservationQueryResponse**](QualifierMappingObservationQueryResponse.html)post_analytics_queues_observations_query(body)

Query for queue observations



Wraps POST /api/v2/analytics/queues/observations/query 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.ObservationQuery() # ObservationQuery | query

try:
    # Query for queue observations
    api_response = api_instance.post_analytics_queues_observations_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->post_analytics_queues_observations_query: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ObservationQuery**](ObservationQuery.html)| query | |
{: class="table table-striped"}

### Return type

[**QualifierMappingObservationQueryResponse**](QualifierMappingObservationQueryResponse.html)

<a name="post_analytics_reporting_schedule_runreport"></a>

## [**RunNowResponse**](RunNowResponse.html)post_analytics_reporting_schedule_runreport(schedule_id)

Place a scheduled report immediately into the reporting queue



Wraps POST /api/v2/analytics/reporting/schedules/{scheduleId}/runreport 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
schedule_id = 'schedule_id_example' # str | Schedule ID

try:
    # Place a scheduled report immediately into the reporting queue
    api_response = api_instance.post_analytics_reporting_schedule_runreport(schedule_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->post_analytics_reporting_schedule_runreport: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID | |
{: class="table table-striped"}

### Return type

[**RunNowResponse**](RunNowResponse.html)

<a name="post_analytics_reporting_schedules"></a>

## [**ReportSchedule**](ReportSchedule.html)post_analytics_reporting_schedules(body)

Create a scheduled report job

Create a scheduled report job.

Wraps POST /api/v2/analytics/reporting/schedules 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.ReportSchedule() # ReportSchedule | ReportSchedule

try:
    # Create a scheduled report job
    api_response = api_instance.post_analytics_reporting_schedules(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->post_analytics_reporting_schedules: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ReportSchedule**](ReportSchedule.html)| ReportSchedule | |
{: class="table table-striped"}

### Return type

[**ReportSchedule**](ReportSchedule.html)

<a name="post_analytics_users_aggregates_query"></a>

## [**PresenceQueryResponse**](PresenceQueryResponse.html)post_analytics_users_aggregates_query(body)

Query for user aggregates



Wraps POST /api/v2/analytics/users/aggregates/query 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.AggregationQuery() # AggregationQuery | query

try:
    # Query for user aggregates
    api_response = api_instance.post_analytics_users_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->post_analytics_users_aggregates_query: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AggregationQuery**](AggregationQuery.html)| query | |
{: class="table table-striped"}

### Return type

[**PresenceQueryResponse**](PresenceQueryResponse.html)

<a name="post_analytics_users_details_query"></a>

## [**AnalyticsUserDetailsQueryResponse**](AnalyticsUserDetailsQueryResponse.html)post_analytics_users_details_query(body)

Query for user details



Wraps POST /api/v2/analytics/users/details/query 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.UserDetailsQuery() # UserDetailsQuery | query

try:
    # Query for user details
    api_response = api_instance.post_analytics_users_details_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->post_analytics_users_details_query: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserDetailsQuery**](UserDetailsQuery.html)| query | |
{: class="table table-striped"}

### Return type

[**AnalyticsUserDetailsQueryResponse**](AnalyticsUserDetailsQueryResponse.html)

<a name="post_analytics_users_observations_query"></a>

## [**ObservationQueryResponse**](ObservationQueryResponse.html)post_analytics_users_observations_query(body)

Query for user observations



Wraps POST /api/v2/analytics/users/observations/query 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
body = PureCloudPlatformClientV2.ObservationQuery() # ObservationQuery | query

try:
    # Query for user observations
    api_response = api_instance.post_analytics_users_observations_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->post_analytics_users_observations_query: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ObservationQuery**](ObservationQuery.html)| query | |
{: class="table table-striped"}

### Return type

[**ObservationQueryResponse**](ObservationQueryResponse.html)

<a name="put_analytics_reporting_schedule"></a>

## [**ReportSchedule**](ReportSchedule.html)put_analytics_reporting_schedule(schedule_id, body)

Update a scheduled report job.



Wraps PUT /api/v2/analytics/reporting/schedules/{scheduleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AnalyticsApi()
schedule_id = 'schedule_id_example' # str | Schedule ID
body = PureCloudPlatformClientV2.ReportSchedule() # ReportSchedule | ReportSchedule

try:
    # Update a scheduled report job.
    api_response = api_instance.put_analytics_reporting_schedule(schedule_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->put_analytics_reporting_schedule: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID | |
| **body** | [**ReportSchedule**](ReportSchedule.html)| ReportSchedule | |
{: class="table table-striped"}

### Return type

[**ReportSchedule**](ReportSchedule.html)


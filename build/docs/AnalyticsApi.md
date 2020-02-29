---
title: AnalyticsApi
---

## PureCloudPlatformClientV2.AnalyticsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_analytics_conversations_details_job**](AnalyticsApi.html#delete_analytics_conversations_details_job) | Delete/cancel an async request|
|[**delete_analytics_reporting_schedule**](AnalyticsApi.html#delete_analytics_reporting_schedule) | Delete a scheduled report job.|
|[**delete_analytics_users_details_job**](AnalyticsApi.html#delete_analytics_users_details_job) | Delete/cancel an async request|
|[**get_analytics_conversation_details**](AnalyticsApi.html#get_analytics_conversation_details) | Get a conversation by id|
|[**get_analytics_conversations_details**](AnalyticsApi.html#get_analytics_conversations_details) | Gets multiple conversations by id|
|[**get_analytics_conversations_details_job**](AnalyticsApi.html#get_analytics_conversations_details_job) | Get status for async query for conversation details|
|[**get_analytics_conversations_details_job_results**](AnalyticsApi.html#get_analytics_conversations_details_job_results) | Fetch a page of results for an async query|
|[**get_analytics_reporting_exports**](AnalyticsApi.html#get_analytics_reporting_exports) | Get all view export requests for a user|
|[**get_analytics_reporting_exports_metadata**](AnalyticsApi.html#get_analytics_reporting_exports_metadata) | Get all export metadata|
|[**get_analytics_reporting_metadata**](AnalyticsApi.html#get_analytics_reporting_metadata) | Get list of reporting metadata.|
|[**get_analytics_reporting_report_id_metadata**](AnalyticsApi.html#get_analytics_reporting_report_id_metadata) | Get a reporting metadata.|
|[**get_analytics_reporting_reportformats**](AnalyticsApi.html#get_analytics_reporting_reportformats) | Get a list of report formats|
|[**get_analytics_reporting_schedule**](AnalyticsApi.html#get_analytics_reporting_schedule) | Get a scheduled report job.|
|[**get_analytics_reporting_schedule_history**](AnalyticsApi.html#get_analytics_reporting_schedule_history) | Get list of completed scheduled report jobs.|
|[**get_analytics_reporting_schedule_history_latest**](AnalyticsApi.html#get_analytics_reporting_schedule_history_latest) | Get most recently completed scheduled report job.|
|[**get_analytics_reporting_schedule_history_run_id**](AnalyticsApi.html#get_analytics_reporting_schedule_history_run_id) | A completed scheduled report job|
|[**get_analytics_reporting_schedules**](AnalyticsApi.html#get_analytics_reporting_schedules) | Get a list of scheduled report jobs|
|[**get_analytics_reporting_timeperiods**](AnalyticsApi.html#get_analytics_reporting_timeperiods) | Get a list of report time periods.|
|[**get_analytics_users_details_job**](AnalyticsApi.html#get_analytics_users_details_job) | Get status for async query for user details|
|[**get_analytics_users_details_job_results**](AnalyticsApi.html#get_analytics_users_details_job_results) | Fetch a page of results for an async query|
|[**post_analytics_conversation_details_properties**](AnalyticsApi.html#post_analytics_conversation_details_properties) | Index conversation properties|
|[**post_analytics_conversations_aggregates_query**](AnalyticsApi.html#post_analytics_conversations_aggregates_query) | Query for conversation aggregates|
|[**post_analytics_conversations_details_jobs**](AnalyticsApi.html#post_analytics_conversations_details_jobs) | Query for conversation details asynchronously|
|[**post_analytics_conversations_details_query**](AnalyticsApi.html#post_analytics_conversations_details_query) | Query for conversation details|
|[**post_analytics_evaluations_aggregates_query**](AnalyticsApi.html#post_analytics_evaluations_aggregates_query) | Query for evaluation aggregates|
|[**post_analytics_flows_aggregates_query**](AnalyticsApi.html#post_analytics_flows_aggregates_query) | Query for flow aggregates|
|[**post_analytics_flows_observations_query**](AnalyticsApi.html#post_analytics_flows_observations_query) | Query for flow observations|
|[**post_analytics_queues_observations_query**](AnalyticsApi.html#post_analytics_queues_observations_query) | Query for queue observations|
|[**post_analytics_reporting_exports**](AnalyticsApi.html#post_analytics_reporting_exports) | Generate a view export request|
|[**post_analytics_reporting_schedule_runreport**](AnalyticsApi.html#post_analytics_reporting_schedule_runreport) | Place a scheduled report immediately into the reporting queue|
|[**post_analytics_reporting_schedules**](AnalyticsApi.html#post_analytics_reporting_schedules) | Create a scheduled report job|
|[**post_analytics_surveys_aggregates_query**](AnalyticsApi.html#post_analytics_surveys_aggregates_query) | Query for survey aggregates|
|[**post_analytics_users_aggregates_query**](AnalyticsApi.html#post_analytics_users_aggregates_query) | Query for user aggregates|
|[**post_analytics_users_details_jobs**](AnalyticsApi.html#post_analytics_users_details_jobs) | Query for user details asynchronously|
|[**post_analytics_users_details_query**](AnalyticsApi.html#post_analytics_users_details_query) | Query for user details|
|[**post_analytics_users_observations_query**](AnalyticsApi.html#post_analytics_users_observations_query) | Query for user observations|
|[**put_analytics_reporting_schedule**](AnalyticsApi.html#put_analytics_reporting_schedule) | Update a scheduled report job.|
{: class="table table-striped"}

<a name="delete_analytics_conversations_details_job"></a>

##  delete_analytics_conversations_details_job(job_id)



Delete/cancel an async request



Wraps DELETE /api/v2/analytics/conversations/details/jobs/{jobId} 

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
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request
    api_instance.delete_analytics_conversations_details_job(job_id)
except ApiException as e:
    print "Exception when calling AnalyticsApi->delete_analytics_conversations_details_job: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_analytics_reporting_schedule"></a>

##  delete_analytics_reporting_schedule(schedule_id)



Delete a scheduled report job.



Wraps DELETE /api/v2/analytics/reporting/schedules/{scheduleId} 

Requires NO permissions: 


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
schedule_id = 'schedule_id_example' # str | Schedule ID

try:
    # Delete a scheduled report job.
    api_instance.delete_analytics_reporting_schedule(schedule_id)
except ApiException as e:
    print "Exception when calling AnalyticsApi->delete_analytics_reporting_schedule: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_analytics_users_details_job"></a>

##  delete_analytics_users_details_job(job_id)



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
    print "Exception when calling AnalyticsApi->delete_analytics_users_details_job: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_analytics_conversation_details"></a>

## [**AnalyticsConversationWithoutAttributes**](AnalyticsConversationWithoutAttributes.html) get_analytics_conversation_details(conversation_id)



Get a conversation by id



Wraps GET /api/v2/analytics/conversations/{conversationId}/details 

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
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get a conversation by id
    api_response = api_instance.get_analytics_conversation_details(conversation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_conversation_details: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**AnalyticsConversationWithoutAttributes**](AnalyticsConversationWithoutAttributes.html)

<a name="get_analytics_conversations_details"></a>

## [**AnalyticsConversationWithoutAttributesMultiGetResponse**](AnalyticsConversationWithoutAttributesMultiGetResponse.html) get_analytics_conversations_details(id=id)



Gets multiple conversations by id



Wraps GET /api/v2/analytics/conversations/details 

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
id = ['id_example'] # list[str] | Comma-separated conversation ids (optional)

try:
    # Gets multiple conversations by id
    api_response = api_instance.get_analytics_conversations_details(id=id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_conversations_details: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str.html)| Comma-separated conversation ids | [optional]  |
{: class="table table-striped"}

### Return type

[**AnalyticsConversationWithoutAttributesMultiGetResponse**](AnalyticsConversationWithoutAttributesMultiGetResponse.html)

<a name="get_analytics_conversations_details_job"></a>

## [**AsyncQueryStatus**](AsyncQueryStatus.html) get_analytics_conversations_details_job(job_id)



Get status for async query for conversation details



Wraps GET /api/v2/analytics/conversations/details/jobs/{jobId} 

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
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for conversation details
    api_response = api_instance.get_analytics_conversations_details_job(job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_conversations_details_job: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus.html)

<a name="get_analytics_conversations_details_job_results"></a>

## [**AnalyticsConversationAsyncQueryResponse**](AnalyticsConversationAsyncQueryResponse.html) get_analytics_conversations_details_job_results(job_id, cursor=cursor, page_size=page_size)



Fetch a page of results for an async query



Wraps GET /api/v2/analytics/conversations/details/jobs/{jobId}/results 

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
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page) (optional)
page_size = 56 # int | The desired maximum number of results (optional)

try:
    # Fetch a page of results for an async query
    api_response = api_instance.get_analytics_conversations_details_job_results(job_id, cursor=cursor, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_conversations_details_job_results: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page) | [optional]  |
| **page_size** | **int**| The desired maximum number of results | [optional]  |
{: class="table table-striped"}

### Return type

[**AnalyticsConversationAsyncQueryResponse**](AnalyticsConversationAsyncQueryResponse.html)

<a name="get_analytics_reporting_exports"></a>

## [**ReportingExportJobListing**](ReportingExportJobListing.html) get_analytics_reporting_exports()



Get all view export requests for a user



Wraps GET /api/v2/analytics/reporting/exports 

Requires ANY permissions: 

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
    # Get all view export requests for a user
    api_response = api_instance.get_analytics_reporting_exports()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_exports: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**ReportingExportJobListing**](ReportingExportJobListing.html)

<a name="get_analytics_reporting_exports_metadata"></a>

## [**ReportingExportMetadataJobListing**](ReportingExportMetadataJobListing.html) get_analytics_reporting_exports_metadata()



Get all export metadata



Wraps GET /api/v2/analytics/reporting/exports/metadata 

Requires ANY permissions: 

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
    print "Exception when calling AnalyticsApi->get_analytics_reporting_exports_metadata: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**ReportingExportMetadataJobListing**](ReportingExportMetadataJobListing.html)

<a name="get_analytics_reporting_metadata"></a>

## [**ReportMetaDataEntityListing**](ReportMetaDataEntityListing.html) get_analytics_reporting_metadata(page_number=page_number, page_size=page_size, locale=locale)



Get list of reporting metadata.



Wraps GET /api/v2/analytics/reporting/metadata 

Requires ANY permissions: 

* reporting:acd:view, reporting:status:view, reporting:interactions:view, reporting:outbound:view, reporting:quality:view, employee

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
locale = 'locale_example' # str | Locale (optional)

try:
    # Get list of reporting metadata.
    api_response = api_instance.get_analytics_reporting_metadata(page_number=page_number, page_size=page_size, locale=locale)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_metadata: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **locale** | **str**| Locale | [optional]  |
{: class="table table-striped"}

### Return type

[**ReportMetaDataEntityListing**](ReportMetaDataEntityListing.html)

<a name="get_analytics_reporting_report_id_metadata"></a>

## [**ReportMetaData**](ReportMetaData.html) get_analytics_reporting_report_id_metadata(report_id, locale=locale)



Get a reporting metadata.



Wraps GET /api/v2/analytics/reporting/{reportId}/metadata 

Requires ANY permissions: 

* reporting:acd:view, reporting:status:view, reporting:interactions:view, reporting:outbound:view, reporting:quality:view, employee

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
report_id = 'report_id_example' # str | Report ID
locale = 'locale_example' # str | Locale (optional)

try:
    # Get a reporting metadata.
    api_response = api_instance.get_analytics_reporting_report_id_metadata(report_id, locale=locale)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_report_id_metadata: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **report_id** | **str**| Report ID |  |
| **locale** | **str**| Locale | [optional]  |
{: class="table table-striped"}

### Return type

[**ReportMetaData**](ReportMetaData.html)

<a name="get_analytics_reporting_reportformats"></a>

## list[str]** get_analytics_reporting_reportformats()



Get a list of report formats

Get a list of report formats.

Wraps GET /api/v2/analytics/reporting/reportformats 

Requires NO permissions: 


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
    # Get a list of report formats
    api_response = api_instance.get_analytics_reporting_reportformats()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_reportformats: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

**list[str]**

<a name="get_analytics_reporting_schedule"></a>

## [**ReportSchedule**](ReportSchedule.html) get_analytics_reporting_schedule(schedule_id)



Get a scheduled report job.



Wraps GET /api/v2/analytics/reporting/schedules/{scheduleId} 

Requires NO permissions: 


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
schedule_id = 'schedule_id_example' # str | Schedule ID

try:
    # Get a scheduled report job.
    api_response = api_instance.get_analytics_reporting_schedule(schedule_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_schedule: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID |  |
{: class="table table-striped"}

### Return type

[**ReportSchedule**](ReportSchedule.html)

<a name="get_analytics_reporting_schedule_history"></a>

## [**ReportRunEntryEntityDomainListing**](ReportRunEntryEntityDomainListing.html) get_analytics_reporting_schedule_history(schedule_id, page_number=page_number, page_size=page_size)



Get list of completed scheduled report jobs.



Wraps GET /api/v2/analytics/reporting/schedules/{scheduleId}/history 

Requires NO permissions: 


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
schedule_id = 'schedule_id_example' # str | Schedule ID
page_number = 1 # int |  (optional) (default to 1)
page_size = 25 # int |  (optional) (default to 25)

try:
    # Get list of completed scheduled report jobs.
    api_response = api_instance.get_analytics_reporting_schedule_history(schedule_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_schedule_history: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID |  |
| **page_number** | **int**|  | [optional] [default to 1] |
| **page_size** | **int**|  | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**ReportRunEntryEntityDomainListing**](ReportRunEntryEntityDomainListing.html)

<a name="get_analytics_reporting_schedule_history_latest"></a>

## [**ReportRunEntry**](ReportRunEntry.html) get_analytics_reporting_schedule_history_latest(schedule_id)



Get most recently completed scheduled report job.



Wraps GET /api/v2/analytics/reporting/schedules/{scheduleId}/history/latest 

Requires NO permissions: 


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
schedule_id = 'schedule_id_example' # str | Schedule ID

try:
    # Get most recently completed scheduled report job.
    api_response = api_instance.get_analytics_reporting_schedule_history_latest(schedule_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_schedule_history_latest: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID |  |
{: class="table table-striped"}

### Return type

[**ReportRunEntry**](ReportRunEntry.html)

<a name="get_analytics_reporting_schedule_history_run_id"></a>

## [**ReportRunEntry**](ReportRunEntry.html) get_analytics_reporting_schedule_history_run_id(run_id, schedule_id)



A completed scheduled report job

A completed scheduled report job.

Wraps GET /api/v2/analytics/reporting/schedules/{scheduleId}/history/{runId} 

Requires NO permissions: 


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
run_id = 'run_id_example' # str | Run ID
schedule_id = 'schedule_id_example' # str | Schedule ID

try:
    # A completed scheduled report job
    api_response = api_instance.get_analytics_reporting_schedule_history_run_id(run_id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_schedule_history_run_id: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **run_id** | **str**| Run ID |  |
| **schedule_id** | **str**| Schedule ID |  |
{: class="table table-striped"}

### Return type

[**ReportRunEntry**](ReportRunEntry.html)

<a name="get_analytics_reporting_schedules"></a>

## [**ReportScheduleEntityListing**](ReportScheduleEntityListing.html) get_analytics_reporting_schedules(page_number=page_number, page_size=page_size)



Get a list of scheduled report jobs

Get a list of scheduled report jobs.

Wraps GET /api/v2/analytics/reporting/schedules 

Requires NO permissions: 


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
    # Get a list of scheduled report jobs
    api_response = api_instance.get_analytics_reporting_schedules(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_schedules: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**ReportScheduleEntityListing**](ReportScheduleEntityListing.html)

<a name="get_analytics_reporting_timeperiods"></a>

## list[str]** get_analytics_reporting_timeperiods()



Get a list of report time periods.



Wraps GET /api/v2/analytics/reporting/timeperiods 

Requires NO permissions: 


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
    # Get a list of report time periods.
    api_response = api_instance.get_analytics_reporting_timeperiods()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_analytics_reporting_timeperiods: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

**list[str]**

<a name="get_analytics_users_details_job"></a>

## [**AsyncQueryStatus**](AsyncQueryStatus.html) get_analytics_users_details_job(job_id)



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
    print "Exception when calling AnalyticsApi->get_analytics_users_details_job: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus.html)

<a name="get_analytics_users_details_job_results"></a>

## [**AnalyticsUserDetailsAsyncQueryResponse**](AnalyticsUserDetailsAsyncQueryResponse.html) get_analytics_users_details_job_results(job_id, cursor=cursor, page_size=page_size)



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
    print "Exception when calling AnalyticsApi->get_analytics_users_details_job_results: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page) | [optional]  |
| **page_size** | **int**| The desired maximum number of results | [optional]  |
{: class="table table-striped"}

### Return type

[**AnalyticsUserDetailsAsyncQueryResponse**](AnalyticsUserDetailsAsyncQueryResponse.html)

<a name="post_analytics_conversation_details_properties"></a>

## [**PropertyIndexRequest**](PropertyIndexRequest.html) post_analytics_conversation_details_properties(conversation_id, body)



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
    print "Exception when calling AnalyticsApi->post_analytics_conversation_details_properties: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**PropertyIndexRequest**](PropertyIndexRequest.html)| request |  |
{: class="table table-striped"}

### Return type

[**PropertyIndexRequest**](PropertyIndexRequest.html)

<a name="post_analytics_conversations_aggregates_query"></a>

## [**ConversationAggregateQueryResponse**](ConversationAggregateQueryResponse.html) post_analytics_conversations_aggregates_query(body)



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
    print "Exception when calling AnalyticsApi->post_analytics_conversations_aggregates_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationAggregationQuery**](ConversationAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**ConversationAggregateQueryResponse**](ConversationAggregateQueryResponse.html)

<a name="post_analytics_conversations_details_jobs"></a>

## [**AsyncQueryResponse**](AsyncQueryResponse.html) post_analytics_conversations_details_jobs(body)



Query for conversation details asynchronously



Wraps POST /api/v2/analytics/conversations/details/jobs 

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
body = PureCloudPlatformClientV2.AsyncConversationQuery() # AsyncConversationQuery | query

try:
    # Query for conversation details asynchronously
    api_response = api_instance.post_analytics_conversations_details_jobs(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->post_analytics_conversations_details_jobs: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AsyncConversationQuery**](AsyncConversationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse.html)

<a name="post_analytics_conversations_details_query"></a>

## [**AnalyticsConversationQueryResponse**](AnalyticsConversationQueryResponse.html) post_analytics_conversations_details_query(body)



Query for conversation details



Wraps POST /api/v2/analytics/conversations/details/query 

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
body = PureCloudPlatformClientV2.ConversationQuery() # ConversationQuery | query

try:
    # Query for conversation details
    api_response = api_instance.post_analytics_conversations_details_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->post_analytics_conversations_details_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationQuery**](ConversationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AnalyticsConversationQueryResponse**](AnalyticsConversationQueryResponse.html)

<a name="post_analytics_evaluations_aggregates_query"></a>

## [**EvaluationAggregateQueryResponse**](EvaluationAggregateQueryResponse.html) post_analytics_evaluations_aggregates_query(body)



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
    print "Exception when calling AnalyticsApi->post_analytics_evaluations_aggregates_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EvaluationAggregationQuery**](EvaluationAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**EvaluationAggregateQueryResponse**](EvaluationAggregateQueryResponse.html)

<a name="post_analytics_flows_aggregates_query"></a>

## [**FlowAggregateQueryResponse**](FlowAggregateQueryResponse.html) post_analytics_flows_aggregates_query(body)



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
    print "Exception when calling AnalyticsApi->post_analytics_flows_aggregates_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowAggregationQuery**](FlowAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**FlowAggregateQueryResponse**](FlowAggregateQueryResponse.html)

<a name="post_analytics_flows_observations_query"></a>

## [**FlowObservationQueryResponse**](FlowObservationQueryResponse.html) post_analytics_flows_observations_query(body)



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
    print "Exception when calling AnalyticsApi->post_analytics_flows_observations_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FlowObservationQuery**](FlowObservationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**FlowObservationQueryResponse**](FlowObservationQueryResponse.html)

<a name="post_analytics_queues_observations_query"></a>

## [**QueueObservationQueryResponse**](QueueObservationQueryResponse.html) post_analytics_queues_observations_query(body)



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
    print "Exception when calling AnalyticsApi->post_analytics_queues_observations_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**QueueObservationQuery**](QueueObservationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**QueueObservationQueryResponse**](QueueObservationQueryResponse.html)

<a name="post_analytics_reporting_exports"></a>

## [**ReportingExportJobResponse**](ReportingExportJobResponse.html) post_analytics_reporting_exports(body)



Generate a view export request



Wraps POST /api/v2/analytics/reporting/exports 

Requires ANY permissions: 

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
    print "Exception when calling AnalyticsApi->post_analytics_reporting_exports: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ReportingExportJobRequest**](ReportingExportJobRequest.html)| ReportingExportJobRequest |  |
{: class="table table-striped"}

### Return type

[**ReportingExportJobResponse**](ReportingExportJobResponse.html)

<a name="post_analytics_reporting_schedule_runreport"></a>

## [**RunNowResponse**](RunNowResponse.html) post_analytics_reporting_schedule_runreport(schedule_id)



Place a scheduled report immediately into the reporting queue



Wraps POST /api/v2/analytics/reporting/schedules/{scheduleId}/runreport 

Requires NO permissions: 


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
schedule_id = 'schedule_id_example' # str | Schedule ID

try:
    # Place a scheduled report immediately into the reporting queue
    api_response = api_instance.post_analytics_reporting_schedule_runreport(schedule_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->post_analytics_reporting_schedule_runreport: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID |  |
{: class="table table-striped"}

### Return type

[**RunNowResponse**](RunNowResponse.html)

<a name="post_analytics_reporting_schedules"></a>

## [**ReportSchedule**](ReportSchedule.html) post_analytics_reporting_schedules(body)



Create a scheduled report job

Create a scheduled report job.

Wraps POST /api/v2/analytics/reporting/schedules 

Requires ANY permissions: 

* reporting:acd:view, reporting:status:view, reporting:interactions:view, reporting:outbound:view, reporting:quality:view, employee

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
body = PureCloudPlatformClientV2.ReportSchedule() # ReportSchedule | ReportSchedule

try:
    # Create a scheduled report job
    api_response = api_instance.post_analytics_reporting_schedules(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->post_analytics_reporting_schedules: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ReportSchedule**](ReportSchedule.html)| ReportSchedule |  |
{: class="table table-striped"}

### Return type

[**ReportSchedule**](ReportSchedule.html)

<a name="post_analytics_surveys_aggregates_query"></a>

## [**SurveyAggregateQueryResponse**](SurveyAggregateQueryResponse.html) post_analytics_surveys_aggregates_query(body)



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
    print "Exception when calling AnalyticsApi->post_analytics_surveys_aggregates_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SurveyAggregationQuery**](SurveyAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**SurveyAggregateQueryResponse**](SurveyAggregateQueryResponse.html)

<a name="post_analytics_users_aggregates_query"></a>

## [**UserAggregateQueryResponse**](UserAggregateQueryResponse.html) post_analytics_users_aggregates_query(body)



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
    print "Exception when calling AnalyticsApi->post_analytics_users_aggregates_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserAggregationQuery**](UserAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**UserAggregateQueryResponse**](UserAggregateQueryResponse.html)

<a name="post_analytics_users_details_jobs"></a>

## [**AsyncQueryResponse**](AsyncQueryResponse.html) post_analytics_users_details_jobs(body)



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
    print "Exception when calling AnalyticsApi->post_analytics_users_details_jobs: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AsyncUserDetailsQuery**](AsyncUserDetailsQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse.html)

<a name="post_analytics_users_details_query"></a>

## [**AnalyticsUserDetailsQueryResponse**](AnalyticsUserDetailsQueryResponse.html) post_analytics_users_details_query(body)



Query for user details



Wraps POST /api/v2/analytics/users/details/query 

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
body = PureCloudPlatformClientV2.UserDetailsQuery() # UserDetailsQuery | query

try:
    # Query for user details
    api_response = api_instance.post_analytics_users_details_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->post_analytics_users_details_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserDetailsQuery**](UserDetailsQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AnalyticsUserDetailsQueryResponse**](AnalyticsUserDetailsQueryResponse.html)

<a name="post_analytics_users_observations_query"></a>

## [**UserObservationQueryResponse**](UserObservationQueryResponse.html) post_analytics_users_observations_query(body)



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
    print "Exception when calling AnalyticsApi->post_analytics_users_observations_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserObservationQuery**](UserObservationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**UserObservationQueryResponse**](UserObservationQueryResponse.html)

<a name="put_analytics_reporting_schedule"></a>

## [**ReportSchedule**](ReportSchedule.html) put_analytics_reporting_schedule(schedule_id, body)



Update a scheduled report job.



Wraps PUT /api/v2/analytics/reporting/schedules/{scheduleId} 

Requires ANY permissions: 

* reporting:acd:view, reporting:status:view, reporting:interactions:view, reporting:outbound:view, reporting:quality:view, employee

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
schedule_id = 'schedule_id_example' # str | Schedule ID
body = PureCloudPlatformClientV2.ReportSchedule() # ReportSchedule | ReportSchedule

try:
    # Update a scheduled report job.
    api_response = api_instance.put_analytics_reporting_schedule(schedule_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->put_analytics_reporting_schedule: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schedule_id** | **str**| Schedule ID |  |
| **body** | [**ReportSchedule**](ReportSchedule.html)| ReportSchedule |  |
{: class="table table-striped"}

### Return type

[**ReportSchedule**](ReportSchedule.html)


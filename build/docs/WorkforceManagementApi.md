---
title: WorkforceManagementApi
---

## PureCloudPlatformClientV2.WorkforceManagementApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_workforcemanagement_adherence**](WorkforceManagementApi.html#get_workforcemanagement_adherence) | Get a list of UserScheduleAdherence records for the requested users|
|[**get_workforcemanagement_managementunit_activitycodes**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_activitycodes) | Get activity codes|
|[**get_workforcemanagement_managementunit_intraday_queues**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_intraday_queues) | Get intraday queues for the given date|
|[**get_workforcemanagement_managementunit_user_timeoffrequest**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_user_timeoffrequest) | Get a time off request|
|[**get_workforcemanagement_managementunit_user_timeoffrequests**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_user_timeoffrequests) | Get a list of time off requests for a given user|
|[**get_workforcemanagement_managementunit_users**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_users) | Get agents in the management unit|
|[**get_workforcemanagement_managementunits**](WorkforceManagementApi.html#get_workforcemanagement_managementunits) | Get management units|
|[**patch_workforcemanagement_managementunit_user_timeoffrequest**](WorkforceManagementApi.html#patch_workforcemanagement_managementunit_user_timeoffrequest) | Update a time off request|
|[**post_workforcemanagement_managementunit_activitycodes**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_activitycodes) | Create a new activity code|
|[**post_workforcemanagement_managementunit_historicaladherencequery**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_historicaladherencequery) | Request a historical adherence report|
|[**post_workforcemanagement_managementunit_intraday**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_intraday) | Get intraday data for the given date for the requested queueIds|
|[**post_workforcemanagement_managementunit_schedules_search**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_schedules_search) | Query published schedules for given given time range for set of users|
{: class="table table-striped"}

<a name="get_workforcemanagement_adherence"></a>

## [**list[UserScheduleAdherence]**](UserScheduleAdherence.html) get_workforcemanagement_adherence(user_id)



Get a list of UserScheduleAdherence records for the requested users



Wraps GET /api/v2/workforcemanagement/adherence 

Requires ANY permissions: 

* wfm:realtimeAdherence:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
user_id = ['user_id_example'] # list[str] | User Id(s) for which to fetch current schedule adherence information.  Min 1, Max of 100 userIds per request

try:
    # Get a list of UserScheduleAdherence records for the requested users
    api_response = api_instance.get_workforcemanagement_adherence(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_adherence: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | [**list[str]**](str.html)| User Id(s) for which to fetch current schedule adherence information.  Min 1, Max of 100 userIds per request |  |
{: class="table table-striped"}

### Return type

[**list[UserScheduleAdherence]**](UserScheduleAdherence.html)

<a name="get_workforcemanagement_managementunit_activitycodes"></a>

## [**ActivityCodeContainer**](ActivityCodeContainer.html) get_workforcemanagement_managementunit_activitycodes(mu_id)



Get activity codes



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/activitycodes 

Requires ANY permissions: 

* wfm:activityCode:administer* wfm:agent:administer* wfm:agentSchedule:view* wfm:historicalAdherence:view* wfm:intraday:view* wfm:managementUnit:administer* wfm:publishedSchedule:view* wfm:realtimeAdherence:view* wfm:schedule:administer* wfm:schedule:generate* wfm:serviceGoalGroup:administer* wfm:shortTermForecast:administer* wfm:agentTimeOffRequest:submit* wfm:timeOffRequest:administer* wfm:workPlan:administer

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.

try:
    # Get activity codes
    api_response = api_instance.get_workforcemanagement_managementunit_activitycodes(mu_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_activitycodes: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
{: class="table table-striped"}

### Return type

[**ActivityCodeContainer**](ActivityCodeContainer.html)

<a name="get_workforcemanagement_managementunit_intraday_queues"></a>

## [**WfmIntradayQueueListing**](WfmIntradayQueueListing.html) get_workforcemanagement_managementunit_intraday_queues(mu_id, date)



Get intraday queues for the given date



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/intraday/queues 

Requires ANY permissions: 

* wfm:intraday:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The management unit ID of the management unit, or 'mine' for the management unit of the logged-in user.
date = 'date_example' # str | ISO-8601 date string with no time or timezone component, interpreted in the configured management unit time zone, e.g. 2017-01-23

try:
    # Get intraday queues for the given date
    api_response = api_instance.get_workforcemanagement_managementunit_intraday_queues(mu_id, date)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_intraday_queues: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The management unit ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **date** | **str**| ISO-8601 date string with no time or timezone component, interpreted in the configured management unit time zone, e.g. 2017-01-23 |  |
{: class="table table-striped"}

### Return type

[**WfmIntradayQueueListing**](WfmIntradayQueueListing.html)

<a name="get_workforcemanagement_managementunit_user_timeoffrequest"></a>

## [**TimeOffRequestResponse**](TimeOffRequestResponse.html) get_workforcemanagement_managementunit_user_timeoffrequest(mu_id, user_id, time_off_request_id)



Get a time off request



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/users/{userId}/timeoffrequests/{timeOffRequestId} 

Requires ANY permissions: 

* wfm:timeOffRequest:administer

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The muId of the management unit, or 'mine' for the management unit of the logged-in user.
user_id = 'user_id_example' # str | The userId to whom the Time Off Request applies.
time_off_request_id = 'time_off_request_id_example' # str | Time Off Request Id

try:
    # Get a time off request
    api_response = api_instance.get_workforcemanagement_managementunit_user_timeoffrequest(mu_id, user_id, time_off_request_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_user_timeoffrequest: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The muId of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **user_id** | **str**| The userId to whom the Time Off Request applies. |  |
| **time_off_request_id** | **str**| Time Off Request Id |  |
{: class="table table-striped"}

### Return type

[**TimeOffRequestResponse**](TimeOffRequestResponse.html)

<a name="get_workforcemanagement_managementunit_user_timeoffrequests"></a>

## [**TimeOffRequestList**](TimeOffRequestList.html) get_workforcemanagement_managementunit_user_timeoffrequests(mu_id, user_id, recently_reviewed=recently_reviewed)



Get a list of time off requests for a given user



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/users/{userId}/timeoffrequests 

Requires ANY permissions: 

* wfm:timeOffRequest:administer

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The muId of the management unit, or 'mine' for the management unit of the logged-in user.
user_id = 'user_id_example' # str | The userId to whom the Time Off Request applies.
recently_reviewed = false # bool | Limit results to requests that have been reviewed within the preceding 30 days (optional) (default to false)

try:
    # Get a list of time off requests for a given user
    api_response = api_instance.get_workforcemanagement_managementunit_user_timeoffrequests(mu_id, user_id, recently_reviewed=recently_reviewed)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_user_timeoffrequests: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The muId of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **user_id** | **str**| The userId to whom the Time Off Request applies. |  |
| **recently_reviewed** | **bool**| Limit results to requests that have been reviewed within the preceding 30 days | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**TimeOffRequestList**](TimeOffRequestList.html)

<a name="get_workforcemanagement_managementunit_users"></a>

## [**WfmUserEntityListing**](WfmUserEntityListing.html) get_workforcemanagement_managementunit_users(mu_id)



Get agents in the management unit



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/users 

Requires ANY permissions: 

* wfm:agent:administer

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The management unit ID of the management unit, or 'mine' for the management unit of the logged-in user.

try:
    # Get agents in the management unit
    api_response = api_instance.get_workforcemanagement_managementunit_users(mu_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_users: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The management unit ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
{: class="table table-striped"}

### Return type

[**WfmUserEntityListing**](WfmUserEntityListing.html)

<a name="get_workforcemanagement_managementunits"></a>

## [**ManagementUnitListing**](ManagementUnitListing.html) get_workforcemanagement_managementunits(page_size=page_size, page_number=page_number, expand=expand)



Get management units



Wraps GET /api/v2/workforcemanagement/managementunits 

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
page_size = 56 # int |  (optional)
page_number = 56 # int |  (optional)
expand = 'expand_example' # str |  (optional)

try:
    # Get management units
    api_response = api_instance.get_workforcemanagement_managementunits(page_size=page_size, page_number=page_number, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunits: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**|  | [optional]  |
| **page_number** | **int**|  | [optional]  |
| **expand** | **str**|  | [optional] <br />**Values**: details |
{: class="table table-striped"}

### Return type

[**ManagementUnitListing**](ManagementUnitListing.html)

<a name="patch_workforcemanagement_managementunit_user_timeoffrequest"></a>

## [**TimeOffRequestResponse**](TimeOffRequestResponse.html) patch_workforcemanagement_managementunit_user_timeoffrequest(mu_id, user_id, time_off_request_id, body=body)



Update a time off request



Wraps PATCH /api/v2/workforcemanagement/managementunits/{muId}/users/{userId}/timeoffrequests/{timeOffRequestId} 

Requires ANY permissions: 

* wfm:timeOffRequest:administer

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The muId of the management unit, or 'mine' for the management unit of the logged-in user.
user_id = 'user_id_example' # str | The id of the user the requested time off request belongs to
time_off_request_id = 'time_off_request_id_example' # str | The id of the time off request to update
body = PureCloudPlatformClientV2.AdminTimeOffRequestPatch() # AdminTimeOffRequestPatch | body (optional)

try:
    # Update a time off request
    api_response = api_instance.patch_workforcemanagement_managementunit_user_timeoffrequest(mu_id, user_id, time_off_request_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_user_timeoffrequest: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The muId of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **user_id** | **str**| The id of the user the requested time off request belongs to |  |
| **time_off_request_id** | **str**| The id of the time off request to update |  |
| **body** | [**AdminTimeOffRequestPatch**](AdminTimeOffRequestPatch.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**TimeOffRequestResponse**](TimeOffRequestResponse.html)

<a name="post_workforcemanagement_managementunit_activitycodes"></a>

## [**ActivityCode**](ActivityCode.html) post_workforcemanagement_managementunit_activitycodes(mu_id, body=body)



Create a new activity code



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/activitycodes 

Requires ANY permissions: 

* wfm:activityCode:administer

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.CreateActivityCodeRequest() # CreateActivityCodeRequest | body (optional)

try:
    # Create a new activity code
    api_response = api_instance.post_workforcemanagement_managementunit_activitycodes(mu_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_activitycodes: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**CreateActivityCodeRequest**](CreateActivityCodeRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**ActivityCode**](ActivityCode.html)

<a name="post_workforcemanagement_managementunit_historicaladherencequery"></a>

## [**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse.html) post_workforcemanagement_managementunit_historicaladherencequery(mu_id, body=body)



Request a historical adherence report



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/historicaladherencequery 

Requires ANY permissions: 

* wfm:historicalAdherence:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The management unit ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.WfmHistoricalAdherenceQuery() # WfmHistoricalAdherenceQuery | body (optional)

try:
    # Request a historical adherence report
    api_response = api_instance.post_workforcemanagement_managementunit_historicaladherencequery(mu_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_historicaladherencequery: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The management unit ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**WfmHistoricalAdherenceQuery**](WfmHistoricalAdherenceQuery.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse.html)

<a name="post_workforcemanagement_managementunit_intraday"></a>

## [**IntradayResponse**](IntradayResponse.html) post_workforcemanagement_managementunit_intraday(mu_id, body=body)



Get intraday data for the given date for the requested queueIds



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/intraday 

Requires ANY permissions: 

* wfm:intraday:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The management unit ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.IntradayQueryDataCommand() # IntradayQueryDataCommand | body (optional)

try:
    # Get intraday data for the given date for the requested queueIds
    api_response = api_instance.post_workforcemanagement_managementunit_intraday(mu_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_intraday: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The management unit ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**IntradayQueryDataCommand**](IntradayQueryDataCommand.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**IntradayResponse**](IntradayResponse.html)

<a name="post_workforcemanagement_managementunit_schedules_search"></a>

## [**UserScheduleContainer**](UserScheduleContainer.html) post_workforcemanagement_managementunit_schedules_search(mu_id, body=body)



Query published schedules for given given time range for set of users



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/schedules/search 

Requires ANY permissions: 

* wfm:schedule:administer* wfm:publishedSchedule:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The management unit ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.UserListScheduleRequestBody() # UserListScheduleRequestBody | body (optional)

try:
    # Query published schedules for given given time range for set of users
    api_response = api_instance.post_workforcemanagement_managementunit_schedules_search(mu_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_schedules_search: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The management unit ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**UserListScheduleRequestBody**](UserListScheduleRequestBody.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**UserScheduleContainer**](UserScheduleContainer.html)


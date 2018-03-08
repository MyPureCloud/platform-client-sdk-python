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
|[**get_workforcemanagement_managementunit_user_timeoffrequest**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_user_timeoffrequest) | Get a time off request by id|
|[**get_workforcemanagement_managementunit_user_timeoffrequests**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_user_timeoffrequests) | Get a list of time off requests for any user|
|[**get_workforcemanagement_managementunit_users**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_users) | Get agents in the management unit|
|[**get_workforcemanagement_managementunits**](WorkforceManagementApi.html#get_workforcemanagement_managementunits) | Get management units|
|[**post_workforcemanagement_managementunit_activitycodes**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_activitycodes) | Create a new activity code|
|[**post_workforcemanagement_managementunit_historicaladherencequery**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_historicaladherencequery) | Request a historical adherence report|
|[**post_workforcemanagement_managementunit_intraday**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_intraday) | Get intraday data for the given date for the requested queueIds|
|[**post_workforcemanagement_managementunit_schedules_search**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_schedules_search) | Get user schedules within the given time range|
{: class="table table-striped"}

<a name="get_workforcemanagement_adherence"></a>

## [**list[UserScheduleAdherence]**](UserScheduleAdherence.html) get_workforcemanagement_adherence(user_id)

Get a list of UserScheduleAdherence records for the requested users



Wraps GET /api/v2/workforcemanagement/adherence 

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
| **mu_id** | **str**| The muId of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
{: class="table table-striped"}

### Return type

[**ActivityCodeContainer**](ActivityCodeContainer.html)

<a name="get_workforcemanagement_managementunit_intraday_queues"></a>

## [**WfmIntradayQueueListing**](WfmIntradayQueueListing.html) get_workforcemanagement_managementunit_intraday_queues(mu_id, date)

Get intraday queues for the given date



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/intraday/queues 

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
| **mu_id** | **str**| The muId of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **date** | **str**| ISO-8601 date string with no time or timezone component, interpreted in the configured management unit time zone, e.g. 2017-01-23 |  |
{: class="table table-striped"}

### Return type

[**WfmIntradayQueueListing**](WfmIntradayQueueListing.html)

<a name="get_workforcemanagement_managementunit_user_timeoffrequest"></a>

## [**TimeOffRequest**](TimeOffRequest.html) get_workforcemanagement_managementunit_user_timeoffrequest(mu_id, user_id, time_off_request_id)

Get a time off request by id



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/users/{userId}/timeoffrequests/{timeOffRequestId} 

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
    # Get a time off request by id
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

[**TimeOffRequest**](TimeOffRequest.html)

<a name="get_workforcemanagement_managementunit_user_timeoffrequests"></a>

## [**TimeOffRequestList**](TimeOffRequestList.html) get_workforcemanagement_managementunit_user_timeoffrequests(mu_id, user_id, recently_reviewed=recently_reviewed)

Get a list of time off requests for any user



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/users/{userId}/timeoffrequests 

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
    # Get a list of time off requests for any user
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
| **mu_id** | **str**| The muId of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
{: class="table table-striped"}

### Return type

[**WfmUserEntityListing**](WfmUserEntityListing.html)

<a name="get_workforcemanagement_managementunits"></a>

## [**ManagementUnitListing**](ManagementUnitListing.html) get_workforcemanagement_managementunits(page_size=page_size, page_number=page_number, expand=expand)

Get management units



Wraps GET /api/v2/workforcemanagement/managementunits 

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
page_number = 1 # int |  (optional) (default to 1)
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
| **page_number** | **int**|  | [optional] [default to 1] |
| **expand** | **str**|  | [optional] <br />**Values**: details |
{: class="table table-striped"}

### Return type

[**ManagementUnitListing**](ManagementUnitListing.html)

<a name="post_workforcemanagement_managementunit_activitycodes"></a>

## [**ActivityCode**](ActivityCode.html) post_workforcemanagement_managementunit_activitycodes(mu_id, body=body)

Create a new activity code



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/activitycodes 

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
| **mu_id** | **str**| The muId of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**CreateActivityCodeRequest**](CreateActivityCodeRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**ActivityCode**](ActivityCode.html)

<a name="post_workforcemanagement_managementunit_historicaladherencequery"></a>

## [**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse.html) post_workforcemanagement_managementunit_historicaladherencequery(mu_id, body=body)

Request a historical adherence report



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/historicaladherencequery 

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
| **mu_id** | **str**| The muId of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**WfmHistoricalAdherenceQuery**](WfmHistoricalAdherenceQuery.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse.html)

<a name="post_workforcemanagement_managementunit_intraday"></a>

## [**IntradayResponse**](IntradayResponse.html) post_workforcemanagement_managementunit_intraday(mu_id, body=body)

Get intraday data for the given date for the requested queueIds



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/intraday 

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
| **mu_id** | **str**| The muId of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**IntradayQueryDataCommand**](IntradayQueryDataCommand.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**IntradayResponse**](IntradayResponse.html)

<a name="post_workforcemanagement_managementunit_schedules_search"></a>

## [**UserScheduleContainer**](UserScheduleContainer.html) post_workforcemanagement_managementunit_schedules_search(mu_id, body=body)

Get user schedules within the given time range



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/schedules/search 

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
body = PureCloudPlatformClientV2.UserListScheduleRequestBody() # UserListScheduleRequestBody | body (optional)

try:
    # Get user schedules within the given time range
    api_response = api_instance.post_workforcemanagement_managementunit_schedules_search(mu_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_schedules_search: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The muId of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**UserListScheduleRequestBody**](UserListScheduleRequestBody.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**UserScheduleContainer**](UserScheduleContainer.html)


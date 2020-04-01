---
title: WorkforceManagementApi
---

## PureCloudPlatformClientV2.WorkforceManagementApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_workforcemanagement_managementunit**](WorkforceManagementApi.html#delete_workforcemanagement_managementunit) | Delete management unit|
|[**delete_workforcemanagement_managementunit_activitycode**](WorkforceManagementApi.html#delete_workforcemanagement_managementunit_activitycode) | Deletes an activity code|
|[**delete_workforcemanagement_managementunit_scheduling_run**](WorkforceManagementApi.html#delete_workforcemanagement_managementunit_scheduling_run) | Cancel a schedule run|
|[**delete_workforcemanagement_managementunit_servicegoalgroup**](WorkforceManagementApi.html#delete_workforcemanagement_managementunit_servicegoalgroup) | Delete a service goal group|
|[**delete_workforcemanagement_managementunit_week_schedule**](WorkforceManagementApi.html#delete_workforcemanagement_managementunit_week_schedule) | Delete a schedule|
|[**delete_workforcemanagement_managementunit_week_shorttermforecast**](WorkforceManagementApi.html#delete_workforcemanagement_managementunit_week_shorttermforecast) | Delete a short term forecast|
|[**delete_workforcemanagement_managementunit_workplan**](WorkforceManagementApi.html#delete_workforcemanagement_managementunit_workplan) | Delete a work plan|
|[**get_workforcemanagement_adherence**](WorkforceManagementApi.html#get_workforcemanagement_adherence) | Get a list of UserScheduleAdherence records for the requested users|
|[**get_workforcemanagement_adhocmodelingjob**](WorkforceManagementApi.html#get_workforcemanagement_adhocmodelingjob) | Get status of the modeling job|
|[**get_workforcemanagement_managementunit**](WorkforceManagementApi.html#get_workforcemanagement_managementunit) | Get management unit|
|[**get_workforcemanagement_managementunit_activitycode**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_activitycode) | Get an activity code|
|[**get_workforcemanagement_managementunit_activitycodes**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_activitycodes) | Get activity codes|
|[**get_workforcemanagement_managementunit_agent**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_agent) | Get data for agent in the management unit|
|[**get_workforcemanagement_managementunit_intraday_queues**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_intraday_queues) | Get intraday queues for the given date|
|[**get_workforcemanagement_managementunit_scheduling_run**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_scheduling_run) | Gets the status for a specific scheduling run|
|[**get_workforcemanagement_managementunit_scheduling_run_result**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_scheduling_run_result) | Gets the result of a specific scheduling run|
|[**get_workforcemanagement_managementunit_scheduling_runs**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_scheduling_runs) | Get the status of all the ongoing schedule runs|
|[**get_workforcemanagement_managementunit_servicegoalgroup**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_servicegoalgroup) | Get a service goal group|
|[**get_workforcemanagement_managementunit_servicegoalgroups**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_servicegoalgroups) | Get service goal groups|
|[**get_workforcemanagement_managementunit_settings**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_settings) | Get the settings for the requested management unit. Deprecated, use the GET management unit route instead|
|[**get_workforcemanagement_managementunit_shifttrades_matched**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_shifttrades_matched) | Gets a summary of all shift trades in the matched state|
|[**get_workforcemanagement_managementunit_shifttrades_users**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_shifttrades_users) | Gets list of users available for whom you can send direct shift trade requests|
|[**get_workforcemanagement_managementunit_user_timeoffrequest**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_user_timeoffrequest) | Get a time off request|
|[**get_workforcemanagement_managementunit_user_timeoffrequests**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_user_timeoffrequests) | Get a list of time off requests for a given user|
|[**get_workforcemanagement_managementunit_users**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_users) | Get users in the management unit|
|[**get_workforcemanagement_managementunit_week_schedule**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_week_schedule) | Get a week schedule|
|[**get_workforcemanagement_managementunit_week_schedule_generationresults**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_week_schedule_generationresults) | Get week schedule generation results|
|[**get_workforcemanagement_managementunit_week_schedules**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_week_schedules) | Get the list of schedules in a week in management unit|
|[**get_workforcemanagement_managementunit_week_shorttermforecast_final**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_week_shorttermforecast_final) | Get the final result of a short term forecast calculation with modifications applied|
|[**get_workforcemanagement_managementunit_week_shorttermforecasts**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_week_shorttermforecasts) | Get short term forecasts|
|[**get_workforcemanagement_managementunit_workplan**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_workplan) | Get a work plan|
|[**get_workforcemanagement_managementunit_workplans**](WorkforceManagementApi.html#get_workforcemanagement_managementunit_workplans) | Get work plans|
|[**get_workforcemanagement_managementunits**](WorkforceManagementApi.html#get_workforcemanagement_managementunits) | Get management units|
|[**get_workforcemanagement_managementunits_divisionviews**](WorkforceManagementApi.html#get_workforcemanagement_managementunits_divisionviews) | Get management units across divisions|
|[**get_workforcemanagement_notifications**](WorkforceManagementApi.html#get_workforcemanagement_notifications) | Get a list of notifications for the current user|
|[**get_workforcemanagement_schedulingjob**](WorkforceManagementApi.html#get_workforcemanagement_schedulingjob) | Get status of the scheduling job|
|[**get_workforcemanagement_shifttrades**](WorkforceManagementApi.html#get_workforcemanagement_shifttrades) | Gets all of my shift trades|
|[**get_workforcemanagement_timeoffrequest**](WorkforceManagementApi.html#get_workforcemanagement_timeoffrequest) | Get a time off request for the current user|
|[**get_workforcemanagement_timeoffrequests**](WorkforceManagementApi.html#get_workforcemanagement_timeoffrequests) | Get a list of time off requests for the current user|
|[**patch_workforcemanagement_managementunit**](WorkforceManagementApi.html#patch_workforcemanagement_managementunit) | Update the requested management unit|
|[**patch_workforcemanagement_managementunit_activitycode**](WorkforceManagementApi.html#patch_workforcemanagement_managementunit_activitycode) | Update an activity code|
|[**patch_workforcemanagement_managementunit_scheduling_run**](WorkforceManagementApi.html#patch_workforcemanagement_managementunit_scheduling_run) | Marks a specific scheduling run as applied, allowing a new rescheduling run to be started|
|[**patch_workforcemanagement_managementunit_servicegoalgroup**](WorkforceManagementApi.html#patch_workforcemanagement_managementunit_servicegoalgroup) | Update a service goal group|
|[**patch_workforcemanagement_managementunit_settings**](WorkforceManagementApi.html#patch_workforcemanagement_managementunit_settings) | Update the settings for the requested management unit|
|[**patch_workforcemanagement_managementunit_user_timeoffrequest**](WorkforceManagementApi.html#patch_workforcemanagement_managementunit_user_timeoffrequest) | Update a time off request|
|[**patch_workforcemanagement_managementunit_week_schedule**](WorkforceManagementApi.html#patch_workforcemanagement_managementunit_week_schedule) | Update a week schedule|
|[**patch_workforcemanagement_managementunit_workplan**](WorkforceManagementApi.html#patch_workforcemanagement_managementunit_workplan) | Update a work plan|
|[**patch_workforcemanagement_timeoffrequest**](WorkforceManagementApi.html#patch_workforcemanagement_timeoffrequest) | Update a time off request for the current user|
|[**post_workforcemanagement_adherence_historical**](WorkforceManagementApi.html#post_workforcemanagement_adherence_historical) | Request a historical adherence report for users across management units|
|[**post_workforcemanagement_managementunit_activitycodes**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_activitycodes) | Create a new activity code|
|[**post_workforcemanagement_managementunit_agentschedules_search**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_agentschedules_search) | Query published schedules for given given time range for set of users|
|[**post_workforcemanagement_managementunit_historicaladherencequery**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_historicaladherencequery) | Request a historical adherence report|
|[**post_workforcemanagement_managementunit_intraday**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_intraday) | Get intraday data for the given date for the requested queueIds|
|[**post_workforcemanagement_managementunit_move**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_move) | Move the requested management unit to a new business unit|
|[**post_workforcemanagement_managementunit_schedules_search**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_schedules_search) | Query published schedules for given given time range for set of users|
|[**post_workforcemanagement_managementunit_servicegoalgroups**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_servicegoalgroups) | Create a new service goal group|
|[**post_workforcemanagement_managementunit_timeoffrequests**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_timeoffrequests) | Create a new time off request|
|[**post_workforcemanagement_managementunit_timeoffrequests_fetchdetails**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_timeoffrequests_fetchdetails) | Gets a list of time off requests from lookup ids|
|[**post_workforcemanagement_managementunit_timeoffrequests_query**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_timeoffrequests_query) | Gets the lookup ids to fetch the specified set of requests|
|[**post_workforcemanagement_managementunit_week_schedule_copy**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_week_schedule_copy) | Copy a week schedule|
|[**post_workforcemanagement_managementunit_week_schedule_reschedule**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_week_schedule_reschedule) | Start a scheduling run to compute the reschedule. When the scheduling run finishes, a client can get the reschedule changes and then the client can apply them to the schedule, save the schedule, and mark the scheduling run as applied|
|[**post_workforcemanagement_managementunit_week_schedules**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_week_schedules) | Add a schedule for a week in management unit using imported data. Use partial uploads of user schedules if activity count in schedule is greater than 17500|
|[**post_workforcemanagement_managementunit_week_schedules_generate**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_week_schedules_generate) | Generate a week schedule|
|[**post_workforcemanagement_managementunit_week_schedules_partialupload**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_week_schedules_partialupload) | Partial upload of user schedules where activity count is greater than 17500|
|[**post_workforcemanagement_managementunit_week_shorttermforecast_copy**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_week_shorttermforecast_copy) | Copy a short term forecast|
|[**post_workforcemanagement_managementunit_week_shorttermforecasts**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_week_shorttermforecasts) | Import a short term forecast|
|[**post_workforcemanagement_managementunit_week_shorttermforecasts_generate**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_week_shorttermforecasts_generate) | Generate a short term forecast|
|[**post_workforcemanagement_managementunit_week_shorttermforecasts_partialupload**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_week_shorttermforecasts_partialupload) | Import a short term forecast|
|[**post_workforcemanagement_managementunit_workplan_copy**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_workplan_copy) | Create a copy of work plan|
|[**post_workforcemanagement_managementunit_workplans**](WorkforceManagementApi.html#post_workforcemanagement_managementunit_workplans) | Create a new work plan|
|[**post_workforcemanagement_managementunits**](WorkforceManagementApi.html#post_workforcemanagement_managementunits) | Add a management unit|
|[**post_workforcemanagement_notifications_update**](WorkforceManagementApi.html#post_workforcemanagement_notifications_update) | Mark a list of notifications as read or unread|
|[**post_workforcemanagement_schedules**](WorkforceManagementApi.html#post_workforcemanagement_schedules) | Get published schedule for the current user|
|[**post_workforcemanagement_timeoffrequests**](WorkforceManagementApi.html#post_workforcemanagement_timeoffrequests) | Create a time off request for the current user|
{: class="table table-striped"}

<a name="delete_workforcemanagement_managementunit"></a>

##  delete_workforcemanagement_managementunit(mu_id)



Delete management unit



Wraps DELETE /api/v2/workforcemanagement/managementunits/{muId} 

Requires ANY permissions: 

* wfm:managementUnit:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.

try:
    # Delete management unit
    api_instance.delete_workforcemanagement_managementunit(mu_id)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->delete_workforcemanagement_managementunit: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_workforcemanagement_managementunit_activitycode"></a>

##  delete_workforcemanagement_managementunit_activitycode(mu_id, ac_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Deletes an activity code



Wraps DELETE /api/v2/workforcemanagement/managementunits/{muId}/activitycodes/{acId} 

Requires ANY permissions: 

* wfm:activityCode:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
ac_id = 'ac_id_example' # str | The ID of the activity code to delete

try:
    # Deletes an activity code
    api_instance.delete_workforcemanagement_managementunit_activitycode(mu_id, ac_id)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->delete_workforcemanagement_managementunit_activitycode: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **ac_id** | **str**| The ID of the activity code to delete |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_workforcemanagement_managementunit_scheduling_run"></a>

##  delete_workforcemanagement_managementunit_scheduling_run(management_unit_id, run_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Cancel a schedule run



Wraps DELETE /api/v2/workforcemanagement/managementunits/{managementUnitId}/scheduling/runs/{runId} 

Requires ANY permissions: 

* wfm:schedule:generate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
run_id = 'run_id_example' # str | The ID of the schedule run

try:
    # Cancel a schedule run
    api_instance.delete_workforcemanagement_managementunit_scheduling_run(management_unit_id, run_id)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->delete_workforcemanagement_managementunit_scheduling_run: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **run_id** | **str**| The ID of the schedule run |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_workforcemanagement_managementunit_servicegoalgroup"></a>

##  delete_workforcemanagement_managementunit_servicegoalgroup(management_unit_id, service_goal_group_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Delete a service goal group



Wraps DELETE /api/v2/workforcemanagement/managementunits/{managementUnitId}/servicegoalgroups/{serviceGoalGroupId} 

Requires ANY permissions: 

* wfm:serviceGoalGroup:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
service_goal_group_id = 'service_goal_group_id_example' # str | The ID of the service goal group to delete

try:
    # Delete a service goal group
    api_instance.delete_workforcemanagement_managementunit_servicegoalgroup(management_unit_id, service_goal_group_id)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->delete_workforcemanagement_managementunit_servicegoalgroup: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **service_goal_group_id** | **str**| The ID of the service goal group to delete |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_workforcemanagement_managementunit_week_schedule"></a>

##  delete_workforcemanagement_managementunit_week_schedule(management_unit_id, week_id, schedule_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Delete a schedule



Wraps DELETE /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekId}/schedules/{scheduleId} 

Requires ANY permissions: 

* wfm:schedule:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format.
schedule_id = 'schedule_id_example' # str | The ID of theschedule to delete

try:
    # Delete a schedule
    api_instance.delete_workforcemanagement_managementunit_week_schedule(management_unit_id, week_id, schedule_id)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->delete_workforcemanagement_managementunit_week_schedule: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format. |  |
| **schedule_id** | **str**| The ID of theschedule to delete |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_workforcemanagement_managementunit_week_shorttermforecast"></a>

##  delete_workforcemanagement_managementunit_week_shorttermforecast(management_unit_id, week_date_id, forecast_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Delete a short term forecast

Must not be tied to any schedules

Wraps DELETE /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId} 

Requires ANY permissions: 

* wfm:shortTermForecast:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The management unit ID of the management unit to which the forecast belongs
week_date_id = 'week_date_id_example' # str | The week start date of the forecast in yyyy-MM-dd format
forecast_id = 'forecast_id_example' # str | The ID of the forecast

try:
    # Delete a short term forecast
    api_instance.delete_workforcemanagement_managementunit_week_shorttermforecast(management_unit_id, week_date_id, forecast_id)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->delete_workforcemanagement_managementunit_week_shorttermforecast: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The management unit ID of the management unit to which the forecast belongs |  |
| **week_date_id** | **str**| The week start date of the forecast in yyyy-MM-dd format |  |
| **forecast_id** | **str**| The ID of the forecast |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_workforcemanagement_managementunit_workplan"></a>

##  delete_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id)



Delete a work plan



Wraps DELETE /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans/{workPlanId} 

Requires ANY permissions: 

* wfm:workPlan:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
work_plan_id = 'work_plan_id_example' # str | The ID of the work plan to delete

try:
    # Delete a work plan
    api_instance.delete_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->delete_workforcemanagement_managementunit_workplan: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **work_plan_id** | **str**| The ID of the work plan to delete |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_workforcemanagement_adherence"></a>

## [**list[UserScheduleAdherence]**](UserScheduleAdherence.html) get_workforcemanagement_adherence(user_id)



Get a list of UserScheduleAdherence records for the requested users



Wraps GET /api/v2/workforcemanagement/adherence 

Requires ANY permissions: 

* wfm:realtimeAdherence:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | [**list[str]**](str.html)| User Id(s) for which to fetch current schedule adherence information.  Min 1, Max of 100 userIds per request |  |
{: class="table table-striped"}

### Return type

[**list[UserScheduleAdherence]**](UserScheduleAdherence.html)

<a name="get_workforcemanagement_adhocmodelingjob"></a>

## [**ModelingStatusResponse**](ModelingStatusResponse.html) get_workforcemanagement_adhocmodelingjob(job_id)



Get status of the modeling job



Wraps GET /api/v2/workforcemanagement/adhocmodelingjobs/{jobId} 

Requires ANY permissions: 

* wfm:adhocModel:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | The id of the modeling job

try:
    # Get status of the modeling job
    api_response = api_instance.get_workforcemanagement_adhocmodelingjob(job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_adhocmodelingjob: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The id of the modeling job |  |
{: class="table table-striped"}

### Return type

[**ModelingStatusResponse**](ModelingStatusResponse.html)

<a name="get_workforcemanagement_managementunit"></a>

## [**ManagementUnit**](ManagementUnit.html) get_workforcemanagement_managementunit(mu_id, expand=expand)



Get management unit



Wraps GET /api/v2/workforcemanagement/managementunits/{muId} 

Requires ANY permissions: 

* wfm:activityCode:add
* wfm:activityCode:delete
* wfm:activityCode:edit
* wfm:activityCode:view
* wfm:agent:edit
* wfm:agentSchedule:view
* wfm:agentTimeOffRequest:submit
* wfm:agent:view
* wfm:businessUnit:add
* wfm:businessUnit:delete
* wfm:businessUnit:edit
* wfm:businessUnit:view
* wfm:historicalAdherence:view
* wfm:intraday:view
* wfm:managementUnit:add
* wfm:managementUnit:delete
* wfm:managementUnit:edit
* wfm:managementUnit:view
* wfm:publishedSchedule:view
* wfm:realtimeAdherence:view
* wfm:schedule:add
* wfm:schedule:delete
* wfm:schedule:edit
* wfm:schedule:generate
* wfm:schedule:view
* wfm:serviceGoalGroup:add
* wfm:serviceGoalGroup:delete
* wfm:serviceGoalGroup:edit
* wfm:serviceGoalGroup:view
* wfm:serviceGoalTemplate:add
* wfm:serviceGoalTemplate:delete
* wfm:serviceGoalTemplate:edit
* wfm:serviceGoalTemplate:view
* wfm:planningGroup:add
* wfm:planningGroup:delete
* wfm:planningGroup:edit
* wfm:planningGroup:view
* wfm:shiftTradeRequest:edit
* wfm:shiftTradeRequest:view
* wfm:agentShiftTradeRequest:participate
* wfm:shortTermForecast:add
* wfm:shortTermForecast:delete
* wfm:shortTermForecast:edit
* wfm:shortTermForecast:view
* wfm:timeOffRequest:add
* wfm:timeOffRequest:edit
* wfm:timeOffRequest:view
* wfm:workPlan:add
* wfm:workPlan:delete
* wfm:workPlan:edit
* wfm:workPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
expand = ['expand_example'] # list[str] |  (optional)

try:
    # Get management unit
    api_response = api_instance.get_workforcemanagement_managementunit(mu_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **expand** | [**list[str]**](str.html)|  | [optional] <br />**Values**: settings, settings.adherence, settings.timeOff, settings.scheduling, settings.shortTermForecasting, settings.shiftTrading |
{: class="table table-striped"}

### Return type

[**ManagementUnit**](ManagementUnit.html)

<a name="get_workforcemanagement_managementunit_activitycode"></a>

## [**ActivityCode**](ActivityCode.html) get_workforcemanagement_managementunit_activitycode(mu_id, ac_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get an activity code



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/activitycodes/{acId} 

Requires ANY permissions: 

* wfm:activityCode:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
ac_id = 'ac_id_example' # str | The ID of the activity code to fetch

try:
    # Get an activity code
    api_response = api_instance.get_workforcemanagement_managementunit_activitycode(mu_id, ac_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_activitycode: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **ac_id** | **str**| The ID of the activity code to fetch |  |
{: class="table table-striped"}

### Return type

[**ActivityCode**](ActivityCode.html)

<a name="get_workforcemanagement_managementunit_activitycodes"></a>

## [**ActivityCodeContainer**](ActivityCodeContainer.html) get_workforcemanagement_managementunit_activitycodes(mu_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get activity codes



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/activitycodes 

Requires ANY permissions: 

* wfm:activityCode:add
* wfm:activityCode:delete
* wfm:activityCode:edit
* wfm:activityCode:view
* wfm:agent:edit
* wfm:agentSchedule:view
* wfm:agentTimeOffRequest:submit
* wfm:agent:view
* wfm:businessUnit:add
* wfm:businessUnit:delete
* wfm:businessUnit:edit
* wfm:businessUnit:view
* wfm:historicalAdherence:view
* wfm:intraday:view
* wfm:managementUnit:add
* wfm:managementUnit:delete
* wfm:managementUnit:edit
* wfm:managementUnit:view
* wfm:publishedSchedule:view
* wfm:realtimeAdherence:view
* wfm:schedule:add
* wfm:schedule:delete
* wfm:schedule:edit
* wfm:schedule:generate
* wfm:schedule:view
* wfm:serviceGoalGroup:add
* wfm:serviceGoalGroup:delete
* wfm:serviceGoalGroup:edit
* wfm:serviceGoalGroup:view
* wfm:shortTermForecast:add
* wfm:shortTermForecast:delete
* wfm:shortTermForecast:edit
* wfm:shortTermForecast:view
* wfm:timeOffRequest:add
* wfm:timeOffRequest:edit
* wfm:timeOffRequest:view
* wfm:workPlan:add
* wfm:workPlan:delete
* wfm:workPlan:edit
* wfm:workPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
{: class="table table-striped"}

### Return type

[**ActivityCodeContainer**](ActivityCodeContainer.html)

<a name="get_workforcemanagement_managementunit_agent"></a>

## [**WfmAgent**](WfmAgent.html) get_workforcemanagement_managementunit_agent(management_unit_id, agent_id)



Get data for agent in the management unit



Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/agents/{agentId} 

Requires ANY permissions: 

* wfm:agent:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The id of the management unit, or 'mine' for the management unit of the logged-in user.
agent_id = 'agent_id_example' # str | The agent id

try:
    # Get data for agent in the management unit
    api_response = api_instance.get_workforcemanagement_managementunit_agent(management_unit_id, agent_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_agent: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The id of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **agent_id** | **str**| The agent id |  |
{: class="table table-striped"}

### Return type

[**WfmAgent**](WfmAgent.html)

<a name="get_workforcemanagement_managementunit_intraday_queues"></a>

## [**WfmIntradayQueueListing**](WfmIntradayQueueListing.html) get_workforcemanagement_managementunit_intraday_queues(mu_id, date)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get intraday queues for the given date



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/intraday/queues 

Requires ANY permissions: 

* wfm:intraday:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The management unit ID of the management unit
date = 'date_example' # str | yyyy-MM-dd date string interpreted in the configured management unit time zone

try:
    # Get intraday queues for the given date
    api_response = api_instance.get_workforcemanagement_managementunit_intraday_queues(mu_id, date)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_intraday_queues: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The management unit ID of the management unit |  |
| **date** | **str**| yyyy-MM-dd date string interpreted in the configured management unit time zone |  |
{: class="table table-striped"}

### Return type

[**WfmIntradayQueueListing**](WfmIntradayQueueListing.html)

<a name="get_workforcemanagement_managementunit_scheduling_run"></a>

## [**SchedulingRunResponse**](SchedulingRunResponse.html) get_workforcemanagement_managementunit_scheduling_run(management_unit_id, run_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Gets the status for a specific scheduling run



Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/scheduling/runs/{runId} 

Requires ANY permissions: 

* wfm:schedule:generate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
run_id = 'run_id_example' # str | The ID of the schedule run

try:
    # Gets the status for a specific scheduling run
    api_response = api_instance.get_workforcemanagement_managementunit_scheduling_run(management_unit_id, run_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_scheduling_run: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **run_id** | **str**| The ID of the schedule run |  |
{: class="table table-striped"}

### Return type

[**SchedulingRunResponse**](SchedulingRunResponse.html)

<a name="get_workforcemanagement_managementunit_scheduling_run_result"></a>

## [**RescheduleResult**](RescheduleResult.html) get_workforcemanagement_managementunit_scheduling_run_result(management_unit_id, run_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Gets the result of a specific scheduling run



Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/scheduling/runs/{runId}/result 

Requires ANY permissions: 

* wfm:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
run_id = 'run_id_example' # str | The ID of the schedule run

try:
    # Gets the result of a specific scheduling run
    api_response = api_instance.get_workforcemanagement_managementunit_scheduling_run_result(management_unit_id, run_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_scheduling_run_result: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **run_id** | **str**| The ID of the schedule run |  |
{: class="table table-striped"}

### Return type

[**RescheduleResult**](RescheduleResult.html)

<a name="get_workforcemanagement_managementunit_scheduling_runs"></a>

## [**SchedulingRunListResponse**](SchedulingRunListResponse.html) get_workforcemanagement_managementunit_scheduling_runs(management_unit_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get the status of all the ongoing schedule runs



Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/scheduling/runs 

Requires ANY permissions: 

* wfm:schedule:generate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.

try:
    # Get the status of all the ongoing schedule runs
    api_response = api_instance.get_workforcemanagement_managementunit_scheduling_runs(management_unit_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_scheduling_runs: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
{: class="table table-striped"}

### Return type

[**SchedulingRunListResponse**](SchedulingRunListResponse.html)

<a name="get_workforcemanagement_managementunit_servicegoalgroup"></a>

## [**ServiceGoalGroup**](ServiceGoalGroup.html) get_workforcemanagement_managementunit_servicegoalgroup(management_unit_id, service_goal_group_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get a service goal group



Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/servicegoalgroups/{serviceGoalGroupId} 

Requires ANY permissions: 

* wfm:serviceGoalGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
service_goal_group_id = 'service_goal_group_id_example' # str | The ID of the service goal group to fetch

try:
    # Get a service goal group
    api_response = api_instance.get_workforcemanagement_managementunit_servicegoalgroup(management_unit_id, service_goal_group_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_servicegoalgroup: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **service_goal_group_id** | **str**| The ID of the service goal group to fetch |  |
{: class="table table-striped"}

### Return type

[**ServiceGoalGroup**](ServiceGoalGroup.html)

<a name="get_workforcemanagement_managementunit_servicegoalgroups"></a>

## [**ServiceGoalGroupList**](ServiceGoalGroupList.html) get_workforcemanagement_managementunit_servicegoalgroups(management_unit_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get service goal groups



Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/servicegoalgroups 

Requires ANY permissions: 

* wfm:serviceGoalGroup:view
* wfm:shortTermForecast:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.

try:
    # Get service goal groups
    api_response = api_instance.get_workforcemanagement_managementunit_servicegoalgroups(management_unit_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_servicegoalgroups: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
{: class="table table-striped"}

### Return type

[**ServiceGoalGroupList**](ServiceGoalGroupList.html)

<a name="get_workforcemanagement_managementunit_settings"></a>

## [**ManagementUnitSettingsResponse**](ManagementUnitSettingsResponse.html) get_workforcemanagement_managementunit_settings(mu_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get the settings for the requested management unit. Deprecated, use the GET management unit route instead



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/settings 

Requires ANY permissions: 

* wfm:managementUnit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.

try:
    # Get the settings for the requested management unit. Deprecated, use the GET management unit route instead
    api_response = api_instance.get_workforcemanagement_managementunit_settings(mu_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_settings: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
{: class="table table-striped"}

### Return type

[**ManagementUnitSettingsResponse**](ManagementUnitSettingsResponse.html)

<a name="get_workforcemanagement_managementunit_shifttrades_matched"></a>

## [**ShiftTradeMatchesSummaryResponse**](ShiftTradeMatchesSummaryResponse.html) get_workforcemanagement_managementunit_shifttrades_matched(mu_id)



Gets a summary of all shift trades in the matched state



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/shifttrades/matched 

Requires ANY permissions: 

* wfm:shiftTradeRequest:view
* wfm:shiftTradeRequest:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The management unit ID of the management unit, or 'mine' for the management unit of the logged-in user.

try:
    # Gets a summary of all shift trades in the matched state
    api_response = api_instance.get_workforcemanagement_managementunit_shifttrades_matched(mu_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_shifttrades_matched: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The management unit ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
{: class="table table-striped"}

### Return type

[**ShiftTradeMatchesSummaryResponse**](ShiftTradeMatchesSummaryResponse.html)

<a name="get_workforcemanagement_managementunit_shifttrades_users"></a>

## [**WfmUserEntityListing**](WfmUserEntityListing.html) get_workforcemanagement_managementunit_shifttrades_users(mu_id)



Gets list of users available for whom you can send direct shift trade requests



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/shifttrades/users 

Requires ANY permissions: 

* wfm:agentShiftTradeRequest:participate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The management unit ID of the management unit, or 'mine' for the management unit of the logged-in user.

try:
    # Gets list of users available for whom you can send direct shift trade requests
    api_response = api_instance.get_workforcemanagement_managementunit_shifttrades_users(mu_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_shifttrades_users: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The management unit ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
{: class="table table-striped"}

### Return type

[**WfmUserEntityListing**](WfmUserEntityListing.html)

<a name="get_workforcemanagement_managementunit_user_timeoffrequest"></a>

## [**TimeOffRequestResponse**](TimeOffRequestResponse.html) get_workforcemanagement_managementunit_user_timeoffrequest(mu_id, user_id, time_off_request_id)



Get a time off request



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/users/{userId}/timeoffrequests/{timeOffRequestId} 

Requires ANY permissions: 

* wfm:timeOffRequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
```

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

* wfm:timeOffRequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
```

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



Get users in the management unit



Wraps GET /api/v2/workforcemanagement/managementunits/{muId}/users 

Requires ANY permissions: 

* wfm:agent:view
* wfm:historicalAdherence:view
* wfm:publishedSchedule:view
* wfm:realtimeAdherence:view
* wfm:schedule:view
* wfm:timeOffRequest:view
* wfm:workPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The management unit ID of the management unit, or 'mine' for the management unit of the logged-in user.

try:
    # Get users in the management unit
    api_response = api_instance.get_workforcemanagement_managementunit_users(mu_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_users: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The management unit ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
{: class="table table-striped"}

### Return type

[**WfmUserEntityListing**](WfmUserEntityListing.html)

<a name="get_workforcemanagement_managementunit_week_schedule"></a>

## [**WeekScheduleResponse**](WeekScheduleResponse.html) get_workforcemanagement_managementunit_week_schedule(management_unit_id, week_id, schedule_id, expand=expand, force_download_service=force_download_service)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get a week schedule



Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekId}/schedules/{scheduleId} 

Requires ANY permissions: 

* wfm:publishedSchedule:view
* wfm:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format.
schedule_id = 'schedule_id_example' # str | The ID of the schedule to fetch
expand = 'expand_example' # str | Which fields, if any, to expand (optional)
force_download_service = true # bool | Force the result of this operation to be sent via download service.  For testing/app development purposes (optional)

try:
    # Get a week schedule
    api_response = api_instance.get_workforcemanagement_managementunit_week_schedule(management_unit_id, week_id, schedule_id, expand=expand, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_week_schedule: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format. |  |
| **schedule_id** | **str**| The ID of the schedule to fetch |  |
| **expand** | **str**| Which fields, if any, to expand | [optional] <br />**Values**: generationResults, headcountForecast |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service.  For testing/app development purposes | [optional]  |
{: class="table table-striped"}

### Return type

[**WeekScheduleResponse**](WeekScheduleResponse.html)

<a name="get_workforcemanagement_managementunit_week_schedule_generationresults"></a>

## [**WeekScheduleGenerationResult**](WeekScheduleGenerationResult.html) get_workforcemanagement_managementunit_week_schedule_generationresults(management_unit_id, week_id, schedule_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get week schedule generation results



Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekId}/schedules/{scheduleId}/generationresults 

Requires ANY permissions: 

* wfm:publishedSchedule:view
* wfm:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format.
schedule_id = 'schedule_id_example' # str | The ID of the schedule to fetch generation results

try:
    # Get week schedule generation results
    api_response = api_instance.get_workforcemanagement_managementunit_week_schedule_generationresults(management_unit_id, week_id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_week_schedule_generationresults: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format. |  |
| **schedule_id** | **str**| The ID of the schedule to fetch generation results |  |
{: class="table table-striped"}

### Return type

[**WeekScheduleGenerationResult**](WeekScheduleGenerationResult.html)

<a name="get_workforcemanagement_managementunit_week_schedules"></a>

## [**WeekScheduleListResponse**](WeekScheduleListResponse.html) get_workforcemanagement_managementunit_week_schedules(management_unit_id, week_id, include_only_published=include_only_published, earliest_week_date=earliest_week_date, latest_week_date=latest_week_date)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get the list of schedules in a week in management unit



Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekId}/schedules 

Requires ANY permissions: 

* wfm:publishedSchedule:view
* wfm:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format.
include_only_published = true # bool | Return only published schedules (optional)
earliest_week_date = 'earliest_week_date_example' # str | The start date of the earliest week to query in yyyy-MM-dd format (optional)
latest_week_date = 'latest_week_date_example' # str | The start date of the latest week to query in yyyy-MM-dd format (optional)

try:
    # Get the list of schedules in a week in management unit
    api_response = api_instance.get_workforcemanagement_managementunit_week_schedules(management_unit_id, week_id, include_only_published=include_only_published, earliest_week_date=earliest_week_date, latest_week_date=latest_week_date)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_week_schedules: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format. |  |
| **include_only_published** | **bool**| Return only published schedules | [optional]  |
| **earliest_week_date** | **str**| The start date of the earliest week to query in yyyy-MM-dd format | [optional]  |
| **latest_week_date** | **str**| The start date of the latest week to query in yyyy-MM-dd format | [optional]  |
{: class="table table-striped"}

### Return type

[**WeekScheduleListResponse**](WeekScheduleListResponse.html)

<a name="get_workforcemanagement_managementunit_week_shorttermforecast_final"></a>

## [**ForecastResultResponse**](ForecastResultResponse.html) get_workforcemanagement_managementunit_week_shorttermforecast_final(management_unit_id, week_date_id, forecast_id, force_download_service=force_download_service)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get the final result of a short term forecast calculation with modifications applied



Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}/final 

Requires ANY permissions: 

* wfm:shortTermForecast:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The management unit ID of the management unit to which the forecast belongs
week_date_id = 'week_date_id_example' # str | The week start date of the forecast in yyyy-MM-dd format
forecast_id = 'forecast_id_example' # str | The ID of the forecast
force_download_service = true # bool | Force the result of this operation to be sent via download service.  For testing/app development purposes (optional)

try:
    # Get the final result of a short term forecast calculation with modifications applied
    api_response = api_instance.get_workforcemanagement_managementunit_week_shorttermforecast_final(management_unit_id, week_date_id, forecast_id, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_week_shorttermforecast_final: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The management unit ID of the management unit to which the forecast belongs |  |
| **week_date_id** | **str**| The week start date of the forecast in yyyy-MM-dd format |  |
| **forecast_id** | **str**| The ID of the forecast |  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service.  For testing/app development purposes | [optional]  |
{: class="table table-striped"}

### Return type

[**ForecastResultResponse**](ForecastResultResponse.html)

<a name="get_workforcemanagement_managementunit_week_shorttermforecasts"></a>

## [**ShortTermForecastListResponse**](ShortTermForecastListResponse.html) get_workforcemanagement_managementunit_week_shorttermforecasts(management_unit_id, week_date_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get short term forecasts

Use \"recent\" for the `weekDateId` path parameter to fetch all forecasts for +/- 26 weeks from the current date

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shorttermforecasts 

Requires ANY permissions: 

* wfm:schedule:generate
* wfm:shortTermForecast:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The management unit ID of the management unit to which the forecast belongs
week_date_id = 'week_date_id_example' # str | The week start date of the forecast in yyyy-MM-dd format

try:
    # Get short term forecasts
    api_response = api_instance.get_workforcemanagement_managementunit_week_shorttermforecasts(management_unit_id, week_date_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_week_shorttermforecasts: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The management unit ID of the management unit to which the forecast belongs |  |
| **week_date_id** | **str**| The week start date of the forecast in yyyy-MM-dd format |  |
{: class="table table-striped"}

### Return type

[**ShortTermForecastListResponse**](ShortTermForecastListResponse.html)

<a name="get_workforcemanagement_managementunit_workplan"></a>

## [**WorkPlan**](WorkPlan.html) get_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id)



Get a work plan



Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans/{workPlanId} 

Requires ANY permissions: 

* wfm:workPlan:view
* wfm:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
work_plan_id = 'work_plan_id_example' # str | The ID of the work plan to fetch

try:
    # Get a work plan
    api_response = api_instance.get_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_workplan: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **work_plan_id** | **str**| The ID of the work plan to fetch |  |
{: class="table table-striped"}

### Return type

[**WorkPlan**](WorkPlan.html)

<a name="get_workforcemanagement_managementunit_workplans"></a>

## [**WorkPlanListResponse**](WorkPlanListResponse.html) get_workforcemanagement_managementunit_workplans(management_unit_id, expand=expand)



Get work plans



Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans 

Requires ANY permissions: 

* wfm:agent:view
* wfm:publishedSchedule:view
* wfm:schedule:view
* wfm:workPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
expand = ['expand_example'] # list[str] |  (optional)

try:
    # Get work plans
    api_response = api_instance.get_workforcemanagement_managementunit_workplans(management_unit_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_workplans: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **expand** | [**list[str]**](str.html)|  | [optional] <br />**Values**: agentCount, details |
{: class="table table-striped"}

### Return type

[**WorkPlanListResponse**](WorkPlanListResponse.html)

<a name="get_workforcemanagement_managementunits"></a>

## [**ManagementUnitListing**](ManagementUnitListing.html) get_workforcemanagement_managementunits(page_size=page_size, page_number=page_number, expand=expand, feature=feature, division_id=division_id)



Get management units



Wraps GET /api/v2/workforcemanagement/managementunits 

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
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
page_size = 56 # int |  (optional)
page_number = 56 # int |  (optional)
expand = 'expand_example' # str |  (optional)
feature = 'feature_example' # str |  (optional)
division_id = 'division_id_example' # str |  (optional)

try:
    # Get management units
    api_response = api_instance.get_workforcemanagement_managementunits(page_size=page_size, page_number=page_number, expand=expand, feature=feature, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunits: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**|  | [optional]  |
| **page_number** | **int**|  | [optional]  |
| **expand** | **str**|  | [optional] <br />**Values**: details |
| **feature** | **str**|  | [optional] <br />**Values**: AgentSchedule, AgentTimeOffRequest, ActivityCodes, Agents, BusinessUnitActivityCodes, BusinessUnits, HistoricalAdherence, IntradayMonitoring, BuIntradayMonitoring, ManagementUnits, RealTimeAdherence, Schedules, BuSchedules, ServiceGoalGroups, ServiceGoalTemplates, PlanningGroups, ShiftTrading, ShortTermForecasts, BuShortTermForecasts, TimeOffRequests, WorkPlans |
| **division_id** | **str**|  | [optional]  |
{: class="table table-striped"}

### Return type

[**ManagementUnitListing**](ManagementUnitListing.html)

<a name="get_workforcemanagement_managementunits_divisionviews"></a>

## [**ManagementUnitListing**](ManagementUnitListing.html) get_workforcemanagement_managementunits_divisionviews(division_id=division_id)



Get management units across divisions



Wraps GET /api/v2/workforcemanagement/managementunits/divisionviews 

Requires ANY permissions: 

* wfm:managementUnit:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
division_id = ['division_id_example'] # list[str] | The divisionIds to filter by. If omitted, will return all divisions (optional)

try:
    # Get management units across divisions
    api_response = api_instance.get_workforcemanagement_managementunits_divisionviews(division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunits_divisionviews: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | [**list[str]**](str.html)| The divisionIds to filter by. If omitted, will return all divisions | [optional]  |
{: class="table table-striped"}

### Return type

[**ManagementUnitListing**](ManagementUnitListing.html)

<a name="get_workforcemanagement_notifications"></a>

## [**NotificationsResponse**](NotificationsResponse.html) get_workforcemanagement_notifications()



Get a list of notifications for the current user



Wraps GET /api/v2/workforcemanagement/notifications 

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
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Get a list of notifications for the current user
    api_response = api_instance.get_workforcemanagement_notifications()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_notifications: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**NotificationsResponse**](NotificationsResponse.html)

<a name="get_workforcemanagement_schedulingjob"></a>

## [**SchedulingStatusResponse**](SchedulingStatusResponse.html) get_workforcemanagement_schedulingjob(job_id)



Get status of the scheduling job



Wraps GET /api/v2/workforcemanagement/schedulingjobs/{jobId} 

Requires ANY permissions: 

* wfm:schedulingrequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | The id of the scheduling job

try:
    # Get status of the scheduling job
    api_response = api_instance.get_workforcemanagement_schedulingjob(job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_schedulingjob: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The id of the scheduling job |  |
{: class="table table-striped"}

### Return type

[**SchedulingStatusResponse**](SchedulingStatusResponse.html)

<a name="get_workforcemanagement_shifttrades"></a>

## [**ShiftTradeListResponse**](ShiftTradeListResponse.html) get_workforcemanagement_shifttrades()



Gets all of my shift trades



Wraps GET /api/v2/workforcemanagement/shifttrades 

Requires ANY permissions: 

* wfm:shiftTradeRequest:edit
* wfm:shiftTradeRequest:view
* wfm:agentShiftTradeRequest:participate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Gets all of my shift trades
    api_response = api_instance.get_workforcemanagement_shifttrades()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_shifttrades: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**ShiftTradeListResponse**](ShiftTradeListResponse.html)

<a name="get_workforcemanagement_timeoffrequest"></a>

## [**TimeOffRequestResponse**](TimeOffRequestResponse.html) get_workforcemanagement_timeoffrequest(time_off_request_id)



Get a time off request for the current user



Wraps GET /api/v2/workforcemanagement/timeoffrequests/{timeOffRequestId} 

Requires ANY permissions: 

* wfm:agentSchedule:view
* wfm:agentTimeOffRequest:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
time_off_request_id = 'time_off_request_id_example' # str | Time Off Request Id

try:
    # Get a time off request for the current user
    api_response = api_instance.get_workforcemanagement_timeoffrequest(time_off_request_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_timeoffrequest: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **time_off_request_id** | **str**| Time Off Request Id |  |
{: class="table table-striped"}

### Return type

[**TimeOffRequestResponse**](TimeOffRequestResponse.html)

<a name="get_workforcemanagement_timeoffrequests"></a>

## [**TimeOffRequestList**](TimeOffRequestList.html) get_workforcemanagement_timeoffrequests(recently_reviewed=recently_reviewed)



Get a list of time off requests for the current user



Wraps GET /api/v2/workforcemanagement/timeoffrequests 

Requires ANY permissions: 

* wfm:agentSchedule:view
* wfm:agentTimeOffRequest:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
recently_reviewed = false # bool | Limit results to requests that have been reviewed within the preceding 30 days (optional) (default to false)

try:
    # Get a list of time off requests for the current user
    api_response = api_instance.get_workforcemanagement_timeoffrequests(recently_reviewed=recently_reviewed)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->get_workforcemanagement_timeoffrequests: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recently_reviewed** | **bool**| Limit results to requests that have been reviewed within the preceding 30 days | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**TimeOffRequestList**](TimeOffRequestList.html)

<a name="patch_workforcemanagement_managementunit"></a>

## [**ManagementUnit**](ManagementUnit.html) patch_workforcemanagement_managementunit(mu_id, body=body)



Update the requested management unit



Wraps PATCH /api/v2/workforcemanagement/managementunits/{muId} 

Requires ANY permissions: 

* wfm:managementUnit:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.UpdateManagementUnitRequest() # UpdateManagementUnitRequest | body (optional)

try:
    # Update the requested management unit
    api_response = api_instance.patch_workforcemanagement_managementunit(mu_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**UpdateManagementUnitRequest**](UpdateManagementUnitRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**ManagementUnit**](ManagementUnit.html)

<a name="patch_workforcemanagement_managementunit_activitycode"></a>

## [**ActivityCode**](ActivityCode.html) patch_workforcemanagement_managementunit_activitycode(mu_id, ac_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update an activity code



Wraps PATCH /api/v2/workforcemanagement/managementunits/{muId}/activitycodes/{acId} 

Requires ANY permissions: 

* wfm:activityCode:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
ac_id = 'ac_id_example' # str | The ID of the activity code to update
body = PureCloudPlatformClientV2.UpdateActivityCodeRequest() # UpdateActivityCodeRequest | body (optional)

try:
    # Update an activity code
    api_response = api_instance.patch_workforcemanagement_managementunit_activitycode(mu_id, ac_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_activitycode: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **ac_id** | **str**| The ID of the activity code to update |  |
| **body** | [**UpdateActivityCodeRequest**](UpdateActivityCodeRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**ActivityCode**](ActivityCode.html)

<a name="patch_workforcemanagement_managementunit_scheduling_run"></a>

## [**RescheduleResult**](RescheduleResult.html) patch_workforcemanagement_managementunit_scheduling_run(management_unit_id, run_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Marks a specific scheduling run as applied, allowing a new rescheduling run to be started



Wraps PATCH /api/v2/workforcemanagement/managementunits/{managementUnitId}/scheduling/runs/{runId} 

Requires ANY permissions: 

* wfm:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
run_id = 'run_id_example' # str | The ID of the schedule run
body = PureCloudPlatformClientV2.UpdateSchedulingRunRequest() # UpdateSchedulingRunRequest | body (optional)

try:
    # Marks a specific scheduling run as applied, allowing a new rescheduling run to be started
    api_response = api_instance.patch_workforcemanagement_managementunit_scheduling_run(management_unit_id, run_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_scheduling_run: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **run_id** | **str**| The ID of the schedule run |  |
| **body** | [**UpdateSchedulingRunRequest**](UpdateSchedulingRunRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**RescheduleResult**](RescheduleResult.html)

<a name="patch_workforcemanagement_managementunit_servicegoalgroup"></a>

## [**ServiceGoalGroup**](ServiceGoalGroup.html) patch_workforcemanagement_managementunit_servicegoalgroup(management_unit_id, service_goal_group_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update a service goal group



Wraps PATCH /api/v2/workforcemanagement/managementunits/{managementUnitId}/servicegoalgroups/{serviceGoalGroupId} 

Requires ANY permissions: 

* wfm:serviceGoalGroup:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
service_goal_group_id = 'service_goal_group_id_example' # str | The ID of the service goal group to update
body = PureCloudPlatformClientV2.ServiceGoalGroup() # ServiceGoalGroup | body (optional)

try:
    # Update a service goal group
    api_response = api_instance.patch_workforcemanagement_managementunit_servicegoalgroup(management_unit_id, service_goal_group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_servicegoalgroup: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **service_goal_group_id** | **str**| The ID of the service goal group to update |  |
| **body** | [**ServiceGoalGroup**](ServiceGoalGroup.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**ServiceGoalGroup**](ServiceGoalGroup.html)

<a name="patch_workforcemanagement_managementunit_settings"></a>

## [**ManagementUnitSettingsResponse**](ManagementUnitSettingsResponse.html) patch_workforcemanagement_managementunit_settings(mu_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update the settings for the requested management unit



Wraps PATCH /api/v2/workforcemanagement/managementunits/{muId}/settings 

Requires ANY permissions: 

* wfm:managementUnit:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.ManagementUnitSettingsRequest() # ManagementUnitSettingsRequest | config (optional)

try:
    # Update the settings for the requested management unit
    api_response = api_instance.patch_workforcemanagement_managementunit_settings(mu_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_settings: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**ManagementUnitSettingsRequest**](ManagementUnitSettingsRequest.html)| config | [optional]  |
{: class="table table-striped"}

### Return type

[**ManagementUnitSettingsResponse**](ManagementUnitSettingsResponse.html)

<a name="patch_workforcemanagement_managementunit_user_timeoffrequest"></a>

## [**TimeOffRequestResponse**](TimeOffRequestResponse.html) patch_workforcemanagement_managementunit_user_timeoffrequest(mu_id, user_id, time_off_request_id, body=body)



Update a time off request



Wraps PATCH /api/v2/workforcemanagement/managementunits/{muId}/users/{userId}/timeoffrequests/{timeOffRequestId} 

Requires ANY permissions: 

* wfm:timeOffRequest:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
```

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

<a name="patch_workforcemanagement_managementunit_week_schedule"></a>

## [**AsyncWeekScheduleResponse**](AsyncWeekScheduleResponse.html) patch_workforcemanagement_managementunit_week_schedule(management_unit_id, week_id, schedule_id, force_async=force_async, force_download_service=force_download_service, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update a week schedule



Wraps PATCH /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekId}/schedules/{scheduleId} 

Requires ANY permissions: 

* wfm:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format.
schedule_id = 'schedule_id_example' # str | The ID of the schedule to update. Use partial uploads of user schedules if activity count in schedule is greater than 17500
force_async = true # bool | Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes (optional)
force_download_service = true # bool | Force the result of this operation to be sent via download service.  For testing/app development purposes (optional)
body = PureCloudPlatformClientV2.UpdateWeekScheduleRequest() # UpdateWeekScheduleRequest | body (optional)

try:
    # Update a week schedule
    api_response = api_instance.patch_workforcemanagement_managementunit_week_schedule(management_unit_id, week_id, schedule_id, force_async=force_async, force_download_service=force_download_service, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_week_schedule: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format. |  |
| **schedule_id** | **str**| The ID of the schedule to update. Use partial uploads of user schedules if activity count in schedule is greater than 17500 |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes | [optional]  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service.  For testing/app development purposes | [optional]  |
| **body** | [**UpdateWeekScheduleRequest**](UpdateWeekScheduleRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**AsyncWeekScheduleResponse**](AsyncWeekScheduleResponse.html)

<a name="patch_workforcemanagement_managementunit_workplan"></a>

## [**WorkPlan**](WorkPlan.html) patch_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id, body=body)



Update a work plan



Wraps PATCH /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans/{workPlanId} 

Requires ANY permissions: 

* wfm:workPlan:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
work_plan_id = 'work_plan_id_example' # str | The ID of the work plan to update
body = PureCloudPlatformClientV2.WorkPlan() # WorkPlan | body (optional)

try:
    # Update a work plan
    api_response = api_instance.patch_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_workplan: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **work_plan_id** | **str**| The ID of the work plan to update |  |
| **body** | [**WorkPlan**](WorkPlan.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**WorkPlan**](WorkPlan.html)

<a name="patch_workforcemanagement_timeoffrequest"></a>

## [**TimeOffRequestResponse**](TimeOffRequestResponse.html) patch_workforcemanagement_timeoffrequest(time_off_request_id, body=body)



Update a time off request for the current user



Wraps PATCH /api/v2/workforcemanagement/timeoffrequests/{timeOffRequestId} 

Requires ANY permissions: 

* wfm:agentTimeOffRequest:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
time_off_request_id = 'time_off_request_id_example' # str | Time Off Request Id
body = PureCloudPlatformClientV2.AgentTimeOffRequestPatch() # AgentTimeOffRequestPatch | body (optional)

try:
    # Update a time off request for the current user
    api_response = api_instance.patch_workforcemanagement_timeoffrequest(time_off_request_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->patch_workforcemanagement_timeoffrequest: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **time_off_request_id** | **str**| Time Off Request Id |  |
| **body** | [**AgentTimeOffRequestPatch**](AgentTimeOffRequestPatch.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**TimeOffRequestResponse**](TimeOffRequestResponse.html)

<a name="post_workforcemanagement_adherence_historical"></a>

## [**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse.html) post_workforcemanagement_adherence_historical(body=body)



Request a historical adherence report for users across management units



Wraps POST /api/v2/workforcemanagement/adherence/historical 

Requires ANY permissions: 

* wfm:historicalAdherence:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.WfmHistoricalAdherenceQueryForUsers() # WfmHistoricalAdherenceQueryForUsers | body (optional)

try:
    # Request a historical adherence report for users across management units
    api_response = api_instance.post_workforcemanagement_adherence_historical(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_adherence_historical: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WfmHistoricalAdherenceQueryForUsers**](WfmHistoricalAdherenceQueryForUsers.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse.html)

<a name="post_workforcemanagement_managementunit_activitycodes"></a>

## [**ActivityCode**](ActivityCode.html) post_workforcemanagement_managementunit_activitycodes(mu_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Create a new activity code



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/activitycodes 

Requires ANY permissions: 

* wfm:activityCode:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**CreateActivityCodeRequest**](CreateActivityCodeRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**ActivityCode**](ActivityCode.html)

<a name="post_workforcemanagement_managementunit_agentschedules_search"></a>

## [**BuAsyncAgentSchedulesSearchResponse**](BuAsyncAgentSchedulesSearchResponse.html) post_workforcemanagement_managementunit_agentschedules_search(mu_id, body=body, force_async=force_async, force_download_service=force_download_service)



Query published schedules for given given time range for set of users



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/agentschedules/search 

Requires ANY permissions: 

* wfm:publishedSchedule:view
* wfm:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The management unit ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.BuSearchAgentSchedulesRequest() # BuSearchAgentSchedulesRequest | body (optional)
force_async = true # bool | Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes (optional)
force_download_service = true # bool | Force the result of this operation to be sent via download service.  For testing/app development purposes (optional)

try:
    # Query published schedules for given given time range for set of users
    api_response = api_instance.post_workforcemanagement_managementunit_agentschedules_search(mu_id, body=body, force_async=force_async, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_agentschedules_search: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The management unit ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**BuSearchAgentSchedulesRequest**](BuSearchAgentSchedulesRequest.html)| body | [optional]  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes | [optional]  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service.  For testing/app development purposes | [optional]  |
{: class="table table-striped"}

### Return type

[**BuAsyncAgentSchedulesSearchResponse**](BuAsyncAgentSchedulesSearchResponse.html)

<a name="post_workforcemanagement_managementunit_historicaladherencequery"></a>

## [**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse.html) post_workforcemanagement_managementunit_historicaladherencequery(mu_id, body=body)



Request a historical adherence report

The maximum supported range for historical adherence queries is 31 days, or 7 days with includeExceptions = true

Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/historicaladherencequery 

Requires ANY permissions: 

* wfm:historicalAdherence:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The management unit ID of the management unit
body = PureCloudPlatformClientV2.WfmHistoricalAdherenceQuery() # WfmHistoricalAdherenceQuery | body (optional)

try:
    # Request a historical adherence report
    api_response = api_instance.post_workforcemanagement_managementunit_historicaladherencequery(mu_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_historicaladherencequery: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The management unit ID of the management unit |  |
| **body** | [**WfmHistoricalAdherenceQuery**](WfmHistoricalAdherenceQuery.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse.html)

<a name="post_workforcemanagement_managementunit_intraday"></a>

## [**IntradayResponse**](IntradayResponse.html) post_workforcemanagement_managementunit_intraday(mu_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get intraday data for the given date for the requested queueIds



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/intraday 

Requires ANY permissions: 

* wfm:intraday:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The management unit ID of the management unit
body = PureCloudPlatformClientV2.IntradayQueryDataCommand() # IntradayQueryDataCommand | body (optional)

try:
    # Get intraday data for the given date for the requested queueIds
    api_response = api_instance.post_workforcemanagement_managementunit_intraday(mu_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_intraday: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The management unit ID of the management unit |  |
| **body** | [**IntradayQueryDataCommand**](IntradayQueryDataCommand.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**IntradayResponse**](IntradayResponse.html)

<a name="post_workforcemanagement_managementunit_move"></a>

## [**MoveManagementUnitResponse**](MoveManagementUnitResponse.html) post_workforcemanagement_managementunit_move(mu_id, body=body)



Move the requested management unit to a new business unit

Returns status 200 if the management unit is already in the requested business unit

Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/move 

Requires ANY permissions: 

* wfm:managementUnit:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.MoveManagementUnitRequest() # MoveManagementUnitRequest | body (optional)

try:
    # Move the requested management unit to a new business unit
    api_response = api_instance.post_workforcemanagement_managementunit_move(mu_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_move: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**MoveManagementUnitRequest**](MoveManagementUnitRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**MoveManagementUnitResponse**](MoveManagementUnitResponse.html)

<a name="post_workforcemanagement_managementunit_schedules_search"></a>

## [**UserScheduleContainer**](UserScheduleContainer.html) post_workforcemanagement_managementunit_schedules_search(mu_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Query published schedules for given given time range for set of users



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/schedules/search 

Requires ANY permissions: 

* wfm:publishedSchedule:view
* wfm:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The management unit ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**UserListScheduleRequestBody**](UserListScheduleRequestBody.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**UserScheduleContainer**](UserScheduleContainer.html)

<a name="post_workforcemanagement_managementunit_servicegoalgroups"></a>

## [**ServiceGoalGroup**](ServiceGoalGroup.html) post_workforcemanagement_managementunit_servicegoalgroups(management_unit_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Create a new service goal group



Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/servicegoalgroups 

Requires ANY permissions: 

* wfm:serviceGoalGroup:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.CreateServiceGoalGroupRequest() # CreateServiceGoalGroupRequest | body (optional)

try:
    # Create a new service goal group
    api_response = api_instance.post_workforcemanagement_managementunit_servicegoalgroups(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_servicegoalgroups: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**CreateServiceGoalGroupRequest**](CreateServiceGoalGroupRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**ServiceGoalGroup**](ServiceGoalGroup.html)

<a name="post_workforcemanagement_managementunit_timeoffrequests"></a>

## [**TimeOffRequestList**](TimeOffRequestList.html) post_workforcemanagement_managementunit_timeoffrequests(mu_id, body=body)



Create a new time off request



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/timeoffrequests 

Requires ANY permissions: 

* wfm:timeOffRequest:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The muId of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.CreateAdminTimeOffRequest() # CreateAdminTimeOffRequest | body (optional)

try:
    # Create a new time off request
    api_response = api_instance.post_workforcemanagement_managementunit_timeoffrequests(mu_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_timeoffrequests: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The muId of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**CreateAdminTimeOffRequest**](CreateAdminTimeOffRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**TimeOffRequestList**](TimeOffRequestList.html)

<a name="post_workforcemanagement_managementunit_timeoffrequests_fetchdetails"></a>

## [**TimeOffRequestEntityList**](TimeOffRequestEntityList.html) post_workforcemanagement_managementunit_timeoffrequests_fetchdetails(mu_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Gets a list of time off requests from lookup ids



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/timeoffrequests/fetchdetails 

Requires ANY permissions: 

* wfm:timeOffRequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The muId of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.TimeOffRequestLookupList() # TimeOffRequestLookupList | body (optional)

try:
    # Gets a list of time off requests from lookup ids
    api_response = api_instance.post_workforcemanagement_managementunit_timeoffrequests_fetchdetails(mu_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_timeoffrequests_fetchdetails: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The muId of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**TimeOffRequestLookupList**](TimeOffRequestLookupList.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**TimeOffRequestEntityList**](TimeOffRequestEntityList.html)

<a name="post_workforcemanagement_managementunit_timeoffrequests_query"></a>

## [**TimeOffRequestLookupList**](TimeOffRequestLookupList.html) post_workforcemanagement_managementunit_timeoffrequests_query(mu_id, body=body)



Gets the lookup ids to fetch the specified set of requests



Wraps POST /api/v2/workforcemanagement/managementunits/{muId}/timeoffrequests/query 

Requires ANY permissions: 

* wfm:timeOffRequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
mu_id = 'mu_id_example' # str | The muId of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.TimeOffRequestQueryBody() # TimeOffRequestQueryBody | body (optional)

try:
    # Gets the lookup ids to fetch the specified set of requests
    api_response = api_instance.post_workforcemanagement_managementunit_timeoffrequests_query(mu_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_timeoffrequests_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mu_id** | **str**| The muId of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**TimeOffRequestQueryBody**](TimeOffRequestQueryBody.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**TimeOffRequestLookupList**](TimeOffRequestLookupList.html)

<a name="post_workforcemanagement_managementunit_week_schedule_copy"></a>

## [**AsyncWeekScheduleResponse**](AsyncWeekScheduleResponse.html) post_workforcemanagement_managementunit_week_schedule_copy(management_unit_id, week_id, schedule_id, force_async=force_async, force_download_service=force_download_service, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Copy a week schedule



Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekId}/schedules/{scheduleId}/copy 

Requires ANY permissions: 

* wfm:schedule:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format.
schedule_id = 'schedule_id_example' # str | The ID of the schedule to copy from
force_async = true # bool | Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes (optional)
force_download_service = true # bool | Force the result of this operation to be sent via download service.  For testing/app development purposes (optional)
body = PureCloudPlatformClientV2.CopyWeekScheduleRequest() # CopyWeekScheduleRequest | body (optional)

try:
    # Copy a week schedule
    api_response = api_instance.post_workforcemanagement_managementunit_week_schedule_copy(management_unit_id, week_id, schedule_id, force_async=force_async, force_download_service=force_download_service, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_week_schedule_copy: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format. |  |
| **schedule_id** | **str**| The ID of the schedule to copy from |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes | [optional]  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service.  For testing/app development purposes | [optional]  |
| **body** | [**CopyWeekScheduleRequest**](CopyWeekScheduleRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**AsyncWeekScheduleResponse**](AsyncWeekScheduleResponse.html)

<a name="post_workforcemanagement_managementunit_week_schedule_reschedule"></a>

## [**AsyncWeekScheduleResponse**](AsyncWeekScheduleResponse.html) post_workforcemanagement_managementunit_week_schedule_reschedule(management_unit_id, week_id, schedule_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Start a scheduling run to compute the reschedule. When the scheduling run finishes, a client can get the reschedule changes and then the client can apply them to the schedule, save the schedule, and mark the scheduling run as applied



Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekId}/schedules/{scheduleId}/reschedule 

Requires ANY permissions: 

* wfm:schedule:generate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format.
schedule_id = 'schedule_id_example' # str | The ID of the schedule to re-optimize
body = PureCloudPlatformClientV2.RescheduleRequest() # RescheduleRequest | body (optional)

try:
    # Start a scheduling run to compute the reschedule. When the scheduling run finishes, a client can get the reschedule changes and then the client can apply them to the schedule, save the schedule, and mark the scheduling run as applied
    api_response = api_instance.post_workforcemanagement_managementunit_week_schedule_reschedule(management_unit_id, week_id, schedule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_week_schedule_reschedule: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format. |  |
| **schedule_id** | **str**| The ID of the schedule to re-optimize |  |
| **body** | [**RescheduleRequest**](RescheduleRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**AsyncWeekScheduleResponse**](AsyncWeekScheduleResponse.html)

<a name="post_workforcemanagement_managementunit_week_schedules"></a>

## [**AsyncWeekScheduleResponse**](AsyncWeekScheduleResponse.html) post_workforcemanagement_managementunit_week_schedules(management_unit_id, week_id, force_async=force_async, force_download_service=force_download_service, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Add a schedule for a week in management unit using imported data. Use partial uploads of user schedules if activity count in schedule is greater than 17500



Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekId}/schedules 

Requires ANY permissions: 

* wfm:schedule:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format.
force_async = true # bool | Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes (optional)
force_download_service = true # bool | Force the result of this operation to be sent via download service.  For testing/app development purposes (optional)
body = PureCloudPlatformClientV2.ImportWeekScheduleRequest() # ImportWeekScheduleRequest | body (optional)

try:
    # Add a schedule for a week in management unit using imported data. Use partial uploads of user schedules if activity count in schedule is greater than 17500
    api_response = api_instance.post_workforcemanagement_managementunit_week_schedules(management_unit_id, week_id, force_async=force_async, force_download_service=force_download_service, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_week_schedules: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format. |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes | [optional]  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service.  For testing/app development purposes | [optional]  |
| **body** | [**ImportWeekScheduleRequest**](ImportWeekScheduleRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**AsyncWeekScheduleResponse**](AsyncWeekScheduleResponse.html)

<a name="post_workforcemanagement_managementunit_week_schedules_generate"></a>

## [**GenerateWeekScheduleResponse**](GenerateWeekScheduleResponse.html) post_workforcemanagement_managementunit_week_schedules_generate(management_unit_id, week_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Generate a week schedule



Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekId}/schedules/generate 

Requires ANY permissions: 

* wfm:schedule:generate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format.
body = PureCloudPlatformClientV2.GenerateWeekScheduleRequest() # GenerateWeekScheduleRequest | body (optional)

try:
    # Generate a week schedule
    api_response = api_instance.post_workforcemanagement_managementunit_week_schedules_generate(management_unit_id, week_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_week_schedules_generate: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format. |  |
| **body** | [**GenerateWeekScheduleRequest**](GenerateWeekScheduleRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**GenerateWeekScheduleResponse**](GenerateWeekScheduleResponse.html)

<a name="post_workforcemanagement_managementunit_week_schedules_partialupload"></a>

## [**PartialUploadResponse**](PartialUploadResponse.html) post_workforcemanagement_managementunit_week_schedules_partialupload(management_unit_id, week_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Partial upload of user schedules where activity count is greater than 17500



Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekId}/schedules/partialupload 

Requires ANY permissions: 

* wfm:schedule:add
* wfm:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format.
body = PureCloudPlatformClientV2.UserSchedulesPartialUploadRequest() # UserSchedulesPartialUploadRequest | body (optional)

try:
    # Partial upload of user schedules where activity count is greater than 17500
    api_response = api_instance.post_workforcemanagement_managementunit_week_schedules_partialupload(management_unit_id, week_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_week_schedules_partialupload: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format. |  |
| **body** | [**UserSchedulesPartialUploadRequest**](UserSchedulesPartialUploadRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**PartialUploadResponse**](PartialUploadResponse.html)

<a name="post_workforcemanagement_managementunit_week_shorttermforecast_copy"></a>

## [**ShortTermForecastResponse**](ShortTermForecastResponse.html) post_workforcemanagement_managementunit_week_shorttermforecast_copy(management_unit_id, week_date_id, forecast_id, body, force_async=force_async)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Copy a short term forecast



Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}/copy 

Requires ANY permissions: 

* wfm:shortTermForecast:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The management unit ID of the management unit to which the forecast belongs
week_date_id = 'week_date_id_example' # str | The week start date of the forecast in yyyy-MM-dd format
forecast_id = 'forecast_id_example' # str | The ID of the forecast to copy
body = PureCloudPlatformClientV2.CopyShortTermForecastRequest() # CopyShortTermForecastRequest | body
force_async = true # bool | Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes (optional)

try:
    # Copy a short term forecast
    api_response = api_instance.post_workforcemanagement_managementunit_week_shorttermforecast_copy(management_unit_id, week_date_id, forecast_id, body, force_async=force_async)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_week_shorttermforecast_copy: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The management unit ID of the management unit to which the forecast belongs |  |
| **week_date_id** | **str**| The week start date of the forecast in yyyy-MM-dd format |  |
| **forecast_id** | **str**| The ID of the forecast to copy |  |
| **body** | [**CopyShortTermForecastRequest**](CopyShortTermForecastRequest.html)| body |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes | [optional]  |
{: class="table table-striped"}

### Return type

[**ShortTermForecastResponse**](ShortTermForecastResponse.html)

<a name="post_workforcemanagement_managementunit_week_shorttermforecasts"></a>

## [**ShortTermForecastResponse**](ShortTermForecastResponse.html) post_workforcemanagement_managementunit_week_shorttermforecasts(management_unit_id, week_date_id, body, force_async=force_async)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Import a short term forecast



Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shorttermforecasts 

Requires ANY permissions: 

* wfm:shortTermForecast:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The management unit ID of the management unit to which the forecast belongs
week_date_id = 'week_date_id_example' # str | The week start date of the forecast in yyyy-MM-dd format
body = PureCloudPlatformClientV2.ImportShortTermForecastRequest() # ImportShortTermForecastRequest | body
force_async = true # bool | Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes (optional)

try:
    # Import a short term forecast
    api_response = api_instance.post_workforcemanagement_managementunit_week_shorttermforecasts(management_unit_id, week_date_id, body, force_async=force_async)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_week_shorttermforecasts: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The management unit ID of the management unit to which the forecast belongs |  |
| **week_date_id** | **str**| The week start date of the forecast in yyyy-MM-dd format |  |
| **body** | [**ImportShortTermForecastRequest**](ImportShortTermForecastRequest.html)| body |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes | [optional]  |
{: class="table table-striped"}

### Return type

[**ShortTermForecastResponse**](ShortTermForecastResponse.html)

<a name="post_workforcemanagement_managementunit_week_shorttermforecasts_generate"></a>

## [**GenerateShortTermForecastResponse**](GenerateShortTermForecastResponse.html) post_workforcemanagement_managementunit_week_shorttermforecasts_generate(management_unit_id, week_date_id, body, force_async=force_async)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Generate a short term forecast



Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shorttermforecasts/generate 

Requires ANY permissions: 

* wfm:shortTermForecast:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The management unit ID of the management unit to which the forecast belongs
week_date_id = 'week_date_id_example' # str | The week start date of the forecast in yyyy-MM-dd format
body = PureCloudPlatformClientV2.GenerateShortTermForecastRequest() # GenerateShortTermForecastRequest | 
force_async = true # bool | Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes (optional)

try:
    # Generate a short term forecast
    api_response = api_instance.post_workforcemanagement_managementunit_week_shorttermforecasts_generate(management_unit_id, week_date_id, body, force_async=force_async)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_week_shorttermforecasts_generate: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The management unit ID of the management unit to which the forecast belongs |  |
| **week_date_id** | **str**| The week start date of the forecast in yyyy-MM-dd format |  |
| **body** | [**GenerateShortTermForecastRequest**](GenerateShortTermForecastRequest.html)|  |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes | [optional]  |
{: class="table table-striped"}

### Return type

[**GenerateShortTermForecastResponse**](GenerateShortTermForecastResponse.html)

<a name="post_workforcemanagement_managementunit_week_shorttermforecasts_partialupload"></a>

## [**PartialUploadResponse**](PartialUploadResponse.html) post_workforcemanagement_managementunit_week_shorttermforecasts_partialupload(management_unit_id, week_date_id, body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Import a short term forecast



Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shorttermforecasts/partialupload 

Requires ANY permissions: 

* wfm:shortTermForecast:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The management unit ID of the management unit to which the forecast belongs
week_date_id = 'week_date_id_example' # str | The week start date of the forecast in yyyy-MM-dd format
body = PureCloudPlatformClientV2.RouteGroupList() # RouteGroupList | body

try:
    # Import a short term forecast
    api_response = api_instance.post_workforcemanagement_managementunit_week_shorttermforecasts_partialupload(management_unit_id, week_date_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_week_shorttermforecasts_partialupload: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The management unit ID of the management unit to which the forecast belongs |  |
| **week_date_id** | **str**| The week start date of the forecast in yyyy-MM-dd format |  |
| **body** | [**RouteGroupList**](RouteGroupList.html)| body |  |
{: class="table table-striped"}

### Return type

[**PartialUploadResponse**](PartialUploadResponse.html)

<a name="post_workforcemanagement_managementunit_workplan_copy"></a>

## [**WorkPlan**](WorkPlan.html) post_workforcemanagement_managementunit_workplan_copy(management_unit_id, work_plan_id, body=body)



Create a copy of work plan



Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans/{workPlanId}/copy 

Requires ANY permissions: 

* wfm:workPlan:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
work_plan_id = 'work_plan_id_example' # str | The ID of the work plan to create a copy
body = PureCloudPlatformClientV2.CopyWorkPlan() # CopyWorkPlan | body (optional)

try:
    # Create a copy of work plan
    api_response = api_instance.post_workforcemanagement_managementunit_workplan_copy(management_unit_id, work_plan_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_workplan_copy: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **work_plan_id** | **str**| The ID of the work plan to create a copy |  |
| **body** | [**CopyWorkPlan**](CopyWorkPlan.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**WorkPlan**](WorkPlan.html)

<a name="post_workforcemanagement_managementunit_workplans"></a>

## [**WorkPlan**](WorkPlan.html) post_workforcemanagement_managementunit_workplans(management_unit_id, body=body)



Create a new work plan



Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans 

Requires ANY permissions: 

* wfm:workPlan:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.CreateWorkPlan() # CreateWorkPlan | body (optional)

try:
    # Create a new work plan
    api_response = api_instance.post_workforcemanagement_managementunit_workplans(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_workplans: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**CreateWorkPlan**](CreateWorkPlan.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**WorkPlan**](WorkPlan.html)

<a name="post_workforcemanagement_managementunits"></a>

## [**ManagementUnit**](ManagementUnit.html) post_workforcemanagement_managementunits(body=body)



Add a management unit



Wraps POST /api/v2/workforcemanagement/managementunits 

Requires ANY permissions: 

* wfm:managementUnit:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.CreateManagementUnitApiRequest() # CreateManagementUnitApiRequest | body (optional)

try:
    # Add a management unit
    api_response = api_instance.post_workforcemanagement_managementunits(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunits: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateManagementUnitApiRequest**](CreateManagementUnitApiRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**ManagementUnit**](ManagementUnit.html)

<a name="post_workforcemanagement_notifications_update"></a>

## [**UpdateNotificationsResponse**](UpdateNotificationsResponse.html) post_workforcemanagement_notifications_update(body=body)



Mark a list of notifications as read or unread



Wraps POST /api/v2/workforcemanagement/notifications/update 

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
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.UpdateNotificationsRequest() # UpdateNotificationsRequest | body (optional)

try:
    # Mark a list of notifications as read or unread
    api_response = api_instance.post_workforcemanagement_notifications_update(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_notifications_update: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UpdateNotificationsRequest**](UpdateNotificationsRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**UpdateNotificationsResponse**](UpdateNotificationsResponse.html)

<a name="post_workforcemanagement_schedules"></a>

## [**UserScheduleContainer**](UserScheduleContainer.html) post_workforcemanagement_schedules(body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get published schedule for the current user



Wraps POST /api/v2/workforcemanagement/schedules 

Requires ANY permissions: 

* wfm:agentSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.CurrentUserScheduleRequestBody() # CurrentUserScheduleRequestBody | body (optional)

try:
    # Get published schedule for the current user
    api_response = api_instance.post_workforcemanagement_schedules(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_schedules: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CurrentUserScheduleRequestBody**](CurrentUserScheduleRequestBody.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**UserScheduleContainer**](UserScheduleContainer.html)

<a name="post_workforcemanagement_timeoffrequests"></a>

## [**TimeOffRequestResponse**](TimeOffRequestResponse.html) post_workforcemanagement_timeoffrequests(body=body)



Create a time off request for the current user



Wraps POST /api/v2/workforcemanagement/timeoffrequests 

Requires ANY permissions: 

* wfm:agentTimeOffRequest:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.CreateAgentTimeOffRequest() # CreateAgentTimeOffRequest | body (optional)

try:
    # Create a time off request for the current user
    api_response = api_instance.post_workforcemanagement_timeoffrequests(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkforceManagementApi->post_workforcemanagement_timeoffrequests: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateAgentTimeOffRequest**](CreateAgentTimeOffRequest.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**TimeOffRequestResponse**](TimeOffRequestResponse.html)


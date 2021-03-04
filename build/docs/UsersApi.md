---
title: UsersApi
---

## PureCloudPlatformClientV2.UsersApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_analytics_users_details_job**](UsersApi.html#delete_analytics_users_details_job) | Delete/cancel an async request|
|[**delete_authorization_subject_division_role**](UsersApi.html#delete_authorization_subject_division_role) | Delete a grant of a role in a division|
|[**delete_routing_user_utilization**](UsersApi.html#delete_routing_user_utilization) | Delete the user&#39;s max utilization settings and revert to the organization-wide default.|
|[**delete_user**](UsersApi.html#delete_user) | Delete user|
|[**delete_user_routinglanguage**](UsersApi.html#delete_user_routinglanguage) | Remove routing language from user|
|[**delete_user_routingskill**](UsersApi.html#delete_user_routingskill) | Remove routing skill from user|
|[**delete_user_station_associatedstation**](UsersApi.html#delete_user_station_associatedstation) | Clear associated station|
|[**delete_user_station_defaultstation**](UsersApi.html#delete_user_station_defaultstation) | Clear default station|
|[**get_analytics_users_details_job**](UsersApi.html#get_analytics_users_details_job) | Get status for async query for user details|
|[**get_analytics_users_details_job_results**](UsersApi.html#get_analytics_users_details_job_results) | Fetch a page of results for an async query|
|[**get_analytics_users_details_jobs_availability**](UsersApi.html#get_analytics_users_details_jobs_availability) | Lookup the datalake availability date and time|
|[**get_authorization_divisionspermitted_me**](UsersApi.html#get_authorization_divisionspermitted_me) | Returns which divisions the current user has the given permission in.|
|[**get_authorization_divisionspermitted_paged_me**](UsersApi.html#get_authorization_divisionspermitted_paged_me) | Returns which divisions the current user has the given permission in.|
|[**get_authorization_divisionspermitted_paged_subject_id**](UsersApi.html#get_authorization_divisionspermitted_paged_subject_id) | Returns which divisions the specified user has the given permission in.|
|[**get_authorization_subject**](UsersApi.html#get_authorization_subject) | Returns a listing of roles and permissions for a user.|
|[**get_authorization_subjects_me**](UsersApi.html#get_authorization_subjects_me) | Returns a listing of roles and permissions for the currently authenticated user.|
|[**get_fieldconfig**](UsersApi.html#get_fieldconfig) | Fetch field config for an entity type|
|[**get_profiles_users**](UsersApi.html#get_profiles_users) | Get a user profile listing|
|[**get_routing_user_utilization**](UsersApi.html#get_routing_user_utilization) | Get the user&#39;s max utilization settings.  If not configured, the organization-wide default is returned.|
|[**get_user**](UsersApi.html#get_user) | Get user.|
|[**get_user_adjacents**](UsersApi.html#get_user_adjacents) | Get adjacents|
|[**get_user_callforwarding**](UsersApi.html#get_user_callforwarding) | Get a user&#39;s CallForwarding|
|[**get_user_directreports**](UsersApi.html#get_user_directreports) | Get direct reports|
|[**get_user_favorites**](UsersApi.html#get_user_favorites) | Get favorites|
|[**get_user_geolocation**](UsersApi.html#get_user_geolocation) | Get a user&#39;s Geolocation|
|[**get_user_outofoffice**](UsersApi.html#get_user_outofoffice) | Get a OutOfOffice|
|[**get_user_profile**](UsersApi.html#get_user_profile) | Get user profile|
|[**get_user_profileskills**](UsersApi.html#get_user_profileskills) | List profile skills for a user|
|[**get_user_queues**](UsersApi.html#get_user_queues) | Get queues for user|
|[**get_user_roles**](UsersApi.html#get_user_roles) | Returns a listing of roles and permissions for a user.|
|[**get_user_routinglanguages**](UsersApi.html#get_user_routinglanguages) | List routing language for user|
|[**get_user_routingskills**](UsersApi.html#get_user_routingskills) | List routing skills for user|
|[**get_user_routingstatus**](UsersApi.html#get_user_routingstatus) | Fetch the routing status of a user|
|[**get_user_station**](UsersApi.html#get_user_station) | Get station information for user|
|[**get_user_superiors**](UsersApi.html#get_user_superiors) | Get superiors|
|[**get_user_trustors**](UsersApi.html#get_user_trustors) | List the organizations that have authorized/trusted the user.|
|[**get_users**](UsersApi.html#get_users) | Get the list of available users.|
|[**get_users_development_activities**](UsersApi.html#get_users_development_activities) | Get list of Development Activities|
|[**get_users_development_activities_me**](UsersApi.html#get_users_development_activities_me) | Get list of Development Activities for current user|
|[**get_users_development_activity**](UsersApi.html#get_users_development_activity) | Get a Development Activity|
|[**get_users_me**](UsersApi.html#get_users_me) | Get current user details.|
|[**get_users_search**](UsersApi.html#get_users_search) | Search users using the q64 value returned from a previous search|
|[**patch_user**](UsersApi.html#patch_user) | Update user|
|[**patch_user_callforwarding**](UsersApi.html#patch_user_callforwarding) | Patch a user&#39;s CallForwarding|
|[**patch_user_geolocation**](UsersApi.html#patch_user_geolocation) | Patch a user&#39;s Geolocation|
|[**patch_user_queue**](UsersApi.html#patch_user_queue) | Join or unjoin a queue for a user|
|[**patch_user_queues**](UsersApi.html#patch_user_queues) | Join or unjoin a set of queues for a user|
|[**patch_user_routinglanguage**](UsersApi.html#patch_user_routinglanguage) | Update routing language proficiency or state.|
|[**patch_user_routinglanguages_bulk**](UsersApi.html#patch_user_routinglanguages_bulk) | Add bulk routing language to user. Max limit 50 languages|
|[**patch_user_routingskills_bulk**](UsersApi.html#patch_user_routingskills_bulk) | Bulk add routing skills to user|
|[**patch_users_bulk**](UsersApi.html#patch_users_bulk) | Update bulk acd autoanswer on users|
|[**post_analytics_users_aggregates_query**](UsersApi.html#post_analytics_users_aggregates_query) | Query for user aggregates|
|[**post_analytics_users_details_jobs**](UsersApi.html#post_analytics_users_details_jobs) | Query for user details asynchronously|
|[**post_analytics_users_details_query**](UsersApi.html#post_analytics_users_details_query) | Query for user details|
|[**post_analytics_users_observations_query**](UsersApi.html#post_analytics_users_observations_query) | Query for user observations|
|[**post_authorization_subject_bulkadd**](UsersApi.html#post_authorization_subject_bulkadd) | Bulk-grant roles and divisions to a subject.|
|[**post_authorization_subject_bulkremove**](UsersApi.html#post_authorization_subject_bulkremove) | Bulk-remove grants from a subject.|
|[**post_authorization_subject_division_role**](UsersApi.html#post_authorization_subject_division_role) | Make a grant of a role in a division|
|[**post_user_invite**](UsersApi.html#post_user_invite) | Send an activation email to the user|
|[**post_user_password**](UsersApi.html#post_user_password) | Change a users password|
|[**post_user_routinglanguages**](UsersApi.html#post_user_routinglanguages) | Add routing language to user|
|[**post_user_routingskills**](UsersApi.html#post_user_routingskills) | Add routing skill to user|
|[**post_users**](UsersApi.html#post_users) | Create user|
|[**post_users_development_activities_aggregates_query**](UsersApi.html#post_users_development_activities_aggregates_query) | Retrieve aggregated development activity data|
|[**post_users_me_password**](UsersApi.html#post_users_me_password) | Change your password|
|[**post_users_search**](UsersApi.html#post_users_search) | Search users|
|[**put_routing_user_utilization**](UsersApi.html#put_routing_user_utilization) | Update the user&#39;s max utilization settings.  Include only those media types requiring custom configuration.|
|[**put_user_callforwarding**](UsersApi.html#put_user_callforwarding) | Update a user&#39;s CallForwarding|
|[**put_user_outofoffice**](UsersApi.html#put_user_outofoffice) | Update an OutOfOffice|
|[**put_user_profileskills**](UsersApi.html#put_user_profileskills) | Update profile skills for a user|
|[**put_user_roles**](UsersApi.html#put_user_roles) | Sets the user&#39;s roles|
|[**put_user_routingskill**](UsersApi.html#put_user_routingskill) | Update routing skill proficiency or state.|
|[**put_user_routingskills_bulk**](UsersApi.html#put_user_routingskills_bulk) | Replace all routing skills assigned to a user|
|[**put_user_routingstatus**](UsersApi.html#put_user_routingstatus) | Update the routing status of a user|
|[**put_user_station_associatedstation_station_id**](UsersApi.html#put_user_station_associatedstation_station_id) | Set associated station|
|[**put_user_station_defaultstation_station_id**](UsersApi.html#put_user_station_defaultstation_station_id) | Set default station|
{: class="table table-striped"}

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
api_instance = PureCloudPlatformClientV2.UsersApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async request
    api_instance.delete_analytics_users_details_job(job_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_analytics_users_details_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_authorization_subject_division_role"></a>

##  delete_authorization_subject_division_role(subject_id, division_id, role_id)



Delete a grant of a role in a division



Wraps DELETE /api/v2/authorization/subjects/{subjectId}/divisions/{divisionId}/roles/{roleId} 

Requires ANY permissions: 

* authorization:grant:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
division_id = 'division_id_example' # str | the id of the division of the grant
role_id = 'role_id_example' # str | the id of the role of the grant

try:
    # Delete a grant of a role in a division
    api_instance.delete_authorization_subject_division_role(subject_id, division_id, role_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_authorization_subject_division_role: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **subject_id** | **str**| Subject ID (user or group) |  |
| **division_id** | **str**| the id of the division of the grant |  |
| **role_id** | **str**| the id of the role of the grant |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_user_utilization"></a>

##  delete_routing_user_utilization(user_id)



Delete the user's max utilization settings and revert to the organization-wide default.



Wraps DELETE /api/v2/routing/users/{userId}/utilization 

Requires ANY permissions: 

* routing:utilization:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Delete the user's max utilization settings and revert to the organization-wide default.
    api_instance.delete_routing_user_utilization(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_routing_user_utilization: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_user"></a>

## [**Empty**](Empty.html) delete_user(user_id)



Delete user



Wraps DELETE /api/v2/users/{userId} 

Requires ANY permissions: 

* directory:user:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Delete user
    api_response = api_instance.delete_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="delete_user_routinglanguage"></a>

##  delete_user_routinglanguage(user_id, language_id)



Remove routing language from user



Wraps DELETE /api/v2/users/{userId}/routinglanguages/{languageId} 

Requires ANY permissions: 

* routing:skill:assign
* routing:language:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
language_id = 'language_id_example' # str | languageId

try:
    # Remove routing language from user
    api_instance.delete_user_routinglanguage(user_id, language_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_routinglanguage: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **language_id** | **str**| languageId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_user_routingskill"></a>

##  delete_user_routingskill(user_id, skill_id)



Remove routing skill from user



Wraps DELETE /api/v2/users/{userId}/routingskills/{skillId} 

Requires ALL permissions: 

* routing:skill:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
skill_id = 'skill_id_example' # str | skillId

try:
    # Remove routing skill from user
    api_instance.delete_user_routingskill(user_id, skill_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_routingskill: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **skill_id** | **str**| skillId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_user_station_associatedstation"></a>

##  delete_user_station_associatedstation(user_id)



Clear associated station



Wraps DELETE /api/v2/users/{userId}/station/associatedstation 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Clear associated station
    api_instance.delete_user_station_associatedstation(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_station_associatedstation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_user_station_defaultstation"></a>

##  delete_user_station_defaultstation(user_id)



Clear default station



Wraps DELETE /api/v2/users/{userId}/station/defaultstation 

Requires ANY permissions: 

* telephony:plugin:all
* telephony:phone:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Clear default station
    api_instance.delete_user_station_defaultstation(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_station_defaultstation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

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
api_instance = PureCloudPlatformClientV2.UsersApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for user details
    api_response = api_instance.get_analytics_users_details_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_analytics_users_details_job: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.UsersApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page) (optional)
page_size = 56 # int | The desired maximum number of results (optional)

try:
    # Fetch a page of results for an async query
    api_response = api_instance.get_analytics_users_details_job_results(job_id, cursor=cursor, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_analytics_users_details_job_results: %s\n" % e)
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

<a name="get_analytics_users_details_jobs_availability"></a>

## [**DataAvailabilityResponse**](DataAvailabilityResponse.html) get_analytics_users_details_jobs_availability()



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
api_instance = PureCloudPlatformClientV2.UsersApi()

try:
    # Lookup the datalake availability date and time
    api_response = api_instance.get_analytics_users_details_jobs_availability()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_analytics_users_details_jobs_availability: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**DataAvailabilityResponse**](DataAvailabilityResponse.html)

<a name="get_authorization_divisionspermitted_me"></a>

## [**list[AuthzDivision]**](AuthzDivision.html) get_authorization_divisionspermitted_me(permission, name=name)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Returns which divisions the current user has the given permission in.

This route is deprecated, use authorization/divisionspermitted/paged/me instead.

Wraps GET /api/v2/authorization/divisionspermitted/me 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
permission = 'permission_example' # str | The permission string, including the object to access, e.g. routing:queue:view
name = 'name_example' # str | Search term to filter by division name (optional)

try:
    # Returns which divisions the current user has the given permission in.
    api_response = api_instance.get_authorization_divisionspermitted_me(permission, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_authorization_divisionspermitted_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **permission** | **str**| The permission string, including the object to access, e.g. routing:queue:view |  |
| **name** | **str**| Search term to filter by division name | [optional]  |
{: class="table table-striped"}

### Return type

[**list[AuthzDivision]**](AuthzDivision.html)

<a name="get_authorization_divisionspermitted_paged_me"></a>

## [**DivsPermittedEntityListing**](DivsPermittedEntityListing.html) get_authorization_divisionspermitted_paged_me(permission, page_number=page_number, page_size=page_size)



Returns which divisions the current user has the given permission in.



Wraps GET /api/v2/authorization/divisionspermitted/paged/me 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
permission = 'permission_example' # str | The permission string, including the object to access, e.g. routing:queue:view
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Returns which divisions the current user has the given permission in.
    api_response = api_instance.get_authorization_divisionspermitted_paged_me(permission, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_authorization_divisionspermitted_paged_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **permission** | **str**| The permission string, including the object to access, e.g. routing:queue:view |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**DivsPermittedEntityListing**](DivsPermittedEntityListing.html)

<a name="get_authorization_divisionspermitted_paged_subject_id"></a>

## [**DivsPermittedEntityListing**](DivsPermittedEntityListing.html) get_authorization_divisionspermitted_paged_subject_id(subject_id, permission, page_number=page_number, page_size=page_size)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Returns which divisions the specified user has the given permission in.

This route is deprecated, use authorization/divisionspermitted/paged/me instead.

Wraps GET /api/v2/authorization/divisionspermitted/paged/{subjectId} 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
permission = 'permission_example' # str | The permission string, including the object to access, e.g. routing:queue:view
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Returns which divisions the specified user has the given permission in.
    api_response = api_instance.get_authorization_divisionspermitted_paged_subject_id(subject_id, permission, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_authorization_divisionspermitted_paged_subject_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **subject_id** | **str**| Subject ID (user or group) |  |
| **permission** | **str**| The permission string, including the object to access, e.g. routing:queue:view |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**DivsPermittedEntityListing**](DivsPermittedEntityListing.html)

<a name="get_authorization_subject"></a>

## [**AuthzSubject**](AuthzSubject.html) get_authorization_subject(subject_id)



Returns a listing of roles and permissions for a user.



Wraps GET /api/v2/authorization/subjects/{subjectId} 

Requires ANY permissions: 

* authorization:grant:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)

try:
    # Returns a listing of roles and permissions for a user.
    api_response = api_instance.get_authorization_subject(subject_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_authorization_subject: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **subject_id** | **str**| Subject ID (user or group) |  |
{: class="table table-striped"}

### Return type

[**AuthzSubject**](AuthzSubject.html)

<a name="get_authorization_subjects_me"></a>

## [**AuthzSubject**](AuthzSubject.html) get_authorization_subjects_me()



Returns a listing of roles and permissions for the currently authenticated user.



Wraps GET /api/v2/authorization/subjects/me 

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
api_instance = PureCloudPlatformClientV2.UsersApi()

try:
    # Returns a listing of roles and permissions for the currently authenticated user.
    api_response = api_instance.get_authorization_subjects_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_authorization_subjects_me: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**AuthzSubject**](AuthzSubject.html)

<a name="get_fieldconfig"></a>

## [**FieldConfig**](FieldConfig.html) get_fieldconfig(type)



Fetch field config for an entity type



Wraps GET /api/v2/fieldconfig 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
type = 'type_example' # str | Field type

try:
    # Fetch field config for an entity type
    api_response = api_instance.get_fieldconfig(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_fieldconfig: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | **str**| Field type | <br />**Values**: person, group, org, externalContact |
{: class="table table-striped"}

### Return type

[**FieldConfig**](FieldConfig.html)

<a name="get_profiles_users"></a>

## [**UserProfileEntityListing**](UserProfileEntityListing.html) get_profiles_users(page_size=page_size, page_number=page_number, id=id, jid=jid, sort_order=sort_order, expand=expand, integration_presence_source=integration_presence_source)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get a user profile listing

This api is deprecated. User /api/v2/users

Wraps GET /api/v2/profiles/users 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
id = ['id_example'] # list[str] | id (optional)
jid = ['jid_example'] # list[str] | jid (optional)
sort_order = 'ASC' # str | Ascending or descending sort order (optional) (default to ASC)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
integration_presence_source = 'integration_presence_source_example' # str | Gets an integration presence for users instead of their defaults. This parameter will only be used when presence is provided as an \"expand\". (optional)

try:
    # Get a user profile listing
    api_response = api_instance.get_profiles_users(page_size=page_size, page_number=page_number, id=id, jid=jid, sort_order=sort_order, expand=expand, integration_presence_source=integration_presence_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_profiles_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **id** | [**list[str]**](str.html)| id | [optional]  |
| **jid** | [**list[str]**](str.html)| jid | [optional]  |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to ASC]<br />**Values**: ascending, descending |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization |
| **integration_presence_source** | **str**| Gets an integration presence for users instead of their defaults. This parameter will only be used when presence is provided as an \&quot;expand\&quot;. | [optional] <br />**Values**: MicrosoftTeams, ZoomPhone, RingCentral |
{: class="table table-striped"}

### Return type

[**UserProfileEntityListing**](UserProfileEntityListing.html)

<a name="get_routing_user_utilization"></a>

## [**Utilization**](Utilization.html) get_routing_user_utilization(user_id)



Get the user's max utilization settings.  If not configured, the organization-wide default is returned.



Wraps GET /api/v2/routing/users/{userId}/utilization 

Requires ANY permissions: 

* routing:utilization:manage
* routing:utilization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Get the user's max utilization settings.  If not configured, the organization-wide default is returned.
    api_response = api_instance.get_routing_user_utilization(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_routing_user_utilization: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

[**Utilization**](Utilization.html)

<a name="get_user"></a>

## [**User**](User.html) get_user(user_id, expand=expand, integration_presence_source=integration_presence_source, state=state)



Get user.



Wraps GET /api/v2/users/{userId} 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
integration_presence_source = 'integration_presence_source_example' # str | Gets an integration presence for a user instead of their default. (optional)
state = 'active' # str | Search for a user with this state (optional) (default to active)

try:
    # Get user.
    api_response = api_instance.get_user(user_id, expand=expand, integration_presence_source=integration_presence_source, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography |
| **integration_presence_source** | **str**| Gets an integration presence for a user instead of their default. | [optional] <br />**Values**: MicrosoftTeams, ZoomPhone, RingCentral |
| **state** | **str**| Search for a user with this state | [optional] [default to active]<br />**Values**: active, deleted |
{: class="table table-striped"}

### Return type

[**User**](User.html)

<a name="get_user_adjacents"></a>

## [**Adjacents**](Adjacents.html) get_user_adjacents(user_id, expand=expand)



Get adjacents



Wraps GET /api/v2/users/{userId}/adjacents 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get adjacents
    api_response = api_instance.get_user_adjacents(user_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_adjacents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography |
{: class="table table-striped"}

### Return type

[**Adjacents**](Adjacents.html)

<a name="get_user_callforwarding"></a>

## [**CallForwarding**](CallForwarding.html) get_user_callforwarding(user_id)



Get a user's CallForwarding



Wraps GET /api/v2/users/{userId}/callforwarding 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Get a user's CallForwarding
    api_response = api_instance.get_user_callforwarding(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_callforwarding: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

[**CallForwarding**](CallForwarding.html)

<a name="get_user_directreports"></a>

## [**list[User]**](User.html) get_user_directreports(user_id, expand=expand)



Get direct reports



Wraps GET /api/v2/users/{userId}/directreports 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get direct reports
    api_response = api_instance.get_user_directreports(user_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_directreports: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography |
{: class="table table-striped"}

### Return type

[**list[User]**](User.html)

<a name="get_user_favorites"></a>

## [**UserEntityListing**](UserEntityListing.html) get_user_favorites(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand)



Get favorites



Wraps GET /api/v2/users/{userId}/favorites 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'ASC' # str | Sort order (optional) (default to ASC)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get favorites
    api_response = api_instance.get_user_favorites(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_favorites: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Sort order | [optional] [default to ASC] |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography |
{: class="table table-striped"}

### Return type

[**UserEntityListing**](UserEntityListing.html)

<a name="get_user_geolocation"></a>

## [**Geolocation**](Geolocation.html) get_user_geolocation(user_id, client_id)



Get a user's Geolocation



Wraps GET /api/v2/users/{userId}/geolocations/{clientId} 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | user Id
client_id = 'client_id_example' # str | client Id

try:
    # Get a user's Geolocation
    api_response = api_instance.get_user_geolocation(user_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_geolocation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| user Id |  |
| **client_id** | **str**| client Id |  |
{: class="table table-striped"}

### Return type

[**Geolocation**](Geolocation.html)

<a name="get_user_outofoffice"></a>

## [**OutOfOffice**](OutOfOffice.html) get_user_outofoffice(user_id)



Get a OutOfOffice



Wraps GET /api/v2/users/{userId}/outofoffice 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Get a OutOfOffice
    api_response = api_instance.get_user_outofoffice(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_outofoffice: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

[**OutOfOffice**](OutOfOffice.html)

<a name="get_user_profile"></a>

## [**UserProfile**](UserProfile.html) get_user_profile(user_id, expand=expand, integration_presence_source=integration_presence_source)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get user profile

This api has been deprecated. Use api/v2/users instead

Wraps GET /api/v2/users/{userId}/profile 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | userId
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
integration_presence_source = 'integration_presence_source_example' # str | Gets an integration presence for a user instead of their default. (optional)

try:
    # Get user profile
    api_response = api_instance.get_user_profile(user_id, expand=expand, integration_presence_source=integration_presence_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_profile: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| userId |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team |
| **integration_presence_source** | **str**| Gets an integration presence for a user instead of their default. | [optional] <br />**Values**: MicrosoftTeams, ZoomPhone, RingCentral |
{: class="table table-striped"}

### Return type

[**UserProfile**](UserProfile.html)

<a name="get_user_profileskills"></a>

## list[str]** get_user_profileskills(user_id)



List profile skills for a user



Wraps GET /api/v2/users/{userId}/profileskills 

Requires ANY permissions: 

* directory:userProfile:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # List profile skills for a user
    api_response = api_instance.get_user_profileskills(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_profileskills: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

**list[str]**

<a name="get_user_queues"></a>

## [**UserQueueEntityListing**](UserQueueEntityListing.html) get_user_queues(user_id, page_size=page_size, page_number=page_number, joined=joined, division_id=division_id)



Get queues for user



Wraps GET /api/v2/users/{userId}/queues 

Requires ANY permissions: 

* routing:queue:view
* routing:queue:join
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
joined = true # bool | Is joined to the queue (optional) (default to true)
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)

try:
    # Get queues for user
    api_response = api_instance.get_user_queues(user_id, page_size=page_size, page_number=page_number, joined=joined, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_queues: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **joined** | **bool**| Is joined to the queue | [optional] [default to true] |
| **division_id** | [**list[str]**](str.html)| Division ID(s) | [optional]  |
{: class="table table-striped"}

### Return type

[**UserQueueEntityListing**](UserQueueEntityListing.html)

<a name="get_user_roles"></a>

## [**UserAuthorization**](UserAuthorization.html) get_user_roles(user_id)



Returns a listing of roles and permissions for a user.



Wraps GET /api/v2/users/{userId}/roles 

Requires ANY permissions: 

* authorization:grant:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Returns a listing of roles and permissions for a user.
    api_response = api_instance.get_user_roles(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

[**UserAuthorization**](UserAuthorization.html)

<a name="get_user_routinglanguages"></a>

## [**UserLanguageEntityListing**](UserLanguageEntityListing.html) get_user_routinglanguages(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)



List routing language for user



Wraps GET /api/v2/users/{userId}/routinglanguages 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'ASC' # str | Ascending or descending sort order (optional) (default to ASC)

try:
    # List routing language for user
    api_response = api_instance.get_user_routinglanguages(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_routinglanguages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to ASC]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**UserLanguageEntityListing**](UserLanguageEntityListing.html)

<a name="get_user_routingskills"></a>

## [**UserSkillEntityListing**](UserSkillEntityListing.html) get_user_routingskills(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)



List routing skills for user



Wraps GET /api/v2/users/{userId}/routingskills 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'ASC' # str | Ascending or descending sort order (optional) (default to ASC)

try:
    # List routing skills for user
    api_response = api_instance.get_user_routingskills(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_routingskills: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to ASC]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**UserSkillEntityListing**](UserSkillEntityListing.html)

<a name="get_user_routingstatus"></a>

## [**RoutingStatus**](RoutingStatus.html) get_user_routingstatus(user_id)



Fetch the routing status of a user



Wraps GET /api/v2/users/{userId}/routingstatus 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Fetch the routing status of a user
    api_response = api_instance.get_user_routingstatus(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_routingstatus: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

[**RoutingStatus**](RoutingStatus.html)

<a name="get_user_station"></a>

## [**UserStations**](UserStations.html) get_user_station(user_id)



Get station information for user



Wraps GET /api/v2/users/{userId}/station 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Get station information for user
    api_response = api_instance.get_user_station(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_station: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

[**UserStations**](UserStations.html)

<a name="get_user_superiors"></a>

## [**list[User]**](User.html) get_user_superiors(user_id, expand=expand)



Get superiors



Wraps GET /api/v2/users/{userId}/superiors 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get superiors
    api_response = api_instance.get_user_superiors(user_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_superiors: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography |
{: class="table table-striped"}

### Return type

[**list[User]**](User.html)

<a name="get_user_trustors"></a>

## [**TrustorEntityListing**](TrustorEntityListing.html) get_user_trustors(user_id, page_size=page_size, page_number=page_number)



List the organizations that have authorized/trusted the user.



Wraps GET /api/v2/users/{userId}/trustors 

Requires ALL permissions: 

* authorization:orgTrustor:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # List the organizations that have authorized/trusted the user.
    api_response = api_instance.get_user_trustors(user_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_trustors: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**TrustorEntityListing**](TrustorEntityListing.html)

<a name="get_users"></a>

## [**UserEntityListing**](UserEntityListing.html) get_users(page_size=page_size, page_number=page_number, id=id, jabber_id=jabber_id, sort_order=sort_order, expand=expand, integration_presence_source=integration_presence_source, state=state)



Get the list of available users.



Wraps GET /api/v2/users 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
id = ['id_example'] # list[str] | A list of user IDs to fetch by bulk (optional)
jabber_id = ['jabber_id_example'] # list[str] | A list of jabberIds to fetch by bulk (cannot be used with the \"id\" parameter) (optional)
sort_order = 'ASC' # str | Ascending or descending sort order (optional) (default to ASC)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
integration_presence_source = 'integration_presence_source_example' # str | Gets an integration presence for users instead of their defaults. This parameter will only be used when presence is provided as an \"expand\". When using this parameter the maximum number of users that can be returned is 10. (optional)
state = 'active' # str | Only list users of this state (optional) (default to active)

try:
    # Get the list of available users.
    api_response = api_instance.get_users(page_size=page_size, page_number=page_number, id=id, jabber_id=jabber_id, sort_order=sort_order, expand=expand, integration_presence_source=integration_presence_source, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **id** | [**list[str]**](str.html)| A list of user IDs to fetch by bulk | [optional]  |
| **jabber_id** | [**list[str]**](str.html)| A list of jabberIds to fetch by bulk (cannot be used with the \&quot;id\&quot; parameter) | [optional]  |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to ASC]<br />**Values**: ascending, descending |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography |
| **integration_presence_source** | **str**| Gets an integration presence for users instead of their defaults. This parameter will only be used when presence is provided as an \&quot;expand\&quot;. When using this parameter the maximum number of users that can be returned is 10. | [optional] <br />**Values**: MicrosoftTeams, ZoomPhone, RingCentral |
| **state** | **str**| Only list users of this state | [optional] [default to active]<br />**Values**: active, inactive, deleted, any |
{: class="table table-striped"}

### Return type

[**UserEntityListing**](UserEntityListing.html)

<a name="get_users_development_activities"></a>

## [**DevelopmentActivityListing**](DevelopmentActivityListing.html) get_users_development_activities(user_id=user_id, module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, sort_order=sort_order, types=types, statuses=statuses, relationship=relationship)



Get list of Development Activities

Either moduleId or userId is required. Results are filtered based on the applicable permissions.

Wraps GET /api/v2/users/development/activities 

Requires ANY permissions: 

* learning:assignment:view
* coaching:appointment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = ['user_id_example'] # list[str] | Specifies the list of user IDs to be queried, up to 100 user IDs. It searches for any relationship for the userId. (optional)
module_id = 'module_id_example' # str | Specifies the ID of the learning module. (optional)
interval = 'interval_example' # str | Specifies the dateDue range to be queried. Milliseconds will be truncated. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
completion_interval = 'completion_interval_example' # str | Specifies the range of completion dates to be used for filtering. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
overdue = 'Any' # str | Specifies if non-overdue, overdue, or all activities are returned. If not specified, all activities are returned (optional) (default to Any)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'Desc' # str | Specifies result set sort order sorted by the date due; if not specified, default sort order is descending (Desc) (optional) (default to Desc)
types = ['types_example'] # list[str] | Specifies the activity types. (optional)
statuses = ['statuses_example'] # list[str] | Specifies the activity statuses to filter by (optional)
relationship = ['relationship_example'] # list[str] | Specifies how the current user relation should be interpreted, and filters the activities returned to only the activities that have the specified relationship. If a value besides Attendee is specified, it will only return Coaching Appointments. If not specified, no filtering is applied. (optional)

try:
    # Get list of Development Activities
    api_response = api_instance.get_users_development_activities(user_id=user_id, module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, sort_order=sort_order, types=types, statuses=statuses, relationship=relationship)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_development_activities: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | [**list[str]**](str.html)| Specifies the list of user IDs to be queried, up to 100 user IDs. It searches for any relationship for the userId. | [optional]  |
| **module_id** | **str**| Specifies the ID of the learning module. | [optional]  |
| **interval** | **str**| Specifies the dateDue range to be queried. Milliseconds will be truncated. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **completion_interval** | **str**| Specifies the range of completion dates to be used for filtering. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **overdue** | **str**| Specifies if non-overdue, overdue, or all activities are returned. If not specified, all activities are returned | [optional] [default to Any]<br />**Values**: True, False, Any |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Specifies result set sort order sorted by the date due; if not specified, default sort order is descending (Desc) | [optional] [default to Desc]<br />**Values**: Asc, Desc |
| **types** | [**list[str]**](str.html)| Specifies the activity types. | [optional] <br />**Values**: Informational, Coaching |
| **statuses** | [**list[str]**](str.html)| Specifies the activity statuses to filter by | [optional] <br />**Values**: Planned, InProgress, Completed, InvalidSchedule |
| **relationship** | [**list[str]**](str.html)| Specifies how the current user relation should be interpreted, and filters the activities returned to only the activities that have the specified relationship. If a value besides Attendee is specified, it will only return Coaching Appointments. If not specified, no filtering is applied. | [optional] <br />**Values**: Creator, Facilitator, Attendee |
{: class="table table-striped"}

### Return type

[**DevelopmentActivityListing**](DevelopmentActivityListing.html)

<a name="get_users_development_activities_me"></a>

## [**DevelopmentActivityListing**](DevelopmentActivityListing.html) get_users_development_activities_me(module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, sort_order=sort_order, types=types, statuses=statuses, relationship=relationship)



Get list of Development Activities for current user

Results are filtered based on the applicable permissions.

Wraps GET /api/v2/users/development/activities/me 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
module_id = 'module_id_example' # str | Specifies the ID of the learning module. (optional)
interval = 'interval_example' # str | Specifies the dateDue range to be queried. Milliseconds will be truncated. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
completion_interval = 'completion_interval_example' # str | Specifies the range of completion dates to be used for filtering. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
overdue = 'Any' # str | Specifies if non-overdue, overdue, or all activities are returned. If not specified, all activities are returned (optional) (default to Any)
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'Desc' # str | Specifies result set sort order sorted by the date due; if not specified, default sort order is descending (Desc) (optional) (default to Desc)
types = ['types_example'] # list[str] | Specifies the activity types. (optional)
statuses = ['statuses_example'] # list[str] | Specifies the activity statuses to filter by (optional)
relationship = ['relationship_example'] # list[str] | Specifies how the current user relation should be interpreted, and filters the activities returned to only the activities that have the specified relationship. If a value besides Attendee is specified, it will only return Coaching Appointments. If not specified, no filtering is applied. (optional)

try:
    # Get list of Development Activities for current user
    api_response = api_instance.get_users_development_activities_me(module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, page_size=page_size, page_number=page_number, sort_order=sort_order, types=types, statuses=statuses, relationship=relationship)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_development_activities_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **module_id** | **str**| Specifies the ID of the learning module. | [optional]  |
| **interval** | **str**| Specifies the dateDue range to be queried. Milliseconds will be truncated. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **completion_interval** | **str**| Specifies the range of completion dates to be used for filtering. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **overdue** | **str**| Specifies if non-overdue, overdue, or all activities are returned. If not specified, all activities are returned | [optional] [default to Any]<br />**Values**: True, False, Any |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Specifies result set sort order sorted by the date due; if not specified, default sort order is descending (Desc) | [optional] [default to Desc]<br />**Values**: Asc, Desc |
| **types** | [**list[str]**](str.html)| Specifies the activity types. | [optional] <br />**Values**: Informational, Coaching |
| **statuses** | [**list[str]**](str.html)| Specifies the activity statuses to filter by | [optional] <br />**Values**: Planned, InProgress, Completed, InvalidSchedule |
| **relationship** | [**list[str]**](str.html)| Specifies how the current user relation should be interpreted, and filters the activities returned to only the activities that have the specified relationship. If a value besides Attendee is specified, it will only return Coaching Appointments. If not specified, no filtering is applied. | [optional] <br />**Values**: Creator, Facilitator, Attendee |
{: class="table table-striped"}

### Return type

[**DevelopmentActivityListing**](DevelopmentActivityListing.html)

<a name="get_users_development_activity"></a>

## [**DevelopmentActivity**](DevelopmentActivity.html) get_users_development_activity(activity_id, type)



Get a Development Activity

Permission not required if you are the attendee, creator or facilitator of the coaching appointment or you are the assigned user of the learning assignment.

Wraps GET /api/v2/users/development/activities/{activityId} 

Requires ANY permissions: 

* learning:assignment:view
* coaching:appointment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
activity_id = 'activity_id_example' # str | Specifies the activity ID, maps to either assignment or appointment ID
type = 'type_example' # str | Specifies the activity type.

try:
    # Get a Development Activity
    api_response = api_instance.get_users_development_activity(activity_id, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_development_activity: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **activity_id** | **str**| Specifies the activity ID, maps to either assignment or appointment ID |  |
| **type** | **str**| Specifies the activity type. | <br />**Values**: Informational, Coaching |
{: class="table table-striped"}

### Return type

[**DevelopmentActivity**](DevelopmentActivity.html)

<a name="get_users_me"></a>

## [**UserMe**](UserMe.html) get_users_me(expand=expand, integration_presence_source=integration_presence_source)



Get current user details.

This request is not valid when using the Client Credentials OAuth grant.

Wraps GET /api/v2/users/me 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)
integration_presence_source = 'integration_presence_source_example' # str | Get your presence for a given integration. This parameter will only be used when presence is provided as an \"expand\". (optional)

try:
    # Get current user details.
    api_response = api_instance.get_users_me(expand=expand, integration_presence_source=integration_presence_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand. | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, date, geolocationsettings, organization, presencedefinitions, locationdefinitions, orgauthorization, orgproducts, favorites, superiors, directreports, adjacents, routingskills, routinglanguages, fieldconfigs, token, trustors, logCapture |
| **integration_presence_source** | **str**| Get your presence for a given integration. This parameter will only be used when presence is provided as an \&quot;expand\&quot;. | [optional] <br />**Values**: MicrosoftTeams, ZoomPhone, RingCentral |
{: class="table table-striped"}

### Return type

[**UserMe**](UserMe.html)

<a name="get_users_search"></a>

## [**UsersSearchResponse**](UsersSearchResponse.html) get_users_search(q64, expand=expand, integration_presence_source=integration_presence_source)



Search users using the q64 value returned from a previous search



Wraps GET /api/v2/users/search 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | expand (optional)
integration_presence_source = 'integration_presence_source_example' # str | integrationPresenceSource (optional)

try:
    # Search users using the q64 value returned from a previous search
    api_response = api_instance.get_users_search(q64, expand=expand, integration_presence_source=integration_presence_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str.html)| expand | [optional]  |
| **integration_presence_source** | **str**| integrationPresenceSource | [optional] <br />**Values**: MicrosoftTeams, ZoomPhone, RingCentral |
{: class="table table-striped"}

### Return type

[**UsersSearchResponse**](UsersSearchResponse.html)

<a name="patch_user"></a>

## [**User**](User.html) patch_user(user_id, body)



Update user



Wraps PATCH /api/v2/users/{userId} 

Requires ANY permissions: 

* directory:user:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.UpdateUser() # UpdateUser | User

try:
    # Update user
    api_response = api_instance.patch_user(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**UpdateUser**](UpdateUser.html)| User |  |
{: class="table table-striped"}

### Return type

[**User**](User.html)

<a name="patch_user_callforwarding"></a>

## [**CallForwarding**](CallForwarding.html) patch_user_callforwarding(user_id, body)



Patch a user's CallForwarding



Wraps PATCH /api/v2/users/{userId}/callforwarding 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.CallForwarding() # CallForwarding | Call forwarding

try:
    # Patch a user's CallForwarding
    api_response = api_instance.patch_user_callforwarding(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_user_callforwarding: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**CallForwarding**](CallForwarding.html)| Call forwarding |  |
{: class="table table-striped"}

### Return type

[**CallForwarding**](CallForwarding.html)

<a name="patch_user_geolocation"></a>

## [**Geolocation**](Geolocation.html) patch_user_geolocation(user_id, client_id, body)



Patch a user's Geolocation

The geolocation object can be patched one of three ways. Option 1: Set the 'primary' property to true. This will set the client as the user's primary geolocation source.  Option 2: Provide the 'latitude' and 'longitude' values.  This will enqueue an asynchronous update of the 'city', 'region', and 'country', generating a notification. A subsequent GET operation will include the new values for 'city', 'region' and 'country'.  Option 3:  Provide the 'city', 'region', 'country' values.  Option 1 can be combined with Option 2 or Option 3.  For example, update the client as primary and provide latitude and longitude values.

Wraps PATCH /api/v2/users/{userId}/geolocations/{clientId} 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | user Id
client_id = 'client_id_example' # str | client Id
body = PureCloudPlatformClientV2.Geolocation() # Geolocation | Geolocation

try:
    # Patch a user's Geolocation
    api_response = api_instance.patch_user_geolocation(user_id, client_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_user_geolocation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| user Id |  |
| **client_id** | **str**| client Id |  |
| **body** | [**Geolocation**](Geolocation.html)| Geolocation |  |
{: class="table table-striped"}

### Return type

[**Geolocation**](Geolocation.html)

<a name="patch_user_queue"></a>

## [**UserQueue**](UserQueue.html) patch_user_queue(queue_id, user_id, body)



Join or unjoin a queue for a user



Wraps PATCH /api/v2/users/{userId}/queues/{queueId} 

Requires ANY permissions: 

* routing:queue:join
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
queue_id = 'queue_id_example' # str | Queue ID
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.UserQueue() # UserQueue | Queue Member

try:
    # Join or unjoin a queue for a user
    api_response = api_instance.patch_user_queue(queue_id, user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_user_queue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **user_id** | **str**| User ID |  |
| **body** | [**UserQueue**](UserQueue.html)| Queue Member |  |
{: class="table table-striped"}

### Return type

[**UserQueue**](UserQueue.html)

<a name="patch_user_queues"></a>

## [**UserQueueEntityListing**](UserQueueEntityListing.html) patch_user_queues(user_id, body, division_id=division_id)



Join or unjoin a set of queues for a user



Wraps PATCH /api/v2/users/{userId}/queues 

Requires ANY permissions: 

* routing:queue:join
* routing:queueMember:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = [PureCloudPlatformClientV2.UserQueue()] # list[UserQueue] | User Queues
division_id = ['division_id_example'] # list[str] | Division ID(s) (optional)

try:
    # Join or unjoin a set of queues for a user
    api_response = api_instance.patch_user_queues(user_id, body, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_user_queues: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserQueue]**](UserQueue.html)| User Queues |  |
| **division_id** | [**list[str]**](str.html)| Division ID(s) | [optional]  |
{: class="table table-striped"}

### Return type

[**UserQueueEntityListing**](UserQueueEntityListing.html)

<a name="patch_user_routinglanguage"></a>

## [**UserRoutingLanguage**](UserRoutingLanguage.html) patch_user_routinglanguage(user_id, language_id, body)



Update routing language proficiency or state.



Wraps PATCH /api/v2/users/{userId}/routinglanguages/{languageId} 

Requires ANY permissions: 

* routing:skill:assign
* routing:language:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
language_id = 'language_id_example' # str | languageId
body = PureCloudPlatformClientV2.UserRoutingLanguage() # UserRoutingLanguage | Language

try:
    # Update routing language proficiency or state.
    api_response = api_instance.patch_user_routinglanguage(user_id, language_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_user_routinglanguage: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **language_id** | **str**| languageId |  |
| **body** | [**UserRoutingLanguage**](UserRoutingLanguage.html)| Language |  |
{: class="table table-striped"}

### Return type

[**UserRoutingLanguage**](UserRoutingLanguage.html)

<a name="patch_user_routinglanguages_bulk"></a>

## [**UserLanguageEntityListing**](UserLanguageEntityListing.html) patch_user_routinglanguages_bulk(user_id, body)



Add bulk routing language to user. Max limit 50 languages



Wraps PATCH /api/v2/users/{userId}/routinglanguages/bulk 

Requires ANY permissions: 

* routing:skill:assign
* routing:language:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = [PureCloudPlatformClientV2.UserRoutingLanguagePost()] # list[UserRoutingLanguagePost] | Language

try:
    # Add bulk routing language to user. Max limit 50 languages
    api_response = api_instance.patch_user_routinglanguages_bulk(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_user_routinglanguages_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserRoutingLanguagePost]**](UserRoutingLanguagePost.html)| Language |  |
{: class="table table-striped"}

### Return type

[**UserLanguageEntityListing**](UserLanguageEntityListing.html)

<a name="patch_user_routingskills_bulk"></a>

## [**UserSkillEntityListing**](UserSkillEntityListing.html) patch_user_routingskills_bulk(user_id, body)



Bulk add routing skills to user



Wraps PATCH /api/v2/users/{userId}/routingskills/bulk 

Requires ANY permissions: 

* routing:skill:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = [PureCloudPlatformClientV2.UserRoutingSkillPost()] # list[UserRoutingSkillPost] | Skill

try:
    # Bulk add routing skills to user
    api_response = api_instance.patch_user_routingskills_bulk(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_user_routingskills_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserRoutingSkillPost]**](UserRoutingSkillPost.html)| Skill |  |
{: class="table table-striped"}

### Return type

[**UserSkillEntityListing**](UserSkillEntityListing.html)

<a name="patch_users_bulk"></a>

## [**UserEntityListing**](UserEntityListing.html) patch_users_bulk(body)



Update bulk acd autoanswer on users



Wraps PATCH /api/v2/users/bulk 

Requires ANY permissions: 

* directory:user:add
* directory:user:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
body = [PureCloudPlatformClientV2.PatchUser()] # list[PatchUser] | Users

try:
    # Update bulk acd autoanswer on users
    api_response = api_instance.patch_users_bulk(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_users_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**list[PatchUser]**](PatchUser.html)| Users |  |
{: class="table table-striped"}

### Return type

[**UserEntityListing**](UserEntityListing.html)

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
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.UserAggregationQuery() # UserAggregationQuery | query

try:
    # Query for user aggregates
    api_response = api_instance.post_analytics_users_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_analytics_users_aggregates_query: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.AsyncUserDetailsQuery() # AsyncUserDetailsQuery | query

try:
    # Query for user details asynchronously
    api_response = api_instance.post_analytics_users_details_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_analytics_users_details_jobs: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.UserDetailsQuery() # UserDetailsQuery | query

try:
    # Query for user details
    api_response = api_instance.post_analytics_users_details_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_analytics_users_details_query: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.UserObservationQuery() # UserObservationQuery | query

try:
    # Query for user observations
    api_response = api_instance.post_analytics_users_observations_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_analytics_users_observations_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserObservationQuery**](UserObservationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**UserObservationQueryResponse**](UserObservationQueryResponse.html)

<a name="post_authorization_subject_bulkadd"></a>

##  post_authorization_subject_bulkadd(subject_id, body, subject_type=subject_type)



Bulk-grant roles and divisions to a subject.



Wraps POST /api/v2/authorization/subjects/{subjectId}/bulkadd 

Requires ANY permissions: 

* authorization:grant:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
body = PureCloudPlatformClientV2.RoleDivisionGrants() # RoleDivisionGrants | Pairs of role and division IDs
subject_type = 'PC_USER' # str | what the type of the subject is (PC_GROUP, PC_USER or PC_OAUTH_CLIENT) (optional) (default to PC_USER)

try:
    # Bulk-grant roles and divisions to a subject.
    api_instance.post_authorization_subject_bulkadd(subject_id, body, subject_type=subject_type)
except ApiException as e:
    print("Exception when calling UsersApi->post_authorization_subject_bulkadd: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **subject_id** | **str**| Subject ID (user or group) |  |
| **body** | [**RoleDivisionGrants**](RoleDivisionGrants.html)| Pairs of role and division IDs |  |
| **subject_type** | **str**| what the type of the subject is (PC_GROUP, PC_USER or PC_OAUTH_CLIENT) | [optional] [default to PC_USER] |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_authorization_subject_bulkremove"></a>

##  post_authorization_subject_bulkremove(subject_id, body)



Bulk-remove grants from a subject.



Wraps POST /api/v2/authorization/subjects/{subjectId}/bulkremove 

Requires ANY permissions: 

* authorization:grant:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
body = PureCloudPlatformClientV2.RoleDivisionGrants() # RoleDivisionGrants | Pairs of role and division IDs

try:
    # Bulk-remove grants from a subject.
    api_instance.post_authorization_subject_bulkremove(subject_id, body)
except ApiException as e:
    print("Exception when calling UsersApi->post_authorization_subject_bulkremove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **subject_id** | **str**| Subject ID (user or group) |  |
| **body** | [**RoleDivisionGrants**](RoleDivisionGrants.html)| Pairs of role and division IDs |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_authorization_subject_division_role"></a>

##  post_authorization_subject_division_role(subject_id, division_id, role_id, subject_type=subject_type)



Make a grant of a role in a division



Wraps POST /api/v2/authorization/subjects/{subjectId}/divisions/{divisionId}/roles/{roleId} 

Requires ANY permissions: 

* authorization:grant:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
division_id = 'division_id_example' # str | the id of the division to which to make the grant
role_id = 'role_id_example' # str | the id of the role to grant
subject_type = 'PC_USER' # str | what the type of the subject is: PC_GROUP, PC_USER or PC_OAUTH_CLIENT (note: for cross-org authorization, please use the Organization Authorization endpoints) (optional) (default to PC_USER)

try:
    # Make a grant of a role in a division
    api_instance.post_authorization_subject_division_role(subject_id, division_id, role_id, subject_type=subject_type)
except ApiException as e:
    print("Exception when calling UsersApi->post_authorization_subject_division_role: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **subject_id** | **str**| Subject ID (user or group) |  |
| **division_id** | **str**| the id of the division to which to make the grant |  |
| **role_id** | **str**| the id of the role to grant |  |
| **subject_type** | **str**| what the type of the subject is: PC_GROUP, PC_USER or PC_OAUTH_CLIENT (note: for cross-org authorization, please use the Organization Authorization endpoints) | [optional] [default to PC_USER] |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_user_invite"></a>

##  post_user_invite(user_id, force=force)



Send an activation email to the user



Wraps POST /api/v2/users/{userId}/invite 

Requires ANY permissions: 

* directory:user:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
force = false # bool | Resend the invitation even if one is already outstanding (optional) (default to false)

try:
    # Send an activation email to the user
    api_instance.post_user_invite(user_id, force=force)
except ApiException as e:
    print("Exception when calling UsersApi->post_user_invite: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **force** | **bool**| Resend the invitation even if one is already outstanding | [optional] [default to false] |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_user_password"></a>

##  post_user_password(user_id, body)



Change a users password



Wraps POST /api/v2/users/{userId}/password 

Requires ANY permissions: 

* directory:user:setPassword

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.ChangePasswordRequest() # ChangePasswordRequest | Password

try:
    # Change a users password
    api_instance.post_user_password(user_id, body)
except ApiException as e:
    print("Exception when calling UsersApi->post_user_password: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**ChangePasswordRequest**](ChangePasswordRequest.html)| Password |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_user_routinglanguages"></a>

## [**UserRoutingLanguage**](UserRoutingLanguage.html) post_user_routinglanguages(user_id, body)



Add routing language to user



Wraps POST /api/v2/users/{userId}/routinglanguages 

Requires ANY permissions: 

* routing:skill:assign
* routing:language:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.UserRoutingLanguagePost() # UserRoutingLanguagePost | Language

try:
    # Add routing language to user
    api_response = api_instance.post_user_routinglanguages(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_user_routinglanguages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**UserRoutingLanguagePost**](UserRoutingLanguagePost.html)| Language |  |
{: class="table table-striped"}

### Return type

[**UserRoutingLanguage**](UserRoutingLanguage.html)

<a name="post_user_routingskills"></a>

## [**UserRoutingSkill**](UserRoutingSkill.html) post_user_routingskills(user_id, body)



Add routing skill to user



Wraps POST /api/v2/users/{userId}/routingskills 

Requires ALL permissions: 

* routing:skill:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.UserRoutingSkillPost() # UserRoutingSkillPost | Skill

try:
    # Add routing skill to user
    api_response = api_instance.post_user_routingskills(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_user_routingskills: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**UserRoutingSkillPost**](UserRoutingSkillPost.html)| Skill |  |
{: class="table table-striped"}

### Return type

[**UserRoutingSkill**](UserRoutingSkill.html)

<a name="post_users"></a>

## [**User**](User.html) post_users(body)



Create user



Wraps POST /api/v2/users 

Requires ANY permissions: 

* directory:user:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.CreateUser() # CreateUser | User

try:
    # Create user
    api_response = api_instance.post_users(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateUser**](CreateUser.html)| User |  |
{: class="table table-striped"}

### Return type

[**User**](User.html)

<a name="post_users_development_activities_aggregates_query"></a>

## [**DevelopmentActivityAggregateResponse**](DevelopmentActivityAggregateResponse.html) post_users_development_activities_aggregates_query(body)



Retrieve aggregated development activity data

Results are filtered based on the applicable permissions.

Wraps POST /api/v2/users/development/activities/aggregates/query 

Requires ANY permissions: 

* learning:assignment:view
* coaching:appointment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.DevelopmentActivityAggregateParam() # DevelopmentActivityAggregateParam | Aggregate Request

try:
    # Retrieve aggregated development activity data
    api_response = api_instance.post_users_development_activities_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_development_activities_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DevelopmentActivityAggregateParam**](DevelopmentActivityAggregateParam.html)| Aggregate Request |  |
{: class="table table-striped"}

### Return type

[**DevelopmentActivityAggregateResponse**](DevelopmentActivityAggregateResponse.html)

<a name="post_users_me_password"></a>

##  post_users_me_password(body)



Change your password



Wraps POST /api/v2/users/me/password 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.ChangeMyPasswordRequest() # ChangeMyPasswordRequest | Password

try:
    # Change your password
    api_instance.post_users_me_password(body)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_me_password: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ChangeMyPasswordRequest**](ChangeMyPasswordRequest.html)| Password |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_users_search"></a>

## [**UsersSearchResponse**](UsersSearchResponse.html) post_users_search(body)



Search users



Wraps POST /api/v2/users/search 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.UserSearchRequest() # UserSearchRequest | Search request options

try:
    # Search users
    api_response = api_instance.post_users_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserSearchRequest**](UserSearchRequest.html)| Search request options |  |
{: class="table table-striped"}

### Return type

[**UsersSearchResponse**](UsersSearchResponse.html)

<a name="put_routing_user_utilization"></a>

## [**Utilization**](Utilization.html) put_routing_user_utilization(user_id, body)



Update the user's max utilization settings.  Include only those media types requiring custom configuration.



Wraps PUT /api/v2/routing/users/{userId}/utilization 

Requires ANY permissions: 

* routing:utilization:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.Utilization() # Utilization | utilization

try:
    # Update the user's max utilization settings.  Include only those media types requiring custom configuration.
    api_response = api_instance.put_routing_user_utilization(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_routing_user_utilization: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**Utilization**](Utilization.html)| utilization |  |
{: class="table table-striped"}

### Return type

[**Utilization**](Utilization.html)

<a name="put_user_callforwarding"></a>

## [**CallForwarding**](CallForwarding.html) put_user_callforwarding(user_id, body)



Update a user's CallForwarding



Wraps PUT /api/v2/users/{userId}/callforwarding 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.CallForwarding() # CallForwarding | Call forwarding

try:
    # Update a user's CallForwarding
    api_response = api_instance.put_user_callforwarding(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_user_callforwarding: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**CallForwarding**](CallForwarding.html)| Call forwarding |  |
{: class="table table-striped"}

### Return type

[**CallForwarding**](CallForwarding.html)

<a name="put_user_outofoffice"></a>

## [**OutOfOffice**](OutOfOffice.html) put_user_outofoffice(user_id, body)



Update an OutOfOffice



Wraps PUT /api/v2/users/{userId}/outofoffice 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.OutOfOffice() # OutOfOffice | The updated OutOffOffice

try:
    # Update an OutOfOffice
    api_response = api_instance.put_user_outofoffice(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_user_outofoffice: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**OutOfOffice**](OutOfOffice.html)| The updated OutOffOffice |  |
{: class="table table-striped"}

### Return type

[**OutOfOffice**](OutOfOffice.html)

<a name="put_user_profileskills"></a>

## list[str]** put_user_profileskills(user_id, body)



Update profile skills for a user



Wraps PUT /api/v2/users/{userId}/profileskills 

Requires ANY permissions: 

* directory:userProfile:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | Skills

try:
    # Update profile skills for a user
    api_response = api_instance.put_user_profileskills(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_user_profileskills: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | **list[str]**| Skills |  |
{: class="table table-striped"}

### Return type

**list[str]**

<a name="put_user_roles"></a>

## [**UserAuthorization**](UserAuthorization.html) put_user_roles(user_id, body)



Sets the user's roles



Wraps PUT /api/v2/users/{userId}/roles 

Requires ANY permissions: 

* authorization:grant:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | List of roles

try:
    # Sets the user's roles
    api_response = api_instance.put_user_roles(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_user_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | **list[str]**| List of roles |  |
{: class="table table-striped"}

### Return type

[**UserAuthorization**](UserAuthorization.html)

<a name="put_user_routingskill"></a>

## [**UserRoutingSkill**](UserRoutingSkill.html) put_user_routingskill(user_id, skill_id, body)



Update routing skill proficiency or state.



Wraps PUT /api/v2/users/{userId}/routingskills/{skillId} 

Requires ALL permissions: 

* routing:skill:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
skill_id = 'skill_id_example' # str | skillId
body = PureCloudPlatformClientV2.UserRoutingSkill() # UserRoutingSkill | Skill

try:
    # Update routing skill proficiency or state.
    api_response = api_instance.put_user_routingskill(user_id, skill_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_user_routingskill: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **skill_id** | **str**| skillId |  |
| **body** | [**UserRoutingSkill**](UserRoutingSkill.html)| Skill |  |
{: class="table table-striped"}

### Return type

[**UserRoutingSkill**](UserRoutingSkill.html)

<a name="put_user_routingskills_bulk"></a>

## [**UserSkillEntityListing**](UserSkillEntityListing.html) put_user_routingskills_bulk(user_id, body)



Replace all routing skills assigned to a user



Wraps PUT /api/v2/users/{userId}/routingskills/bulk 

Requires ANY permissions: 

* routing:skill:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = [PureCloudPlatformClientV2.UserRoutingSkillPost()] # list[UserRoutingSkillPost] | Skill

try:
    # Replace all routing skills assigned to a user
    api_response = api_instance.put_user_routingskills_bulk(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_user_routingskills_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserRoutingSkillPost]**](UserRoutingSkillPost.html)| Skill |  |
{: class="table table-striped"}

### Return type

[**UserSkillEntityListing**](UserSkillEntityListing.html)

<a name="put_user_routingstatus"></a>

## [**RoutingStatus**](RoutingStatus.html) put_user_routingstatus(user_id, body)



Update the routing status of a user



Wraps PUT /api/v2/users/{userId}/routingstatus 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.RoutingStatus() # RoutingStatus | Routing Status

try:
    # Update the routing status of a user
    api_response = api_instance.put_user_routingstatus(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_user_routingstatus: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**RoutingStatus**](RoutingStatus.html)| Routing Status |  |
{: class="table table-striped"}

### Return type

[**RoutingStatus**](RoutingStatus.html)

<a name="put_user_station_associatedstation_station_id"></a>

##  put_user_station_associatedstation_station_id(user_id, station_id)



Set associated station



Wraps PUT /api/v2/users/{userId}/station/associatedstation/{stationId} 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
station_id = 'station_id_example' # str | stationId

try:
    # Set associated station
    api_instance.put_user_station_associatedstation_station_id(user_id, station_id)
except ApiException as e:
    print("Exception when calling UsersApi->put_user_station_associatedstation_station_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **station_id** | **str**| stationId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="put_user_station_defaultstation_station_id"></a>

##  put_user_station_defaultstation_station_id(user_id, station_id)



Set default station



Wraps PUT /api/v2/users/{userId}/station/defaultstation/{stationId} 

Requires ANY permissions: 

* telephony:plugin:all
* telephony:phone:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
station_id = 'station_id_example' # str | stationId

try:
    # Set default station
    api_instance.put_user_station_defaultstation_station_id(user_id, station_id)
except ApiException as e:
    print("Exception when calling UsersApi->put_user_station_defaultstation_station_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **station_id** | **str**| stationId |  |
{: class="table table-striped"}

### Return type

void (empty response body)


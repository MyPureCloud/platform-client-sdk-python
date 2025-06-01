# UsersApi

## PureCloudPlatformClientV2.UsersApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_analytics_users_details_job**](#delete_analytics_users_details_job) | Delete/cancel an async request|
|[**delete_authorization_subject_division_role**](#delete_authorization_subject_division_role) | Delete a grant of a role in a division|
|[**delete_routing_directroutingbackup_settings_me**](#delete_routing_directroutingbackup_settings_me) | Delete the user&#39;s Direct Routing Backup settings and revert to the Direct Routing Queue default.|
|[**delete_routing_user_directroutingbackup_settings**](#delete_routing_user_directroutingbackup_settings) | Delete the user&#39;s Direct Routing Backup settings and revert to the Direct Routing Queue default.|
|[**delete_routing_user_utilization**](#delete_routing_user_utilization) | Delete the user&#39;s max utilization settings and revert to the organization-wide default.|
|[**delete_user**](#delete_user) | Delete user|
|[**delete_user_externalid_authority_name_external_key**](#delete_user_externalid_authority_name_external_key) | Delete the external identifier for user.|
|[**delete_user_routinglanguage**](#delete_user_routinglanguage) | Remove a routing language from a user|
|[**delete_user_routingskill**](#delete_user_routingskill) | Remove a routing skill from a user|
|[**delete_user_station_associatedstation**](#delete_user_station_associatedstation) | Clear associated station|
|[**delete_user_station_defaultstation**](#delete_user_station_defaultstation) | Clear default station|
|[**delete_user_verifier**](#delete_user_verifier) | Delete a verifier|
|[**get_analytics_users_aggregates_job**](#get_analytics_users_aggregates_job) | Get status for async query for user aggregates|
|[**get_analytics_users_aggregates_job_results**](#get_analytics_users_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_users_details_job**](#get_analytics_users_details_job) | Get status for async query for user details|
|[**get_analytics_users_details_job_results**](#get_analytics_users_details_job_results) | Fetch a page of results for an async query|
|[**get_analytics_users_details_jobs_availability**](#get_analytics_users_details_jobs_availability) | Lookup the datalake availability date and time|
|[**get_authorization_divisionspermitted_me**](#get_authorization_divisionspermitted_me) | Returns which divisions the current user has the given permission in.|
|[**get_authorization_divisionspermitted_paged_me**](#get_authorization_divisionspermitted_paged_me) | Returns which divisions the current user has the given permission in.|
|[**get_authorization_divisionspermitted_paged_subject_id**](#get_authorization_divisionspermitted_paged_subject_id) | Returns which divisions the specified user has the given permission in.|
|[**get_authorization_subject**](#get_authorization_subject) | Returns a listing of roles and permissions for a user.|
|[**get_authorization_subjects_me**](#get_authorization_subjects_me) | Returns a listing of roles and permissions for the currently authenticated user.|
|[**get_fieldconfig**](#get_fieldconfig) | Fetch field config for an entity type|
|[**get_profiles_users**](#get_profiles_users) | Get a user profile listing|
|[**get_routing_directroutingbackup_settings_me**](#get_routing_directroutingbackup_settings_me) | Get the user&#39;s Direct Routing Backup settings.|
|[**get_routing_user_directroutingbackup_settings**](#get_routing_user_directroutingbackup_settings) | Get the user&#39;s Direct Routing Backup settings.|
|[**get_routing_user_utilization**](#get_routing_user_utilization) | Get the user&#39;s max utilization settings.  If not configured, the organization-wide default is returned.|
|[**get_user**](#get_user) | Get user.|
|[**get_user_adjacents**](#get_user_adjacents) | Get adjacents|
|[**get_user_callforwarding**](#get_user_callforwarding) | Get a user&#39;s CallForwarding|
|[**get_user_directreports**](#get_user_directreports) | Get direct reports|
|[**get_user_externalid**](#get_user_externalid) | Get the external identifiers for a user.|
|[**get_user_externalid_authority_name**](#get_user_externalid_authority_name) | Get the external identifier of user for an authority.|
|[**get_user_favorites**](#get_user_favorites) | Deprecated; will be revived with new contract|
|[**get_user_geolocation**](#get_user_geolocation) | Get a user&#39;s Geolocation|
|[**get_user_outofoffice**](#get_user_outofoffice) | Get a OutOfOffice|
|[**get_user_profile**](#get_user_profile) | Get user profile|
|[**get_user_profileskills**](#get_user_profileskills) | List profile skills for a user|
|[**get_user_queues**](#get_user_queues) | Get queues for user|
|[**get_user_roles**](#get_user_roles) | Returns a listing of roles and permissions for a user.|
|[**get_user_routinglanguages**](#get_user_routinglanguages) | List routing languages assigned to a user|
|[**get_user_routingskills**](#get_user_routingskills) | List routing skills assigned to a user|
|[**get_user_routingstatus**](#get_user_routingstatus) | Fetch the routing status of a user|
|[**get_user_skillgroups**](#get_user_skillgroups) | Get skill groups for a user|
|[**get_user_state**](#get_user_state) | Get user state information.|
|[**get_user_station**](#get_user_station) | Get station information for user|
|[**get_user_superiors**](#get_user_superiors) | Get superiors|
|[**get_user_trustors**](#get_user_trustors) | List the organizations that have authorized/trusted the user.|
|[**get_user_verifiers**](#get_user_verifiers) | Get a list of verifiers|
|[**get_users**](#get_users) | Get the list of available users.|
|[**get_users_chats_me**](#get_users_chats_me) | Get chats for a user|
|[**get_users_development_activities**](#get_users_development_activities) | Get list of Development Activities|
|[**get_users_development_activities_me**](#get_users_development_activities_me) | Get list of Development Activities for current user|
|[**get_users_development_activity**](#get_users_development_activity) | Get a Development Activity|
|[**get_users_externalid_authority_name_external_key**](#get_users_externalid_authority_name_external_key) | Get the user associated with external identifier.|
|[**get_users_me**](#get_users_me) | Get current user details.|
|[**get_users_search**](#get_users_search) | Search users using the q64 value returned from a previous search|
|[**patch_user**](#patch_user) | Update user|
|[**patch_user_callforwarding**](#patch_user_callforwarding) | Patch a user&#39;s CallForwarding|
|[**patch_user_geolocation**](#patch_user_geolocation) | Patch a user&#39;s Geolocation|
|[**patch_user_queue**](#patch_user_queue) | Join or unjoin a queue for a user|
|[**patch_user_queues**](#patch_user_queues) | Join or unjoin a set of queues for a user|
|[**patch_user_routinglanguage**](#patch_user_routinglanguage) | Update an assigned routing language&#39;s proficiency|
|[**patch_user_routinglanguages_bulk**](#patch_user_routinglanguages_bulk) | Assign multiple routing languages to a user. Max 50 routing languages in request body|
|[**patch_user_routingskills_bulk**](#patch_user_routingskills_bulk) | Assign multiple routing skills to a user|
|[**patch_users_bulk**](#patch_users_bulk) | Update bulk acd autoanswer on users. Max 50 users can be updated at a time.|
|[**post_analytics_users_activity_query**](#post_analytics_users_activity_query) | Query for user activity observations|
|[**post_analytics_users_aggregates_jobs**](#post_analytics_users_aggregates_jobs) | Query for user aggregates asynchronously|
|[**post_analytics_users_aggregates_query**](#post_analytics_users_aggregates_query) | Query for user aggregates|
|[**post_analytics_users_details_jobs**](#post_analytics_users_details_jobs) | Query for user details asynchronously|
|[**post_analytics_users_details_query**](#post_analytics_users_details_query) | Query for user details|
|[**post_analytics_users_observations_query**](#post_analytics_users_observations_query) | Query for user observations|
|[**post_authorization_subject_bulkadd**](#post_authorization_subject_bulkadd) | Bulk-grant roles and divisions to a subject.|
|[**post_authorization_subject_bulkremove**](#post_authorization_subject_bulkremove) | Bulk-remove grants from a subject.|
|[**post_authorization_subject_bulkreplace**](#post_authorization_subject_bulkreplace) | Replace subject&#39;s roles and divisions with the exact list supplied in the request.|
|[**post_authorization_subject_division_role**](#post_authorization_subject_division_role) | Make a grant of a role in a division|
|[**post_user_externalid**](#post_user_externalid) | Create mapping between external identifier and user. Limit 100 per entity.|
|[**post_user_invite**](#post_user_invite) | Send an activation email to the user|
|[**post_user_password**](#post_user_password) | Change a users password|
|[**post_user_routinglanguages**](#post_user_routinglanguages) | Assign a routing language to a user|
|[**post_user_routingskills**](#post_user_routingskills) | Assign a routing skill to a user|
|[**post_users**](#post_users) | Create user|
|[**post_users_development_activities_aggregates_query**](#post_users_development_activities_aggregates_query) | Retrieve aggregated development activity data|
|[**post_users_me_password**](#post_users_me_password) | Change your password|
|[**post_users_search**](#post_users_search) | Search users|
|[**post_users_search_conversation_target**](#post_users_search_conversation_target) | Search users as conversation targets|
|[**post_users_search_queuemembers_manage**](#post_users_search_queuemembers_manage) | Search manage queue member|
|[**post_users_search_teams_assign**](#post_users_search_teams_assign) | Search users assigned to teams|
|[**put_routing_directroutingbackup_settings_me**](#put_routing_directroutingbackup_settings_me) | Update the user&#39;s Direct Routing Backup settings.|
|[**put_routing_user_directroutingbackup_settings**](#put_routing_user_directroutingbackup_settings) | Update the user&#39;s Direct Routing Backup settings.|
|[**put_routing_user_utilization**](#put_routing_user_utilization) | Update the user&#39;s max utilization settings.  Include only those media types requiring custom configuration.|
|[**put_user_callforwarding**](#put_user_callforwarding) | Update a user&#39;s CallForwarding|
|[**put_user_outofoffice**](#put_user_outofoffice) | Update an OutOfOffice|
|[**put_user_profileskills**](#put_user_profileskills) | Update profile skills for a user|
|[**put_user_roles**](#put_user_roles) | Sets the user&#39;s roles|
|[**put_user_routingskill**](#put_user_routingskill) | Update an assigned routing skill&#39;s proficiency|
|[**put_user_routingskills_bulk**](#put_user_routingskills_bulk) | Assign multiple routing skills to a user, replacing any current assignments|
|[**put_user_routingstatus**](#put_user_routingstatus) | Update the routing status of a user|
|[**put_user_state**](#put_user_state) | Update user state information.|
|[**put_user_station_associatedstation_station_id**](#put_user_station_associatedstation_station_id) | Set associated station|
|[**put_user_station_defaultstation_station_id**](#put_user_station_defaultstation_station_id) | Set default station|
|[**put_user_verifier**](#put_user_verifier) | Update a verifier|



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

### Return type

void (empty response body)


## delete_authorization_subject_division_role

>  delete_authorization_subject_division_role(subject_id, division_id, role_id)


Delete a grant of a role in a division

Wraps DELETE /api/v2/authorization/subjects/{subjectId}/divisions/{divisionId}/roles/{roleId} 

Requires ALL permissions: 

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

### Return type

void (empty response body)


## delete_routing_directroutingbackup_settings_me

>  delete_routing_directroutingbackup_settings_me()


Delete the user's Direct Routing Backup settings and revert to the Direct Routing Queue default.

Wraps DELETE /api/v2/routing/directroutingbackup/settings/me 

Requires ANY permissions: 

* routing:directRoutingBackup:selfDelete

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
    # Delete the user's Direct Routing Backup settings and revert to the Direct Routing Queue default.
    api_instance.delete_routing_directroutingbackup_settings_me()
except ApiException as e:
    print("Exception when calling UsersApi->delete_routing_directroutingbackup_settings_me: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

void (empty response body)


## delete_routing_user_directroutingbackup_settings

>  delete_routing_user_directroutingbackup_settings(user_id)


Delete the user's Direct Routing Backup settings and revert to the Direct Routing Queue default.

Wraps DELETE /api/v2/routing/users/{userId}/directroutingbackup/settings 

Requires ANY permissions: 

* routing:directRoutingBackup:delete

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
    # Delete the user's Direct Routing Backup settings and revert to the Direct Routing Queue default.
    api_instance.delete_routing_user_directroutingbackup_settings(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_routing_user_directroutingbackup_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |

### Return type

void (empty response body)


## delete_routing_user_utilization

>  delete_routing_user_utilization(user_id)


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

### Return type

void (empty response body)


## delete_user

> object** delete_user(user_id)


Delete user

Wraps DELETE /api/v2/users/{userId} 

Requires ANY permissions: 

* admin
* directory:user:delete
* directory:organization:admin

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

### Return type

**object**


## delete_user_externalid_authority_name_external_key

>  delete_user_externalid_authority_name_external_key(user_id, authority_name, external_key)


Delete the external identifier for user.

Wraps DELETE /api/v2/users/{userId}/externalid/{authorityName}/{externalKey} 

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
authority_name = 'authority_name_example' # str | Authority Name
external_key = 'external_key_example' # str | External Key

try:
    # Delete the external identifier for user.
    api_instance.delete_user_externalid_authority_name_external_key(user_id, authority_name, external_key)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_externalid_authority_name_external_key: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **authority_name** | **str**| Authority Name |  |
| **external_key** | **str**| External Key |  |

### Return type

void (empty response body)


## delete_user_routinglanguage

>  delete_user_routinglanguage(user_id, language_id)


Remove a routing language from a user

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
    # Remove a routing language from a user
    api_instance.delete_user_routinglanguage(user_id, language_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_routinglanguage: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **language_id** | **str**| languageId |  |

### Return type

void (empty response body)


## delete_user_routingskill

>  delete_user_routingskill(user_id, skill_id)


Remove a routing skill from a user

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
    # Remove a routing skill from a user
    api_instance.delete_user_routingskill(user_id, skill_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_routingskill: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **skill_id** | **str**| skillId |  |

### Return type

void (empty response body)


## delete_user_station_associatedstation

>  delete_user_station_associatedstation(user_id)


Clear associated station

Wraps DELETE /api/v2/users/{userId}/station/associatedstation 

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

### Return type

void (empty response body)


## delete_user_station_defaultstation

>  delete_user_station_defaultstation(user_id)


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

### Return type

void (empty response body)


## delete_user_verifier

>  delete_user_verifier(user_id, verifier_id)


Delete a verifier

Wraps DELETE /api/v2/users/{userId}/verifiers/{verifierId} 

Requires ANY permissions: 

* mfa:verifier:delete

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
verifier_id = 'verifier_id_example' # str | Verifier ID

try:
    # Delete a verifier
    api_instance.delete_user_verifier(user_id, verifier_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_verifier: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **verifier_id** | **str**| Verifier ID |  |

### Return type

void (empty response body)


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
api_instance = PureCloudPlatformClientV2.UsersApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for user aggregates
    api_response = api_instance.get_analytics_users_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_analytics_users_aggregates_job: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.UsersApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_users_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_analytics_users_aggregates_job_results: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.UsersApi()

try:
    # Lookup the datalake availability date and time
    api_response = api_instance.get_analytics_users_details_jobs_availability()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_analytics_users_details_jobs_availability: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**DataAvailabilityResponse**](DataAvailabilityResponse)


## get_authorization_divisionspermitted_me

> [**list[AuthzDivision]**](AuthzDivision) get_authorization_divisionspermitted_me(permission, name=name)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Returns which divisions the current user has the given permission in.

This route is deprecated, use authorization/divisionspermitted/paged/me instead.

Wraps GET /api/v2/authorization/divisionspermitted/me 

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

### Return type

[**list[AuthzDivision]**](AuthzDivision)


## get_authorization_divisionspermitted_paged_me

> [**DivsPermittedEntityListing**](DivsPermittedEntityListing) get_authorization_divisionspermitted_paged_me(permission, page_number=page_number, page_size=page_size)


Returns which divisions the current user has the given permission in.

Wraps GET /api/v2/authorization/divisionspermitted/paged/me 

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

### Return type

[**DivsPermittedEntityListing**](DivsPermittedEntityListing)


## get_authorization_divisionspermitted_paged_subject_id

> [**DivsPermittedEntityListing**](DivsPermittedEntityListing) get_authorization_divisionspermitted_paged_subject_id(subject_id, permission, page_number=page_number, page_size=page_size)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Returns which divisions the specified user has the given permission in.

This route is deprecated, use authorization/divisionspermitted/paged/me instead.

Wraps GET /api/v2/authorization/divisionspermitted/paged/{subjectId} 

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

### Return type

[**DivsPermittedEntityListing**](DivsPermittedEntityListing)


## get_authorization_subject

> [**AuthzSubject**](AuthzSubject) get_authorization_subject(subject_id, include_duplicates=include_duplicates)


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
include_duplicates = False # bool | Include multiple entries with the same role and division but different subjects (optional) (default to False)

try:
    # Returns a listing of roles and permissions for a user.
    api_response = api_instance.get_authorization_subject(subject_id, include_duplicates=include_duplicates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_authorization_subject: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **subject_id** | **str**| Subject ID (user or group) |  |
| **include_duplicates** | **bool**| Include multiple entries with the same role and division but different subjects | [optional] [default to False]<br />**Values**: true, false |

### Return type

[**AuthzSubject**](AuthzSubject)


## get_authorization_subjects_me

> [**AuthzSubject**](AuthzSubject) get_authorization_subjects_me(include_duplicates=include_duplicates)


Returns a listing of roles and permissions for the currently authenticated user.

Wraps GET /api/v2/authorization/subjects/me 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
include_duplicates = False # bool | Include multiple entries with the same role and division but different subjects (optional) (default to False)

try:
    # Returns a listing of roles and permissions for the currently authenticated user.
    api_response = api_instance.get_authorization_subjects_me(include_duplicates=include_duplicates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_authorization_subjects_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **include_duplicates** | **bool**| Include multiple entries with the same role and division but different subjects | [optional] [default to False]<br />**Values**: true, false |

### Return type

[**AuthzSubject**](AuthzSubject)


## get_fieldconfig

> [**FieldConfig**](FieldConfig) get_fieldconfig(type)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Fetch field config for an entity type

Wraps GET /api/v2/fieldconfig 

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
| **type** | **str**| Field type | <br />**Values**: person, group, org |

### Return type

[**FieldConfig**](FieldConfig)


## get_profiles_users

> [**UserProfileEntityListing**](UserProfileEntityListing) get_profiles_users(page_size=page_size, page_number=page_number, id=id, jid=jid, sort_order=sort_order, expand=expand, integration_presence_source=integration_presence_source)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get a user profile listing

This api is deprecated. User /api/v2/users

Wraps GET /api/v2/profiles/users 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
id = ['id_example'] # list[str] | id (optional)
jid = ['jid_example'] # list[str] | jid (optional)
sort_order = ''ASC'' # str | Ascending or descending sort order (optional) (default to 'ASC')
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
| **id** | [**list[str]**](str)| id | [optional]  |
| **jid** | [**list[str]**](str)| jid | [optional]  |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;ASC&#39;]<br />**Values**: ascending, descending |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization |
| **integration_presence_source** | **str**| Gets an integration presence for users instead of their defaults. This parameter will only be used when presence is provided as an \&quot;expand\&quot;. | [optional] <br />**Values**: MicrosoftTeams, ZoomPhone, EightByEight |

### Return type

[**UserProfileEntityListing**](UserProfileEntityListing)


## get_routing_directroutingbackup_settings_me

> [**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings) get_routing_directroutingbackup_settings_me()


Get the user's Direct Routing Backup settings.

Wraps GET /api/v2/routing/directroutingbackup/settings/me 

Requires ANY permissions: 

* routing:directRoutingBackup:selfView

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
    # Get the user's Direct Routing Backup settings.
    api_response = api_instance.get_routing_directroutingbackup_settings_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_routing_directroutingbackup_settings_me: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings)


## get_routing_user_directroutingbackup_settings

> [**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings) get_routing_user_directroutingbackup_settings(user_id)


Get the user's Direct Routing Backup settings.

Wraps GET /api/v2/routing/users/{userId}/directroutingbackup/settings 

Requires ANY permissions: 

* routing:directRoutingBackup:view

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
    # Get the user's Direct Routing Backup settings.
    api_response = api_instance.get_routing_user_directroutingbackup_settings(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_routing_user_directroutingbackup_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |

### Return type

[**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings)


## get_routing_user_utilization

> [**AgentMaxUtilizationResponse**](AgentMaxUtilizationResponse) get_routing_user_utilization(user_id)


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

### Return type

[**AgentMaxUtilizationResponse**](AgentMaxUtilizationResponse)


## get_user

> [**User**](User) get_user(user_id, expand=expand, integration_presence_source=integration_presence_source, state=state)


Get user.

Wraps GET /api/v2/users/{userId} 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. Note, expand parameters are resolved with a best effort approach and not guaranteed to be returned. If requested expand information is absolutely required, it's recommended to use specific API requests instead. (optional)
integration_presence_source = 'integration_presence_source_example' # str | Gets an integration presence for a user instead of their default. (optional)
state = ''active'' # str | Search for a user with this state (optional) (default to 'active')

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
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. Note, expand parameters are resolved with a best effort approach and not guaranteed to be returned. If requested expand information is absolutely required, it&#39;s recommended to use specific API requests instead. | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, dateLastLogin, dateWelcomeSent |
| **integration_presence_source** | **str**| Gets an integration presence for a user instead of their default. | [optional] <br />**Values**: MicrosoftTeams, ZoomPhone, EightByEight |
| **state** | **str**| Search for a user with this state | [optional] [default to &#39;active&#39;]<br />**Values**: active, deleted |

### Return type

[**User**](User)


## get_user_adjacents

> [**Adjacents**](Adjacents) get_user_adjacents(user_id, expand=expand)


Get adjacents

Wraps GET /api/v2/users/{userId}/adjacents 

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
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, dateLastLogin, dateWelcomeSent |

### Return type

[**Adjacents**](Adjacents)


## get_user_callforwarding

> [**CallForwarding**](CallForwarding) get_user_callforwarding(user_id)


Get a user's CallForwarding

Wraps GET /api/v2/users/{userId}/callforwarding 

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

### Return type

[**CallForwarding**](CallForwarding)


## get_user_directreports

> [**list[User]**](User) get_user_directreports(user_id, expand=expand)


Get direct reports

Wraps GET /api/v2/users/{userId}/directreports 

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
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, dateLastLogin, dateWelcomeSent |

### Return type

[**list[User]**](User)


## get_user_externalid

> [**list[UserExternalIdentifier]**](UserExternalIdentifier) get_user_externalid(user_id)


Get the external identifiers for a user.

Wraps GET /api/v2/users/{userId}/externalid 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Get the external identifiers for a user.
    api_response = api_instance.get_user_externalid(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_externalid: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |

### Return type

[**list[UserExternalIdentifier]**](UserExternalIdentifier)


## get_user_externalid_authority_name

> [**UserExternalIdentifier**](UserExternalIdentifier) get_user_externalid_authority_name(user_id, authority_name)


Get the external identifier of user for an authority.

Authority name and external key are case sensitive.

Wraps GET /api/v2/users/{userId}/externalid/{authorityName} 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
authority_name = 'authority_name_example' # str | Authority Name

try:
    # Get the external identifier of user for an authority.
    api_response = api_instance.get_user_externalid_authority_name(user_id, authority_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_externalid_authority_name: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **authority_name** | **str**| Authority Name |  |

### Return type

[**UserExternalIdentifier**](UserExternalIdentifier)


## get_user_favorites

> [**UserEntityListing**](UserEntityListing) get_user_favorites(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Deprecated; will be revived with new contract

Wraps GET /api/v2/users/{userId}/favorites 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''ASC'' # str | Sort order (optional) (default to 'ASC')
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Deprecated; will be revived with new contract
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
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ASC&#39;] |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, dateLastLogin, dateWelcomeSent |

### Return type

[**UserEntityListing**](UserEntityListing)


## get_user_geolocation

> [**Geolocation**](Geolocation) get_user_geolocation(user_id, client_id)


Get a user's Geolocation

Wraps GET /api/v2/users/{userId}/geolocations/{clientId} 

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

### Return type

[**Geolocation**](Geolocation)


## get_user_outofoffice

> [**OutOfOffice**](OutOfOffice) get_user_outofoffice(user_id)


Get a OutOfOffice

Wraps GET /api/v2/users/{userId}/outofoffice 

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

### Return type

[**OutOfOffice**](OutOfOffice)


## get_user_profile

> [**UserProfile**](UserProfile) get_user_profile(user_id, expand=expand, integration_presence_source=integration_presence_source)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get user profile

This api has been deprecated. Use api/v2/users instead

Wraps GET /api/v2/users/{userId}/profile 

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
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings |
| **integration_presence_source** | **str**| Gets an integration presence for a user instead of their default. | [optional] <br />**Values**: MicrosoftTeams, ZoomPhone, EightByEight |

### Return type

[**UserProfile**](UserProfile)


## get_user_profileskills

> list[str]** get_user_profileskills(user_id)


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

### Return type

**list[str]**


## get_user_queues

> [**UserQueueEntityListing**](UserQueueEntityListing) get_user_queues(user_id, page_size=page_size, page_number=page_number, joined=joined, division_id=division_id)


Get queues for user

Wraps GET /api/v2/users/{userId}/queues 

Requires ANY permissions: 

* routing:queue:view

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
joined = True # bool | Is joined to the queue (optional) (default to True)
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
| **joined** | **bool**| Is joined to the queue | [optional] [default to True] |
| **division_id** | [**list[str]**](str)| Division ID(s) | [optional]  |

### Return type

[**UserQueueEntityListing**](UserQueueEntityListing)


## get_user_roles

> [**UserAuthorization**](UserAuthorization) get_user_roles(subject_id)


Returns a listing of roles and permissions for a user.

Wraps GET /api/v2/users/{subjectId}/roles 

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
subject_id = 'subject_id_example' # str | User ID

try:
    # Returns a listing of roles and permissions for a user.
    api_response = api_instance.get_user_roles(subject_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **subject_id** | **str**| User ID |  |

### Return type

[**UserAuthorization**](UserAuthorization)


## get_user_routinglanguages

> [**UserLanguageEntityListing**](UserLanguageEntityListing) get_user_routinglanguages(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)


List routing languages assigned to a user

Wraps GET /api/v2/users/{userId}/routinglanguages 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''ASC'' # str | Ascending or descending sort order (optional) (default to 'ASC')

try:
    # List routing languages assigned to a user
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
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;ASC&#39;]<br />**Values**: ascending, descending |

### Return type

[**UserLanguageEntityListing**](UserLanguageEntityListing)


## get_user_routingskills

> [**UserSkillEntityListing**](UserSkillEntityListing) get_user_routingskills(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)


List routing skills assigned to a user

Wraps GET /api/v2/users/{userId}/routingskills 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''ASC'' # str | Ascending or descending sort order (optional) (default to 'ASC')

try:
    # List routing skills assigned to a user
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
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;ASC&#39;]<br />**Values**: ascending, descending |

### Return type

[**UserSkillEntityListing**](UserSkillEntityListing)


## get_user_routingstatus

> [**RoutingStatus**](RoutingStatus) get_user_routingstatus(user_id)


Fetch the routing status of a user

Wraps GET /api/v2/users/{userId}/routingstatus 

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

### Return type

[**RoutingStatus**](RoutingStatus)


## get_user_skillgroups

> [**UserSkillGroupEntityListing**](UserSkillGroupEntityListing) get_user_skillgroups(user_id, page_size=page_size, after=after, before=before)


Get skill groups for a user

Wraps GET /api/v2/users/{userId}/skillgroups 

Requires ANY permissions: 

* routing:skillGroup:view

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
after = 'after_example' # str | The cursor that points to the next page (optional)
before = 'before_example' # str | The cursor that points to the previous page (optional)

try:
    # Get skill groups for a user
    api_response = api_instance.get_user_skillgroups(user_id, page_size=page_size, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_skillgroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **after** | **str**| The cursor that points to the next page | [optional]  |
| **before** | **str**| The cursor that points to the previous page | [optional]  |

### Return type

[**UserSkillGroupEntityListing**](UserSkillGroupEntityListing)


## get_user_state

> [**UserState**](UserState) get_user_state(user_id)


Get user state information.

Wraps GET /api/v2/users/{userId}/state 

Requires ANY permissions: 

* directory:userStateChange:view

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
    # Get user state information.
    api_response = api_instance.get_user_state(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_state: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |

### Return type

[**UserState**](UserState)


## get_user_station

> [**UserStations**](UserStations) get_user_station(user_id)


Get station information for user

Wraps GET /api/v2/users/{userId}/station 

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

### Return type

[**UserStations**](UserStations)


## get_user_superiors

> [**list[User]**](User) get_user_superiors(user_id, expand=expand)


Get superiors

Wraps GET /api/v2/users/{userId}/superiors 

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
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, dateLastLogin, dateWelcomeSent |

### Return type

[**list[User]**](User)


## get_user_trustors

> [**TrustorEntityListing**](TrustorEntityListing) get_user_trustors(user_id, page_size=page_size, page_number=page_number)


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

### Return type

[**TrustorEntityListing**](TrustorEntityListing)


## get_user_verifiers

> [**VerifierEntityListing**](VerifierEntityListing) get_user_verifiers(user_id)


Get a list of verifiers

Wraps GET /api/v2/users/{userId}/verifiers 

Requires ANY permissions: 

* mfa:verifier:view

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
    # Get a list of verifiers
    api_response = api_instance.get_user_verifiers(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_verifiers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |

### Return type

[**VerifierEntityListing**](VerifierEntityListing)


## get_users

> [**UserEntityListing**](UserEntityListing) get_users(page_size=page_size, page_number=page_number, id=id, jabber_id=jabber_id, sort_order=sort_order, expand=expand, integration_presence_source=integration_presence_source, state=state)


Get the list of available users.

Wraps GET /api/v2/users 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
id = ['id_example'] # list[str] | A list of user IDs to fetch by bulk (optional)
jabber_id = ['jabber_id_example'] # list[str] | A list of jabberIds to fetch by bulk (cannot be used with the \"id\" parameter) (optional)
sort_order = ''ASC'' # str | Ascending or descending sort order (optional) (default to 'ASC')
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. Note, expand parameters are resolved with a best effort approach and not guaranteed to be returned. If requested expand information is absolutely required, it's recommended to use specific API requests instead. (optional)
integration_presence_source = 'integration_presence_source_example' # str | Gets an integration presence for users instead of their defaults. This parameter will only be used when presence is provided as an \"expand\". When using this parameter the maximum number of users that can be returned is 100. (optional)
state = ''active'' # str | Only list users of this state (optional) (default to 'active')

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
| **id** | [**list[str]**](str)| A list of user IDs to fetch by bulk | [optional]  |
| **jabber_id** | [**list[str]**](str)| A list of jabberIds to fetch by bulk (cannot be used with the \&quot;id\&quot; parameter) | [optional]  |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;ASC&#39;]<br />**Values**: ascending, descending |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. Note, expand parameters are resolved with a best effort approach and not guaranteed to be returned. If requested expand information is absolutely required, it&#39;s recommended to use specific API requests instead. | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, dateLastLogin, dateWelcomeSent |
| **integration_presence_source** | **str**| Gets an integration presence for users instead of their defaults. This parameter will only be used when presence is provided as an \&quot;expand\&quot;. When using this parameter the maximum number of users that can be returned is 100. | [optional] <br />**Values**: MicrosoftTeams, ZoomPhone, EightByEight |
| **state** | **str**| Only list users of this state | [optional] [default to &#39;active&#39;]<br />**Values**: active, inactive, deleted, any |

### Return type

[**UserEntityListing**](UserEntityListing)


## get_users_chats_me

> [**ChatItemCursorListing**](ChatItemCursorListing) get_users_chats_me(exclude_closed=exclude_closed, include_presence=include_presence, after=after)


Get chats for a user

Wraps GET /api/v2/users/chats/me 

Requires ANY permissions: 

* chat:chat:access
* user:chats:view

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
exclude_closed = True # bool | Whether or not to exclude closed chats (optional)
include_presence = True # bool | Whether or not to include user presence (optional)
after = 'after_example' # str | The key to start after (optional)

try:
    # Get chats for a user
    api_response = api_instance.get_users_chats_me(exclude_closed=exclude_closed, include_presence=include_presence, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_chats_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **exclude_closed** | **bool**| Whether or not to exclude closed chats | [optional]  |
| **include_presence** | **bool**| Whether or not to include user presence | [optional]  |
| **after** | **str**| The key to start after | [optional]  |

### Return type

[**ChatItemCursorListing**](ChatItemCursorListing)


## get_users_development_activities

> [**DevelopmentActivityListing**](DevelopmentActivityListing) get_users_development_activities(user_id=user_id, module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, pcPass=pcPass, page_size=page_size, page_number=page_number, sort_order=sort_order, types=types, statuses=statuses, relationship=relationship)


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
overdue = ''Any'' # str | Specifies if non-overdue, overdue, or all activities are returned. If not specified, all activities are returned (optional) (default to 'Any')
pcPass = ''Any'' # str | Specifies if only the failed (pass is \"False\") or passed (pass is \"True\") activities are returned. If pass is \"Any\" or if the pass parameter is not supplied, all activities are returned (optional) (default to 'Any')
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''Desc'' # str | Specifies result set sort order sorted by the date due; if not specified, default sort order is descending (Desc) (optional) (default to 'Desc')
types = ['types_example'] # list[str] | Specifies the activity types. Informational, AssessedContent and Assessment are deprecated (optional)
statuses = ['statuses_example'] # list[str] | Specifies the activity statuses to filter by (optional)
relationship = ['relationship_example'] # list[str] | Specifies how the current user relation should be interpreted, and filters the activities returned to only the activities that have the specified relationship. If a value besides Attendee is specified, it will only return Coaching Appointments. If not specified, no filtering is applied. (optional)

try:
    # Get list of Development Activities
    api_response = api_instance.get_users_development_activities(user_id=user_id, module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, pcPass=pcPass, page_size=page_size, page_number=page_number, sort_order=sort_order, types=types, statuses=statuses, relationship=relationship)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_development_activities: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | [**list[str]**](str)| Specifies the list of user IDs to be queried, up to 100 user IDs. It searches for any relationship for the userId. | [optional]  |
| **module_id** | **str**| Specifies the ID of the learning module. | [optional]  |
| **interval** | **str**| Specifies the dateDue range to be queried. Milliseconds will be truncated. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **completion_interval** | **str**| Specifies the range of completion dates to be used for filtering. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional]  |
| **overdue** | **str**| Specifies if non-overdue, overdue, or all activities are returned. If not specified, all activities are returned | [optional] [default to &#39;Any&#39;]<br />**Values**: True, False, Any |
| **pcPass** | **str**| Specifies if only the failed (pass is \&quot;False\&quot;) or passed (pass is \&quot;True\&quot;) activities are returned. If pass is \&quot;Any\&quot; or if the pass parameter is not supplied, all activities are returned | [optional] [default to &#39;Any&#39;]<br />**Values**: True, False, Any |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Specifies result set sort order sorted by the date due; if not specified, default sort order is descending (Desc) | [optional] [default to &#39;Desc&#39;]<br />**Values**: Asc, Desc |
| **types** | [**list[str]**](str)| Specifies the activity types. Informational, AssessedContent and Assessment are deprecated | [optional] <br />**Values**: Informational, Coaching, AssessedContent, Assessment, External, Native |
| **statuses** | [**list[str]**](str)| Specifies the activity statuses to filter by | [optional] <br />**Values**: Planned, InProgress, Completed, InvalidSchedule, NotCompleted |
| **relationship** | [**list[str]**](str)| Specifies how the current user relation should be interpreted, and filters the activities returned to only the activities that have the specified relationship. If a value besides Attendee is specified, it will only return Coaching Appointments. If not specified, no filtering is applied. | [optional] <br />**Values**: Creator, Facilitator, Attendee |

### Return type

[**DevelopmentActivityListing**](DevelopmentActivityListing)


## get_users_development_activities_me

> [**DevelopmentActivityListing**](DevelopmentActivityListing) get_users_development_activities_me(module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, pcPass=pcPass, page_size=page_size, page_number=page_number, sort_order=sort_order, types=types, statuses=statuses, relationship=relationship)


Get list of Development Activities for current user

Results are filtered based on the applicable permissions.

Wraps GET /api/v2/users/development/activities/me 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
module_id = 'module_id_example' # str | Specifies the ID of the learning module. (optional)
interval = 'interval_example' # str | Specifies the dateDue range to be queried. Milliseconds will be truncated. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
completion_interval = 'completion_interval_example' # str | Specifies the range of completion dates to be used for filtering. A maximum of 1 year can be specified in the range. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss (optional)
overdue = ''Any'' # str | Specifies if non-overdue, overdue, or all activities are returned. If not specified, all activities are returned (optional) (default to 'Any')
pcPass = ''Any'' # str | Specifies if only the failed (pass is \"False\") or passed (pass is \"True\") activities are returned. If pass is \"Any\" or if the pass parameter is not supplied, all activities are returned (optional) (default to 'Any')
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''Desc'' # str | Specifies result set sort order sorted by the date due; if not specified, default sort order is descending (Desc) (optional) (default to 'Desc')
types = ['types_example'] # list[str] | Specifies the activity types. Informational, AssessedContent and Assessment are deprecated (optional)
statuses = ['statuses_example'] # list[str] | Specifies the activity statuses to filter by (optional)
relationship = ['relationship_example'] # list[str] | Specifies how the current user relation should be interpreted, and filters the activities returned to only the activities that have the specified relationship. If a value besides Attendee is specified, it will only return Coaching Appointments. If not specified, no filtering is applied. (optional)

try:
    # Get list of Development Activities for current user
    api_response = api_instance.get_users_development_activities_me(module_id=module_id, interval=interval, completion_interval=completion_interval, overdue=overdue, pcPass=pcPass, page_size=page_size, page_number=page_number, sort_order=sort_order, types=types, statuses=statuses, relationship=relationship)
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
| **overdue** | **str**| Specifies if non-overdue, overdue, or all activities are returned. If not specified, all activities are returned | [optional] [default to &#39;Any&#39;]<br />**Values**: True, False, Any |
| **pcPass** | **str**| Specifies if only the failed (pass is \&quot;False\&quot;) or passed (pass is \&quot;True\&quot;) activities are returned. If pass is \&quot;Any\&quot; or if the pass parameter is not supplied, all activities are returned | [optional] [default to &#39;Any&#39;]<br />**Values**: True, False, Any |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Specifies result set sort order sorted by the date due; if not specified, default sort order is descending (Desc) | [optional] [default to &#39;Desc&#39;]<br />**Values**: Asc, Desc |
| **types** | [**list[str]**](str)| Specifies the activity types. Informational, AssessedContent and Assessment are deprecated | [optional] <br />**Values**: Informational, Coaching, AssessedContent, Assessment, External, Native |
| **statuses** | [**list[str]**](str)| Specifies the activity statuses to filter by | [optional] <br />**Values**: Planned, InProgress, Completed, InvalidSchedule, NotCompleted |
| **relationship** | [**list[str]**](str)| Specifies how the current user relation should be interpreted, and filters the activities returned to only the activities that have the specified relationship. If a value besides Attendee is specified, it will only return Coaching Appointments. If not specified, no filtering is applied. | [optional] <br />**Values**: Creator, Facilitator, Attendee |

### Return type

[**DevelopmentActivityListing**](DevelopmentActivityListing)


## get_users_development_activity

> [**DevelopmentActivity**](DevelopmentActivity) get_users_development_activity(activity_id, type)


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
type = 'type_example' # str | Specifies the activity type. Informational, AssessedContent and Assessment are deprecated

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
| **type** | **str**| Specifies the activity type. Informational, AssessedContent and Assessment are deprecated | <br />**Values**: Informational, Coaching, AssessedContent, Assessment, External, Native |

### Return type

[**DevelopmentActivity**](DevelopmentActivity)


## get_users_externalid_authority_name_external_key

> [**User**](User) get_users_externalid_authority_name_external_key(authority_name, external_key, expand=expand)


Get the user associated with external identifier.

Authority name and external key are case sensitive.

Wraps GET /api/v2/users/externalid/{authorityName}/{externalKey} 

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
api_instance = PureCloudPlatformClientV2.UsersApi()
authority_name = 'authority_name_example' # str | Authority Name
external_key = 'external_key_example' # str | External Key
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get the user associated with external identifier.
    api_response = api_instance.get_users_externalid_authority_name_external_key(authority_name, external_key, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_externalid_authority_name_external_key: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **authority_name** | **str**| Authority Name |  |
| **external_key** | **str**| External Key |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, dateLastLogin, dateWelcomeSent |

### Return type

[**User**](User)


## get_users_me

> [**UserMe**](UserMe) get_users_me(expand=expand, integration_presence_source=integration_presence_source)


Get current user details.

This request is not valid when using the Client Credentials OAuth grant.

Wraps GET /api/v2/users/me 

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
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, dateLastLogin, dateWelcomeSent, date, geolocationsettings, organization, presencedefinitions, divisionedpresencedefinitions, locationdefinitions, orgauthorization, orgproducts, favorites, superiors, directreports, adjacents, routingskills, routinglanguages, fieldconfigs, token, trustors, logCapture, autoanswersettings |
| **integration_presence_source** | **str**| Get your presence for a given integration. This parameter will only be used when presence is provided as an \&quot;expand\&quot;. | [optional] <br />**Values**: MicrosoftTeams, ZoomPhone, EightByEight |

### Return type

[**UserMe**](UserMe)


## get_users_search

> [**UsersSearchResponse**](UsersSearchResponse) get_users_search(q64, expand=expand, integration_presence_source=integration_presence_source)


Search users using the q64 value returned from a previous search

Wraps GET /api/v2/users/search 

Requires ANY permissions: 

* directory:user:view

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
| **expand** | [**list[str]**](str)| expand | [optional]  |
| **integration_presence_source** | **str**| integrationPresenceSource | [optional] <br />**Values**: MicrosoftTeams, ZoomPhone, EightByEight |

### Return type

[**UsersSearchResponse**](UsersSearchResponse)


## patch_user

> [**User**](User) patch_user(user_id, body)


Update user

Wraps PATCH /api/v2/users/{userId} 

Requires ANY permissions: 

* admin
* directory:user:edit
* directory:organization:admin

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
| **body** | [**UpdateUser**](UpdateUser)| User |  |

### Return type

[**User**](User)


## patch_user_callforwarding

> [**CallForwarding**](CallForwarding) patch_user_callforwarding(user_id, body)


Patch a user's CallForwarding

Wraps PATCH /api/v2/users/{userId}/callforwarding 

Requires ANY permissions: 

* conversation:callForwarding:edit

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
| **body** | [**CallForwarding**](CallForwarding)| Call forwarding |  |

### Return type

[**CallForwarding**](CallForwarding)


## patch_user_geolocation

> [**Geolocation**](Geolocation) patch_user_geolocation(user_id, client_id, body)


Patch a user's Geolocation

The geolocation object can be patched one of three ways. Option 1: Set the 'primary' property to true. This will set the client as the user's primary geolocation source.  Option 2: Provide the 'latitude' and 'longitude' values.  This will enqueue an asynchronous update of the 'city', 'region', and 'country', generating a notification. A subsequent GET operation will include the new values for 'city', 'region' and 'country'.  Option 3:  Provide the 'city', 'region', 'country' values.  Option 1 can be combined with Option 2 or Option 3.  For example, update the client as primary and provide latitude and longitude values.

Wraps PATCH /api/v2/users/{userId}/geolocations/{clientId} 

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
| **body** | [**Geolocation**](Geolocation)| Geolocation |  |

### Return type

[**Geolocation**](Geolocation)


## patch_user_queue

> [**UserQueue**](UserQueue) patch_user_queue(queue_id, user_id, body)


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
| **body** | [**UserQueue**](UserQueue)| Queue Member |  |

### Return type

[**UserQueue**](UserQueue)


## patch_user_queues

> [**UserQueueEntityListing**](UserQueueEntityListing) patch_user_queues(user_id, body, division_id=division_id)


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
| **body** | [**list[UserQueue]**](UserQueue)| User Queues |  |
| **division_id** | [**list[str]**](str)| Division ID(s) | [optional]  |

### Return type

[**UserQueueEntityListing**](UserQueueEntityListing)


## patch_user_routinglanguage

> [**UserRoutingLanguage**](UserRoutingLanguage) patch_user_routinglanguage(user_id, language_id, body)


Update an assigned routing language's proficiency

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
    # Update an assigned routing language's proficiency
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
| **body** | [**UserRoutingLanguage**](UserRoutingLanguage)| Language |  |

### Return type

[**UserRoutingLanguage**](UserRoutingLanguage)


## patch_user_routinglanguages_bulk

> [**UserLanguageEntityListing**](UserLanguageEntityListing) patch_user_routinglanguages_bulk(user_id, body)


Assign multiple routing languages to a user. Max 50 routing languages in request body

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
    # Assign multiple routing languages to a user. Max 50 routing languages in request body
    api_response = api_instance.patch_user_routinglanguages_bulk(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_user_routinglanguages_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserRoutingLanguagePost]**](UserRoutingLanguagePost)| Language |  |

### Return type

[**UserLanguageEntityListing**](UserLanguageEntityListing)


## patch_user_routingskills_bulk

> [**UserSkillEntityListing**](UserSkillEntityListing) patch_user_routingskills_bulk(user_id, body)


Assign multiple routing skills to a user

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
    # Assign multiple routing skills to a user
    api_response = api_instance.patch_user_routingskills_bulk(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_user_routingskills_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserRoutingSkillPost]**](UserRoutingSkillPost)| Skill |  |

### Return type

[**UserSkillEntityListing**](UserSkillEntityListing)


## patch_users_bulk

> [**UserEntityListing**](UserEntityListing) patch_users_bulk(body)


Update bulk acd autoanswer on users. Max 50 users can be updated at a time.

Wraps PATCH /api/v2/users/bulk 

Requires ANY permissions: 

* directory:user:edit
* directory:organization:admin

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
    # Update bulk acd autoanswer on users. Max 50 users can be updated at a time.
    api_response = api_instance.patch_users_bulk(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_users_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**list[PatchUser]**](PatchUser)| Users |  |

### Return type

[**UserEntityListing**](UserEntityListing)


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
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.UserActivityQuery() # UserActivityQuery | query
page_size = 56 # int | The desired page size (optional)
page_number = 56 # int | The desired page number (optional)

try:
    # Query for user activity observations
    api_response = api_instance.post_analytics_users_activity_query(body, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_analytics_users_activity_query: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.UserAsyncAggregationQuery() # UserAsyncAggregationQuery | query

try:
    # Query for user aggregates asynchronously
    api_response = api_instance.post_analytics_users_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_analytics_users_aggregates_jobs: %s\n" % e)
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
| **body** | [**UserObservationQuery**](UserObservationQuery)| query |  |

### Return type

[**UserObservationQueryResponse**](UserObservationQueryResponse)


## post_authorization_subject_bulkadd

>  post_authorization_subject_bulkadd(subject_id, body, subject_type=subject_type)


Bulk-grant roles and divisions to a subject.

Wraps POST /api/v2/authorization/subjects/{subjectId}/bulkadd 

Requires ALL permissions: 

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
subject_type = ''PC_USER'' # str | what the type of the subject is (PC_GROUP, PC_USER or PC_OAUTH_CLIENT) (optional) (default to 'PC_USER')

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
| **body** | [**RoleDivisionGrants**](RoleDivisionGrants)| Pairs of role and division IDs |  |
| **subject_type** | **str**| what the type of the subject is (PC_GROUP, PC_USER or PC_OAUTH_CLIENT) | [optional] [default to &#39;PC_USER&#39;] |

### Return type

void (empty response body)


## post_authorization_subject_bulkremove

>  post_authorization_subject_bulkremove(subject_id, body)


Bulk-remove grants from a subject.

Wraps POST /api/v2/authorization/subjects/{subjectId}/bulkremove 

Requires ALL permissions: 

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
| **body** | [**RoleDivisionGrants**](RoleDivisionGrants)| Pairs of role and division IDs |  |

### Return type

void (empty response body)


## post_authorization_subject_bulkreplace

>  post_authorization_subject_bulkreplace(subject_id, body, subject_type=subject_type)


Replace subject's roles and divisions with the exact list supplied in the request.

This operation will not remove grants that are inherited from group membership. It will only set the grants directly applied to the subject.

Wraps POST /api/v2/authorization/subjects/{subjectId}/bulkreplace 

Requires ALL permissions: 

* authorization:grant:add
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
subject_type = ''PC_USER'' # str | what the type of the subject is (PC_GROUP, PC_USER or PC_OAUTH_CLIENT) (optional) (default to 'PC_USER')

try:
    # Replace subject's roles and divisions with the exact list supplied in the request.
    api_instance.post_authorization_subject_bulkreplace(subject_id, body, subject_type=subject_type)
except ApiException as e:
    print("Exception when calling UsersApi->post_authorization_subject_bulkreplace: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **subject_id** | **str**| Subject ID (user or group) |  |
| **body** | [**RoleDivisionGrants**](RoleDivisionGrants)| Pairs of role and division IDs |  |
| **subject_type** | **str**| what the type of the subject is (PC_GROUP, PC_USER or PC_OAUTH_CLIENT) | [optional] [default to &#39;PC_USER&#39;] |

### Return type

void (empty response body)


## post_authorization_subject_division_role

>  post_authorization_subject_division_role(subject_id, division_id, role_id, subject_type=subject_type)


Make a grant of a role in a division

Wraps POST /api/v2/authorization/subjects/{subjectId}/divisions/{divisionId}/roles/{roleId} 

Requires ALL permissions: 

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
subject_type = ''PC_USER'' # str | what the type of the subject is: PC_GROUP, PC_USER or PC_OAUTH_CLIENT (note: for cross-org authorization, please use the Organization Authorization endpoints) (optional) (default to 'PC_USER')

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
| **subject_type** | **str**| what the type of the subject is: PC_GROUP, PC_USER or PC_OAUTH_CLIENT (note: for cross-org authorization, please use the Organization Authorization endpoints) | [optional] [default to &#39;PC_USER&#39;] |

### Return type

void (empty response body)


## post_user_externalid

> [**list[UserExternalIdentifier]**](UserExternalIdentifier) post_user_externalid(user_id, body)


Create mapping between external identifier and user. Limit 100 per entity.

Authority Name and External key are case sensitive.

Wraps POST /api/v2/users/{userId}/externalid 

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
body = PureCloudPlatformClientV2.UserExternalIdentifier() # UserExternalIdentifier | 

try:
    # Create mapping between external identifier and user. Limit 100 per entity.
    api_response = api_instance.post_user_externalid(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_user_externalid: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**UserExternalIdentifier**](UserExternalIdentifier)|  |  |

### Return type

[**list[UserExternalIdentifier]**](UserExternalIdentifier)


## post_user_invite

>  post_user_invite(user_id, force=force)


Send an activation email to the user

Wraps POST /api/v2/users/{userId}/invite 

Requires ANY permissions: 

* admin
* directory:organization:admin
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
force = False # bool | Resend the invitation even if one is already outstanding (optional) (default to False)

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
| **force** | **bool**| Resend the invitation even if one is already outstanding | [optional] [default to False] |

### Return type

void (empty response body)


## post_user_password

>  post_user_password(user_id, body)


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
| **body** | [**ChangePasswordRequest**](ChangePasswordRequest)| Password |  |

### Return type

void (empty response body)


## post_user_routinglanguages

> [**UserRoutingLanguage**](UserRoutingLanguage) post_user_routinglanguages(user_id, body)


Assign a routing language to a user

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
    # Assign a routing language to a user
    api_response = api_instance.post_user_routinglanguages(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_user_routinglanguages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**UserRoutingLanguagePost**](UserRoutingLanguagePost)| Language |  |

### Return type

[**UserRoutingLanguage**](UserRoutingLanguage)


## post_user_routingskills

> [**UserRoutingSkill**](UserRoutingSkill) post_user_routingskills(user_id, body)


Assign a routing skill to a user

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
    # Assign a routing skill to a user
    api_response = api_instance.post_user_routingskills(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_user_routingskills: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**UserRoutingSkillPost**](UserRoutingSkillPost)| Skill |  |

### Return type

[**UserRoutingSkill**](UserRoutingSkill)


## post_users

> [**User**](User) post_users(body)


Create user

If user creation is successful but the provided password is invalid or configuration fails, POST api/v2/users/{userId}/password can be used to re-attempt password configuration.

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
| **body** | [**CreateUser**](CreateUser)| User |  |

### Return type

[**User**](User)


## post_users_development_activities_aggregates_query

> [**DevelopmentActivityAggregateResponse**](DevelopmentActivityAggregateResponse) post_users_development_activities_aggregates_query(body)


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
| **body** | [**DevelopmentActivityAggregateParam**](DevelopmentActivityAggregateParam)| Aggregate Request |  |

### Return type

[**DevelopmentActivityAggregateResponse**](DevelopmentActivityAggregateResponse)


## post_users_me_password

>  post_users_me_password(body)


Change your password

Wraps POST /api/v2/users/me/password 

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
| **body** | [**ChangeMyPasswordRequest**](ChangeMyPasswordRequest)| Password |  |

### Return type

void (empty response body)


## post_users_search

> [**UsersSearchResponse**](UsersSearchResponse) post_users_search(body)


Search users

Wraps POST /api/v2/users/search 

Requires ANY permissions: 

* directory:user:view

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
| **body** | [**UserSearchRequest**](UserSearchRequest)| Search request options |  |

### Return type

[**UsersSearchResponse**](UsersSearchResponse)


## post_users_search_conversation_target

> [**UsersSearchResponse**](UsersSearchResponse) post_users_search_conversation_target(body)


Search users as conversation targets

post_users_search_conversation_target is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/users/search/conversation/target 

Requires ANY permissions: 

* conversation:communication:target

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
    # Search users as conversation targets
    api_response = api_instance.post_users_search_conversation_target(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_search_conversation_target: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserSearchRequest**](UserSearchRequest)| Search request options |  |

### Return type

[**UsersSearchResponse**](UsersSearchResponse)


## post_users_search_queuemembers_manage

> [**UsersSearchResponse**](UsersSearchResponse) post_users_search_queuemembers_manage(body)


Search manage queue member

post_users_search_queuemembers_manage is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/users/search/queuemembers/manage 

Requires ANY permissions: 

* routing:queueMember:manage
* routing:queue:edit

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
    # Search manage queue member
    api_response = api_instance.post_users_search_queuemembers_manage(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_search_queuemembers_manage: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserSearchRequest**](UserSearchRequest)| Search request options |  |

### Return type

[**UsersSearchResponse**](UsersSearchResponse)


## post_users_search_teams_assign

> [**UsersSearchResponse**](UsersSearchResponse) post_users_search_teams_assign(body)


Search users assigned to teams

Wraps POST /api/v2/users/search/teams/assign 

Requires ANY permissions: 

* groups:team:assign

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
    # Search users assigned to teams
    api_response = api_instance.post_users_search_teams_assign(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_search_teams_assign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserSearchRequest**](UserSearchRequest)| Search request options |  |

### Return type

[**UsersSearchResponse**](UsersSearchResponse)


## put_routing_directroutingbackup_settings_me

> [**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings) put_routing_directroutingbackup_settings_me(body)


Update the user's Direct Routing Backup settings.

Wraps PUT /api/v2/routing/directroutingbackup/settings/me 

Requires ANY permissions: 

* routing:directRoutingBackup:selfEdit

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
body = PureCloudPlatformClientV2.AgentDirectRoutingBackupSettings() # AgentDirectRoutingBackupSettings | directRoutingBackup

try:
    # Update the user's Direct Routing Backup settings.
    api_response = api_instance.put_routing_directroutingbackup_settings_me(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_routing_directroutingbackup_settings_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings)| directRoutingBackup |  |

### Return type

[**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings)


## put_routing_user_directroutingbackup_settings

> [**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings) put_routing_user_directroutingbackup_settings(user_id, body)


Update the user's Direct Routing Backup settings.

Wraps PUT /api/v2/routing/users/{userId}/directroutingbackup/settings 

Requires ANY permissions: 

* routing:directRoutingBackup:edit

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
body = PureCloudPlatformClientV2.AgentDirectRoutingBackupSettings() # AgentDirectRoutingBackupSettings | directRoutingBackup

try:
    # Update the user's Direct Routing Backup settings.
    api_response = api_instance.put_routing_user_directroutingbackup_settings(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_routing_user_directroutingbackup_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings)| directRoutingBackup |  |

### Return type

[**AgentDirectRoutingBackupSettings**](AgentDirectRoutingBackupSettings)


## put_routing_user_utilization

> [**AgentMaxUtilizationResponse**](AgentMaxUtilizationResponse) put_routing_user_utilization(user_id, body)


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
body = PureCloudPlatformClientV2.UtilizationRequest() # UtilizationRequest | utilization

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
| **body** | [**UtilizationRequest**](UtilizationRequest)| utilization |  |

### Return type

[**AgentMaxUtilizationResponse**](AgentMaxUtilizationResponse)


## put_user_callforwarding

> [**CallForwarding**](CallForwarding) put_user_callforwarding(user_id, body)


Update a user's CallForwarding

Wraps PUT /api/v2/users/{userId}/callforwarding 

Requires ANY permissions: 

* conversation:callForwarding:edit

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
| **body** | [**CallForwarding**](CallForwarding)| Call forwarding |  |

### Return type

[**CallForwarding**](CallForwarding)


## put_user_outofoffice

> [**OutOfOffice**](OutOfOffice) put_user_outofoffice(user_id, body)


Update an OutOfOffice

Wraps PUT /api/v2/users/{userId}/outofoffice 

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
| **body** | [**OutOfOffice**](OutOfOffice)| The updated OutOffOffice |  |

### Return type

[**OutOfOffice**](OutOfOffice)


## put_user_profileskills

> list[str]** put_user_profileskills(user_id, body)


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
body = ['body_example'] # list[str] | Skills

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
| **body** | [**list[str]**](str)| Skills |  |

### Return type

**list[str]**


## put_user_roles

> [**UserAuthorization**](UserAuthorization) put_user_roles(subject_id, body)


Sets the user's roles

Wraps PUT /api/v2/users/{subjectId}/roles 

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
subject_id = 'subject_id_example' # str | User ID
body = ['body_example'] # list[str] | List of roles

try:
    # Sets the user's roles
    api_response = api_instance.put_user_roles(subject_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_user_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **subject_id** | **str**| User ID |  |
| **body** | [**list[str]**](str)| List of roles |  |

### Return type

[**UserAuthorization**](UserAuthorization)


## put_user_routingskill

> [**UserRoutingSkill**](UserRoutingSkill) put_user_routingskill(user_id, skill_id, body)


Update an assigned routing skill's proficiency

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
    # Update an assigned routing skill's proficiency
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
| **body** | [**UserRoutingSkill**](UserRoutingSkill)| Skill |  |

### Return type

[**UserRoutingSkill**](UserRoutingSkill)


## put_user_routingskills_bulk

> [**UserSkillEntityListing**](UserSkillEntityListing) put_user_routingskills_bulk(user_id, body)


Assign multiple routing skills to a user, replacing any current assignments

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
    # Assign multiple routing skills to a user, replacing any current assignments
    api_response = api_instance.put_user_routingskills_bulk(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_user_routingskills_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserRoutingSkillPost]**](UserRoutingSkillPost)| Skill |  |

### Return type

[**UserSkillEntityListing**](UserSkillEntityListing)


## put_user_routingstatus

> [**RoutingStatus**](RoutingStatus) put_user_routingstatus(user_id, body)


Update the routing status of a user

Wraps PUT /api/v2/users/{userId}/routingstatus 

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
| **body** | [**RoutingStatus**](RoutingStatus)| Routing Status |  |

### Return type

[**RoutingStatus**](RoutingStatus)


## put_user_state

> [**UserState**](UserState) put_user_state(user_id, body)


Update user state information.

Wraps PUT /api/v2/users/{userId}/state 

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
body = PureCloudPlatformClientV2.UserState() # UserState | User

try:
    # Update user state information.
    api_response = api_instance.put_user_state(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_user_state: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**UserState**](UserState)| User |  |

### Return type

[**UserState**](UserState)


## put_user_station_associatedstation_station_id

>  put_user_station_associatedstation_station_id(user_id, station_id)


Set associated station

Wraps PUT /api/v2/users/{userId}/station/associatedstation/{stationId} 

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

### Return type

void (empty response body)


## put_user_station_defaultstation_station_id

>  put_user_station_defaultstation_station_id(user_id, station_id)


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

### Return type

void (empty response body)


## put_user_verifier

> [**Verifier**](Verifier) put_user_verifier(user_id, verifier_id, body)


Update a verifier

Wraps PUT /api/v2/users/{userId}/verifiers/{verifierId} 

Requires ANY permissions: 

* mfa:verifier:edit

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
verifier_id = 'verifier_id_example' # str | Verifier ID
body = PureCloudPlatformClientV2.UpdateVerifierRequest() # UpdateVerifierRequest | Verifier Update

try:
    # Update a verifier
    api_response = api_instance.put_user_verifier(user_id, verifier_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_user_verifier: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **verifier_id** | **str**| Verifier ID |  |
| **body** | [**UpdateVerifierRequest**](UpdateVerifierRequest)| Verifier Update |  |

### Return type

[**Verifier**](Verifier)


_PureCloudPlatformClientV2 230.0.0_

---
title: UsersApi
---

## PureCloudPlatformClientV2.UsersApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_user**](UsersApi.html#delete_user) | Delete user|
|[**delete_user_roles**](UsersApi.html#delete_user_roles) | Removes all the roles from the user.|
|[**delete_user_routingskill**](UsersApi.html#delete_user_routingskill) | Remove routing skill from user|
|[**delete_user_station_associatedstation**](UsersApi.html#delete_user_station_associatedstation) | Clear associated station|
|[**delete_user_station_defaultstation**](UsersApi.html#delete_user_station_defaultstation) | Clear default station|
|[**get_fieldconfig**](UsersApi.html#get_fieldconfig) | Fetch field config for an entity type|
|[**get_profiles_users**](UsersApi.html#get_profiles_users) | Get a user profile listing|
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
|[**get_user_routingskills**](UsersApi.html#get_user_routingskills) | List routing skills for user|
|[**get_user_routingstatus**](UsersApi.html#get_user_routingstatus) | Fetch the routing status of a user|
|[**get_user_station**](UsersApi.html#get_user_station) | Get station information for user|
|[**get_user_superiors**](UsersApi.html#get_user_superiors) | Get superiors|
|[**get_users**](UsersApi.html#get_users) | Get the list of available users.|
|[**get_users_me**](UsersApi.html#get_users_me) | Get current user details.|
|[**get_users_search**](UsersApi.html#get_users_search) | Search users using the q64 value returned from a previous search|
|[**patch_user**](UsersApi.html#patch_user) | Update user|
|[**patch_user_callforwarding**](UsersApi.html#patch_user_callforwarding) | Patch a user&#39;s CallForwarding|
|[**patch_user_geolocation**](UsersApi.html#patch_user_geolocation) | Patch a user&#39;s Geolocation|
|[**patch_user_queue**](UsersApi.html#patch_user_queue) | Join or unjoin a queue for a user|
|[**patch_user_queues**](UsersApi.html#patch_user_queues) | Join or unjoin a set of queues for a user|
|[**post_analytics_users_aggregates_query**](UsersApi.html#post_analytics_users_aggregates_query) | Query for user aggregates|
|[**post_analytics_users_details_query**](UsersApi.html#post_analytics_users_details_query) | Query for user details|
|[**post_analytics_users_observations_query**](UsersApi.html#post_analytics_users_observations_query) | Query for user observations|
|[**post_user_invite**](UsersApi.html#post_user_invite) | Send an activation email to the user|
|[**post_user_password**](UsersApi.html#post_user_password) | Change a users password|
|[**post_user_routingskills**](UsersApi.html#post_user_routingskills) | Add routing skill to user|
|[**post_users**](UsersApi.html#post_users) | Create user|
|[**post_users_me_password**](UsersApi.html#post_users_me_password) | Change your password|
|[**post_users_search**](UsersApi.html#post_users_search) | Search users|
|[**put_user_callforwarding**](UsersApi.html#put_user_callforwarding) | Update a user&#39;s CallForwarding|
|[**put_user_outofoffice**](UsersApi.html#put_user_outofoffice) | Update an OutOfOffice|
|[**put_user_profileskills**](UsersApi.html#put_user_profileskills) | Update profile skills for a user|
|[**put_user_roles**](UsersApi.html#put_user_roles) | Sets the user&#39;s roles|
|[**put_user_routingskill**](UsersApi.html#put_user_routingskill) | Update routing skill proficiency or state.|
|[**put_user_routingstatus**](UsersApi.html#put_user_routingstatus) | Update the routing status of a user|
|[**put_user_station_associatedstation_station_id**](UsersApi.html#put_user_station_associatedstation_station_id) | Set associated station|
|[**put_user_station_defaultstation_station_id**](UsersApi.html#put_user_station_defaultstation_station_id) | Set default station|
{: class="table table-striped"}

<a name="delete_user"></a>

## [**Empty**](Empty.html) delete_user(user_id)

Delete user



Wraps DELETE /api/v2/users/{userId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Delete user
    api_response = api_instance.delete_user(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->delete_user: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="delete_user_roles"></a>

##  delete_user_roles(user_id)

Removes all the roles from the user.



Wraps DELETE /api/v2/users/{userId}/roles 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Removes all the roles from the user.
    api_instance.delete_user_roles(user_id)
except ApiException as e:
    print "Exception when calling UsersApi->delete_user_roles: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_user_routingskill"></a>

##  delete_user_routingskill(user_id, skill_id)

Remove routing skill from user



Wraps DELETE /api/v2/users/{userId}/routingskills/{skillId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
skill_id = 'skill_id_example' # str | skillId

try:
    # Remove routing skill from user
    api_instance.delete_user_routingskill(user_id, skill_id)
except ApiException as e:
    print "Exception when calling UsersApi->delete_user_routingskill: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Clear associated station
    api_instance.delete_user_station_associatedstation(user_id)
except ApiException as e:
    print "Exception when calling UsersApi->delete_user_station_associatedstation: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Clear default station
    api_instance.delete_user_station_defaultstation(user_id)
except ApiException as e:
    print "Exception when calling UsersApi->delete_user_station_defaultstation: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_fieldconfig"></a>

## [**FieldConfig**](FieldConfig.html) get_fieldconfig(type)

Fetch field config for an entity type



Wraps GET /api/v2/fieldconfig 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
type = 'type_example' # str | Field type

try:
    # Fetch field config for an entity type
    api_response = api_instance.get_fieldconfig(type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_fieldconfig: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | **str**| Field type | <br />**Values**: person, group, org, externalContact |
{: class="table table-striped"}

### Return type

[**FieldConfig**](FieldConfig.html)

<a name="get_profiles_users"></a>

## [**UserProfileEntityListing**](UserProfileEntityListing.html) get_profiles_users(page_size=page_size, page_number=page_number, id=id, jid=jid, sort_order=sort_order, expand=expand, state=state)

Get a user profile listing



Wraps GET /api/v2/profiles/users 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
id = ['id_example'] # list[str] | id (optional)
jid = ['jid_example'] # list[str] | jid (optional)
sort_order = 'ASC' # str | Ascending or descending sort order (optional) (default to ASC)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
state = 'active' # str | Only list users of this state (optional) (default to active)

try:
    # Get a user profile listing
    api_response = api_instance.get_profiles_users(page_size=page_size, page_number=page_number, id=id, jid=jid, sort_order=sort_order, expand=expand, state=state)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_profiles_users: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **id** | [**list[str]**](str.html)| id | [optional]  |
| **jid** | [**list[str]**](str.html)| jid | [optional]  |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to ASC]<br />**Values**: ascending, descending |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization |
| **state** | **str**| Only list users of this state | [optional] [default to active]<br />**Values**: active, deleted |
{: class="table table-striped"}

### Return type

[**UserProfileEntityListing**](UserProfileEntityListing.html)

<a name="get_user"></a>

## [**User**](User.html) get_user(user_id, expand=expand, state=state)

Get user.



Wraps GET /api/v2/users/{userId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
state = 'active' # str | Search for a user with this state (optional) (default to active)

try:
    # Get user.
    api_response = api_instance.get_user(user_id, expand=expand, state=state)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, profileSkills, locations, groups |
| **state** | **str**| Search for a user with this state | [optional] [default to active]<br />**Values**: active, deleted |
{: class="table table-striped"}

### Return type

[**User**](User.html)

<a name="get_user_adjacents"></a>

## [**Adjacents**](Adjacents.html) get_user_adjacents(user_id, expand=expand)

Get adjacents



Wraps GET /api/v2/users/{userId}/adjacents 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->get_user_adjacents: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, profileSkills, locations, groups |
{: class="table table-striped"}

### Return type

[**Adjacents**](Adjacents.html)

<a name="get_user_callforwarding"></a>

## [**CallForwarding**](CallForwarding.html) get_user_callforwarding(user_id)

Get a user's CallForwarding



Wraps GET /api/v2/users/{userId}/callforwarding 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Get a user's CallForwarding
    api_response = api_instance.get_user_callforwarding(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_callforwarding: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->get_user_directreports: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, profileSkills, locations, groups |
{: class="table table-striped"}

### Return type

[**list[User]**](User.html)

<a name="get_user_favorites"></a>

## [**UserEntityListing**](UserEntityListing.html) get_user_favorites(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand)

Get favorites



Wraps GET /api/v2/users/{userId}/favorites 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->get_user_favorites: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Sort order | [optional] [default to ASC] |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, profileSkills, locations, groups |
{: class="table table-striped"}

### Return type

[**UserEntityListing**](UserEntityListing.html)

<a name="get_user_geolocation"></a>

## [**Geolocation**](Geolocation.html) get_user_geolocation(user_id, client_id)

Get a user's Geolocation



Wraps GET /api/v2/users/{userId}/geolocations/{clientId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->get_user_geolocation: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Get a OutOfOffice
    api_response = api_instance.get_user_outofoffice(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_outofoffice: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

[**OutOfOffice**](OutOfOffice.html)

<a name="get_user_profile"></a>

## [**UserProfile**](UserProfile.html) get_user_profile(user_id, expand=expand)

Get user profile



Wraps GET /api/v2/users/{userId}/profile 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | userId
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get user profile
    api_response = api_instance.get_user_profile(user_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_profile: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| userId |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, profileSkills, locations, groups |
{: class="table table-striped"}

### Return type

[**UserProfile**](UserProfile.html)

<a name="get_user_profileskills"></a>

## list[str]** get_user_profileskills(user_id)

List profile skills for a user



Wraps GET /api/v2/users/{userId}/profileskills 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # List profile skills for a user
    api_response = api_instance.get_user_profileskills(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_profileskills: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

**list[str]**

<a name="get_user_queues"></a>

## [**UserQueueEntityListing**](UserQueueEntityListing.html) get_user_queues(user_id, page_size=page_size, page_number=page_number, joined=joined)

Get queues for user



Wraps GET /api/v2/users/{userId}/queues 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
joined = true # bool | Is joined to the queue (optional) (default to true)

try:
    # Get queues for user
    api_response = api_instance.get_user_queues(user_id, page_size=page_size, page_number=page_number, joined=joined)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_queues: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **joined** | **bool**| Is joined to the queue | [optional] [default to true] |
{: class="table table-striped"}

### Return type

[**UserQueueEntityListing**](UserQueueEntityListing.html)

<a name="get_user_roles"></a>

## [**UserAuthorization**](UserAuthorization.html) get_user_roles(user_id)

Returns a listing of roles and permissions for a user.



Wraps GET /api/v2/users/{userId}/roles 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Returns a listing of roles and permissions for a user.
    api_response = api_instance.get_user_roles(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_roles: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

[**UserAuthorization**](UserAuthorization.html)

<a name="get_user_routingskills"></a>

## [**UserSkillEntityListing**](UserSkillEntityListing.html) get_user_routingskills(user_id, page_size=page_size, page_number=page_number, sort_order=sort_order)

List routing skills for user



Wraps GET /api/v2/users/{userId}/routingskills 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->get_user_routingskills: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Fetch the routing status of a user
    api_response = api_instance.get_user_routingstatus(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_routingstatus: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID

try:
    # Get station information for user
    api_response = api_instance.get_user_station(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_station: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->get_user_superiors: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, profileSkills, locations, groups |
{: class="table table-striped"}

### Return type

[**list[User]**](User.html)

<a name="get_users"></a>

## [**UserEntityListing**](UserEntityListing.html) get_users(page_size=page_size, page_number=page_number, id=id, sort_order=sort_order, expand=expand, state=state)

Get the list of available users.



Wraps GET /api/v2/users 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
id = ['id_example'] # list[str] | id (optional)
sort_order = 'ASC' # str | Ascending or descending sort order (optional) (default to ASC)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
state = 'active' # str | Only list users of this state (optional) (default to active)

try:
    # Get the list of available users.
    api_response = api_instance.get_users(page_size=page_size, page_number=page_number, id=id, sort_order=sort_order, expand=expand, state=state)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_users: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **id** | [**list[str]**](str.html)| id | [optional]  |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to ASC]<br />**Values**: ascending, descending |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, profileSkills, locations, groups |
| **state** | **str**| Only list users of this state | [optional] [default to active]<br />**Values**: active, inactive, deleted |
{: class="table table-striped"}

### Return type

[**UserEntityListing**](UserEntityListing.html)

<a name="get_users_me"></a>

## [**UserMe**](UserMe.html) get_users_me(expand=expand)

Get current user details.

This request is not valid when using the Client Credentials OAuth grant.

Wraps GET /api/v2/users/me 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get current user details.
    api_response = api_instance.get_users_me(expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_users_me: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand. | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, profileSkills, locations, groups, date, geolocationsettings, organization, presencedefinitions, locationdefinitions, orgauthorization, favorites, superiors, directreports, adjacents, routingskills, routinglanguages, fieldconfigs, token, trustors |
{: class="table table-striped"}

### Return type

[**UserMe**](UserMe.html)

<a name="get_users_search"></a>

## [**UsersSearchResponse**](UsersSearchResponse.html) get_users_search(q64, expand=expand)

Search users using the q64 value returned from a previous search



Wraps GET /api/v2/users/search 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | expand (optional)

try:
    # Search users using the q64 value returned from a previous search
    api_response = api_instance.get_users_search(q64, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_users_search: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str.html)| expand | [optional]  |
{: class="table table-striped"}

### Return type

[**UsersSearchResponse**](UsersSearchResponse.html)

<a name="patch_user"></a>

## [**User**](User.html) patch_user(user_id, body)

Update user



Wraps PATCH /api/v2/users/{userId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->patch_user: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->patch_user_callforwarding: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->patch_user_geolocation: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->patch_user_queue: %s\n" % e
~~~

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

## [**UserQueueEntityListing**](UserQueueEntityListing.html) patch_user_queues(user_id, body)

Join or unjoin a set of queues for a user



Wraps PATCH /api/v2/users/{userId}/queues 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = [PureCloudPlatformClientV2.UserQueue()] # list[UserQueue] | User Queues

try:
    # Join or unjoin a set of queues for a user
    api_response = api_instance.patch_user_queues(user_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->patch_user_queues: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**list[UserQueue]**](UserQueue.html)| User Queues |  |
{: class="table table-striped"}

### Return type

[**UserQueueEntityListing**](UserQueueEntityListing.html)

<a name="post_analytics_users_aggregates_query"></a>

## [**PresenceQueryResponse**](PresenceQueryResponse.html) post_analytics_users_aggregates_query(body)

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
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.AggregationQuery() # AggregationQuery | query

try:
    # Query for user aggregates
    api_response = api_instance.post_analytics_users_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->post_analytics_users_aggregates_query: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AggregationQuery**](AggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**PresenceQueryResponse**](PresenceQueryResponse.html)

<a name="post_analytics_users_details_query"></a>

## [**AnalyticsUserDetailsQueryResponse**](AnalyticsUserDetailsQueryResponse.html) post_analytics_users_details_query(body)

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
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.UserDetailsQuery() # UserDetailsQuery | query

try:
    # Query for user details
    api_response = api_instance.post_analytics_users_details_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->post_analytics_users_details_query: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserDetailsQuery**](UserDetailsQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AnalyticsUserDetailsQueryResponse**](AnalyticsUserDetailsQueryResponse.html)

<a name="post_analytics_users_observations_query"></a>

## [**ObservationQueryResponse**](ObservationQueryResponse.html) post_analytics_users_observations_query(body)

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
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.ObservationQuery() # ObservationQuery | query

try:
    # Query for user observations
    api_response = api_instance.post_analytics_users_observations_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->post_analytics_users_observations_query: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ObservationQuery**](ObservationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**ObservationQueryResponse**](ObservationQueryResponse.html)

<a name="post_user_invite"></a>

##  post_user_invite(user_id, force=force)

Send an activation email to the user



Wraps POST /api/v2/users/{userId}/invite 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
force = false # bool | Resend the invitation even if one is already outstanding (optional) (default to false)

try:
    # Send an activation email to the user
    api_instance.post_user_invite(user_id, force=force)
except ApiException as e:
    print "Exception when calling UsersApi->post_user_invite: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.ChangePasswordRequest() # ChangePasswordRequest | Password

try:
    # Change a users password
    api_instance.post_user_password(user_id, body)
except ApiException as e:
    print "Exception when calling UsersApi->post_user_password: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**ChangePasswordRequest**](ChangePasswordRequest.html)| Password |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_user_routingskills"></a>

## [**UserRoutingSkill**](UserRoutingSkill.html) post_user_routingskills(user_id, body)

Add routing skill to user



Wraps POST /api/v2/users/{userId}/routingskills 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->post_user_routingskills: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.CreateUser() # CreateUser | User

try:
    # Create user
    api_response = api_instance.post_users(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->post_users: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateUser**](CreateUser.html)| User |  |
{: class="table table-striped"}

### Return type

[**User**](User.html)

<a name="post_users_me_password"></a>

##  post_users_me_password(body)

Change your password



Wraps POST /api/v2/users/me/password 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.ChangeMyPasswordRequest() # ChangeMyPasswordRequest | Password

try:
    # Change your password
    api_instance.post_users_me_password(body)
except ApiException as e:
    print "Exception when calling UsersApi->post_users_me_password: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
body = PureCloudPlatformClientV2.UserSearchRequest() # UserSearchRequest | Search request options

try:
    # Search users
    api_response = api_instance.post_users_search(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->post_users_search: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserSearchRequest**](UserSearchRequest.html)| Search request options |  |
{: class="table table-striped"}

### Return type

[**UsersSearchResponse**](UsersSearchResponse.html)

<a name="put_user_callforwarding"></a>

## [**CallForwarding**](CallForwarding.html) put_user_callforwarding(user_id, body)

Update a user's CallForwarding



Wraps PUT /api/v2/users/{userId}/callforwarding 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->put_user_callforwarding: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->put_user_outofoffice: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**OutOfOffice**](OutOfOffice.html)| The updated OutOffOffice |  |
{: class="table table-striped"}

### Return type

[**OutOfOffice**](OutOfOffice.html)

<a name="put_user_profileskills"></a>

## list[str]** put_user_profileskills(user_id, body=body)

Update profile skills for a user



Wraps PUT /api/v2/users/{userId}/profileskills 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | Skills (optional)

try:
    # Update profile skills for a user
    api_response = api_instance.put_user_profileskills(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->put_user_profileskills: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | **list[str]**| Skills | [optional]  |
{: class="table table-striped"}

### Return type

**list[str]**

<a name="put_user_roles"></a>

## [**UserAuthorization**](UserAuthorization.html) put_user_roles(user_id, body)

Sets the user's roles



Wraps PUT /api/v2/users/{userId}/roles 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->put_user_roles: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->put_user_routingskill: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **skill_id** | **str**| skillId |  |
| **body** | [**UserRoutingSkill**](UserRoutingSkill.html)| Skill |  |
{: class="table table-striped"}

### Return type

[**UserRoutingSkill**](UserRoutingSkill.html)

<a name="put_user_routingstatus"></a>

## [**RoutingStatus**](RoutingStatus.html) put_user_routingstatus(user_id, body)

Update the routing status of a user



Wraps PUT /api/v2/users/{userId}/routingstatus 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UsersApi->put_user_routingstatus: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
station_id = 'station_id_example' # str | stationId

try:
    # Set associated station
    api_instance.put_user_station_associatedstation_station_id(user_id, station_id)
except ApiException as e:
    print "Exception when calling UsersApi->put_user_station_associatedstation_station_id: %s\n" % e
~~~

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

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UsersApi()
user_id = 'user_id_example' # str | User ID
station_id = 'station_id_example' # str | stationId

try:
    # Set default station
    api_instance.put_user_station_defaultstation_station_id(user_id, station_id)
except ApiException as e:
    print "Exception when calling UsersApi->put_user_station_defaultstation_station_id: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **station_id** | **str**| stationId |  |
{: class="table table-striped"}

### Return type

void (empty response body)


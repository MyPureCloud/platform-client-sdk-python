---
title: AuthorizationApi
---

## PureCloudPlatformClientV2.AuthorizationApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_authorization_role**](AuthorizationApi.html#delete_authorization_role) | Delete an organization role.|
|[**delete_user_roles**](AuthorizationApi.html#delete_user_roles) | Removes all the roles from the user.|
|[**get_authorization_permissions**](AuthorizationApi.html#get_authorization_permissions) | Get all permissions.|
|[**get_authorization_products**](AuthorizationApi.html#get_authorization_products) | Get the list of enabled products|
|[**get_authorization_role**](AuthorizationApi.html#get_authorization_role) | Get a single organization role.|
|[**get_authorization_role_comparedefault_right_role_id**](AuthorizationApi.html#get_authorization_role_comparedefault_right_role_id) | Get an org role to default role comparison comparison|
|[**get_authorization_roles**](AuthorizationApi.html#get_authorization_roles) | Retrieve a list of all roles defined for the organization|
|[**get_user_roles**](AuthorizationApi.html#get_user_roles) | Returns a listing of roles and permissions for a user.|
|[**patch_authorization_role**](AuthorizationApi.html#patch_authorization_role) | Patch Organization Role for needsUpdate Field|
|[**post_authorization_role_comparedefault_right_role_id**](AuthorizationApi.html#post_authorization_role_comparedefault_right_role_id) | Get an unsaved org role to default role comparison|
|[**post_authorization_roles**](AuthorizationApi.html#post_authorization_roles) | Create an organization role.|
|[**post_authorization_roles_default**](AuthorizationApi.html#post_authorization_roles_default) | Restores all default roles|
|[**put_authorization_role**](AuthorizationApi.html#put_authorization_role) | Update an organization role.|
|[**put_authorization_role_users_add**](AuthorizationApi.html#put_authorization_role_users_add) | Sets the users for the role|
|[**put_authorization_role_users_remove**](AuthorizationApi.html#put_authorization_role_users_remove) | Removes the users from the role|
|[**put_authorization_roles_default**](AuthorizationApi.html#put_authorization_roles_default) | Restore specified default roles|
|[**put_user_roles**](AuthorizationApi.html#put_user_roles) | Sets the user&#39;s roles|
{: class="table table-striped"}

<a name="delete_authorization_role"></a>

##  delete_authorization_role(role_id)

Delete an organization role.



Wraps DELETE /api/v2/authorization/roles/{roleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
role_id = 'role_id_example' # str | Role ID

try:
    # Delete an organization role.
    api_instance.delete_authorization_role(role_id)
except ApiException as e:
    print "Exception when calling AuthorizationApi->delete_authorization_role: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
user_id = 'user_id_example' # str | User ID

try:
    # Removes all the roles from the user.
    api_instance.delete_user_roles(user_id)
except ApiException as e:
    print "Exception when calling AuthorizationApi->delete_user_roles: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_authorization_permissions"></a>

## [**PermissionCollectionEntityListing**](PermissionCollectionEntityListing.html) get_authorization_permissions(page_size=page_size, page_number=page_number)

Get all permissions.

Retrieve a list of all permission defined in the system.

Wraps GET /api/v2/authorization/permissions 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get all permissions.
    api_response = api_instance.get_authorization_permissions(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->get_authorization_permissions: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **page_number** | **int**| Page number | [optional] [default to 1]|
{: class="table table-striped"}

### Return type

[**PermissionCollectionEntityListing**](PermissionCollectionEntityListing.html)

<a name="get_authorization_products"></a>

## [**OrganizationProductEntityListing**](OrganizationProductEntityListing.html) get_authorization_products()

Get the list of enabled products

Gets the list of enabled products. Some example product names are: collaborateFree, collaboratePro, communicate, and engage.

Wraps GET /api/v2/authorization/products 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()

try:
    # Get the list of enabled products
    api_response = api_instance.get_authorization_products()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->get_authorization_products: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**OrganizationProductEntityListing**](OrganizationProductEntityListing.html)

<a name="get_authorization_role"></a>

## [**DomainOrganizationRole**](DomainOrganizationRole.html) get_authorization_role(role_id)

Get a single organization role.

Get the organization role specified by its ID.

Wraps GET /api/v2/authorization/roles/{roleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
role_id = 'role_id_example' # str | Role ID

try:
    # Get a single organization role.
    api_response = api_instance.get_authorization_role(role_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->get_authorization_role: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID | |
{: class="table table-striped"}

### Return type

[**DomainOrganizationRole**](DomainOrganizationRole.html)

<a name="get_authorization_role_comparedefault_right_role_id"></a>

## [**DomainOrgRoleDifference**](DomainOrgRoleDifference.html) get_authorization_role_comparedefault_right_role_id(left_role_id, right_role_id)

Get an org role to default role comparison comparison

Compares any organization role to a default role id and show differences

Wraps GET /api/v2/authorization/roles/{leftRoleId}/comparedefault/{rightRoleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
left_role_id = 'left_role_id_example' # str | Left Role ID
right_role_id = 'right_role_id_example' # str | Right Role id

try:
    # Get an org role to default role comparison comparison
    api_response = api_instance.get_authorization_role_comparedefault_right_role_id(left_role_id, right_role_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->get_authorization_role_comparedefault_right_role_id: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **left_role_id** | **str**| Left Role ID | |
| **right_role_id** | **str**| Right Role id | |
{: class="table table-striped"}

### Return type

[**DomainOrgRoleDifference**](DomainOrgRoleDifference.html)

<a name="get_authorization_roles"></a>

## [**OrganizationRoleEntityListing**](OrganizationRoleEntityListing.html) get_authorization_roles(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, permission=permission, default_role_id=default_role_id, user_count=user_count)

Retrieve a list of all roles defined for the organization



Wraps GET /api/v2/authorization/roles 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = NULL # list[object] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
permission = NULL # list[object] |  (optional)
default_role_id = NULL # list[object] |  (optional)
user_count = true # bool |  (optional) (default to true)

try:
    # Retrieve a list of all roles defined for the organization
    api_response = api_instance.get_authorization_roles(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, permission=permission, default_role_id=default_role_id, user_count=user_count)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->get_authorization_roles: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25]|
| **page_number** | **int**| The page number requested | [optional] [default to 1]|
| **sort_by** | **str**| variable name requested to sort by | [optional] |
| **expand** | [**list[object]**](object.html)| variable name requested by expand list | [optional] |
| **next_page** | **str**| next page token | [optional] |
| **previous_page** | **str**| Previous page token | [optional] |
| **permission** | [**list[object]**](object.html)|  | [optional] |
| **default_role_id** | [**list[object]**](object.html)|  | [optional] |
| **user_count** | **bool**|  | [optional] [default to true]|
{: class="table table-striped"}

### Return type

[**OrganizationRoleEntityListing**](OrganizationRoleEntityListing.html)

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
user_id = 'user_id_example' # str | User ID

try:
    # Returns a listing of roles and permissions for a user.
    api_response = api_instance.get_user_roles(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->get_user_roles: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID | |
{: class="table table-striped"}

### Return type

[**UserAuthorization**](UserAuthorization.html)

<a name="patch_authorization_role"></a>

## [**DomainOrganizationRole**](DomainOrganizationRole.html) patch_authorization_role(role_id, body)

Patch Organization Role for needsUpdate Field

Patch Organization Role for needsUpdate Field

Wraps PATCH /api/v2/authorization/roles/{roleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
role_id = 'role_id_example' # str | Role ID
body = PureCloudPlatformClientV2.DomainOrganizationRole() # DomainOrganizationRole | Organization role

try:
    # Patch Organization Role for needsUpdate Field
    api_response = api_instance.patch_authorization_role(role_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->patch_authorization_role: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID | |
| **body** | [**DomainOrganizationRole**](DomainOrganizationRole.html)| Organization role | |
{: class="table table-striped"}

### Return type

[**DomainOrganizationRole**](DomainOrganizationRole.html)

<a name="post_authorization_role_comparedefault_right_role_id"></a>

## [**DomainOrgRoleDifference**](DomainOrgRoleDifference.html) post_authorization_role_comparedefault_right_role_id(left_role_id, right_role_id, body)

Get an unsaved org role to default role comparison

Allows users to compare their existing roles in an unsaved state to its default role

Wraps POST /api/v2/authorization/roles/{leftRoleId}/comparedefault/{rightRoleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
left_role_id = 'left_role_id_example' # str | Left Role ID
right_role_id = 'right_role_id_example' # str | Right Role id
body = PureCloudPlatformClientV2.DomainOrganizationRole() # DomainOrganizationRole | Organization role

try:
    # Get an unsaved org role to default role comparison
    api_response = api_instance.post_authorization_role_comparedefault_right_role_id(left_role_id, right_role_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->post_authorization_role_comparedefault_right_role_id: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **left_role_id** | **str**| Left Role ID | |
| **right_role_id** | **str**| Right Role id | |
| **body** | [**DomainOrganizationRole**](DomainOrganizationRole.html)| Organization role | |
{: class="table table-striped"}

### Return type

[**DomainOrgRoleDifference**](DomainOrgRoleDifference.html)

<a name="post_authorization_roles"></a>

## [**DomainOrganizationRole**](DomainOrganizationRole.html) post_authorization_roles(body)

Create an organization role.



Wraps POST /api/v2/authorization/roles 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
body = PureCloudPlatformClientV2.DomainOrganizationRoleCreate() # DomainOrganizationRoleCreate | Organization role

try:
    # Create an organization role.
    api_response = api_instance.post_authorization_roles(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->post_authorization_roles: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DomainOrganizationRoleCreate**](DomainOrganizationRoleCreate.html)| Organization role | |
{: class="table table-striped"}

### Return type

[**DomainOrganizationRole**](DomainOrganizationRole.html)

<a name="post_authorization_roles_default"></a>

## [**OrganizationRoleEntityListing**](OrganizationRoleEntityListing.html) post_authorization_roles_default(force=force)

Restores all default roles

This endpoint serves several purposes. 1. It provides the org with default roles. This is important for default roles that will be added after go-live (they can retroactively add the new default-role). Note: When not using a query param of force=true, it only adds the default roles not configured for the org; it does not overwrite roles. 2. Using the query param force=true, you can restore all default roles. Note: This does not have an effect on custom roles.

Wraps POST /api/v2/authorization/roles/default 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
force = false # bool | Restore default roles (optional) (default to false)

try:
    # Restores all default roles
    api_response = api_instance.post_authorization_roles_default(force=force)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->post_authorization_roles_default: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **force** | **bool**| Restore default roles | [optional] [default to false]|
{: class="table table-striped"}

### Return type

[**OrganizationRoleEntityListing**](OrganizationRoleEntityListing.html)

<a name="put_authorization_role"></a>

## [**DomainOrganizationRole**](DomainOrganizationRole.html) put_authorization_role(role_id, body)

Update an organization role.

Update

Wraps PUT /api/v2/authorization/roles/{roleId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
role_id = 'role_id_example' # str | Role ID
body = PureCloudPlatformClientV2.DomainOrganizationRoleUpdate() # DomainOrganizationRoleUpdate | Organization role

try:
    # Update an organization role.
    api_response = api_instance.put_authorization_role(role_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->put_authorization_role: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID | |
| **body** | [**DomainOrganizationRoleUpdate**](DomainOrganizationRoleUpdate.html)| Organization role | |
{: class="table table-striped"}

### Return type

[**DomainOrganizationRole**](DomainOrganizationRole.html)

<a name="put_authorization_role_users_add"></a>

## list[str]** put_authorization_role_users_add(role_id, body)

Sets the users for the role



Wraps PUT /api/v2/authorization/roles/{roleId}/users/add 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
role_id = 'role_id_example' # str | Role ID
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | List of user IDs

try:
    # Sets the users for the role
    api_response = api_instance.put_authorization_role_users_add(role_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->put_authorization_role_users_add: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID | |
| **body** | **list[str]**| List of user IDs | |
{: class="table table-striped"}

### Return type

**list[str]**

<a name="put_authorization_role_users_remove"></a>

## list[str]** put_authorization_role_users_remove(role_id, body)

Removes the users from the role



Wraps PUT /api/v2/authorization/roles/{roleId}/users/remove 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
role_id = 'role_id_example' # str | Role ID
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | List of user IDs

try:
    # Removes the users from the role
    api_response = api_instance.put_authorization_role_users_remove(role_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->put_authorization_role_users_remove: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID | |
| **body** | **list[str]**| List of user IDs | |
{: class="table table-striped"}

### Return type

**list[str]**

<a name="put_authorization_roles_default"></a>

## [**OrganizationRoleEntityListing**](OrganizationRoleEntityListing.html) put_authorization_roles_default(body)

Restore specified default roles



Wraps PUT /api/v2/authorization/roles/default 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
body = [PureCloudPlatformClientV2.DomainOrganizationRole()] # list[DomainOrganizationRole] | Organization roles list

try:
    # Restore specified default roles
    api_response = api_instance.put_authorization_roles_default(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->put_authorization_roles_default: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**list[DomainOrganizationRole]**](DomainOrganizationRole.html)| Organization roles list | |
{: class="table table-striped"}

### Return type

[**OrganizationRoleEntityListing**](OrganizationRoleEntityListing.html)

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
user_id = 'user_id_example' # str | User ID
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | List of roles

try:
    # Sets the user's roles
    api_response = api_instance.put_user_roles(user_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthorizationApi->put_user_roles: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID | |
| **body** | **list[str]**| List of roles | |
{: class="table table-striped"}

### Return type

[**UserAuthorization**](UserAuthorization.html)


---
title: AuthorizationApi
---

## PureCloudPlatformClientV2.AuthorizationApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_authorization_division**](AuthorizationApi.html#delete_authorization_division) | Delete a division.|
|[**delete_authorization_role**](AuthorizationApi.html#delete_authorization_role) | Delete an organization role.|
|[**delete_authorization_subject_division_role**](AuthorizationApi.html#delete_authorization_subject_division_role) | Delete a grant of a role in a division|
|[**get_authorization_division**](AuthorizationApi.html#get_authorization_division) | Returns an authorization division.|
|[**get_authorization_division_grants**](AuthorizationApi.html#get_authorization_division_grants) | Gets all grants for a given division.|
|[**get_authorization_divisions**](AuthorizationApi.html#get_authorization_divisions) | Retrieve a list of all divisions defined for the organization|
|[**get_authorization_divisions_home**](AuthorizationApi.html#get_authorization_divisions_home) | Retrieve the home division for the organization.|
|[**get_authorization_divisions_limit**](AuthorizationApi.html#get_authorization_divisions_limit) | Returns the maximum allowed number of divisions.|
|[**get_authorization_divisionspermitted_me**](AuthorizationApi.html#get_authorization_divisionspermitted_me) | Returns which divisions the current user has the given permission in.|
|[**get_authorization_divisionspermitted_paged_me**](AuthorizationApi.html#get_authorization_divisionspermitted_paged_me) | Returns which divisions the current user has the given permission in.|
|[**get_authorization_divisionspermitted_paged_subject_id**](AuthorizationApi.html#get_authorization_divisionspermitted_paged_subject_id) | Returns which divisions the specified user has the given permission in.|
|[**get_authorization_permissions**](AuthorizationApi.html#get_authorization_permissions) | Get all permissions.|
|[**get_authorization_products**](AuthorizationApi.html#get_authorization_products) | Get the list of enabled products|
|[**get_authorization_role**](AuthorizationApi.html#get_authorization_role) | Get a single organization role.|
|[**get_authorization_role_comparedefault_right_role_id**](AuthorizationApi.html#get_authorization_role_comparedefault_right_role_id) | Get an org role to default role comparison|
|[**get_authorization_role_subjectgrants**](AuthorizationApi.html#get_authorization_role_subjectgrants) | Get the subjects&#39; granted divisions in the specified role.|
|[**get_authorization_role_users**](AuthorizationApi.html#get_authorization_role_users) | Get a list of the users in a specified role.|
|[**get_authorization_roles**](AuthorizationApi.html#get_authorization_roles) | Retrieve a list of all roles defined for the organization|
|[**get_authorization_subject**](AuthorizationApi.html#get_authorization_subject) | Returns a listing of roles and permissions for a user.|
|[**get_authorization_subjects_me**](AuthorizationApi.html#get_authorization_subjects_me) | Returns a listing of roles and permissions for the currently authenticated user.|
|[**get_authorization_subjects_rolecounts**](AuthorizationApi.html#get_authorization_subjects_rolecounts) | Get the count of roles granted to a list of subjects|
|[**get_user_roles**](AuthorizationApi.html#get_user_roles) | Returns a listing of roles and permissions for a user.|
|[**patch_authorization_role**](AuthorizationApi.html#patch_authorization_role) | Patch Organization Role for needsUpdate Field|
|[**post_authorization_division_object**](AuthorizationApi.html#post_authorization_division_object) | Assign a list of objects to a division|
|[**post_authorization_division_restore**](AuthorizationApi.html#post_authorization_division_restore) | Recreate a previously deleted division.|
|[**post_authorization_divisions**](AuthorizationApi.html#post_authorization_divisions) | Create a division.|
|[**post_authorization_role**](AuthorizationApi.html#post_authorization_role) | Bulk-grant subjects and divisions with an organization role.|
|[**post_authorization_role_comparedefault_right_role_id**](AuthorizationApi.html#post_authorization_role_comparedefault_right_role_id) | Get an unsaved org role to default role comparison|
|[**post_authorization_roles**](AuthorizationApi.html#post_authorization_roles) | Create an organization role.|
|[**post_authorization_roles_default**](AuthorizationApi.html#post_authorization_roles_default) | Restores all default roles|
|[**post_authorization_subject_bulkadd**](AuthorizationApi.html#post_authorization_subject_bulkadd) | Bulk-grant roles and divisions to a subject.|
|[**post_authorization_subject_bulkremove**](AuthorizationApi.html#post_authorization_subject_bulkremove) | Bulk-remove grants from a subject.|
|[**post_authorization_subject_bulkreplace**](AuthorizationApi.html#post_authorization_subject_bulkreplace) | Replace subject&#39;s roles and divisions with the exact list supplied in the request.|
|[**post_authorization_subject_division_role**](AuthorizationApi.html#post_authorization_subject_division_role) | Make a grant of a role in a division|
|[**put_authorization_division**](AuthorizationApi.html#put_authorization_division) | Update a division.|
|[**put_authorization_role**](AuthorizationApi.html#put_authorization_role) | Update an organization role.|
|[**put_authorization_role_users_add**](AuthorizationApi.html#put_authorization_role_users_add) | Sets the users for the role|
|[**put_authorization_role_users_remove**](AuthorizationApi.html#put_authorization_role_users_remove) | Removes the users from the role|
|[**put_authorization_roles_default**](AuthorizationApi.html#put_authorization_roles_default) | Restore specified default roles|
|[**put_user_roles**](AuthorizationApi.html#put_user_roles) | Sets the user&#39;s roles|
{: class="table table-striped"}

<a name="delete_authorization_division"></a>

##  delete_authorization_division(division_id, force=force)



Delete a division.



Wraps DELETE /api/v2/authorization/divisions/{divisionId} 

Requires ANY permissions: 

* authorization:division:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
division_id = 'division_id_example' # str | Division ID
force = false # bool | Force delete this division as well as the grants and objects associated with it (optional) (default to false)

try:
    # Delete a division.
    api_instance.delete_authorization_division(division_id, force=force)
except ApiException as e:
    print("Exception when calling AuthorizationApi->delete_authorization_division: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | **str**| Division ID |  |
| **force** | **bool**| Force delete this division as well as the grants and objects associated with it | [optional] [default to false] |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_authorization_role"></a>

##  delete_authorization_role(role_id)



Delete an organization role.



Wraps DELETE /api/v2/authorization/roles/{roleId} 

Requires ANY permissions: 

* authorization:role:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
role_id = 'role_id_example' # str | Role ID

try:
    # Delete an organization role.
    api_instance.delete_authorization_role(role_id)
except ApiException as e:
    print("Exception when calling AuthorizationApi->delete_authorization_role: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID |  |
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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
division_id = 'division_id_example' # str | the id of the division of the grant
role_id = 'role_id_example' # str | the id of the role of the grant

try:
    # Delete a grant of a role in a division
    api_instance.delete_authorization_subject_division_role(subject_id, division_id, role_id)
except ApiException as e:
    print("Exception when calling AuthorizationApi->delete_authorization_subject_division_role: %s\n" % e)
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

<a name="get_authorization_division"></a>

## [**AuthzDivision**](AuthzDivision.html) get_authorization_division(division_id, object_count=object_count)



Returns an authorization division.



Wraps GET /api/v2/authorization/divisions/{divisionId} 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
division_id = 'division_id_example' # str | Division ID
object_count = false # bool | Get count of objects in this division, grouped by type (optional) (default to false)

try:
    # Returns an authorization division.
    api_response = api_instance.get_authorization_division(division_id, object_count=object_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_division: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | **str**| Division ID |  |
| **object_count** | **bool**| Get count of objects in this division, grouped by type | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**AuthzDivision**](AuthzDivision.html)

<a name="get_authorization_division_grants"></a>

## [**AuthzDivisionGrantEntityListing**](AuthzDivisionGrantEntityListing.html) get_authorization_division_grants(division_id, page_number=page_number, page_size=page_size)



Gets all grants for a given division.

Returns all grants assigned to a given division. Maximum page size is 500.

Wraps GET /api/v2/authorization/divisions/{divisionId}/grants 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
division_id = 'division_id_example' # str | Division ID
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Gets all grants for a given division.
    api_response = api_instance.get_authorization_division_grants(division_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_division_grants: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | **str**| Division ID |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**AuthzDivisionGrantEntityListing**](AuthzDivisionGrantEntityListing.html)

<a name="get_authorization_divisions"></a>

## [**AuthzDivisionEntityListing**](AuthzDivisionEntityListing.html) get_authorization_divisions(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, object_count=object_count, id=id, name=name)



Retrieve a list of all divisions defined for the organization

Request specific divisions by id using a query param \"id\", e.g.  ?id=5f777167-63be-4c24-ad41-374155d9e28b&id=72e9fb25-c484-488d-9312-7acba82435b3

Wraps GET /api/v2/authorization/divisions 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
object_count = false # bool | Include the count of objects contained in the division (optional) (default to false)
id = ['id_example'] # list[str] | Optionally request specific divisions by their IDs (optional)
name = 'name_example' # str | Search term to filter by division name (optional)

try:
    # Retrieve a list of all divisions defined for the organization
    api_response = api_instance.get_authorization_divisions(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, object_count=object_count, id=id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_divisions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **object_count** | **bool**| Include the count of objects contained in the division | [optional] [default to false] |
| **id** | [**list[str]**](str.html)| Optionally request specific divisions by their IDs | [optional]  |
| **name** | **str**| Search term to filter by division name | [optional]  |
{: class="table table-striped"}

### Return type

[**AuthzDivisionEntityListing**](AuthzDivisionEntityListing.html)

<a name="get_authorization_divisions_home"></a>

## [**AuthzDivision**](AuthzDivision.html) get_authorization_divisions_home()



Retrieve the home division for the organization.

Will not include object counts.

Wraps GET /api/v2/authorization/divisions/home 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()

try:
    # Retrieve the home division for the organization.
    api_response = api_instance.get_authorization_divisions_home()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_divisions_home: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**AuthzDivision**](AuthzDivision.html)

<a name="get_authorization_divisions_limit"></a>

## int** get_authorization_divisions_limit()



Returns the maximum allowed number of divisions.



Wraps GET /api/v2/authorization/divisions/limit 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()

try:
    # Returns the maximum allowed number of divisions.
    api_response = api_instance.get_authorization_divisions_limit()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_divisions_limit: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

**int**

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
permission = 'permission_example' # str | The permission string, including the object to access, e.g. routing:queue:view
name = 'name_example' # str | Search term to filter by division name (optional)

try:
    # Returns which divisions the current user has the given permission in.
    api_response = api_instance.get_authorization_divisionspermitted_me(permission, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_divisionspermitted_me: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
permission = 'permission_example' # str | The permission string, including the object to access, e.g. routing:queue:view
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Returns which divisions the current user has the given permission in.
    api_response = api_instance.get_authorization_divisionspermitted_paged_me(permission, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_divisionspermitted_paged_me: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
permission = 'permission_example' # str | The permission string, including the object to access, e.g. routing:queue:view
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Returns which divisions the specified user has the given permission in.
    api_response = api_instance.get_authorization_divisionspermitted_paged_subject_id(subject_id, permission, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_divisionspermitted_paged_subject_id: %s\n" % e)
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

<a name="get_authorization_permissions"></a>

## [**PermissionCollectionEntityListing**](PermissionCollectionEntityListing.html) get_authorization_permissions(page_size=page_size, page_number=page_number, query_type=query_type, query=query)



Get all permissions.

Retrieve a list of all permission defined in the system.

Wraps GET /api/v2/authorization/permissions 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
query_type = 'query_type_example' # str | Query filter type (optional)
query = 'query_example' # str | Comma-separated list of permissions or domains to query (optional)

try:
    # Get all permissions.
    api_response = api_instance.get_authorization_permissions(page_size=page_size, page_number=page_number, query_type=query_type, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_permissions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **query_type** | **str**| Query filter type | [optional] <br />**Values**: domain, permission |
| **query** | **str**| Comma-separated list of permissions or domains to query | [optional]  |
{: class="table table-striped"}

### Return type

[**PermissionCollectionEntityListing**](PermissionCollectionEntityListing.html)

<a name="get_authorization_products"></a>

## [**OrganizationProductEntityListing**](OrganizationProductEntityListing.html) get_authorization_products()



Get the list of enabled products

Gets the list of enabled products. Some example product names are: collaborateFree, collaboratePro, communicate, and engage.

Wraps GET /api/v2/authorization/products 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()

try:
    # Get the list of enabled products
    api_response = api_instance.get_authorization_products()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_products: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**OrganizationProductEntityListing**](OrganizationProductEntityListing.html)

<a name="get_authorization_role"></a>

## [**DomainOrganizationRole**](DomainOrganizationRole.html) get_authorization_role(role_id, expand=expand)



Get a single organization role.

Get the organization role specified by its ID.

Wraps GET /api/v2/authorization/roles/{roleId} 

Requires ANY permissions: 

* authorization:role:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
role_id = 'role_id_example' # str | Role ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. \"unusedPermissions\" returns the permissions not used for the role (optional)

try:
    # Get a single organization role.
    api_response = api_instance.get_authorization_role(role_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_role: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand. \&quot;unusedPermissions\&quot; returns the permissions not used for the role | [optional] <br />**Values**: unusedPermissions |
{: class="table table-striped"}

### Return type

[**DomainOrganizationRole**](DomainOrganizationRole.html)

<a name="get_authorization_role_comparedefault_right_role_id"></a>

## [**DomainOrgRoleDifference**](DomainOrgRoleDifference.html) get_authorization_role_comparedefault_right_role_id(left_role_id, right_role_id)



Get an org role to default role comparison

Compares any organization role to a default role id and show differences

Wraps GET /api/v2/authorization/roles/{leftRoleId}/comparedefault/{rightRoleId} 

Requires ANY permissions: 

* authorization:role:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
left_role_id = 'left_role_id_example' # str | Left Role ID
right_role_id = 'right_role_id_example' # str | Right Role id

try:
    # Get an org role to default role comparison
    api_response = api_instance.get_authorization_role_comparedefault_right_role_id(left_role_id, right_role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_role_comparedefault_right_role_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **left_role_id** | **str**| Left Role ID |  |
| **right_role_id** | **str**| Right Role id |  |
{: class="table table-striped"}

### Return type

[**DomainOrgRoleDifference**](DomainOrgRoleDifference.html)

<a name="get_authorization_role_subjectgrants"></a>

## [**SubjectDivisionGrantsEntityListing**](SubjectDivisionGrantsEntityListing.html) get_authorization_role_subjectgrants(role_id, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)



Get the subjects' granted divisions in the specified role.

Includes the divisions for which the subject has a grant.

Wraps GET /api/v2/authorization/roles/{roleId}/subjectgrants 

Requires ANY permissions: 

* authorization:role:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
role_id = 'role_id_example' # str | Role ID
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)

try:
    # Get the subjects' granted divisions in the specified role.
    api_response = api_instance.get_authorization_role_subjectgrants(role_id, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_role_subjectgrants: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID |  |
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
{: class="table table-striped"}

### Return type

[**SubjectDivisionGrantsEntityListing**](SubjectDivisionGrantsEntityListing.html)

<a name="get_authorization_role_users"></a>

## [**UserEntityListing**](UserEntityListing.html) get_authorization_role_users(role_id, page_size=page_size, page_number=page_number)



Get a list of the users in a specified role.

Get an array of the UUIDs of the users in the specified role.

Wraps GET /api/v2/authorization/roles/{roleId}/users 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
role_id = 'role_id_example' # str | Role ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of the users in a specified role.
    api_response = api_instance.get_authorization_role_users(role_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_role_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**UserEntityListing**](UserEntityListing.html)

<a name="get_authorization_roles"></a>

## [**OrganizationRoleEntityListing**](OrganizationRoleEntityListing.html) get_authorization_roles(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, name=name, permission=permission, default_role_id=default_role_id, user_count=user_count, id=id)



Retrieve a list of all roles defined for the organization



Wraps GET /api/v2/authorization/roles 

Requires ANY permissions: 

* authorization:role:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
name = 'name_example' # str |  (optional)
permission = ['permission_example'] # list[str] |  (optional)
default_role_id = ['default_role_id_example'] # list[str] |  (optional)
user_count = true # bool |  (optional) (default to true)
id = ['id_example'] # list[str] | id (optional)

try:
    # Retrieve a list of all roles defined for the organization
    api_response = api_instance.get_authorization_roles(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, name=name, permission=permission, default_role_id=default_role_id, user_count=user_count, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[str]**](str.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **name** | **str**|  | [optional]  |
| **permission** | [**list[str]**](str.html)|  | [optional]  |
| **default_role_id** | [**list[str]**](str.html)|  | [optional]  |
| **user_count** | **bool**|  | [optional] [default to true] |
| **id** | [**list[str]**](str.html)| id | [optional]  |
{: class="table table-striped"}

### Return type

[**OrganizationRoleEntityListing**](OrganizationRoleEntityListing.html)

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)

try:
    # Returns a listing of roles and permissions for a user.
    api_response = api_instance.get_authorization_subject(subject_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_subject: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()

try:
    # Returns a listing of roles and permissions for the currently authenticated user.
    api_response = api_instance.get_authorization_subjects_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_subjects_me: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**AuthzSubject**](AuthzSubject.html)

<a name="get_authorization_subjects_rolecounts"></a>

## [**dict(str, object)**](dict.html) get_authorization_subjects_rolecounts(id=id)



Get the count of roles granted to a list of subjects



Wraps GET /api/v2/authorization/subjects/rolecounts 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
id = ['id_example'] # list[str] | id (optional)

try:
    # Get the count of roles granted to a list of subjects
    api_response = api_instance.get_authorization_subjects_rolecounts(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_subjects_rolecounts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str.html)| id | [optional]  |
{: class="table table-striped"}

### Return type

[**dict(str, object)**](dict.html)

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
user_id = 'user_id_example' # str | User ID

try:
    # Returns a listing of roles and permissions for a user.
    api_response = api_instance.get_user_roles(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_user_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

[**UserAuthorization**](UserAuthorization.html)

<a name="patch_authorization_role"></a>

## [**DomainOrganizationRole**](DomainOrganizationRole.html) patch_authorization_role(role_id, body)



Patch Organization Role for needsUpdate Field

Patch Organization Role for needsUpdate Field

Wraps PATCH /api/v2/authorization/roles/{roleId} 

Requires ANY permissions: 

* authorization:role:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling AuthorizationApi->patch_authorization_role: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID |  |
| **body** | [**DomainOrganizationRole**](DomainOrganizationRole.html)| Organization role |  |
{: class="table table-striped"}

### Return type

[**DomainOrganizationRole**](DomainOrganizationRole.html)

<a name="post_authorization_division_object"></a>

##  post_authorization_division_object(division_id, object_type, body)



Assign a list of objects to a division

Set the division of a specified list of objects. The objects must all be of the same type, one of:  CAMPAIGN, MANAGEMENTUNIT, FLOW, QUEUE, DATATABLES or USER.  The body of the request is a list of object IDs, which are expected to be  GUIDs, e.g. [\"206ce31f-61ec-40ed-a8b1-be6f06303998\",\"250a754e-f5e4-4f51-800f-a92f09d3bf8c\"]

Wraps POST /api/v2/authorization/divisions/{divisionId}/objects/{objectType} 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
division_id = 'division_id_example' # str | Division ID
object_type = 'object_type_example' # str | The type of the objects. Must be one of the valid object types
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | Object Id List

try:
    # Assign a list of objects to a division
    api_instance.post_authorization_division_object(division_id, object_type, body)
except ApiException as e:
    print("Exception when calling AuthorizationApi->post_authorization_division_object: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | **str**| Division ID |  |
| **object_type** | **str**| The type of the objects. Must be one of the valid object types | <br />**Values**: QUEUE, CAMPAIGN, CONTACTLIST, DNCLIST, EMAILCAMPAIGN, MESSAGINGCAMPAIGN, MANAGEMENTUNIT, BUSINESSUNIT, FLOW, FLOWMILESTONE, FLOWOUTCOME, USER, CALLROUTE, EMERGENCYGROUPS, ROUTINGSCHEDULES, ROUTINGSCHEDULEGROUPS, DATATABLES, TEAM, WORKBIN, WORKTYPE |
| **body** | **list[str]**| Object Id List |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_authorization_division_restore"></a>

## [**AuthzDivision**](AuthzDivision.html) post_authorization_division_restore(division_id, body)



Recreate a previously deleted division.



Wraps POST /api/v2/authorization/divisions/{divisionId}/restore 

Requires ANY permissions: 

* authorization:division:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
division_id = 'division_id_example' # str | Division ID
body = PureCloudPlatformClientV2.AuthzDivision() # AuthzDivision | Recreated division data

try:
    # Recreate a previously deleted division.
    api_response = api_instance.post_authorization_division_restore(division_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->post_authorization_division_restore: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | **str**| Division ID |  |
| **body** | [**AuthzDivision**](AuthzDivision.html)| Recreated division data |  |
{: class="table table-striped"}

### Return type

[**AuthzDivision**](AuthzDivision.html)

<a name="post_authorization_divisions"></a>

## [**AuthzDivision**](AuthzDivision.html) post_authorization_divisions(body)



Create a division.



Wraps POST /api/v2/authorization/divisions 

Requires ALL permissions: 

* authorization:division:add
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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
body = PureCloudPlatformClientV2.AuthzDivision() # AuthzDivision | Division

try:
    # Create a division.
    api_response = api_instance.post_authorization_divisions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->post_authorization_divisions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AuthzDivision**](AuthzDivision.html)| Division |  |
{: class="table table-striped"}

### Return type

[**AuthzDivision**](AuthzDivision.html)

<a name="post_authorization_role"></a>

##  post_authorization_role(role_id, body, subject_type=subject_type)



Bulk-grant subjects and divisions with an organization role.



Wraps POST /api/v2/authorization/roles/{roleId} 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
role_id = 'role_id_example' # str | Role ID
body = PureCloudPlatformClientV2.SubjectDivisions() # SubjectDivisions | Subjects and Divisions
subject_type = 'PC_USER' # str | what the type of the subjects are (PC_GROUP, PC_USER or PC_OAUTH_CLIENT) (optional) (default to PC_USER)

try:
    # Bulk-grant subjects and divisions with an organization role.
    api_instance.post_authorization_role(role_id, body, subject_type=subject_type)
except ApiException as e:
    print("Exception when calling AuthorizationApi->post_authorization_role: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID |  |
| **body** | [**SubjectDivisions**](SubjectDivisions.html)| Subjects and Divisions |  |
| **subject_type** | **str**| what the type of the subjects are (PC_GROUP, PC_USER or PC_OAUTH_CLIENT) | [optional] [default to PC_USER] |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_authorization_role_comparedefault_right_role_id"></a>

## [**DomainOrgRoleDifference**](DomainOrgRoleDifference.html) post_authorization_role_comparedefault_right_role_id(left_role_id, right_role_id, body)



Get an unsaved org role to default role comparison

Allows users to compare their existing roles in an unsaved state to its default role

Wraps POST /api/v2/authorization/roles/{leftRoleId}/comparedefault/{rightRoleId} 

Requires ANY permissions: 

* authorization:role:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling AuthorizationApi->post_authorization_role_comparedefault_right_role_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **left_role_id** | **str**| Left Role ID |  |
| **right_role_id** | **str**| Right Role id |  |
| **body** | [**DomainOrganizationRole**](DomainOrganizationRole.html)| Organization role |  |
{: class="table table-striped"}

### Return type

[**DomainOrgRoleDifference**](DomainOrgRoleDifference.html)

<a name="post_authorization_roles"></a>

## [**DomainOrganizationRole**](DomainOrganizationRole.html) post_authorization_roles(body)



Create an organization role.



Wraps POST /api/v2/authorization/roles 

Requires ANY permissions: 

* authorization:role:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
body = PureCloudPlatformClientV2.DomainOrganizationRoleCreate() # DomainOrganizationRoleCreate | Organization role

try:
    # Create an organization role.
    api_response = api_instance.post_authorization_roles(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->post_authorization_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DomainOrganizationRoleCreate**](DomainOrganizationRoleCreate.html)| Organization role |  |
{: class="table table-striped"}

### Return type

[**DomainOrganizationRole**](DomainOrganizationRole.html)

<a name="post_authorization_roles_default"></a>

## [**OrganizationRoleEntityListing**](OrganizationRoleEntityListing.html) post_authorization_roles_default(force=force)



Restores all default roles

This endpoint serves several purposes. 1. It provides the org with default roles. This is important for default roles that will be added after go-live (they can retroactively add the new default-role). Note: When not using a query param of force=true, it only adds the default roles not configured for the org; it does not overwrite roles. 2. Using the query param force=true, you can restore all default roles. Note: This does not have an effect on custom roles.

Wraps POST /api/v2/authorization/roles/default 

Requires ANY permissions: 

* authorization:role:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
force = false # bool | Restore default roles (optional) (default to false)

try:
    # Restores all default roles
    api_response = api_instance.post_authorization_roles_default(force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->post_authorization_roles_default: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **force** | **bool**| Restore default roles | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**OrganizationRoleEntityListing**](OrganizationRoleEntityListing.html)

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
body = PureCloudPlatformClientV2.RoleDivisionGrants() # RoleDivisionGrants | Pairs of role and division IDs
subject_type = 'PC_USER' # str | what the type of the subject is (PC_GROUP, PC_USER or PC_OAUTH_CLIENT) (optional) (default to PC_USER)

try:
    # Bulk-grant roles and divisions to a subject.
    api_instance.post_authorization_subject_bulkadd(subject_id, body, subject_type=subject_type)
except ApiException as e:
    print("Exception when calling AuthorizationApi->post_authorization_subject_bulkadd: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
body = PureCloudPlatformClientV2.RoleDivisionGrants() # RoleDivisionGrants | Pairs of role and division IDs

try:
    # Bulk-remove grants from a subject.
    api_instance.post_authorization_subject_bulkremove(subject_id, body)
except ApiException as e:
    print("Exception when calling AuthorizationApi->post_authorization_subject_bulkremove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **subject_id** | **str**| Subject ID (user or group) |  |
| **body** | [**RoleDivisionGrants**](RoleDivisionGrants.html)| Pairs of role and division IDs |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_authorization_subject_bulkreplace"></a>

##  post_authorization_subject_bulkreplace(subject_id, body, subject_type=subject_type)



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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
body = PureCloudPlatformClientV2.RoleDivisionGrants() # RoleDivisionGrants | Pairs of role and division IDs
subject_type = 'PC_USER' # str | what the type of the subject is (PC_GROUP, PC_USER or PC_OAUTH_CLIENT) (optional) (default to PC_USER)

try:
    # Replace subject's roles and divisions with the exact list supplied in the request.
    api_instance.post_authorization_subject_bulkreplace(subject_id, body, subject_type=subject_type)
except ApiException as e:
    print("Exception when calling AuthorizationApi->post_authorization_subject_bulkreplace: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
division_id = 'division_id_example' # str | the id of the division to which to make the grant
role_id = 'role_id_example' # str | the id of the role to grant
subject_type = 'PC_USER' # str | what the type of the subject is: PC_GROUP, PC_USER or PC_OAUTH_CLIENT (note: for cross-org authorization, please use the Organization Authorization endpoints) (optional) (default to PC_USER)

try:
    # Make a grant of a role in a division
    api_instance.post_authorization_subject_division_role(subject_id, division_id, role_id, subject_type=subject_type)
except ApiException as e:
    print("Exception when calling AuthorizationApi->post_authorization_subject_division_role: %s\n" % e)
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

<a name="put_authorization_division"></a>

## [**AuthzDivision**](AuthzDivision.html) put_authorization_division(division_id, body)



Update a division.



Wraps PUT /api/v2/authorization/divisions/{divisionId} 

Requires ANY permissions: 

* authorization:division:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
division_id = 'division_id_example' # str | Division ID
body = PureCloudPlatformClientV2.AuthzDivision() # AuthzDivision | Updated division data

try:
    # Update a division.
    api_response = api_instance.put_authorization_division(division_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->put_authorization_division: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | **str**| Division ID |  |
| **body** | [**AuthzDivision**](AuthzDivision.html)| Updated division data |  |
{: class="table table-striped"}

### Return type

[**AuthzDivision**](AuthzDivision.html)

<a name="put_authorization_role"></a>

## [**DomainOrganizationRole**](DomainOrganizationRole.html) put_authorization_role(role_id, body)



Update an organization role.

Update

Wraps PUT /api/v2/authorization/roles/{roleId} 

Requires ANY permissions: 

* authorization:role:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling AuthorizationApi->put_authorization_role: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID |  |
| **body** | [**DomainOrganizationRoleUpdate**](DomainOrganizationRoleUpdate.html)| Organization role |  |
{: class="table table-striped"}

### Return type

[**DomainOrganizationRole**](DomainOrganizationRole.html)

<a name="put_authorization_role_users_add"></a>

## list[str]** put_authorization_role_users_add(role_id, body)



Sets the users for the role



Wraps PUT /api/v2/authorization/roles/{roleId}/users/add 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
role_id = 'role_id_example' # str | Role ID
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | List of user IDs

try:
    # Sets the users for the role
    api_response = api_instance.put_authorization_role_users_add(role_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->put_authorization_role_users_add: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID |  |
| **body** | **list[str]**| List of user IDs |  |
{: class="table table-striped"}

### Return type

**list[str]**

<a name="put_authorization_role_users_remove"></a>

## list[str]** put_authorization_role_users_remove(role_id, body)



Removes the users from the role



Wraps PUT /api/v2/authorization/roles/{roleId}/users/remove 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
role_id = 'role_id_example' # str | Role ID
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | List of user IDs

try:
    # Removes the users from the role
    api_response = api_instance.put_authorization_role_users_remove(role_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->put_authorization_role_users_remove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID |  |
| **body** | **list[str]**| List of user IDs |  |
{: class="table table-striped"}

### Return type

**list[str]**

<a name="put_authorization_roles_default"></a>

## [**OrganizationRoleEntityListing**](OrganizationRoleEntityListing.html) put_authorization_roles_default(body)



Restore specified default roles



Wraps PUT /api/v2/authorization/roles/default 

Requires ANY permissions: 

* authorization:role:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
body = [PureCloudPlatformClientV2.DomainOrganizationRole()] # list[DomainOrganizationRole] | Organization roles list

try:
    # Restore specified default roles
    api_response = api_instance.put_authorization_roles_default(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->put_authorization_roles_default: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**list[DomainOrganizationRole]**](DomainOrganizationRole.html)| Organization roles list |  |
{: class="table table-striped"}

### Return type

[**OrganizationRoleEntityListing**](OrganizationRoleEntityListing.html)

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
user_id = 'user_id_example' # str | User ID
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | List of roles

try:
    # Sets the user's roles
    api_response = api_instance.put_user_roles(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->put_user_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | **list[str]**| List of roles |  |
{: class="table table-striped"}

### Return type

[**UserAuthorization**](UserAuthorization.html)


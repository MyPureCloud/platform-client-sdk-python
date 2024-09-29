# AuthorizationApi

## PureCloudPlatformClientV2.AuthorizationApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_authorization_division**](#delete_authorization_division) | Delete a division.|
|[**delete_authorization_role**](#delete_authorization_role) | Delete an organization role.|
|[**delete_authorization_subject_division_role**](#delete_authorization_subject_division_role) | Delete a grant of a role in a division|
|[**get_authorization_division**](#get_authorization_division) | Returns an authorization division.|
|[**get_authorization_division_grants**](#get_authorization_division_grants) | Gets all grants for a given division.|
|[**get_authorization_divisions**](#get_authorization_divisions) | Retrieve a list of all divisions defined for the organization|
|[**get_authorization_divisions_home**](#get_authorization_divisions_home) | Retrieve the home division for the organization.|
|[**get_authorization_divisions_limit**](#get_authorization_divisions_limit) | Returns the maximum allowed number of divisions.|
|[**get_authorization_divisionspermitted_me**](#get_authorization_divisionspermitted_me) | Returns which divisions the current user has the given permission in.|
|[**get_authorization_divisionspermitted_paged_me**](#get_authorization_divisionspermitted_paged_me) | Returns which divisions the current user has the given permission in.|
|[**get_authorization_divisionspermitted_paged_subject_id**](#get_authorization_divisionspermitted_paged_subject_id) | Returns which divisions the specified user has the given permission in.|
|[**get_authorization_permissions**](#get_authorization_permissions) | Get all permissions.|
|[**get_authorization_products**](#get_authorization_products) | Get the list of enabled products|
|[**get_authorization_role**](#get_authorization_role) | Get a single organization role.|
|[**get_authorization_role_comparedefault_right_role_id**](#get_authorization_role_comparedefault_right_role_id) | Get an org role to default role comparison|
|[**get_authorization_role_subjectgrants**](#get_authorization_role_subjectgrants) | Get the subjects&#39; granted divisions in the specified role.|
|[**get_authorization_role_users**](#get_authorization_role_users) | Get a list of the users in a specified role.|
|[**get_authorization_roles**](#get_authorization_roles) | Retrieve a list of all roles defined for the organization|
|[**get_authorization_roles_settings**](#get_authorization_roles_settings) | Get authorization role settings|
|[**get_authorization_settings**](#get_authorization_settings) | Get authorization settings|
|[**get_authorization_subject**](#get_authorization_subject) | Returns a listing of roles and permissions for a user.|
|[**get_authorization_subjects_me**](#get_authorization_subjects_me) | Returns a listing of roles and permissions for the currently authenticated user.|
|[**get_authorization_subjects_rolecounts**](#get_authorization_subjects_rolecounts) | Get the count of roles granted to a list of subjects|
|[**get_user_roles**](#get_user_roles) | Returns a listing of roles and permissions for a user.|
|[**patch_authorization_role**](#patch_authorization_role) | Patch Organization Role for needsUpdate Field|
|[**patch_authorization_settings**](#patch_authorization_settings) | Change authorization settings|
|[**post_authorization_division_object**](#post_authorization_division_object) | Assign a list of objects to a division|
|[**post_authorization_division_restore**](#post_authorization_division_restore) | Recreate a previously deleted division.|
|[**post_authorization_divisions**](#post_authorization_divisions) | Create a division.|
|[**post_authorization_role**](#post_authorization_role) | Bulk-grant subjects and divisions with an organization role.|
|[**post_authorization_role_comparedefault_right_role_id**](#post_authorization_role_comparedefault_right_role_id) | Get an unsaved org role to default role comparison|
|[**post_authorization_roles**](#post_authorization_roles) | Create an organization role.|
|[**post_authorization_roles_default**](#post_authorization_roles_default) | Restores all default roles|
|[**post_authorization_subject_bulkadd**](#post_authorization_subject_bulkadd) | Bulk-grant roles and divisions to a subject.|
|[**post_authorization_subject_bulkremove**](#post_authorization_subject_bulkremove) | Bulk-remove grants from a subject.|
|[**post_authorization_subject_bulkreplace**](#post_authorization_subject_bulkreplace) | Replace subject&#39;s roles and divisions with the exact list supplied in the request.|
|[**post_authorization_subject_division_role**](#post_authorization_subject_division_role) | Make a grant of a role in a division|
|[**put_authorization_division**](#put_authorization_division) | Update a division.|
|[**put_authorization_role**](#put_authorization_role) | Update an organization role.|
|[**put_authorization_role_users_add**](#put_authorization_role_users_add) | Sets the users for the role|
|[**put_authorization_role_users_remove**](#put_authorization_role_users_remove) | Removes the users from the role|
|[**put_authorization_roles_default**](#put_authorization_roles_default) | Restore specified default roles|
|[**put_authorization_roles_settings**](#put_authorization_roles_settings) | Change authorization role settings|
|[**put_user_roles**](#put_user_roles) | Sets the user&#39;s roles|



## delete_authorization_division

>  delete_authorization_division(division_id, force=force)


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
force = False # bool | Force delete this division as well as the grants and objects associated with it (optional) (default to False)

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
| **force** | **bool**| Force delete this division as well as the grants and objects associated with it | [optional] [default to False] |

### Return type

void (empty response body)


## delete_authorization_role

>  delete_authorization_role(role_id)


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

### Return type

void (empty response body)


## get_authorization_division

> [**AuthzDivision**](AuthzDivision) get_authorization_division(division_id, object_count=object_count)


Returns an authorization division.

Wraps GET /api/v2/authorization/divisions/{divisionId} 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
division_id = 'division_id_example' # str | Division ID
object_count = False # bool | Get count of objects in this division, grouped by type (optional) (default to False)

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
| **object_count** | **bool**| Get count of objects in this division, grouped by type | [optional] [default to False]<br />**Values**: true, false |

### Return type

[**AuthzDivision**](AuthzDivision)


## get_authorization_division_grants

> [**AuthzDivisionGrantEntityListing**](AuthzDivisionGrantEntityListing) get_authorization_division_grants(division_id, page_number=page_number, page_size=page_size)


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

### Return type

[**AuthzDivisionGrantEntityListing**](AuthzDivisionGrantEntityListing)


## get_authorization_divisions

> [**AuthzDivisionEntityListing**](AuthzDivisionEntityListing) get_authorization_divisions(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, object_count=object_count, id=id, name=name)


Retrieve a list of all divisions defined for the organization

Request specific divisions by id using a query param \"id\", e.g.  ?id=5f777167-63be-4c24-ad41-374155d9e28b&id=72e9fb25-c484-488d-9312-7acba82435b3

Wraps GET /api/v2/authorization/divisions 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
object_count = False # bool | Include the count of objects contained in the division (optional) (default to False)
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
| **expand** | [**list[str]**](str)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **object_count** | **bool**| Include the count of objects contained in the division | [optional] [default to False] |
| **id** | [**list[str]**](str)| Optionally request specific divisions by their IDs | [optional]  |
| **name** | **str**| Search term to filter by division name | [optional]  |

### Return type

[**AuthzDivisionEntityListing**](AuthzDivisionEntityListing)


## get_authorization_divisions_home

> [**AuthzDivision**](AuthzDivision) get_authorization_divisions_home()


Retrieve the home division for the organization.

Will not include object counts.

Wraps GET /api/v2/authorization/divisions/home 

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

[**AuthzDivision**](AuthzDivision)


## get_authorization_divisions_limit

> int** get_authorization_divisions_limit()


Returns the maximum allowed number of divisions.

Wraps GET /api/v2/authorization/divisions/limit 

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

### Return type

[**DivsPermittedEntityListing**](DivsPermittedEntityListing)


## get_authorization_permissions

> [**PermissionCollectionEntityListing**](PermissionCollectionEntityListing) get_authorization_permissions(page_size=page_size, page_number=page_number, query_type=query_type, query=query)


Get all permissions.

Retrieve a list of all permission defined in the system.

Wraps GET /api/v2/authorization/permissions 

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

### Return type

[**PermissionCollectionEntityListing**](PermissionCollectionEntityListing)


## get_authorization_products

> [**OrganizationProductEntityListing**](OrganizationProductEntityListing) get_authorization_products()


Get the list of enabled products

Gets the list of enabled products. Some example product names are: collaborateFree, collaboratePro, communicate, and engage.

Wraps GET /api/v2/authorization/products 

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

[**OrganizationProductEntityListing**](OrganizationProductEntityListing)


## get_authorization_role

> [**DomainOrganizationRole**](DomainOrganizationRole) get_authorization_role(role_id, user_count=user_count, expand=expand)


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
user_count = True # bool | Fetch the count of users who have this role granted in at least one division. Setting this value or defaulting to 'true' can lead to slower load times or timeouts for role queries with large member counts. (optional) (default to True)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. \"unusedPermissions\" returns the permissions not used for the role (optional)

try:
    # Get a single organization role.
    api_response = api_instance.get_authorization_role(role_id, user_count=user_count, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_role: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **role_id** | **str**| Role ID |  |
| **user_count** | **bool**| Fetch the count of users who have this role granted in at least one division. Setting this value or defaulting to &#39;true&#39; can lead to slower load times or timeouts for role queries with large member counts. | [optional] [default to True]<br />**Values**: true, false |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. \&quot;unusedPermissions\&quot; returns the permissions not used for the role | [optional] <br />**Values**: unusedPermissions |

### Return type

[**DomainOrganizationRole**](DomainOrganizationRole)


## get_authorization_role_comparedefault_right_role_id

> [**DomainOrgRoleDifference**](DomainOrgRoleDifference) get_authorization_role_comparedefault_right_role_id(left_role_id, right_role_id)


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

### Return type

[**DomainOrgRoleDifference**](DomainOrgRoleDifference)


## get_authorization_role_subjectgrants

> [**SubjectDivisionGrantsEntityListing**](SubjectDivisionGrantsEntityListing) get_authorization_role_subjectgrants(role_id, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)


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
| **expand** | [**list[str]**](str)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |

### Return type

[**SubjectDivisionGrantsEntityListing**](SubjectDivisionGrantsEntityListing)


## get_authorization_role_users

> [**UserEntityListing**](UserEntityListing) get_authorization_role_users(role_id, page_size=page_size, page_number=page_number)


Get a list of the users in a specified role.

Get an array of the UUIDs of the users in the specified role.

Wraps GET /api/v2/authorization/roles/{roleId}/users 

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

### Return type

[**UserEntityListing**](UserEntityListing)


## get_authorization_roles

> [**OrganizationRoleEntityListing**](OrganizationRoleEntityListing) get_authorization_roles(page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, name=name, permission=permission, default_role_id=default_role_id, user_count=user_count, id=id)


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
user_count = True # bool |  (optional) (default to True)
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
| **expand** | [**list[str]**](str)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
| **name** | **str**|  | [optional]  |
| **permission** | [**list[str]**](str)|  | [optional]  |
| **default_role_id** | [**list[str]**](str)|  | [optional]  |
| **user_count** | **bool**|  | [optional] [default to True] |
| **id** | [**list[str]**](str)| id | [optional]  |

### Return type

[**OrganizationRoleEntityListing**](OrganizationRoleEntityListing)


## get_authorization_roles_settings

> [**RoleSettings**](RoleSettings) get_authorization_roles_settings()


Get authorization role settings

Wraps GET /api/v2/authorization/roles/settings 

Requires ANY permissions: 

* directory:organization:admin
* authorization:settings:view

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
    # Get authorization role settings
    api_response = api_instance.get_authorization_roles_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_roles_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**RoleSettings**](RoleSettings)


## get_authorization_settings

> [**AuthorizationSettings**](AuthorizationSettings) get_authorization_settings()


Get authorization settings

Wraps GET /api/v2/authorization/settings 

Requires ANY permissions: 

* directory:organization:admin
* authorization:settings:view

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
    # Get authorization settings
    api_response = api_instance.get_authorization_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**AuthorizationSettings**](AuthorizationSettings)


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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
include_duplicates = False # bool | Include multiple entries with the same role and division but different subjects (optional) (default to False)

try:
    # Returns a listing of roles and permissions for a user.
    api_response = api_instance.get_authorization_subject(subject_id, include_duplicates=include_duplicates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_subject: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
include_duplicates = False # bool | Include multiple entries with the same role and division but different subjects (optional) (default to False)

try:
    # Returns a listing of roles and permissions for the currently authenticated user.
    api_response = api_instance.get_authorization_subjects_me(include_duplicates=include_duplicates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_subjects_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **include_duplicates** | **bool**| Include multiple entries with the same role and division but different subjects | [optional] [default to False]<br />**Values**: true, false |

### Return type

[**AuthzSubject**](AuthzSubject)


## get_authorization_subjects_rolecounts

> dict(str, object)** get_authorization_subjects_rolecounts(id=id)


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
| **id** | [**list[str]**](str)| id | [optional]  |

### Return type

**dict(str, object)**


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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
subject_id = 'subject_id_example' # str | User ID

try:
    # Returns a listing of roles and permissions for a user.
    api_response = api_instance.get_user_roles(subject_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_user_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **subject_id** | **str**| User ID |  |

### Return type

[**UserAuthorization**](UserAuthorization)


## patch_authorization_role

> [**DomainOrganizationRole**](DomainOrganizationRole) patch_authorization_role(role_id, body)


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
| **body** | [**DomainOrganizationRole**](DomainOrganizationRole)| Organization role |  |

### Return type

[**DomainOrganizationRole**](DomainOrganizationRole)


## patch_authorization_settings

> [**AuthorizationSettings**](AuthorizationSettings) patch_authorization_settings(body)


Change authorization settings

Change authorization settings

Wraps PATCH /api/v2/authorization/settings 

Requires ANY permissions: 

* directory:organization:admin
* authorization:settings:edit

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
body = PureCloudPlatformClientV2.AuthorizationSettings() # AuthorizationSettings | Authorization Settings

try:
    # Change authorization settings
    api_response = api_instance.patch_authorization_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->patch_authorization_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AuthorizationSettings**](AuthorizationSettings)| Authorization Settings |  |

### Return type

[**AuthorizationSettings**](AuthorizationSettings)


## post_authorization_division_object

>  post_authorization_division_object(division_id, object_type, body)


Assign a list of objects to a division

Set the division of a specified list of objects. The objects must all be of the same type, one of:  CAMPAIGN, MANAGEMENTUNIT, FLOW, QUEUE, DATATABLES or USER.  The body of the request is a list of object IDs, which are expected to be  GUIDs, e.g. [\"206ce31f-61ec-40ed-a8b1-be6f06303998\",\"250a754e-f5e4-4f51-800f-a92f09d3bf8c\"]

Wraps POST /api/v2/authorization/divisions/{divisionId}/objects/{objectType} 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
division_id = 'division_id_example' # str | Division ID
object_type = 'object_type_example' # str | The type of the objects. Must be one of the valid object types
body = ['body_example'] # list[str] | Object Id List

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
| **object_type** | **str**| The type of the objects. Must be one of the valid object types | <br />**Values**: QUEUE, CAMPAIGN, CONTACTLIST, DNCLIST, EMAILCAMPAIGN, MESSAGINGCAMPAIGN, MANAGEMENTUNIT, BUSINESSUNIT, FLOW, FLOWMILESTONE, FLOWOUTCOME, USER, CALLROUTE, EMERGENCYGROUPS, ROUTINGSCHEDULES, ROUTINGSCHEDULEGROUPS, DATATABLES, TEAM, WORKBIN, WORKTYPE, EXTENSIONPOOL, SKILLGROUP, SCRIPT |
| **body** | [**list[str]**](str)| Object Id List |  |

### Return type

void (empty response body)


## post_authorization_division_restore

> [**AuthzDivision**](AuthzDivision) post_authorization_division_restore(division_id, body=body)


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
body = PureCloudPlatformClientV2.AuthzDivision() # AuthzDivision | Recreated division data (optional)

try:
    # Recreate a previously deleted division.
    api_response = api_instance.post_authorization_division_restore(division_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->post_authorization_division_restore: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | **str**| Division ID |  |
| **body** | [**AuthzDivision**](AuthzDivision)| Recreated division data | [optional]  |

### Return type

[**AuthzDivision**](AuthzDivision)


## post_authorization_divisions

> [**AuthzDivision**](AuthzDivision) post_authorization_divisions(body)


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
| **body** | [**AuthzDivision**](AuthzDivision)| Division |  |

### Return type

[**AuthzDivision**](AuthzDivision)


## post_authorization_role

>  post_authorization_role(role_id, body, subject_type=subject_type)


Bulk-grant subjects and divisions with an organization role.

Wraps POST /api/v2/authorization/roles/{roleId} 

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
role_id = 'role_id_example' # str | Role ID
body = PureCloudPlatformClientV2.SubjectDivisions() # SubjectDivisions | Subjects and Divisions
subject_type = ''PC_USER'' # str | what the type of the subjects are (PC_GROUP, PC_USER or PC_OAUTH_CLIENT) (optional) (default to 'PC_USER')

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
| **body** | [**SubjectDivisions**](SubjectDivisions)| Subjects and Divisions |  |
| **subject_type** | **str**| what the type of the subjects are (PC_GROUP, PC_USER or PC_OAUTH_CLIENT) | [optional] [default to &#39;PC_USER&#39;] |

### Return type

void (empty response body)


## post_authorization_role_comparedefault_right_role_id

> [**DomainOrgRoleDifference**](DomainOrgRoleDifference) post_authorization_role_comparedefault_right_role_id(left_role_id, right_role_id, body)


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
| **body** | [**DomainOrganizationRole**](DomainOrganizationRole)| Organization role |  |

### Return type

[**DomainOrgRoleDifference**](DomainOrgRoleDifference)


## post_authorization_roles

> [**DomainOrganizationRole**](DomainOrganizationRole) post_authorization_roles(body)


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
| **body** | [**DomainOrganizationRoleCreate**](DomainOrganizationRoleCreate)| Organization role |  |

### Return type

[**DomainOrganizationRole**](DomainOrganizationRole)


## post_authorization_roles_default

> [**OrganizationRoleEntityListing**](OrganizationRoleEntityListing) post_authorization_roles_default(force=force)


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
force = False # bool | Restore default roles (optional) (default to False)

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
| **force** | **bool**| Restore default roles | [optional] [default to False] |

### Return type

[**OrganizationRoleEntityListing**](OrganizationRoleEntityListing)


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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
body = PureCloudPlatformClientV2.RoleDivisionGrants() # RoleDivisionGrants | Pairs of role and division IDs
subject_type = ''PC_USER'' # str | what the type of the subject is (PC_GROUP, PC_USER or PC_OAUTH_CLIENT) (optional) (default to 'PC_USER')

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
body = PureCloudPlatformClientV2.RoleDivisionGrants() # RoleDivisionGrants | Pairs of role and division IDs
subject_type = ''PC_USER'' # str | what the type of the subject is (PC_GROUP, PC_USER or PC_OAUTH_CLIENT) (optional) (default to 'PC_USER')

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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
subject_id = 'subject_id_example' # str | Subject ID (user or group)
division_id = 'division_id_example' # str | the id of the division to which to make the grant
role_id = 'role_id_example' # str | the id of the role to grant
subject_type = ''PC_USER'' # str | what the type of the subject is: PC_GROUP, PC_USER or PC_OAUTH_CLIENT (note: for cross-org authorization, please use the Organization Authorization endpoints) (optional) (default to 'PC_USER')

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
| **subject_type** | **str**| what the type of the subject is: PC_GROUP, PC_USER or PC_OAUTH_CLIENT (note: for cross-org authorization, please use the Organization Authorization endpoints) | [optional] [default to &#39;PC_USER&#39;] |

### Return type

void (empty response body)


## put_authorization_division

> [**AuthzDivision**](AuthzDivision) put_authorization_division(division_id, body)


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
| **body** | [**AuthzDivision**](AuthzDivision)| Updated division data |  |

### Return type

[**AuthzDivision**](AuthzDivision)


## put_authorization_role

> [**DomainOrganizationRole**](DomainOrganizationRole) put_authorization_role(role_id, body)


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
| **body** | [**DomainOrganizationRoleUpdate**](DomainOrganizationRoleUpdate)| Organization role |  |

### Return type

[**DomainOrganizationRole**](DomainOrganizationRole)


## put_authorization_role_users_add

> list[str]** put_authorization_role_users_add(role_id, body)


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
body = ['body_example'] # list[str] | List of user IDs

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
| **body** | [**list[str]**](str)| List of user IDs |  |

### Return type

**list[str]**


## put_authorization_role_users_remove

> list[str]** put_authorization_role_users_remove(role_id, body)


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
body = ['body_example'] # list[str] | List of user IDs

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
| **body** | [**list[str]**](str)| List of user IDs |  |

### Return type

**list[str]**


## put_authorization_roles_default

> [**OrganizationRoleEntityListing**](OrganizationRoleEntityListing) put_authorization_roles_default(body)


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
| **body** | [**list[DomainOrganizationRole]**](DomainOrganizationRole)| Organization roles list |  |

### Return type

[**OrganizationRoleEntityListing**](OrganizationRoleEntityListing)


## put_authorization_roles_settings

> [**RoleSettings**](RoleSettings) put_authorization_roles_settings(body)


Change authorization role settings

Change role settings

Wraps PUT /api/v2/authorization/roles/settings 

Requires ANY permissions: 

* directory:organization:admin
* authorization:settings:edit

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
body = PureCloudPlatformClientV2.RoleSettings() # RoleSettings | Authorization Role Settings

try:
    # Change authorization role settings
    api_response = api_instance.put_authorization_roles_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->put_authorization_roles_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**RoleSettings**](RoleSettings)| Authorization Role Settings |  |

### Return type

[**RoleSettings**](RoleSettings)


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
api_instance = PureCloudPlatformClientV2.AuthorizationApi()
subject_id = 'subject_id_example' # str | User ID
body = ['body_example'] # list[str] | List of roles

try:
    # Sets the user's roles
    api_response = api_instance.put_user_roles(subject_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->put_user_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **subject_id** | **str**| User ID |  |
| **body** | [**list[str]**](str)| List of roles |  |

### Return type

[**UserAuthorization**](UserAuthorization)


_PureCloudPlatformClientV2 212.0.0_

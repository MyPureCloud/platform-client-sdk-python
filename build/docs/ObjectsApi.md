# ObjectsApi

## PureCloudPlatformClientV2.ObjectsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_authorization_division**](#delete_authorization_division) | Delete a division.|
|[**get_authorization_division**](#get_authorization_division) | Returns an authorization division.|
|[**get_authorization_divisions**](#get_authorization_divisions) | Retrieve a list of all divisions defined for the organization|
|[**get_authorization_divisions_deleted**](#get_authorization_divisions_deleted) | Get a list of soft deleted divisions for the org|
|[**get_authorization_divisions_home**](#get_authorization_divisions_home) | Retrieve the home division for the organization.|
|[**get_authorization_divisions_limit**](#get_authorization_divisions_limit) | Returns the maximum allowed number of divisions.|
|[**get_authorization_divisions_query**](#get_authorization_divisions_query) | Retrieve a list of all divisions defined for the organization with cursor|
|[**post_authorization_division_object**](#post_authorization_division_object) | Assign a list of objects to a division|
|[**post_authorization_division_restore**](#post_authorization_division_restore) | Recreate a previously deleted division.|
|[**post_authorization_divisions**](#post_authorization_divisions) | Create a division.|
|[**put_authorization_division**](#put_authorization_division) | Update a division.|



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
api_instance = PureCloudPlatformClientV2.ObjectsApi()
division_id = 'division_id_example' # str | Division ID
force = False # bool | DEPRECATED -  Force delete this division. Warning: This option may cause any remaining objects in this division to be inaccessible. (optional) (default to False)

try:
    # Delete a division.
    api_instance.delete_authorization_division(division_id, force=force)
except ApiException as e:
    print("Exception when calling ObjectsApi->delete_authorization_division: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | **str**| Division ID |  |
| **force** | **bool**| DEPRECATED -  Force delete this division. Warning: This option may cause any remaining objects in this division to be inaccessible. | [optional] [default to False] |

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
api_instance = PureCloudPlatformClientV2.ObjectsApi()
division_id = 'division_id_example' # str | Division ID
object_count = False # bool | Get count of objects in this division, grouped by type (optional) (default to False)

try:
    # Returns an authorization division.
    api_response = api_instance.get_authorization_division(division_id, object_count=object_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->get_authorization_division: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | **str**| Division ID |  |
| **object_count** | **bool**| Get count of objects in this division, grouped by type | [optional] [default to False]<br />**Values**: true, false |

### Return type

[**AuthzDivision**](AuthzDivision)


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
api_instance = PureCloudPlatformClientV2.ObjectsApi()
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
    print("Exception when calling ObjectsApi->get_authorization_divisions: %s\n" % e)
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


## get_authorization_divisions_deleted

> [**AuthzDivisionEntityListing**](AuthzDivisionEntityListing) get_authorization_divisions_deleted(page_number=page_number, page_size=page_size)


Get a list of soft deleted divisions for the org

Wraps GET /api/v2/authorization/divisions/deleted 

Requires ANY permissions: 

* authorization:divisionDeleted:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ObjectsApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get a list of soft deleted divisions for the org
    api_response = api_instance.get_authorization_divisions_deleted(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->get_authorization_divisions_deleted: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

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
api_instance = PureCloudPlatformClientV2.ObjectsApi()

try:
    # Retrieve the home division for the organization.
    api_response = api_instance.get_authorization_divisions_home()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->get_authorization_divisions_home: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.ObjectsApi()

try:
    # Returns the maximum allowed number of divisions.
    api_response = api_instance.get_authorization_divisions_limit()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->get_authorization_divisions_limit: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

**int**


## get_authorization_divisions_query

> [**AuthzDivisionCursorListing**](AuthzDivisionCursorListing) get_authorization_divisions_query(before=before, after=after, page_size=page_size, id=id, name=name)


Retrieve a list of all divisions defined for the organization with cursor

Use \"after\" and \"before\" param to fetch next/previous page}

Wraps GET /api/v2/authorization/divisions/query 

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
api_instance = PureCloudPlatformClientV2.ObjectsApi()
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
id = ['id_example'] # list[str] | Optionally request specific divisions by their IDs (optional)
name = 'name_example' # str | Optionally request specific divisions by division name (optional)

try:
    # Retrieve a list of all divisions defined for the organization with cursor
    api_response = api_instance.get_authorization_divisions_query(before=before, after=after, page_size=page_size, id=id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->get_authorization_divisions_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **id** | [**list[str]**](str)| Optionally request specific divisions by their IDs | [optional]  |
| **name** | **str**| Optionally request specific divisions by division name | [optional]  |

### Return type

[**AuthzDivisionCursorListing**](AuthzDivisionCursorListing)


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
api_instance = PureCloudPlatformClientV2.ObjectsApi()
division_id = 'division_id_example' # str | Division ID
object_type = 'object_type_example' # str | The type of the objects. Must be one of the valid object types
body = ['body_example'] # list[str] | Object Id List

try:
    # Assign a list of objects to a division
    api_instance.post_authorization_division_object(division_id, object_type, body)
except ApiException as e:
    print("Exception when calling ObjectsApi->post_authorization_division_object: %s\n" % e)
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

> [**AuthzDivision**](AuthzDivision) post_authorization_division_restore(division_id, body)


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
api_instance = PureCloudPlatformClientV2.ObjectsApi()
division_id = 'division_id_example' # str | Division ID
body = PureCloudPlatformClientV2.AuthzDivision() # AuthzDivision | Recreated division data

try:
    # Recreate a previously deleted division.
    api_response = api_instance.post_authorization_division_restore(division_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->post_authorization_division_restore: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | **str**| Division ID |  |
| **body** | [**AuthzDivision**](AuthzDivision)| Recreated division data |  |

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
api_instance = PureCloudPlatformClientV2.ObjectsApi()
body = PureCloudPlatformClientV2.AuthzDivision() # AuthzDivision | Division

try:
    # Create a division.
    api_response = api_instance.post_authorization_divisions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->post_authorization_divisions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AuthzDivision**](AuthzDivision)| Division |  |

### Return type

[**AuthzDivision**](AuthzDivision)


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
api_instance = PureCloudPlatformClientV2.ObjectsApi()
division_id = 'division_id_example' # str | Division ID
body = PureCloudPlatformClientV2.AuthzDivision() # AuthzDivision | Updated division data

try:
    # Update a division.
    api_response = api_instance.put_authorization_division(division_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->put_authorization_division: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | **str**| Division ID |  |
| **body** | [**AuthzDivision**](AuthzDivision)| Updated division data |  |

### Return type

[**AuthzDivision**](AuthzDivision)


_PureCloudPlatformClientV2 237.0.0_

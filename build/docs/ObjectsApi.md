---
title: ObjectsApi
---

## PureCloudPlatformClientV2.ObjectsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_authorization_division**](ObjectsApi.html#delete_authorization_division) | Delete a division.|
|[**get_authorization_division**](ObjectsApi.html#get_authorization_division) | Returns an authorization division.|
|[**get_authorization_divisions**](ObjectsApi.html#get_authorization_divisions) | Retrieve a list of all divisions defined for the organization|
|[**get_authorization_divisions_home**](ObjectsApi.html#get_authorization_divisions_home) | Retrieve the home division for the organization.|
|[**get_authorization_divisions_limit**](ObjectsApi.html#get_authorization_divisions_limit) | Returns the maximum allowed number of divisions.|
|[**post_authorization_division_object**](ObjectsApi.html#post_authorization_division_object) | Assign a list of objects to a division|
|[**post_authorization_divisions**](ObjectsApi.html#post_authorization_divisions) | Create a division.|
|[**put_authorization_division**](ObjectsApi.html#put_authorization_division) | Update a division.|
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
api_instance = PureCloudPlatformClientV2.ObjectsApi()
division_id = 'division_id_example' # str | Division ID
force = false # bool | Force delete this division as well as the grants and objects associated with it (optional) (default to false)

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
| **force** | **bool**| Force delete this division as well as the grants and objects associated with it | [optional] [default to false] |
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
api_instance = PureCloudPlatformClientV2.ObjectsApi()
division_id = 'division_id_example' # str | Division ID
object_count = false # bool | Get count of objects in this division, grouped by type (optional) (default to false)

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
| **object_count** | **bool**| Get count of objects in this division, grouped by type | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**AuthzDivision**](AuthzDivision.html)

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
api_instance = PureCloudPlatformClientV2.ObjectsApi()
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
    print("Exception when calling ObjectsApi->get_authorization_divisions: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.ObjectsApi()

try:
    # Retrieve the home division for the organization.
    api_response = api_instance.get_authorization_divisions_home()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->get_authorization_divisions_home: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

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
api_instance = PureCloudPlatformClientV2.ObjectsApi()

try:
    # Returns the maximum allowed number of divisions.
    api_response = api_instance.get_authorization_divisions_limit()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->get_authorization_divisions_limit: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

**int**

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
api_instance = PureCloudPlatformClientV2.ObjectsApi()
division_id = 'division_id_example' # str | Division ID
object_type = 'object_type_example' # str | The type of the objects. Must be one of the valid object types
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | Object Id List

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
| **object_type** | **str**| The type of the objects. Must be one of the valid object types | <br />**Values**: QUEUE, CAMPAIGN, CONTACTLIST, DNCLIST, MESSAGINGCAMPAIGN, MANAGEMENTUNIT, BUSINESSUNIT, FLOW, USER, DATATABLES |
| **body** | **list[str]**| Object Id List |  |
{: class="table table-striped"}

### Return type

void (empty response body)

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
| **body** | [**AuthzDivision**](AuthzDivision.html)| Division |  |
{: class="table table-striped"}

### Return type

[**AuthzDivision**](AuthzDivision.html)

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
| **body** | [**AuthzDivision**](AuthzDivision.html)| Updated division data |  |
{: class="table table-striped"}

### Return type

[**AuthzDivision**](AuthzDivision.html)


---
title: ObjectsApi
---

## PureCloudPlatformClientV2.ObjectsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_authorization_divisions_limit**](ObjectsApi.html#get_authorization_divisions_limit) | Returns the maximum allowed number of divisions.|
|[**post_authorization_division_object**](ObjectsApi.html#post_authorization_division_object) | Set the division of a list of objects. The objects must all be of the same type: CAMPAIGN, CONTACTLIST, DNCLIST, MANAGEMENTUNIT, FLOW, QUEUE, USER|
{: class="table table-striped"}

<a name="get_authorization_divisions_limit"></a>

## int** get_authorization_divisions_limit()

Returns the maximum allowed number of divisions.



Wraps GET /api/v2/authorization/divisions/limit 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ObjectsApi()

try:
    # Returns the maximum allowed number of divisions.
    api_response = api_instance.get_authorization_divisions_limit()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ObjectsApi->get_authorization_divisions_limit: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

**int**

<a name="post_authorization_division_object"></a>

## [**list[AuthzTypedObject]**](AuthzTypedObject.html) post_authorization_division_object(division_id, object_type, body)

Set the division of a list of objects. The objects must all be of the same type: CAMPAIGN, CONTACTLIST, DNCLIST, MANAGEMENTUNIT, FLOW, QUEUE, USER



Wraps POST /api/v2/authorization/divisions/{divisionId}/objects/{objectType} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ObjectsApi()
division_id = 'division_id_example' # str | Division ID
object_type = 'object_type_example' # str | The type of the objects. Must be one of the valid object types
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | Object Id List

try:
    # Set the division of a list of objects. The objects must all be of the same type: CAMPAIGN, CONTACTLIST, DNCLIST, MANAGEMENTUNIT, FLOW, QUEUE, USER
    api_response = api_instance.post_authorization_division_object(division_id, object_type, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ObjectsApi->post_authorization_division_object: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | **str**| Division ID |  |
| **object_type** | **str**| The type of the objects. Must be one of the valid object types | <br />**Values**: QUEUE, CAMPAIGN, CONTACTLIST, DNCLIST, MANAGEMENTUNIT, FLOW, USER |
| **body** | **list[str]**| Object Id List |  |
{: class="table table-striped"}

### Return type

[**list[AuthzTypedObject]**](AuthzTypedObject.html)


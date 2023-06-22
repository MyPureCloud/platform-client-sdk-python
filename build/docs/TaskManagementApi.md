---
title: TaskManagementApi
---

## PureCloudPlatformClientV2.TaskManagementApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_taskmanagement_workbin**](TaskManagementApi.html#delete_taskmanagement_workbin) | Delete a workbin|
|[**delete_taskmanagement_workitem**](TaskManagementApi.html#delete_taskmanagement_workitem) | Delete a workitem|
|[**delete_taskmanagement_workitems_schema**](TaskManagementApi.html#delete_taskmanagement_workitems_schema) | Delete a schema|
|[**delete_taskmanagement_worktype**](TaskManagementApi.html#delete_taskmanagement_worktype) | Delete a worktype|
|[**delete_taskmanagement_worktype_status**](TaskManagementApi.html#delete_taskmanagement_worktype_status) | Delete a status|
|[**get_taskmanagement_workbin**](TaskManagementApi.html#get_taskmanagement_workbin) | Get a workbin|
|[**get_taskmanagement_workbin_history**](TaskManagementApi.html#get_taskmanagement_workbin_history) | Get a listing of a workbin&#39;s attribute change history|
|[**get_taskmanagement_workbin_version**](TaskManagementApi.html#get_taskmanagement_workbin_version) | Get a version of a workbin|
|[**get_taskmanagement_workbin_versions**](TaskManagementApi.html#get_taskmanagement_workbin_versions) | Get all versions of a workbin|
|[**get_taskmanagement_workitem**](TaskManagementApi.html#get_taskmanagement_workitem) | Get a workitem|
|[**get_taskmanagement_workitem_history**](TaskManagementApi.html#get_taskmanagement_workitem_history) | Get a listing of a workitem&#39;s attribute change history|
|[**get_taskmanagement_workitem_user_wrapups**](TaskManagementApi.html#get_taskmanagement_workitem_user_wrapups) | Get all wrapup codes added for the given user for a workitem.|
|[**get_taskmanagement_workitem_version**](TaskManagementApi.html#get_taskmanagement_workitem_version) | Get a version of a workitem|
|[**get_taskmanagement_workitem_versions**](TaskManagementApi.html#get_taskmanagement_workitem_versions) | Get all versions of a workitem|
|[**get_taskmanagement_workitem_wrapups**](TaskManagementApi.html#get_taskmanagement_workitem_wrapups) | Get all wrapup codes added for all users for a workitem.|
|[**get_taskmanagement_workitems_schema**](TaskManagementApi.html#get_taskmanagement_workitems_schema) | Get a schema|
|[**get_taskmanagement_workitems_schema_version**](TaskManagementApi.html#get_taskmanagement_workitems_schema_version) | Get a specific version of a schema|
|[**get_taskmanagement_workitems_schema_versions**](TaskManagementApi.html#get_taskmanagement_workitems_schema_versions) | Get all versions of a schema|
|[**get_taskmanagement_workitems_schemas**](TaskManagementApi.html#get_taskmanagement_workitems_schemas) | Get a list of schemas.|
|[**get_taskmanagement_worktype**](TaskManagementApi.html#get_taskmanagement_worktype) | Get a worktype|
|[**get_taskmanagement_worktype_history**](TaskManagementApi.html#get_taskmanagement_worktype_history) | Get a listing of a worktype&#39;s attribute change history|
|[**get_taskmanagement_worktype_status**](TaskManagementApi.html#get_taskmanagement_worktype_status) | Get a status|
|[**get_taskmanagement_worktype_version**](TaskManagementApi.html#get_taskmanagement_worktype_version) | Get a version of a worktype|
|[**get_taskmanagement_worktype_versions**](TaskManagementApi.html#get_taskmanagement_worktype_versions) | Get all versions of a worktype|
|[**patch_taskmanagement_workbin**](TaskManagementApi.html#patch_taskmanagement_workbin) | Update the attributes of a workbin|
|[**patch_taskmanagement_workitem**](TaskManagementApi.html#patch_taskmanagement_workitem) | Update the attributes of a workitem|
|[**patch_taskmanagement_workitem_assignment**](TaskManagementApi.html#patch_taskmanagement_workitem_assignment) | Attempts to manually assign a specified workitem to a specified user.  Ignores bullseye ring, PAR score, skills, and languages.|
|[**patch_taskmanagement_workitem_user_wrapups**](TaskManagementApi.html#patch_taskmanagement_workitem_user_wrapups) | Add/Remove a wrapup code for a given user in a workitem.|
|[**patch_taskmanagement_workitem_users_me_wrapups**](TaskManagementApi.html#patch_taskmanagement_workitem_users_me_wrapups) | Add/Remove a wrapup code for the current user in a workitem.|
|[**patch_taskmanagement_worktype**](TaskManagementApi.html#patch_taskmanagement_worktype) | Update the attributes of a worktype|
|[**patch_taskmanagement_worktype_status**](TaskManagementApi.html#patch_taskmanagement_worktype_status) | Update the attributes of a status|
|[**post_taskmanagement_workbins**](TaskManagementApi.html#post_taskmanagement_workbins) | Create a workbin|
|[**post_taskmanagement_workbins_query**](TaskManagementApi.html#post_taskmanagement_workbins_query) | Query for workbins|
|[**post_taskmanagement_workitem_acd_cancel**](TaskManagementApi.html#post_taskmanagement_workitem_acd_cancel) | Cancel the assignment process for a workitem that is currently queued for assignment through ACD.|
|[**post_taskmanagement_workitem_disconnect**](TaskManagementApi.html#post_taskmanagement_workitem_disconnect) | Disconnect the assignee of the workitem|
|[**post_taskmanagement_workitem_terminate**](TaskManagementApi.html#post_taskmanagement_workitem_terminate) | Terminate a workitem|
|[**post_taskmanagement_workitems**](TaskManagementApi.html#post_taskmanagement_workitems) | Create a workitem|
|[**post_taskmanagement_workitems_query**](TaskManagementApi.html#post_taskmanagement_workitems_query) | Query for workitems|
|[**post_taskmanagement_workitems_schemas**](TaskManagementApi.html#post_taskmanagement_workitems_schemas) | Create a schema|
|[**post_taskmanagement_worktype_statuses**](TaskManagementApi.html#post_taskmanagement_worktype_statuses) | Add a status to a worktype|
|[**post_taskmanagement_worktypes**](TaskManagementApi.html#post_taskmanagement_worktypes) | Create a worktype|
|[**post_taskmanagement_worktypes_query**](TaskManagementApi.html#post_taskmanagement_worktypes_query) | Query for worktypes|
|[**put_taskmanagement_workitems_schema**](TaskManagementApi.html#put_taskmanagement_workitems_schema) | Update a schema|
{: class="table table-striped"}

<a name="delete_taskmanagement_workbin"></a>

##  delete_taskmanagement_workbin(workbin_id)



Delete a workbin

delete_taskmanagement_workbin is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/taskmanagement/workbins/{workbinId} 

Requires ANY permissions: 

* workitems:workbin:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workbin_id = 'workbin_id_example' # str | Workbin ID

try:
    # Delete a workbin
    api_instance.delete_taskmanagement_workbin(workbin_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_workbin: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workbin_id** | **str**| Workbin ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_taskmanagement_workitem"></a>

##  delete_taskmanagement_workitem(workitem_id)



Delete a workitem

delete_taskmanagement_workitem is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/taskmanagement/workitems/{workitemId} 

Requires ANY permissions: 

* workitems:workitem:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID

try:
    # Delete a workitem
    api_instance.delete_taskmanagement_workitem(workitem_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_workitem: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_taskmanagement_workitems_schema"></a>

##  delete_taskmanagement_workitems_schema(schema_id)



Delete a schema

delete_taskmanagement_workitems_schema is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/taskmanagement/workitems/schemas/{schemaId} 

Requires ANY permissions: 

* workitems:workitemSchema:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
schema_id = 'schema_id_example' # str | Schema ID

try:
    # Delete a schema
    api_instance.delete_taskmanagement_workitems_schema(schema_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_workitems_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_taskmanagement_worktype"></a>

##  delete_taskmanagement_worktype(worktype_id)



Delete a worktype

delete_taskmanagement_worktype is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/taskmanagement/worktypes/{worktypeId} 

Requires ANY permissions: 

* workitems:worktype:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id

try:
    # Delete a worktype
    api_instance.delete_taskmanagement_worktype(worktype_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_worktype: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_taskmanagement_worktype_status"></a>

##  delete_taskmanagement_worktype_status(worktype_id, status_id)



Delete a status

delete_taskmanagement_worktype_status is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/taskmanagement/worktypes/{worktypeId}/statuses/{statusId} 

Requires ANY permissions: 

* workitems:status:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
status_id = 'status_id_example' # str | Status id

try:
    # Delete a status
    api_instance.delete_taskmanagement_worktype_status(worktype_id, status_id)
except ApiException as e:
    print("Exception when calling TaskManagementApi->delete_taskmanagement_worktype_status: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **status_id** | **str**| Status id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_taskmanagement_workbin"></a>

## [**Workbin**](Workbin.html) get_taskmanagement_workbin(workbin_id)



Get a workbin

get_taskmanagement_workbin is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/workbins/{workbinId} 

Requires ANY permissions: 

* workitems:workbin:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workbin_id = 'workbin_id_example' # str | Workbin ID

try:
    # Get a workbin
    api_response = api_instance.get_taskmanagement_workbin(workbin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workbin: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workbin_id** | **str**| Workbin ID |  |
{: class="table table-striped"}

### Return type

[**Workbin**](Workbin.html)

<a name="get_taskmanagement_workbin_history"></a>

## [**WorkbinChangeListing**](WorkbinChangeListing.html) get_taskmanagement_workbin_history(workbin_id, after=after, page_size=page_size, sort_order=sort_order)



Get a listing of a workbin's attribute change history

get_taskmanagement_workbin_history is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/workbins/{workbinId}/history 

Requires ANY permissions: 

* workitems:workbin:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workbin_id = 'workbin_id_example' # str | Workbin ID
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get a listing of a workbin's attribute change history
    api_response = api_instance.get_taskmanagement_workbin_history(workbin_id, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workbin_history: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workbin_id** | **str**| Workbin ID |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**WorkbinChangeListing**](WorkbinChangeListing.html)

<a name="get_taskmanagement_workbin_version"></a>

## [**WorkbinVersion**](WorkbinVersion.html) get_taskmanagement_workbin_version(workbin_id, entity_version)



Get a version of a workbin

get_taskmanagement_workbin_version is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/workbins/{workbinId}/versions/{entityVersion} 

Requires ANY permissions: 

* workitems:workbin:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workbin_id = 'workbin_id_example' # str | Workbin ID
entity_version = 56 # int | Workbin version

try:
    # Get a version of a workbin
    api_response = api_instance.get_taskmanagement_workbin_version(workbin_id, entity_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workbin_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workbin_id** | **str**| Workbin ID |  |
| **entity_version** | **int**| Workbin version |  |
{: class="table table-striped"}

### Return type

[**WorkbinVersion**](WorkbinVersion.html)

<a name="get_taskmanagement_workbin_versions"></a>

## [**WorkbinVersionListing**](WorkbinVersionListing.html) get_taskmanagement_workbin_versions(workbin_id, after=after, page_size=page_size, sort_order=sort_order)



Get all versions of a workbin

get_taskmanagement_workbin_versions is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/workbins/{workbinId}/versions 

Requires ANY permissions: 

* workitems:workbin:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workbin_id = 'workbin_id_example' # str | Workbin ID
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get all versions of a workbin
    api_response = api_instance.get_taskmanagement_workbin_versions(workbin_id, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workbin_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workbin_id** | **str**| Workbin ID |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**WorkbinVersionListing**](WorkbinVersionListing.html)

<a name="get_taskmanagement_workitem"></a>

## [**Workitem**](Workitem.html) get_taskmanagement_workitem(workitem_id, expands=expands)



Get a workitem

get_taskmanagement_workitem is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/workitems/{workitemId} 

Requires ANY permissions: 

* workitems:workitem:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID
expands = 'expands_example' # str | Which fields to expand. Comma separated if more than one. (optional)

try:
    # Get a workitem
    api_response = api_instance.get_taskmanagement_workitem(workitem_id, expands=expands)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitem: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
| **expands** | **str**| Which fields to expand. Comma separated if more than one. | [optional] <br />**Values**: type, workbin, status |
{: class="table table-striped"}

### Return type

[**Workitem**](Workitem.html)

<a name="get_taskmanagement_workitem_history"></a>

## [**WorkitemChangeListing**](WorkitemChangeListing.html) get_taskmanagement_workitem_history(workitem_id, after=after, page_size=page_size, sort_order=sort_order)



Get a listing of a workitem's attribute change history

get_taskmanagement_workitem_history is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/workitems/{workitemId}/history 

Requires ANY permissions: 

* workitems:workitem:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get a listing of a workitem's attribute change history
    api_response = api_instance.get_taskmanagement_workitem_history(workitem_id, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitem_history: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**WorkitemChangeListing**](WorkitemChangeListing.html)

<a name="get_taskmanagement_workitem_user_wrapups"></a>

## [**WorkitemWrapup**](WorkitemWrapup.html) get_taskmanagement_workitem_user_wrapups(workitem_id, user_id, expands=expands, after=after, page_size=page_size, sort_order=sort_order)



Get all wrapup codes added for the given user for a workitem.

get_taskmanagement_workitem_user_wrapups is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/workitems/{workitemId}/users/{userId}/wrapups 

Requires ANY permissions: 

* workitems:wrapup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | The ID of the Workitem.
user_id = 'user_id_example' # str | The ID of the user
expands = 'expands_example' # str | Which fields, if any, to expand. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 50. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get all wrapup codes added for the given user for a workitem.
    api_response = api_instance.get_taskmanagement_workitem_user_wrapups(workitem_id, user_id, expands=expands, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitem_user_wrapups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| The ID of the Workitem. |  |
| **user_id** | **str**| The ID of the user |  |
| **expands** | **str**| Which fields, if any, to expand. | [optional] <br />**Values**: wrapupCode |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 50. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**WorkitemWrapup**](WorkitemWrapup.html)

<a name="get_taskmanagement_workitem_version"></a>

## [**WorkitemVersion**](WorkitemVersion.html) get_taskmanagement_workitem_version(workitem_id, entity_version)



Get a version of a workitem

get_taskmanagement_workitem_version is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/workitems/{workitemId}/versions/{entityVersion} 

Requires ANY permissions: 

* workitems:workitem:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID
entity_version = 56 # int | Workitem version

try:
    # Get a version of a workitem
    api_response = api_instance.get_taskmanagement_workitem_version(workitem_id, entity_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitem_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
| **entity_version** | **int**| Workitem version |  |
{: class="table table-striped"}

### Return type

[**WorkitemVersion**](WorkitemVersion.html)

<a name="get_taskmanagement_workitem_versions"></a>

## [**WorkitemVersionListing**](WorkitemVersionListing.html) get_taskmanagement_workitem_versions(workitem_id, after=after, page_size=page_size, sort_order=sort_order)



Get all versions of a workitem

get_taskmanagement_workitem_versions is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/workitems/{workitemId}/versions 

Requires ANY permissions: 

* workitems:workitem:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get all versions of a workitem
    api_response = api_instance.get_taskmanagement_workitem_versions(workitem_id, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitem_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**WorkitemVersionListing**](WorkitemVersionListing.html)

<a name="get_taskmanagement_workitem_wrapups"></a>

## [**WorkitemWrapupEntityListing**](WorkitemWrapupEntityListing.html) get_taskmanagement_workitem_wrapups(workitem_id, expands=expands, after=after, page_size=page_size, sort_order=sort_order)



Get all wrapup codes added for all users for a workitem.

get_taskmanagement_workitem_wrapups is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/workitems/{workitemId}/wrapups 

Requires ANY permissions: 

* workitems:wrapup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | The ID of the Workitem.
expands = 'expands_example' # str | Which fields, if any, to expand. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 50. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get all wrapup codes added for all users for a workitem.
    api_response = api_instance.get_taskmanagement_workitem_wrapups(workitem_id, expands=expands, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitem_wrapups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| The ID of the Workitem. |  |
| **expands** | **str**| Which fields, if any, to expand. | [optional] <br />**Values**: wrapupCode |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 50. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**WorkitemWrapupEntityListing**](WorkitemWrapupEntityListing.html)

<a name="get_taskmanagement_workitems_schema"></a>

## [**DataSchema**](DataSchema.html) get_taskmanagement_workitems_schema(schema_id)



Get a schema

get_taskmanagement_workitems_schema is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/workitems/schemas/{schemaId} 

Requires ANY permissions: 

* workitems:workitemSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
schema_id = 'schema_id_example' # str | Schema ID

try:
    # Get a schema
    api_response = api_instance.get_taskmanagement_workitems_schema(schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)

<a name="get_taskmanagement_workitems_schema_version"></a>

## [**DataSchema**](DataSchema.html) get_taskmanagement_workitems_schema_version(schema_id, version_id)



Get a specific version of a schema

get_taskmanagement_workitems_schema_version is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/workitems/schemas/{schemaId}/versions/{versionId} 

Requires ANY permissions: 

* workitems:workitemSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
schema_id = 'schema_id_example' # str | Schema ID
version_id = 'version_id_example' # str | Schema version

try:
    # Get a specific version of a schema
    api_response = api_instance.get_taskmanagement_workitems_schema_version(schema_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_schema_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |
| **version_id** | **str**| Schema version |  |
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)

<a name="get_taskmanagement_workitems_schema_versions"></a>

## [**DataSchema**](DataSchema.html) get_taskmanagement_workitems_schema_versions(schema_id)



Get all versions of a schema

get_taskmanagement_workitems_schema_versions is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/workitems/schemas/{schemaId}/versions 

Requires ANY permissions: 

* workitems:workitemSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
schema_id = 'schema_id_example' # str | Schema ID

try:
    # Get all versions of a schema
    api_response = api_instance.get_taskmanagement_workitems_schema_versions(schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_schema_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)

<a name="get_taskmanagement_workitems_schemas"></a>

## [**DataSchemaListing**](DataSchemaListing.html) get_taskmanagement_workitems_schemas()



Get a list of schemas.

get_taskmanagement_workitems_schemas is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/workitems/schemas 

Requires ANY permissions: 

* workitems:workitemSchema:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()

try:
    # Get a list of schemas.
    api_response = api_instance.get_taskmanagement_workitems_schemas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_workitems_schemas: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**DataSchemaListing**](DataSchemaListing.html)

<a name="get_taskmanagement_worktype"></a>

## [**Worktype**](Worktype.html) get_taskmanagement_worktype(worktype_id, expands=expands)



Get a worktype

get_taskmanagement_worktype is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId} 

Requires ANY permissions: 

* workitems:worktype:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
expands = ['expands_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get a worktype
    api_response = api_instance.get_taskmanagement_worktype(worktype_id, expands=expands)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **expands** | [**list[str]**](str.html)| Which fields, if any, to expand. | [optional] <br />**Values**: defaultQueue, defaultSkills, defaultLanguage, schema |
{: class="table table-striped"}

### Return type

[**Worktype**](Worktype.html)

<a name="get_taskmanagement_worktype_history"></a>

## [**WorktypeChangeListing**](WorktypeChangeListing.html) get_taskmanagement_worktype_history(worktype_id, after=after, page_size=page_size, sort_order=sort_order)



Get a listing of a worktype's attribute change history

get_taskmanagement_worktype_history is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/history 

Requires ANY permissions: 

* workitems:worktype:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get a listing of a worktype's attribute change history
    api_response = api_instance.get_taskmanagement_worktype_history(worktype_id, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_history: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**WorktypeChangeListing**](WorktypeChangeListing.html)

<a name="get_taskmanagement_worktype_status"></a>

## [**WorkitemStatus**](WorkitemStatus.html) get_taskmanagement_worktype_status(worktype_id, status_id)



Get a status

get_taskmanagement_worktype_status is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/statuses/{statusId} 

Requires ANY permissions: 

* workitems:status:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
status_id = 'status_id_example' # str | Status id

try:
    # Get a status
    api_response = api_instance.get_taskmanagement_worktype_status(worktype_id, status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_status: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **status_id** | **str**| Status id |  |
{: class="table table-striped"}

### Return type

[**WorkitemStatus**](WorkitemStatus.html)

<a name="get_taskmanagement_worktype_version"></a>

## [**WorktypeVersion**](WorktypeVersion.html) get_taskmanagement_worktype_version(worktype_id, entity_version)



Get a version of a worktype

get_taskmanagement_worktype_version is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/versions/{entityVersion} 

Requires ANY permissions: 

* workitems:worktype:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
entity_version = 56 # int | Worktype version

try:
    # Get a version of a worktype
    api_response = api_instance.get_taskmanagement_worktype_version(worktype_id, entity_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **entity_version** | **int**| Worktype version |  |
{: class="table table-striped"}

### Return type

[**WorktypeVersion**](WorktypeVersion.html)

<a name="get_taskmanagement_worktype_versions"></a>

## [**WorktypeVersionListing**](WorktypeVersionListing.html) get_taskmanagement_worktype_versions(worktype_id, after=after, page_size=page_size, sort_order=sort_order)



Get all versions of a worktype

get_taskmanagement_worktype_versions is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/taskmanagement/worktypes/{worktypeId}/versions 

Requires ANY permissions: 

* workitems:worktype:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 25 # int | Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an `after` key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. (optional) (default to 25)
sort_order = ''descending'' # str | Ascending or descending sort order (optional) (default to 'descending')

try:
    # Get all versions of a worktype
    api_response = api_instance.get_taskmanagement_worktype_versions(worktype_id, after=after, page_size=page_size, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->get_taskmanagement_worktype_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **int**| Limit the number of entities to return. It is not guaranteed that the requested number of entities will be filled in a single request. If an &#x60;after&#x60; key is returned as part of the response it is possible that more entities that match the filter criteria exist. Maximum of 200. | [optional] [default to 25] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;descending&#39;]<br />**Values**: ascending, descending |
{: class="table table-striped"}

### Return type

[**WorktypeVersionListing**](WorktypeVersionListing.html)

<a name="patch_taskmanagement_workbin"></a>

## [**Workbin**](Workbin.html) patch_taskmanagement_workbin(workbin_id, body)



Update the attributes of a workbin

patch_taskmanagement_workbin is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/taskmanagement/workbins/{workbinId} 

Requires ANY permissions: 

* workitems:workbin:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workbin_id = 'workbin_id_example' # str | Workbin ID
body = PureCloudPlatformClientV2.WorkbinUpdate() # WorkbinUpdate | Json with attributes and their new values: {\"description\":\"new description\", \"name\":\"new name\"}.

try:
    # Update the attributes of a workbin
    api_response = api_instance.patch_taskmanagement_workbin(workbin_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_workbin: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workbin_id** | **str**| Workbin ID |  |
| **body** | [**WorkbinUpdate**](WorkbinUpdate.html)| Json with attributes and their new values: {\&quot;description\&quot;:\&quot;new description\&quot;, \&quot;name\&quot;:\&quot;new name\&quot;}. |  |
{: class="table table-striped"}

### Return type

[**Workbin**](Workbin.html)

<a name="patch_taskmanagement_workitem"></a>

## [**Workitem**](Workitem.html) patch_taskmanagement_workitem(workitem_id, body)



Update the attributes of a workitem

patch_taskmanagement_workitem is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/taskmanagement/workitems/{workitemId} 

Requires ANY permissions: 

* workitems:workitem:edit
* workitems:workitem:accept

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID
body = PureCloudPlatformClientV2.WorkitemUpdate() # WorkitemUpdate | Workitem

try:
    # Update the attributes of a workitem
    api_response = api_instance.patch_taskmanagement_workitem(workitem_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_workitem: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
| **body** | [**WorkitemUpdate**](WorkitemUpdate.html)| Workitem |  |
{: class="table table-striped"}

### Return type

[**Workitem**](Workitem.html)

<a name="patch_taskmanagement_workitem_assignment"></a>

##  patch_taskmanagement_workitem_assignment(workitem_id, body)



Attempts to manually assign a specified workitem to a specified user.  Ignores bullseye ring, PAR score, skills, and languages.

patch_taskmanagement_workitem_assignment is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/taskmanagement/workitems/{workitemId}/assignment 

Requires ANY permissions: 

* workitems:workitem:pull
* workitems:workitem:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID
body = PureCloudPlatformClientV2.WorkitemManualAssign() # WorkitemManualAssign | Targeted user

try:
    # Attempts to manually assign a specified workitem to a specified user.  Ignores bullseye ring, PAR score, skills, and languages.
    api_instance.patch_taskmanagement_workitem_assignment(workitem_id, body)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_workitem_assignment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
| **body** | [**WorkitemManualAssign**](WorkitemManualAssign.html)| Targeted user |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_taskmanagement_workitem_user_wrapups"></a>

## [**WorkitemWrapup**](WorkitemWrapup.html) patch_taskmanagement_workitem_user_wrapups(workitem_id, user_id, body)



Add/Remove a wrapup code for a given user in a workitem.

patch_taskmanagement_workitem_user_wrapups is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/taskmanagement/workitems/{workitemId}/users/{userId}/wrapups 

Requires ANY permissions: 

* workitems:wrapup:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | The ID of the Workitem.
user_id = 'user_id_example' # str | The ID of the user
body = PureCloudPlatformClientV2.WorkitemWrapupUpdate() # WorkitemWrapupUpdate | Request body to add/remove a wrapup code for a workitem

try:
    # Add/Remove a wrapup code for a given user in a workitem.
    api_response = api_instance.patch_taskmanagement_workitem_user_wrapups(workitem_id, user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_workitem_user_wrapups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| The ID of the Workitem. |  |
| **user_id** | **str**| The ID of the user |  |
| **body** | [**WorkitemWrapupUpdate**](WorkitemWrapupUpdate.html)| Request body to add/remove a wrapup code for a workitem |  |
{: class="table table-striped"}

### Return type

[**WorkitemWrapup**](WorkitemWrapup.html)

<a name="patch_taskmanagement_workitem_users_me_wrapups"></a>

## [**WorkitemWrapup**](WorkitemWrapup.html) patch_taskmanagement_workitem_users_me_wrapups(workitem_id, body)



Add/Remove a wrapup code for the current user in a workitem.

patch_taskmanagement_workitem_users_me_wrapups is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/taskmanagement/workitems/{workitemId}/users/me/wrapups 

Requires ANY permissions: 

* workitems:wrapupSelf:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | The ID of the Workitem.
body = PureCloudPlatformClientV2.WorkitemWrapupUpdate() # WorkitemWrapupUpdate | Request body to add/remove the wrapup code for workitem

try:
    # Add/Remove a wrapup code for the current user in a workitem.
    api_response = api_instance.patch_taskmanagement_workitem_users_me_wrapups(workitem_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_workitem_users_me_wrapups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| The ID of the Workitem. |  |
| **body** | [**WorkitemWrapupUpdate**](WorkitemWrapupUpdate.html)| Request body to add/remove the wrapup code for workitem |  |
{: class="table table-striped"}

### Return type

[**WorkitemWrapup**](WorkitemWrapup.html)

<a name="patch_taskmanagement_worktype"></a>

## [**Worktype**](Worktype.html) patch_taskmanagement_worktype(worktype_id, body=body)



Update the attributes of a worktype

patch_taskmanagement_worktype is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/taskmanagement/worktypes/{worktypeId} 

Requires ALL permissions: 

* workitems:worktype:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
body = PureCloudPlatformClientV2.WorktypeUpdate() # WorktypeUpdate | body (optional)

try:
    # Update the attributes of a worktype
    api_response = api_instance.patch_taskmanagement_worktype(worktype_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_worktype: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **body** | [**WorktypeUpdate**](WorktypeUpdate.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**Worktype**](Worktype.html)

<a name="patch_taskmanagement_worktype_status"></a>

## [**WorkitemStatus**](WorkitemStatus.html) patch_taskmanagement_worktype_status(worktype_id, status_id, body=body)



Update the attributes of a status

patch_taskmanagement_worktype_status is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/taskmanagement/worktypes/{worktypeId}/statuses/{statusId} 

Requires ANY permissions: 

* workitems:status:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
status_id = 'status_id_example' # str | Status id
body = PureCloudPlatformClientV2.WorkitemStatusUpdate() # WorkitemStatusUpdate | body (optional)

try:
    # Update the attributes of a status
    api_response = api_instance.patch_taskmanagement_worktype_status(worktype_id, status_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->patch_taskmanagement_worktype_status: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **status_id** | **str**| Status id |  |
| **body** | [**WorkitemStatusUpdate**](WorkitemStatusUpdate.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**WorkitemStatus**](WorkitemStatus.html)

<a name="post_taskmanagement_workbins"></a>

## [**Workbin**](Workbin.html) post_taskmanagement_workbins(body=body)



Create a workbin

post_taskmanagement_workbins is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/taskmanagement/workbins 

Requires ANY permissions: 

* workitems:workbin:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.WorkbinCreate() # WorkbinCreate | body (optional)

try:
    # Create a workbin
    api_response = api_instance.post_taskmanagement_workbins(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workbins: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WorkbinCreate**](WorkbinCreate.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**Workbin**](Workbin.html)

<a name="post_taskmanagement_workbins_query"></a>

## [**WorkbinQueryEntityListing**](WorkbinQueryEntityListing.html) post_taskmanagement_workbins_query(body)



Query for workbins

post_taskmanagement_workbins_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/taskmanagement/workbins/query 

Requires ALL permissions: 

* workitems:workbin:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.WorkbinQueryRequest() # WorkbinQueryRequest | QueryPostRequest

try:
    # Query for workbins
    api_response = api_instance.post_taskmanagement_workbins_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workbins_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WorkbinQueryRequest**](WorkbinQueryRequest.html)| QueryPostRequest |  |
{: class="table table-striped"}

### Return type

[**WorkbinQueryEntityListing**](WorkbinQueryEntityListing.html)

<a name="post_taskmanagement_workitem_acd_cancel"></a>

## [**Workitem**](Workitem.html) post_taskmanagement_workitem_acd_cancel(workitem_id)



Cancel the assignment process for a workitem that is currently queued for assignment through ACD.

post_taskmanagement_workitem_acd_cancel is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/taskmanagement/workitems/{workitemId}/acd/cancel 

Requires ANY permissions: 

* workitems:workitem:cancelRouting

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID

try:
    # Cancel the assignment process for a workitem that is currently queued for assignment through ACD.
    api_response = api_instance.post_taskmanagement_workitem_acd_cancel(workitem_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitem_acd_cancel: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
{: class="table table-striped"}

### Return type

[**Workitem**](Workitem.html)

<a name="post_taskmanagement_workitem_disconnect"></a>

## [**Workitem**](Workitem.html) post_taskmanagement_workitem_disconnect(workitem_id)



Disconnect the assignee of the workitem

post_taskmanagement_workitem_disconnect is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/taskmanagement/workitems/{workitemId}/disconnect 

Requires ANY permissions: 

* workitems:workitem:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID

try:
    # Disconnect the assignee of the workitem
    api_response = api_instance.post_taskmanagement_workitem_disconnect(workitem_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitem_disconnect: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
{: class="table table-striped"}

### Return type

[**Workitem**](Workitem.html)

<a name="post_taskmanagement_workitem_terminate"></a>

## [**Workitem**](Workitem.html) post_taskmanagement_workitem_terminate(workitem_id, body=body)



Terminate a workitem

post_taskmanagement_workitem_terminate is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/taskmanagement/workitems/{workitemId}/terminate 

Requires ANY permissions: 

* workitems:workitem:terminate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
workitem_id = 'workitem_id_example' # str | Workitem ID
body = PureCloudPlatformClientV2.WorkitemTerminate() # WorkitemTerminate | Terminated request (optional)

try:
    # Terminate a workitem
    api_response = api_instance.post_taskmanagement_workitem_terminate(workitem_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitem_terminate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **workitem_id** | **str**| Workitem ID |  |
| **body** | [**WorkitemTerminate**](WorkitemTerminate.html)| Terminated request | [optional]  |
{: class="table table-striped"}

### Return type

[**Workitem**](Workitem.html)

<a name="post_taskmanagement_workitems"></a>

## [**Workitem**](Workitem.html) post_taskmanagement_workitems(body)



Create a workitem

post_taskmanagement_workitems is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/taskmanagement/workitems 

Requires ANY permissions: 

* workitems:workitem:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.WorkitemCreate() # WorkitemCreate | Workitem

try:
    # Create a workitem
    api_response = api_instance.post_taskmanagement_workitems(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitems: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WorkitemCreate**](WorkitemCreate.html)| Workitem |  |
{: class="table table-striped"}

### Return type

[**Workitem**](Workitem.html)

<a name="post_taskmanagement_workitems_query"></a>

## [**WorkitemPostQueryEntityListing**](WorkitemPostQueryEntityListing.html) post_taskmanagement_workitems_query(body)



Query for workitems

This query requires at least one EQ filter on the workbinId, assigneeId or typeId attributes.

post_taskmanagement_workitems_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/taskmanagement/workitems/query 

Requires ANY permissions: 

* workitems:workitem:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.WorkitemQueryPostRequest() # WorkitemQueryPostRequest | WorkitemQueryPostRequest

try:
    # Query for workitems
    api_response = api_instance.post_taskmanagement_workitems_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitems_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WorkitemQueryPostRequest**](WorkitemQueryPostRequest.html)| WorkitemQueryPostRequest |  |
{: class="table table-striped"}

### Return type

[**WorkitemPostQueryEntityListing**](WorkitemPostQueryEntityListing.html)

<a name="post_taskmanagement_workitems_schemas"></a>

## [**DataSchema**](DataSchema.html) post_taskmanagement_workitems_schemas(body)



Create a schema

post_taskmanagement_workitems_schemas is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/taskmanagement/workitems/schemas 

Requires ANY permissions: 

* workitems:workitemSchema:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.DataSchema() # DataSchema | Schema

try:
    # Create a schema
    api_response = api_instance.post_taskmanagement_workitems_schemas(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_workitems_schemas: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DataSchema**](DataSchema.html)| Schema |  |
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)

<a name="post_taskmanagement_worktype_statuses"></a>

## [**WorkitemStatus**](WorkitemStatus.html) post_taskmanagement_worktype_statuses(worktype_id, body=body)



Add a status to a worktype

post_taskmanagement_worktype_statuses is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/taskmanagement/worktypes/{worktypeId}/statuses 

Requires ANY permissions: 

* workitems:status:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
worktype_id = 'worktype_id_example' # str | Worktype id
body = PureCloudPlatformClientV2.WorkitemStatusCreate() # WorkitemStatusCreate | body (optional)

try:
    # Add a status to a worktype
    api_response = api_instance.post_taskmanagement_worktype_statuses(worktype_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_worktype_statuses: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **worktype_id** | **str**| Worktype id |  |
| **body** | [**WorkitemStatusCreate**](WorkitemStatusCreate.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**WorkitemStatus**](WorkitemStatus.html)

<a name="post_taskmanagement_worktypes"></a>

## [**Worktype**](Worktype.html) post_taskmanagement_worktypes(body=body)



Create a worktype

post_taskmanagement_worktypes is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/taskmanagement/worktypes 

Requires ANY permissions: 

* workitems:worktype:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.WorktypeCreate() # WorktypeCreate | body (optional)

try:
    # Create a worktype
    api_response = api_instance.post_taskmanagement_worktypes(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_worktypes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WorktypeCreate**](WorktypeCreate.html)| body | [optional]  |
{: class="table table-striped"}

### Return type

[**Worktype**](Worktype.html)

<a name="post_taskmanagement_worktypes_query"></a>

## [**WorktypeQueryEntityListing**](WorktypeQueryEntityListing.html) post_taskmanagement_worktypes_query(body)



Query for worktypes

post_taskmanagement_worktypes_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/taskmanagement/worktypes/query 

Requires ALL permissions: 

* workitems:worktype:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
body = PureCloudPlatformClientV2.WorktypeQueryRequest() # WorktypeQueryRequest | QueryPostRequest

try:
    # Query for worktypes
    api_response = api_instance.post_taskmanagement_worktypes_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->post_taskmanagement_worktypes_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WorktypeQueryRequest**](WorktypeQueryRequest.html)| QueryPostRequest |  |
{: class="table table-striped"}

### Return type

[**WorktypeQueryEntityListing**](WorktypeQueryEntityListing.html)

<a name="put_taskmanagement_workitems_schema"></a>

## [**DataSchema**](DataSchema.html) put_taskmanagement_workitems_schema(schema_id, body)



Update a schema

put_taskmanagement_workitems_schema is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PUT /api/v2/taskmanagement/workitems/schemas/{schemaId} 

Requires ANY permissions: 

* workitems:workitemSchema:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TaskManagementApi()
schema_id = 'schema_id_example' # str | Schema ID
body = PureCloudPlatformClientV2.DataSchema() # DataSchema | Data Schema

try:
    # Update a schema
    api_response = api_instance.put_taskmanagement_workitems_schema(schema_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskManagementApi->put_taskmanagement_workitems_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| Schema ID |  |
| **body** | [**DataSchema**](DataSchema.html)| Data Schema |  |
{: class="table table-striped"}

### Return type

[**DataSchema**](DataSchema.html)


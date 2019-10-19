---
title: SCIMApi
---

## PureCloudPlatformClientV2.SCIMApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_scim_user**](SCIMApi.html#delete_scim_user) | Delete a user|
|[**delete_scim_v2_user**](SCIMApi.html#delete_scim_v2_user) | Delete a user|
|[**get_scim_group**](SCIMApi.html#get_scim_group) | Get a group|
|[**get_scim_groups**](SCIMApi.html#get_scim_groups) | Get a list of groups|
|[**get_scim_resourcetype**](SCIMApi.html#get_scim_resourcetype) | Get a resource type|
|[**get_scim_resourcetypes**](SCIMApi.html#get_scim_resourcetypes) | Get a list of resource types|
|[**get_scim_serviceproviderconfig**](SCIMApi.html#get_scim_serviceproviderconfig) | Get a service provider&#39;s configuration|
|[**get_scim_user**](SCIMApi.html#get_scim_user) | Get a user|
|[**get_scim_users**](SCIMApi.html#get_scim_users) | Get a list of users|
|[**get_scim_v2_group**](SCIMApi.html#get_scim_v2_group) | Get a group|
|[**get_scim_v2_groups**](SCIMApi.html#get_scim_v2_groups) | Get a list of groups|
|[**get_scim_v2_resourcetype**](SCIMApi.html#get_scim_v2_resourcetype) | Get a resource type|
|[**get_scim_v2_resourcetypes**](SCIMApi.html#get_scim_v2_resourcetypes) | Get a list of resource types|
|[**get_scim_v2_serviceproviderconfig**](SCIMApi.html#get_scim_v2_serviceproviderconfig) | Get a service provider&#39;s configuration|
|[**get_scim_v2_user**](SCIMApi.html#get_scim_v2_user) | Get a user|
|[**get_scim_v2_users**](SCIMApi.html#get_scim_v2_users) | Get a list of users|
|[**patch_scim_group**](SCIMApi.html#patch_scim_group) | Modify a group|
|[**patch_scim_user**](SCIMApi.html#patch_scim_user) | Modify a user|
|[**patch_scim_v2_group**](SCIMApi.html#patch_scim_v2_group) | Modify a group|
|[**patch_scim_v2_user**](SCIMApi.html#patch_scim_v2_user) | Modify a user|
|[**post_scim_users**](SCIMApi.html#post_scim_users) | Create a user|
|[**post_scim_v2_users**](SCIMApi.html#post_scim_v2_users) | Create a user|
|[**put_scim_group**](SCIMApi.html#put_scim_group) | Replace a group|
|[**put_scim_user**](SCIMApi.html#put_scim_user) | Replace a user|
|[**put_scim_v2_group**](SCIMApi.html#put_scim_v2_group) | Replace a group|
|[**put_scim_v2_user**](SCIMApi.html#put_scim_v2_user) | Replace a user|
{: class="table table-striped"}

<a name="delete_scim_user"></a>

## [**Empty**](Empty.html) delete_scim_user(user_id, if_match=if_match)



Delete a user



Wraps DELETE /api/v2/scim/users/{userId} 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
user_id = 'user_id_example' # str | The ID of a user. Returned with GET /api/v2/scim/users.
if_match = 'if_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/users/{userId}. Example: \"42\". If the ETag is different from the version on the server, returns 400 with a \"scimType\" of \"invalidVers\". (optional)

try:
    # Delete a user
    api_response = api_instance.delete_scim_user(user_id, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->delete_scim_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/users. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="delete_scim_v2_user"></a>

## [**Empty**](Empty.html) delete_scim_v2_user(user_id, if_match=if_match)



Delete a user



Wraps DELETE /api/v2/scim/v2/users/{userId} 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
user_id = 'user_id_example' # str | The ID of a user. Returned with GET /api/v2/scim/v2/users.
if_match = 'if_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/users/{userId}. Example: \"42\". If the ETag is different from the version on the server, returns 400 with a \"scimType\" of \"invalidVers\". (optional)

try:
    # Delete a user
    api_response = api_instance.delete_scim_v2_user(user_id, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->delete_scim_v2_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/v2/users. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="get_scim_group"></a>

## [**ScimV2Group**](ScimV2Group.html) get_scim_group(group_id, if_none_match=if_none_match)



Get a group



Wraps GET /api/v2/scim/groups/{groupId} 

Requires ANY permissions: 

* directory:group:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SCIMApi()
group_id = 'group_id_example' # str | The ID of a group. Returned with GET /api/v2/scim/groups.
if_none_match = 'if_none_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/groups/{groupId}. Example: \"42\". If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified. (optional)

try:
    # Get a group
    api_response = api_instance.get_scim_group(group_id, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_group: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| The ID of a group. Returned with GET /api/v2/scim/groups. |  |
| **if_none_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/groups/{groupId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified. | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2Group**](ScimV2Group.html)

<a name="get_scim_groups"></a>

## [**ScimGroupListResponse**](ScimGroupListResponse.html) get_scim_groups(start_index=start_index, count=count, filter=filter)



Get a list of groups



Wraps GET /api/v2/scim/groups 

Requires ANY permissions: 

* directory:group:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SCIMApi()
start_index = 1 # int | The 1-based index of the first query result. (optional) (default to 1)
count = 25 # int | The requested number of items per page. A value of 0 returns \"totalResults\". (optional) (default to 25)
filter = 'displayName eq groupName' # str | Filters results. (optional)

try:
    # Get a list of groups
    api_response = api_instance.get_scim_groups(start_index=start_index, count=count, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_groups: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **start_index** | **int**| The 1-based index of the first query result. | [optional] [default to 1] |
| **count** | **int**| The requested number of items per page. A value of 0 returns \&quot;totalResults\&quot;. | [optional] [default to 25] |
| **filter** | **str**| Filters results. | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimGroupListResponse**](ScimGroupListResponse.html)

<a name="get_scim_resourcetype"></a>

## [**ScimConfigResourceType**](ScimConfigResourceType.html) get_scim_resourcetype(resource_type)



Get a resource type



Wraps GET /api/v2/scim/resourcetypes/{resourceType} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SCIMApi()
resource_type = 'resource_type_example' # str | The type of resource. Returned with GET /api/v2/scim/resourcetypes.

try:
    # Get a resource type
    api_response = api_instance.get_scim_resourcetype(resource_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_resourcetype: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **resource_type** | **str**| The type of resource. Returned with GET /api/v2/scim/resourcetypes. | <br />**Values**: User, Group, ServiceProviderConfig, ResourceType |
{: class="table table-striped"}

### Return type

[**ScimConfigResourceType**](ScimConfigResourceType.html)

<a name="get_scim_resourcetypes"></a>

## [**ScimConfigResourceTypesListResponse**](ScimConfigResourceTypesListResponse.html) get_scim_resourcetypes()



Get a list of resource types



Wraps GET /api/v2/scim/resourcetypes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SCIMApi()

try:
    # Get a list of resource types
    api_response = api_instance.get_scim_resourcetypes()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_resourcetypes: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**ScimConfigResourceTypesListResponse**](ScimConfigResourceTypesListResponse.html)

<a name="get_scim_serviceproviderconfig"></a>

## [**ScimServiceProviderConfig**](ScimServiceProviderConfig.html) get_scim_serviceproviderconfig(if_none_match=if_none_match)



Get a service provider's configuration



Wraps GET /api/v2/scim/serviceproviderconfig 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SCIMApi()
if_none_match = 'if_none_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/serviceproviderconfig. Example: \"42\". If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified.  (optional)

try:
    # Get a service provider's configuration
    api_response = api_instance.get_scim_serviceproviderconfig(if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_serviceproviderconfig: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **if_none_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/serviceproviderconfig. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified.  | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimServiceProviderConfig**](ScimServiceProviderConfig.html)

<a name="get_scim_user"></a>

## [**ScimV2User**](ScimV2User.html) get_scim_user(user_id, if_none_match=if_none_match)



Get a user



Wraps GET /api/v2/scim/users/{userId} 

Requires ANY permissions: 

* directory:user:view
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
api_instance = PureCloudPlatformClientV2.SCIMApi()
user_id = 'user_id_example' # str | The ID of a user. Returned with GET /api/v2/scim/users.
if_none_match = 'if_none_match_example' # str | TThe ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/users/{userId}. Example: \"42\". If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified. (optional)

try:
    # Get a user
    api_response = api_instance.get_scim_user(user_id, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/users. |  |
| **if_none_match** | **str**| TThe ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified. | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)

<a name="get_scim_users"></a>

## [**ScimUserListResponse**](ScimUserListResponse.html) get_scim_users(filter, start_index=start_index, count=count)



Get a list of users



Wraps GET /api/v2/scim/users 

Requires ANY permissions: 

* directory:user:view
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
api_instance = PureCloudPlatformClientV2.SCIMApi()
filter = 'filter_example' # str | Filters results.
start_index = 1 # int | The 1-based index of the first query result. (optional) (default to 1)
count = 25 # int | The requested number of items per page. A value of 0 returns \"totalResults\". (optional) (default to 25)

try:
    # Get a list of users
    api_response = api_instance.get_scim_users(filter, start_index=start_index, count=count)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_users: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter** | **str**| Filters results. |  |
| **start_index** | **int**| The 1-based index of the first query result. | [optional] [default to 1] |
| **count** | **int**| The requested number of items per page. A value of 0 returns \&quot;totalResults\&quot;. | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**ScimUserListResponse**](ScimUserListResponse.html)

<a name="get_scim_v2_group"></a>

## [**ScimV2Group**](ScimV2Group.html) get_scim_v2_group(group_id, if_none_match=if_none_match)



Get a group



Wraps GET /api/v2/scim/v2/groups/{groupId} 

Requires ANY permissions: 

* directory:group:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SCIMApi()
group_id = 'group_id_example' # str | The ID of a group. Returned with GET /api/v2/scim/v2/groups.
if_none_match = 'if_none_match_example' # str | TThe ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/groups/{groupId}. Example: \"42\". If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified.  (optional)

try:
    # Get a group
    api_response = api_instance.get_scim_v2_group(group_id, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_v2_group: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| The ID of a group. Returned with GET /api/v2/scim/v2/groups. |  |
| **if_none_match** | **str**| TThe ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/groups/{groupId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified.  | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2Group**](ScimV2Group.html)

<a name="get_scim_v2_groups"></a>

## [**ScimGroupListResponse**](ScimGroupListResponse.html) get_scim_v2_groups(filter, start_index=start_index, count=count)



Get a list of groups



Wraps GET /api/v2/scim/v2/groups 

Requires ANY permissions: 

* directory:group:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SCIMApi()
filter = 'displayName eq groupName' # str | Filters results.
start_index = 1 # int | The 1-based index of the first query result. (optional) (default to 1)
count = 25 # int | The requested number of items per page. A value of 0 returns \"totalResults\". (optional) (default to 25)

try:
    # Get a list of groups
    api_response = api_instance.get_scim_v2_groups(filter, start_index=start_index, count=count)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_v2_groups: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter** | **str**| Filters results. |  |
| **start_index** | **int**| The 1-based index of the first query result. | [optional] [default to 1] |
| **count** | **int**| The requested number of items per page. A value of 0 returns \&quot;totalResults\&quot;. | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**ScimGroupListResponse**](ScimGroupListResponse.html)

<a name="get_scim_v2_resourcetype"></a>

## [**ScimConfigResourceType**](ScimConfigResourceType.html) get_scim_v2_resourcetype(resource_type)



Get a resource type



Wraps GET /api/v2/scim/v2/resourcetypes/{resourceType} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SCIMApi()
resource_type = 'resource_type_example' # str | The type of resource. Returned with GET /api/v2/scim/v2/resourcetypes.

try:
    # Get a resource type
    api_response = api_instance.get_scim_v2_resourcetype(resource_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_v2_resourcetype: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **resource_type** | **str**| The type of resource. Returned with GET /api/v2/scim/v2/resourcetypes. | <br />**Values**: User, Group, ServiceProviderConfig, ResourceType |
{: class="table table-striped"}

### Return type

[**ScimConfigResourceType**](ScimConfigResourceType.html)

<a name="get_scim_v2_resourcetypes"></a>

## [**ScimConfigResourceTypesListResponse**](ScimConfigResourceTypesListResponse.html) get_scim_v2_resourcetypes()



Get a list of resource types



Wraps GET /api/v2/scim/v2/resourcetypes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SCIMApi()

try:
    # Get a list of resource types
    api_response = api_instance.get_scim_v2_resourcetypes()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_v2_resourcetypes: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**ScimConfigResourceTypesListResponse**](ScimConfigResourceTypesListResponse.html)

<a name="get_scim_v2_serviceproviderconfig"></a>

## [**ScimServiceProviderConfig**](ScimServiceProviderConfig.html) get_scim_v2_serviceproviderconfig(if_none_match=if_none_match)



Get a service provider's configuration



Wraps GET /api/v2/scim/v2/serviceproviderconfig 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SCIMApi()
if_none_match = 'if_none_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/serviceproviderconfig. Example: \"42\". If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified.  (optional)

try:
    # Get a service provider's configuration
    api_response = api_instance.get_scim_v2_serviceproviderconfig(if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_v2_serviceproviderconfig: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **if_none_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/serviceproviderconfig. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified.  | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimServiceProviderConfig**](ScimServiceProviderConfig.html)

<a name="get_scim_v2_user"></a>

## [**ScimV2User**](ScimV2User.html) get_scim_v2_user(user_id, if_none_match=if_none_match)



Get a user



Wraps GET /api/v2/scim/v2/users/{userId} 

Requires ANY permissions: 

* directory:user:view
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
api_instance = PureCloudPlatformClientV2.SCIMApi()
user_id = 'user_id_example' # str | The ID of a user. Returned with GET /api/v2/scim/v2/users.
if_none_match = 'if_none_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/users/{userId}. Example: \"42\". If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified. (optional)

try:
    # Get a user
    api_response = api_instance.get_scim_v2_user(user_id, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_v2_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/v2/users. |  |
| **if_none_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified. | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)

<a name="get_scim_v2_users"></a>

## [**ScimUserListResponse**](ScimUserListResponse.html) get_scim_v2_users(filter, start_index=start_index, count=count)



Get a list of users



Wraps GET /api/v2/scim/v2/users 

Requires ANY permissions: 

* directory:user:view
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
api_instance = PureCloudPlatformClientV2.SCIMApi()
filter = 'filter_example' # str | Filters results.
start_index = 1 # int | The 1-based index of the first query result. (optional) (default to 1)
count = 25 # int | The requested number of items per page. A value of 0 returns \"totalResults\". (optional) (default to 25)

try:
    # Get a list of users
    api_response = api_instance.get_scim_v2_users(filter, start_index=start_index, count=count)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_v2_users: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter** | **str**| Filters results. |  |
| **start_index** | **int**| The 1-based index of the first query result. | [optional] [default to 1] |
| **count** | **int**| The requested number of items per page. A value of 0 returns \&quot;totalResults\&quot;. | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**ScimUserListResponse**](ScimUserListResponse.html)

<a name="patch_scim_group"></a>

## [**ScimV2Group**](ScimV2Group.html) patch_scim_group(group_id, body, if_match=if_match)



Modify a group



Wraps PATCH /api/v2/scim/groups/{groupId} 

Requires ANY permissions: 

* directory:group:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SCIMApi()
group_id = 'group_id_example' # str | The ID of a group. Returned with GET /api/v2/scim/groups.
body = PureCloudPlatformClientV2.ScimV2PatchRequest() # ScimV2PatchRequest | The information used to modify a group.
if_match = 'if_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/groups/{groupId}. Example: \"42\". If the ETag is different from the version on the server, returns 400 with a \"scimType\" of \"invalidVers\". (optional)

try:
    # Modify a group
    api_response = api_instance.patch_scim_group(group_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->patch_scim_group: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| The ID of a group. Returned with GET /api/v2/scim/groups. |  |
| **body** | [**ScimV2PatchRequest**](ScimV2PatchRequest.html)| The information used to modify a group. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/groups/{groupId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2Group**](ScimV2Group.html)

<a name="patch_scim_user"></a>

## [**ScimV2User**](ScimV2User.html) patch_scim_user(user_id, body, if_match=if_match)



Modify a user



Wraps PATCH /api/v2/scim/users/{userId} 

Requires ANY permissions: 

* directory:user:edit
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
api_instance = PureCloudPlatformClientV2.SCIMApi()
user_id = 'user_id_example' # str | The ID of a user. Returned with GET /api/v2/scim/users.
body = PureCloudPlatformClientV2.ScimV2PatchRequest() # ScimV2PatchRequest | The information used to modify a user.
if_match = 'if_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/users/{userId}. Example: \"42\". If the ETag is different from the version on the server, returns 400 with a \"scimType\" of \"invalidVers\". (optional)

try:
    # Modify a user
    api_response = api_instance.patch_scim_user(user_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->patch_scim_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/users. |  |
| **body** | [**ScimV2PatchRequest**](ScimV2PatchRequest.html)| The information used to modify a user. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)

<a name="patch_scim_v2_group"></a>

## [**ScimV2Group**](ScimV2Group.html) patch_scim_v2_group(group_id, body, if_match=if_match)



Modify a group



Wraps PATCH /api/v2/scim/v2/groups/{groupId} 

Requires ANY permissions: 

* directory:group:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SCIMApi()
group_id = 'group_id_example' # str | The ID of a group. Returned with GET /api/v2/scim/v2/groups.
body = PureCloudPlatformClientV2.ScimV2PatchRequest() # ScimV2PatchRequest | The information used to modify a group.
if_match = 'if_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/groups/{groupId}. Example: \"42\". If the ETag is different from the version on the server, returns 400 with a \"scimType\" of \"invalidVers\". (optional)

try:
    # Modify a group
    api_response = api_instance.patch_scim_v2_group(group_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->patch_scim_v2_group: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| The ID of a group. Returned with GET /api/v2/scim/v2/groups. |  |
| **body** | [**ScimV2PatchRequest**](ScimV2PatchRequest.html)| The information used to modify a group. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/groups/{groupId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2Group**](ScimV2Group.html)

<a name="patch_scim_v2_user"></a>

## [**ScimV2User**](ScimV2User.html) patch_scim_v2_user(user_id, body, if_match=if_match)



Modify a user



Wraps PATCH /api/v2/scim/v2/users/{userId} 

Requires ANY permissions: 

* directory:user:edit
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
api_instance = PureCloudPlatformClientV2.SCIMApi()
user_id = 'user_id_example' # str | The ID of a user. Returned with GET /api/v2/scim/v2/users.
body = PureCloudPlatformClientV2.ScimV2PatchRequest() # ScimV2PatchRequest | The information used to modify a user.
if_match = 'if_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/users/{userId}. Example: \"42\". If the ETag is different from the version on the server, returns 400 with a \"scimType\" of \"invalidVers\". (optional)

try:
    # Modify a user
    api_response = api_instance.patch_scim_v2_user(user_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->patch_scim_v2_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/v2/users. |  |
| **body** | [**ScimV2PatchRequest**](ScimV2PatchRequest.html)| The information used to modify a user. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)

<a name="post_scim_users"></a>

## [**ScimV2User**](ScimV2User.html) post_scim_users(body)



Create a user



Wraps POST /api/v2/scim/users 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
body = PureCloudPlatformClientV2.ScimV2CreateUser() # ScimV2CreateUser | The information used to create a user.

try:
    # Create a user
    api_response = api_instance.post_scim_users(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->post_scim_users: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ScimV2CreateUser**](ScimV2CreateUser.html)| The information used to create a user. |  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)

<a name="post_scim_v2_users"></a>

## [**ScimV2User**](ScimV2User.html) post_scim_v2_users(body)



Create a user



Wraps POST /api/v2/scim/v2/users 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
body = PureCloudPlatformClientV2.ScimV2CreateUser() # ScimV2CreateUser | The information used to create a user.

try:
    # Create a user
    api_response = api_instance.post_scim_v2_users(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->post_scim_v2_users: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ScimV2CreateUser**](ScimV2CreateUser.html)| The information used to create a user. |  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)

<a name="put_scim_group"></a>

## [**ScimV2Group**](ScimV2Group.html) put_scim_group(group_id, body, if_match=if_match)



Replace a group



Wraps PUT /api/v2/scim/groups/{groupId} 

Requires ANY permissions: 

* directory:group:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SCIMApi()
group_id = 'group_id_example' # str | The ID of a group. Returned with GET /api/v2/scim/groups.
body = PureCloudPlatformClientV2.ScimV2Group() # ScimV2Group | The information used to replace a group.
if_match = 'if_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/groups/{groupId}. Example: \"42\". If the ETag is different from the version on the server, returns 400 with a \"scimType\" of \"invalidVers\". (optional)

try:
    # Replace a group
    api_response = api_instance.put_scim_group(group_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->put_scim_group: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| The ID of a group. Returned with GET /api/v2/scim/groups. |  |
| **body** | [**ScimV2Group**](ScimV2Group.html)| The information used to replace a group. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/groups/{groupId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2Group**](ScimV2Group.html)

<a name="put_scim_user"></a>

## [**ScimV2User**](ScimV2User.html) put_scim_user(user_id, body, if_match=if_match)



Replace a user



Wraps PUT /api/v2/scim/users/{userId} 

Requires ANY permissions: 

* directory:user:edit
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
api_instance = PureCloudPlatformClientV2.SCIMApi()
user_id = 'user_id_example' # str | The ID of a user. Returned with GET /api/v2/scim/users.
body = PureCloudPlatformClientV2.ScimV2User() # ScimV2User | The information used to replace a user.
if_match = 'if_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/users/{userId}. Example: \"42\". If the ETag is different from the version on the server, returns 400 with a \"scimType\" of \"invalidVers\". (optional)

try:
    # Replace a user
    api_response = api_instance.put_scim_user(user_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->put_scim_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/users. |  |
| **body** | [**ScimV2User**](ScimV2User.html)| The information used to replace a user. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)

<a name="put_scim_v2_group"></a>

## [**ScimV2Group**](ScimV2Group.html) put_scim_v2_group(group_id, body, if_match=if_match)



Replace a group



Wraps PUT /api/v2/scim/v2/groups/{groupId} 

Requires ANY permissions: 

* directory:group:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SCIMApi()
group_id = 'group_id_example' # str | The ID of a group. Returned with GET /api/v2/scim/v2/groups.
body = PureCloudPlatformClientV2.ScimV2Group() # ScimV2Group | The information used to replace a group.
if_match = 'if_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/groups/{groupId}. Example: \"42\". If the ETag is different from the version on the server, returns 400 with a \"scimType\" of \"invalidVers\". (optional)

try:
    # Replace a group
    api_response = api_instance.put_scim_v2_group(group_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->put_scim_v2_group: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| The ID of a group. Returned with GET /api/v2/scim/v2/groups. |  |
| **body** | [**ScimV2Group**](ScimV2Group.html)| The information used to replace a group. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/groups/{groupId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2Group**](ScimV2Group.html)

<a name="put_scim_v2_user"></a>

## [**ScimV2User**](ScimV2User.html) put_scim_v2_user(user_id, body, if_match=if_match)



Replace a user



Wraps PUT /api/v2/scim/v2/users/{userId} 

Requires ANY permissions: 

* directory:user:edit
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
api_instance = PureCloudPlatformClientV2.SCIMApi()
user_id = 'user_id_example' # str | The ID of a user. Returned with GET /api/v2/scim/v2/users.
body = PureCloudPlatformClientV2.ScimV2User() # ScimV2User | The information used to replace a user.
if_match = 'if_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/users/{userId}. Example: \"42\". If the ETag is different from the version on the server, returns 400 with a \"scimType\" of \"invalidVers\". (optional)

try:
    # Replace a user
    api_response = api_instance.put_scim_v2_user(user_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->put_scim_v2_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/v2/users. |  |
| **body** | [**ScimV2User**](ScimV2User.html)| The information used to replace a user. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)


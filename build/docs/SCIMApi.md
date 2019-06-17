---
title: SCIMApi
---

## PureCloudPlatformClientV2.SCIMApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_scim_user**](SCIMApi.html#delete_scim_user) | Soft delete user with specified ID|
|[**delete_scim_v2_user**](SCIMApi.html#delete_scim_v2_user) | Soft delete user with specified ID|
|[**get_scim_group**](SCIMApi.html#get_scim_group) | Return Group with specified ID|
|[**get_scim_groups**](SCIMApi.html#get_scim_groups) | Query Groups|
|[**get_scim_user**](SCIMApi.html#get_scim_user) | Return user with specified ID (default version)|
|[**get_scim_users**](SCIMApi.html#get_scim_users) | Query Users|
|[**get_scim_v2_group**](SCIMApi.html#get_scim_v2_group) | Return Group with specified ID|
|[**get_scim_v2_groups**](SCIMApi.html#get_scim_v2_groups) | Query Groups|
|[**get_scim_v2_serviceproviderconfig**](SCIMApi.html#get_scim_v2_serviceproviderconfig) | Get SCIM Configuration|
|[**get_scim_v2_user**](SCIMApi.html#get_scim_v2_user) | Return User with specified ID|
|[**get_scim_v2_users**](SCIMApi.html#get_scim_v2_users) | Query Users|
|[**patch_scim_group**](SCIMApi.html#patch_scim_group) | Update Group with specified ID|
|[**patch_scim_user**](SCIMApi.html#patch_scim_user) | Patch user with specified ID|
|[**patch_scim_v2_group**](SCIMApi.html#patch_scim_v2_group) | Update Group with specified ID|
|[**patch_scim_v2_user**](SCIMApi.html#patch_scim_v2_user) | Update user with specified ID|
|[**post_scim_users**](SCIMApi.html#post_scim_users) | Create user|
|[**post_scim_v2_users**](SCIMApi.html#post_scim_v2_users) | Create user|
|[**put_scim_group**](SCIMApi.html#put_scim_group) | Update Group with specified ID|
|[**put_scim_user**](SCIMApi.html#put_scim_user) | Update user with specified ID|
|[**put_scim_v2_group**](SCIMApi.html#put_scim_v2_group) | Update Group with specified ID|
|[**put_scim_v2_user**](SCIMApi.html#put_scim_v2_user) | Update user with specified ID|
{: class="table table-striped"}

<a name="delete_scim_user"></a>

## [**Empty**](Empty.html) delete_scim_user(user_id, if_match=if_match)



Soft delete user with specified ID



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
user_id = 'user_id_example' # str | 
if_match = 'if_match_example' # str | If-Match for ETag version checking (optional)

try:
    # Soft delete user with specified ID
    api_response = api_instance.delete_scim_user(user_id, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->delete_scim_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**|  |  |
| **if_match** | **str**| If-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="delete_scim_v2_user"></a>

## [**Empty**](Empty.html) delete_scim_v2_user(user_id, if_match=if_match)



Soft delete user with specified ID



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
user_id = 'user_id_example' # str | 
if_match = 'if_match_example' # str | If-Match for ETag version checking (optional)

try:
    # Soft delete user with specified ID
    api_response = api_instance.delete_scim_v2_user(user_id, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->delete_scim_v2_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**|  |  |
| **if_match** | **str**| If-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="get_scim_group"></a>

## [**ScimV2Group**](ScimV2Group.html) get_scim_group(group_id, if_none_match=if_none_match)



Return Group with specified ID



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
group_id = 'group_id_example' # str | 
if_none_match = 'if_none_match_example' # str | If-None-Match for ETag version checking (optional)

try:
    # Return Group with specified ID
    api_response = api_instance.get_scim_group(group_id, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_group: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**|  |  |
| **if_none_match** | **str**| If-None-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2Group**](ScimV2Group.html)

<a name="get_scim_groups"></a>

## [**ScimListResponse**](ScimListResponse.html) get_scim_groups(start_index=start_index, count=count, filter=filter)



Query Groups



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
start_index = 1 # int | Starting item of request. 1-based (optional) (default to 1)
count = 25 # int | The requested number of items per page. A value of 0 will return no results other than the totalResults count. (optional) (default to 25)
filter = 'displayName eq groupName' # str | filter parameter e.g. displayName eq groupName (optional)

try:
    # Query Groups
    api_response = api_instance.get_scim_groups(start_index=start_index, count=count, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_groups: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **start_index** | **int**| Starting item of request. 1-based | [optional] [default to 1] |
| **count** | **int**| The requested number of items per page. A value of 0 will return no results other than the totalResults count. | [optional] [default to 25] |
| **filter** | **str**| filter parameter e.g. displayName eq groupName | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimListResponse**](ScimListResponse.html)

<a name="get_scim_user"></a>

## [**ScimV2User**](ScimV2User.html) get_scim_user(user_id, if_none_match=if_none_match)



Return user with specified ID (default version)



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
user_id = 'user_id_example' # str | 
if_none_match = 'if_none_match_example' # str | If-None-Match for ETag version checking (optional)

try:
    # Return user with specified ID (default version)
    api_response = api_instance.get_scim_user(user_id, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**|  |  |
| **if_none_match** | **str**| If-None-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)

<a name="get_scim_users"></a>

## [**ScimListResponse**](ScimListResponse.html) get_scim_users(filter, start_index=start_index, count=count)



Query Users



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
filter = 'filter_example' # str | filter parameter e.g. userName eq search@sample.org
start_index = 1 # int | Starting item of request. 1-based (optional) (default to 1)
count = 25 # int | The requested number of items per page. A value of 0 will return no results other than the totalResults count. (optional) (default to 25)

try:
    # Query Users
    api_response = api_instance.get_scim_users(filter, start_index=start_index, count=count)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_users: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter** | **str**| filter parameter e.g. userName eq search@sample.org |  |
| **start_index** | **int**| Starting item of request. 1-based | [optional] [default to 1] |
| **count** | **int**| The requested number of items per page. A value of 0 will return no results other than the totalResults count. | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**ScimListResponse**](ScimListResponse.html)

<a name="get_scim_v2_group"></a>

## [**ScimV2Group**](ScimV2Group.html) get_scim_v2_group(group_id, if_none_match=if_none_match)



Return Group with specified ID



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
group_id = 'group_id_example' # str | 
if_none_match = 'if_none_match_example' # str | If-None-Match for ETag version checking (optional)

try:
    # Return Group with specified ID
    api_response = api_instance.get_scim_v2_group(group_id, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_v2_group: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**|  |  |
| **if_none_match** | **str**| If-None-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2Group**](ScimV2Group.html)

<a name="get_scim_v2_groups"></a>

## [**ScimListResponse**](ScimListResponse.html) get_scim_v2_groups(filter, start_index=start_index, count=count)



Query Groups



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
filter = 'displayName eq groupName' # str | filter parameter e.g. displayName eq groupName
start_index = 1 # int | Starting item of request. 1-based (optional) (default to 1)
count = 25 # int | The requested number of items per page. A value of 0 will return no results other than the totalResults count. (optional) (default to 25)

try:
    # Query Groups
    api_response = api_instance.get_scim_v2_groups(filter, start_index=start_index, count=count)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_v2_groups: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter** | **str**| filter parameter e.g. displayName eq groupName |  |
| **start_index** | **int**| Starting item of request. 1-based | [optional] [default to 1] |
| **count** | **int**| The requested number of items per page. A value of 0 will return no results other than the totalResults count. | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**ScimListResponse**](ScimListResponse.html)

<a name="get_scim_v2_serviceproviderconfig"></a>

## [**ScimServiceProviderConfig**](ScimServiceProviderConfig.html) get_scim_v2_serviceproviderconfig(if_none_match=if_none_match)



Get SCIM Configuration



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
if_none_match = 'if_none_match_example' # str | If-None-Match for ETag version checking (optional)

try:
    # Get SCIM Configuration
    api_response = api_instance.get_scim_v2_serviceproviderconfig(if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_v2_serviceproviderconfig: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **if_none_match** | **str**| If-None-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimServiceProviderConfig**](ScimServiceProviderConfig.html)

<a name="get_scim_v2_user"></a>

## [**ScimV2User**](ScimV2User.html) get_scim_v2_user(user_id, if_none_match=if_none_match)



Return User with specified ID



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
user_id = 'user_id_example' # str | 
if_none_match = 'if_none_match_example' # str | If-None-Match for ETag version checking (optional)

try:
    # Return User with specified ID
    api_response = api_instance.get_scim_v2_user(user_id, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_v2_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**|  |  |
| **if_none_match** | **str**| If-None-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)

<a name="get_scim_v2_users"></a>

## [**ScimListResponse**](ScimListResponse.html) get_scim_v2_users(filter, start_index=start_index, count=count)



Query Users



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
filter = 'filter_example' # str | filter parameter e.g. userName eq search@sample.org
start_index = 1 # int | Starting item of request. 1-based (optional) (default to 1)
count = 25 # int | The requested number of items per page. A value of 0 will return no results other than the totalResults count. (optional) (default to 25)

try:
    # Query Users
    api_response = api_instance.get_scim_v2_users(filter, start_index=start_index, count=count)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->get_scim_v2_users: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter** | **str**| filter parameter e.g. userName eq search@sample.org |  |
| **start_index** | **int**| Starting item of request. 1-based | [optional] [default to 1] |
| **count** | **int**| The requested number of items per page. A value of 0 will return no results other than the totalResults count. | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**ScimListResponse**](ScimListResponse.html)

<a name="patch_scim_group"></a>

## [**ScimV2Group**](ScimV2Group.html) patch_scim_group(group_id, body, if_match=if_match)



Update Group with specified ID



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
group_id = 'group_id_example' # str | 
body = PureCloudPlatformClientV2.PatchRequest() # PatchRequest | Group
if_match = 'if_match_example' # str | If-Match for ETag version checking (optional)

try:
    # Update Group with specified ID
    api_response = api_instance.patch_scim_group(group_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->patch_scim_group: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**|  |  |
| **body** | [**PatchRequest**](PatchRequest.html)| Group |  |
| **if_match** | **str**| If-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2Group**](ScimV2Group.html)

<a name="patch_scim_user"></a>

## [**ScimV2User**](ScimV2User.html) patch_scim_user(user_id, body, if_match=if_match)



Patch user with specified ID



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
user_id = 'user_id_example' # str | 
body = PureCloudPlatformClientV2.ScimV2PatchRequest() # ScimV2PatchRequest | SCIM Patch Request
if_match = 'if_match_example' # str | If-Match for ETag version checking (optional)

try:
    # Patch user with specified ID
    api_response = api_instance.patch_scim_user(user_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->patch_scim_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**|  |  |
| **body** | [**ScimV2PatchRequest**](ScimV2PatchRequest.html)| SCIM Patch Request |  |
| **if_match** | **str**| If-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)

<a name="patch_scim_v2_group"></a>

## [**ScimV2Group**](ScimV2Group.html) patch_scim_v2_group(group_id, body, if_match=if_match)



Update Group with specified ID



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
group_id = 'group_id_example' # str | 
body = PureCloudPlatformClientV2.PatchRequest() # PatchRequest | Group
if_match = 'if_match_example' # str | If-Match for ETag version checking (optional)

try:
    # Update Group with specified ID
    api_response = api_instance.patch_scim_v2_group(group_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->patch_scim_v2_group: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**|  |  |
| **body** | [**PatchRequest**](PatchRequest.html)| Group |  |
| **if_match** | **str**| If-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2Group**](ScimV2Group.html)

<a name="patch_scim_v2_user"></a>

## [**ScimV2User**](ScimV2User.html) patch_scim_v2_user(user_id, body, if_match=if_match)



Update user with specified ID



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
user_id = 'user_id_example' # str | User Id
body = PureCloudPlatformClientV2.ScimV2PatchRequest() # ScimV2PatchRequest | SCIM Patch Request
if_match = 'if_match_example' # str | If-Match for ETag version checking (optional)

try:
    # Update user with specified ID
    api_response = api_instance.patch_scim_v2_user(user_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->patch_scim_v2_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User Id |  |
| **body** | [**ScimV2PatchRequest**](ScimV2PatchRequest.html)| SCIM Patch Request |  |
| **if_match** | **str**| If-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)

<a name="post_scim_users"></a>

## [**ScimV2User**](ScimV2User.html) post_scim_users(body)



Create user



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
body = PureCloudPlatformClientV2.ScimV2CreateUser() # ScimV2CreateUser | SCIM Create User

try:
    # Create user
    api_response = api_instance.post_scim_users(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->post_scim_users: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ScimV2CreateUser**](ScimV2CreateUser.html)| SCIM Create User |  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)

<a name="post_scim_v2_users"></a>

## [**ScimV2User**](ScimV2User.html) post_scim_v2_users(body)



Create user



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
body = PureCloudPlatformClientV2.ScimV2CreateUser() # ScimV2CreateUser | SCIM Create User

try:
    # Create user
    api_response = api_instance.post_scim_v2_users(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->post_scim_v2_users: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ScimV2CreateUser**](ScimV2CreateUser.html)| SCIM Create User |  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)

<a name="put_scim_group"></a>

## [**ScimV2Group**](ScimV2Group.html) put_scim_group(group_id, body, if_match=if_match)



Update Group with specified ID



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
group_id = 'group_id_example' # str | 
body = PureCloudPlatformClientV2.ScimV2Group() # ScimV2Group | Group
if_match = 'if_match_example' # str | If-Match for ETag version checking (optional)

try:
    # Update Group with specified ID
    api_response = api_instance.put_scim_group(group_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->put_scim_group: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**|  |  |
| **body** | [**ScimV2Group**](ScimV2Group.html)| Group |  |
| **if_match** | **str**| If-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2Group**](ScimV2Group.html)

<a name="put_scim_user"></a>

## [**ScimV2User**](ScimV2User.html) put_scim_user(user_id, body, if_match=if_match)



Update user with specified ID



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
user_id = 'user_id_example' # str | 
body = PureCloudPlatformClientV2.ScimV2User() # ScimV2User | User
if_match = 'if_match_example' # str | If-Match for ETag version checking (optional)

try:
    # Update user with specified ID
    api_response = api_instance.put_scim_user(user_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->put_scim_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**|  |  |
| **body** | [**ScimV2User**](ScimV2User.html)| User |  |
| **if_match** | **str**| If-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)

<a name="put_scim_v2_group"></a>

## [**ScimV2Group**](ScimV2Group.html) put_scim_v2_group(group_id, body, if_match=if_match)



Update Group with specified ID



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
group_id = 'group_id_example' # str | 
body = PureCloudPlatformClientV2.ScimV2Group() # ScimV2Group | Group
if_match = 'if_match_example' # str | If-Match for ETag version checking (optional)

try:
    # Update Group with specified ID
    api_response = api_instance.put_scim_v2_group(group_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->put_scim_v2_group: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**|  |  |
| **body** | [**ScimV2Group**](ScimV2Group.html)| Group |  |
| **if_match** | **str**| If-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2Group**](ScimV2Group.html)

<a name="put_scim_v2_user"></a>

## [**ScimV2User**](ScimV2User.html) put_scim_v2_user(user_id, body, if_match=if_match)



Update user with specified ID



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
user_id = 'user_id_example' # str | User Id
body = PureCloudPlatformClientV2.ScimV2User() # ScimV2User | User
if_match = 'if_match_example' # str | If-Match for ETag version checking (optional)

try:
    # Update user with specified ID
    api_response = api_instance.put_scim_v2_user(user_id, body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SCIMApi->put_scim_v2_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User Id |  |
| **body** | [**ScimV2User**](ScimV2User.html)| User |  |
| **if_match** | **str**| If-Match for ETag version checking | [optional]  |
{: class="table table-striped"}

### Return type

[**ScimV2User**](ScimV2User.html)


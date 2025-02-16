# SCIMApi

## PureCloudPlatformClientV2.SCIMApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_scim_user**](#delete_scim_user) | Delete a user|
|[**delete_scim_v2_user**](#delete_scim_v2_user) | Delete a user|
|[**get_scim_group**](#get_scim_group) | Get a group|
|[**get_scim_groups**](#get_scim_groups) | Get a list of groups|
|[**get_scim_resourcetype**](#get_scim_resourcetype) | Get a resource type|
|[**get_scim_resourcetypes**](#get_scim_resourcetypes) | Get a list of resource types|
|[**get_scim_schema**](#get_scim_schema) | Get a SCIM schema|
|[**get_scim_schemas**](#get_scim_schemas) | Get a list of SCIM schemas|
|[**get_scim_serviceproviderconfig**](#get_scim_serviceproviderconfig) | Get a service provider&#39;s configuration|
|[**get_scim_user**](#get_scim_user) | Get a user|
|[**get_scim_users**](#get_scim_users) | Get a list of users|
|[**get_scim_v2_group**](#get_scim_v2_group) | Get a group|
|[**get_scim_v2_groups**](#get_scim_v2_groups) | Get a list of groups|
|[**get_scim_v2_resourcetype**](#get_scim_v2_resourcetype) | Get a resource type|
|[**get_scim_v2_resourcetypes**](#get_scim_v2_resourcetypes) | Get a list of resource types|
|[**get_scim_v2_schema**](#get_scim_v2_schema) | Get a SCIM schema|
|[**get_scim_v2_schemas**](#get_scim_v2_schemas) | Get a list of SCIM schemas|
|[**get_scim_v2_serviceproviderconfig**](#get_scim_v2_serviceproviderconfig) | Get a service provider&#39;s configuration|
|[**get_scim_v2_user**](#get_scim_v2_user) | Get a user|
|[**get_scim_v2_users**](#get_scim_v2_users) | Get a list of users|
|[**patch_scim_group**](#patch_scim_group) | Modify a group|
|[**patch_scim_user**](#patch_scim_user) | Modify a user|
|[**patch_scim_v2_group**](#patch_scim_v2_group) | Modify a group|
|[**patch_scim_v2_user**](#patch_scim_v2_user) | Modify a user|
|[**post_scim_users**](#post_scim_users) | Create a user|
|[**post_scim_v2_users**](#post_scim_v2_users) | Create a user|
|[**put_scim_group**](#put_scim_group) | Replace a group|
|[**put_scim_user**](#put_scim_user) | Replace a user|
|[**put_scim_v2_group**](#put_scim_v2_group) | Replace a group|
|[**put_scim_v2_user**](#put_scim_v2_user) | Replace a user|



## delete_scim_user

> object** delete_scim_user(user_id, if_match=if_match)


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
    print("Exception when calling SCIMApi->delete_scim_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/users. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |

### Return type

**object**


## delete_scim_v2_user

> object** delete_scim_v2_user(user_id, if_match=if_match)


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
    print("Exception when calling SCIMApi->delete_scim_v2_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/v2/users. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |

### Return type

**object**


## get_scim_group

> [**ScimV2Group**](ScimV2Group) get_scim_group(group_id, attributes=attributes, excluded_attributes=excluded_attributes, if_none_match=if_none_match)


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
attributes = ['attributes_example'] # list[str] | Indicates which attributes to include. Returns these attributes and the \"id\", \"active\", and \"meta\" attributes. Use \"attributes\" to avoid expensive secondary calls for the default attributes. (optional)
excluded_attributes = ['excluded_attributes_example'] # list[str] | Indicates which attributes to exclude. Returns the default attributes minus \"excludedAttributes\". Always returns \"id\", \"active\", and \"meta\" attributes. Use \"excludedAttributes\" to avoid expensive secondary calls for the default attributes. (optional)
if_none_match = 'if_none_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/groups/{groupId}. Example: \"42\". If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified. (optional)

try:
    # Get a group
    api_response = api_instance.get_scim_group(group_id, attributes=attributes, excluded_attributes=excluded_attributes, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| The ID of a group. Returned with GET /api/v2/scim/groups. |  |
| **attributes** | [**list[str]**](str)| Indicates which attributes to include. Returns these attributes and the \&quot;id\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;attributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, displayName, members, externalId, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:id, urn:ietf:params:scim:schemas:core:2.0:Group:meta, urn:ietf:params:scim:schemas:core:2.0:Group:meta.version, urn:ietf:params:scim:schemas:core:2.0:Group:meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:displayName, urn:ietf:params:scim:schemas:core:2.0:Group:members, urn:ietf:params:scim:schemas:core:2.0:Group:externalId |
| **excluded_attributes** | [**list[str]**](str)| Indicates which attributes to exclude. Returns the default attributes minus \&quot;excludedAttributes\&quot;. Always returns \&quot;id\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;excludedAttributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, displayName, members, externalId, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:id, urn:ietf:params:scim:schemas:core:2.0:Group:meta, urn:ietf:params:scim:schemas:core:2.0:Group:meta.version, urn:ietf:params:scim:schemas:core:2.0:Group:meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:displayName, urn:ietf:params:scim:schemas:core:2.0:Group:members, urn:ietf:params:scim:schemas:core:2.0:Group:externalId |
| **if_none_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/groups/{groupId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified. | [optional]  |

### Return type

[**ScimV2Group**](ScimV2Group)


## get_scim_groups

> [**ScimGroupListResponse**](ScimGroupListResponse) get_scim_groups(start_index=start_index, count=count, attributes=attributes, excluded_attributes=excluded_attributes, filter=filter)


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
count = 25 # int | The requested number of items per page. A value of 0 returns \"totalResults\". A page size over 25 may exceed internal resource limits and return a 429 error. For a page size over 25, use the \"excludedAttributes\" or \"attributes\" query parameters to exclude or only include secondary lookup values such as \"externalId\",  \"roles\", \"urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages\", or \"urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills\". (optional) (default to 25)
attributes = ['attributes_example'] # list[str] | Indicates which attributes to include. Returns these attributes and the \"id\", \"active\", and \"meta\" attributes. Use \"attributes\" to avoid expensive secondary calls for the default attributes. (optional)
excluded_attributes = ['excluded_attributes_example'] # list[str] | Indicates which attributes to exclude. Returns the default attributes minus \"excludedAttributes\". Always returns \"id\", \"active\", and \"meta\" attributes. Use \"excludedAttributes\" to avoid expensive secondary calls for the default attributes. (optional)
filter = 'displayName eq groupName' # str | Filters results. If nothing is specified, returns all groups. Examples of valid values: \"id eq 5f4bc742-a019-4e38-8e2a-d39d5bc0b0f3\", \"displayname eq Sales\". (optional)

try:
    # Get a list of groups
    api_response = api_instance.get_scim_groups(start_index=start_index, count=count, attributes=attributes, excluded_attributes=excluded_attributes, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_groups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **start_index** | **int**| The 1-based index of the first query result. | [optional] [default to 1] |
| **count** | **int**| The requested number of items per page. A value of 0 returns \&quot;totalResults\&quot;. A page size over 25 may exceed internal resource limits and return a 429 error. For a page size over 25, use the \&quot;excludedAttributes\&quot; or \&quot;attributes\&quot; query parameters to exclude or only include secondary lookup values such as \&quot;externalId\&quot;,  \&quot;roles\&quot;, \&quot;urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages\&quot;, or \&quot;urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills\&quot;. | [optional] [default to 25] |
| **attributes** | [**list[str]**](str)| Indicates which attributes to include. Returns these attributes and the \&quot;id\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;attributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, displayName, members, externalId, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:id, urn:ietf:params:scim:schemas:core:2.0:Group:meta, urn:ietf:params:scim:schemas:core:2.0:Group:meta.version, urn:ietf:params:scim:schemas:core:2.0:Group:meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:displayName, urn:ietf:params:scim:schemas:core:2.0:Group:members, urn:ietf:params:scim:schemas:core:2.0:Group:externalId |
| **excluded_attributes** | [**list[str]**](str)| Indicates which attributes to exclude. Returns the default attributes minus \&quot;excludedAttributes\&quot;. Always returns \&quot;id\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;excludedAttributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, displayName, members, externalId, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:id, urn:ietf:params:scim:schemas:core:2.0:Group:meta, urn:ietf:params:scim:schemas:core:2.0:Group:meta.version, urn:ietf:params:scim:schemas:core:2.0:Group:meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:displayName, urn:ietf:params:scim:schemas:core:2.0:Group:members, urn:ietf:params:scim:schemas:core:2.0:Group:externalId |
| **filter** | **str**| Filters results. If nothing is specified, returns all groups. Examples of valid values: \&quot;id eq 5f4bc742-a019-4e38-8e2a-d39d5bc0b0f3\&quot;, \&quot;displayname eq Sales\&quot;. | [optional]  |

### Return type

[**ScimGroupListResponse**](ScimGroupListResponse)


## get_scim_resourcetype

> [**ScimConfigResourceType**](ScimConfigResourceType) get_scim_resourcetype(resource_type)


Get a resource type

Wraps GET /api/v2/scim/resourcetypes/{resourceType} 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
resource_type = 'resource_type_example' # str | The type of resource. Returned with GET /api/v2/scim/resourcetypes.

try:
    # Get a resource type
    api_response = api_instance.get_scim_resourcetype(resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_resourcetype: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **resource_type** | **str**| The type of resource. Returned with GET /api/v2/scim/resourcetypes. | <br />**Values**: User, Group, ServiceProviderConfig, ResourceType, Schema |

### Return type

[**ScimConfigResourceType**](ScimConfigResourceType)


## get_scim_resourcetypes

> [**ScimConfigResourceTypesListResponse**](ScimConfigResourceTypesListResponse) get_scim_resourcetypes()


Get a list of resource types

Wraps GET /api/v2/scim/resourcetypes 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()

try:
    # Get a list of resource types
    api_response = api_instance.get_scim_resourcetypes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_resourcetypes: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**ScimConfigResourceTypesListResponse**](ScimConfigResourceTypesListResponse)


## get_scim_schema

> [**ScimV2SchemaDefinition**](ScimV2SchemaDefinition) get_scim_schema(schema_id)


Get a SCIM schema

Wraps GET /api/v2/scim/schemas/{schemaId} 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
schema_id = 'schema_id_example' # str | The ID of a schema. Returned with GET /api/v2/scim/schemas.

try:
    # Get a SCIM schema
    api_response = api_instance.get_scim_schema(schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| The ID of a schema. Returned with GET /api/v2/scim/schemas. | <br />**Values**: urn:ietf:params:scim:schemas:core:2.0:User, urn:ietf:params:scim:schemas:core:2.0:Group, urn:ietf:params:scim:schemas:core:2.0:ServiceProviderConfig, urn:ietf:params:scim:schemas:core:2.0:ResourceType, urn:ietf:params:scim:schemas:core:2.0:Schema, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User |

### Return type

[**ScimV2SchemaDefinition**](ScimV2SchemaDefinition)


## get_scim_schemas

> [**ScimV2SchemaListResponse**](ScimV2SchemaListResponse) get_scim_schemas(filter=filter)


Get a list of SCIM schemas

Wraps GET /api/v2/scim/schemas 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
filter = 'displayName eq groupName' # str | Filtered results are invalid and return 403 Unauthorized. (optional)

try:
    # Get a list of SCIM schemas
    api_response = api_instance.get_scim_schemas(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_schemas: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter** | **str**| Filtered results are invalid and return 403 Unauthorized. | [optional]  |

### Return type

[**ScimV2SchemaListResponse**](ScimV2SchemaListResponse)


## get_scim_serviceproviderconfig

> [**ScimServiceProviderConfig**](ScimServiceProviderConfig) get_scim_serviceproviderconfig(if_none_match=if_none_match)


Get a service provider's configuration

Wraps GET /api/v2/scim/serviceproviderconfig 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
if_none_match = 'if_none_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/serviceproviderconfig. Example: \"42\". If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified.  (optional)

try:
    # Get a service provider's configuration
    api_response = api_instance.get_scim_serviceproviderconfig(if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_serviceproviderconfig: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **if_none_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/serviceproviderconfig. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified.  | [optional]  |

### Return type

[**ScimServiceProviderConfig**](ScimServiceProviderConfig)


## get_scim_user

> [**ScimV2User**](ScimV2User) get_scim_user(user_id, attributes=attributes, excluded_attributes=excluded_attributes, if_none_match=if_none_match)


Get a user

Wraps GET /api/v2/scim/users/{userId} 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
user_id = 'user_id_example' # str | The ID of a user. Returned with GET /api/v2/scim/users.
attributes = ['attributes_example'] # list[str] | Indicates which attributes to include. Returns these attributes and the \"id\", \"userName\", \"active\", and \"meta\" attributes. Use \"attributes\" to avoid expensive secondary calls for the default attributes. (optional)
excluded_attributes = ['excluded_attributes_example'] # list[str] | Indicates which attributes to exclude. Returns the default attributes minus \"excludedAttributes\". Always returns the \"id\", \"userName\", \"active\", and \"meta\" attributes. Use \"excludedAttributes\" to avoid expensive secondary calls for the default attributes. (optional)
if_none_match = 'if_none_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/users/{userId}. Example: \"42\". If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified. (optional)

try:
    # Get a user
    api_response = api_instance.get_scim_user(user_id, attributes=attributes, excluded_attributes=excluded_attributes, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/users. |  |
| **attributes** | [**list[str]**](str)| Indicates which attributes to include. Returns these attributes and the \&quot;id\&quot;, \&quot;userName\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;attributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, userName, displayName, title, active, externalId, phoneNumbers, emails, groups, roles, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:User:id, urn:ietf:params:scim:schemas:core:2.0:User:userName, urn:ietf:params:scim:schemas:core:2.0:User:displayName, urn:ietf:params:scim:schemas:core:2.0:User:title, urn:ietf:params:scim:schemas:core:2.0:User:active, urn:ietf:params:scim:schemas:core:2.0:User:externalId, urn:ietf:params:scim:schemas:core:2.0:User:phoneNumbers, urn:ietf:params:scim:schemas:core:2.0:User:emails, urn:ietf:params:scim:schemas:core:2.0:User:groups, urn:ietf:params:scim:schemas:core:2.0:User:roles, urn:ietf:params:scim:schemas:core:2.0:User:meta, urn:ietf:params:scim:schemas:core:2.0:User:meta.version, urn:ietf:params:scim:schemas:core:2.0:User:meta.lastModified, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:division, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:department, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager.value, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:employeeNumber, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:dateHire, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:externalIds |
| **excluded_attributes** | [**list[str]**](str)| Indicates which attributes to exclude. Returns the default attributes minus \&quot;excludedAttributes\&quot;. Always returns the \&quot;id\&quot;, \&quot;userName\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;excludedAttributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, userName, displayName, title, active, externalId, phoneNumbers, emails, groups, roles, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:User:id, urn:ietf:params:scim:schemas:core:2.0:User:userName, urn:ietf:params:scim:schemas:core:2.0:User:displayName, urn:ietf:params:scim:schemas:core:2.0:User:title, urn:ietf:params:scim:schemas:core:2.0:User:active, urn:ietf:params:scim:schemas:core:2.0:User:externalId, urn:ietf:params:scim:schemas:core:2.0:User:phoneNumbers, urn:ietf:params:scim:schemas:core:2.0:User:emails, urn:ietf:params:scim:schemas:core:2.0:User:groups, urn:ietf:params:scim:schemas:core:2.0:User:roles, urn:ietf:params:scim:schemas:core:2.0:User:meta, urn:ietf:params:scim:schemas:core:2.0:User:meta.version, urn:ietf:params:scim:schemas:core:2.0:User:meta.lastModified, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:division, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:department, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager.value, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:employeeNumber, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:dateHire, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:externalIds |
| **if_none_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified. | [optional]  |

### Return type

[**ScimV2User**](ScimV2User)


## get_scim_users

> [**ScimUserListResponse**](ScimUserListResponse) get_scim_users(start_index=start_index, count=count, attributes=attributes, excluded_attributes=excluded_attributes, filter=filter)


Get a list of users

To return all active users, do not use the filter parameter. To return inactive users, set the filter parameter to \"active eq false\". By default, returns SCIM attributes \"externalId\", \"enterprise-user:manager\", and \"roles\". To exclude these attributes, set the attributes parameter to \"id,active\" or the excludeAttributes parameter to \"externalId,roles,urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:division\".

Wraps GET /api/v2/scim/users 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
start_index = 1 # int | The 1-based index of the first query result. (optional) (default to 1)
count = 25 # int | The requested number of items per page. A value of 0 returns \"totalResults\". A page size over 25 may exceed internal resource limits and return a 429 error. For a page size over 25, use the \"excludedAttributes\" or \"attributes\" query parameters to exclude or only include secondary lookup values such as \"externalId\",  \"roles\", \"urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages\", or \"urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills\". (optional) (default to 25)
attributes = ['attributes_example'] # list[str] | Indicates which attributes to include. Returns these attributes and the \"id\", \"userName\", \"active\", and \"meta\" attributes. Use \"attributes\" to avoid expensive secondary calls for the default attributes. (optional)
excluded_attributes = ['excluded_attributes_example'] # list[str] | Indicates which attributes to exclude. Returns the default attributes minus \"excludedAttributes\". Always returns the \"id\", \"userName\", \"active\", and \"meta\" attributes. Use \"excludedAttributes\" to avoid expensive secondary calls for the default attributes. (optional)
filter = 'filter_example' # str | Filters results. If nothing is specified, returns all active users. Examples of valid values: \"id eq 857449b0-d9e7-4cd0-acbf-a6adfb9ef1e9\", \"userName eq search@sample.org\", \"manager eq 16e10e2f-1136-43fe-bb84-eac073168a49\", \"email eq search@sample.org\", \"division eq divisionName\", \"externalId eq 167844\", \"active eq false\", \"employeeNumber eq 9876543210\". (optional)

try:
    # Get a list of users
    api_response = api_instance.get_scim_users(start_index=start_index, count=count, attributes=attributes, excluded_attributes=excluded_attributes, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **start_index** | **int**| The 1-based index of the first query result. | [optional] [default to 1] |
| **count** | **int**| The requested number of items per page. A value of 0 returns \&quot;totalResults\&quot;. A page size over 25 may exceed internal resource limits and return a 429 error. For a page size over 25, use the \&quot;excludedAttributes\&quot; or \&quot;attributes\&quot; query parameters to exclude or only include secondary lookup values such as \&quot;externalId\&quot;,  \&quot;roles\&quot;, \&quot;urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages\&quot;, or \&quot;urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills\&quot;. | [optional] [default to 25] |
| **attributes** | [**list[str]**](str)| Indicates which attributes to include. Returns these attributes and the \&quot;id\&quot;, \&quot;userName\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;attributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, userName, displayName, title, active, externalId, phoneNumbers, emails, groups, roles, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:User:id, urn:ietf:params:scim:schemas:core:2.0:User:userName, urn:ietf:params:scim:schemas:core:2.0:User:displayName, urn:ietf:params:scim:schemas:core:2.0:User:title, urn:ietf:params:scim:schemas:core:2.0:User:active, urn:ietf:params:scim:schemas:core:2.0:User:externalId, urn:ietf:params:scim:schemas:core:2.0:User:phoneNumbers, urn:ietf:params:scim:schemas:core:2.0:User:emails, urn:ietf:params:scim:schemas:core:2.0:User:groups, urn:ietf:params:scim:schemas:core:2.0:User:roles, urn:ietf:params:scim:schemas:core:2.0:User:meta, urn:ietf:params:scim:schemas:core:2.0:User:meta.version, urn:ietf:params:scim:schemas:core:2.0:User:meta.lastModified, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:division, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:department, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager.value, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:employeeNumber, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:dateHire, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:externalIds |
| **excluded_attributes** | [**list[str]**](str)| Indicates which attributes to exclude. Returns the default attributes minus \&quot;excludedAttributes\&quot;. Always returns the \&quot;id\&quot;, \&quot;userName\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;excludedAttributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, userName, displayName, title, active, externalId, phoneNumbers, emails, groups, roles, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:User:id, urn:ietf:params:scim:schemas:core:2.0:User:userName, urn:ietf:params:scim:schemas:core:2.0:User:displayName, urn:ietf:params:scim:schemas:core:2.0:User:title, urn:ietf:params:scim:schemas:core:2.0:User:active, urn:ietf:params:scim:schemas:core:2.0:User:externalId, urn:ietf:params:scim:schemas:core:2.0:User:phoneNumbers, urn:ietf:params:scim:schemas:core:2.0:User:emails, urn:ietf:params:scim:schemas:core:2.0:User:groups, urn:ietf:params:scim:schemas:core:2.0:User:roles, urn:ietf:params:scim:schemas:core:2.0:User:meta, urn:ietf:params:scim:schemas:core:2.0:User:meta.version, urn:ietf:params:scim:schemas:core:2.0:User:meta.lastModified, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:division, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:department, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager.value, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:employeeNumber, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:dateHire, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:externalIds |
| **filter** | **str**| Filters results. If nothing is specified, returns all active users. Examples of valid values: \&quot;id eq 857449b0-d9e7-4cd0-acbf-a6adfb9ef1e9\&quot;, \&quot;userName eq search@sample.org\&quot;, \&quot;manager eq 16e10e2f-1136-43fe-bb84-eac073168a49\&quot;, \&quot;email eq search@sample.org\&quot;, \&quot;division eq divisionName\&quot;, \&quot;externalId eq 167844\&quot;, \&quot;active eq false\&quot;, \&quot;employeeNumber eq 9876543210\&quot;. | [optional]  |

### Return type

[**ScimUserListResponse**](ScimUserListResponse)


## get_scim_v2_group

> [**ScimV2Group**](ScimV2Group) get_scim_v2_group(group_id, attributes=attributes, excluded_attributes=excluded_attributes, if_none_match=if_none_match)


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
attributes = ['attributes_example'] # list[str] | Indicates which attributes to include. Returns these attributes and the \"id\", \"active\", and \"meta\" attributes. Use \"attributes\" to avoid expensive secondary calls for the default attributes. (optional)
excluded_attributes = ['excluded_attributes_example'] # list[str] | Indicates which attributes to exclude. Returns the default attributes minus \"excludedAttributes\". Always returns \"id\", \"active\", and \"meta\" attributes. Use \"excludedAttributes\" to avoid expensive secondary calls for the default attributes. (optional)
if_none_match = 'if_none_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/groups/{groupId}. Example: \"42\". If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified. (optional)

try:
    # Get a group
    api_response = api_instance.get_scim_v2_group(group_id, attributes=attributes, excluded_attributes=excluded_attributes, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_v2_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| The ID of a group. Returned with GET /api/v2/scim/v2/groups. |  |
| **attributes** | [**list[str]**](str)| Indicates which attributes to include. Returns these attributes and the \&quot;id\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;attributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, displayName, members, externalId, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:id, urn:ietf:params:scim:schemas:core:2.0:Group:meta, urn:ietf:params:scim:schemas:core:2.0:Group:meta.version, urn:ietf:params:scim:schemas:core:2.0:Group:meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:displayName, urn:ietf:params:scim:schemas:core:2.0:Group:members, urn:ietf:params:scim:schemas:core:2.0:Group:externalId |
| **excluded_attributes** | [**list[str]**](str)| Indicates which attributes to exclude. Returns the default attributes minus \&quot;excludedAttributes\&quot;. Always returns \&quot;id\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;excludedAttributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, displayName, members, externalId, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:id, urn:ietf:params:scim:schemas:core:2.0:Group:meta, urn:ietf:params:scim:schemas:core:2.0:Group:meta.version, urn:ietf:params:scim:schemas:core:2.0:Group:meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:displayName, urn:ietf:params:scim:schemas:core:2.0:Group:members, urn:ietf:params:scim:schemas:core:2.0:Group:externalId |
| **if_none_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/groups/{groupId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified. | [optional]  |

### Return type

[**ScimV2Group**](ScimV2Group)


## get_scim_v2_groups

> [**ScimGroupListResponse**](ScimGroupListResponse) get_scim_v2_groups(filter, start_index=start_index, count=count, attributes=attributes, excluded_attributes=excluded_attributes)


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
filter = 'displayName eq groupName' # str | Filters results. If nothing is specified, returns all groups. Examples of valid values: \"id eq 5f4bc742-a019-4e38-8e2a-d39d5bc0b0f3\", \"displayname eq Sales\".
start_index = 1 # int | The 1-based index of the first query result. (optional) (default to 1)
count = 25 # int | The requested number of items per page. A value of 0 returns \"totalResults\". A page size over 25 may exceed internal resource limits and return a 429 error. For a page size over 25, use the \"excludedAttributes\" or \"attributes\" query parameters to exclude or only include secondary lookup values such as \"externalId\",  \"roles\", \"urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages\", or \"urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills\". (optional) (default to 25)
attributes = ['attributes_example'] # list[str] | Indicates which attributes to include. Returns these attributes and the \"id\", \"active\", and \"meta\" attributes. Use \"attributes\" to avoid expensive secondary calls for the default attributes. (optional)
excluded_attributes = ['excluded_attributes_example'] # list[str] | Indicates which attributes to exclude. Returns the default attributes minus \"excludedAttributes\". Always returns \"id\", \"active\", and \"meta\" attributes. Use \"excludedAttributes\" to avoid expensive secondary calls for the default attributes. (optional)

try:
    # Get a list of groups
    api_response = api_instance.get_scim_v2_groups(filter, start_index=start_index, count=count, attributes=attributes, excluded_attributes=excluded_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_v2_groups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter** | **str**| Filters results. If nothing is specified, returns all groups. Examples of valid values: \&quot;id eq 5f4bc742-a019-4e38-8e2a-d39d5bc0b0f3\&quot;, \&quot;displayname eq Sales\&quot;. |  |
| **start_index** | **int**| The 1-based index of the first query result. | [optional] [default to 1] |
| **count** | **int**| The requested number of items per page. A value of 0 returns \&quot;totalResults\&quot;. A page size over 25 may exceed internal resource limits and return a 429 error. For a page size over 25, use the \&quot;excludedAttributes\&quot; or \&quot;attributes\&quot; query parameters to exclude or only include secondary lookup values such as \&quot;externalId\&quot;,  \&quot;roles\&quot;, \&quot;urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages\&quot;, or \&quot;urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills\&quot;. | [optional] [default to 25] |
| **attributes** | [**list[str]**](str)| Indicates which attributes to include. Returns these attributes and the \&quot;id\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;attributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, displayName, members, externalId, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:id, urn:ietf:params:scim:schemas:core:2.0:Group:meta, urn:ietf:params:scim:schemas:core:2.0:Group:meta.version, urn:ietf:params:scim:schemas:core:2.0:Group:meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:displayName, urn:ietf:params:scim:schemas:core:2.0:Group:members, urn:ietf:params:scim:schemas:core:2.0:Group:externalId |
| **excluded_attributes** | [**list[str]**](str)| Indicates which attributes to exclude. Returns the default attributes minus \&quot;excludedAttributes\&quot;. Always returns \&quot;id\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;excludedAttributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, displayName, members, externalId, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:id, urn:ietf:params:scim:schemas:core:2.0:Group:meta, urn:ietf:params:scim:schemas:core:2.0:Group:meta.version, urn:ietf:params:scim:schemas:core:2.0:Group:meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:Group:displayName, urn:ietf:params:scim:schemas:core:2.0:Group:members, urn:ietf:params:scim:schemas:core:2.0:Group:externalId |

### Return type

[**ScimGroupListResponse**](ScimGroupListResponse)


## get_scim_v2_resourcetype

> [**ScimConfigResourceType**](ScimConfigResourceType) get_scim_v2_resourcetype(resource_type)


Get a resource type

Wraps GET /api/v2/scim/v2/resourcetypes/{resourceType} 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
resource_type = 'resource_type_example' # str | The type of resource. Returned with GET /api/v2/scim/v2/resourcetypes.

try:
    # Get a resource type
    api_response = api_instance.get_scim_v2_resourcetype(resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_v2_resourcetype: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **resource_type** | **str**| The type of resource. Returned with GET /api/v2/scim/v2/resourcetypes. | <br />**Values**: User, Group, ServiceProviderConfig, ResourceType, Schema |

### Return type

[**ScimConfigResourceType**](ScimConfigResourceType)


## get_scim_v2_resourcetypes

> [**ScimConfigResourceTypesListResponse**](ScimConfigResourceTypesListResponse) get_scim_v2_resourcetypes()


Get a list of resource types

Wraps GET /api/v2/scim/v2/resourcetypes 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()

try:
    # Get a list of resource types
    api_response = api_instance.get_scim_v2_resourcetypes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_v2_resourcetypes: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**ScimConfigResourceTypesListResponse**](ScimConfigResourceTypesListResponse)


## get_scim_v2_schema

> [**ScimV2SchemaDefinition**](ScimV2SchemaDefinition) get_scim_v2_schema(schema_id)


Get a SCIM schema

Wraps GET /api/v2/scim/v2/schemas/{schemaId} 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
schema_id = 'schema_id_example' # str | The ID of a schema. Returned with GET /api/v2/scim/v2/schemas.

try:
    # Get a SCIM schema
    api_response = api_instance.get_scim_v2_schema(schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_v2_schema: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **schema_id** | **str**| The ID of a schema. Returned with GET /api/v2/scim/v2/schemas. | <br />**Values**: urn:ietf:params:scim:schemas:core:2.0:User, urn:ietf:params:scim:schemas:core:2.0:Group, urn:ietf:params:scim:schemas:core:2.0:ServiceProviderConfig, urn:ietf:params:scim:schemas:core:2.0:ResourceType, urn:ietf:params:scim:schemas:core:2.0:Schema, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User |

### Return type

[**ScimV2SchemaDefinition**](ScimV2SchemaDefinition)


## get_scim_v2_schemas

> [**ScimV2SchemaListResponse**](ScimV2SchemaListResponse) get_scim_v2_schemas(filter=filter)


Get a list of SCIM schemas

Wraps GET /api/v2/scim/v2/schemas 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
filter = 'displayName eq groupName' # str | Filtered results are invalid and return 403 Unauthorized. (optional)

try:
    # Get a list of SCIM schemas
    api_response = api_instance.get_scim_v2_schemas(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_v2_schemas: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **filter** | **str**| Filtered results are invalid and return 403 Unauthorized. | [optional]  |

### Return type

[**ScimV2SchemaListResponse**](ScimV2SchemaListResponse)


## get_scim_v2_serviceproviderconfig

> [**ScimServiceProviderConfig**](ScimServiceProviderConfig) get_scim_v2_serviceproviderconfig(if_none_match=if_none_match)


Get a service provider's configuration

Wraps GET /api/v2/scim/v2/serviceproviderconfig 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
if_none_match = 'if_none_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/serviceproviderconfig. Example: \"42\". If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified.  (optional)

try:
    # Get a service provider's configuration
    api_response = api_instance.get_scim_v2_serviceproviderconfig(if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_v2_serviceproviderconfig: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **if_none_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/serviceproviderconfig. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified.  | [optional]  |

### Return type

[**ScimServiceProviderConfig**](ScimServiceProviderConfig)


## get_scim_v2_user

> [**ScimV2User**](ScimV2User) get_scim_v2_user(user_id, attributes=attributes, excluded_attributes=excluded_attributes, if_none_match=if_none_match)


Get a user

Wraps GET /api/v2/scim/v2/users/{userId} 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
user_id = 'user_id_example' # str | The ID of a user. Returned with GET /api/v2/scim/v2/users.
attributes = ['attributes_example'] # list[str] | Indicates which attributes to include. Returns these attributes and the \"id\", \"userName\", \"active\", and \"meta\" attributes. Use \"attributes\" to avoid expensive secondary calls for the default attributes. (optional)
excluded_attributes = ['excluded_attributes_example'] # list[str] | Indicates which attributes to exclude. Returns the default attributes minus \"excludedAttributes\". Always returns the \"id\", \"userName\", \"active\", and \"meta\" attributes. Use \"excludedAttributes\" to avoid expensive secondary calls for the default attributes. (optional)
if_none_match = 'if_none_match_example' # str | The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/users/{userId}. Example: \"42\". If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified. (optional)

try:
    # Get a user
    api_response = api_instance.get_scim_v2_user(user_id, attributes=attributes, excluded_attributes=excluded_attributes, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_v2_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/v2/users. |  |
| **attributes** | [**list[str]**](str)| Indicates which attributes to include. Returns these attributes and the \&quot;id\&quot;, \&quot;userName\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;attributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, userName, displayName, title, active, externalId, phoneNumbers, emails, groups, roles, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:User:id, urn:ietf:params:scim:schemas:core:2.0:User:userName, urn:ietf:params:scim:schemas:core:2.0:User:displayName, urn:ietf:params:scim:schemas:core:2.0:User:title, urn:ietf:params:scim:schemas:core:2.0:User:active, urn:ietf:params:scim:schemas:core:2.0:User:externalId, urn:ietf:params:scim:schemas:core:2.0:User:phoneNumbers, urn:ietf:params:scim:schemas:core:2.0:User:emails, urn:ietf:params:scim:schemas:core:2.0:User:groups, urn:ietf:params:scim:schemas:core:2.0:User:roles, urn:ietf:params:scim:schemas:core:2.0:User:meta, urn:ietf:params:scim:schemas:core:2.0:User:meta.version, urn:ietf:params:scim:schemas:core:2.0:User:meta.lastModified, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:division, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:department, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager.value, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:employeeNumber, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:dateHire, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:externalIds |
| **excluded_attributes** | [**list[str]**](str)| Indicates which attributes to exclude. Returns the default attributes minus \&quot;excludedAttributes\&quot;. Always returns the \&quot;id\&quot;, \&quot;userName\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;excludedAttributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, userName, displayName, title, active, externalId, phoneNumbers, emails, groups, roles, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:User:id, urn:ietf:params:scim:schemas:core:2.0:User:userName, urn:ietf:params:scim:schemas:core:2.0:User:displayName, urn:ietf:params:scim:schemas:core:2.0:User:title, urn:ietf:params:scim:schemas:core:2.0:User:active, urn:ietf:params:scim:schemas:core:2.0:User:externalId, urn:ietf:params:scim:schemas:core:2.0:User:phoneNumbers, urn:ietf:params:scim:schemas:core:2.0:User:emails, urn:ietf:params:scim:schemas:core:2.0:User:groups, urn:ietf:params:scim:schemas:core:2.0:User:roles, urn:ietf:params:scim:schemas:core:2.0:User:meta, urn:ietf:params:scim:schemas:core:2.0:User:meta.version, urn:ietf:params:scim:schemas:core:2.0:User:meta.lastModified, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:division, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:department, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager.value, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:employeeNumber, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:dateHire, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:externalIds |
| **if_none_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns the current configuration of the resource. If the ETag is current, returns 304 Not Modified. | [optional]  |

### Return type

[**ScimV2User**](ScimV2User)


## get_scim_v2_users

> [**ScimUserListResponse**](ScimUserListResponse) get_scim_v2_users(start_index=start_index, count=count, attributes=attributes, excluded_attributes=excluded_attributes, filter=filter)


Get a list of users

To return all active users, do not use the filter parameter. To return inactive users, set the filter parameter to \"active eq false\". By default, returns SCIM attributes \"externalId\", \"enterprise-user:manager\", and \"roles\". To exclude these attributes, set the attributes parameter to \"id,active\" or the excludeAttributes parameter to \"externalId,roles,urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:division\".

Wraps GET /api/v2/scim/v2/users 

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
api_instance = PureCloudPlatformClientV2.SCIMApi()
start_index = 1 # int | The 1-based index of the first query result. (optional) (default to 1)
count = 25 # int | The requested number of items per page. A value of 0 returns \"totalResults\". A page size over 25 may exceed internal resource limits and return a 429 error. For a page size over 25, use the \"excludedAttributes\" or \"attributes\" query parameters to exclude or only include secondary lookup values such as \"externalId\",  \"roles\", \"urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages\", or \"urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills\". (optional) (default to 25)
attributes = ['attributes_example'] # list[str] | Indicates which attributes to include. Returns these attributes and the \"id\", \"userName\", \"active\", and \"meta\" attributes. Use \"attributes\" to avoid expensive secondary calls for the default attributes. (optional)
excluded_attributes = ['excluded_attributes_example'] # list[str] | Indicates which attributes to exclude. Returns the default attributes minus \"excludedAttributes\". Always returns the \"id\", \"userName\", \"active\", and \"meta\" attributes. Use \"excludedAttributes\" to avoid expensive secondary calls for the default attributes. (optional)
filter = 'filter_example' # str | Filters results. If nothing is specified, returns all active users. Examples of valid values: \"id eq 857449b0-d9e7-4cd0-acbf-a6adfb9ef1e9\", \"userName eq search@sample.org\", \"manager eq 16e10e2f-1136-43fe-bb84-eac073168a49\", \"email eq search@sample.org\", \"division eq divisionName\", \"externalId eq 167844\", \"active eq false\", \"employeeNumber eq 9876543210\". (optional)

try:
    # Get a list of users
    api_response = api_instance.get_scim_v2_users(start_index=start_index, count=count, attributes=attributes, excluded_attributes=excluded_attributes, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_v2_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **start_index** | **int**| The 1-based index of the first query result. | [optional] [default to 1] |
| **count** | **int**| The requested number of items per page. A value of 0 returns \&quot;totalResults\&quot;. A page size over 25 may exceed internal resource limits and return a 429 error. For a page size over 25, use the \&quot;excludedAttributes\&quot; or \&quot;attributes\&quot; query parameters to exclude or only include secondary lookup values such as \&quot;externalId\&quot;,  \&quot;roles\&quot;, \&quot;urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages\&quot;, or \&quot;urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills\&quot;. | [optional] [default to 25] |
| **attributes** | [**list[str]**](str)| Indicates which attributes to include. Returns these attributes and the \&quot;id\&quot;, \&quot;userName\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;attributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, userName, displayName, title, active, externalId, phoneNumbers, emails, groups, roles, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:User:id, urn:ietf:params:scim:schemas:core:2.0:User:userName, urn:ietf:params:scim:schemas:core:2.0:User:displayName, urn:ietf:params:scim:schemas:core:2.0:User:title, urn:ietf:params:scim:schemas:core:2.0:User:active, urn:ietf:params:scim:schemas:core:2.0:User:externalId, urn:ietf:params:scim:schemas:core:2.0:User:phoneNumbers, urn:ietf:params:scim:schemas:core:2.0:User:emails, urn:ietf:params:scim:schemas:core:2.0:User:groups, urn:ietf:params:scim:schemas:core:2.0:User:roles, urn:ietf:params:scim:schemas:core:2.0:User:meta, urn:ietf:params:scim:schemas:core:2.0:User:meta.version, urn:ietf:params:scim:schemas:core:2.0:User:meta.lastModified, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:division, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:department, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager.value, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:employeeNumber, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:dateHire, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:externalIds |
| **excluded_attributes** | [**list[str]**](str)| Indicates which attributes to exclude. Returns the default attributes minus \&quot;excludedAttributes\&quot;. Always returns the \&quot;id\&quot;, \&quot;userName\&quot;, \&quot;active\&quot;, and \&quot;meta\&quot; attributes. Use \&quot;excludedAttributes\&quot; to avoid expensive secondary calls for the default attributes. | [optional] <br />**Values**: id, userName, displayName, title, active, externalId, phoneNumbers, emails, groups, roles, meta, meta.version, meta.lastModified, urn:ietf:params:scim:schemas:core:2.0:User:id, urn:ietf:params:scim:schemas:core:2.0:User:userName, urn:ietf:params:scim:schemas:core:2.0:User:displayName, urn:ietf:params:scim:schemas:core:2.0:User:title, urn:ietf:params:scim:schemas:core:2.0:User:active, urn:ietf:params:scim:schemas:core:2.0:User:externalId, urn:ietf:params:scim:schemas:core:2.0:User:phoneNumbers, urn:ietf:params:scim:schemas:core:2.0:User:emails, urn:ietf:params:scim:schemas:core:2.0:User:groups, urn:ietf:params:scim:schemas:core:2.0:User:roles, urn:ietf:params:scim:schemas:core:2.0:User:meta, urn:ietf:params:scim:schemas:core:2.0:User:meta.version, urn:ietf:params:scim:schemas:core:2.0:User:meta.lastModified, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:division, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:department, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:manager.value, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:employeeNumber, urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:dateHire, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingSkills, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:routingLanguages, urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:externalIds |
| **filter** | **str**| Filters results. If nothing is specified, returns all active users. Examples of valid values: \&quot;id eq 857449b0-d9e7-4cd0-acbf-a6adfb9ef1e9\&quot;, \&quot;userName eq search@sample.org\&quot;, \&quot;manager eq 16e10e2f-1136-43fe-bb84-eac073168a49\&quot;, \&quot;email eq search@sample.org\&quot;, \&quot;division eq divisionName\&quot;, \&quot;externalId eq 167844\&quot;, \&quot;active eq false\&quot;, \&quot;employeeNumber eq 9876543210\&quot;. | [optional]  |

### Return type

[**ScimUserListResponse**](ScimUserListResponse)


## patch_scim_group

> [**ScimV2Group**](ScimV2Group) patch_scim_group(group_id, body, if_match=if_match)


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
    print("Exception when calling SCIMApi->patch_scim_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| The ID of a group. Returned with GET /api/v2/scim/groups. |  |
| **body** | [**ScimV2PatchRequest**](ScimV2PatchRequest)| The information used to modify a group. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/groups/{groupId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |

### Return type

[**ScimV2Group**](ScimV2Group)


## patch_scim_user

> [**ScimV2User**](ScimV2User) patch_scim_user(user_id, body, if_match=if_match)


Modify a user

Wraps PATCH /api/v2/scim/users/{userId} 

Requires ANY permissions: 

* directory:user:edit
* directory:user:setPassword
* authorization:grant:add
* authorization:grant:delete
* routing:skill:assign
* routing:language:assign
* telephony:extension:assign

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
    print("Exception when calling SCIMApi->patch_scim_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/users. |  |
| **body** | [**ScimV2PatchRequest**](ScimV2PatchRequest)| The information used to modify a user. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |

### Return type

[**ScimV2User**](ScimV2User)


## patch_scim_v2_group

> [**ScimV2Group**](ScimV2Group) patch_scim_v2_group(group_id, body, if_match=if_match)


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
    print("Exception when calling SCIMApi->patch_scim_v2_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| The ID of a group. Returned with GET /api/v2/scim/v2/groups. |  |
| **body** | [**ScimV2PatchRequest**](ScimV2PatchRequest)| The information used to modify a group. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/groups/{groupId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |

### Return type

[**ScimV2Group**](ScimV2Group)


## patch_scim_v2_user

> [**ScimV2User**](ScimV2User) patch_scim_v2_user(user_id, body, if_match=if_match)


Modify a user

Wraps PATCH /api/v2/scim/v2/users/{userId} 

Requires ANY permissions: 

* directory:user:edit
* directory:user:setPassword
* authorization:grant:add
* authorization:grant:delete
* routing:skill:assign
* routing:language:assign
* telephony:extension:assign

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
    print("Exception when calling SCIMApi->patch_scim_v2_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/v2/users. |  |
| **body** | [**ScimV2PatchRequest**](ScimV2PatchRequest)| The information used to modify a user. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |

### Return type

[**ScimV2User**](ScimV2User)


## post_scim_users

> [**ScimV2User**](ScimV2User) post_scim_users(body)


Create a user

Wraps POST /api/v2/scim/users 

Requires ANY permissions: 

* directory:user:add
* authorization:grant:add
* authorization:grant:delete
* routing:skill:assign
* routing:language:assign
* telephony:extension:assign

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
    print("Exception when calling SCIMApi->post_scim_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ScimV2CreateUser**](ScimV2CreateUser)| The information used to create a user. |  |

### Return type

[**ScimV2User**](ScimV2User)


## post_scim_v2_users

> [**ScimV2User**](ScimV2User) post_scim_v2_users(body)


Create a user

Wraps POST /api/v2/scim/v2/users 

Requires ANY permissions: 

* directory:user:add
* authorization:grant:add
* authorization:grant:delete
* routing:skill:assign
* routing:language:assign
* telephony:extension:assign

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
    print("Exception when calling SCIMApi->post_scim_v2_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ScimV2CreateUser**](ScimV2CreateUser)| The information used to create a user. |  |

### Return type

[**ScimV2User**](ScimV2User)


## put_scim_group

> [**ScimV2Group**](ScimV2Group) put_scim_group(group_id, body, if_match=if_match)


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
    print("Exception when calling SCIMApi->put_scim_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| The ID of a group. Returned with GET /api/v2/scim/groups. |  |
| **body** | [**ScimV2Group**](ScimV2Group)| The information used to replace a group. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/groups/{groupId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |

### Return type

[**ScimV2Group**](ScimV2Group)


## put_scim_user

> [**ScimV2User**](ScimV2User) put_scim_user(user_id, body, if_match=if_match)


Replace a user

Wraps PUT /api/v2/scim/users/{userId} 

Requires ANY permissions: 

* directory:user:edit
* directory:user:setPassword
* authorization:grant:add
* authorization:grant:delete
* routing:skill:assign
* routing:language:assign
* telephony:extension:assign

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
    print("Exception when calling SCIMApi->put_scim_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/users. |  |
| **body** | [**ScimV2User**](ScimV2User)| The information used to replace a user. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |

### Return type

[**ScimV2User**](ScimV2User)


## put_scim_v2_group

> [**ScimV2Group**](ScimV2Group) put_scim_v2_group(group_id, body, if_match=if_match)


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
    print("Exception when calling SCIMApi->put_scim_v2_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| The ID of a group. Returned with GET /api/v2/scim/v2/groups. |  |
| **body** | [**ScimV2Group**](ScimV2Group)| The information used to replace a group. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/groups/{groupId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |

### Return type

[**ScimV2Group**](ScimV2Group)


## put_scim_v2_user

> [**ScimV2User**](ScimV2User) put_scim_v2_user(user_id, body, if_match=if_match)


Replace a user

Wraps PUT /api/v2/scim/v2/users/{userId} 

Requires ANY permissions: 

* directory:user:edit
* directory:user:setPassword
* authorization:grant:add
* authorization:grant:delete
* routing:skill:assign
* routing:language:assign
* telephony:extension:assign

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
    print("Exception when calling SCIMApi->put_scim_v2_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The ID of a user. Returned with GET /api/v2/scim/v2/users. |  |
| **body** | [**ScimV2User**](ScimV2User)| The information used to replace a user. |  |
| **if_match** | **str**| The ETag of a resource in double quotes. Returned as header and meta.version with initial call to GET /api/v2/scim/v2/users/{userId}. Example: \&quot;42\&quot;. If the ETag is different from the version on the server, returns 400 with a \&quot;scimType\&quot; of \&quot;invalidVers\&quot;. | [optional]  |

### Return type

[**ScimV2User**](ScimV2User)


_PureCloudPlatformClientV2 222.0.0_

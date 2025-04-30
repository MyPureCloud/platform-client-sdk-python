# GroupsApi

## PureCloudPlatformClientV2.GroupsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_group**](#delete_group) | Delete group|
|[**delete_group_dynamicsettings**](#delete_group_dynamicsettings) | Remove dynamic group definition|
|[**delete_group_members**](#delete_group_members) | Remove members|
|[**get_fieldconfig**](#get_fieldconfig) | Fetch field config for an entity type|
|[**get_group**](#get_group) | Get group|
|[**get_group_dynamicsettings**](#get_group_dynamicsettings) | Get dynamic group definition|
|[**get_group_individuals**](#get_group_individuals) | Get all individuals associated with the group|
|[**get_group_members**](#get_group_members) | Get group members, includes individuals, owners, and dynamically included people|
|[**get_group_profile**](#get_group_profile) | Get group profile|
|[**get_groups**](#get_groups) | Get a group list|
|[**get_groups_search**](#get_groups_search) | Search groups using the q64 value returned from a previous search|
|[**get_profiles_groups**](#get_profiles_groups) | Get group profile listing|
|[**post_group_members**](#post_group_members) | Add members|
|[**post_groups**](#post_groups) | Create a group|
|[**post_groups_dynamicsettings_preview**](#post_groups_dynamicsettings_preview) | Preview the number of users selected for a dynamic group definition query|
|[**post_groups_search**](#post_groups_search) | Search groups|
|[**put_group**](#put_group) | Update group|
|[**put_group_dynamicsettings**](#put_group_dynamicsettings) | Create / Update dynamic group definition|



## delete_group

>  delete_group(group_id)


Delete group

Wraps DELETE /api/v2/groups/{groupId} 

Requires ANY permissions: 

* directory:group:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID

try:
    # Delete group
    api_instance.delete_group(group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |

### Return type

void (empty response body)


## delete_group_dynamicsettings

>  delete_group_dynamicsettings(group_id)


Remove dynamic group definition

delete_group_dynamicsettings is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/groups/{groupId}/dynamicsettings 

Requires ANY permissions: 

* directory:group:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID

try:
    # Remove dynamic group definition
    api_instance.delete_group_dynamicsettings(group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_group_dynamicsettings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |

### Return type

void (empty response body)


## delete_group_members

> object** delete_group_members(group_id, ids)


Remove members

Wraps DELETE /api/v2/groups/{groupId}/members 

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
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID
ids = 'ids_example' # str | Comma separated list of userIds to remove. A maximum of 50 members are allowed per request.

try:
    # Remove members
    api_response = api_instance.delete_group_members(group_id, ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_group_members: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |
| **ids** | **str**| Comma separated list of userIds to remove. A maximum of 50 members are allowed per request. |  |

### Return type

**object**


## get_fieldconfig

> [**FieldConfig**](FieldConfig) get_fieldconfig(type)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Fetch field config for an entity type

Wraps GET /api/v2/fieldconfig 

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
api_instance = PureCloudPlatformClientV2.GroupsApi()
type = 'type_example' # str | Field type

try:
    # Fetch field config for an entity type
    api_response = api_instance.get_fieldconfig(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_fieldconfig: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | **str**| Field type | <br />**Values**: person, group, org |

### Return type

[**FieldConfig**](FieldConfig)


## get_group

> [**Group**](Group) get_group(group_id)


Get group

Wraps GET /api/v2/groups/{groupId} 

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
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID

try:
    # Get group
    api_response = api_instance.get_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |

### Return type

[**Group**](Group)


## get_group_dynamicsettings

> [**DynamicGroupDefinition**](DynamicGroupDefinition) get_group_dynamicsettings(group_id)


Get dynamic group definition

get_group_dynamicsettings is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/groups/{groupId}/dynamicsettings 

Requires ANY permissions: 

* directory:group:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID

try:
    # Get dynamic group definition
    api_response = api_instance.get_group_dynamicsettings(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_group_dynamicsettings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |

### Return type

[**DynamicGroupDefinition**](DynamicGroupDefinition)


## get_group_individuals

> [**UserEntityListing**](UserEntityListing) get_group_individuals(group_id)


Get all individuals associated with the group

Wraps GET /api/v2/groups/{groupId}/individuals 

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
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID

try:
    # Get all individuals associated with the group
    api_response = api_instance.get_group_individuals(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_group_individuals: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |

### Return type

[**UserEntityListing**](UserEntityListing)


## get_group_members

> [**UserEntityListing**](UserEntityListing) get_group_members(group_id, page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand)


Get group members, includes individuals, owners, and dynamically included people

Wraps GET /api/v2/groups/{groupId}/members 

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
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''ASC'' # str | Ascending or descending sort order (optional) (default to 'ASC')
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get group members, includes individuals, owners, and dynamically included people
    api_response = api_instance.get_group_members(group_id, page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_group_members: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;ASC&#39;]<br />**Values**: ascending, descending |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, dateLastLogin, dateWelcomeSent |

### Return type

[**UserEntityListing**](UserEntityListing)


## get_group_profile

> [**GroupProfile**](GroupProfile) get_group_profile(group_id, fields=fields)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get group profile

This api is deprecated. Use /api/v2/groups instead

Wraps GET /api/v2/groups/{groupId}/profile 

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
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | groupId
fields = 'fields_example' # str | Comma separated fields to return.  Allowable values can be found by querying /api/v2/fieldconfig?type=group and using the key for the elements returned by the fieldList (optional)

try:
    # Get group profile
    api_response = api_instance.get_group_profile(group_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_group_profile: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| groupId |  |
| **fields** | **str**| Comma separated fields to return.  Allowable values can be found by querying /api/v2/fieldconfig?type&#x3D;group and using the key for the elements returned by the fieldList | [optional]  |

### Return type

[**GroupProfile**](GroupProfile)


## get_groups

> [**GroupEntityListing**](GroupEntityListing) get_groups(page_size=page_size, page_number=page_number, id=id, jabber_id=jabber_id, sort_order=sort_order)


Get a group list

Wraps GET /api/v2/groups 

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
api_instance = PureCloudPlatformClientV2.GroupsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
id = ['id_example'] # list[str] | id (optional)
jabber_id = ['jabber_id_example'] # list[str] | A list of jabberIds to fetch by bulk (cannot be used with the \"id\" parameter) (optional)
sort_order = ''ASC'' # str | Ascending or descending sort order (optional) (default to 'ASC')

try:
    # Get a group list
    api_response = api_instance.get_groups(page_size=page_size, page_number=page_number, id=id, jabber_id=jabber_id, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_groups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **id** | [**list[str]**](str)| id | [optional]  |
| **jabber_id** | [**list[str]**](str)| A list of jabberIds to fetch by bulk (cannot be used with the \&quot;id\&quot; parameter) | [optional]  |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;ASC&#39;]<br />**Values**: ascending, descending |

### Return type

[**GroupEntityListing**](GroupEntityListing)


## get_groups_search

> [**GroupsSearchResponse**](GroupsSearchResponse) get_groups_search(q64, expand=expand)


Search groups using the q64 value returned from a previous search

Wraps GET /api/v2/groups/search 

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
api_instance = PureCloudPlatformClientV2.GroupsApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | expand (optional)

try:
    # Search groups using the q64 value returned from a previous search
    api_response = api_instance.get_groups_search(q64, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_groups_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str)| expand | [optional]  |

### Return type

[**GroupsSearchResponse**](GroupsSearchResponse)


## get_profiles_groups

> [**GroupProfileEntityListing**](GroupProfileEntityListing) get_profiles_groups(page_size=page_size, page_number=page_number, id=id, jabber_id=jabber_id, sort_order=sort_order)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get group profile listing

This api is deprecated. Use /api/v2/groups instead.

Wraps GET /api/v2/profiles/groups 

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
api_instance = PureCloudPlatformClientV2.GroupsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
id = ['id_example'] # list[str] | id (optional)
jabber_id = ['jabber_id_example'] # list[str] | A list of jabberIds to fetch by bulk (cannot be used with the \"id\" parameter) (optional)
sort_order = ''ASC'' # str | Ascending or descending sort order (optional) (default to 'ASC')

try:
    # Get group profile listing
    api_response = api_instance.get_profiles_groups(page_size=page_size, page_number=page_number, id=id, jabber_id=jabber_id, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_profiles_groups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **id** | [**list[str]**](str)| id | [optional]  |
| **jabber_id** | [**list[str]**](str)| A list of jabberIds to fetch by bulk (cannot be used with the \&quot;id\&quot; parameter) | [optional]  |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;ASC&#39;]<br />**Values**: ascending, descending |

### Return type

[**GroupProfileEntityListing**](GroupProfileEntityListing)


## post_group_members

> object** post_group_members(group_id, body)


Add members

Wraps POST /api/v2/groups/{groupId}/members 

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
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID
body = PureCloudPlatformClientV2.GroupMembersUpdate() # GroupMembersUpdate | Add members

try:
    # Add members
    api_response = api_instance.post_group_members(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->post_group_members: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |
| **body** | [**GroupMembersUpdate**](GroupMembersUpdate)| Add members |  |

### Return type

**object**


## post_groups

> [**Group**](Group) post_groups(body)


Create a group

Wraps POST /api/v2/groups 

Requires ANY permissions: 

* directory:group:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
body = PureCloudPlatformClientV2.GroupCreate() # GroupCreate | Group

try:
    # Create a group
    api_response = api_instance.post_groups(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->post_groups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GroupCreate**](GroupCreate)| Group |  |

### Return type

[**Group**](Group)


## post_groups_dynamicsettings_preview

> [**DynamicGroupQueryPreview**](DynamicGroupQueryPreview) post_groups_dynamicsettings_preview(body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Preview the number of users selected for a dynamic group definition query

post_groups_dynamicsettings_preview is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/groups/dynamicsettings/preview 

Requires ANY permissions: 

* directory:group:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
body = PureCloudPlatformClientV2.DynamicGroupQuery() # DynamicGroupQuery | Group query to preview

try:
    # Preview the number of users selected for a dynamic group definition query
    api_response = api_instance.post_groups_dynamicsettings_preview(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->post_groups_dynamicsettings_preview: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DynamicGroupQuery**](DynamicGroupQuery)| Group query to preview |  |

### Return type

[**DynamicGroupQueryPreview**](DynamicGroupQueryPreview)


## post_groups_search

> [**GroupsSearchResponse**](GroupsSearchResponse) post_groups_search(body)


Search groups

Wraps POST /api/v2/groups/search 

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
api_instance = PureCloudPlatformClientV2.GroupsApi()
body = PureCloudPlatformClientV2.GroupSearchRequest() # GroupSearchRequest | Search request options

try:
    # Search groups
    api_response = api_instance.post_groups_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->post_groups_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GroupSearchRequest**](GroupSearchRequest)| Search request options |  |

### Return type

[**GroupsSearchResponse**](GroupsSearchResponse)


## put_group

> [**Group**](Group) put_group(group_id, body=body)


Update group

Wraps PUT /api/v2/groups/{groupId} 

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
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID
body = PureCloudPlatformClientV2.GroupUpdate() # GroupUpdate | Group (optional)

try:
    # Update group
    api_response = api_instance.put_group(group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->put_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |
| **body** | [**GroupUpdate**](GroupUpdate)| Group | [optional]  |

### Return type

[**Group**](Group)


## put_group_dynamicsettings

>  put_group_dynamicsettings(group_id, body)


Create / Update dynamic group definition

put_group_dynamicsettings is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PUT /api/v2/groups/{groupId}/dynamicsettings 

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
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID
body = PureCloudPlatformClientV2.DynamicGroupQuery() # DynamicGroupQuery | Create/Update dynamic groups

try:
    # Create / Update dynamic group definition
    api_instance.put_group_dynamicsettings(group_id, body)
except ApiException as e:
    print("Exception when calling GroupsApi->put_group_dynamicsettings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |
| **body** | [**DynamicGroupQuery**](DynamicGroupQuery)| Create/Update dynamic groups |  |

### Return type

void (empty response body)


_PureCloudPlatformClientV2 227.0.0_

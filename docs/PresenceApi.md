# PresenceApi

## PureCloudPlatformClientV2.PresenceApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_presence_definition**](#delete_presence_definition) | Delete a Presence Definition|
|[**delete_presence_source**](#delete_presence_source) | Delete a Presence Source|
|[**delete_presencedefinition**](#delete_presencedefinition) | Delete a Presence Definition. Apps should migrate to use DELETE /api/v2/presence/definitions/{definitionId} instead|
|[**get_presence_definition**](#get_presence_definition) | Get a Presence Definition|
|[**get_presence_definitions**](#get_presence_definitions) | Get a list of Presence Definitions|
|[**get_presence_settings**](#get_presence_settings) | Get the presence settings|
|[**get_presence_source**](#get_presence_source) | Get a Presence Source|
|[**get_presence_sources**](#get_presence_sources) | Get a list of Presence Sources|
|[**get_presence_user_primarysource**](#get_presence_user_primarysource) | Get a user&#39;s Primary Presence Source|
|[**get_presencedefinition**](#get_presencedefinition) | Get a Presence Definition. Apps should migrate to use GET /api/v2/presence/definitions/{definitionId} instead|
|[**get_presencedefinitions**](#get_presencedefinitions) | Get an Organization&#39;s list of Presence Definitions. Apps should migrate to use GET /api/v2/presence/definitions instead|
|[**get_systempresences**](#get_systempresences) | Get the list of SystemPresences|
|[**get_user_presence**](#get_user_presence) | Get a user&#39;s Presence|
|[**get_user_presences_purecloud**](#get_user_presences_purecloud) | Get a user&#39;s Genesys Cloud presence.|
|[**get_users_presence_bulk**](#get_users_presence_bulk) | Get bulk user presences for a single presence source|
|[**get_users_presences_purecloud_bulk**](#get_users_presences_purecloud_bulk) | Get bulk user presences for a Genesys Cloud (PURECLOUD) presence source|
|[**patch_user_presence**](#patch_user_presence) | Patch a user&#39;s Presence|
|[**patch_user_presences_purecloud**](#patch_user_presences_purecloud) | Patch a Genesys Cloud user&#39;s presence|
|[**post_presence_definitions**](#post_presence_definitions) | Create a Presence Definition|
|[**post_presence_sources**](#post_presence_sources) | Create a Presence Source|
|[**post_presencedefinitions**](#post_presencedefinitions) | Create a Presence Definition. Apps should migrate to use POST /api/v2/presence/definitions instead|
|[**put_presence_definition**](#put_presence_definition) | Update a Presence Definition|
|[**put_presence_settings**](#put_presence_settings) | Update the presence settings|
|[**put_presence_source**](#put_presence_source) | Update a Presence Source|
|[**put_presence_user_primarysource**](#put_presence_user_primarysource) | Update a user&#39;s Primary Presence Source|
|[**put_presencedefinition**](#put_presencedefinition) | Update a Presence Definition. Apps should migrate to use PUT /api/v2/presence/definitions/{definitionId} instead)|
|[**put_users_presences_bulk**](#put_users_presences_bulk) | Update bulk user Presences|



## delete_presence_definition

>  delete_presence_definition(definition_id)


Delete a Presence Definition

Wraps DELETE /api/v2/presence/definitions/{definitionId} 

Requires ANY permissions: 

* presence:presenceDefinition:delete
* presence:presenceDefinition:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
definition_id = 'definition_id_example' # str | Presence Definition ID

try:
    # Delete a Presence Definition
    api_instance.delete_presence_definition(definition_id)
except ApiException as e:
    print("Exception when calling PresenceApi->delete_presence_definition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **definition_id** | **str**| Presence Definition ID |  |

### Return type

void (empty response body)


## delete_presence_source

>  delete_presence_source(source_id)


Delete a Presence Source

Wraps DELETE /api/v2/presence/sources/{sourceId} 

Requires ANY permissions: 

* presence:source:delete
* presence:source:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
source_id = 'source_id_example' # str | Presence Source ID

try:
    # Delete a Presence Source
    api_instance.delete_presence_source(source_id)
except ApiException as e:
    print("Exception when calling PresenceApi->delete_presence_source: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **source_id** | **str**| Presence Source ID |  |

### Return type

void (empty response body)


## delete_presencedefinition

>  delete_presencedefinition(presence_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Delete a Presence Definition. Apps should migrate to use DELETE /api/v2/presence/definitions/{definitionId} instead

Wraps DELETE /api/v2/presencedefinitions/{presenceId} 

Requires ALL permissions: 

* presence:presenceDefinition:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
presence_id = 'presence_id_example' # str | Organization Presence ID

try:
    # Delete a Presence Definition. Apps should migrate to use DELETE /api/v2/presence/definitions/{definitionId} instead
    api_instance.delete_presencedefinition(presence_id)
except ApiException as e:
    print("Exception when calling PresenceApi->delete_presencedefinition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **presence_id** | **str**| Organization Presence ID |  |

### Return type

void (empty response body)


## get_presence_definition

> [**OrganizationPresenceDefinition**](OrganizationPresenceDefinition) get_presence_definition(definition_id, locale_code=locale_code)


Get a Presence Definition

Wraps GET /api/v2/presence/definitions/{definitionId} 

Requires ALL permissions: 

* presence:presenceDefinition:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
definition_id = 'definition_id_example' # str | Presence Definition ID
locale_code = 'locale_code_example' # str | The locale code to fetch for the presence definition. Use ALL to fetch everything. (optional)

try:
    # Get a Presence Definition
    api_response = api_instance.get_presence_definition(definition_id, locale_code=locale_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->get_presence_definition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **definition_id** | **str**| Presence Definition ID |  |
| **locale_code** | **str**| The locale code to fetch for the presence definition. Use ALL to fetch everything. | [optional] <br />**Values**: ALL, he, fr, en_US, da, de, it, cs, es, fi, ar, ja, ko, nl, no, pl, pt_BR, pt_PT, ru, sv, th, tr, uk, zh_CN, zh_TW |

### Return type

[**OrganizationPresenceDefinition**](OrganizationPresenceDefinition)


## get_presence_definitions

> [**OrganizationPresenceDefinitionEntityListing**](OrganizationPresenceDefinitionEntityListing) get_presence_definitions(deactivated=deactivated, division_id=division_id, locale_code=locale_code)


Get a list of Presence Definitions

Wraps GET /api/v2/presence/definitions 

Requires ALL permissions: 

* presence:presenceDefinition:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
deactivated = ''false'' # str | Deactivated query can be TRUE or FALSE (optional) (default to 'false')
division_id = ['division_id_example'] # list[str] | One or more division IDs. If nothing is provided, the definitions associated withthe list of divisions that the user has access to will be returned. (optional)
locale_code = 'locale_code_example' # str | The locale code to fetch for the presence definition. Use ALL to fetch everything. (optional)

try:
    # Get a list of Presence Definitions
    api_response = api_instance.get_presence_definitions(deactivated=deactivated, division_id=division_id, locale_code=locale_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->get_presence_definitions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deactivated** | **str**| Deactivated query can be TRUE or FALSE | [optional] [default to &#39;false&#39;] |
| **division_id** | [**list[str]**](str)| One or more division IDs. If nothing is provided, the definitions associated withthe list of divisions that the user has access to will be returned. | [optional]  |
| **locale_code** | **str**| The locale code to fetch for the presence definition. Use ALL to fetch everything. | [optional] <br />**Values**: ALL, he, fr, en_US, da, de, it, cs, es, fi, ar, ja, ko, nl, no, pl, pt_BR, pt_PT, ru, sv, th, tr, uk, zh_CN, zh_TW |

### Return type

[**OrganizationPresenceDefinitionEntityListing**](OrganizationPresenceDefinitionEntityListing)


## get_presence_settings

> [**PresenceSettings**](PresenceSettings) get_presence_settings()


Get the presence settings

Wraps GET /api/v2/presence/settings 

Requires ALL permissions: 

* presence:settings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()

try:
    # Get the presence settings
    api_response = api_instance.get_presence_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->get_presence_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**PresenceSettings**](PresenceSettings)


## get_presence_source

> [**Source**](Source) get_presence_source(source_id)


Get a Presence Source

Wraps GET /api/v2/presence/sources/{sourceId} 

Requires ALL permissions: 

* presence:source:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
source_id = 'source_id_example' # str | Presence Source ID

try:
    # Get a Presence Source
    api_response = api_instance.get_presence_source(source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->get_presence_source: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **source_id** | **str**| Presence Source ID |  |

### Return type

[**Source**](Source)


## get_presence_sources

> [**SourceEntityListing**](SourceEntityListing) get_presence_sources(deactivated=deactivated)


Get a list of Presence Sources

Wraps GET /api/v2/presence/sources 

Requires ALL permissions: 

* presence:source:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
deactivated = ''false'' # str | Deactivated query can be TRUE or FALSE (optional) (default to 'false')

try:
    # Get a list of Presence Sources
    api_response = api_instance.get_presence_sources(deactivated=deactivated)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->get_presence_sources: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deactivated** | **str**| Deactivated query can be TRUE or FALSE | [optional] [default to &#39;false&#39;] |

### Return type

[**SourceEntityListing**](SourceEntityListing)


## get_presence_user_primarysource

> [**UserPrimarySource**](UserPrimarySource) get_presence_user_primarysource(user_id)


Get a user's Primary Presence Source

Wraps GET /api/v2/presence/users/{userId}/primarysource 

Requires ALL permissions: 

* presence:userPrimarySource:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
user_id = 'user_id_example' # str | user ID

try:
    # Get a user's Primary Presence Source
    api_response = api_instance.get_presence_user_primarysource(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->get_presence_user_primarysource: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| user ID |  |

### Return type

[**UserPrimarySource**](UserPrimarySource)


## get_presencedefinition

> [**OrganizationPresence**](OrganizationPresence) get_presencedefinition(presence_id, locale_code=locale_code)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get a Presence Definition. Apps should migrate to use GET /api/v2/presence/definitions/{definitionId} instead

Wraps GET /api/v2/presencedefinitions/{presenceId} 

Requires ALL permissions: 

* presence:presenceDefinition:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
presence_id = 'presence_id_example' # str | Organization Presence ID
locale_code = 'locale_code_example' # str | The locale code to fetch for the presence definition. Use ALL to fetch everything. (optional)

try:
    # Get a Presence Definition. Apps should migrate to use GET /api/v2/presence/definitions/{definitionId} instead
    api_response = api_instance.get_presencedefinition(presence_id, locale_code=locale_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->get_presencedefinition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **presence_id** | **str**| Organization Presence ID |  |
| **locale_code** | **str**| The locale code to fetch for the presence definition. Use ALL to fetch everything. | [optional]  |

### Return type

[**OrganizationPresence**](OrganizationPresence)


## get_presencedefinitions

> [**OrganizationPresenceEntityListing**](OrganizationPresenceEntityListing) get_presencedefinitions(page_number=page_number, page_size=page_size, deleted=deleted, locale_code=locale_code)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get an Organization's list of Presence Definitions. Apps should migrate to use GET /api/v2/presence/definitions instead

Wraps GET /api/v2/presencedefinitions 

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
api_instance = PureCloudPlatformClientV2.PresenceApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
deleted = ''false'' # str | Deleted query can be TRUE, FALSE or ALL (optional) (default to 'false')
locale_code = 'locale_code_example' # str | The locale code to fetch for each presence definition. Use ALL to fetch everything. (optional)

try:
    # Get an Organization's list of Presence Definitions. Apps should migrate to use GET /api/v2/presence/definitions instead
    api_response = api_instance.get_presencedefinitions(page_number=page_number, page_size=page_size, deleted=deleted, locale_code=locale_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->get_presencedefinitions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **deleted** | **str**| Deleted query can be TRUE, FALSE or ALL | [optional] [default to &#39;false&#39;] |
| **locale_code** | **str**| The locale code to fetch for each presence definition. Use ALL to fetch everything. | [optional]  |

### Return type

[**OrganizationPresenceEntityListing**](OrganizationPresenceEntityListing)


## get_systempresences

> [**list[SystemPresence]**](SystemPresence) get_systempresences()


Get the list of SystemPresences

Wraps GET /api/v2/systempresences 

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
api_instance = PureCloudPlatformClientV2.PresenceApi()

try:
    # Get the list of SystemPresences
    api_response = api_instance.get_systempresences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->get_systempresences: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**list[SystemPresence]**](SystemPresence)


## get_user_presence

> [**UserPresence**](UserPresence) get_user_presence(user_id, source_id)


Get a user's Presence

Get a user's presence for the specified source that is not specifically listed.  Used to support custom presence sources. This endpoint does not support registered presence sources.

Wraps GET /api/v2/users/{userId}/presences/{sourceId} 

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
api_instance = PureCloudPlatformClientV2.PresenceApi()
user_id = 'user_id_example' # str | user Id
source_id = 'source_id_example' # str | Presence source ID

try:
    # Get a user's Presence
    api_response = api_instance.get_user_presence(user_id, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->get_user_presence: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| user Id |  |
| **source_id** | **str**| Presence source ID |  |

### Return type

[**UserPresence**](UserPresence)


## get_user_presences_purecloud

> [**UserPresence**](UserPresence) get_user_presences_purecloud(user_id)


Get a user's Genesys Cloud presence.

Get the default Genesys Cloud user presence source PURECLOUD

Wraps GET /api/v2/users/{userId}/presences/purecloud 

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
api_instance = PureCloudPlatformClientV2.PresenceApi()
user_id = 'user_id_example' # str | user Id

try:
    # Get a user's Genesys Cloud presence.
    api_response = api_instance.get_user_presences_purecloud(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->get_user_presences_purecloud: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| user Id |  |

### Return type

[**UserPresence**](UserPresence)


## get_users_presence_bulk

> [**list[UcUserPresence]**](UcUserPresence) get_users_presence_bulk(source_id, id=id)


Get bulk user presences for a single presence source

Wraps GET /api/v2/users/presences/{sourceId}/bulk 

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
api_instance = PureCloudPlatformClientV2.PresenceApi()
source_id = 'source_id_example' # str | The requested presence source ID.
id = ['id_example'] # list[str] | A comma separated list of user IDs to fetch their presence status in bulk. Limit 50. (optional)

try:
    # Get bulk user presences for a single presence source
    api_response = api_instance.get_users_presence_bulk(source_id, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->get_users_presence_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **source_id** | **str**| The requested presence source ID. |  |
| **id** | [**list[str]**](str)| A comma separated list of user IDs to fetch their presence status in bulk. Limit 50. | [optional]  |

### Return type

[**list[UcUserPresence]**](UcUserPresence)


## get_users_presences_purecloud_bulk

> [**list[UcUserPresence]**](UcUserPresence) get_users_presences_purecloud_bulk(id=id)


Get bulk user presences for a Genesys Cloud (PURECLOUD) presence source

Wraps GET /api/v2/users/presences/purecloud/bulk 

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
api_instance = PureCloudPlatformClientV2.PresenceApi()
id = ['id_example'] # list[str] | A comma separated list of user IDs to fetch their presence status in bulk. Limit 50. (optional)

try:
    # Get bulk user presences for a Genesys Cloud (PURECLOUD) presence source
    api_response = api_instance.get_users_presences_purecloud_bulk(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->get_users_presences_purecloud_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str)| A comma separated list of user IDs to fetch their presence status in bulk. Limit 50. | [optional]  |

### Return type

[**list[UcUserPresence]**](UcUserPresence)


## patch_user_presence

> [**UserPresence**](UserPresence) patch_user_presence(user_id, source_id, body)


Patch a user's Presence

Patch a user's presence for the specified source that is not specifically listed. This endpoint does not support registered presence sources. The presence object can be patched one of three ways. Option 1: Set the 'primary' property to true. This will set the 'source' defined in the path as the user's primary presence source. Option 2: Provide the presenceDefinition value. The 'id' is the only value required within the presenceDefinition. Option 3: Provide the message value. Option 1 can be combined with Option 2 and/or Option 3.

Wraps PATCH /api/v2/users/{userId}/presences/{sourceId} 

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
api_instance = PureCloudPlatformClientV2.PresenceApi()
user_id = 'user_id_example' # str | user Id
source_id = 'source_id_example' # str | Presence source ID
body = PureCloudPlatformClientV2.UserPresence() # UserPresence | User presence

try:
    # Patch a user's Presence
    api_response = api_instance.patch_user_presence(user_id, source_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->patch_user_presence: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| user Id |  |
| **source_id** | **str**| Presence source ID |  |
| **body** | [**UserPresence**](UserPresence)| User presence |  |

### Return type

[**UserPresence**](UserPresence)


## patch_user_presences_purecloud

> [**UserPresence**](UserPresence) patch_user_presences_purecloud(user_id, body)


Patch a Genesys Cloud user's presence

The presence object can be patched one of three ways. Option 1: Set the 'primary' property to true. This will set the PURECLOUD source as the user's primary presence source. Option 2: Provide the presenceDefinition value. The 'id' is the only value required within the presenceDefinition. Option 3: Provide the message value. Option 1 can be combined with Option 2 and/or Option 3.

Wraps PATCH /api/v2/users/{userId}/presences/purecloud 

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
api_instance = PureCloudPlatformClientV2.PresenceApi()
user_id = 'user_id_example' # str | user Id
body = PureCloudPlatformClientV2.UserPresence() # UserPresence | User presence

try:
    # Patch a Genesys Cloud user's presence
    api_response = api_instance.patch_user_presences_purecloud(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->patch_user_presences_purecloud: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| user Id |  |
| **body** | [**UserPresence**](UserPresence)| User presence |  |

### Return type

[**UserPresence**](UserPresence)


## post_presence_definitions

> [**OrganizationPresenceDefinition**](OrganizationPresenceDefinition) post_presence_definitions(body)


Create a Presence Definition

Wraps POST /api/v2/presence/definitions 

Requires ALL permissions: 

* presence:presenceDefinition:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
body = PureCloudPlatformClientV2.OrganizationPresenceDefinition() # OrganizationPresenceDefinition | The Presence Definition to create

try:
    # Create a Presence Definition
    api_response = api_instance.post_presence_definitions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->post_presence_definitions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OrganizationPresenceDefinition**](OrganizationPresenceDefinition)| The Presence Definition to create |  |

### Return type

[**OrganizationPresenceDefinition**](OrganizationPresenceDefinition)


## post_presence_sources

> [**Source**](Source) post_presence_sources(body)


Create a Presence Source

Wraps POST /api/v2/presence/sources 

Requires ALL permissions: 

* presence:source:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
body = PureCloudPlatformClientV2.Source() # Source | The Presence Source to create

try:
    # Create a Presence Source
    api_response = api_instance.post_presence_sources(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->post_presence_sources: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Source**](Source)| The Presence Source to create |  |

### Return type

[**Source**](Source)


## post_presencedefinitions

> [**OrganizationPresence**](OrganizationPresence) post_presencedefinitions(body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Create a Presence Definition. Apps should migrate to use POST /api/v2/presence/definitions instead

Wraps POST /api/v2/presencedefinitions 

Requires ALL permissions: 

* presence:presenceDefinition:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
body = PureCloudPlatformClientV2.OrganizationPresence() # OrganizationPresence | The Presence Definition to create

try:
    # Create a Presence Definition. Apps should migrate to use POST /api/v2/presence/definitions instead
    api_response = api_instance.post_presencedefinitions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->post_presencedefinitions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OrganizationPresence**](OrganizationPresence)| The Presence Definition to create |  |

### Return type

[**OrganizationPresence**](OrganizationPresence)


## put_presence_definition

> [**OrganizationPresenceDefinition**](OrganizationPresenceDefinition) put_presence_definition(definition_id, body)


Update a Presence Definition

Wraps PUT /api/v2/presence/definitions/{definitionId} 

Requires ALL permissions: 

* presence:presenceDefinition:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
definition_id = 'definition_id_example' # str | Presence Definition ID
body = PureCloudPlatformClientV2.OrganizationPresenceDefinition() # OrganizationPresenceDefinition | The updated Presence Definition

try:
    # Update a Presence Definition
    api_response = api_instance.put_presence_definition(definition_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->put_presence_definition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **definition_id** | **str**| Presence Definition ID |  |
| **body** | [**OrganizationPresenceDefinition**](OrganizationPresenceDefinition)| The updated Presence Definition |  |

### Return type

[**OrganizationPresenceDefinition**](OrganizationPresenceDefinition)


## put_presence_settings

> [**PresenceSettings**](PresenceSettings) put_presence_settings(body)


Update the presence settings

Wraps PUT /api/v2/presence/settings 

Requires ALL permissions: 

* presence:settings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
body = PureCloudPlatformClientV2.PresenceSettings() # PresenceSettings | Presence Settings

try:
    # Update the presence settings
    api_response = api_instance.put_presence_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->put_presence_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PresenceSettings**](PresenceSettings)| Presence Settings |  |

### Return type

[**PresenceSettings**](PresenceSettings)


## put_presence_source

> [**Source**](Source) put_presence_source(source_id, body)


Update a Presence Source

Wraps PUT /api/v2/presence/sources/{sourceId} 

Requires ALL permissions: 

* presence:source:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
source_id = 'source_id_example' # str | Presence Source ID
body = PureCloudPlatformClientV2.Source() # Source | The updated Presence Source

try:
    # Update a Presence Source
    api_response = api_instance.put_presence_source(source_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->put_presence_source: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **source_id** | **str**| Presence Source ID |  |
| **body** | [**Source**](Source)| The updated Presence Source |  |

### Return type

[**Source**](Source)


## put_presence_user_primarysource

> [**UserPrimarySource**](UserPrimarySource) put_presence_user_primarysource(user_id, body)


Update a user's Primary Presence Source

Wraps PUT /api/v2/presence/users/{userId}/primarysource 

Requires ALL permissions: 

* presence:userPrimarySource:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
user_id = 'user_id_example' # str | user ID
body = PureCloudPlatformClientV2.UserPrimarySource() # UserPrimarySource | Primary Source

try:
    # Update a user's Primary Presence Source
    api_response = api_instance.put_presence_user_primarysource(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->put_presence_user_primarysource: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| user ID |  |
| **body** | [**UserPrimarySource**](UserPrimarySource)| Primary Source |  |

### Return type

[**UserPrimarySource**](UserPrimarySource)


## put_presencedefinition

> [**OrganizationPresence**](OrganizationPresence) put_presencedefinition(presence_id, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Update a Presence Definition. Apps should migrate to use PUT /api/v2/presence/definitions/{definitionId} instead)

Wraps PUT /api/v2/presencedefinitions/{presenceId} 

Requires ALL permissions: 

* presence:presenceDefinition:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
presence_id = 'presence_id_example' # str | Organization Presence ID
body = PureCloudPlatformClientV2.OrganizationPresence() # OrganizationPresence | The OrganizationPresence to update

try:
    # Update a Presence Definition. Apps should migrate to use PUT /api/v2/presence/definitions/{definitionId} instead)
    api_response = api_instance.put_presencedefinition(presence_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->put_presencedefinition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **presence_id** | **str**| Organization Presence ID |  |
| **body** | [**OrganizationPresence**](OrganizationPresence)| The OrganizationPresence to update |  |

### Return type

[**OrganizationPresence**](OrganizationPresence)


## put_users_presences_bulk

> [**list[UserPresence]**](UserPresence) put_users_presences_bulk(body)


Update bulk user Presences

Wraps PUT /api/v2/users/presences/bulk 

Requires ANY permissions: 

* presence:userPresence:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
body = [PureCloudPlatformClientV2.MutableUserPresence()] # list[MutableUserPresence] | List of User presences

try:
    # Update bulk user Presences
    api_response = api_instance.put_users_presences_bulk(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->put_users_presences_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**list[MutableUserPresence]**](MutableUserPresence)| List of User presences |  |

### Return type

[**list[UserPresence]**](UserPresence)


_PureCloudPlatformClientV2 227.1.0_

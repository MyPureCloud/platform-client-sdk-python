---
title: PresenceApi
---

## PureCloudPlatformClientV2.PresenceApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_presence_definition**](PresenceApi.html#delete_presence_definition) | Delete a Presence Definition|
|[**delete_presence_source**](PresenceApi.html#delete_presence_source) | Delete a Presence Source|
|[**delete_presencedefinition**](PresenceApi.html#delete_presencedefinition) | Delete a Presence Definition|
|[**get_presence_definition**](PresenceApi.html#get_presence_definition) | Get a Presence Definition|
|[**get_presence_definitions**](PresenceApi.html#get_presence_definitions) | Get a list of Presence Definitions|
|[**get_presence_settings**](PresenceApi.html#get_presence_settings) | Get the presence settings|
|[**get_presence_source**](PresenceApi.html#get_presence_source) | Get a Presence Source|
|[**get_presence_sources**](PresenceApi.html#get_presence_sources) | Get a list of Presence Sources|
|[**get_presence_user_primarysource**](PresenceApi.html#get_presence_user_primarysource) | Get a user&#39;s Primary Presence Source|
|[**get_presencedefinition**](PresenceApi.html#get_presencedefinition) | Get a Presence Definition|
|[**get_presencedefinitions**](PresenceApi.html#get_presencedefinitions) | Get an Organization&#39;s list of Presence Definitions|
|[**get_systempresences**](PresenceApi.html#get_systempresences) | Get the list of SystemPresences|
|[**get_user_presence**](PresenceApi.html#get_user_presence) | Get a user&#39;s Presence|
|[**get_user_presences_purecloud**](PresenceApi.html#get_user_presences_purecloud) | Get a user&#39;s Genesys Cloud presence.|
|[**get_users_presence_bulk**](PresenceApi.html#get_users_presence_bulk) | Get bulk user presences for a single presence source|
|[**get_users_presences_purecloud_bulk**](PresenceApi.html#get_users_presences_purecloud_bulk) | Get bulk user presences for a Genesys Cloud (PURECLOUD) presence source|
|[**patch_user_presence**](PresenceApi.html#patch_user_presence) | Patch a user&#39;s Presence|
|[**patch_user_presences_purecloud**](PresenceApi.html#patch_user_presences_purecloud) | Patch a Genesys Cloud user&#39;s presence|
|[**post_presence_definitions**](PresenceApi.html#post_presence_definitions) | Create a Presence Definition|
|[**post_presence_sources**](PresenceApi.html#post_presence_sources) | Create a Presence Source|
|[**post_presencedefinitions**](PresenceApi.html#post_presencedefinitions) | Create a Presence Definition|
|[**put_presence_definition**](PresenceApi.html#put_presence_definition) | Update a Presence Definition|
|[**put_presence_settings**](PresenceApi.html#put_presence_settings) | Update the presence settings|
|[**put_presence_source**](PresenceApi.html#put_presence_source) | Update a Presence Source|
|[**put_presence_user_primarysource**](PresenceApi.html#put_presence_user_primarysource) | Update a user&#39;s Primary Presence Source|
|[**put_presencedefinition**](PresenceApi.html#put_presencedefinition) | Update a Presence Definition|
|[**put_users_presences_bulk**](PresenceApi.html#put_users_presences_bulk) | Update bulk user Presences|
{: class="table table-striped"}

<a name="delete_presence_definition"></a>

##  delete_presence_definition(definition_id)



Delete a Presence Definition

delete_presence_definition is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_presence_source"></a>

##  delete_presence_source(source_id)



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
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_presencedefinition"></a>

##  delete_presencedefinition(presence_id)



Delete a Presence Definition

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
    # Delete a Presence Definition
    api_instance.delete_presencedefinition(presence_id)
except ApiException as e:
    print("Exception when calling PresenceApi->delete_presencedefinition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **presence_id** | **str**| Organization Presence ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_presence_definition"></a>

## [**OrganizationPresenceDefinition**](OrganizationPresenceDefinition.html) get_presence_definition(definition_id, locale_code=locale_code)



Get a Presence Definition

get_presence_definition is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
{: class="table table-striped"}

### Return type

[**OrganizationPresenceDefinition**](OrganizationPresenceDefinition.html)

<a name="get_presence_definitions"></a>

## [**OrganizationPresenceDefinitionEntityListing**](OrganizationPresenceDefinitionEntityListing.html) get_presence_definitions(deactivated=deactivated, division_id=division_id, locale_code=locale_code)



Get a list of Presence Definitions

get_presence_definitions is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
| **division_id** | [**list[str]**](str.html)| One or more division IDs. If nothing is provided, the definitions associated withthe list of divisions that the user has access to will be returned. | [optional]  |
| **locale_code** | **str**| The locale code to fetch for the presence definition. Use ALL to fetch everything. | [optional] <br />**Values**: ALL, he, fr, en_US, da, de, it, cs, es, fi, ar, ja, ko, nl, no, pl, pt_BR, pt_PT, ru, sv, th, tr, uk, zh_CN, zh_TW |
{: class="table table-striped"}

### Return type

[**OrganizationPresenceDefinitionEntityListing**](OrganizationPresenceDefinitionEntityListing.html)

<a name="get_presence_settings"></a>

## [**PresenceSettings**](PresenceSettings.html) get_presence_settings()



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

[**PresenceSettings**](PresenceSettings.html)

<a name="get_presence_source"></a>

## [**Source**](Source.html) get_presence_source(source_id)



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
{: class="table table-striped"}

### Return type

[**Source**](Source.html)

<a name="get_presence_sources"></a>

## [**SourceEntityListing**](SourceEntityListing.html) get_presence_sources(deactivated=deactivated)



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
{: class="table table-striped"}

### Return type

[**SourceEntityListing**](SourceEntityListing.html)

<a name="get_presence_user_primarysource"></a>

## [**UserPrimarySource**](UserPrimarySource.html) get_presence_user_primarysource(user_id)



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
{: class="table table-striped"}

### Return type

[**UserPrimarySource**](UserPrimarySource.html)

<a name="get_presencedefinition"></a>

## [**OrganizationPresence**](OrganizationPresence.html) get_presencedefinition(presence_id, locale_code=locale_code)



Get a Presence Definition

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
    # Get a Presence Definition
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
{: class="table table-striped"}

### Return type

[**OrganizationPresence**](OrganizationPresence.html)

<a name="get_presencedefinitions"></a>

## [**OrganizationPresenceEntityListing**](OrganizationPresenceEntityListing.html) get_presencedefinitions(page_number=page_number, page_size=page_size, deleted=deleted, locale_code=locale_code)



Get an Organization's list of Presence Definitions

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
    # Get an Organization's list of Presence Definitions
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
{: class="table table-striped"}

### Return type

[**OrganizationPresenceEntityListing**](OrganizationPresenceEntityListing.html)

<a name="get_systempresences"></a>

## [**list[SystemPresence]**](SystemPresence.html) get_systempresences()



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

[**list[SystemPresence]**](SystemPresence.html)

<a name="get_user_presence"></a>

## [**UserPresence**](UserPresence.html) get_user_presence(user_id, source_id)



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
{: class="table table-striped"}

### Return type

[**UserPresence**](UserPresence.html)

<a name="get_user_presences_purecloud"></a>

## [**UserPresence**](UserPresence.html) get_user_presences_purecloud(user_id)



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
{: class="table table-striped"}

### Return type

[**UserPresence**](UserPresence.html)

<a name="get_users_presence_bulk"></a>

## [**list[UcUserPresence]**](UcUserPresence.html) get_users_presence_bulk(source_id, id=id)



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
| **id** | [**list[str]**](str.html)| A comma separated list of user IDs to fetch their presence status in bulk. Limit 50. | [optional]  |
{: class="table table-striped"}

### Return type

[**list[UcUserPresence]**](UcUserPresence.html)

<a name="get_users_presences_purecloud_bulk"></a>

## [**list[UcUserPresence]**](UcUserPresence.html) get_users_presences_purecloud_bulk(id=id)



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
| **id** | [**list[str]**](str.html)| A comma separated list of user IDs to fetch their presence status in bulk. Limit 50. | [optional]  |
{: class="table table-striped"}

### Return type

[**list[UcUserPresence]**](UcUserPresence.html)

<a name="patch_user_presence"></a>

## [**UserPresence**](UserPresence.html) patch_user_presence(user_id, source_id, body)



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
| **body** | [**UserPresence**](UserPresence.html)| User presence |  |
{: class="table table-striped"}

### Return type

[**UserPresence**](UserPresence.html)

<a name="patch_user_presences_purecloud"></a>

## [**UserPresence**](UserPresence.html) patch_user_presences_purecloud(user_id, body)



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
| **body** | [**UserPresence**](UserPresence.html)| User presence |  |
{: class="table table-striped"}

### Return type

[**UserPresence**](UserPresence.html)

<a name="post_presence_definitions"></a>

## [**OrganizationPresenceDefinition**](OrganizationPresenceDefinition.html) post_presence_definitions(body)



Create a Presence Definition

post_presence_definitions is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
| **body** | [**OrganizationPresenceDefinition**](OrganizationPresenceDefinition.html)| The Presence Definition to create |  |
{: class="table table-striped"}

### Return type

[**OrganizationPresenceDefinition**](OrganizationPresenceDefinition.html)

<a name="post_presence_sources"></a>

## [**Source**](Source.html) post_presence_sources(body)



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
| **body** | [**Source**](Source.html)| The Presence Source to create |  |
{: class="table table-striped"}

### Return type

[**Source**](Source.html)

<a name="post_presencedefinitions"></a>

## [**OrganizationPresence**](OrganizationPresence.html) post_presencedefinitions(body)



Create a Presence Definition

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
    # Create a Presence Definition
    api_response = api_instance.post_presencedefinitions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->post_presencedefinitions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OrganizationPresence**](OrganizationPresence.html)| The Presence Definition to create |  |
{: class="table table-striped"}

### Return type

[**OrganizationPresence**](OrganizationPresence.html)

<a name="put_presence_definition"></a>

## [**OrganizationPresenceDefinition**](OrganizationPresenceDefinition.html) put_presence_definition(definition_id, body)



Update a Presence Definition

put_presence_definition is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
| **body** | [**OrganizationPresenceDefinition**](OrganizationPresenceDefinition.html)| The updated Presence Definition |  |
{: class="table table-striped"}

### Return type

[**OrganizationPresenceDefinition**](OrganizationPresenceDefinition.html)

<a name="put_presence_settings"></a>

## [**PresenceSettings**](PresenceSettings.html) put_presence_settings(body)



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
| **body** | [**PresenceSettings**](PresenceSettings.html)| Presence Settings |  |
{: class="table table-striped"}

### Return type

[**PresenceSettings**](PresenceSettings.html)

<a name="put_presence_source"></a>

## [**Source**](Source.html) put_presence_source(source_id, body)



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
| **body** | [**Source**](Source.html)| The updated Presence Source |  |
{: class="table table-striped"}

### Return type

[**Source**](Source.html)

<a name="put_presence_user_primarysource"></a>

## [**UserPrimarySource**](UserPrimarySource.html) put_presence_user_primarysource(user_id, body)



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
| **body** | [**UserPrimarySource**](UserPrimarySource.html)| Primary Source |  |
{: class="table table-striped"}

### Return type

[**UserPrimarySource**](UserPrimarySource.html)

<a name="put_presencedefinition"></a>

## [**OrganizationPresence**](OrganizationPresence.html) put_presencedefinition(presence_id, body)



Update a Presence Definition

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
    # Update a Presence Definition
    api_response = api_instance.put_presencedefinition(presence_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresenceApi->put_presencedefinition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **presence_id** | **str**| Organization Presence ID |  |
| **body** | [**OrganizationPresence**](OrganizationPresence.html)| The OrganizationPresence to update |  |
{: class="table table-striped"}

### Return type

[**OrganizationPresence**](OrganizationPresence.html)

<a name="put_users_presences_bulk"></a>

## [**list[UserPresence]**](UserPresence.html) put_users_presences_bulk(body)



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
| **body** | [**list[MutableUserPresence]**](MutableUserPresence.html)| List of User presences |  |
{: class="table table-striped"}

### Return type

[**list[UserPresence]**](UserPresence.html)


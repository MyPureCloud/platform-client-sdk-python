---
title: ChatApi
---

## PureCloudPlatformClientV2.ChatApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_chat_settings**](ChatApi.html#get_chat_settings) | Get Chat Settings.|
|[**get_chats_settings**](ChatApi.html#get_chats_settings) | Get Chat Settings.|
|[**patch_chat_settings**](ChatApi.html#patch_chat_settings) | Patch Chat Settings.|
|[**patch_chats_settings**](ChatApi.html#patch_chats_settings) | Patch Chat Settings.|
|[**put_chat_settings**](ChatApi.html#put_chat_settings) | Update Chat Settings.|
|[**put_chats_settings**](ChatApi.html#put_chats_settings) | Update Chat Settings.|
{: class="table table-striped"}

<a name="get_chat_settings"></a>

## [**ChatSettings**](ChatSettings.html) get_chat_settings()

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get Chat Settings.

This route is deprecated, please use /chats/settings instead

Wraps GET /api/v2/chat/settings 

Requires ANY permissions: 

* chat:setting:view
* chat:setting:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ChatApi()

try:
    # Get Chat Settings.
    api_response = api_instance.get_chat_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chat_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**ChatSettings**](ChatSettings.html)

<a name="get_chats_settings"></a>

## [**ChatSettings**](ChatSettings.html) get_chats_settings()



Get Chat Settings.

Wraps GET /api/v2/chats/settings 

Requires ANY permissions: 

* chat:setting:view
* chat:setting:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ChatApi()

try:
    # Get Chat Settings.
    api_response = api_instance.get_chats_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chats_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**ChatSettings**](ChatSettings.html)

<a name="patch_chat_settings"></a>

## [**ChatSettings**](ChatSettings.html) patch_chat_settings(body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Patch Chat Settings.

This route is deprecated, please use /chats/settings instead

Wraps PATCH /api/v2/chat/settings 

Requires ANY permissions: 

* chat:setting:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ChatApi()
body = PureCloudPlatformClientV2.ChatSettings() # ChatSettings | Chat

try:
    # Patch Chat Settings.
    api_response = api_instance.patch_chat_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->patch_chat_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ChatSettings**](ChatSettings.html)| Chat |  |
{: class="table table-striped"}

### Return type

[**ChatSettings**](ChatSettings.html)

<a name="patch_chats_settings"></a>

## [**ChatSettings**](ChatSettings.html) patch_chats_settings(body)



Patch Chat Settings.

Wraps PATCH /api/v2/chats/settings 

Requires ANY permissions: 

* chat:setting:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ChatApi()
body = PureCloudPlatformClientV2.ChatSettings() # ChatSettings | Chat

try:
    # Patch Chat Settings.
    api_response = api_instance.patch_chats_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->patch_chats_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ChatSettings**](ChatSettings.html)| Chat |  |
{: class="table table-striped"}

### Return type

[**ChatSettings**](ChatSettings.html)

<a name="put_chat_settings"></a>

## [**ChatSettings**](ChatSettings.html) put_chat_settings(body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update Chat Settings.

This route is deprecated, please use /chats/settings instead

Wraps PUT /api/v2/chat/settings 

Requires ANY permissions: 

* chat:setting:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ChatApi()
body = PureCloudPlatformClientV2.ChatSettings() # ChatSettings | Chat

try:
    # Update Chat Settings.
    api_response = api_instance.put_chat_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->put_chat_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ChatSettings**](ChatSettings.html)| Chat |  |
{: class="table table-striped"}

### Return type

[**ChatSettings**](ChatSettings.html)

<a name="put_chats_settings"></a>

## [**ChatSettings**](ChatSettings.html) put_chats_settings(body)



Update Chat Settings.

Wraps PUT /api/v2/chats/settings 

Requires ANY permissions: 

* chat:setting:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ChatApi()
body = PureCloudPlatformClientV2.ChatSettings() # ChatSettings | Chat

try:
    # Update Chat Settings.
    api_response = api_instance.put_chats_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->put_chats_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ChatSettings**](ChatSettings.html)| Chat |  |
{: class="table table-striped"}

### Return type

[**ChatSettings**](ChatSettings.html)


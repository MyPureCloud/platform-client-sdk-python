---
title: ChatApi
---

## PureCloudPlatformClientV2.ChatApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_chats_room_message**](ChatApi.html#delete_chats_room_message) | Delete a message in a room|
|[**delete_chats_room_participant**](ChatApi.html#delete_chats_room_participant) | Remove a user from a room.|
|[**delete_chats_room_pinnedmessage**](ChatApi.html#delete_chats_room_pinnedmessage) | Remove a pinned message from a room|
|[**delete_chats_user_message**](ChatApi.html#delete_chats_user_message) | Delete a message to a user|
|[**get_chats_message**](ChatApi.html#get_chats_message) | Get a message|
|[**get_chats_room**](ChatApi.html#get_chats_room) | Get a room|
|[**get_chats_room_message**](ChatApi.html#get_chats_room_message) | Get messages by id(s) from a room|
|[**get_chats_room_messages**](ChatApi.html#get_chats_room_messages) | Get a room&#39;s message history|
|[**get_chats_settings**](ChatApi.html#get_chats_settings) | Get Chat Settings.|
|[**get_chats_thread_messages**](ChatApi.html#get_chats_thread_messages) | Get history by thread|
|[**get_chats_user_message**](ChatApi.html#get_chats_user_message) | Get messages by id(s) from a 1on1|
|[**get_chats_user_messages**](ChatApi.html#get_chats_user_messages) | Get 1on1 History between a user|
|[**get_chats_user_settings**](ChatApi.html#get_chats_user_settings) | Get a user&#39;s chat settings|
|[**patch_chats_room**](ChatApi.html#patch_chats_room) | Set properties for a room|
|[**patch_chats_room_message**](ChatApi.html#patch_chats_room_message) | Edit a message in a room|
|[**patch_chats_settings**](ChatApi.html#patch_chats_settings) | Patch Chat Settings.|
|[**patch_chats_user_message**](ChatApi.html#patch_chats_user_message) | Edit a message to a user|
|[**patch_chats_user_settings**](ChatApi.html#patch_chats_user_settings) | Update a user&#39;s chat settings|
|[**post_chats_room_messages**](ChatApi.html#post_chats_room_messages) | Send a message to a room|
|[**post_chats_room_participant**](ChatApi.html#post_chats_room_participant) | Join a room|
|[**post_chats_room_pinnedmessages**](ChatApi.html#post_chats_room_pinnedmessages) | Add pinned messages for a room, up to a maximum of 5 pinned messages|
|[**post_chats_rooms**](ChatApi.html#post_chats_rooms) | Create an adhoc room|
|[**post_chats_user_messages**](ChatApi.html#post_chats_user_messages) | Send a message to a user|
|[**put_chats_settings**](ChatApi.html#put_chats_settings) | Update Chat Settings.|
{: class="table table-striped"}

<a name="delete_chats_room_message"></a>

##  delete_chats_room_message(room_jid, message_id)



Delete a message in a room

delete_chats_room_message is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/chats/rooms/{roomJid}/messages/{messageId} 

Requires ANY permissions: 

* chat:chat:access
* chat:roomMessage:delete

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
room_jid = 'room_jid_example' # str | roomId
message_id = 'message_id_example' # str | messageId

try:
    # Delete a message in a room
    api_instance.delete_chats_room_message(room_jid, message_id)
except ApiException as e:
    print("Exception when calling ChatApi->delete_chats_room_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomId |  |
| **message_id** | **str**| messageId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_chats_room_participant"></a>

##  delete_chats_room_participant(room_jid, user_id)



Remove a user from a room.

delete_chats_room_participant is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/chats/rooms/{roomJid}/participants/{userId} 

Requires ANY permissions: 

* chat:chat:access
* chat:participant:delete

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
room_jid = 'room_jid_example' # str | roomJid
user_id = 'user_id_example' # str | userId

try:
    # Remove a user from a room.
    api_instance.delete_chats_room_participant(room_jid, user_id)
except ApiException as e:
    print("Exception when calling ChatApi->delete_chats_room_participant: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomJid |  |
| **user_id** | **str**| userId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_chats_room_pinnedmessage"></a>

##  delete_chats_room_pinnedmessage(room_jid, pinned_message_id)



Remove a pinned message from a room

delete_chats_room_pinnedmessage is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/chats/rooms/{roomJid}/pinnedmessages/{pinnedMessageId} 

Requires ANY permissions: 

* chat:chat:access
* chat:room:edit

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
room_jid = 'room_jid_example' # str | roomJid
pinned_message_id = 'pinned_message_id_example' # str | pinnedMessageId

try:
    # Remove a pinned message from a room
    api_instance.delete_chats_room_pinnedmessage(room_jid, pinned_message_id)
except ApiException as e:
    print("Exception when calling ChatApi->delete_chats_room_pinnedmessage: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomJid |  |
| **pinned_message_id** | **str**| pinnedMessageId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_chats_user_message"></a>

##  delete_chats_user_message(user_id, message_id)



Delete a message to a user

delete_chats_user_message is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/chats/users/{userId}/messages/{messageId} 

Requires ANY permissions: 

* chat:chat:access
* chat:1on1Message:delete

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
user_id = 'user_id_example' # str | userId
message_id = 'message_id_example' # str | messageId

try:
    # Delete a message to a user
    api_instance.delete_chats_user_message(user_id, message_id)
except ApiException as e:
    print("Exception when calling ChatApi->delete_chats_user_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| userId |  |
| **message_id** | **str**| messageId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_chats_message"></a>

## [**ChatMessageResponse**](ChatMessageResponse.html) get_chats_message(message_id)



Get a message

get_chats_message is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/chats/messages/{messageId} 

Requires ANY permissions: 

* chat:chat:access
* chat:1on1Message:view
* chat:room:view

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
message_id = 'message_id_example' # str | messageId

try:
    # Get a message
    api_response = api_instance.get_chats_message(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chats_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_id** | **str**| messageId |  |
{: class="table table-striped"}

### Return type

[**ChatMessageResponse**](ChatMessageResponse.html)

<a name="get_chats_room"></a>

## [**Room**](Room.html) get_chats_room(room_jid)



Get a room

get_chats_room is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/chats/rooms/{roomJid} 

Requires ANY permissions: 

* chat:chat:access
* chat:room:view

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
room_jid = 'room_jid_example' # str | roomJid

try:
    # Get a room
    api_response = api_instance.get_chats_room(room_jid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chats_room: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomJid |  |
{: class="table table-striped"}

### Return type

[**Room**](Room.html)

<a name="get_chats_room_message"></a>

## [**ChatMessageEntityListing**](ChatMessageEntityListing.html) get_chats_room_message(room_jid, message_ids)



Get messages by id(s) from a room

get_chats_room_message is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/chats/rooms/{roomJid}/messages/{messageIds} 

Requires ANY permissions: 

* chat:chat:access
* chat:room:view

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
room_jid = 'room_jid_example' # str | roomJid
message_ids = 'message_ids_example' # str | messageIds, comma separated

try:
    # Get messages by id(s) from a room
    api_response = api_instance.get_chats_room_message(room_jid, message_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chats_room_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomJid |  |
| **message_ids** | **str**| messageIds, comma separated |  |
{: class="table table-striped"}

### Return type

[**ChatMessageEntityListing**](ChatMessageEntityListing.html)

<a name="get_chats_room_messages"></a>

## [**ChatMessageEntityListing**](ChatMessageEntityListing.html) get_chats_room_messages(room_jid, limit=limit, before=before, after=after)



Get a room's message history

get_chats_room_messages is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/chats/rooms/{roomJid}/messages 

Requires ANY permissions: 

* chat:chat:access
* chat:room:view

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
room_jid = 'room_jid_example' # str | roomJid
limit = 'limit_example' # str | The maximum number of messages to retrieve (optional)
before = 'before_example' # str | The cutoff date for messages to retrieve (optional)
after = 'after_example' # str | The beginning date for messages to retrieve (optional)

try:
    # Get a room's message history
    api_response = api_instance.get_chats_room_messages(room_jid, limit=limit, before=before, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chats_room_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomJid |  |
| **limit** | **str**| The maximum number of messages to retrieve | [optional]  |
| **before** | **str**| The cutoff date for messages to retrieve | [optional]  |
| **after** | **str**| The beginning date for messages to retrieve | [optional]  |
{: class="table table-striped"}

### Return type

[**ChatMessageEntityListing**](ChatMessageEntityListing.html)

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

<a name="get_chats_thread_messages"></a>

## [**ChatMessageEntityListing**](ChatMessageEntityListing.html) get_chats_thread_messages(thread_id, limit=limit, before=before, after=after)



Get history by thread

get_chats_thread_messages is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/chats/threads/{threadId}/messages 

Requires ANY permissions: 

* chat:chat:access
* chat:room:view

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
thread_id = 'thread_id_example' # str | threadId
limit = 'limit_example' # str | The maximum number of messages to retrieve (optional)
before = 'before_example' # str | The cutoff date for messages to retrieve (optional)
after = 'after_example' # str | The beginning date for messages to retrieve (optional)

try:
    # Get history by thread
    api_response = api_instance.get_chats_thread_messages(thread_id, limit=limit, before=before, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chats_thread_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **thread_id** | **str**| threadId |  |
| **limit** | **str**| The maximum number of messages to retrieve | [optional]  |
| **before** | **str**| The cutoff date for messages to retrieve | [optional]  |
| **after** | **str**| The beginning date for messages to retrieve | [optional]  |
{: class="table table-striped"}

### Return type

[**ChatMessageEntityListing**](ChatMessageEntityListing.html)

<a name="get_chats_user_message"></a>

## [**ChatMessageEntityListing**](ChatMessageEntityListing.html) get_chats_user_message(user_id, message_ids)



Get messages by id(s) from a 1on1

get_chats_user_message is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/chats/users/{userId}/messages/{messageIds} 

Requires ANY permissions: 

* chat:chat:access
* chat:1on1Message:view

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
user_id = 'user_id_example' # str | userId
message_ids = 'message_ids_example' # str | messageIds, comma separated

try:
    # Get messages by id(s) from a 1on1
    api_response = api_instance.get_chats_user_message(user_id, message_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chats_user_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| userId |  |
| **message_ids** | **str**| messageIds, comma separated |  |
{: class="table table-striped"}

### Return type

[**ChatMessageEntityListing**](ChatMessageEntityListing.html)

<a name="get_chats_user_messages"></a>

## [**ChatMessageResponse**](ChatMessageResponse.html) get_chats_user_messages(user_id, limit=limit, before=before, after=after)



Get 1on1 History between a user

get_chats_user_messages is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/chats/users/{userId}/messages 

Requires ANY permissions: 

* chat:chat:access
* chat:1on1Message:view

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
user_id = 'user_id_example' # str | userId
limit = 'limit_example' # str | The maximum number of messages to retrieve (optional)
before = 'before_example' # str | The cutoff date for messages to retrieve (optional)
after = 'after_example' # str | The beginning date for messages to retrieve (optional)

try:
    # Get 1on1 History between a user
    api_response = api_instance.get_chats_user_messages(user_id, limit=limit, before=before, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chats_user_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| userId |  |
| **limit** | **str**| The maximum number of messages to retrieve | [optional]  |
| **before** | **str**| The cutoff date for messages to retrieve | [optional]  |
| **after** | **str**| The beginning date for messages to retrieve | [optional]  |
{: class="table table-striped"}

### Return type

[**ChatMessageResponse**](ChatMessageResponse.html)

<a name="get_chats_user_settings"></a>

## [**ChatUserSettings**](ChatUserSettings.html) get_chats_user_settings(user_id)



Get a user's chat settings

get_chats_user_settings is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/chats/users/{userId}/settings 

Requires ANY permissions: 

* chat:usersettings:view
* chat:setting:view

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
user_id = 'user_id_example' # str | User ID

try:
    # Get a user's chat settings
    api_response = api_instance.get_chats_user_settings(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chats_user_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

[**ChatUserSettings**](ChatUserSettings.html)

<a name="patch_chats_room"></a>

##  patch_chats_room(room_jid, body)



Set properties for a room

patch_chats_room is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/chats/rooms/{roomJid} 

Requires ANY permissions: 

* chat:chat:access
* chat:room:edit

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
room_jid = 'room_jid_example' # str | roomJid
body = PureCloudPlatformClientV2.RoomUpdateRequest() # RoomUpdateRequest | Room properties

try:
    # Set properties for a room
    api_instance.patch_chats_room(room_jid, body)
except ApiException as e:
    print("Exception when calling ChatApi->patch_chats_room: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomJid |  |
| **body** | [**RoomUpdateRequest**](RoomUpdateRequest.html)| Room properties |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_chats_room_message"></a>

## [**ChatSendMessageResponse**](ChatSendMessageResponse.html) patch_chats_room_message(room_jid, message_id, body)



Edit a message in a room

patch_chats_room_message is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/chats/rooms/{roomJid}/messages/{messageId} 

Requires ANY permissions: 

* chat:chat:access
* chat:roomMessage:edit

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
room_jid = 'room_jid_example' # str | roomId
message_id = 'message_id_example' # str | messageId
body = PureCloudPlatformClientV2.SendMessageBody() # SendMessageBody | messageBody

try:
    # Edit a message in a room
    api_response = api_instance.patch_chats_room_message(room_jid, message_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->patch_chats_room_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomId |  |
| **message_id** | **str**| messageId |  |
| **body** | [**SendMessageBody**](SendMessageBody.html)| messageBody |  |
{: class="table table-striped"}

### Return type

[**ChatSendMessageResponse**](ChatSendMessageResponse.html)

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

<a name="patch_chats_user_message"></a>

## [**ChatSendMessageResponse**](ChatSendMessageResponse.html) patch_chats_user_message(user_id, message_id, body)



Edit a message to a user

patch_chats_user_message is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/chats/users/{userId}/messages/{messageId} 

Requires ANY permissions: 

* chat:chat:access
* chat:1on1Message:view

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
user_id = 'user_id_example' # str | userId
message_id = 'message_id_example' # str | messageId
body = PureCloudPlatformClientV2.SendMessageBody() # SendMessageBody | message body

try:
    # Edit a message to a user
    api_response = api_instance.patch_chats_user_message(user_id, message_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->patch_chats_user_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| userId |  |
| **message_id** | **str**| messageId |  |
| **body** | [**SendMessageBody**](SendMessageBody.html)| message body |  |
{: class="table table-striped"}

### Return type

[**ChatSendMessageResponse**](ChatSendMessageResponse.html)

<a name="patch_chats_user_settings"></a>

## [**ChatUserSettings**](ChatUserSettings.html) patch_chats_user_settings(user_id, body)



Update a user's chat settings

patch_chats_user_settings is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/chats/users/{userId}/settings 

Requires ANY permissions: 

* chat:usersettings:edit
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
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.ChatUserSettings() # ChatUserSettings | 

try:
    # Update a user's chat settings
    api_response = api_instance.patch_chats_user_settings(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->patch_chats_user_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**ChatUserSettings**](ChatUserSettings.html)|  |  |
{: class="table table-striped"}

### Return type

[**ChatUserSettings**](ChatUserSettings.html)

<a name="post_chats_room_messages"></a>

## [**ChatSendMessageResponse**](ChatSendMessageResponse.html) post_chats_room_messages(room_jid, body)



Send a message to a room

post_chats_room_messages is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/chats/rooms/{roomJid}/messages 

Requires ANY permissions: 

* chat:chat:access
* chat:roomMessage:add

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
room_jid = 'room_jid_example' # str | roomId
body = PureCloudPlatformClientV2.SendMessageBody() # SendMessageBody | messageBody

try:
    # Send a message to a room
    api_response = api_instance.post_chats_room_messages(room_jid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->post_chats_room_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomId |  |
| **body** | [**SendMessageBody**](SendMessageBody.html)| messageBody |  |
{: class="table table-striped"}

### Return type

[**ChatSendMessageResponse**](ChatSendMessageResponse.html)

<a name="post_chats_room_participant"></a>

##  post_chats_room_participant(room_jid, user_id)



Join a room

post_chats_room_participant is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/chats/rooms/{roomJid}/participants/{userId} 

Requires ANY permissions: 

* chat:chat:access
* chat:participant:add

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
room_jid = 'room_jid_example' # str | roomJid
user_id = 'user_id_example' # str | userId

try:
    # Join a room
    api_instance.post_chats_room_participant(room_jid, user_id)
except ApiException as e:
    print("Exception when calling ChatApi->post_chats_room_participant: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomJid |  |
| **user_id** | **str**| userId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_chats_room_pinnedmessages"></a>

##  post_chats_room_pinnedmessages(room_jid, body)



Add pinned messages for a room, up to a maximum of 5 pinned messages

post_chats_room_pinnedmessages is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/chats/rooms/{roomJid}/pinnedmessages 

Requires ANY permissions: 

* chat:chat:access
* chat:room:edit

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
room_jid = 'room_jid_example' # str | roomJid
body = PureCloudPlatformClientV2.PinnedMessageRequest() # PinnedMessageRequest | Pinned Message Ids

try:
    # Add pinned messages for a room, up to a maximum of 5 pinned messages
    api_instance.post_chats_room_pinnedmessages(room_jid, body)
except ApiException as e:
    print("Exception when calling ChatApi->post_chats_room_pinnedmessages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomJid |  |
| **body** | [**PinnedMessageRequest**](PinnedMessageRequest.html)| Pinned Message Ids |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_chats_rooms"></a>

## [**CreateRoomResponse**](CreateRoomResponse.html) post_chats_rooms(body)



Create an adhoc room

post_chats_rooms is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/chats/rooms 

Requires ANY permissions: 

* chat:chat:access
* chat:room:add

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
body = PureCloudPlatformClientV2.CreateRoomRequest() # CreateRoomRequest | Room properties

try:
    # Create an adhoc room
    api_response = api_instance.post_chats_rooms(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->post_chats_rooms: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateRoomRequest**](CreateRoomRequest.html)| Room properties |  |
{: class="table table-striped"}

### Return type

[**CreateRoomResponse**](CreateRoomResponse.html)

<a name="post_chats_user_messages"></a>

## [**ChatSendMessageResponse**](ChatSendMessageResponse.html) post_chats_user_messages(user_id, body)



Send a message to a user

post_chats_user_messages is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/chats/users/{userId}/messages 

Requires ANY permissions: 

* chat:chat:access
* chat:1on1Message:add

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
user_id = 'user_id_example' # str | userId
body = PureCloudPlatformClientV2.SendMessageBody() # SendMessageBody | message body

try:
    # Send a message to a user
    api_response = api_instance.post_chats_user_messages(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->post_chats_user_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| userId |  |
| **body** | [**SendMessageBody**](SendMessageBody.html)| message body |  |
{: class="table table-striped"}

### Return type

[**ChatSendMessageResponse**](ChatSendMessageResponse.html)

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


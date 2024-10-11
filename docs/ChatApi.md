# ChatApi

## PureCloudPlatformClientV2.ChatApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_chats_room_message**](#delete_chats_room_message) | Delete a message in a room|
|[**delete_chats_room_messages_pin**](#delete_chats_room_messages_pin) | Remove a pinned message from a room|
|[**delete_chats_room_participant**](#delete_chats_room_participant) | Remove a user from a room.|
|[**delete_chats_user_message**](#delete_chats_user_message) | Delete a message to a user|
|[**delete_chats_user_messages_pin**](#delete_chats_user_messages_pin) | Remove a pinned message from a 1on1|
|[**get_chats_message**](#get_chats_message) | Get a message|
|[**get_chats_room**](#get_chats_room) | Get a room|
|[**get_chats_room_message**](#get_chats_room_message) | Get messages by id(s) from a room|
|[**get_chats_room_messages**](#get_chats_room_messages) | Get a room&#39;s message history|
|[**get_chats_room_participant**](#get_chats_room_participant) | Get a room participant|
|[**get_chats_room_participants**](#get_chats_room_participants) | Get room participants in a room|
|[**get_chats_settings**](#get_chats_settings) | Get Chat Settings.|
|[**get_chats_thread_messages**](#get_chats_thread_messages) | Get history by thread|
|[**get_chats_user**](#get_chats_user) | Get information for a 1on1|
|[**get_chats_user_message**](#get_chats_user_message) | Get messages by id(s) from a 1on1|
|[**get_chats_user_messages**](#get_chats_user_messages) | Get 1on1 History between a user|
|[**get_chats_user_settings**](#get_chats_user_settings) | Get a user&#39;s chat settings|
|[**get_chats_users_me_settings**](#get_chats_users_me_settings) | Get a user&#39;s chat settings|
|[**patch_chats_room**](#patch_chats_room) | Set properties for a room|
|[**patch_chats_room_message**](#patch_chats_room_message) | Edit a message in a room|
|[**patch_chats_settings**](#patch_chats_settings) | Patch Chat Settings.|
|[**patch_chats_user_message**](#patch_chats_user_message) | Edit a message to a user|
|[**patch_chats_user_settings**](#patch_chats_user_settings) | Update a user&#39;s chat settings|
|[**patch_chats_users_me_settings**](#patch_chats_users_me_settings) | Update a user&#39;s chat settings|
|[**post_chats_room_messages**](#post_chats_room_messages) | Send a message to a room|
|[**post_chats_room_messages_pins**](#post_chats_room_messages_pins) | Add pinned messages for a room, up to a maximum of 5 pinned messages|
|[**post_chats_room_participant**](#post_chats_room_participant) | Join a room|
|[**post_chats_rooms**](#post_chats_rooms) | Create an adhoc room|
|[**post_chats_user_messages**](#post_chats_user_messages) | Send a message to a user|
|[**post_chats_user_messages_pins**](#post_chats_user_messages_pins) | Add pinned messages for a 1on1, up to a maximum of 5 pinned messages|
|[**put_chats_message_reactions**](#put_chats_message_reactions) | Update reactions to a message|
|[**put_chats_settings**](#put_chats_settings) | Update Chat Settings.|



## delete_chats_room_message

>  delete_chats_room_message(room_jid, message_id)


Delete a message in a room

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

### Return type

void (empty response body)


## delete_chats_room_messages_pin

>  delete_chats_room_messages_pin(room_jid, pinned_message_id)


Remove a pinned message from a room

Wraps DELETE /api/v2/chats/rooms/{roomJid}/messages/pins/{pinnedMessageId} 

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
    api_instance.delete_chats_room_messages_pin(room_jid, pinned_message_id)
except ApiException as e:
    print("Exception when calling ChatApi->delete_chats_room_messages_pin: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomJid |  |
| **pinned_message_id** | **str**| pinnedMessageId |  |

### Return type

void (empty response body)


## delete_chats_room_participant

>  delete_chats_room_participant(room_jid, user_id)


Remove a user from a room.

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

### Return type

void (empty response body)


## delete_chats_user_message

>  delete_chats_user_message(user_id, message_id)


Delete a message to a user

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

### Return type

void (empty response body)


## delete_chats_user_messages_pin

>  delete_chats_user_messages_pin(user_id, pinned_message_id)


Remove a pinned message from a 1on1

delete_chats_user_messages_pin is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/chats/users/{userId}/messages/pins/{pinnedMessageId} 

Requires ANY permissions: 

* chat:chat:access
* chat:1on1:edit

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
pinned_message_id = 'pinned_message_id_example' # str | pinnedMessageId

try:
    # Remove a pinned message from a 1on1
    api_instance.delete_chats_user_messages_pin(user_id, pinned_message_id)
except ApiException as e:
    print("Exception when calling ChatApi->delete_chats_user_messages_pin: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| userId |  |
| **pinned_message_id** | **str**| pinnedMessageId |  |

### Return type

void (empty response body)


## get_chats_message

> [**ChatMessageResponse**](ChatMessageResponse) get_chats_message(message_id)


Get a message

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

### Return type

[**ChatMessageResponse**](ChatMessageResponse)


## get_chats_room

> [**Room**](Room) get_chats_room(room_jid)


Get a room

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

### Return type

[**Room**](Room)


## get_chats_room_message

> [**ChatMessageEntityListing**](ChatMessageEntityListing) get_chats_room_message(room_jid, message_ids)


Get messages by id(s) from a room

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

### Return type

[**ChatMessageEntityListing**](ChatMessageEntityListing)


## get_chats_room_messages

> [**ChatMessageEntityListing**](ChatMessageEntityListing) get_chats_room_messages(room_jid, limit=limit, before=before, after=after)


Get a room's message history

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

### Return type

[**ChatMessageEntityListing**](ChatMessageEntityListing)


## get_chats_room_participant

> [**RoomParticipant**](RoomParticipant) get_chats_room_participant(room_jid, participant_jid)


Get a room participant

Wraps GET /api/v2/chats/rooms/{roomJid}/participants/{participantJid} 

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
api_instance = PureCloudPlatformClientV2.ChatApi()
room_jid = 'room_jid_example' # str | roomJid
participant_jid = 'participant_jid_example' # str | participantJid

try:
    # Get a room participant
    api_response = api_instance.get_chats_room_participant(room_jid, participant_jid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chats_room_participant: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomJid |  |
| **participant_jid** | **str**| participantJid |  |

### Return type

[**RoomParticipant**](RoomParticipant)


## get_chats_room_participants

> [**RoomParticipantsResponse**](RoomParticipantsResponse) get_chats_room_participants(room_jid)


Get room participants in a room

Wraps GET /api/v2/chats/rooms/{roomJid}/participants 

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
    # Get room participants in a room
    api_response = api_instance.get_chats_room_participants(room_jid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chats_room_participants: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomJid |  |

### Return type

[**RoomParticipantsResponse**](RoomParticipantsResponse)


## get_chats_settings

> [**ChatSettings**](ChatSettings) get_chats_settings()


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

[**ChatSettings**](ChatSettings)


## get_chats_thread_messages

> [**ChatMessageEntityListing**](ChatMessageEntityListing) get_chats_thread_messages(thread_id, limit=limit, before=before, after=after)


Get history by thread

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

### Return type

[**ChatMessageEntityListing**](ChatMessageEntityListing)


## get_chats_user

> [**OneOnOne**](OneOnOne) get_chats_user(user_id)


Get information for a 1on1

get_chats_user is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/chats/users/{userId} 

Requires ANY permissions: 

* chat:chat:access
* chat:1on1:view

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

try:
    # Get information for a 1on1
    api_response = api_instance.get_chats_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chats_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| userId |  |

### Return type

[**OneOnOne**](OneOnOne)


## get_chats_user_message

> [**ChatMessageEntityListing**](ChatMessageEntityListing) get_chats_user_message(user_id, message_ids)


Get messages by id(s) from a 1on1

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

### Return type

[**ChatMessageEntityListing**](ChatMessageEntityListing)


## get_chats_user_messages

> [**ChatMessageResponse**](ChatMessageResponse) get_chats_user_messages(user_id, limit=limit, before=before, after=after)


Get 1on1 History between a user

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

### Return type

[**ChatMessageResponse**](ChatMessageResponse)


## get_chats_user_settings

> [**ChatUserSettings**](ChatUserSettings) get_chats_user_settings(user_id)


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

### Return type

[**ChatUserSettings**](ChatUserSettings)


## get_chats_users_me_settings

> [**ChatUserSettings**](ChatUserSettings) get_chats_users_me_settings()


Get a user's chat settings

get_chats_users_me_settings is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/chats/users/me/settings 

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
api_instance = PureCloudPlatformClientV2.ChatApi()

try:
    # Get a user's chat settings
    api_response = api_instance.get_chats_users_me_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chats_users_me_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**ChatUserSettings**](ChatUserSettings)


## patch_chats_room

>  patch_chats_room(room_jid, body)


Set properties for a room

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
| **body** | [**RoomUpdateRequest**](RoomUpdateRequest)| Room properties |  |

### Return type

void (empty response body)


## patch_chats_room_message

> [**ChatSendMessageResponse**](ChatSendMessageResponse) patch_chats_room_message(room_jid, message_id, body)


Edit a message in a room

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
| **body** | [**SendMessageBody**](SendMessageBody)| messageBody |  |

### Return type

[**ChatSendMessageResponse**](ChatSendMessageResponse)


## patch_chats_settings

> [**ChatSettings**](ChatSettings) patch_chats_settings(body)


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
| **body** | [**ChatSettings**](ChatSettings)| Chat |  |

### Return type

[**ChatSettings**](ChatSettings)


## patch_chats_user_message

> [**ChatSendMessageResponse**](ChatSendMessageResponse) patch_chats_user_message(user_id, message_id, body)


Edit a message to a user

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
| **body** | [**SendMessageBody**](SendMessageBody)| message body |  |

### Return type

[**ChatSendMessageResponse**](ChatSendMessageResponse)


## patch_chats_user_settings

> [**ChatUserSettings**](ChatUserSettings) patch_chats_user_settings(user_id, body)


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
| **body** | [**ChatUserSettings**](ChatUserSettings)|  |  |

### Return type

[**ChatUserSettings**](ChatUserSettings)


## patch_chats_users_me_settings

> [**ChatUserSettings**](ChatUserSettings) patch_chats_users_me_settings(body)


Update a user's chat settings

patch_chats_users_me_settings is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/chats/users/me/settings 

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
api_instance = PureCloudPlatformClientV2.ChatApi()
body = PureCloudPlatformClientV2.ChatUserSettings() # ChatUserSettings | 

try:
    # Update a user's chat settings
    api_response = api_instance.patch_chats_users_me_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->patch_chats_users_me_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ChatUserSettings**](ChatUserSettings)|  |  |

### Return type

[**ChatUserSettings**](ChatUserSettings)


## post_chats_room_messages

> [**ChatSendMessageResponse**](ChatSendMessageResponse) post_chats_room_messages(room_jid, body)


Send a message to a room

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
| **body** | [**SendMessageBody**](SendMessageBody)| messageBody |  |

### Return type

[**ChatSendMessageResponse**](ChatSendMessageResponse)


## post_chats_room_messages_pins

>  post_chats_room_messages_pins(room_jid, body)


Add pinned messages for a room, up to a maximum of 5 pinned messages

Wraps POST /api/v2/chats/rooms/{roomJid}/messages/pins 

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
    api_instance.post_chats_room_messages_pins(room_jid, body)
except ApiException as e:
    print("Exception when calling ChatApi->post_chats_room_messages_pins: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **room_jid** | **str**| roomJid |  |
| **body** | [**PinnedMessageRequest**](PinnedMessageRequest)| Pinned Message Ids |  |

### Return type

void (empty response body)


## post_chats_room_participant

>  post_chats_room_participant(room_jid, user_id)


Join a room

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

### Return type

void (empty response body)


## post_chats_rooms

> [**CreateRoomResponse**](CreateRoomResponse) post_chats_rooms(body)


Create an adhoc room

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
| **body** | [**CreateRoomRequest**](CreateRoomRequest)| Room properties |  |

### Return type

[**CreateRoomResponse**](CreateRoomResponse)


## post_chats_user_messages

> [**ChatSendMessageResponse**](ChatSendMessageResponse) post_chats_user_messages(user_id, body)


Send a message to a user

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
| **body** | [**SendMessageBody**](SendMessageBody)| message body |  |

### Return type

[**ChatSendMessageResponse**](ChatSendMessageResponse)


## post_chats_user_messages_pins

>  post_chats_user_messages_pins(user_id, body)


Add pinned messages for a 1on1, up to a maximum of 5 pinned messages

post_chats_user_messages_pins is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/chats/users/{userId}/messages/pins 

Requires ANY permissions: 

* chat:chat:access
* chat:1on1:edit

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
body = PureCloudPlatformClientV2.PinnedMessageRequest() # PinnedMessageRequest | Pinned Message Ids

try:
    # Add pinned messages for a 1on1, up to a maximum of 5 pinned messages
    api_instance.post_chats_user_messages_pins(user_id, body)
except ApiException as e:
    print("Exception when calling ChatApi->post_chats_user_messages_pins: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| userId |  |
| **body** | [**PinnedMessageRequest**](PinnedMessageRequest)| Pinned Message Ids |  |

### Return type

void (empty response body)


## put_chats_message_reactions

>  put_chats_message_reactions(message_id, body)


Update reactions to a message

Wraps PUT /api/v2/chats/messages/{messageId}/reactions 

Requires ANY permissions: 

* chat:chat:access
* chat:reactions:edit

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
body = PureCloudPlatformClientV2.ChatReactionUpdate() # ChatReactionUpdate | reactionUpdate

try:
    # Update reactions to a message
    api_instance.put_chats_message_reactions(message_id, body)
except ApiException as e:
    print("Exception when calling ChatApi->put_chats_message_reactions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_id** | **str**| messageId |  |
| **body** | [**ChatReactionUpdate**](ChatReactionUpdate)| reactionUpdate |  |

### Return type

void (empty response body)


## put_chats_settings

> [**ChatSettings**](ChatSettings) put_chats_settings(body)


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
| **body** | [**ChatSettings**](ChatSettings)| Chat |  |

### Return type

[**ChatSettings**](ChatSettings)


_PureCloudPlatformClientV2 213.0.0_

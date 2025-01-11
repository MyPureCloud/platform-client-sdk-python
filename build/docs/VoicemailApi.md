# VoicemailApi

## PureCloudPlatformClientV2.VoicemailApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_voicemail_message**](#delete_voicemail_message) | Delete a voicemail message.|
|[**delete_voicemail_messages**](#delete_voicemail_messages) | Delete all voicemail messages|
|[**get_voicemail_group_mailbox**](#get_voicemail_group_mailbox) | Get the group&#39;s mailbox information|
|[**get_voicemail_group_messages**](#get_voicemail_group_messages) | List voicemail messages|
|[**get_voicemail_group_policy**](#get_voicemail_group_policy) | Get a group&#39;s voicemail policy|
|[**get_voicemail_mailbox**](#get_voicemail_mailbox) | Get the current user&#39;s mailbox information|
|[**get_voicemail_me_mailbox**](#get_voicemail_me_mailbox) | Get the current user&#39;s mailbox information|
|[**get_voicemail_me_messages**](#get_voicemail_me_messages) | List voicemail messages|
|[**get_voicemail_me_policy**](#get_voicemail_me_policy) | Get the current user&#39;s voicemail policy|
|[**get_voicemail_message**](#get_voicemail_message) | Get a voicemail message|
|[**get_voicemail_message_media**](#get_voicemail_message_media) | Get media playback URI for this voicemail message|
|[**get_voicemail_messages**](#get_voicemail_messages) | List voicemail messages|
|[**get_voicemail_policy**](#get_voicemail_policy) | Get a policy|
|[**get_voicemail_queue_messages**](#get_voicemail_queue_messages) | List voicemail messages|
|[**get_voicemail_search**](#get_voicemail_search) | Search voicemails using the q64 value returned from a previous search|
|[**get_voicemail_user_mailbox**](#get_voicemail_user_mailbox) | Get a user&#39;s mailbox information|
|[**get_voicemail_user_messages**](#get_voicemail_user_messages) | List voicemail messages|
|[**get_voicemail_userpolicy**](#get_voicemail_userpolicy) | Get a user&#39;s voicemail policy|
|[**patch_voicemail_group_policy**](#patch_voicemail_group_policy) | Update a group&#39;s voicemail policy|
|[**patch_voicemail_me_policy**](#patch_voicemail_me_policy) | Update the current user&#39;s voicemail policy|
|[**patch_voicemail_message**](#patch_voicemail_message) | Update a voicemail message|
|[**patch_voicemail_userpolicy**](#patch_voicemail_userpolicy) | Update a user&#39;s voicemail policy|
|[**post_voicemail_messages**](#post_voicemail_messages) | Copy a voicemail message to a user or group|
|[**post_voicemail_search**](#post_voicemail_search) | Search voicemails|
|[**put_voicemail_message**](#put_voicemail_message) | Update a voicemail message|
|[**put_voicemail_policy**](#put_voicemail_policy) | Update a policy|
|[**put_voicemail_userpolicy**](#put_voicemail_userpolicy) | Update a user&#39;s voicemail policy|



## delete_voicemail_message

>  delete_voicemail_message(message_id)


Delete a voicemail message.

A user voicemail can only be deleted by its associated user. A group voicemail can only be deleted by a user that is a member of the group. A queue voicemail can only be deleted by a user with the acd voicemail delete permission.

Wraps DELETE /api/v2/voicemail/messages/{messageId} 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
message_id = 'message_id_example' # str | Message ID

try:
    # Delete a voicemail message.
    api_instance.delete_voicemail_message(message_id)
except ApiException as e:
    print("Exception when calling VoicemailApi->delete_voicemail_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_id** | **str**| Message ID |  |

### Return type

void (empty response body)


## delete_voicemail_messages

>  delete_voicemail_messages()


Delete all voicemail messages

Wraps DELETE /api/v2/voicemail/messages 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()

try:
    # Delete all voicemail messages
    api_instance.delete_voicemail_messages()
except ApiException as e:
    print("Exception when calling VoicemailApi->delete_voicemail_messages: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

void (empty response body)


## get_voicemail_group_mailbox

> [**VoicemailMailboxInfo**](VoicemailMailboxInfo) get_voicemail_group_mailbox(group_id)


Get the group's mailbox information

Wraps GET /api/v2/voicemail/groups/{groupId}/mailbox 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
group_id = 'group_id_example' # str | groupId

try:
    # Get the group's mailbox information
    api_response = api_instance.get_voicemail_group_mailbox(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_group_mailbox: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| groupId |  |

### Return type

[**VoicemailMailboxInfo**](VoicemailMailboxInfo)


## get_voicemail_group_messages

> [**VoicemailMessageEntityListing**](VoicemailMessageEntityListing) get_voicemail_group_messages(group_id, page_size=page_size, page_number=page_number)


List voicemail messages

Wraps GET /api/v2/voicemail/groups/{groupId}/messages 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
group_id = 'group_id_example' # str | Group ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # List voicemail messages
    api_response = api_instance.get_voicemail_group_messages(group_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_group_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**VoicemailMessageEntityListing**](VoicemailMessageEntityListing)


## get_voicemail_group_policy

> [**VoicemailGroupPolicy**](VoicemailGroupPolicy) get_voicemail_group_policy(group_id)


Get a group's voicemail policy

Wraps GET /api/v2/voicemail/groups/{groupId}/policy 

Requires ANY permissions: 

* directory:group:add
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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
group_id = 'group_id_example' # str | Group ID

try:
    # Get a group's voicemail policy
    api_response = api_instance.get_voicemail_group_policy(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_group_policy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |

### Return type

[**VoicemailGroupPolicy**](VoicemailGroupPolicy)


## get_voicemail_mailbox

> [**VoicemailMailboxInfo**](VoicemailMailboxInfo) get_voicemail_mailbox()


Get the current user's mailbox information

Wraps GET /api/v2/voicemail/mailbox 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()

try:
    # Get the current user's mailbox information
    api_response = api_instance.get_voicemail_mailbox()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_mailbox: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**VoicemailMailboxInfo**](VoicemailMailboxInfo)


## get_voicemail_me_mailbox

> [**VoicemailMailboxInfo**](VoicemailMailboxInfo) get_voicemail_me_mailbox()


Get the current user's mailbox information

Wraps GET /api/v2/voicemail/me/mailbox 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()

try:
    # Get the current user's mailbox information
    api_response = api_instance.get_voicemail_me_mailbox()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_me_mailbox: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**VoicemailMailboxInfo**](VoicemailMailboxInfo)


## get_voicemail_me_messages

> [**VoicemailMessageEntityListing**](VoicemailMessageEntityListing) get_voicemail_me_messages(page_size=page_size, page_number=page_number)


List voicemail messages

Wraps GET /api/v2/voicemail/me/messages 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # List voicemail messages
    api_response = api_instance.get_voicemail_me_messages(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_me_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**VoicemailMessageEntityListing**](VoicemailMessageEntityListing)


## get_voicemail_me_policy

> [**VoicemailUserPolicy**](VoicemailUserPolicy) get_voicemail_me_policy()


Get the current user's voicemail policy

Wraps GET /api/v2/voicemail/me/policy 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()

try:
    # Get the current user's voicemail policy
    api_response = api_instance.get_voicemail_me_policy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_me_policy: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**VoicemailUserPolicy**](VoicemailUserPolicy)


## get_voicemail_message

> [**VoicemailMessage**](VoicemailMessage) get_voicemail_message(message_id, expand=expand)


Get a voicemail message

Wraps GET /api/v2/voicemail/messages/{messageId} 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
message_id = 'message_id_example' # str | Message ID
expand = ['expand_example'] # list[str] | If the caller is a known user, which fields, if any, to expand (optional)

try:
    # Get a voicemail message
    api_response = api_instance.get_voicemail_message(message_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_id** | **str**| Message ID |  |
| **expand** | [**list[str]**](str)| If the caller is a known user, which fields, if any, to expand | [optional] <br />**Values**: callerUser.routingStatus, callerUser.primaryPresence, callerUser.conversationSummary, callerUser.outOfOffice, callerUser.geolocation, conversations, transcription |

### Return type

[**VoicemailMessage**](VoicemailMessage)


## get_voicemail_message_media

> [**VoicemailMediaInfo**](VoicemailMediaInfo) get_voicemail_message_media(message_id, format_id=format_id)


Get media playback URI for this voicemail message

Wraps GET /api/v2/voicemail/messages/{messageId}/media 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
message_id = 'message_id_example' # str | Message ID
format_id = ''WEBM'' # str | The desired media format. (optional) (default to 'WEBM')

try:
    # Get media playback URI for this voicemail message
    api_response = api_instance.get_voicemail_message_media(message_id, format_id=format_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_message_media: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_id** | **str**| Message ID |  |
| **format_id** | **str**| The desired media format. | [optional] [default to &#39;WEBM&#39;]<br />**Values**: WAV, WEBM, WAV_ULAW, OGG_VORBIS, OGG_OPUS, MP3, NONE |

### Return type

[**VoicemailMediaInfo**](VoicemailMediaInfo)


## get_voicemail_messages

> [**VoicemailMessageEntityListing**](VoicemailMessageEntityListing) get_voicemail_messages(ids=ids, expand=expand)


List voicemail messages

Wraps GET /api/v2/voicemail/messages 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
ids = 'ids_example' # str | An optional comma separated list of VoicemailMessage ids (optional)
expand = ['expand_example'] # list[str] | If the caller is a known user, which fields, if any, to expand (optional)

try:
    # List voicemail messages
    api_response = api_instance.get_voicemail_messages(ids=ids, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ids** | **str**| An optional comma separated list of VoicemailMessage ids | [optional]  |
| **expand** | [**list[str]**](str)| If the caller is a known user, which fields, if any, to expand | [optional] <br />**Values**: callerUser.routingStatus, callerUser.primaryPresence, callerUser.conversationSummary, callerUser.outOfOffice, callerUser.geolocation, conversations, transcription |

### Return type

[**VoicemailMessageEntityListing**](VoicemailMessageEntityListing)


## get_voicemail_policy

> [**VoicemailOrganizationPolicy**](VoicemailOrganizationPolicy) get_voicemail_policy()


Get a policy

Wraps GET /api/v2/voicemail/policy 

Requires ALL permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.VoicemailApi()

try:
    # Get a policy
    api_response = api_instance.get_voicemail_policy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_policy: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**VoicemailOrganizationPolicy**](VoicemailOrganizationPolicy)


## get_voicemail_queue_messages

> [**VoicemailMessageEntityListing**](VoicemailMessageEntityListing) get_voicemail_queue_messages(queue_id, page_size=page_size, page_number=page_number)


List voicemail messages

Wraps GET /api/v2/voicemail/queues/{queueId}/messages 

Requires ANY permissions: 

* voicemail:acdvoicemail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.VoicemailApi()
queue_id = 'queue_id_example' # str | Queue ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # List voicemail messages
    api_response = api_instance.get_voicemail_queue_messages(queue_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_queue_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **queue_id** | **str**| Queue ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**VoicemailMessageEntityListing**](VoicemailMessageEntityListing)


## get_voicemail_search

> [**VoicemailsSearchResponse**](VoicemailsSearchResponse) get_voicemail_search(q64, expand=expand)


Search voicemails using the q64 value returned from a previous search

Wraps GET /api/v2/voicemail/search 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | expand (optional)

try:
    # Search voicemails using the q64 value returned from a previous search
    api_response = api_instance.get_voicemail_search(q64, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str)| expand | [optional]  |

### Return type

[**VoicemailsSearchResponse**](VoicemailsSearchResponse)


## get_voicemail_user_mailbox

> [**VoicemailMailboxInfo**](VoicemailMailboxInfo) get_voicemail_user_mailbox(user_id)


Get a user's mailbox information

Wraps GET /api/v2/voicemail/users/{userId}/mailbox 

Requires ANY permissions: 

* voicemail:mailbox:viewOther

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.VoicemailApi()
user_id = 'user_id_example' # str | userId

try:
    # Get a user's mailbox information
    api_response = api_instance.get_voicemail_user_mailbox(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_user_mailbox: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| userId |  |

### Return type

[**VoicemailMailboxInfo**](VoicemailMailboxInfo)


## get_voicemail_user_messages

> [**VoicemailMessageEntityListing**](VoicemailMessageEntityListing) get_voicemail_user_messages(user_id, page_size=page_size, page_number=page_number)


List voicemail messages

Wraps GET /api/v2/voicemail/users/{userId}/messages 

Requires ANY permissions: 

* voicemail:voicemail:viewOther

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.VoicemailApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # List voicemail messages
    api_response = api_instance.get_voicemail_user_messages(user_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_user_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**VoicemailMessageEntityListing**](VoicemailMessageEntityListing)


## get_voicemail_userpolicy

> [**VoicemailUserPolicy**](VoicemailUserPolicy) get_voicemail_userpolicy(user_id)


Get a user's voicemail policy

Wraps GET /api/v2/voicemail/userpolicies/{userId} 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
user_id = 'user_id_example' # str | User ID

try:
    # Get a user's voicemail policy
    api_response = api_instance.get_voicemail_userpolicy(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_voicemail_userpolicy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |

### Return type

[**VoicemailUserPolicy**](VoicemailUserPolicy)


## patch_voicemail_group_policy

> [**VoicemailGroupPolicy**](VoicemailGroupPolicy) patch_voicemail_group_policy(group_id, body)


Update a group's voicemail policy

Wraps PATCH /api/v2/voicemail/groups/{groupId}/policy 

Requires ANY permissions: 

* directory:group:add
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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
group_id = 'group_id_example' # str | Group ID
body = PureCloudPlatformClientV2.VoicemailGroupPolicy() # VoicemailGroupPolicy | The group's voicemail policy

try:
    # Update a group's voicemail policy
    api_response = api_instance.patch_voicemail_group_policy(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->patch_voicemail_group_policy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |
| **body** | [**VoicemailGroupPolicy**](VoicemailGroupPolicy)| The group&#39;s voicemail policy |  |

### Return type

[**VoicemailGroupPolicy**](VoicemailGroupPolicy)


## patch_voicemail_me_policy

> [**VoicemailUserPolicy**](VoicemailUserPolicy) patch_voicemail_me_policy(body)


Update the current user's voicemail policy

Wraps PATCH /api/v2/voicemail/me/policy 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
body = PureCloudPlatformClientV2.VoicemailUserPolicy() # VoicemailUserPolicy | The user's voicemail policy

try:
    # Update the current user's voicemail policy
    api_response = api_instance.patch_voicemail_me_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->patch_voicemail_me_policy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**VoicemailUserPolicy**](VoicemailUserPolicy)| The user&#39;s voicemail policy |  |

### Return type

[**VoicemailUserPolicy**](VoicemailUserPolicy)


## patch_voicemail_message

> [**VoicemailMessage**](VoicemailMessage) patch_voicemail_message(message_id, body)


Update a voicemail message

A user voicemail can only be modified by its associated user. A group voicemail can only be modified by a user that is a member of the group. A queue voicemail can only be modified by a participant of the conversation the voicemail is associated with.

Wraps PATCH /api/v2/voicemail/messages/{messageId} 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
message_id = 'message_id_example' # str | Message ID
body = PureCloudPlatformClientV2.VoicemailMessage() # VoicemailMessage | VoicemailMessage

try:
    # Update a voicemail message
    api_response = api_instance.patch_voicemail_message(message_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->patch_voicemail_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_id** | **str**| Message ID |  |
| **body** | [**VoicemailMessage**](VoicemailMessage)| VoicemailMessage |  |

### Return type

[**VoicemailMessage**](VoicemailMessage)


## patch_voicemail_userpolicy

> [**VoicemailUserPolicy**](VoicemailUserPolicy) patch_voicemail_userpolicy(user_id, body)


Update a user's voicemail policy

Wraps PATCH /api/v2/voicemail/userpolicies/{userId} 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.VoicemailUserPolicy() # VoicemailUserPolicy | The user's voicemail policy

try:
    # Update a user's voicemail policy
    api_response = api_instance.patch_voicemail_userpolicy(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->patch_voicemail_userpolicy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**VoicemailUserPolicy**](VoicemailUserPolicy)| The user&#39;s voicemail policy |  |

### Return type

[**VoicemailUserPolicy**](VoicemailUserPolicy)


## post_voicemail_messages

> [**VoicemailMessage**](VoicemailMessage) post_voicemail_messages(body=body)


Copy a voicemail message to a user or group

Wraps POST /api/v2/voicemail/messages 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
body = PureCloudPlatformClientV2.CopyVoicemailMessage() # CopyVoicemailMessage |  (optional)

try:
    # Copy a voicemail message to a user or group
    api_response = api_instance.post_voicemail_messages(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->post_voicemail_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CopyVoicemailMessage**](CopyVoicemailMessage)|  | [optional]  |

### Return type

[**VoicemailMessage**](VoicemailMessage)


## post_voicemail_search

> [**VoicemailsSearchResponse**](VoicemailsSearchResponse) post_voicemail_search(body)


Search voicemails

Wraps POST /api/v2/voicemail/search 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
body = PureCloudPlatformClientV2.VoicemailSearchRequest() # VoicemailSearchRequest | Search request options

try:
    # Search voicemails
    api_response = api_instance.post_voicemail_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->post_voicemail_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**VoicemailSearchRequest**](VoicemailSearchRequest)| Search request options |  |

### Return type

[**VoicemailsSearchResponse**](VoicemailsSearchResponse)


## put_voicemail_message

> [**VoicemailMessage**](VoicemailMessage) put_voicemail_message(message_id, body)


Update a voicemail message

A user voicemail can only be modified by its associated user. A group voicemail can only be modified by a user that is a member of the group. A queue voicemail can only be modified by a participant of the conversation the voicemail is associated with.

Wraps PUT /api/v2/voicemail/messages/{messageId} 

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
api_instance = PureCloudPlatformClientV2.VoicemailApi()
message_id = 'message_id_example' # str | Message ID
body = PureCloudPlatformClientV2.VoicemailMessage() # VoicemailMessage | VoicemailMessage

try:
    # Update a voicemail message
    api_response = api_instance.put_voicemail_message(message_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->put_voicemail_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_id** | **str**| Message ID |  |
| **body** | [**VoicemailMessage**](VoicemailMessage)| VoicemailMessage |  |

### Return type

[**VoicemailMessage**](VoicemailMessage)


## put_voicemail_policy

> [**VoicemailOrganizationPolicy**](VoicemailOrganizationPolicy) put_voicemail_policy(body)


Update a policy

Wraps PUT /api/v2/voicemail/policy 

Requires ALL permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.VoicemailApi()
body = PureCloudPlatformClientV2.VoicemailOrganizationPolicy() # VoicemailOrganizationPolicy | Policy

try:
    # Update a policy
    api_response = api_instance.put_voicemail_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->put_voicemail_policy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**VoicemailOrganizationPolicy**](VoicemailOrganizationPolicy)| Policy |  |

### Return type

[**VoicemailOrganizationPolicy**](VoicemailOrganizationPolicy)


## put_voicemail_userpolicy

> [**VoicemailUserPolicy**](VoicemailUserPolicy) put_voicemail_userpolicy(user_id, body)


Update a user's voicemail policy

Wraps PUT /api/v2/voicemail/userpolicies/{userId} 

Requires ALL permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.VoicemailApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.VoicemailUserPolicy() # VoicemailUserPolicy | The user's voicemail policy

try:
    # Update a user's voicemail policy
    api_response = api_instance.put_voicemail_userpolicy(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->put_voicemail_userpolicy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**VoicemailUserPolicy**](VoicemailUserPolicy)| The user&#39;s voicemail policy |  |

### Return type

[**VoicemailUserPolicy**](VoicemailUserPolicy)


_PureCloudPlatformClientV2 219.1.0_

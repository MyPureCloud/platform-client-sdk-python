---
title: WebChatApi
---

## PureCloudPlatformClientV2.WebChatApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_webchat_deployment**](WebChatApi.html#delete_webchat_deployment) | Delete a WebChat deployment|
|[**delete_webchat_guest_conversation_member**](WebChatApi.html#delete_webchat_guest_conversation_member) | Remove a member from a chat conversation|
|[**delete_webchat_settings**](WebChatApi.html#delete_webchat_settings) | Remove WebChat deployment settings|
|[**get_webchat_deployment**](WebChatApi.html#get_webchat_deployment) | Get a WebChat deployment|
|[**get_webchat_deployments**](WebChatApi.html#get_webchat_deployments) | List WebChat deployments|
|[**get_webchat_guest_conversation_mediarequest**](WebChatApi.html#get_webchat_guest_conversation_mediarequest) | Get a media request in the conversation|
|[**get_webchat_guest_conversation_mediarequests**](WebChatApi.html#get_webchat_guest_conversation_mediarequests) | Get all media requests to the guest in the conversation|
|[**get_webchat_guest_conversation_member**](WebChatApi.html#get_webchat_guest_conversation_member) | Get a web chat conversation member|
|[**get_webchat_guest_conversation_members**](WebChatApi.html#get_webchat_guest_conversation_members) | Get the members of a chat conversation.|
|[**get_webchat_guest_conversation_message**](WebChatApi.html#get_webchat_guest_conversation_message) | Get a web chat conversation message|
|[**get_webchat_guest_conversation_messages**](WebChatApi.html#get_webchat_guest_conversation_messages) | Get the messages of a chat conversation.|
|[**get_webchat_settings**](WebChatApi.html#get_webchat_settings) | Get WebChat deployment settings|
|[**patch_webchat_guest_conversation_mediarequest**](WebChatApi.html#patch_webchat_guest_conversation_mediarequest) | Update a media request in the conversation, setting the state to ACCEPTED/DECLINED/ERRORED|
|[**post_webchat_deployments**](WebChatApi.html#post_webchat_deployments) | Create WebChat deployment|
|[**post_webchat_guest_conversation_member_messages**](WebChatApi.html#post_webchat_guest_conversation_member_messages) | Send a message in a chat conversation.|
|[**post_webchat_guest_conversation_member_typing**](WebChatApi.html#post_webchat_guest_conversation_member_typing) | Send a typing-indicator in a chat conversation.|
|[**post_webchat_guest_conversations**](WebChatApi.html#post_webchat_guest_conversations) | Create an ACD chat conversation from an external customer.|
|[**put_webchat_deployment**](WebChatApi.html#put_webchat_deployment) | Update a WebChat deployment|
|[**put_webchat_settings**](WebChatApi.html#put_webchat_settings) | Update WebChat deployment settings|
{: class="table table-striped"}

<a name="delete_webchat_deployment"></a>

##  delete_webchat_deployment(deployment_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Delete a WebChat deployment



Wraps DELETE /api/v2/webchat/deployments/{deploymentId} 

Requires ANY permissions: 

* webchat:deployment:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
deployment_id = 'deployment_id_example' # str | Deployment Id

try:
    # Delete a WebChat deployment
    api_instance.delete_webchat_deployment(deployment_id)
except ApiException as e:
    print("Exception when calling WebChatApi->delete_webchat_deployment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| Deployment Id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_webchat_guest_conversation_member"></a>

##  delete_webchat_guest_conversation_member(conversation_id, member_id)



Remove a member from a chat conversation



Wraps DELETE /api/v2/webchat/guest/conversations/{conversationId}/members/{memberId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure API key authorization: Guest Chat JWT
PureCloudPlatformClientV2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# PureCloudPlatformClientV2.configuration.api_key_prefix['Authorization'] = 'BEARER'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
conversation_id = 'conversation_id_example' # str | conversationId
member_id = 'member_id_example' # str | memberId

try:
    # Remove a member from a chat conversation
    api_instance.delete_webchat_guest_conversation_member(conversation_id, member_id)
except ApiException as e:
    print("Exception when calling WebChatApi->delete_webchat_guest_conversation_member: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **member_id** | **str**| memberId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_webchat_settings"></a>

##  delete_webchat_settings()



Remove WebChat deployment settings



Wraps DELETE /api/v2/webchat/settings 

Requires ANY permissions: 

* webchat:deployment:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()

try:
    # Remove WebChat deployment settings
    api_instance.delete_webchat_settings()
except ApiException as e:
    print("Exception when calling WebChatApi->delete_webchat_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

void (empty response body)

<a name="get_webchat_deployment"></a>

## [**WebChatDeployment**](WebChatDeployment.html) get_webchat_deployment(deployment_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get a WebChat deployment



Wraps GET /api/v2/webchat/deployments/{deploymentId} 

Requires ANY permissions: 

* webchat:deployment:read

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
deployment_id = 'deployment_id_example' # str | Deployment Id

try:
    # Get a WebChat deployment
    api_response = api_instance.get_webchat_deployment(deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->get_webchat_deployment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| Deployment Id |  |
{: class="table table-striped"}

### Return type

[**WebChatDeployment**](WebChatDeployment.html)

<a name="get_webchat_deployments"></a>

## [**WebChatDeploymentEntityListing**](WebChatDeploymentEntityListing.html) get_webchat_deployments()

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

List WebChat deployments



Wraps GET /api/v2/webchat/deployments 

Requires ANY permissions: 

* webchat:deployment:read

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()

try:
    # List WebChat deployments
    api_response = api_instance.get_webchat_deployments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->get_webchat_deployments: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**WebChatDeploymentEntityListing**](WebChatDeploymentEntityListing.html)

<a name="get_webchat_guest_conversation_mediarequest"></a>

## [**WebChatGuestMediaRequest**](WebChatGuestMediaRequest.html) get_webchat_guest_conversation_mediarequest(conversation_id, media_request_id)



Get a media request in the conversation



Wraps GET /api/v2/webchat/guest/conversations/{conversationId}/mediarequests/{mediaRequestId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure API key authorization: Guest Chat JWT
PureCloudPlatformClientV2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# PureCloudPlatformClientV2.configuration.api_key_prefix['Authorization'] = 'BEARER'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
conversation_id = 'conversation_id_example' # str | conversationId
media_request_id = 'media_request_id_example' # str | mediaRequestId

try:
    # Get a media request in the conversation
    api_response = api_instance.get_webchat_guest_conversation_mediarequest(conversation_id, media_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->get_webchat_guest_conversation_mediarequest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **media_request_id** | **str**| mediaRequestId |  |
{: class="table table-striped"}

### Return type

[**WebChatGuestMediaRequest**](WebChatGuestMediaRequest.html)

<a name="get_webchat_guest_conversation_mediarequests"></a>

## [**WebChatGuestMediaRequestEntityList**](WebChatGuestMediaRequestEntityList.html) get_webchat_guest_conversation_mediarequests(conversation_id)



Get all media requests to the guest in the conversation



Wraps GET /api/v2/webchat/guest/conversations/{conversationId}/mediarequests 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure API key authorization: Guest Chat JWT
PureCloudPlatformClientV2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# PureCloudPlatformClientV2.configuration.api_key_prefix['Authorization'] = 'BEARER'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get all media requests to the guest in the conversation
    api_response = api_instance.get_webchat_guest_conversation_mediarequests(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->get_webchat_guest_conversation_mediarequests: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**WebChatGuestMediaRequestEntityList**](WebChatGuestMediaRequestEntityList.html)

<a name="get_webchat_guest_conversation_member"></a>

## [**WebChatMemberInfo**](WebChatMemberInfo.html) get_webchat_guest_conversation_member(conversation_id, member_id)



Get a web chat conversation member



Wraps GET /api/v2/webchat/guest/conversations/{conversationId}/members/{memberId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure API key authorization: Guest Chat JWT
PureCloudPlatformClientV2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# PureCloudPlatformClientV2.configuration.api_key_prefix['Authorization'] = 'BEARER'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
conversation_id = 'conversation_id_example' # str | conversationId
member_id = 'member_id_example' # str | memberId

try:
    # Get a web chat conversation member
    api_response = api_instance.get_webchat_guest_conversation_member(conversation_id, member_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->get_webchat_guest_conversation_member: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **member_id** | **str**| memberId |  |
{: class="table table-striped"}

### Return type

[**WebChatMemberInfo**](WebChatMemberInfo.html)

<a name="get_webchat_guest_conversation_members"></a>

## [**WebChatMemberInfoEntityList**](WebChatMemberInfoEntityList.html) get_webchat_guest_conversation_members(conversation_id, page_size=page_size, page_number=page_number, exclude_disconnected_members=exclude_disconnected_members)



Get the members of a chat conversation.



Wraps GET /api/v2/webchat/guest/conversations/{conversationId}/members 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure API key authorization: Guest Chat JWT
PureCloudPlatformClientV2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# PureCloudPlatformClientV2.configuration.api_key_prefix['Authorization'] = 'BEARER'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
conversation_id = 'conversation_id_example' # str | conversationId
page_size = 25 # int | The number of entries to return per page, or omitted for the default. (optional) (default to 25)
page_number = 1 # int | The page number to return, or omitted for the first page. (optional) (default to 1)
exclude_disconnected_members = False # bool | If true, the results will not contain members who have a DISCONNECTED state. (optional) (default to False)

try:
    # Get the members of a chat conversation.
    api_response = api_instance.get_webchat_guest_conversation_members(conversation_id, page_size=page_size, page_number=page_number, exclude_disconnected_members=exclude_disconnected_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->get_webchat_guest_conversation_members: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **page_size** | **int**| The number of entries to return per page, or omitted for the default. | [optional] [default to 25] |
| **page_number** | **int**| The page number to return, or omitted for the first page. | [optional] [default to 1] |
| **exclude_disconnected_members** | **bool**| If true, the results will not contain members who have a DISCONNECTED state. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**WebChatMemberInfoEntityList**](WebChatMemberInfoEntityList.html)

<a name="get_webchat_guest_conversation_message"></a>

## [**WebChatMessage**](WebChatMessage.html) get_webchat_guest_conversation_message(conversation_id, message_id)



Get a web chat conversation message



Wraps GET /api/v2/webchat/guest/conversations/{conversationId}/messages/{messageId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure API key authorization: Guest Chat JWT
PureCloudPlatformClientV2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# PureCloudPlatformClientV2.configuration.api_key_prefix['Authorization'] = 'BEARER'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
conversation_id = 'conversation_id_example' # str | conversationId
message_id = 'message_id_example' # str | messageId

try:
    # Get a web chat conversation message
    api_response = api_instance.get_webchat_guest_conversation_message(conversation_id, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->get_webchat_guest_conversation_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **message_id** | **str**| messageId |  |
{: class="table table-striped"}

### Return type

[**WebChatMessage**](WebChatMessage.html)

<a name="get_webchat_guest_conversation_messages"></a>

## [**WebChatMessageEntityList**](WebChatMessageEntityList.html) get_webchat_guest_conversation_messages(conversation_id, after=after, before=before, sort_order=sort_order, max_results=max_results)



Get the messages of a chat conversation.



Wraps GET /api/v2/webchat/guest/conversations/{conversationId}/messages 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure API key authorization: Guest Chat JWT
PureCloudPlatformClientV2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# PureCloudPlatformClientV2.configuration.api_key_prefix['Authorization'] = 'BEARER'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
conversation_id = 'conversation_id_example' # str | conversationId
after = 'after_example' # str | If available, get the messages chronologically after the id of this message (optional)
before = 'before_example' # str | If available, get the messages chronologically before the id of this message (optional)
sort_order = ''ascending'' # str | Sort order (optional) (default to 'ascending')
max_results = 100 # int | Limit the returned number of messages, up to a maximum of 100 (optional) (default to 100)

try:
    # Get the messages of a chat conversation.
    api_response = api_instance.get_webchat_guest_conversation_messages(conversation_id, after=after, before=before, sort_order=sort_order, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->get_webchat_guest_conversation_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **after** | **str**| If available, get the messages chronologically after the id of this message | [optional]  |
| **before** | **str**| If available, get the messages chronologically before the id of this message | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ascending&#39;]<br />**Values**: ascending, descending |
| **max_results** | **int**| Limit the returned number of messages, up to a maximum of 100 | [optional] [default to 100] |
{: class="table table-striped"}

### Return type

[**WebChatMessageEntityList**](WebChatMessageEntityList.html)

<a name="get_webchat_settings"></a>

## [**WebChatSettings**](WebChatSettings.html) get_webchat_settings()



Get WebChat deployment settings



Wraps GET /api/v2/webchat/settings 

Requires ANY permissions: 

* webchat:deployment:read

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()

try:
    # Get WebChat deployment settings
    api_response = api_instance.get_webchat_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->get_webchat_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**WebChatSettings**](WebChatSettings.html)

<a name="patch_webchat_guest_conversation_mediarequest"></a>

## [**WebChatGuestMediaRequest**](WebChatGuestMediaRequest.html) patch_webchat_guest_conversation_mediarequest(conversation_id, media_request_id, body)



Update a media request in the conversation, setting the state to ACCEPTED/DECLINED/ERRORED



Wraps PATCH /api/v2/webchat/guest/conversations/{conversationId}/mediarequests/{mediaRequestId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure API key authorization: Guest Chat JWT
PureCloudPlatformClientV2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# PureCloudPlatformClientV2.configuration.api_key_prefix['Authorization'] = 'BEARER'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
conversation_id = 'conversation_id_example' # str | conversationId
media_request_id = 'media_request_id_example' # str | mediaRequestId
body = PureCloudPlatformClientV2.WebChatGuestMediaRequest() # WebChatGuestMediaRequest | Request

try:
    # Update a media request in the conversation, setting the state to ACCEPTED/DECLINED/ERRORED
    api_response = api_instance.patch_webchat_guest_conversation_mediarequest(conversation_id, media_request_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->patch_webchat_guest_conversation_mediarequest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **media_request_id** | **str**| mediaRequestId |  |
| **body** | [**WebChatGuestMediaRequest**](WebChatGuestMediaRequest.html)| Request |  |
{: class="table table-striped"}

### Return type

[**WebChatGuestMediaRequest**](WebChatGuestMediaRequest.html)

<a name="post_webchat_deployments"></a>

## [**WebChatDeployment**](WebChatDeployment.html) post_webchat_deployments(body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Create WebChat deployment



Wraps POST /api/v2/webchat/deployments 

Requires ANY permissions: 

* webchat:deployment:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
body = PureCloudPlatformClientV2.WebChatDeployment() # WebChatDeployment | Deployment

try:
    # Create WebChat deployment
    api_response = api_instance.post_webchat_deployments(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->post_webchat_deployments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WebChatDeployment**](WebChatDeployment.html)| Deployment |  |
{: class="table table-striped"}

### Return type

[**WebChatDeployment**](WebChatDeployment.html)

<a name="post_webchat_guest_conversation_member_messages"></a>

## [**WebChatMessage**](WebChatMessage.html) post_webchat_guest_conversation_member_messages(conversation_id, member_id, body)



Send a message in a chat conversation.



Wraps POST /api/v2/webchat/guest/conversations/{conversationId}/members/{memberId}/messages 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure API key authorization: Guest Chat JWT
PureCloudPlatformClientV2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# PureCloudPlatformClientV2.configuration.api_key_prefix['Authorization'] = 'BEARER'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
conversation_id = 'conversation_id_example' # str | conversationId
member_id = 'member_id_example' # str | memberId
body = PureCloudPlatformClientV2.CreateWebChatMessageRequest() # CreateWebChatMessageRequest | Message

try:
    # Send a message in a chat conversation.
    api_response = api_instance.post_webchat_guest_conversation_member_messages(conversation_id, member_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->post_webchat_guest_conversation_member_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **member_id** | **str**| memberId |  |
| **body** | [**CreateWebChatMessageRequest**](CreateWebChatMessageRequest.html)| Message |  |
{: class="table table-striped"}

### Return type

[**WebChatMessage**](WebChatMessage.html)

<a name="post_webchat_guest_conversation_member_typing"></a>

## [**WebChatTyping**](WebChatTyping.html) post_webchat_guest_conversation_member_typing(conversation_id, member_id)



Send a typing-indicator in a chat conversation.



Wraps POST /api/v2/webchat/guest/conversations/{conversationId}/members/{memberId}/typing 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure API key authorization: Guest Chat JWT
PureCloudPlatformClientV2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# PureCloudPlatformClientV2.configuration.api_key_prefix['Authorization'] = 'BEARER'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
conversation_id = 'conversation_id_example' # str | conversationId
member_id = 'member_id_example' # str | memberId

try:
    # Send a typing-indicator in a chat conversation.
    api_response = api_instance.post_webchat_guest_conversation_member_typing(conversation_id, member_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->post_webchat_guest_conversation_member_typing: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **member_id** | **str**| memberId |  |
{: class="table table-striped"}

### Return type

[**WebChatTyping**](WebChatTyping.html)

<a name="post_webchat_guest_conversations"></a>

## [**CreateWebChatConversationResponse**](CreateWebChatConversationResponse.html) post_webchat_guest_conversations(body)



Create an ACD chat conversation from an external customer.

This endpoint will create a new ACD Chat conversation under the specified Chat Deployment.  The conversation will begin with a guest member in it (with a role=CUSTOMER) according to the customer information that is supplied. If the guest member is authenticated, the 'memberAuthToken' field should include his JWT as generated by the 'POST /api/v2/signeddata' resource; if the guest member is anonymous (and the Deployment permits it) this field can be omitted.  The returned data includes the IDs of the conversation created, along with a newly-create JWT token that you can supply to all future endpoints as authentication to perform operations against that conversation. After successfully creating a conversation, you should connect a websocket to the event stream named in the 'eventStreamUri' field of the response; the conversation is not routed until the event stream is attached.



Wraps POST /api/v2/webchat/guest/conversations 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
body = PureCloudPlatformClientV2.CreateWebChatConversationRequest() # CreateWebChatConversationRequest | CreateConversationRequest

try:
    # Create an ACD chat conversation from an external customer.
    api_response = api_instance.post_webchat_guest_conversations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->post_webchat_guest_conversations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateWebChatConversationRequest**](CreateWebChatConversationRequest.html)| CreateConversationRequest |  |
{: class="table table-striped"}

### Return type

[**CreateWebChatConversationResponse**](CreateWebChatConversationResponse.html)

<a name="put_webchat_deployment"></a>

## [**WebChatDeployment**](WebChatDeployment.html) put_webchat_deployment(deployment_id, body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update a WebChat deployment



Wraps PUT /api/v2/webchat/deployments/{deploymentId} 

Requires ANY permissions: 

* webchat:deployment:update

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
deployment_id = 'deployment_id_example' # str | Deployment Id
body = PureCloudPlatformClientV2.WebChatDeployment() # WebChatDeployment | Deployment

try:
    # Update a WebChat deployment
    api_response = api_instance.put_webchat_deployment(deployment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->put_webchat_deployment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| Deployment Id |  |
| **body** | [**WebChatDeployment**](WebChatDeployment.html)| Deployment |  |
{: class="table table-striped"}

### Return type

[**WebChatDeployment**](WebChatDeployment.html)

<a name="put_webchat_settings"></a>

## [**WebChatSettings**](WebChatSettings.html) put_webchat_settings(body)



Update WebChat deployment settings



Wraps PUT /api/v2/webchat/settings 

Requires ANY permissions: 

* webchat:deployment:update

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
body = PureCloudPlatformClientV2.WebChatSettings() # WebChatSettings | webChatSettings

try:
    # Update WebChat deployment settings
    api_response = api_instance.put_webchat_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebChatApi->put_webchat_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WebChatSettings**](WebChatSettings.html)| webChatSettings |  |
{: class="table table-striped"}

### Return type

[**WebChatSettings**](WebChatSettings.html)


---
title: ConversationsApi
---

## PureCloudPlatformClientV2.ConversationsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_conversation_participant_code**](ConversationsApi.html#delete_conversation_participant_code) | Delete a code used to add a communication to this participant|
|[**delete_conversations_call_participant_consult**](ConversationsApi.html#delete_conversations_call_participant_consult) | Cancel the transfer|
|[**delete_conversations_email_messages_draft_attachment**](ConversationsApi.html#delete_conversations_email_messages_draft_attachment) | Delete attachment from draft|
|[**get_analytics_conversation_details**](ConversationsApi.html#get_analytics_conversation_details) | Get a conversation by id|
|[**get_analytics_conversations_details**](ConversationsApi.html#get_analytics_conversations_details) | Gets multiple conversations by id|
|[**get_conversation**](ConversationsApi.html#get_conversation) | Get conversation|
|[**get_conversation_participant_secureivrsession**](ConversationsApi.html#get_conversation_participant_secureivrsession) | Fetch info on a secure session|
|[**get_conversation_participant_secureivrsessions**](ConversationsApi.html#get_conversation_participant_secureivrsessions) | Get a list of secure sessions for this participant.|
|[**get_conversation_participant_wrapup**](ConversationsApi.html#get_conversation_participant_wrapup) | Get the wrap-up for this conversation participant. |
|[**get_conversation_participant_wrapupcodes**](ConversationsApi.html#get_conversation_participant_wrapupcodes) | Get list of wrapup codes for this conversation participant|
|[**get_conversations**](ConversationsApi.html#get_conversations) | Get active conversations for the logged in user|
|[**get_conversations_call**](ConversationsApi.html#get_conversations_call) | Get call conversation|
|[**get_conversations_call_participant_wrapup**](ConversationsApi.html#get_conversations_call_participant_wrapup) | Get the wrap-up for this conversation participant. |
|[**get_conversations_call_participant_wrapupcodes**](ConversationsApi.html#get_conversations_call_participant_wrapupcodes) | Get list of wrapup codes for this conversation participant|
|[**get_conversations_callback**](ConversationsApi.html#get_conversations_callback) | Get callback conversation|
|[**get_conversations_callback_participant_wrapup**](ConversationsApi.html#get_conversations_callback_participant_wrapup) | Get the wrap-up for this conversation participant. |
|[**get_conversations_callback_participant_wrapupcodes**](ConversationsApi.html#get_conversations_callback_participant_wrapupcodes) | Get list of wrapup codes for this conversation participant|
|[**get_conversations_callbacks**](ConversationsApi.html#get_conversations_callbacks) | Get active callback conversations for the logged in user|
|[**get_conversations_calls**](ConversationsApi.html#get_conversations_calls) | Get active call conversations for the logged in user|
|[**get_conversations_calls_history**](ConversationsApi.html#get_conversations_calls_history) | Get call history|
|[**get_conversations_calls_maximumconferenceparties**](ConversationsApi.html#get_conversations_calls_maximumconferenceparties) | Get the maximum number of participants that this user can have on a conference|
|[**get_conversations_chat**](ConversationsApi.html#get_conversations_chat) | Get chat conversation|
|[**get_conversations_chat_participant_wrapup**](ConversationsApi.html#get_conversations_chat_participant_wrapup) | Get the wrap-up for this conversation participant. |
|[**get_conversations_chat_participant_wrapupcodes**](ConversationsApi.html#get_conversations_chat_participant_wrapupcodes) | Get list of wrapup codes for this conversation participant|
|[**get_conversations_chats**](ConversationsApi.html#get_conversations_chats) | Get active chat conversations for the logged in user|
|[**get_conversations_cobrowsesession**](ConversationsApi.html#get_conversations_cobrowsesession) | Get cobrowse conversation|
|[**get_conversations_cobrowsesession_participant_wrapup**](ConversationsApi.html#get_conversations_cobrowsesession_participant_wrapup) | Get the wrap-up for this conversation participant. |
|[**get_conversations_cobrowsesession_participant_wrapupcodes**](ConversationsApi.html#get_conversations_cobrowsesession_participant_wrapupcodes) | Get list of wrapup codes for this conversation participant|
|[**get_conversations_cobrowsesessions**](ConversationsApi.html#get_conversations_cobrowsesessions) | Get active cobrowse conversations for the logged in user|
|[**get_conversations_email**](ConversationsApi.html#get_conversations_email) | Get email conversation|
|[**get_conversations_email_message**](ConversationsApi.html#get_conversations_email_message) | Get conversation message|
|[**get_conversations_email_messages**](ConversationsApi.html#get_conversations_email_messages) | Get conversation messages|
|[**get_conversations_email_messages_draft**](ConversationsApi.html#get_conversations_email_messages_draft) | Get conversation draft reply|
|[**get_conversations_email_participant_wrapup**](ConversationsApi.html#get_conversations_email_participant_wrapup) | Get the wrap-up for this conversation participant. |
|[**get_conversations_email_participant_wrapupcodes**](ConversationsApi.html#get_conversations_email_participant_wrapupcodes) | Get list of wrapup codes for this conversation participant|
|[**get_conversations_emails**](ConversationsApi.html#get_conversations_emails) | Get active email conversations for the logged in user|
|[**get_conversations_message**](ConversationsApi.html#get_conversations_message) | Get message conversation|
|[**get_conversations_message_communication_messages_media_media_id**](ConversationsApi.html#get_conversations_message_communication_messages_media_media_id) | Get media|
|[**get_conversations_message_message**](ConversationsApi.html#get_conversations_message_message) | Get message|
|[**get_conversations_message_participant_wrapup**](ConversationsApi.html#get_conversations_message_participant_wrapup) | Get the wrap-up for this conversation participant. |
|[**get_conversations_message_participant_wrapupcodes**](ConversationsApi.html#get_conversations_message_participant_wrapupcodes) | Get list of wrapup codes for this conversation participant|
|[**get_conversations_messages**](ConversationsApi.html#get_conversations_messages) | Get active message conversations for the logged in user|
|[**patch_conversation_participant**](ConversationsApi.html#patch_conversation_participant) | Update a participant.|
|[**patch_conversation_participant_attributes**](ConversationsApi.html#patch_conversation_participant_attributes) | Update the attributes on a conversation participant.|
|[**patch_conversations_call**](ConversationsApi.html#patch_conversations_call) | Update a conversation by setting it&#39;s recording state, merging in other conversations to create a conference, or disconnecting all of the participants|
|[**patch_conversations_call_participant**](ConversationsApi.html#patch_conversations_call_participant) | Update conversation participant|
|[**patch_conversations_call_participant_attributes**](ConversationsApi.html#patch_conversations_call_participant_attributes) | Update the attributes on a conversation participant.|
|[**patch_conversations_call_participant_communication**](ConversationsApi.html#patch_conversations_call_participant_communication) | Update conversation participant&#39;s communication by disconnecting it.|
|[**patch_conversations_call_participant_consult**](ConversationsApi.html#patch_conversations_call_participant_consult) | Change who can speak|
|[**patch_conversations_callback**](ConversationsApi.html#patch_conversations_callback) | Update a conversation by disconnecting all of the participants|
|[**patch_conversations_callback_participant**](ConversationsApi.html#patch_conversations_callback_participant) | Update conversation participant|
|[**patch_conversations_callback_participant_attributes**](ConversationsApi.html#patch_conversations_callback_participant_attributes) | Update the attributes on a conversation participant.|
|[**patch_conversations_callback_participant_communication**](ConversationsApi.html#patch_conversations_callback_participant_communication) | Update conversation participant&#39;s communication by disconnecting it.|
|[**patch_conversations_chat**](ConversationsApi.html#patch_conversations_chat) | Update a conversation by disconnecting all of the participants|
|[**patch_conversations_chat_participant**](ConversationsApi.html#patch_conversations_chat_participant) | Update conversation participant|
|[**patch_conversations_chat_participant_attributes**](ConversationsApi.html#patch_conversations_chat_participant_attributes) | Update the attributes on a conversation participant.|
|[**patch_conversations_chat_participant_communication**](ConversationsApi.html#patch_conversations_chat_participant_communication) | Update conversation participant&#39;s communication by disconnecting it.|
|[**patch_conversations_cobrowsesession**](ConversationsApi.html#patch_conversations_cobrowsesession) | Update a conversation by disconnecting all of the participants|
|[**patch_conversations_cobrowsesession_participant**](ConversationsApi.html#patch_conversations_cobrowsesession_participant) | Update conversation participant|
|[**patch_conversations_cobrowsesession_participant_attributes**](ConversationsApi.html#patch_conversations_cobrowsesession_participant_attributes) | Update the attributes on a conversation participant.|
|[**patch_conversations_cobrowsesession_participant_communication**](ConversationsApi.html#patch_conversations_cobrowsesession_participant_communication) | Update conversation participant&#39;s communication by disconnecting it.|
|[**patch_conversations_email**](ConversationsApi.html#patch_conversations_email) | Update a conversation by disconnecting all of the participants|
|[**patch_conversations_email_participant**](ConversationsApi.html#patch_conversations_email_participant) | Update conversation participant|
|[**patch_conversations_email_participant_attributes**](ConversationsApi.html#patch_conversations_email_participant_attributes) | Update the attributes on a conversation participant.|
|[**patch_conversations_email_participant_communication**](ConversationsApi.html#patch_conversations_email_participant_communication) | Update conversation participant&#39;s communication by disconnecting it.|
|[**patch_conversations_message**](ConversationsApi.html#patch_conversations_message) | Update a conversation by disconnecting all of the participants|
|[**patch_conversations_message_participant**](ConversationsApi.html#patch_conversations_message_participant) | Update conversation participant|
|[**patch_conversations_message_participant_attributes**](ConversationsApi.html#patch_conversations_message_participant_attributes) | Update the attributes on a conversation participant.|
|[**patch_conversations_message_participant_communication**](ConversationsApi.html#patch_conversations_message_participant_communication) | Update conversation participant&#39;s communication by disconnecting it.|
|[**post_analytics_conversation_details_properties**](ConversationsApi.html#post_analytics_conversation_details_properties) | Index conversation properties|
|[**post_analytics_conversations_aggregates_query**](ConversationsApi.html#post_analytics_conversations_aggregates_query) | Query for conversation aggregates|
|[**post_analytics_conversations_details_query**](ConversationsApi.html#post_analytics_conversations_details_query) | Query for conversation details|
|[**post_conversation_disconnect**](ConversationsApi.html#post_conversation_disconnect) | Performs a full conversation teardown. Issues disconnect requests for any connected media. Applies a system wrap-up code to any participants that are pending wrap-up. This is not intended to be the normal way of ending interactions but is available in the event of problems with the application to allow a resyncronization of state across all components. It is recommended that users submit a support case if they are relying on this endpoint systematically as there is likely something that needs investigation.|
|[**post_conversation_participant_callbacks**](ConversationsApi.html#post_conversation_participant_callbacks) | Create a new callback for the specified participant on the conversation.|
|[**post_conversation_participant_digits**](ConversationsApi.html#post_conversation_participant_digits) | Sends DTMF to the participant|
|[**post_conversation_participant_replace**](ConversationsApi.html#post_conversation_participant_replace) | Replace this participant with the specified user and/or address|
|[**post_conversation_participant_secureivrsessions**](ConversationsApi.html#post_conversation_participant_secureivrsessions) | Create secure IVR session. Only a participant in the conversation can invoke a secure IVR.|
|[**post_conversations_call**](ConversationsApi.html#post_conversations_call) | Place a new call as part of a callback conversation.|
|[**post_conversations_call_participant_consult**](ConversationsApi.html#post_conversations_call_participant_consult) | Initiate and update consult transfer|
|[**post_conversations_call_participant_monitor**](ConversationsApi.html#post_conversations_call_participant_monitor) | Listen in on the conversation from the point of view of a given participant.|
|[**post_conversations_call_participant_replace**](ConversationsApi.html#post_conversations_call_participant_replace) | Replace this participant with the specified user and/or address|
|[**post_conversations_call_participants**](ConversationsApi.html#post_conversations_call_participants) | Add participants to a conversation|
|[**post_conversations_callback_participant_replace**](ConversationsApi.html#post_conversations_callback_participant_replace) | Replace this participant with the specified user and/or address|
|[**post_conversations_callbacks**](ConversationsApi.html#post_conversations_callbacks) | Create a Callback|
|[**post_conversations_calls**](ConversationsApi.html#post_conversations_calls) | Create a call conversation|
|[**post_conversations_chat_participant_replace**](ConversationsApi.html#post_conversations_chat_participant_replace) | Replace this participant with the specified user and/or address|
|[**post_conversations_chats**](ConversationsApi.html#post_conversations_chats) | Create a web chat conversation|
|[**post_conversations_cobrowsesession_participant_replace**](ConversationsApi.html#post_conversations_cobrowsesession_participant_replace) | Replace this participant with the specified user and/or address|
|[**post_conversations_email_inboundmessages**](ConversationsApi.html#post_conversations_email_inboundmessages) | Send an email to an external conversation. An external conversation is one where the provider is not PureCloud based. This endpoint allows the sender of the external email to reply or send a new message to the existing conversation. The new message will be treated as part of the existing conversation and chained to it.|
|[**post_conversations_email_messages**](ConversationsApi.html#post_conversations_email_messages) | Send an email reply|
|[**post_conversations_email_participant_replace**](ConversationsApi.html#post_conversations_email_participant_replace) | Replace this participant with the specified user and/or address|
|[**post_conversations_emails**](ConversationsApi.html#post_conversations_emails) | Create an email conversation|
|[**post_conversations_faxes**](ConversationsApi.html#post_conversations_faxes) | Create Fax Conversation|
|[**post_conversations_message_communication_messages**](ConversationsApi.html#post_conversations_message_communication_messages) | Send message|
|[**post_conversations_message_communication_messages_media**](ConversationsApi.html#post_conversations_message_communication_messages_media) | Create media|
|[**post_conversations_message_messages_bulk**](ConversationsApi.html#post_conversations_message_messages_bulk) | Get messages in batch|
|[**post_conversations_message_participant_replace**](ConversationsApi.html#post_conversations_message_participant_replace) | Replace this participant with the specified user and/or address|
|[**post_conversations_messages**](ConversationsApi.html#post_conversations_messages) | Create an outbound messaging conversation.|
|[**put_conversations_call_participant_communication_uuidata**](ConversationsApi.html#put_conversations_call_participant_communication_uuidata) | Set uuiData to be sent on future commands.|
|[**put_conversations_email_messages_draft**](ConversationsApi.html#put_conversations_email_messages_draft) | Update conversation draft reply|
{: class="table table-striped"}

<a name="delete_conversation_participant_code"></a>

##  delete_conversation_participant_code(conversation_id, participant_id, add_communication_code)



Delete a code used to add a communication to this participant



Wraps DELETE /api/v2/conversations/{conversationId}/participants/{participantId}/codes/{addCommunicationCode} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
add_communication_code = 'add_communication_code_example' # str | addCommunicationCode

try:
    # Delete a code used to add a communication to this participant
    api_instance.delete_conversation_participant_code(conversation_id, participant_id, add_communication_code)
except ApiException as e:
    print "Exception when calling ConversationsApi->delete_conversation_participant_code: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **add_communication_code** | **str**| addCommunicationCode |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_conversations_call_participant_consult"></a>

##  delete_conversations_call_participant_consult(conversation_id, participant_id)



Cancel the transfer



Wraps DELETE /api/v2/conversations/calls/{conversationId}/participants/{participantId}/consult 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Cancel the transfer
    api_instance.delete_conversations_call_participant_consult(conversation_id, participant_id)
except ApiException as e:
    print "Exception when calling ConversationsApi->delete_conversations_call_participant_consult: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_conversations_email_messages_draft_attachment"></a>

##  delete_conversations_email_messages_draft_attachment(conversation_id, attachment_id)



Delete attachment from draft



Wraps DELETE /api/v2/conversations/emails/{conversationId}/messages/draft/attachments/{attachmentId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
attachment_id = 'attachment_id_example' # str | attachmentId

try:
    # Delete attachment from draft
    api_instance.delete_conversations_email_messages_draft_attachment(conversation_id, attachment_id)
except ApiException as e:
    print "Exception when calling ConversationsApi->delete_conversations_email_messages_draft_attachment: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **attachment_id** | **str**| attachmentId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_analytics_conversation_details"></a>

## [**AnalyticsConversation**](AnalyticsConversation.html) get_analytics_conversation_details(conversation_id)



Get a conversation by id



Wraps GET /api/v2/analytics/conversations/{conversationId}/details 

Requires ANY permissions: 

* analytics:conversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get a conversation by id
    api_response = api_instance.get_analytics_conversation_details(conversation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_analytics_conversation_details: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**AnalyticsConversation**](AnalyticsConversation.html)

<a name="get_analytics_conversations_details"></a>

## [**AnalyticsConversation**](AnalyticsConversation.html) get_analytics_conversations_details(id=id)



Gets multiple conversations by id



Wraps GET /api/v2/analytics/conversations/details 

Requires ANY permissions: 

* analytics:conversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
id = ['id_example'] # list[str] | Comma-separated conversation ids (optional)

try:
    # Gets multiple conversations by id
    api_response = api_instance.get_analytics_conversations_details(id=id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_analytics_conversations_details: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str.html)| Comma-separated conversation ids | [optional]  |
{: class="table table-striped"}

### Return type

[**AnalyticsConversation**](AnalyticsConversation.html)

<a name="get_conversation"></a>

## [**Conversation**](Conversation.html) get_conversation(conversation_id)



Get conversation



Wraps GET /api/v2/conversations/{conversationId} 

Requires ANY permissions: 

* conversation:communication:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID

try:
    # Get conversation
    api_response = api_instance.get_conversation(conversation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversation: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="get_conversation_participant_secureivrsession"></a>

## [**SecureSession**](SecureSession.html) get_conversation_participant_secureivrsession(conversation_id, participant_id, secure_session_id)



Fetch info on a secure session



Wraps GET /api/v2/conversations/{conversationId}/participants/{participantId}/secureivrsessions/{secureSessionId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
secure_session_id = 'secure_session_id_example' # str | secure IVR session ID

try:
    # Fetch info on a secure session
    api_response = api_instance.get_conversation_participant_secureivrsession(conversation_id, participant_id, secure_session_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversation_participant_secureivrsession: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **secure_session_id** | **str**| secure IVR session ID |  |
{: class="table table-striped"}

### Return type

[**SecureSession**](SecureSession.html)

<a name="get_conversation_participant_secureivrsessions"></a>

## [**SecureSessionEntityListing**](SecureSessionEntityListing.html) get_conversation_participant_secureivrsessions(conversation_id, participant_id)



Get a list of secure sessions for this participant.



Wraps GET /api/v2/conversations/{conversationId}/participants/{participantId}/secureivrsessions 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID

try:
    # Get a list of secure sessions for this participant.
    api_response = api_instance.get_conversation_participant_secureivrsessions(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversation_participant_secureivrsessions: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
{: class="table table-striped"}

### Return type

[**SecureSessionEntityListing**](SecureSessionEntityListing.html)

<a name="get_conversation_participant_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversation_participant_wrapup(conversation_id, participant_id, provisional=provisional)



Get the wrap-up for this conversation participant. 



Wraps GET /api/v2/conversations/{conversationId}/participants/{participantId}/wrapup 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
provisional = false # bool | Indicates if the wrap-up code is provisional. (optional) (default to false)

try:
    # Get the wrap-up for this conversation participant. 
    api_response = api_instance.get_conversation_participant_wrapup(conversation_id, participant_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversation_participant_wrapup: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversation_participant_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) get_conversation_participant_wrapupcodes(conversation_id, participant_id)



Get list of wrapup codes for this conversation participant



Wraps GET /api/v2/conversations/{conversationId}/participants/{participantId}/wrapupcodes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID

try:
    # Get list of wrapup codes for this conversation participant
    api_response = api_instance.get_conversation_participant_wrapupcodes(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversation_participant_wrapupcodes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="get_conversations"></a>

## [**ConversationEntityListing**](ConversationEntityListing.html) get_conversations(communication_type=communication_type)



Get active conversations for the logged in user



Wraps GET /api/v2/conversations 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
communication_type = 'communication_type_example' # str | Call or Chat communication filtering (optional)

try:
    # Get active conversations for the logged in user
    api_response = api_instance.get_conversations(communication_type=communication_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **communication_type** | **str**| Call or Chat communication filtering | [optional]  |
{: class="table table-striped"}

### Return type

[**ConversationEntityListing**](ConversationEntityListing.html)

<a name="get_conversations_call"></a>

## [**CallConversation**](CallConversation.html) get_conversations_call(conversation_id)



Get call conversation



Wraps GET /api/v2/conversations/calls/{conversationId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get call conversation
    api_response = api_instance.get_conversations_call(conversation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_call: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**CallConversation**](CallConversation.html)

<a name="get_conversations_call_participant_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_call_participant_wrapup(conversation_id, participant_id, provisional=provisional)



Get the wrap-up for this conversation participant. 



Wraps GET /api/v2/conversations/calls/{conversationId}/participants/{participantId}/wrapup 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
provisional = false # bool | Indicates if the wrap-up code is provisional. (optional) (default to false)

try:
    # Get the wrap-up for this conversation participant. 
    api_response = api_instance.get_conversations_call_participant_wrapup(conversation_id, participant_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_call_participant_wrapup: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_call_participant_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) get_conversations_call_participant_wrapupcodes(conversation_id, participant_id)



Get list of wrapup codes for this conversation participant



Wraps GET /api/v2/conversations/calls/{conversationId}/participants/{participantId}/wrapupcodes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Get list of wrapup codes for this conversation participant
    api_response = api_instance.get_conversations_call_participant_wrapupcodes(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_call_participant_wrapupcodes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="get_conversations_callback"></a>

## [**CallbackConversation**](CallbackConversation.html) get_conversations_callback(conversation_id)



Get callback conversation



Wraps GET /api/v2/conversations/callbacks/{conversationId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get callback conversation
    api_response = api_instance.get_conversations_callback(conversation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_callback: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**CallbackConversation**](CallbackConversation.html)

<a name="get_conversations_callback_participant_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_callback_participant_wrapup(conversation_id, participant_id, provisional=provisional)



Get the wrap-up for this conversation participant. 



Wraps GET /api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/wrapup 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
provisional = false # bool | Indicates if the wrap-up code is provisional. (optional) (default to false)

try:
    # Get the wrap-up for this conversation participant. 
    api_response = api_instance.get_conversations_callback_participant_wrapup(conversation_id, participant_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_callback_participant_wrapup: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_callback_participant_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) get_conversations_callback_participant_wrapupcodes(conversation_id, participant_id)



Get list of wrapup codes for this conversation participant



Wraps GET /api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/wrapupcodes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Get list of wrapup codes for this conversation participant
    api_response = api_instance.get_conversations_callback_participant_wrapupcodes(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_callback_participant_wrapupcodes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="get_conversations_callbacks"></a>

## [**CallbackConversationEntityListing**](CallbackConversationEntityListing.html) get_conversations_callbacks()



Get active callback conversations for the logged in user



Wraps GET /api/v2/conversations/callbacks 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get active callback conversations for the logged in user
    api_response = api_instance.get_conversations_callbacks()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_callbacks: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**CallbackConversationEntityListing**](CallbackConversationEntityListing.html)

<a name="get_conversations_calls"></a>

## [**CallConversationEntityListing**](CallConversationEntityListing.html) get_conversations_calls()



Get active call conversations for the logged in user



Wraps GET /api/v2/conversations/calls 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get active call conversations for the logged in user
    api_response = api_instance.get_conversations_calls()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_calls: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**CallConversationEntityListing**](CallConversationEntityListing.html)

<a name="get_conversations_calls_history"></a>

## [**CallHistoryConversationEntityListing**](CallHistoryConversationEntityListing.html) get_conversations_calls_history(page_size=page_size, page_number=page_number, interval=interval, expand=expand)



Get call history



Wraps GET /api/v2/conversations/calls/history 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
page_size = 25 # int | Page size, maximum 50 (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
interval = 'interval_example' # str | Interval string; format is ISO-8601. Separate start and end times with forward slash '/' (optional)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get call history
    api_response = api_instance.get_conversations_calls_history(page_size=page_size, page_number=page_number, interval=interval, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_calls_history: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size, maximum 50 | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **interval** | **str**| Interval string; format is ISO-8601. Separate start and end times with forward slash &#39;/&#39; | [optional]  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand. | [optional] <br />**Values**: externalorganization, externalcontact, user, queue, group |
{: class="table table-striped"}

### Return type

[**CallHistoryConversationEntityListing**](CallHistoryConversationEntityListing.html)

<a name="get_conversations_calls_maximumconferenceparties"></a>

## [**MaxParticipants**](MaxParticipants.html) get_conversations_calls_maximumconferenceparties()



Get the maximum number of participants that this user can have on a conference



Wraps GET /api/v2/conversations/calls/maximumconferenceparties 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get the maximum number of participants that this user can have on a conference
    api_response = api_instance.get_conversations_calls_maximumconferenceparties()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_calls_maximumconferenceparties: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**MaxParticipants**](MaxParticipants.html)

<a name="get_conversations_chat"></a>

## [**ChatConversation**](ChatConversation.html) get_conversations_chat(conversation_id)



Get chat conversation



Wraps GET /api/v2/conversations/chats/{conversationId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get chat conversation
    api_response = api_instance.get_conversations_chat(conversation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_chat: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**ChatConversation**](ChatConversation.html)

<a name="get_conversations_chat_participant_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_chat_participant_wrapup(conversation_id, participant_id, provisional=provisional)



Get the wrap-up for this conversation participant. 



Wraps GET /api/v2/conversations/chats/{conversationId}/participants/{participantId}/wrapup 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
provisional = false # bool | Indicates if the wrap-up code is provisional. (optional) (default to false)

try:
    # Get the wrap-up for this conversation participant. 
    api_response = api_instance.get_conversations_chat_participant_wrapup(conversation_id, participant_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_chat_participant_wrapup: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_chat_participant_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) get_conversations_chat_participant_wrapupcodes(conversation_id, participant_id)



Get list of wrapup codes for this conversation participant



Wraps GET /api/v2/conversations/chats/{conversationId}/participants/{participantId}/wrapupcodes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Get list of wrapup codes for this conversation participant
    api_response = api_instance.get_conversations_chat_participant_wrapupcodes(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_chat_participant_wrapupcodes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="get_conversations_chats"></a>

## [**ChatConversationEntityListing**](ChatConversationEntityListing.html) get_conversations_chats()



Get active chat conversations for the logged in user



Wraps GET /api/v2/conversations/chats 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get active chat conversations for the logged in user
    api_response = api_instance.get_conversations_chats()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_chats: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**ChatConversationEntityListing**](ChatConversationEntityListing.html)

<a name="get_conversations_cobrowsesession"></a>

## [**CobrowseConversation**](CobrowseConversation.html) get_conversations_cobrowsesession(conversation_id)



Get cobrowse conversation



Wraps GET /api/v2/conversations/cobrowsesessions/{conversationId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get cobrowse conversation
    api_response = api_instance.get_conversations_cobrowsesession(conversation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_cobrowsesession: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**CobrowseConversation**](CobrowseConversation.html)

<a name="get_conversations_cobrowsesession_participant_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_cobrowsesession_participant_wrapup(conversation_id, participant_id, provisional=provisional)



Get the wrap-up for this conversation participant. 



Wraps GET /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/wrapup 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
provisional = false # bool | Indicates if the wrap-up code is provisional. (optional) (default to false)

try:
    # Get the wrap-up for this conversation participant. 
    api_response = api_instance.get_conversations_cobrowsesession_participant_wrapup(conversation_id, participant_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_cobrowsesession_participant_wrapup: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_cobrowsesession_participant_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) get_conversations_cobrowsesession_participant_wrapupcodes(conversation_id, participant_id)



Get list of wrapup codes for this conversation participant



Wraps GET /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/wrapupcodes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Get list of wrapup codes for this conversation participant
    api_response = api_instance.get_conversations_cobrowsesession_participant_wrapupcodes(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_cobrowsesession_participant_wrapupcodes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="get_conversations_cobrowsesessions"></a>

## [**CobrowseConversationEntityListing**](CobrowseConversationEntityListing.html) get_conversations_cobrowsesessions()



Get active cobrowse conversations for the logged in user



Wraps GET /api/v2/conversations/cobrowsesessions 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get active cobrowse conversations for the logged in user
    api_response = api_instance.get_conversations_cobrowsesessions()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_cobrowsesessions: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**CobrowseConversationEntityListing**](CobrowseConversationEntityListing.html)

<a name="get_conversations_email"></a>

## [**EmailConversation**](EmailConversation.html) get_conversations_email(conversation_id)



Get email conversation



Wraps GET /api/v2/conversations/emails/{conversationId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get email conversation
    api_response = api_instance.get_conversations_email(conversation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_email: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**EmailConversation**](EmailConversation.html)

<a name="get_conversations_email_message"></a>

## [**EmailMessage**](EmailMessage.html) get_conversations_email_message(conversation_id, message_id)



Get conversation message



Wraps GET /api/v2/conversations/emails/{conversationId}/messages/{messageId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
message_id = 'message_id_example' # str | messageId

try:
    # Get conversation message
    api_response = api_instance.get_conversations_email_message(conversation_id, message_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_email_message: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **message_id** | **str**| messageId |  |
{: class="table table-striped"}

### Return type

[**EmailMessage**](EmailMessage.html)

<a name="get_conversations_email_messages"></a>

## [**EmailMessageListing**](EmailMessageListing.html) get_conversations_email_messages(conversation_id)



Get conversation messages



Wraps GET /api/v2/conversations/emails/{conversationId}/messages 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get conversation messages
    api_response = api_instance.get_conversations_email_messages(conversation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_email_messages: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**EmailMessageListing**](EmailMessageListing.html)

<a name="get_conversations_email_messages_draft"></a>

## [**EmailMessage**](EmailMessage.html) get_conversations_email_messages_draft(conversation_id)



Get conversation draft reply



Wraps GET /api/v2/conversations/emails/{conversationId}/messages/draft 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get conversation draft reply
    api_response = api_instance.get_conversations_email_messages_draft(conversation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_email_messages_draft: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**EmailMessage**](EmailMessage.html)

<a name="get_conversations_email_participant_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_email_participant_wrapup(conversation_id, participant_id, provisional=provisional)



Get the wrap-up for this conversation participant. 



Wraps GET /api/v2/conversations/emails/{conversationId}/participants/{participantId}/wrapup 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
provisional = false # bool | Indicates if the wrap-up code is provisional. (optional) (default to false)

try:
    # Get the wrap-up for this conversation participant. 
    api_response = api_instance.get_conversations_email_participant_wrapup(conversation_id, participant_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_email_participant_wrapup: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_email_participant_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) get_conversations_email_participant_wrapupcodes(conversation_id, participant_id)



Get list of wrapup codes for this conversation participant



Wraps GET /api/v2/conversations/emails/{conversationId}/participants/{participantId}/wrapupcodes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Get list of wrapup codes for this conversation participant
    api_response = api_instance.get_conversations_email_participant_wrapupcodes(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_email_participant_wrapupcodes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="get_conversations_emails"></a>

## [**EmailConversationEntityListing**](EmailConversationEntityListing.html) get_conversations_emails()



Get active email conversations for the logged in user



Wraps GET /api/v2/conversations/emails 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get active email conversations for the logged in user
    api_response = api_instance.get_conversations_emails()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_emails: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**EmailConversationEntityListing**](EmailConversationEntityListing.html)

<a name="get_conversations_message"></a>

## [**MessageConversation**](MessageConversation.html) get_conversations_message(conversation_id)



Get message conversation



Wraps GET /api/v2/conversations/messages/{conversationId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get message conversation
    api_response = api_instance.get_conversations_message(conversation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_message: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**MessageConversation**](MessageConversation.html)

<a name="get_conversations_message_communication_messages_media_media_id"></a>

## [**MessageMediaData**](MessageMediaData.html) get_conversations_message_communication_messages_media_media_id(conversation_id, communication_id, media_id)



Get media



Wraps GET /api/v2/conversations/messages/{conversationId}/communications/{communicationId}/messages/media/{mediaId} 

Requires ANY permissions: 

* conversation:message:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
communication_id = 'communication_id_example' # str | communicationId
media_id = 'media_id_example' # str | mediaId

try:
    # Get media
    api_response = api_instance.get_conversations_message_communication_messages_media_media_id(conversation_id, communication_id, media_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_message_communication_messages_media_media_id: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **communication_id** | **str**| communicationId |  |
| **media_id** | **str**| mediaId |  |
{: class="table table-striped"}

### Return type

[**MessageMediaData**](MessageMediaData.html)

<a name="get_conversations_message_message"></a>

## [**MessageData**](MessageData.html) get_conversations_message_message(conversation_id, message_id)



Get message



Wraps GET /api/v2/conversations/messages/{conversationId}/messages/{messageId} 

Requires ANY permissions: 

* conversation:message:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
message_id = 'message_id_example' # str | messageId

try:
    # Get message
    api_response = api_instance.get_conversations_message_message(conversation_id, message_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_message_message: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **message_id** | **str**| messageId |  |
{: class="table table-striped"}

### Return type

[**MessageData**](MessageData.html)

<a name="get_conversations_message_participant_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_message_participant_wrapup(conversation_id, participant_id, provisional=provisional)



Get the wrap-up for this conversation participant. 



Wraps GET /api/v2/conversations/messages/{conversationId}/participants/{participantId}/wrapup 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
provisional = false # bool | Indicates if the wrap-up code is provisional. (optional) (default to false)

try:
    # Get the wrap-up for this conversation participant. 
    api_response = api_instance.get_conversations_message_participant_wrapup(conversation_id, participant_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_message_participant_wrapup: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_message_participant_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) get_conversations_message_participant_wrapupcodes(conversation_id, participant_id)



Get list of wrapup codes for this conversation participant



Wraps GET /api/v2/conversations/messages/{conversationId}/participants/{participantId}/wrapupcodes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str |  conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Get list of wrapup codes for this conversation participant
    api_response = api_instance.get_conversations_message_participant_wrapupcodes(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_message_participant_wrapupcodes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**|  conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="get_conversations_messages"></a>

## [**MessageConversationEntityListing**](MessageConversationEntityListing.html) get_conversations_messages()



Get active message conversations for the logged in user



Wraps GET /api/v2/conversations/messages 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get active message conversations for the logged in user
    api_response = api_instance.get_conversations_messages()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->get_conversations_messages: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**MessageConversationEntityListing**](MessageConversationEntityListing.html)

<a name="patch_conversation_participant"></a>

##  patch_conversation_participant(conversation_id, participant_id, body)



Update a participant.

Update conversation participant.

Wraps PATCH /api/v2/conversations/{conversationId}/participants/{participantId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Update request

try:
    # Update a participant.
    api_instance.patch_conversation_participant(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversation_participant: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Update request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversation_participant_attributes"></a>

##  patch_conversation_participant_attributes(conversation_id, participant_id, body)



Update the attributes on a conversation participant.



Wraps PATCH /api/v2/conversations/{conversationId}/participants/{participantId}/attributes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.ParticipantAttributes() # ParticipantAttributes | Participant attributes

try:
    # Update the attributes on a conversation participant.
    api_instance.patch_conversation_participant_attributes(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversation_participant_attributes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**ParticipantAttributes**](ParticipantAttributes.html)| Participant attributes |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_call"></a>

## [**Conversation**](Conversation.html) patch_conversations_call(conversation_id, body)



Update a conversation by setting it's recording state, merging in other conversations to create a conference, or disconnecting all of the participants



Wraps PATCH /api/v2/conversations/calls/{conversationId} 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Conversation() # Conversation | Conversation

try:
    # Update a conversation by setting it's recording state, merging in other conversations to create a conference, or disconnecting all of the participants
    api_response = api_instance.patch_conversations_call(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_call: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Conversation**](Conversation.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="patch_conversations_call_participant"></a>

##  patch_conversations_call_participant(conversation_id, participant_id, body)



Update conversation participant



Wraps PATCH /api/v2/conversations/calls/{conversationId}/participants/{participantId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant request

try:
    # Update conversation participant
    api_instance.patch_conversations_call_participant(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_call_participant: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_call_participant_attributes"></a>

##  patch_conversations_call_participant_attributes(conversation_id, participant_id, body)



Update the attributes on a conversation participant.



Wraps PATCH /api/v2/conversations/calls/{conversationId}/participants/{participantId}/attributes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ParticipantAttributes() # ParticipantAttributes | Participant attributes

try:
    # Update the attributes on a conversation participant.
    api_instance.patch_conversations_call_participant_attributes(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_call_participant_attributes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ParticipantAttributes**](ParticipantAttributes.html)| Participant attributes |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_call_participant_communication"></a>

## [**Empty**](Empty.html) patch_conversations_call_participant_communication(conversation_id, participant_id, communication_id, body)



Update conversation participant's communication by disconnecting it.



Wraps PATCH /api/v2/conversations/calls/{conversationId}/participants/{participantId}/communications/{communicationId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant

try:
    # Update conversation participant's communication by disconnecting it.
    api_response = api_instance.patch_conversations_call_participant_communication(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_call_participant_communication: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant |  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="patch_conversations_call_participant_consult"></a>

## [**ConsultTransferResponse**](ConsultTransferResponse.html) patch_conversations_call_participant_consult(conversation_id, participant_id, body)



Change who can speak



Wraps PATCH /api/v2/conversations/calls/{conversationId}/participants/{participantId}/consult 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ConsultTransferUpdate() # ConsultTransferUpdate | new speak to

try:
    # Change who can speak
    api_response = api_instance.patch_conversations_call_participant_consult(conversation_id, participant_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_call_participant_consult: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ConsultTransferUpdate**](ConsultTransferUpdate.html)| new speak to |  |
{: class="table table-striped"}

### Return type

[**ConsultTransferResponse**](ConsultTransferResponse.html)

<a name="patch_conversations_callback"></a>

## [**Conversation**](Conversation.html) patch_conversations_callback(conversation_id, body)



Update a conversation by disconnecting all of the participants



Wraps PATCH /api/v2/conversations/callbacks/{conversationId} 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Conversation() # Conversation | Conversation

try:
    # Update a conversation by disconnecting all of the participants
    api_response = api_instance.patch_conversations_callback(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_callback: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Conversation**](Conversation.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="patch_conversations_callback_participant"></a>

##  patch_conversations_callback_participant(conversation_id, participant_id, body)



Update conversation participant



Wraps PATCH /api/v2/conversations/callbacks/{conversationId}/participants/{participantId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant

try:
    # Update conversation participant
    api_instance.patch_conversations_callback_participant(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_callback_participant: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_callback_participant_attributes"></a>

##  patch_conversations_callback_participant_attributes(conversation_id, participant_id, body)



Update the attributes on a conversation participant.



Wraps PATCH /api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/attributes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ParticipantAttributes() # ParticipantAttributes | Attributes

try:
    # Update the attributes on a conversation participant.
    api_instance.patch_conversations_callback_participant_attributes(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_callback_participant_attributes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ParticipantAttributes**](ParticipantAttributes.html)| Attributes |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_callback_participant_communication"></a>

## [**Empty**](Empty.html) patch_conversations_callback_participant_communication(conversation_id, participant_id, communication_id, body)



Update conversation participant's communication by disconnecting it.



Wraps PATCH /api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/communications/{communicationId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant

try:
    # Update conversation participant's communication by disconnecting it.
    api_response = api_instance.patch_conversations_callback_participant_communication(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_callback_participant_communication: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant |  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="patch_conversations_chat"></a>

## [**Conversation**](Conversation.html) patch_conversations_chat(conversation_id, body)



Update a conversation by disconnecting all of the participants



Wraps PATCH /api/v2/conversations/chats/{conversationId} 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Conversation() # Conversation | Conversation

try:
    # Update a conversation by disconnecting all of the participants
    api_response = api_instance.patch_conversations_chat(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_chat: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Conversation**](Conversation.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="patch_conversations_chat_participant"></a>

##  patch_conversations_chat_participant(conversation_id, participant_id, body)



Update conversation participant



Wraps PATCH /api/v2/conversations/chats/{conversationId}/participants/{participantId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Update request

try:
    # Update conversation participant
    api_instance.patch_conversations_chat_participant(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_chat_participant: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Update request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_chat_participant_attributes"></a>

##  patch_conversations_chat_participant_attributes(conversation_id, participant_id, body)



Update the attributes on a conversation participant.



Wraps PATCH /api/v2/conversations/chats/{conversationId}/participants/{participantId}/attributes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ParticipantAttributes() # ParticipantAttributes | Participant attributes

try:
    # Update the attributes on a conversation participant.
    api_instance.patch_conversations_chat_participant_attributes(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_chat_participant_attributes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ParticipantAttributes**](ParticipantAttributes.html)| Participant attributes |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_chat_participant_communication"></a>

## [**Empty**](Empty.html) patch_conversations_chat_participant_communication(conversation_id, participant_id, communication_id, body)



Update conversation participant's communication by disconnecting it.



Wraps PATCH /api/v2/conversations/chats/{conversationId}/participants/{participantId}/communications/{communicationId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant

try:
    # Update conversation participant's communication by disconnecting it.
    api_response = api_instance.patch_conversations_chat_participant_communication(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_chat_participant_communication: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant |  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="patch_conversations_cobrowsesession"></a>

## [**Conversation**](Conversation.html) patch_conversations_cobrowsesession(conversation_id, body)



Update a conversation by disconnecting all of the participants



Wraps PATCH /api/v2/conversations/cobrowsesessions/{conversationId} 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Conversation() # Conversation | Conversation

try:
    # Update a conversation by disconnecting all of the participants
    api_response = api_instance.patch_conversations_cobrowsesession(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_cobrowsesession: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Conversation**](Conversation.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="patch_conversations_cobrowsesession_participant"></a>

##  patch_conversations_cobrowsesession_participant(conversation_id, participant_id, body=body)



Update conversation participant



Wraps PATCH /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest |  (optional)

try:
    # Update conversation participant
    api_instance.patch_conversations_cobrowsesession_participant(conversation_id, participant_id, body=body)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_cobrowsesession_participant: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_cobrowsesession_participant_attributes"></a>

##  patch_conversations_cobrowsesession_participant_attributes(conversation_id, participant_id, body=body)



Update the attributes on a conversation participant.



Wraps PATCH /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/attributes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ParticipantAttributes() # ParticipantAttributes |  (optional)

try:
    # Update the attributes on a conversation participant.
    api_instance.patch_conversations_cobrowsesession_participant_attributes(conversation_id, participant_id, body=body)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_cobrowsesession_participant_attributes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ParticipantAttributes**](ParticipantAttributes.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_cobrowsesession_participant_communication"></a>

## [**Empty**](Empty.html) patch_conversations_cobrowsesession_participant_communication(conversation_id, participant_id, communication_id, body)



Update conversation participant's communication by disconnecting it.



Wraps PATCH /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/communications/{communicationId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant

try:
    # Update conversation participant's communication by disconnecting it.
    api_response = api_instance.patch_conversations_cobrowsesession_participant_communication(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_cobrowsesession_participant_communication: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant |  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="patch_conversations_email"></a>

## [**Conversation**](Conversation.html) patch_conversations_email(conversation_id, body)



Update a conversation by disconnecting all of the participants



Wraps PATCH /api/v2/conversations/emails/{conversationId} 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Conversation() # Conversation | Conversation

try:
    # Update a conversation by disconnecting all of the participants
    api_response = api_instance.patch_conversations_email(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_email: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Conversation**](Conversation.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="patch_conversations_email_participant"></a>

##  patch_conversations_email_participant(conversation_id, participant_id, body)



Update conversation participant



Wraps PATCH /api/v2/conversations/emails/{conversationId}/participants/{participantId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Update request

try:
    # Update conversation participant
    api_instance.patch_conversations_email_participant(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_email_participant: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Update request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_email_participant_attributes"></a>

##  patch_conversations_email_participant_attributes(conversation_id, participant_id, body)



Update the attributes on a conversation participant.



Wraps PATCH /api/v2/conversations/emails/{conversationId}/participants/{participantId}/attributes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ParticipantAttributes() # ParticipantAttributes | Participant attributes

try:
    # Update the attributes on a conversation participant.
    api_instance.patch_conversations_email_participant_attributes(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_email_participant_attributes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ParticipantAttributes**](ParticipantAttributes.html)| Participant attributes |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_email_participant_communication"></a>

## [**Empty**](Empty.html) patch_conversations_email_participant_communication(conversation_id, participant_id, communication_id, body)



Update conversation participant's communication by disconnecting it.



Wraps PATCH /api/v2/conversations/emails/{conversationId}/participants/{participantId}/communications/{communicationId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant

try:
    # Update conversation participant's communication by disconnecting it.
    api_response = api_instance.patch_conversations_email_participant_communication(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_email_participant_communication: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant |  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="patch_conversations_message"></a>

## [**Conversation**](Conversation.html) patch_conversations_message(conversation_id, body)



Update a conversation by disconnecting all of the participants



Wraps PATCH /api/v2/conversations/messages/{conversationId} 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Conversation() # Conversation | Conversation

try:
    # Update a conversation by disconnecting all of the participants
    api_response = api_instance.patch_conversations_message(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_message: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Conversation**](Conversation.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="patch_conversations_message_participant"></a>

##  patch_conversations_message_participant(conversation_id, participant_id, body=body)



Update conversation participant



Wraps PATCH /api/v2/conversations/messages/{conversationId}/participants/{participantId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str |  conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest |  (optional)

try:
    # Update conversation participant
    api_instance.patch_conversations_message_participant(conversation_id, participant_id, body=body)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_message_participant: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**|  conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_message_participant_attributes"></a>

##  patch_conversations_message_participant_attributes(conversation_id, participant_id, body=body)



Update the attributes on a conversation participant.



Wraps PATCH /api/v2/conversations/messages/{conversationId}/participants/{participantId}/attributes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str |  conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ParticipantAttributes() # ParticipantAttributes |  (optional)

try:
    # Update the attributes on a conversation participant.
    api_instance.patch_conversations_message_participant_attributes(conversation_id, participant_id, body=body)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_message_participant_attributes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**|  conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ParticipantAttributes**](ParticipantAttributes.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_message_participant_communication"></a>

## [**Empty**](Empty.html) patch_conversations_message_participant_communication(conversation_id, participant_id, communication_id, body)



Update conversation participant's communication by disconnecting it.



Wraps PATCH /api/v2/conversations/messages/{conversationId}/participants/{participantId}/communications/{communicationId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str |  conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant

try:
    # Update conversation participant's communication by disconnecting it.
    api_response = api_instance.patch_conversations_message_participant_communication(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->patch_conversations_message_participant_communication: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**|  conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant |  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="post_analytics_conversation_details_properties"></a>

## [**PropertyIndexRequest**](PropertyIndexRequest.html) post_analytics_conversation_details_properties(conversation_id, body)



Index conversation properties



Wraps POST /api/v2/analytics/conversations/{conversationId}/details/properties 

Requires ANY permissions: 

* analytics:conversationProperties:index

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.PropertyIndexRequest() # PropertyIndexRequest | request

try:
    # Index conversation properties
    api_response = api_instance.post_analytics_conversation_details_properties(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_analytics_conversation_details_properties: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**PropertyIndexRequest**](PropertyIndexRequest.html)| request |  |
{: class="table table-striped"}

### Return type

[**PropertyIndexRequest**](PropertyIndexRequest.html)

<a name="post_analytics_conversations_aggregates_query"></a>

## [**AggregateQueryResponse**](AggregateQueryResponse.html) post_analytics_conversations_aggregates_query(body)



Query for conversation aggregates



Wraps POST /api/v2/analytics/conversations/aggregates/query 

Requires ANY permissions: 

* analytics:conversationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.AggregationQuery() # AggregationQuery | query

try:
    # Query for conversation aggregates
    api_response = api_instance.post_analytics_conversations_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_analytics_conversations_aggregates_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AggregationQuery**](AggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AggregateQueryResponse**](AggregateQueryResponse.html)

<a name="post_analytics_conversations_details_query"></a>

## [**AnalyticsConversationQueryResponse**](AnalyticsConversationQueryResponse.html) post_analytics_conversations_details_query(body)



Query for conversation details



Wraps POST /api/v2/analytics/conversations/details/query 

Requires ANY permissions: 

* analytics:conversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.ConversationQuery() # ConversationQuery | query

try:
    # Query for conversation details
    api_response = api_instance.post_analytics_conversations_details_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_analytics_conversations_details_query: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationQuery**](ConversationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AnalyticsConversationQueryResponse**](AnalyticsConversationQueryResponse.html)

<a name="post_conversation_disconnect"></a>

## str** post_conversation_disconnect(conversation_id)



Performs a full conversation teardown. Issues disconnect requests for any connected media. Applies a system wrap-up code to any participants that are pending wrap-up. This is not intended to be the normal way of ending interactions but is available in the event of problems with the application to allow a resyncronization of state across all components. It is recommended that users submit a support case if they are relying on this endpoint systematically as there is likely something that needs investigation.



Wraps POST /api/v2/conversations/{conversationId}/disconnect 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID

try:
    # Performs a full conversation teardown. Issues disconnect requests for any connected media. Applies a system wrap-up code to any participants that are pending wrap-up. This is not intended to be the normal way of ending interactions but is available in the event of problems with the application to allow a resyncronization of state across all components. It is recommended that users submit a support case if they are relying on this endpoint systematically as there is likely something that needs investigation.
    api_response = api_instance.post_conversation_disconnect(conversation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversation_disconnect: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
{: class="table table-striped"}

### Return type

**str**

<a name="post_conversation_participant_callbacks"></a>

##  post_conversation_participant_callbacks(conversation_id, participant_id, body=body)



Create a new callback for the specified participant on the conversation.



Wraps POST /api/v2/conversations/{conversationId}/participants/{participantId}/callbacks 

Requires ANY permissions: 

* conversation:callback:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.CreateCallbackOnConversationCommand() # CreateCallbackOnConversationCommand |  (optional)

try:
    # Create a new callback for the specified participant on the conversation.
    api_instance.post_conversation_participant_callbacks(conversation_id, participant_id, body=body)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversation_participant_callbacks: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**CreateCallbackOnConversationCommand**](CreateCallbackOnConversationCommand.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversation_participant_digits"></a>

##  post_conversation_participant_digits(conversation_id, participant_id, body=body)



Sends DTMF to the participant



Wraps POST /api/v2/conversations/{conversationId}/participants/{participantId}/digits 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.Digits() # Digits | Digits (optional)

try:
    # Sends DTMF to the participant
    api_instance.post_conversation_participant_digits(conversation_id, participant_id, body=body)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversation_participant_digits: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**Digits**](Digits.html)| Digits | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversation_participant_replace"></a>

##  post_conversation_participant_replace(conversation_id, participant_id, body)



Replace this participant with the specified user and/or address



Wraps POST /api/v2/conversations/{conversationId}/participants/{participantId}/replace 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.TransferRequest() # TransferRequest | Transfer request

try:
    # Replace this participant with the specified user and/or address
    api_instance.post_conversation_participant_replace(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversation_participant_replace: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**TransferRequest**](TransferRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversation_participant_secureivrsessions"></a>

## [**SecureSession**](SecureSession.html) post_conversation_participant_secureivrsessions(conversation_id, participant_id, body=body)



Create secure IVR session. Only a participant in the conversation can invoke a secure IVR.



Wraps POST /api/v2/conversations/{conversationId}/participants/{participantId}/secureivrsessions 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.CreateSecureSession() # CreateSecureSession |  (optional)

try:
    # Create secure IVR session. Only a participant in the conversation can invoke a secure IVR.
    api_response = api_instance.post_conversation_participant_secureivrsessions(conversation_id, participant_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversation_participant_secureivrsessions: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**CreateSecureSession**](CreateSecureSession.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**SecureSession**](SecureSession.html)

<a name="post_conversations_call"></a>

## [**Conversation**](Conversation.html) post_conversations_call(conversation_id, body)



Place a new call as part of a callback conversation.



Wraps POST /api/v2/conversations/calls/{conversationId} 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.CallCommand() # CallCommand | Conversation

try:
    # Place a new call as part of a callback conversation.
    api_response = api_instance.post_conversations_call(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_call: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**CallCommand**](CallCommand.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="post_conversations_call_participant_consult"></a>

## [**ConsultTransferResponse**](ConsultTransferResponse.html) post_conversations_call_participant_consult(conversation_id, participant_id, body)



Initiate and update consult transfer



Wraps POST /api/v2/conversations/calls/{conversationId}/participants/{participantId}/consult 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ConsultTransfer() # ConsultTransfer | Destination address & initial speak to

try:
    # Initiate and update consult transfer
    api_response = api_instance.post_conversations_call_participant_consult(conversation_id, participant_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_call_participant_consult: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ConsultTransfer**](ConsultTransfer.html)| Destination address &amp; initial speak to |  |
{: class="table table-striped"}

### Return type

[**ConsultTransferResponse**](ConsultTransferResponse.html)

<a name="post_conversations_call_participant_monitor"></a>

##  post_conversations_call_participant_monitor(conversation_id, participant_id)



Listen in on the conversation from the point of view of a given participant.



Wraps POST /api/v2/conversations/calls/{conversationId}/participants/{participantId}/monitor 

Requires ANY permissions: 

* conversation:call:monitor

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Listen in on the conversation from the point of view of a given participant.
    api_instance.post_conversations_call_participant_monitor(conversation_id, participant_id)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_call_participant_monitor: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_call_participant_replace"></a>

##  post_conversations_call_participant_replace(conversation_id, participant_id, body)



Replace this participant with the specified user and/or address



Wraps POST /api/v2/conversations/calls/{conversationId}/participants/{participantId}/replace 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.TransferRequest() # TransferRequest | Transfer request

try:
    # Replace this participant with the specified user and/or address
    api_instance.post_conversations_call_participant_replace(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_call_participant_replace: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**TransferRequest**](TransferRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_call_participants"></a>

## [**Conversation**](Conversation.html) post_conversations_call_participants(conversation_id, body)



Add participants to a conversation



Wraps POST /api/v2/conversations/calls/{conversationId}/participants 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Conversation() # Conversation | Conversation

try:
    # Add participants to a conversation
    api_response = api_instance.post_conversations_call_participants(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_call_participants: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Conversation**](Conversation.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="post_conversations_callback_participant_replace"></a>

##  post_conversations_callback_participant_replace(conversation_id, participant_id, body)



Replace this participant with the specified user and/or address



Wraps POST /api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/replace 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.TransferRequest() # TransferRequest | Transfer request

try:
    # Replace this participant with the specified user and/or address
    api_instance.post_conversations_callback_participant_replace(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_callback_participant_replace: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**TransferRequest**](TransferRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_callbacks"></a>

## [**CreateCallbackResponse**](CreateCallbackResponse.html) post_conversations_callbacks(body)



Create a Callback



Wraps POST /api/v2/conversations/callbacks 

Requires ANY permissions: 

* conversation:callback:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.CreateCallbackCommand() # CreateCallbackCommand | Callback

try:
    # Create a Callback
    api_response = api_instance.post_conversations_callbacks(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_callbacks: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateCallbackCommand**](CreateCallbackCommand.html)| Callback |  |
{: class="table table-striped"}

### Return type

[**CreateCallbackResponse**](CreateCallbackResponse.html)

<a name="post_conversations_calls"></a>

## [**CreateCallResponse**](CreateCallResponse.html) post_conversations_calls(body)



Create a call conversation



Wraps POST /api/v2/conversations/calls 

Requires ANY permissions: 

* conversation:conference:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.CreateCallRequest() # CreateCallRequest | Call request

try:
    # Create a call conversation
    api_response = api_instance.post_conversations_calls(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_calls: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateCallRequest**](CreateCallRequest.html)| Call request |  |
{: class="table table-striped"}

### Return type

[**CreateCallResponse**](CreateCallResponse.html)

<a name="post_conversations_chat_participant_replace"></a>

##  post_conversations_chat_participant_replace(conversation_id, participant_id, body)



Replace this participant with the specified user and/or address



Wraps POST /api/v2/conversations/chats/{conversationId}/participants/{participantId}/replace 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.TransferRequest() # TransferRequest | Transfer request

try:
    # Replace this participant with the specified user and/or address
    api_instance.post_conversations_chat_participant_replace(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_chat_participant_replace: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**TransferRequest**](TransferRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_chats"></a>

## [**ChatConversation**](ChatConversation.html) post_conversations_chats(body)



Create a web chat conversation



Wraps POST /api/v2/conversations/chats 

Requires ANY permissions: 

* conversation:webchat:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.CreateWebChatRequest() # CreateWebChatRequest | Create web chat request

try:
    # Create a web chat conversation
    api_response = api_instance.post_conversations_chats(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_chats: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateWebChatRequest**](CreateWebChatRequest.html)| Create web chat request |  |
{: class="table table-striped"}

### Return type

[**ChatConversation**](ChatConversation.html)

<a name="post_conversations_cobrowsesession_participant_replace"></a>

##  post_conversations_cobrowsesession_participant_replace(conversation_id, participant_id, body=body)



Replace this participant with the specified user and/or address



Wraps POST /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/replace 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.TransferRequest() # TransferRequest |  (optional)

try:
    # Replace this participant with the specified user and/or address
    api_instance.post_conversations_cobrowsesession_participant_replace(conversation_id, participant_id, body=body)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_cobrowsesession_participant_replace: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**TransferRequest**](TransferRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_email_inboundmessages"></a>

## [**EmailConversation**](EmailConversation.html) post_conversations_email_inboundmessages(conversation_id, body)



Send an email to an external conversation. An external conversation is one where the provider is not PureCloud based. This endpoint allows the sender of the external email to reply or send a new message to the existing conversation. The new message will be treated as part of the existing conversation and chained to it.



Wraps POST /api/v2/conversations/emails/{conversationId}/inboundmessages 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.InboundMessageRequest() # InboundMessageRequest | Send external email reply

try:
    # Send an email to an external conversation. An external conversation is one where the provider is not PureCloud based. This endpoint allows the sender of the external email to reply or send a new message to the existing conversation. The new message will be treated as part of the existing conversation and chained to it.
    api_response = api_instance.post_conversations_email_inboundmessages(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_email_inboundmessages: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**InboundMessageRequest**](InboundMessageRequest.html)| Send external email reply |  |
{: class="table table-striped"}

### Return type

[**EmailConversation**](EmailConversation.html)

<a name="post_conversations_email_messages"></a>

## [**EmailMessage**](EmailMessage.html) post_conversations_email_messages(conversation_id, body)



Send an email reply



Wraps POST /api/v2/conversations/emails/{conversationId}/messages 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.EmailMessage() # EmailMessage | Reply

try:
    # Send an email reply
    api_response = api_instance.post_conversations_email_messages(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_email_messages: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**EmailMessage**](EmailMessage.html)| Reply |  |
{: class="table table-striped"}

### Return type

[**EmailMessage**](EmailMessage.html)

<a name="post_conversations_email_participant_replace"></a>

##  post_conversations_email_participant_replace(conversation_id, participant_id, body)



Replace this participant with the specified user and/or address



Wraps POST /api/v2/conversations/emails/{conversationId}/participants/{participantId}/replace 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.TransferRequest() # TransferRequest | Transfer request

try:
    # Replace this participant with the specified user and/or address
    api_instance.post_conversations_email_participant_replace(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_email_participant_replace: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**TransferRequest**](TransferRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_emails"></a>

## [**EmailConversation**](EmailConversation.html) post_conversations_emails(body)



Create an email conversation

If the direction of the request is INBOUND, this will create an external conversation with a third party provider. If the direction of the the request is OUTBOUND, this will create a conversation to send outbound emails on behalf of a queue.

Wraps POST /api/v2/conversations/emails 

Requires ANY permissions: 

* conversation:email:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.CreateEmailRequest() # CreateEmailRequest | Create email request

try:
    # Create an email conversation
    api_response = api_instance.post_conversations_emails(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_emails: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateEmailRequest**](CreateEmailRequest.html)| Create email request |  |
{: class="table table-striped"}

### Return type

[**EmailConversation**](EmailConversation.html)

<a name="post_conversations_faxes"></a>

## [**FaxSendResponse**](FaxSendResponse.html) post_conversations_faxes(body)



Create Fax Conversation



Wraps POST /api/v2/conversations/faxes 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.FaxSendRequest() # FaxSendRequest | Fax

try:
    # Create Fax Conversation
    api_response = api_instance.post_conversations_faxes(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_faxes: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FaxSendRequest**](FaxSendRequest.html)| Fax |  |
{: class="table table-striped"}

### Return type

[**FaxSendResponse**](FaxSendResponse.html)

<a name="post_conversations_message_communication_messages"></a>

## [**MessageData**](MessageData.html) post_conversations_message_communication_messages(conversation_id, communication_id, body)



Send message



Wraps POST /api/v2/conversations/messages/{conversationId}/communications/{communicationId}/messages 

Requires ANY permissions: 

* conversation:message:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.AdditionalMessage() # AdditionalMessage | Message

try:
    # Send message
    api_response = api_instance.post_conversations_message_communication_messages(conversation_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_message_communication_messages: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**AdditionalMessage**](AdditionalMessage.html)| Message |  |
{: class="table table-striped"}

### Return type

[**MessageData**](MessageData.html)

<a name="post_conversations_message_communication_messages_media"></a>

## [**MessageMediaData**](MessageMediaData.html) post_conversations_message_communication_messages_media(conversation_id, communication_id)



Create media



Wraps POST /api/v2/conversations/messages/{conversationId}/communications/{communicationId}/messages/media 

Requires ANY permissions: 

* conversation:message:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
communication_id = 'communication_id_example' # str | communicationId

try:
    # Create media
    api_response = api_instance.post_conversations_message_communication_messages_media(conversation_id, communication_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_message_communication_messages_media: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **communication_id** | **str**| communicationId |  |
{: class="table table-striped"}

### Return type

[**MessageMediaData**](MessageMediaData.html)

<a name="post_conversations_message_messages_bulk"></a>

## [**TextMessageListing**](TextMessageListing.html) post_conversations_message_messages_bulk(conversation_id, body=body)



Get messages in batch



Wraps POST /api/v2/conversations/messages/{conversationId}/messages/bulk 

Requires ANY permissions: 

* conversation:message:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | messageIds (optional)

try:
    # Get messages in batch
    api_response = api_instance.post_conversations_message_messages_bulk(conversation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_message_messages_bulk: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | **list[str]**| messageIds | [optional]  |
{: class="table table-striped"}

### Return type

[**TextMessageListing**](TextMessageListing.html)

<a name="post_conversations_message_participant_replace"></a>

##  post_conversations_message_participant_replace(conversation_id, participant_id, body)



Replace this participant with the specified user and/or address



Wraps POST /api/v2/conversations/messages/{conversationId}/participants/{participantId}/replace 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.TransferRequest() # TransferRequest | Transfer request

try:
    # Replace this participant with the specified user and/or address
    api_instance.post_conversations_message_participant_replace(conversation_id, participant_id, body)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_message_participant_replace: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**TransferRequest**](TransferRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_messages"></a>

## [**MessageConversation**](MessageConversation.html) post_conversations_messages(body)



Create an outbound messaging conversation.

If there is an existing conversation between the remote address and the address associated with the queue specified in createOutboundRequest then the result of this request depends on the state of that conversation and the useExistingConversation field of createOutboundRequest. If the existing conversation is in alerting or connected state, then the request will fail. If the existing conversation is disconnected but still within the conversation window then the request will fail unless useExistingConversation is set to true.

Wraps POST /api/v2/conversations/messages 

Requires ANY permissions: 

* conversation:message:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.CreateOutboundMessagingConversationRequest() # CreateOutboundMessagingConversationRequest | Create outbound messaging conversation

try:
    # Create an outbound messaging conversation.
    api_response = api_instance.post_conversations_messages(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->post_conversations_messages: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateOutboundMessagingConversationRequest**](CreateOutboundMessagingConversationRequest.html)| Create outbound messaging conversation |  |
{: class="table table-striped"}

### Return type

[**MessageConversation**](MessageConversation.html)

<a name="put_conversations_call_participant_communication_uuidata"></a>

## [**Empty**](Empty.html) put_conversations_call_participant_communication_uuidata(conversation_id, participant_id, communication_id, body)



Set uuiData to be sent on future commands.



Wraps PUT /api/v2/conversations/calls/{conversationId}/participants/{participantId}/communications/{communicationId}/uuidata 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.SetUuiDataRequest() # SetUuiDataRequest | UUIData Request

try:
    # Set uuiData to be sent on future commands.
    api_response = api_instance.put_conversations_call_participant_communication_uuidata(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->put_conversations_call_participant_communication_uuidata: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**SetUuiDataRequest**](SetUuiDataRequest.html)| UUIData Request |  |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="put_conversations_email_messages_draft"></a>

## [**EmailMessage**](EmailMessage.html) put_conversations_email_messages_draft(conversation_id, body)



Update conversation draft reply



Wraps PUT /api/v2/conversations/emails/{conversationId}/messages/draft 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.EmailMessage() # EmailMessage | Draft

try:
    # Update conversation draft reply
    api_response = api_instance.put_conversations_email_messages_draft(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConversationsApi->put_conversations_email_messages_draft: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**EmailMessage**](EmailMessage.html)| Draft |  |
{: class="table table-striped"}

### Return type

[**EmailMessage**](EmailMessage.html)


---
title: TextbotsApi
---

## PureCloudPlatformClientV2.TextbotsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**post_textbots_botflows_session_turns**](TextbotsApi.html#post_textbots_botflows_session_turns) | Issue a bot flow turn event|
|[**post_textbots_botflows_sessions**](TextbotsApi.html#post_textbots_botflows_sessions) | Create an execution instance of a bot flow definition.|
|[**post_textbots_bots_execute**](TextbotsApi.html#post_textbots_bots_execute) | Send an intent to a bot to start a dialog/interact with it via text|
{: class="table table-striped"}

<a name="post_textbots_botflows_session_turns"></a>

## [**TextBotFlowTurnResponse**](TextBotFlowTurnResponse.html) post_textbots_botflows_session_turns(session_id, turn_request)



Issue a bot flow turn event

Send a turn event to an executing bot flow and produce the next action to take.

Wraps POST /api/v2/textbots/botflows/sessions/{sessionId}/turns 

Requires ANY permissions: 

* textbots:botFlowSession:execute

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TextbotsApi()
session_id = 'session_id_example' # str | The bot flow session ID, typically obtained from 'POST /api/v2/textbots/botflows/sessions'
turn_request = PureCloudPlatformClientV2.TextBotFlowTurnRequest() # TextBotFlowTurnRequest | 

try:
    # Issue a bot flow turn event
    api_response = api_instance.post_textbots_botflows_session_turns(session_id, turn_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextbotsApi->post_textbots_botflows_session_turns: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| The bot flow session ID, typically obtained from &#39;POST /api/v2/textbots/botflows/sessions&#39; |  |
| **turn_request** | [**TextBotFlowTurnRequest**](TextBotFlowTurnRequest.html)|  |  |
{: class="table table-striped"}

### Return type

[**TextBotFlowTurnResponse**](TextBotFlowTurnResponse.html)

<a name="post_textbots_botflows_sessions"></a>

## [**TextBotFlowLaunchResponse**](TextBotFlowLaunchResponse.html) post_textbots_botflows_sessions(launch_request)



Create an execution instance of a bot flow definition.

The launch is asynchronous; use the returned instance ID to post turns to it using 'POST /api/v2/textbots/botflows/sessions/{sessionId}/turns'.

Wraps POST /api/v2/textbots/botflows/sessions 

Requires ANY permissions: 

* textbots:botFlowSession:execute

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TextbotsApi()
launch_request = PureCloudPlatformClientV2.TextBotFlowLaunchRequest() # TextBotFlowLaunchRequest | 

try:
    # Create an execution instance of a bot flow definition.
    api_response = api_instance.post_textbots_botflows_sessions(launch_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextbotsApi->post_textbots_botflows_sessions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **launch_request** | [**TextBotFlowLaunchRequest**](TextBotFlowLaunchRequest.html)|  |  |
{: class="table table-striped"}

### Return type

[**TextBotFlowLaunchResponse**](TextBotFlowLaunchResponse.html)

<a name="post_textbots_bots_execute"></a>

## [**PostTextResponse**](PostTextResponse.html) post_textbots_bots_execute(post_text_request)



Send an intent to a bot to start a dialog/interact with it via text

This will either start a bot with the given id or relay a communication to an existing bot session.

Wraps POST /api/v2/textbots/bots/execute 

Requires ANY permissions: 

* textbots:session:execute

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TextbotsApi()
post_text_request = PureCloudPlatformClientV2.PostTextRequest() # PostTextRequest | 

try:
    # Send an intent to a bot to start a dialog/interact with it via text
    api_response = api_instance.post_textbots_bots_execute(post_text_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextbotsApi->post_textbots_bots_execute: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **post_text_request** | [**PostTextRequest**](PostTextRequest.html)|  |  |
{: class="table table-striped"}

### Return type

[**PostTextResponse**](PostTextResponse.html)


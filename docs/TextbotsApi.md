# TextbotsApi

## PureCloudPlatformClientV2.TextbotsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_textbots_bots_search**](#get_textbots_bots_search) | Find bots using the currently configured friendly name or ID.|
|[**post_textbots_botflows_session_turns**](#post_textbots_botflows_session_turns) | Issue a bot flow turn event|
|[**post_textbots_botflows_sessions**](#post_textbots_botflows_sessions) | Create an execution instance of a bot flow definition.|
|[**post_textbots_bots_execute**](#post_textbots_bots_execute) | Send an intent to a bot to start a dialog/interact with it via text|



## get_textbots_bots_search

> [**BotSearchResponseEntityListing**](BotSearchResponseEntityListing) get_textbots_bots_search(bot_type=bot_type, bot_name=bot_name, bot_id=bot_id, virtual_agent_enabled=virtual_agent_enabled, page_size=page_size)


Find bots using the currently configured friendly name or ID.

The name does allow case-insensitive partial string matches or by IDs (up to 50), but not both at the same time. Optionally you can limit the scope of the search by providing one or more bot types.  You can specify the maximum results to return, up to a limit of 100

Wraps GET /api/v2/textbots/bots/search 

Requires ANY permissions: 

* integrations:integration:view

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
bot_type = ['bot_type_example'] # list[str] | Bot types (optional)
bot_name = 'bot_name_example' # str | Bot name (optional)
bot_id = ['bot_id_example'] # list[str] | Bot IDs. Maximum of 50 (optional)
virtual_agent_enabled = True # bool | Include or exclude virtual agent flows, only applies to GenesysBotFlows or GenesysDigitalBotFlows (optional)
page_size = 25 # int | The maximum results to return. Maximum of 100 (optional) (default to 25)

try:
    # Find bots using the currently configured friendly name or ID.
    api_response = api_instance.get_textbots_bots_search(bot_type=bot_type, bot_name=bot_name, bot_id=bot_id, virtual_agent_enabled=virtual_agent_enabled, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextbotsApi->get_textbots_bots_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bot_type** | [**list[str]**](str)| Bot types | [optional] <br />**Values**: GenesysBotConnector, GenesysDialogEngine, AmazonLex, GoogleDialogFlowES, GoogleDialogFlowCX, NuanceDlg, GenesysBotFlow, GenesysDigitalBotFlow, GenesysVoiceSurveyFlow, GenesysDigitalBotConnector |
| **bot_name** | **str**| Bot name | [optional]  |
| **bot_id** | [**list[str]**](str)| Bot IDs. Maximum of 50 | [optional]  |
| **virtual_agent_enabled** | **bool**| Include or exclude virtual agent flows, only applies to GenesysBotFlows or GenesysDigitalBotFlows | [optional]  |
| **page_size** | **int**| The maximum results to return. Maximum of 100 | [optional] [default to 25] |

### Return type

[**BotSearchResponseEntityListing**](BotSearchResponseEntityListing)


## post_textbots_botflows_session_turns

> [**TextBotFlowTurnResponse**](TextBotFlowTurnResponse) post_textbots_botflows_session_turns(session_id, turn_request)


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
| **turn_request** | [**TextBotFlowTurnRequest**](TextBotFlowTurnRequest)|  |  |

### Return type

[**TextBotFlowTurnResponse**](TextBotFlowTurnResponse)


## post_textbots_botflows_sessions

> [**TextBotFlowLaunchResponse**](TextBotFlowLaunchResponse) post_textbots_botflows_sessions(launch_request)


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
| **launch_request** | [**TextBotFlowLaunchRequest**](TextBotFlowLaunchRequest)|  |  |

### Return type

[**TextBotFlowLaunchResponse**](TextBotFlowLaunchResponse)


## post_textbots_bots_execute

> [**PostTextResponse**](PostTextResponse) post_textbots_bots_execute(post_text_request)


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
| **post_text_request** | [**PostTextRequest**](PostTextRequest)|  |  |

### Return type

[**PostTextResponse**](PostTextResponse)


_PureCloudPlatformClientV2 247.0.0_

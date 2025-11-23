# AgentUIApi

## PureCloudPlatformClientV2.AgentUIApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_users_agentui_agents_autoanswer_agent_id_settings**](#delete_users_agentui_agents_autoanswer_agent_id_settings) | Delete agent auto answer settings|
|[**get_users_agentui_agents_autoanswer_agent_id_settings**](#get_users_agentui_agents_autoanswer_agent_id_settings) | Get agent auto answer settings|
|[**patch_users_agentui_agents_autoanswer_agent_id_settings**](#patch_users_agentui_agents_autoanswer_agent_id_settings) | Update agent auto answer settings|
|[**put_users_agentui_agents_autoanswer_agent_id_settings**](#put_users_agentui_agents_autoanswer_agent_id_settings) | Set agent auto answer settings|



## delete_users_agentui_agents_autoanswer_agent_id_settings

>  delete_users_agentui_agents_autoanswer_agent_id_settings(agent_id)


Delete agent auto answer settings

Wraps DELETE /api/v2/users/agentui/agents/autoanswer/{agentId}/settings 

Requires ANY permissions: 

* agentUI:agents:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentUIApi()
agent_id = 'agent_id_example' # str | The agent to apply the auto answer settings to

try:
    # Delete agent auto answer settings
    api_instance.delete_users_agentui_agents_autoanswer_agent_id_settings(agent_id)
except ApiException as e:
    print("Exception when calling AgentUIApi->delete_users_agentui_agents_autoanswer_agent_id_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The agent to apply the auto answer settings to |  |

### Return type

void (empty response body)


## get_users_agentui_agents_autoanswer_agent_id_settings

> [**AutoAnswerSettings**](AutoAnswerSettings) get_users_agentui_agents_autoanswer_agent_id_settings(agent_id)


Get agent auto answer settings

Wraps GET /api/v2/users/agentui/agents/autoanswer/{agentId}/settings 

Requires ANY permissions: 

* agentUI:agents:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentUIApi()
agent_id = 'agent_id_example' # str | The agent to apply the auto answer settings to

try:
    # Get agent auto answer settings
    api_response = api_instance.get_users_agentui_agents_autoanswer_agent_id_settings(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentUIApi->get_users_agentui_agents_autoanswer_agent_id_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The agent to apply the auto answer settings to |  |

### Return type

[**AutoAnswerSettings**](AutoAnswerSettings)


## patch_users_agentui_agents_autoanswer_agent_id_settings

> [**AutoAnswerSettings**](AutoAnswerSettings) patch_users_agentui_agents_autoanswer_agent_id_settings(agent_id, body)


Update agent auto answer settings

Wraps PATCH /api/v2/users/agentui/agents/autoanswer/{agentId}/settings 

Requires ANY permissions: 

* agentUI:agents:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentUIApi()
agent_id = 'agent_id_example' # str | The agent to apply the auto answer settings to
body = PureCloudPlatformClientV2.AutoAnswerSettings() # AutoAnswerSettings | AutoAnswerSettings

try:
    # Update agent auto answer settings
    api_response = api_instance.patch_users_agentui_agents_autoanswer_agent_id_settings(agent_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentUIApi->patch_users_agentui_agents_autoanswer_agent_id_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The agent to apply the auto answer settings to |  |
| **body** | [**AutoAnswerSettings**](AutoAnswerSettings)| AutoAnswerSettings |  |

### Return type

[**AutoAnswerSettings**](AutoAnswerSettings)


## put_users_agentui_agents_autoanswer_agent_id_settings

> [**AutoAnswerSettings**](AutoAnswerSettings) put_users_agentui_agents_autoanswer_agent_id_settings(agent_id, body)


Set agent auto answer settings

Wraps PUT /api/v2/users/agentui/agents/autoanswer/{agentId}/settings 

Requires ANY permissions: 

* agentUI:agents:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentUIApi()
agent_id = 'agent_id_example' # str | The agent to apply the auto answer settings to
body = PureCloudPlatformClientV2.AutoAnswerSettings() # AutoAnswerSettings | AutoAnswerSettings

try:
    # Set agent auto answer settings
    api_response = api_instance.put_users_agentui_agents_autoanswer_agent_id_settings(agent_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentUIApi->put_users_agentui_agents_autoanswer_agent_id_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The agent to apply the auto answer settings to |  |
| **body** | [**AutoAnswerSettings**](AutoAnswerSettings)| AutoAnswerSettings |  |

### Return type

[**AutoAnswerSettings**](AutoAnswerSettings)


_PureCloudPlatformClientV2 244.0.0_

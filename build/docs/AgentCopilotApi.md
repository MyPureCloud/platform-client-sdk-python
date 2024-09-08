---
title: AgentCopilotApi
---

## PureCloudPlatformClientV2.AgentCopilotApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_assistant_copilot**](AgentCopilotApi.html#get_assistant_copilot) | Get copilot configuration of an assistant.|
|[**put_assistant_copilot**](AgentCopilotApi.html#put_assistant_copilot) | Update agent copilot configuration|
{: class="table table-striped"}

<a name="get_assistant_copilot"></a>

## [**Copilot**](Copilot.html) get_assistant_copilot(assistant_id)



Get copilot configuration of an assistant.

Wraps GET /api/v2/assistants/{assistantId}/copilot 

Requires ALL permissions: 

* assistants:copilot:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentCopilotApi()
assistant_id = 'assistant_id_example' # str | Assistant ID

try:
    # Get copilot configuration of an assistant.
    api_response = api_instance.get_assistant_copilot(assistant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCopilotApi->get_assistant_copilot: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |
{: class="table table-striped"}

### Return type

[**Copilot**](Copilot.html)

<a name="put_assistant_copilot"></a>

## [**Copilot**](Copilot.html) put_assistant_copilot(assistant_id, body)



Update agent copilot configuration

Wraps PUT /api/v2/assistants/{assistantId}/copilot 

Requires ALL permissions: 

* assistants:copilot:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentCopilotApi()
assistant_id = 'assistant_id_example' # str | Assistant ID
body = PureCloudPlatformClientV2.Copilot() # Copilot | 

try:
    # Update agent copilot configuration
    api_response = api_instance.put_assistant_copilot(assistant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCopilotApi->put_assistant_copilot: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |
| **body** | [**Copilot**](Copilot.html)|  |  |
{: class="table table-striped"}

### Return type

[**Copilot**](Copilot.html)


# AgentCopilotApi

## PureCloudPlatformClientV2.AgentCopilotApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_assistant_copilot**](#get_assistant_copilot) | Get copilot configuration of an assistant.|
|[**get_assistants_copilot_featuresupport**](#get_assistants_copilot_featuresupport) | Get information about the support of features for all the languages or only for a certain language.|
|[**put_assistant_copilot**](#put_assistant_copilot) | Update agent copilot configuration|



## get_assistant_copilot

> [**Copilot**](Copilot) get_assistant_copilot(assistant_id)


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

### Return type

[**Copilot**](Copilot)


## get_assistants_copilot_featuresupport

> [**LanguageSupportResponse**](LanguageSupportResponse) get_assistants_copilot_featuresupport(language=language)


Get information about the support of features for all the languages or only for a certain language.

Wraps GET /api/v2/assistants/copilot/featuresupport 

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
language = 'language_example' # str | Which language are the features supported for (optional)

try:
    # Get information about the support of features for all the languages or only for a certain language.
    api_response = api_instance.get_assistants_copilot_featuresupport(language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentCopilotApi->get_assistants_copilot_featuresupport: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language** | **str**| Which language are the features supported for | [optional]  |

### Return type

[**LanguageSupportResponse**](LanguageSupportResponse)


## put_assistant_copilot

> [**Copilot**](Copilot) put_assistant_copilot(assistant_id, body)


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
| **body** | [**Copilot**](Copilot)|  |  |

### Return type

[**Copilot**](Copilot)


_PureCloudPlatformClientV2 244.0.0_

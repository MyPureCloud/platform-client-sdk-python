# AssistantCopilotVariationsApi

## PureCloudPlatformClientV2.AssistantCopilotVariationsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_assistant_variation**](#delete_assistant_variation) | Delete assistant copilot variation by id|
|[**get_assistant_variation**](#get_assistant_variation) | Get assistant copilot variation by id|
|[**get_assistant_variations**](#get_assistant_variations) | Get variations of an assistant copilot|
|[**post_assistant_variations**](#post_assistant_variations) | Create assistant copilot variation|
|[**put_assistant_variation**](#put_assistant_variation) | Update assistant copilot variation by id|



## delete_assistant_variation

>  delete_assistant_variation(assistant_id, variation_id)


Delete assistant copilot variation by id

Wraps DELETE /api/v2/assistants/{assistantId}/variations/{variationId} 

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
api_instance = PureCloudPlatformClientV2.AssistantCopilotVariationsApi()
assistant_id = 'assistant_id_example' # str | Assistant ID
variation_id = 'variation_id_example' # str | Variation ID

try:
    # Delete assistant copilot variation by id
    api_instance.delete_assistant_variation(assistant_id, variation_id)
except ApiException as e:
    print("Exception when calling AssistantCopilotVariationsApi->delete_assistant_variation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |
| **variation_id** | **str**| Variation ID |  |

### Return type

void (empty response body)


## get_assistant_variation

> [**AssistantCopilotVariation**](AssistantCopilotVariation) get_assistant_variation(assistant_id, variation_id)


Get assistant copilot variation by id

Wraps GET /api/v2/assistants/{assistantId}/variations/{variationId} 

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
api_instance = PureCloudPlatformClientV2.AssistantCopilotVariationsApi()
assistant_id = 'assistant_id_example' # str | Assistant ID
variation_id = 'variation_id_example' # str | Variation ID

try:
    # Get assistant copilot variation by id
    api_response = api_instance.get_assistant_variation(assistant_id, variation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantCopilotVariationsApi->get_assistant_variation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |
| **variation_id** | **str**| Variation ID |  |

### Return type

[**AssistantCopilotVariation**](AssistantCopilotVariation)


## get_assistant_variations

> [**AssistantCopilotVariationListing**](AssistantCopilotVariationListing) get_assistant_variations(assistant_id)


Get variations of an assistant copilot

Wraps GET /api/v2/assistants/{assistantId}/variations 

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
api_instance = PureCloudPlatformClientV2.AssistantCopilotVariationsApi()
assistant_id = 'assistant_id_example' # str | Assistant ID

try:
    # Get variations of an assistant copilot
    api_response = api_instance.get_assistant_variations(assistant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantCopilotVariationsApi->get_assistant_variations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |

### Return type

[**AssistantCopilotVariationListing**](AssistantCopilotVariationListing)


## post_assistant_variations

> [**AssistantCopilotVariation**](AssistantCopilotVariation) post_assistant_variations(assistant_id, body)


Create assistant copilot variation

Wraps POST /api/v2/assistants/{assistantId}/variations 

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
api_instance = PureCloudPlatformClientV2.AssistantCopilotVariationsApi()
assistant_id = 'assistant_id_example' # str | Assistant ID
body = PureCloudPlatformClientV2.AssistantCopilotVariation() # AssistantCopilotVariation | 

try:
    # Create assistant copilot variation
    api_response = api_instance.post_assistant_variations(assistant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantCopilotVariationsApi->post_assistant_variations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |
| **body** | [**AssistantCopilotVariation**](AssistantCopilotVariation)|  |  |

### Return type

[**AssistantCopilotVariation**](AssistantCopilotVariation)


## put_assistant_variation

> [**AssistantCopilotVariation**](AssistantCopilotVariation) put_assistant_variation(assistant_id, variation_id, body)


Update assistant copilot variation by id

Wraps PUT /api/v2/assistants/{assistantId}/variations/{variationId} 

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
api_instance = PureCloudPlatformClientV2.AssistantCopilotVariationsApi()
assistant_id = 'assistant_id_example' # str | Assistant ID
variation_id = 'variation_id_example' # str | Variation ID
body = PureCloudPlatformClientV2.AssistantCopilotVariation() # AssistantCopilotVariation | 

try:
    # Update assistant copilot variation by id
    api_response = api_instance.put_assistant_variation(assistant_id, variation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantCopilotVariationsApi->put_assistant_variation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |
| **variation_id** | **str**| Variation ID |  |
| **body** | [**AssistantCopilotVariation**](AssistantCopilotVariation)|  |  |

### Return type

[**AssistantCopilotVariation**](AssistantCopilotVariation)


_PureCloudPlatformClientV2 256.0.0_

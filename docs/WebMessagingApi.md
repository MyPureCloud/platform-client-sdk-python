# WebMessagingApi

## PureCloudPlatformClientV2.WebMessagingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_webmessaging_deployment_pushdevice**](#delete_webmessaging_deployment_pushdevice) | Delete device information|
|[**get_webmessaging_messages**](#get_webmessaging_messages) | Get the messages for a web messaging session.|
|[**patch_webmessaging_deployment_pushdevice**](#patch_webmessaging_deployment_pushdevice) | Edit device information|
|[**post_webmessaging_deployment_pushdevice**](#post_webmessaging_deployment_pushdevice) | Add a new device information|



## delete_webmessaging_deployment_pushdevice

>  delete_webmessaging_deployment_pushdevice(deployment_id, token_id)


Delete device information

Wraps DELETE /api/v2/webmessaging/deployments/{deploymentId}/pushdevices/{tokenId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebMessagingApi()
deployment_id = 'deployment_id_example' # str | WebMessaging deployment id
token_id = 'token_id_example' # str | Device token id or cookie id

try:
    # Delete device information
    api_instance.delete_webmessaging_deployment_pushdevice(deployment_id, token_id)
except ApiException as e:
    print("Exception when calling WebMessagingApi->delete_webmessaging_deployment_pushdevice: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| WebMessaging deployment id |  |
| **token_id** | **str**| Device token id or cookie id |  |

### Return type

void (empty response body)


## get_webmessaging_messages

> [**WebMessagingMessageEntityList**](WebMessagingMessageEntityList) get_webmessaging_messages(page_size=page_size, page_number=page_number)


Get the messages for a web messaging session.

Wraps GET /api/v2/webmessaging/messages 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebMessagingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get the messages for a web messaging session.
    api_response = api_instance.get_webmessaging_messages(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebMessagingApi->get_webmessaging_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**WebMessagingMessageEntityList**](WebMessagingMessageEntityList)


## patch_webmessaging_deployment_pushdevice

>  patch_webmessaging_deployment_pushdevice(deployment_id, token_id, body)


Edit device information

Wraps PATCH /api/v2/webmessaging/deployments/{deploymentId}/pushdevices/{tokenId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebMessagingApi()
deployment_id = 'deployment_id_example' # str | WebMessaging deployment id
token_id = 'token_id_example' # str | Device token id or cookie id
body = PureCloudPlatformClientV2.PushDeviceUpdateRequest() # PushDeviceUpdateRequest | Request body

try:
    # Edit device information
    api_instance.patch_webmessaging_deployment_pushdevice(deployment_id, token_id, body)
except ApiException as e:
    print("Exception when calling WebMessagingApi->patch_webmessaging_deployment_pushdevice: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| WebMessaging deployment id |  |
| **token_id** | **str**| Device token id or cookie id |  |
| **body** | [**PushDeviceUpdateRequest**](PushDeviceUpdateRequest)| Request body |  |

### Return type

void (empty response body)


## post_webmessaging_deployment_pushdevice

>  post_webmessaging_deployment_pushdevice(deployment_id, token_id, body)


Add a new device information

Wraps POST /api/v2/webmessaging/deployments/{deploymentId}/pushdevices/{tokenId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebMessagingApi()
deployment_id = 'deployment_id_example' # str | WebMessaging deployment id
token_id = 'token_id_example' # str | Device token id or cookie id
body = PureCloudPlatformClientV2.PushDeviceInsertRequest() # PushDeviceInsertRequest | Request body

try:
    # Add a new device information
    api_instance.post_webmessaging_deployment_pushdevice(deployment_id, token_id, body)
except ApiException as e:
    print("Exception when calling WebMessagingApi->post_webmessaging_deployment_pushdevice: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| WebMessaging deployment id |  |
| **token_id** | **str**| Device token id or cookie id |  |
| **body** | [**PushDeviceInsertRequest**](PushDeviceInsertRequest)| Request body |  |

### Return type

void (empty response body)


_PureCloudPlatformClientV2 239.0.0_

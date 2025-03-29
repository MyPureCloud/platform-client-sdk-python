# WebMessagingApi

## PureCloudPlatformClientV2.WebMessagingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_webmessaging_messages**](#get_webmessaging_messages) | Get the messages for a web messaging session.|



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


_PureCloudPlatformClientV2 224.1.0_

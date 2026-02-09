# BackgroundAssistantApi

## PureCloudPlatformClientV2.BackgroundAssistantApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**post_backgroundassistant_token**](#post_backgroundassistant_token) | Sign identifying information for Genesys Cloud Background Assistant|
|[**post_screenrecording_token**](#post_screenrecording_token) | Sign identifying information for screen recording|



## post_backgroundassistant_token

> [**SignedData**](SignedData) post_backgroundassistant_token(body=body)


Sign identifying information for Genesys Cloud Background Assistant

post_backgroundassistant_token is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/backgroundassistant/token 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BackgroundAssistantApi()
body = PureCloudPlatformClientV2.BackgroundAssistantUserAuthenticatedInfo() # BackgroundAssistantUserAuthenticatedInfo |  (optional)

try:
    # Sign identifying information for Genesys Cloud Background Assistant
    api_response = api_instance.post_backgroundassistant_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackgroundAssistantApi->post_backgroundassistant_token: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BackgroundAssistantUserAuthenticatedInfo**](BackgroundAssistantUserAuthenticatedInfo)|  | [optional]  |

### Return type

[**SignedData**](SignedData)


## post_screenrecording_token

> [**SignedData**](SignedData) post_screenrecording_token(body=body)


Sign identifying information for screen recording

Wraps POST /api/v2/screenrecording/token 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.BackgroundAssistantApi()
body = PureCloudPlatformClientV2.BackgroundAssistantUserAuthenticatedInfo() # BackgroundAssistantUserAuthenticatedInfo |  (optional)

try:
    # Sign identifying information for screen recording
    api_response = api_instance.post_screenrecording_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackgroundAssistantApi->post_screenrecording_token: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BackgroundAssistantUserAuthenticatedInfo**](BackgroundAssistantUserAuthenticatedInfo)|  | [optional]  |

### Return type

[**SignedData**](SignedData)


_PureCloudPlatformClientV2 250.0.0_

---
title: ScreenRecordingApi
---

## PureCloudPlatformClientV2.ScreenRecordingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**post_screenrecording_token**](ScreenRecordingApi.html#post_screenrecording_token) | Sign identifying information for screen recording|
{: class="table table-striped"}

<a name="post_screenrecording_token"></a>

## [**SignedData**](SignedData.html) post_screenrecording_token(body=body)



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
api_instance = PureCloudPlatformClientV2.ScreenRecordingApi()
body = PureCloudPlatformClientV2.ScreenRecordingUserAuthenticatedInfo() # ScreenRecordingUserAuthenticatedInfo |  (optional)

try:
    # Sign identifying information for screen recording
    api_response = api_instance.post_screenrecording_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenRecordingApi->post_screenrecording_token: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ScreenRecordingUserAuthenticatedInfo**](ScreenRecordingUserAuthenticatedInfo.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**SignedData**](SignedData.html)


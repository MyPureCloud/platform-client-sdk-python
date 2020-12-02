---
title: TextbotsApi
---

## PureCloudPlatformClientV2.TextbotsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**post_textbots_bots_execute**](TextbotsApi.html#post_textbots_bots_execute) | Send an intent to a bot to start a dialog/interact with it via text|
{: class="table table-striped"}

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


---
title: MessagingApi
---

## PureCloudPlatformClientV2.MessagingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_messaging_sticker**](MessagingApi.html#get_messaging_sticker) | Get a list of Messaging Stickers|
{: class="table table-striped"}

<a name="get_messaging_sticker"></a>

## [**MessagingStickerEntityListing**](MessagingStickerEntityListing.html) get_messaging_sticker(messenger_type, page_size=page_size, page_number=page_number)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get a list of Messaging Stickers



Wraps GET /api/v2/messaging/stickers/{messengerType} 

Requires ANY permissions: 

* conversation:message:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
messenger_type = 'messenger_type_example' # str | Messenger Type
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of Messaging Stickers
    api_response = api_instance.get_messaging_sticker(messenger_type, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->get_messaging_sticker: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messenger_type** | **str**| Messenger Type |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**MessagingStickerEntityListing**](MessagingStickerEntityListing.html)


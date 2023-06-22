---
title: MessagingApi
---

## PureCloudPlatformClientV2.MessagingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_messaging_supportedcontent_supported_content_id**](MessagingApi.html#delete_messaging_supportedcontent_supported_content_id) | Delete a supported content profile|
|[**get_messaging_supportedcontent**](MessagingApi.html#get_messaging_supportedcontent) | Get a list of Supported Content profiles|
|[**get_messaging_supportedcontent_supported_content_id**](MessagingApi.html#get_messaging_supportedcontent_supported_content_id) | Get a supported content profile|
|[**patch_messaging_supportedcontent_supported_content_id**](MessagingApi.html#patch_messaging_supportedcontent_supported_content_id) | Update a supported content profile|
|[**post_messaging_supportedcontent**](MessagingApi.html#post_messaging_supportedcontent) | Create a Supported Content profile|
{: class="table table-striped"}

<a name="delete_messaging_supportedcontent_supported_content_id"></a>

##  delete_messaging_supportedcontent_supported_content_id(supported_content_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Delete a supported content profile

Deprecated - use DELETE /api/v2/conversations/messaging/supportedcontent/{supportedContentId} as replacement

Wraps DELETE /api/v2/messaging/supportedcontent/{supportedContentId} 

Requires ALL permissions: 

* messaging:supportedContent:delete

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
supported_content_id = 'supported_content_id_example' # str | Supported Content ID

try:
    # Delete a supported content profile
    api_instance.delete_messaging_supportedcontent_supported_content_id(supported_content_id)
except ApiException as e:
    print("Exception when calling MessagingApi->delete_messaging_supportedcontent_supported_content_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **supported_content_id** | **str**| Supported Content ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_messaging_supportedcontent"></a>

## [**SupportedContentListing**](SupportedContentListing.html) get_messaging_supportedcontent(page_size=page_size, page_number=page_number)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get a list of Supported Content profiles

Deprecated - use GET /api/v2/conversations/messaging/supportedcontent as replacement

Wraps GET /api/v2/messaging/supportedcontent 

Requires ALL permissions: 

* messaging:supportedContent:view

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
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of Supported Content profiles
    api_response = api_instance.get_messaging_supportedcontent(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->get_messaging_supportedcontent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**SupportedContentListing**](SupportedContentListing.html)

<a name="get_messaging_supportedcontent_supported_content_id"></a>

## [**SupportedContent**](SupportedContent.html) get_messaging_supportedcontent_supported_content_id(supported_content_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get a supported content profile

Deprecated - use GET /api/v2/conversations/messaging/supportedcontent/{supportedContentId} as replacement

Wraps GET /api/v2/messaging/supportedcontent/{supportedContentId} 

Requires ALL permissions: 

* messaging:supportedContent:view

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
supported_content_id = 'supported_content_id_example' # str | Supported Content ID

try:
    # Get a supported content profile
    api_response = api_instance.get_messaging_supportedcontent_supported_content_id(supported_content_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->get_messaging_supportedcontent_supported_content_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **supported_content_id** | **str**| Supported Content ID |  |
{: class="table table-striped"}

### Return type

[**SupportedContent**](SupportedContent.html)

<a name="patch_messaging_supportedcontent_supported_content_id"></a>

## [**SupportedContent**](SupportedContent.html) patch_messaging_supportedcontent_supported_content_id(supported_content_id, body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update a supported content profile

Deprecated - use PATCH /api/v2/conversations/messaging/supportedcontent/{supportedContentId} as replacement

Wraps PATCH /api/v2/messaging/supportedcontent/{supportedContentId} 

Requires ALL permissions: 

* messaging:supportedContent:edit

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
supported_content_id = 'supported_content_id_example' # str | Supported Content ID
body = PureCloudPlatformClientV2.SupportedContent() # SupportedContent | SupportedContent

try:
    # Update a supported content profile
    api_response = api_instance.patch_messaging_supportedcontent_supported_content_id(supported_content_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->patch_messaging_supportedcontent_supported_content_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **supported_content_id** | **str**| Supported Content ID |  |
| **body** | [**SupportedContent**](SupportedContent.html)| SupportedContent |  |
{: class="table table-striped"}

### Return type

[**SupportedContent**](SupportedContent.html)

<a name="post_messaging_supportedcontent"></a>

## [**SupportedContent**](SupportedContent.html) post_messaging_supportedcontent(body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Create a Supported Content profile

Deprecated - use POST /api/v2/conversations/messaging/supportedcontent as replacement

Wraps POST /api/v2/messaging/supportedcontent 

Requires ANY permissions: 

* messaging:supportedContent:add

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
body = PureCloudPlatformClientV2.SupportedContent() # SupportedContent | SupportedContent

try:
    # Create a Supported Content profile
    api_response = api_instance.post_messaging_supportedcontent(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->post_messaging_supportedcontent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SupportedContent**](SupportedContent.html)| SupportedContent |  |
{: class="table table-striped"}

### Return type

[**SupportedContent**](SupportedContent.html)


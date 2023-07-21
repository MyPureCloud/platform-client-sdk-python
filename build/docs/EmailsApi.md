---
title: EmailsApi
---

## PureCloudPlatformClientV2.EmailsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_emails_settings**](EmailsApi.html#get_emails_settings) | Get email Contact Center settings|
|[**patch_emails_settings**](EmailsApi.html#patch_emails_settings) | Patch email Contact Center settings|
{: class="table table-striped"}

<a name="get_emails_settings"></a>

## [**EmailSettings**](EmailSettings.html) get_emails_settings()



Get email Contact Center settings

Wraps GET /api/v2/emails/settings 

Requires ANY permissions: 

* conversation:settings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.EmailsApi()

try:
    # Get email Contact Center settings
    api_response = api_instance.get_emails_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailsApi->get_emails_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**EmailSettings**](EmailSettings.html)

<a name="patch_emails_settings"></a>

## [**EmailSettings**](EmailSettings.html) patch_emails_settings(body=body)



Patch email Contact Center settings

Wraps PATCH /api/v2/emails/settings 

Requires ANY permissions: 

* conversation:settings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.EmailsApi()
body = PureCloudPlatformClientV2.EmailSettings() # EmailSettings |  (optional)

try:
    # Patch email Contact Center settings
    api_response = api_instance.patch_emails_settings(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailsApi->patch_emails_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EmailSettings**](EmailSettings.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**EmailSettings**](EmailSettings.html)


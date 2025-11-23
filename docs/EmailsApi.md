# EmailsApi

## PureCloudPlatformClientV2.EmailsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_emails_settings_threading**](#delete_emails_settings_threading) | Reset email threading settings to default|
|[**get_emails_settings**](#get_emails_settings) | Get email Contact Center settings|
|[**get_emails_settings_threading**](#get_emails_settings_threading) | Get email threading settings|
|[**patch_emails_settings**](#patch_emails_settings) | Patch email Contact Center settings|
|[**patch_emails_settings_threading**](#patch_emails_settings_threading) | Patch email threading settings|



## delete_emails_settings_threading

>  delete_emails_settings_threading()


Reset email threading settings to default

Wraps DELETE /api/v2/emails/settings/threading 

Requires ANY permissions: 

* conversation:emailThreadingSettings:edit

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
    # Reset email threading settings to default
    api_instance.delete_emails_settings_threading()
except ApiException as e:
    print("Exception when calling EmailsApi->delete_emails_settings_threading: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

void (empty response body)


## get_emails_settings

> [**EmailSettings**](EmailSettings) get_emails_settings()


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

[**EmailSettings**](EmailSettings)


## get_emails_settings_threading

> [**EmailThreadingSettings**](EmailThreadingSettings) get_emails_settings_threading()


Get email threading settings

Wraps GET /api/v2/emails/settings/threading 

Requires ANY permissions: 

* conversation:emailThreadingSettings:view

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
    # Get email threading settings
    api_response = api_instance.get_emails_settings_threading()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailsApi->get_emails_settings_threading: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**EmailThreadingSettings**](EmailThreadingSettings)


## patch_emails_settings

> [**EmailSettings**](EmailSettings) patch_emails_settings(body=body)


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
| **body** | [**EmailSettings**](EmailSettings)|  | [optional]  |

### Return type

[**EmailSettings**](EmailSettings)


## patch_emails_settings_threading

> [**EmailThreadingSettings**](EmailThreadingSettings) patch_emails_settings_threading(body=body)


Patch email threading settings

Wraps PATCH /api/v2/emails/settings/threading 

Requires ANY permissions: 

* conversation:emailThreadingSettings:edit

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
body = PureCloudPlatformClientV2.EmailThreadingSettings() # EmailThreadingSettings |  (optional)

try:
    # Patch email threading settings
    api_response = api_instance.patch_emails_settings_threading(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailsApi->patch_emails_settings_threading: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EmailThreadingSettings**](EmailThreadingSettings)|  | [optional]  |

### Return type

[**EmailThreadingSettings**](EmailThreadingSettings)


_PureCloudPlatformClientV2 244.0.0_

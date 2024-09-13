# MessagingApi

## PureCloudPlatformClientV2.MessagingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_messaging_setting**](#delete_messaging_setting) | Delete a messaging setting|
|[**delete_messaging_settings_default**](#delete_messaging_settings_default) | Delete the organization&#39;s default setting, a global default will be applied to integrations without settings|
|[**delete_messaging_supportedcontent_supported_content_id**](#delete_messaging_supportedcontent_supported_content_id) | Delete a supported content profile|
|[**get_messaging_setting**](#get_messaging_setting) | Get a messaging setting|
|[**get_messaging_settings**](#get_messaging_settings) | Get a list of messaging settings|
|[**get_messaging_settings_default**](#get_messaging_settings_default) | Get the organization&#39;s default settings that will be used as the default when creating an integration.|
|[**get_messaging_supportedcontent**](#get_messaging_supportedcontent) | Get a list of Supported Content profiles|
|[**get_messaging_supportedcontent_supported_content_id**](#get_messaging_supportedcontent_supported_content_id) | Get a supported content profile|
|[**patch_messaging_setting**](#patch_messaging_setting) | Update a messaging setting|
|[**patch_messaging_supportedcontent_supported_content_id**](#patch_messaging_supportedcontent_supported_content_id) | Update a supported content profile|
|[**post_messaging_settings**](#post_messaging_settings) | Create a messaging setting|
|[**post_messaging_supportedcontent**](#post_messaging_supportedcontent) | Create a Supported Content profile|
|[**put_messaging_settings_default**](#put_messaging_settings_default) | Set the organization&#39;s default settings that may be applied to an integration when it is created.|



## delete_messaging_setting

>  delete_messaging_setting(message_setting_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Delete a messaging setting

Wraps DELETE /api/v2/messaging/settings/{messageSettingId} 

Requires ALL permissions: 

* messaging:setting:delete

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
message_setting_id = 'message_setting_id_example' # str | Message Settings ID

try:
    # Delete a messaging setting
    api_instance.delete_messaging_setting(message_setting_id)
except ApiException as e:
    print("Exception when calling MessagingApi->delete_messaging_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_setting_id** | **str**| Message Settings ID |  |

### Return type

void (empty response body)


## delete_messaging_settings_default

>  delete_messaging_settings_default()

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Delete the organization's default setting, a global default will be applied to integrations without settings

When an integration is created a settings ID may be assigned to it. If the settings ID is not supplied, the default settings will be applied to it.

Wraps DELETE /api/v2/messaging/settings/default 

Requires ALL permissions: 

* messaging:setting:delete

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

try:
    # Delete the organization's default setting, a global default will be applied to integrations without settings
    api_instance.delete_messaging_settings_default()
except ApiException as e:
    print("Exception when calling MessagingApi->delete_messaging_settings_default: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

void (empty response body)


## delete_messaging_supportedcontent_supported_content_id

>  delete_messaging_supportedcontent_supported_content_id(supported_content_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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

### Return type

void (empty response body)


## get_messaging_setting

> [**MessagingSetting**](MessagingSetting) get_messaging_setting(message_setting_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get a messaging setting

Wraps GET /api/v2/messaging/settings/{messageSettingId} 

Requires ALL permissions: 

* messaging:setting:view

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
message_setting_id = 'message_setting_id_example' # str | Message Settings ID

try:
    # Get a messaging setting
    api_response = api_instance.get_messaging_setting(message_setting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->get_messaging_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_setting_id** | **str**| Message Settings ID |  |

### Return type

[**MessagingSetting**](MessagingSetting)


## get_messaging_settings

> [**MessagingConfigListing**](MessagingConfigListing) get_messaging_settings(page_size=page_size, page_number=page_number)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get a list of messaging settings

Wraps GET /api/v2/messaging/settings 

Requires ALL permissions: 

* messaging:setting:view

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
    # Get a list of messaging settings
    api_response = api_instance.get_messaging_settings(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->get_messaging_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**MessagingConfigListing**](MessagingConfigListing)


## get_messaging_settings_default

> [**MessagingSetting**](MessagingSetting) get_messaging_settings_default()

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get the organization's default settings that will be used as the default when creating an integration.

When an integration is created a settings ID may be assigned to it. If the settings ID is not supplied, the default settings will be applied to it.

Wraps GET /api/v2/messaging/settings/default 

Requires ALL permissions: 

* messaging:setting:view

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

try:
    # Get the organization's default settings that will be used as the default when creating an integration.
    api_response = api_instance.get_messaging_settings_default()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->get_messaging_settings_default: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**MessagingSetting**](MessagingSetting)


## get_messaging_supportedcontent

> [**SupportedContentListing**](SupportedContentListing) get_messaging_supportedcontent(page_size=page_size, page_number=page_number)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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

### Return type

[**SupportedContentListing**](SupportedContentListing)


## get_messaging_supportedcontent_supported_content_id

> [**SupportedContent**](SupportedContent) get_messaging_supportedcontent_supported_content_id(supported_content_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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

### Return type

[**SupportedContent**](SupportedContent)


## patch_messaging_setting

> [**MessagingSetting**](MessagingSetting) patch_messaging_setting(message_setting_id, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Update a messaging setting

Wraps PATCH /api/v2/messaging/settings/{messageSettingId} 

Requires ALL permissions: 

* messaging:setting:edit

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
message_setting_id = 'message_setting_id_example' # str | Message Settings ID
body = PureCloudPlatformClientV2.MessagingSettingRequest() # MessagingSettingRequest | MessagingSetting

try:
    # Update a messaging setting
    api_response = api_instance.patch_messaging_setting(message_setting_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->patch_messaging_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_setting_id** | **str**| Message Settings ID |  |
| **body** | [**MessagingSettingRequest**](MessagingSettingRequest)| MessagingSetting |  |

### Return type

[**MessagingSetting**](MessagingSetting)


## patch_messaging_supportedcontent_supported_content_id

> [**SupportedContent**](SupportedContent) patch_messaging_supportedcontent_supported_content_id(supported_content_id, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
| **body** | [**SupportedContent**](SupportedContent)| SupportedContent |  |

### Return type

[**SupportedContent**](SupportedContent)


## post_messaging_settings

> [**MessagingSetting**](MessagingSetting) post_messaging_settings(body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Create a messaging setting

Wraps POST /api/v2/messaging/settings 

Requires ANY permissions: 

* messaging:setting:add

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
body = PureCloudPlatformClientV2.MessagingSettingRequest() # MessagingSettingRequest | MessagingSetting

try:
    # Create a messaging setting
    api_response = api_instance.post_messaging_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->post_messaging_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**MessagingSettingRequest**](MessagingSettingRequest)| MessagingSetting |  |

### Return type

[**MessagingSetting**](MessagingSetting)


## post_messaging_supportedcontent

> [**SupportedContent**](SupportedContent) post_messaging_supportedcontent(body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
| **body** | [**SupportedContent**](SupportedContent)| SupportedContent |  |

### Return type

[**SupportedContent**](SupportedContent)


## put_messaging_settings_default

> [**MessagingSetting**](MessagingSetting) put_messaging_settings_default(body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Set the organization's default settings that may be applied to an integration when it is created.

When an integration is created a settings ID may be assigned to it. If the settings ID is not supplied, the default settings will be applied to it.

Wraps PUT /api/v2/messaging/settings/default 

Requires ALL permissions: 

* messaging:setting:edit

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
body = PureCloudPlatformClientV2.MessagingSettingDefaultRequest() # MessagingSettingDefaultRequest | Messaging Setting ID

try:
    # Set the organization's default settings that may be applied to an integration when it is created.
    api_response = api_instance.put_messaging_settings_default(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->put_messaging_settings_default: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**MessagingSettingDefaultRequest**](MessagingSettingDefaultRequest)| Messaging Setting ID |  |

### Return type

[**MessagingSetting**](MessagingSetting)


_PureCloudPlatformClientV2 211.0.0_

# MobileDevicesApi

## PureCloudPlatformClientV2.MobileDevicesApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_mobiledevice**](#delete_mobiledevice) | (Deprecated, see https://apicentral.genesys.cloud/api-explorer#webmessaging for alternative) Delete device|
|[**get_mobiledevice**](#get_mobiledevice) | (Deprecated) Get device|
|[**get_mobiledevices**](#get_mobiledevices) | (Deprecated) Get a list of all devices.|
|[**post_mobiledevices**](#post_mobiledevices) | (Deprecated, see https://apicentral.genesys.cloud/api-explorer#webmessaging for alternative) Create User device|
|[**put_mobiledevice**](#put_mobiledevice) | (Deprecated, see https://apicentral.genesys.cloud/api-explorer#webmessaging for alternative) Update device|



## delete_mobiledevice

>  delete_mobiledevice(device_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

(Deprecated, see https://apicentral.genesys.cloud/api-explorer#webmessaging for alternative) Delete device

Wraps DELETE /api/v2/mobiledevices/{deviceId} 

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
api_instance = PureCloudPlatformClientV2.MobileDevicesApi()
device_id = 'device_id_example' # str | Device ID

try:
    # (Deprecated, see https://apicentral.genesys.cloud/api-explorer#webmessaging for alternative) Delete device
    api_instance.delete_mobiledevice(device_id)
except ApiException as e:
    print("Exception when calling MobileDevicesApi->delete_mobiledevice: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **device_id** | **str**| Device ID |  |

### Return type

void (empty response body)


## get_mobiledevice

> [**UserDevice**](UserDevice) get_mobiledevice(device_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

(Deprecated) Get device

Wraps GET /api/v2/mobiledevices/{deviceId} 

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
api_instance = PureCloudPlatformClientV2.MobileDevicesApi()
device_id = 'device_id_example' # str | Device ID

try:
    # (Deprecated) Get device
    api_response = api_instance.get_mobiledevice(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileDevicesApi->get_mobiledevice: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **device_id** | **str**| Device ID |  |

### Return type

[**UserDevice**](UserDevice)


## get_mobiledevices

> [**DirectoryUserDevicesListing**](DirectoryUserDevicesListing) get_mobiledevices(page_size=page_size, page_number=page_number, sort_order=sort_order)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

(Deprecated) Get a list of all devices.

Wraps GET /api/v2/mobiledevices 

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
api_instance = PureCloudPlatformClientV2.MobileDevicesApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''ascending'' # str | Ascending or descending sort order (optional) (default to 'ascending')

try:
    # (Deprecated) Get a list of all devices.
    api_response = api_instance.get_mobiledevices(page_size=page_size, page_number=page_number, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileDevicesApi->get_mobiledevices: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;ascending&#39;]<br />**Values**: ascending, descending |

### Return type

[**DirectoryUserDevicesListing**](DirectoryUserDevicesListing)


## post_mobiledevices

> [**UserDevice**](UserDevice) post_mobiledevices(body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

(Deprecated, see https://apicentral.genesys.cloud/api-explorer#webmessaging for alternative) Create User device

Wraps POST /api/v2/mobiledevices 

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
api_instance = PureCloudPlatformClientV2.MobileDevicesApi()
body = PureCloudPlatformClientV2.UserDevice() # UserDevice | Device

try:
    # (Deprecated, see https://apicentral.genesys.cloud/api-explorer#webmessaging for alternative) Create User device
    api_response = api_instance.post_mobiledevices(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileDevicesApi->post_mobiledevices: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserDevice**](UserDevice)| Device |  |

### Return type

[**UserDevice**](UserDevice)


## put_mobiledevice

> [**UserDevice**](UserDevice) put_mobiledevice(device_id, body=body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

(Deprecated, see https://apicentral.genesys.cloud/api-explorer#webmessaging for alternative) Update device

Wraps PUT /api/v2/mobiledevices/{deviceId} 

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
api_instance = PureCloudPlatformClientV2.MobileDevicesApi()
device_id = 'device_id_example' # str | Device ID
body = PureCloudPlatformClientV2.UserDevice() # UserDevice | Device (optional)

try:
    # (Deprecated, see https://apicentral.genesys.cloud/api-explorer#webmessaging for alternative) Update device
    api_response = api_instance.put_mobiledevice(device_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileDevicesApi->put_mobiledevice: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **device_id** | **str**| Device ID |  |
| **body** | [**UserDevice**](UserDevice)| Device | [optional]  |

### Return type

[**UserDevice**](UserDevice)


_PureCloudPlatformClientV2 266.0.0_

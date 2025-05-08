# GeolocationApi

## PureCloudPlatformClientV2.GeolocationApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_geolocations_settings**](#get_geolocations_settings) | Get a organization&#39;s GeolocationSettings|
|[**get_user_geolocation**](#get_user_geolocation) | Get a user&#39;s Geolocation|
|[**patch_geolocations_settings**](#patch_geolocations_settings) | Patch a organization&#39;s GeolocationSettings|
|[**patch_user_geolocation**](#patch_user_geolocation) | Patch a user&#39;s Geolocation|



## get_geolocations_settings

> [**GeolocationSettings**](GeolocationSettings) get_geolocations_settings()


Get a organization's GeolocationSettings

Wraps GET /api/v2/geolocations/settings 

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
api_instance = PureCloudPlatformClientV2.GeolocationApi()

try:
    # Get a organization's GeolocationSettings
    api_response = api_instance.get_geolocations_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeolocationApi->get_geolocations_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**GeolocationSettings**](GeolocationSettings)


## get_user_geolocation

> [**Geolocation**](Geolocation) get_user_geolocation(user_id, client_id)


Get a user's Geolocation

Wraps GET /api/v2/users/{userId}/geolocations/{clientId} 

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
api_instance = PureCloudPlatformClientV2.GeolocationApi()
user_id = 'user_id_example' # str | user Id
client_id = 'client_id_example' # str | client Id

try:
    # Get a user's Geolocation
    api_response = api_instance.get_user_geolocation(user_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeolocationApi->get_user_geolocation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| user Id |  |
| **client_id** | **str**| client Id |  |

### Return type

[**Geolocation**](Geolocation)


## patch_geolocations_settings

> [**GeolocationSettings**](GeolocationSettings) patch_geolocations_settings(body)


Patch a organization's GeolocationSettings

Wraps PATCH /api/v2/geolocations/settings 

Requires ANY permissions: 

* geolocation:settings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GeolocationApi()
body = PureCloudPlatformClientV2.GeolocationSettings() # GeolocationSettings | Geolocation settings

try:
    # Patch a organization's GeolocationSettings
    api_response = api_instance.patch_geolocations_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeolocationApi->patch_geolocations_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GeolocationSettings**](GeolocationSettings)| Geolocation settings |  |

### Return type

[**GeolocationSettings**](GeolocationSettings)


## patch_user_geolocation

> [**Geolocation**](Geolocation) patch_user_geolocation(user_id, client_id, body)


Patch a user's Geolocation

The geolocation object can be patched one of three ways. Option 1: Set the 'primary' property to true. This will set the client as the user's primary geolocation source.  Option 2: Provide the 'latitude' and 'longitude' values.  This will enqueue an asynchronous update of the 'city', 'region', and 'country', generating a notification. A subsequent GET operation will include the new values for 'city', 'region' and 'country'.  Option 3:  Provide the 'city', 'region', 'country' values.  Option 1 can be combined with Option 2 or Option 3.  For example, update the client as primary and provide latitude and longitude values.

Wraps PATCH /api/v2/users/{userId}/geolocations/{clientId} 

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
api_instance = PureCloudPlatformClientV2.GeolocationApi()
user_id = 'user_id_example' # str | user Id
client_id = 'client_id_example' # str | client Id
body = PureCloudPlatformClientV2.Geolocation() # Geolocation | Geolocation

try:
    # Patch a user's Geolocation
    api_response = api_instance.patch_user_geolocation(user_id, client_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeolocationApi->patch_user_geolocation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| user Id |  |
| **client_id** | **str**| client Id |  |
| **body** | [**Geolocation**](Geolocation)| Geolocation |  |

### Return type

[**Geolocation**](Geolocation)


_PureCloudPlatformClientV2 227.1.0_

# CarrierServicesApi

## PureCloudPlatformClientV2.CarrierServicesApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_carrierservices_integrations_emergencylocations_me**](#get_carrierservices_integrations_emergencylocations_me) | Get location for the logged in user|
|[**post_carrierservices_integrations_emergencylocations_me**](#post_carrierservices_integrations_emergencylocations_me) | Set current location for the logged in user|



## get_carrierservices_integrations_emergencylocations_me

> [**EmergencyLocation**](EmergencyLocation) get_carrierservices_integrations_emergencylocations_me(phone_number)


Get location for the logged in user

Wraps GET /api/v2/carrierservices/integrations/emergencylocations/me 

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
api_instance = PureCloudPlatformClientV2.CarrierServicesApi()
phone_number = 'phone_number_example' # str | Phone number in E164 format

try:
    # Get location for the logged in user
    api_response = api_instance.get_carrierservices_integrations_emergencylocations_me(phone_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarrierServicesApi->get_carrierservices_integrations_emergencylocations_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phone_number** | **str**| Phone number in E164 format |  |

### Return type

[**EmergencyLocation**](EmergencyLocation)


## post_carrierservices_integrations_emergencylocations_me

> [**EmergencyLocation**](EmergencyLocation) post_carrierservices_integrations_emergencylocations_me(body=body)


Set current location for the logged in user

Wraps POST /api/v2/carrierservices/integrations/emergencylocations/me 

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
api_instance = PureCloudPlatformClientV2.CarrierServicesApi()
body = PureCloudPlatformClientV2.EmergencyLocation() # EmergencyLocation |  (optional)

try:
    # Set current location for the logged in user
    api_response = api_instance.post_carrierservices_integrations_emergencylocations_me(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarrierServicesApi->post_carrierservices_integrations_emergencylocations_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EmergencyLocation**](EmergencyLocation)|  | [optional]  |

### Return type

[**EmergencyLocation**](EmergencyLocation)


_PureCloudPlatformClientV2 239.0.0_

# UtilitiesApi

## PureCloudPlatformClientV2.UtilitiesApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_date**](#get_date) | Get the current system date/time|
|[**get_ipranges**](#get_ipranges) | Get public ip address ranges for Genesys Cloud|
|[**get_timezones**](#get_timezones) | Get time zones list|
|[**post_certificate_details**](#post_certificate_details) | Returns the information about an X509 PEM encoded certificate or certificate chain.|



## get_date

> [**ServerDate**](ServerDate) get_date()


Get the current system date/time

Wraps GET /api/v2/date 

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
api_instance = PureCloudPlatformClientV2.UtilitiesApi()

try:
    # Get the current system date/time
    api_response = api_instance.get_date()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->get_date: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**ServerDate**](ServerDate)


## get_ipranges

> [**IpAddressRangeListing**](IpAddressRangeListing) get_ipranges()


Get public ip address ranges for Genesys Cloud

Wraps GET /api/v2/ipranges 

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
api_instance = PureCloudPlatformClientV2.UtilitiesApi()

try:
    # Get public ip address ranges for Genesys Cloud
    api_response = api_instance.get_ipranges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->get_ipranges: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**IpAddressRangeListing**](IpAddressRangeListing)


## get_timezones

> [**TimeZoneEntityListing**](TimeZoneEntityListing) get_timezones(page_size=page_size, page_number=page_number)


Get time zones list

Wraps GET /api/v2/timezones 

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
api_instance = PureCloudPlatformClientV2.UtilitiesApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get time zones list
    api_response = api_instance.get_timezones(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->get_timezones: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**TimeZoneEntityListing**](TimeZoneEntityListing)


## post_certificate_details

> [**ParsedCertificate**](ParsedCertificate) post_certificate_details(body)


Returns the information about an X509 PEM encoded certificate or certificate chain.

Wraps POST /api/v2/certificate/details 

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
api_instance = PureCloudPlatformClientV2.UtilitiesApi()
body = PureCloudPlatformClientV2.Certificate() # Certificate | Certificate

try:
    # Returns the information about an X509 PEM encoded certificate or certificate chain.
    api_response = api_instance.post_certificate_details(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->post_certificate_details: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Certificate**](Certificate)| Certificate |  |

### Return type

[**ParsedCertificate**](ParsedCertificate)


_PureCloudPlatformClientV2 211.1.0_

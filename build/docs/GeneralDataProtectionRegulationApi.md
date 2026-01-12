# GeneralDataProtectionRegulationApi

## PureCloudPlatformClientV2.GeneralDataProtectionRegulationApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_gdpr_request**](#get_gdpr_request) | Get an existing GDPR request|
|[**get_gdpr_requests**](#get_gdpr_requests) | Get all GDPR requests|
|[**get_gdpr_subjects**](#get_gdpr_subjects) | Get GDPR subjects|
|[**post_gdpr_requests**](#post_gdpr_requests) | Submit a new GDPR request|



## get_gdpr_request

> [**GDPRRequest**](GDPRRequest) get_gdpr_request(request_id)


Get an existing GDPR request

Wraps GET /api/v2/gdpr/requests/{requestId} 

Requires ANY permissions: 

* gdpr:request:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GeneralDataProtectionRegulationApi()
request_id = 'request_id_example' # str | Request id

try:
    # Get an existing GDPR request
    api_response = api_instance.get_gdpr_request(request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralDataProtectionRegulationApi->get_gdpr_request: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **request_id** | **str**| Request id |  |

### Return type

[**GDPRRequest**](GDPRRequest)


## get_gdpr_requests

> [**GDPRRequestEntityListing**](GDPRRequestEntityListing) get_gdpr_requests(page_size=page_size, page_number=page_number)


Get all GDPR requests

Wraps GET /api/v2/gdpr/requests 

Requires ANY permissions: 

* gdpr:request:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GeneralDataProtectionRegulationApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get all GDPR requests
    api_response = api_instance.get_gdpr_requests(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralDataProtectionRegulationApi->get_gdpr_requests: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**GDPRRequestEntityListing**](GDPRRequestEntityListing)


## get_gdpr_subjects

> [**GDPRSubjectEntityListing**](GDPRSubjectEntityListing) get_gdpr_subjects(search_type, search_value)


Get GDPR subjects

Wraps GET /api/v2/gdpr/subjects 

Requires ANY permissions: 

* gdpr:subject:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GeneralDataProtectionRegulationApi()
search_type = 'search_type_example' # str | Search Type
search_value = 'search_value_example' # str | Search Value

try:
    # Get GDPR subjects
    api_response = api_instance.get_gdpr_subjects(search_type, search_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralDataProtectionRegulationApi->get_gdpr_subjects: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **search_type** | **str**| Search Type | <br />**Values**: NAME, ADDRESS, PHONE, EMAIL, TWITTER, INSTAGRAM, FACEBOOK, APPLE_MESSAGES, EXTERNAL_ID |
| **search_value** | **str**| Search Value |  |

### Return type

[**GDPRSubjectEntityListing**](GDPRSubjectEntityListing)


## post_gdpr_requests

> [**GDPRRequest**](GDPRRequest) post_gdpr_requests(body, delete_confirmed=delete_confirmed)


Submit a new GDPR request

Wraps POST /api/v2/gdpr/requests 

Requires ANY permissions: 

* gdpr:request:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GeneralDataProtectionRegulationApi()
body = PureCloudPlatformClientV2.GDPRRequest() # GDPRRequest | GDPR request
delete_confirmed = False # bool | Confirm delete (optional) (default to False)

try:
    # Submit a new GDPR request
    api_response = api_instance.post_gdpr_requests(body, delete_confirmed=delete_confirmed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralDataProtectionRegulationApi->post_gdpr_requests: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GDPRRequest**](GDPRRequest)| GDPR request |  |
| **delete_confirmed** | **bool**| Confirm delete | [optional] [default to False] |

### Return type

[**GDPRRequest**](GDPRRequest)


_PureCloudPlatformClientV2 247.0.0_

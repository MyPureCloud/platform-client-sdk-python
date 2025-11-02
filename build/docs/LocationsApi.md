# LocationsApi

## PureCloudPlatformClientV2.LocationsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_location**](#delete_location) | Delete a location|
|[**get_location**](#get_location) | Get Location by ID.|
|[**get_location_sublocations**](#get_location_sublocations) | Get sublocations for location ID.|
|[**get_locations**](#get_locations) | Get a list of all locations.|
|[**get_locations_search**](#get_locations_search) | Search locations using the q64 value returned from a previous search|
|[**patch_location**](#patch_location) | Update a location|
|[**post_locations**](#post_locations) | Create a location|
|[**post_locations_search**](#post_locations_search) | Search locations|



## delete_location

>  delete_location(location_id)


Delete a location

Wraps DELETE /api/v2/locations/{locationId} 

Requires ALL permissions: 

* directory:location:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LocationsApi()
location_id = 'location_id_example' # str | Location ID

try:
    # Delete a location
    api_instance.delete_location(location_id)
except ApiException as e:
    print("Exception when calling LocationsApi->delete_location: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **location_id** | **str**| Location ID |  |

### Return type

void (empty response body)


## get_location

> [**LocationDefinition**](LocationDefinition) get_location(location_id, expand=expand)


Get Location by ID.

Wraps GET /api/v2/locations/{locationId} 

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
api_instance = PureCloudPlatformClientV2.LocationsApi()
location_id = 'location_id_example' # str | Location ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get Location by ID.
    api_response = api_instance.get_location(location_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_location: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **location_id** | **str**| Location ID |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: images, addressVerificationDetails |

### Return type

[**LocationDefinition**](LocationDefinition)


## get_location_sublocations

> [**LocationEntityListing**](LocationEntityListing) get_location_sublocations(location_id)


Get sublocations for location ID.

Wraps GET /api/v2/locations/{locationId}/sublocations 

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
api_instance = PureCloudPlatformClientV2.LocationsApi()
location_id = 'location_id_example' # str | Location ID

try:
    # Get sublocations for location ID.
    api_response = api_instance.get_location_sublocations(location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_location_sublocations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **location_id** | **str**| Location ID |  |

### Return type

[**LocationEntityListing**](LocationEntityListing)


## get_locations

> [**LocationEntityListing**](LocationEntityListing) get_locations(page_size=page_size, page_number=page_number, id=id, sort_order=sort_order)


Get a list of all locations.

Wraps GET /api/v2/locations 

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
api_instance = PureCloudPlatformClientV2.LocationsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
id = ['id_example'] # list[str] | id (optional)
sort_order = 'sort_order_example' # str | Sort order (optional)

try:
    # Get a list of all locations.
    api_response = api_instance.get_locations(page_size=page_size, page_number=page_number, id=id, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_locations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **id** | [**list[str]**](str)| id | [optional]  |
| **sort_order** | **str**| Sort order | [optional] <br />**Values**: asc, desc |

### Return type

[**LocationEntityListing**](LocationEntityListing)


## get_locations_search

> [**LocationsSearchResponse**](LocationsSearchResponse) get_locations_search(q64, expand=expand)


Search locations using the q64 value returned from a previous search

Wraps GET /api/v2/locations/search 

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
api_instance = PureCloudPlatformClientV2.LocationsApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | Provides more details about a specified resource (optional)

try:
    # Search locations using the q64 value returned from a previous search
    api_response = api_instance.get_locations_search(q64, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_locations_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str)| Provides more details about a specified resource | [optional] <br />**Values**: images, addressVerificationDetails |

### Return type

[**LocationsSearchResponse**](LocationsSearchResponse)


## patch_location

> [**LocationDefinition**](LocationDefinition) patch_location(location_id, body)


Update a location

Wraps PATCH /api/v2/locations/{locationId} 

Requires ALL permissions: 

* directory:location:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LocationsApi()
location_id = 'location_id_example' # str | Location ID
body = PureCloudPlatformClientV2.LocationUpdateDefinition() # LocationUpdateDefinition | Location

try:
    # Update a location
    api_response = api_instance.patch_location(location_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->patch_location: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **location_id** | **str**| Location ID |  |
| **body** | [**LocationUpdateDefinition**](LocationUpdateDefinition)| Location |  |

### Return type

[**LocationDefinition**](LocationDefinition)


## post_locations

> [**LocationDefinition**](LocationDefinition) post_locations(body)


Create a location

Wraps POST /api/v2/locations 

Requires ALL permissions: 

* directory:location:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LocationsApi()
body = PureCloudPlatformClientV2.LocationCreateDefinition() # LocationCreateDefinition | Location

try:
    # Create a location
    api_response = api_instance.post_locations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->post_locations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LocationCreateDefinition**](LocationCreateDefinition)| Location |  |

### Return type

[**LocationDefinition**](LocationDefinition)


## post_locations_search

> [**LocationsSearchResponse**](LocationsSearchResponse) post_locations_search(body)


Search locations

Wraps POST /api/v2/locations/search 

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
api_instance = PureCloudPlatformClientV2.LocationsApi()
body = PureCloudPlatformClientV2.LocationSearchRequest() # LocationSearchRequest | Search request options

try:
    # Search locations
    api_response = api_instance.post_locations_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->post_locations_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LocationSearchRequest**](LocationSearchRequest)| Search request options |  |

### Return type

[**LocationsSearchResponse**](LocationsSearchResponse)


_PureCloudPlatformClientV2 242.0.0_

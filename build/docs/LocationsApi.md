---
title: LocationsApi
---

## PureCloudPlatformClientV2.LocationsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_location**](LocationsApi.html#delete_location) | Delete a location|
|[**get_location**](LocationsApi.html#get_location) | Get Location by ID.|
|[**get_location_sublocations**](LocationsApi.html#get_location_sublocations) | Get sublocations for location ID.|
|[**get_locations**](LocationsApi.html#get_locations) | Get a list of all locations.|
|[**get_locations_search**](LocationsApi.html#get_locations_search) | Search locations using the q64 value returned from a previous search|
|[**patch_location**](LocationsApi.html#patch_location) | Update a location|
|[**post_locations**](LocationsApi.html#post_locations) | Create a location|
|[**post_locations_search**](LocationsApi.html#post_locations_search) | Search locations|
{: class="table table-striped"}

<a name="delete_location"></a>

##  delete_location(location_id)



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
    print "Exception when calling LocationsApi->delete_location: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **location_id** | **str**| Location ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_location"></a>

## [**LocationDefinition**](LocationDefinition.html) get_location(location_id, expand=expand)



Get Location by ID.



Wraps GET /api/v2/locations/{locationId} 

Requires NO permissions: 


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
    print "Exception when calling LocationsApi->get_location: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **location_id** | **str**| Location ID |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: images, addressVerificationDetails |
{: class="table table-striped"}

### Return type

[**LocationDefinition**](LocationDefinition.html)

<a name="get_location_sublocations"></a>

## [**LocationEntityListing**](LocationEntityListing.html) get_location_sublocations(location_id)



Get sublocations for location ID.



Wraps GET /api/v2/locations/{locationId}/sublocations 

Requires NO permissions: 


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
    print "Exception when calling LocationsApi->get_location_sublocations: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **location_id** | **str**| Location ID |  |
{: class="table table-striped"}

### Return type

[**LocationEntityListing**](LocationEntityListing.html)

<a name="get_locations"></a>

## [**LocationEntityListing**](LocationEntityListing.html) get_locations(page_size=page_size, page_number=page_number, id=id, sort_order=sort_order)



Get a list of all locations.



Wraps GET /api/v2/locations 

Requires NO permissions: 


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
    print "Exception when calling LocationsApi->get_locations: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **id** | [**list[str]**](str.html)| id | [optional]  |
| **sort_order** | **str**| Sort order | [optional] <br />**Values**: asc, desc |
{: class="table table-striped"}

### Return type

[**LocationEntityListing**](LocationEntityListing.html)

<a name="get_locations_search"></a>

## [**LocationsSearchResponse**](LocationsSearchResponse.html) get_locations_search(q64, expand=expand)



Search locations using the q64 value returned from a previous search



Wraps GET /api/v2/locations/search 

Requires NO permissions: 


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
    print "Exception when calling LocationsApi->get_locations_search: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str.html)| Provides more details about a specified resource | [optional] <br />**Values**: images, addressVerificationDetails |
{: class="table table-striped"}

### Return type

[**LocationsSearchResponse**](LocationsSearchResponse.html)

<a name="patch_location"></a>

## [**LocationDefinition**](LocationDefinition.html) patch_location(location_id, body)



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
    print "Exception when calling LocationsApi->patch_location: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **location_id** | **str**| Location ID |  |
| **body** | [**LocationUpdateDefinition**](LocationUpdateDefinition.html)| Location |  |
{: class="table table-striped"}

### Return type

[**LocationDefinition**](LocationDefinition.html)

<a name="post_locations"></a>

## [**LocationDefinition**](LocationDefinition.html) post_locations(body)



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
    print "Exception when calling LocationsApi->post_locations: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LocationCreateDefinition**](LocationCreateDefinition.html)| Location |  |
{: class="table table-striped"}

### Return type

[**LocationDefinition**](LocationDefinition.html)

<a name="post_locations_search"></a>

## [**LocationsSearchResponse**](LocationsSearchResponse.html) post_locations_search(body)



Search locations



Wraps POST /api/v2/locations/search 

Requires NO permissions: 


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
    print "Exception when calling LocationsApi->post_locations_search: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LocationSearchRequest**](LocationSearchRequest.html)| Search request options |  |
{: class="table table-striped"}

### Return type

[**LocationsSearchResponse**](LocationsSearchResponse.html)


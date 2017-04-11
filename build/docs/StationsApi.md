---
title: StationsApi
---

## PureCloudPlatformClientV2.StationsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_station_associateduser**](StationsApi.html#delete_station_associateduser) | Unassigns the user assigned to this station|
|[**get_station**](StationsApi.html#get_station) | Get station.|
|[**get_stations**](StationsApi.html#get_stations) | Get the list of available stations.|
{: class="table table-striped"}

<a name="delete_station_associateduser"></a>

## str** delete_station_associateduser(station_id)

Unassigns the user assigned to this station



Wraps DELETE /api/v2/stations/{stationId}/associateduser 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.StationsApi()
station_id = 'station_id_example' # str | Station ID

try:
    # Unassigns the user assigned to this station
    api_response = api_instance.delete_station_associateduser(station_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StationsApi->delete_station_associateduser: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **station_id** | **str**| Station ID | |
{: class="table table-striped"}

### Return type

**str**

<a name="get_station"></a>

## [**Station**](Station.html) get_station(station_id)

Get station.



Wraps GET /api/v2/stations/{stationId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.StationsApi()
station_id = 'station_id_example' # str | Station ID

try:
    # Get station.
    api_response = api_instance.get_station(station_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StationsApi->get_station: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **station_id** | **str**| Station ID | |
{: class="table table-striped"}

### Return type

[**Station**](Station.html)

<a name="get_stations"></a>

## [**StationEntityListing**](StationEntityListing.html) get_stations(page_size=page_size, page_number=page_number, sort_by=sort_by, name=name, id=id, line_appearance_id=line_appearance_id)

Get the list of available stations.



Wraps GET /api/v2/stations 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.StationsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = 'name' # str | Sort by (optional) (default to name)
name = 'name_example' # str | Name (optional)
id = 'id_example' # str | Comma separated list of stationIds (optional)
line_appearance_id = 'line_appearance_id_example' # str | lineAppearanceId (optional)

try:
    # Get the list of available stations.
    api_response = api_instance.get_stations(page_size=page_size, page_number=page_number, sort_by=sort_by, name=name, id=id, line_appearance_id=line_appearance_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StationsApi->get_stations: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **sort_by** | **str**| Sort by | [optional] [default to name]|
| **name** | **str**| Name | [optional] |
| **id** | **str**| Comma separated list of stationIds | [optional] |
| **line_appearance_id** | **str**| lineAppearanceId | [optional] |
{: class="table table-striped"}

### Return type

[**StationEntityListing**](StationEntityListing.html)


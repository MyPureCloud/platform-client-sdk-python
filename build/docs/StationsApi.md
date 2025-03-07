# StationsApi

## PureCloudPlatformClientV2.StationsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_station_associateduser**](#delete_station_associateduser) | Unassigns the user assigned to this station|
|[**get_station**](#get_station) | Get station.|
|[**get_stations**](#get_stations) | Get the list of available stations.|



## delete_station_associateduser

>  delete_station_associateduser(station_id)


Unassigns the user assigned to this station

Wraps DELETE /api/v2/stations/{stationId}/associateduser 

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
api_instance = PureCloudPlatformClientV2.StationsApi()
station_id = 'station_id_example' # str | Station ID

try:
    # Unassigns the user assigned to this station
    api_instance.delete_station_associateduser(station_id)
except ApiException as e:
    print("Exception when calling StationsApi->delete_station_associateduser: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **station_id** | **str**| Station ID |  |

### Return type

void (empty response body)


## get_station

> [**Station**](Station) get_station(station_id)


Get station.

Wraps GET /api/v2/stations/{stationId} 

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
api_instance = PureCloudPlatformClientV2.StationsApi()
station_id = 'station_id_example' # str | Station ID

try:
    # Get station.
    api_response = api_instance.get_station(station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationsApi->get_station: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **station_id** | **str**| Station ID |  |

### Return type

[**Station**](Station)


## get_stations

> [**StationEntityListing**](StationEntityListing) get_stations(page_size=page_size, page_number=page_number, sort_by=sort_by, name=name, user_selectable=user_selectable, web_rtc_user_id=web_rtc_user_id, id=id, line_appearance_id=line_appearance_id)


Get the list of available stations.

Wraps GET /api/v2/stations 

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
api_instance = PureCloudPlatformClientV2.StationsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = ''name'' # str | Sort by (optional) (default to 'name')
name = 'name_example' # str | Name (optional)
user_selectable = 'user_selectable_example' # str | True for stations that the user can select otherwise false (optional)
web_rtc_user_id = 'web_rtc_user_id_example' # str | Filter for the webRtc station of the webRtcUserId (optional)
id = 'id_example' # str | Comma separated list of stationIds (optional)
line_appearance_id = 'line_appearance_id_example' # str | lineAppearanceId (optional)

try:
    # Get the list of available stations.
    api_response = api_instance.get_stations(page_size=page_size, page_number=page_number, sort_by=sort_by, name=name, user_selectable=user_selectable, web_rtc_user_id=web_rtc_user_id, id=id, line_appearance_id=line_appearance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationsApi->get_stations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;name&#39;] |
| **name** | **str**| Name | [optional]  |
| **user_selectable** | **str**| True for stations that the user can select otherwise false | [optional]  |
| **web_rtc_user_id** | **str**| Filter for the webRtc station of the webRtcUserId | [optional]  |
| **id** | **str**| Comma separated list of stationIds | [optional]  |
| **line_appearance_id** | **str**| lineAppearanceId | [optional]  |

### Return type

[**StationEntityListing**](StationEntityListing)


_PureCloudPlatformClientV2 223.0.0_

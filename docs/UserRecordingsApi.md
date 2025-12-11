# UserRecordingsApi

## PureCloudPlatformClientV2.UserRecordingsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_userrecording**](#delete_userrecording) | Delete a user recording.|
|[**get_userrecording**](#get_userrecording) | Get a user recording.|
|[**get_userrecording_transcoding**](#get_userrecording_transcoding) | Download a user recording.|
|[**get_userrecordings**](#get_userrecordings) | Get a list of user recordings.|
|[**get_userrecordings_summary**](#get_userrecordings_summary) | Get user recording summary|
|[**put_userrecording**](#put_userrecording) | Update a user recording.|



## delete_userrecording

>  delete_userrecording(recording_id)


Delete a user recording.

Wraps DELETE /api/v2/userrecordings/{recordingId} 

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
api_instance = PureCloudPlatformClientV2.UserRecordingsApi()
recording_id = 'recording_id_example' # str | User Recording ID

try:
    # Delete a user recording.
    api_instance.delete_userrecording(recording_id)
except ApiException as e:
    print("Exception when calling UserRecordingsApi->delete_userrecording: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recording_id** | **str**| User Recording ID |  |

### Return type

void (empty response body)


## get_userrecording

> [**UserRecording**](UserRecording) get_userrecording(recording_id, expand=expand)


Get a user recording.

Wraps GET /api/v2/userrecordings/{recordingId} 

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
api_instance = PureCloudPlatformClientV2.UserRecordingsApi()
recording_id = 'recording_id_example' # str | User Recording ID
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get a user recording.
    api_response = api_instance.get_userrecording(recording_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserRecordingsApi->get_userrecording: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recording_id** | **str**| User Recording ID |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: conversation |

### Return type

[**UserRecording**](UserRecording)


## get_userrecording_transcoding

> [**DownloadResponse**](DownloadResponse) get_userrecording_transcoding(recording_id, format_id=format_id)


Download a user recording.

Wraps GET /api/v2/userrecordings/{recordingId}/transcoding 

Requires ANY permissions: 

* They are enforced by the backend

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UserRecordingsApi()
recording_id = 'recording_id_example' # str | User Recording ID
format_id = ''WEBM'' # str | The desired media format. (optional) (default to 'WEBM')

try:
    # Download a user recording.
    api_response = api_instance.get_userrecording_transcoding(recording_id, format_id=format_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserRecordingsApi->get_userrecording_transcoding: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recording_id** | **str**| User Recording ID |  |
| **format_id** | **str**| The desired media format. | [optional] [default to &#39;WEBM&#39;]<br />**Values**: WAV, WEBM, WAV_ULAW, OGG_VORBIS, OGG_OPUS, MP3, NONE |

### Return type

[**DownloadResponse**](DownloadResponse)


## get_userrecordings

> [**UserRecordingEntityListing**](UserRecordingEntityListing) get_userrecordings(page_size=page_size, page_number=page_number, expand=expand)


Get a list of user recordings.

Wraps GET /api/v2/userrecordings 

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
api_instance = PureCloudPlatformClientV2.UserRecordingsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get a list of user recordings.
    api_response = api_instance.get_userrecordings(page_size=page_size, page_number=page_number, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserRecordingsApi->get_userrecordings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: conversation |

### Return type

[**UserRecordingEntityListing**](UserRecordingEntityListing)


## get_userrecordings_summary

> [**FaxSummary**](FaxSummary) get_userrecordings_summary()


Get user recording summary

Wraps GET /api/v2/userrecordings/summary 

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
api_instance = PureCloudPlatformClientV2.UserRecordingsApi()

try:
    # Get user recording summary
    api_response = api_instance.get_userrecordings_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserRecordingsApi->get_userrecordings_summary: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**FaxSummary**](FaxSummary)


## put_userrecording

> [**UserRecording**](UserRecording) put_userrecording(recording_id, body, expand=expand)


Update a user recording.

Wraps PUT /api/v2/userrecordings/{recordingId} 

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
api_instance = PureCloudPlatformClientV2.UserRecordingsApi()
recording_id = 'recording_id_example' # str | User Recording ID
body = PureCloudPlatformClientV2.UserRecording() # UserRecording | UserRecording
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Update a user recording.
    api_response = api_instance.put_userrecording(recording_id, body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserRecordingsApi->put_userrecording: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recording_id** | **str**| User Recording ID |  |
| **body** | [**UserRecording**](UserRecording)| UserRecording |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: conversation |

### Return type

[**UserRecording**](UserRecording)


_PureCloudPlatformClientV2 246.0.0_

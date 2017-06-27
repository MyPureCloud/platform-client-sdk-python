---
title: UserRecordingsApi
---

## PureCloudPlatformClientV2.UserRecordingsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_userrecording**](UserRecordingsApi.html#delete_userrecording) | Delete a user recording.|
|[**get_userrecording**](UserRecordingsApi.html#get_userrecording) | Get a user recording.|
|[**get_userrecording_media**](UserRecordingsApi.html#get_userrecording_media) | Download a user recording.|
|[**get_userrecordings**](UserRecordingsApi.html#get_userrecordings) | Get a list of user recordings.|
|[**get_userrecordings_summary**](UserRecordingsApi.html#get_userrecordings_summary) | Get user recording summary|
|[**put_userrecording**](UserRecordingsApi.html#put_userrecording) | Update a user recording.|
{: class="table table-striped"}

<a name="delete_userrecording"></a>

##  delete_userrecording(recording_id)

Delete a user recording.



Wraps DELETE /api/v2/userrecordings/{recordingId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UserRecordingsApi()
recording_id = 'recording_id_example' # str | User Recording ID

try:
    # Delete a user recording.
    api_instance.delete_userrecording(recording_id)
except ApiException as e:
    print "Exception when calling UserRecordingsApi->delete_userrecording: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recording_id** | **str**| User Recording ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_userrecording"></a>

## [**UserRecording**](UserRecording.html) get_userrecording(recording_id, expand=expand)

Get a user recording.



Wraps GET /api/v2/userrecordings/{recordingId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UserRecordingsApi->get_userrecording: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recording_id** | **str**| User Recording ID |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand. | [optional] <br />**Values**: conversation |
{: class="table table-striped"}

### Return type

[**UserRecording**](UserRecording.html)

<a name="get_userrecording_media"></a>

## [**DownloadResponse**](DownloadResponse.html) get_userrecording_media(recording_id, format_id=format_id)

Download a user recording.



Wraps GET /api/v2/userrecordings/{recordingId}/media 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UserRecordingsApi()
recording_id = 'recording_id_example' # str | User Recording ID
format_id = 'WEBM' # str | The desired media format. (optional) (default to WEBM)

try:
    # Download a user recording.
    api_response = api_instance.get_userrecording_media(recording_id, format_id=format_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserRecordingsApi->get_userrecording_media: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recording_id** | **str**| User Recording ID |  |
| **format_id** | **str**| The desired media format. | [optional] [default to WEBM]<br />**Values**: WAV, WEBM, WAV_ULAW, OGG_VORBIS, OGG_OPUS, MP3, NONE |
{: class="table table-striped"}

### Return type

[**DownloadResponse**](DownloadResponse.html)

<a name="get_userrecordings"></a>

## [**UserRecordingEntityListing**](UserRecordingEntityListing.html) get_userrecordings(page_size=page_size, page_number=page_number, expand=expand)

Get a list of user recordings.



Wraps GET /api/v2/userrecordings 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UserRecordingsApi->get_userrecordings: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand. | [optional] <br />**Values**: conversation |
{: class="table table-striped"}

### Return type

[**UserRecordingEntityListing**](UserRecordingEntityListing.html)

<a name="get_userrecordings_summary"></a>

## [**FaxSummary**](FaxSummary.html) get_userrecordings_summary()

Get user recording summary



Wraps GET /api/v2/userrecordings/summary 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UserRecordingsApi()

try:
    # Get user recording summary
    api_response = api_instance.get_userrecordings_summary()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserRecordingsApi->get_userrecordings_summary: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**FaxSummary**](FaxSummary.html)

<a name="put_userrecording"></a>

## [**UserRecording**](UserRecording.html) put_userrecording(recording_id, body, expand=expand)

Update a user recording.



Wraps PUT /api/v2/userrecordings/{recordingId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling UserRecordingsApi->put_userrecording: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recording_id** | **str**| User Recording ID |  |
| **body** | [**UserRecording**](UserRecording.html)| UserRecording |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand. | [optional] <br />**Values**: conversation |
{: class="table table-striped"}

### Return type

[**UserRecording**](UserRecording.html)


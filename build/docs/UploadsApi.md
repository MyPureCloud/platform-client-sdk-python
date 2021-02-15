---
title: UploadsApi
---

## PureCloudPlatformClientV2.UploadsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**post_uploads_publicassets_images**](UploadsApi.html#post_uploads_publicassets_images) | Creates presigned url for uploading a public asset image|
|[**post_uploads_recordings**](UploadsApi.html#post_uploads_recordings) | Creates presigned url for uploading a recording file|
|[**post_uploads_workforcemanagement_historicaldata_csv**](UploadsApi.html#post_uploads_workforcemanagement_historicaldata_csv) | Creates presigned url for uploading WFM historical data file. Requires data in csv format.|
|[**post_uploads_workforcemanagement_historicaldata_json**](UploadsApi.html#post_uploads_workforcemanagement_historicaldata_json) | Creates presigned url for uploading WFM historical data file. Requires data in json format.|
{: class="table table-striped"}

<a name="post_uploads_publicassets_images"></a>

## [**UploadUrlResponse**](UploadUrlResponse.html) post_uploads_publicassets_images(body)



Creates presigned url for uploading a public asset image



Wraps POST /api/v2/uploads/publicassets/images 

Requires ALL permissions: 

* uploads:publicasset:upload

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UploadsApi()
body = PureCloudPlatformClientV2.UploadUrlRequest() # UploadUrlRequest | query

try:
    # Creates presigned url for uploading a public asset image
    api_response = api_instance.post_uploads_publicassets_images(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadsApi->post_uploads_publicassets_images: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UploadUrlRequest**](UploadUrlRequest.html)| query |  |
{: class="table table-striped"}

### Return type

[**UploadUrlResponse**](UploadUrlResponse.html)

<a name="post_uploads_recordings"></a>

## [**UploadUrlResponse**](UploadUrlResponse.html) post_uploads_recordings(body)



Creates presigned url for uploading a recording file



Wraps POST /api/v2/uploads/recordings 

Requires ALL permissions: 

* recording:recording:upload

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UploadsApi()
body = PureCloudPlatformClientV2.UploadUrlRequest() # UploadUrlRequest | query

try:
    # Creates presigned url for uploading a recording file
    api_response = api_instance.post_uploads_recordings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadsApi->post_uploads_recordings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UploadUrlRequest**](UploadUrlRequest.html)| query |  |
{: class="table table-striped"}

### Return type

[**UploadUrlResponse**](UploadUrlResponse.html)

<a name="post_uploads_workforcemanagement_historicaldata_csv"></a>

## [**UploadUrlResponse**](UploadUrlResponse.html) post_uploads_workforcemanagement_historicaldata_csv(body)



Creates presigned url for uploading WFM historical data file. Requires data in csv format.



Wraps POST /api/v2/uploads/workforcemanagement/historicaldata/csv 

Requires ALL permissions: 

* wfm:historicalData:upload

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UploadsApi()
body = PureCloudPlatformClientV2.UploadUrlRequest() # UploadUrlRequest | query

try:
    # Creates presigned url for uploading WFM historical data file. Requires data in csv format.
    api_response = api_instance.post_uploads_workforcemanagement_historicaldata_csv(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadsApi->post_uploads_workforcemanagement_historicaldata_csv: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UploadUrlRequest**](UploadUrlRequest.html)| query |  |
{: class="table table-striped"}

### Return type

[**UploadUrlResponse**](UploadUrlResponse.html)

<a name="post_uploads_workforcemanagement_historicaldata_json"></a>

## [**UploadUrlResponse**](UploadUrlResponse.html) post_uploads_workforcemanagement_historicaldata_json(body)



Creates presigned url for uploading WFM historical data file. Requires data in json format.



Wraps POST /api/v2/uploads/workforcemanagement/historicaldata/json 

Requires ALL permissions: 

* wfm:historicalData:upload

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.UploadsApi()
body = PureCloudPlatformClientV2.UploadUrlRequest() # UploadUrlRequest | query

try:
    # Creates presigned url for uploading WFM historical data file. Requires data in json format.
    api_response = api_instance.post_uploads_workforcemanagement_historicaldata_json(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadsApi->post_uploads_workforcemanagement_historicaldata_json: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UploadUrlRequest**](UploadUrlRequest.html)| query |  |
{: class="table table-striped"}

### Return type

[**UploadUrlResponse**](UploadUrlResponse.html)


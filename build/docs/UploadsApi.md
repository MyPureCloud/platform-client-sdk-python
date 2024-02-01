---
title: UploadsApi
---

## PureCloudPlatformClientV2.UploadsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**post_integrations_action_draft_function_upload**](UploadsApi.html#post_integrations_action_draft_function_upload) | Create upload presigned URL for draft function package file.|
|[**post_knowledge_documentuploads**](UploadsApi.html#post_knowledge_documentuploads) | Creates a presigned URL for uploading a knowledge import file with a set of documents|
|[**post_languageunderstanding_miner_uploads**](UploadsApi.html#post_languageunderstanding_miner_uploads) | Creates a presigned URL for uploading a chat corpus which will be used for mining by intent miner|
|[**post_uploads_learning_coverart**](UploadsApi.html#post_uploads_learning_coverart) | Generates pre-signed URL to upload cover art for learning modules|
|[**post_uploads_publicassets_images**](UploadsApi.html#post_uploads_publicassets_images) | Creates presigned url for uploading a public asset image|
|[**post_uploads_recordings**](UploadsApi.html#post_uploads_recordings) | Creates presigned url for uploading a recording file|
|[**post_uploads_workforcemanagement_historicaldata_csv**](UploadsApi.html#post_uploads_workforcemanagement_historicaldata_csv) | Creates presigned url for uploading WFM historical data file. Requires data in csv format.|
{: class="table table-striped"}

<a name="post_integrations_action_draft_function_upload"></a>

## [**FunctionUploadResponse**](FunctionUploadResponse.html) post_integrations_action_draft_function_upload(action_id, body)



Create upload presigned URL for draft function package file.

post_integrations_action_draft_function_upload is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/integrations/actions/{actionId}/draft/function/upload 

Requires ANY permissions: 

* integrations:actionFunction:edit

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
action_id = 'action_id_example' # str | actionId
body = PureCloudPlatformClientV2.FunctionUploadRequest() # FunctionUploadRequest | Input used to request URL upload.

try:
    # Create upload presigned URL for draft function package file.
    api_response = api_instance.post_integrations_action_draft_function_upload(action_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadsApi->post_integrations_action_draft_function_upload: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **action_id** | **str**| actionId |  |
| **body** | [**FunctionUploadRequest**](FunctionUploadRequest.html)| Input used to request URL upload. |  |
{: class="table table-striped"}

### Return type

[**FunctionUploadResponse**](FunctionUploadResponse.html)

<a name="post_knowledge_documentuploads"></a>

## [**UploadUrlResponse**](UploadUrlResponse.html) post_knowledge_documentuploads(body)



Creates a presigned URL for uploading a knowledge import file with a set of documents

Wraps POST /api/v2/knowledge/documentuploads 

Requires ALL permissions: 

* knowledge:document:upload

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
    # Creates a presigned URL for uploading a knowledge import file with a set of documents
    api_response = api_instance.post_knowledge_documentuploads(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadsApi->post_knowledge_documentuploads: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UploadUrlRequest**](UploadUrlRequest.html)| query |  |
{: class="table table-striped"}

### Return type

[**UploadUrlResponse**](UploadUrlResponse.html)

<a name="post_languageunderstanding_miner_uploads"></a>

## [**UploadUrlResponse**](UploadUrlResponse.html) post_languageunderstanding_miner_uploads(miner_id, body)



Creates a presigned URL for uploading a chat corpus which will be used for mining by intent miner

Wraps POST /api/v2/languageunderstanding/miners/{minerId}/uploads 

Requires ALL permissions: 

* languageUnderstanding:miner:upload

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
miner_id = 'miner_id_example' # str | Miner ID
body = NULL # Empty | query

try:
    # Creates a presigned URL for uploading a chat corpus which will be used for mining by intent miner
    api_response = api_instance.post_languageunderstanding_miner_uploads(miner_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadsApi->post_languageunderstanding_miner_uploads: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_id** | **str**| Miner ID |  |
| **body** | **Empty**| query |  |
{: class="table table-striped"}

### Return type

[**UploadUrlResponse**](UploadUrlResponse.html)

<a name="post_uploads_learning_coverart"></a>

## [**UploadUrlResponse**](UploadUrlResponse.html) post_uploads_learning_coverart(body)



Generates pre-signed URL to upload cover art for learning modules

Wraps POST /api/v2/uploads/learning/coverart 

Requires ALL permissions: 

* learning:coverart:upload

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
body = PureCloudPlatformClientV2.LearningCoverArtUploadUrlRequest() # LearningCoverArtUploadUrlRequest | query

try:
    # Generates pre-signed URL to upload cover art for learning modules
    api_response = api_instance.post_uploads_learning_coverart(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadsApi->post_uploads_learning_coverart: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LearningCoverArtUploadUrlRequest**](LearningCoverArtUploadUrlRequest.html)| query |  |
{: class="table table-striped"}

### Return type

[**UploadUrlResponse**](UploadUrlResponse.html)

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


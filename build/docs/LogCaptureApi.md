---
title: LogCaptureApi
---

## PureCloudPlatformClientV2.LogCaptureApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_diagnostics_logcapture_browser_user**](LogCaptureApi.html#delete_diagnostics_logcapture_browser_user) | Disable browser log capture for the user|
|[**get_diagnostics_logcapture_browser_entries_download_job**](LogCaptureApi.html#get_diagnostics_logcapture_browser_entries_download_job) | Gets status of async download execution|
|[**get_diagnostics_logcapture_browser_user**](LogCaptureApi.html#get_diagnostics_logcapture_browser_user) | Get log capture configuration for the user|
|[**get_diagnostics_logcapture_browser_users**](LogCaptureApi.html#get_diagnostics_logcapture_browser_users) | Get all log capture enabled users for an org|
|[**post_diagnostics_logcapture_browser_entries_download_jobs**](LogCaptureApi.html#post_diagnostics_logcapture_browser_entries_download_jobs) | Creates an async download execution|
|[**post_diagnostics_logcapture_browser_entries_query**](LogCaptureApi.html#post_diagnostics_logcapture_browser_entries_query) | Query collected log entries. It returns a limited amount of records, to get all records use download endpoint.|
|[**post_diagnostics_logcapture_browser_user**](LogCaptureApi.html#post_diagnostics_logcapture_browser_user) | Enable log capture for a user or update expiration|
{: class="table table-striped"}

<a name="delete_diagnostics_logcapture_browser_user"></a>

##  delete_diagnostics_logcapture_browser_user(user_id)



Disable browser log capture for the user

Wraps DELETE /api/v2/diagnostics/logcapture/browser/users/{userId} 

Requires ANY permissions: 

* troubleshooting:logCapture:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LogCaptureApi()
user_id = 'user_id_example' # str | The id of the user to disable browser log capture

try:
    # Disable browser log capture for the user
    api_instance.delete_diagnostics_logcapture_browser_user(user_id)
except ApiException as e:
    print("Exception when calling LogCaptureApi->delete_diagnostics_logcapture_browser_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The id of the user to disable browser log capture |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_diagnostics_logcapture_browser_entries_download_job"></a>

## [**LogCaptureDownloadExecutionResponse**](LogCaptureDownloadExecutionResponse.html) get_diagnostics_logcapture_browser_entries_download_job(job_id)



Gets status of async download execution

Wraps GET /api/v2/diagnostics/logcapture/browser/entries/download/jobs/{jobId} 

Requires ALL permissions: 

* troubleshooting:logCapture:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LogCaptureApi()
job_id = 'job_id_example' # str | Job ID

try:
    # Gets status of async download execution
    api_response = api_instance.get_diagnostics_logcapture_browser_entries_download_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogCaptureApi->get_diagnostics_logcapture_browser_entries_download_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| Job ID |  |
{: class="table table-striped"}

### Return type

[**LogCaptureDownloadExecutionResponse**](LogCaptureDownloadExecutionResponse.html)

<a name="get_diagnostics_logcapture_browser_user"></a>

## [**LogCaptureUserConfiguration**](LogCaptureUserConfiguration.html) get_diagnostics_logcapture_browser_user(user_id)



Get log capture configuration for the user

Wraps GET /api/v2/diagnostics/logcapture/browser/users/{userId} 

Requires ANY permissions: 

* troubleshooting:logCapture:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LogCaptureApi()
user_id = 'user_id_example' # str | The id of the user to get browser log capture configuration

try:
    # Get log capture configuration for the user
    api_response = api_instance.get_diagnostics_logcapture_browser_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogCaptureApi->get_diagnostics_logcapture_browser_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The id of the user to get browser log capture configuration |  |
{: class="table table-striped"}

### Return type

[**LogCaptureUserConfiguration**](LogCaptureUserConfiguration.html)

<a name="get_diagnostics_logcapture_browser_users"></a>

## [**PagelessEntityListing**](PagelessEntityListing.html) get_diagnostics_logcapture_browser_users(include_expired=include_expired)



Get all log capture enabled users for an org

Wraps GET /api/v2/diagnostics/logcapture/browser/users 

Requires ANY permissions: 

* troubleshooting:logCapture:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LogCaptureApi()
include_expired = False # bool | Include expired users with log captures still available for search or download (optional) (default to False)

try:
    # Get all log capture enabled users for an org
    api_response = api_instance.get_diagnostics_logcapture_browser_users(include_expired=include_expired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogCaptureApi->get_diagnostics_logcapture_browser_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **include_expired** | **bool**| Include expired users with log captures still available for search or download | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**PagelessEntityListing**](PagelessEntityListing.html)

<a name="post_diagnostics_logcapture_browser_entries_download_jobs"></a>

## [**LogCaptureDownloadExecutionResponse**](LogCaptureDownloadExecutionResponse.html) post_diagnostics_logcapture_browser_entries_download_jobs(body=body)



Creates an async download execution

Wraps POST /api/v2/diagnostics/logcapture/browser/entries/download/jobs 

Requires ANY permissions: 

* troubleshooting:logCapture:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LogCaptureApi()
body = PureCloudPlatformClientV2.LogCaptureQueryRequest() # LogCaptureQueryRequest |  (optional)

try:
    # Creates an async download execution
    api_response = api_instance.post_diagnostics_logcapture_browser_entries_download_jobs(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogCaptureApi->post_diagnostics_logcapture_browser_entries_download_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LogCaptureQueryRequest**](LogCaptureQueryRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**LogCaptureDownloadExecutionResponse**](LogCaptureDownloadExecutionResponse.html)

<a name="post_diagnostics_logcapture_browser_entries_query"></a>

## [**LogCaptureQueryResponse**](LogCaptureQueryResponse.html) post_diagnostics_logcapture_browser_entries_query(before=before, after=after, page_size=page_size, body=body)



Query collected log entries. It returns a limited amount of records, to get all records use download endpoint.

Wraps POST /api/v2/diagnostics/logcapture/browser/entries/query 

Requires ANY permissions: 

* troubleshooting:logCapture:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LogCaptureApi()
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
body = PureCloudPlatformClientV2.LogCaptureQueryRequest() # LogCaptureQueryRequest |  (optional)

try:
    # Query collected log entries. It returns a limited amount of records, to get all records use download endpoint.
    api_response = api_instance.post_diagnostics_logcapture_browser_entries_query(before=before, after=after, page_size=page_size, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogCaptureApi->post_diagnostics_logcapture_browser_entries_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **body** | [**LogCaptureQueryRequest**](LogCaptureQueryRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**LogCaptureQueryResponse**](LogCaptureQueryResponse.html)

<a name="post_diagnostics_logcapture_browser_user"></a>

## [**LogCaptureUserConfiguration**](LogCaptureUserConfiguration.html) post_diagnostics_logcapture_browser_user(user_id, body=body)



Enable log capture for a user or update expiration

Wraps POST /api/v2/diagnostics/logcapture/browser/users/{userId} 

Requires ANY permissions: 

* troubleshooting:logCapture:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LogCaptureApi()
user_id = 'user_id_example' # str | The id of the user to enable browser log capture
body = PureCloudPlatformClientV2.LogCaptureUserConfiguration() # LogCaptureUserConfiguration |  (optional)

try:
    # Enable log capture for a user or update expiration
    api_response = api_instance.post_diagnostics_logcapture_browser_user(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogCaptureApi->post_diagnostics_logcapture_browser_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The id of the user to enable browser log capture |  |
| **body** | [**LogCaptureUserConfiguration**](LogCaptureUserConfiguration.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**LogCaptureUserConfiguration**](LogCaptureUserConfiguration.html)


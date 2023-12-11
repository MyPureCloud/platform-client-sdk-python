---
title: LogCaptureApi
---

## PureCloudPlatformClientV2.LogCaptureApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_diagnostics_logcapture_browser_entries_download_job**](LogCaptureApi.html#get_diagnostics_logcapture_browser_entries_download_job) | Gets status of async download execution|
|[**post_diagnostics_logcapture_browser_entries_download_jobs**](LogCaptureApi.html#post_diagnostics_logcapture_browser_entries_download_jobs) | Creates an async download execution|
{: class="table table-striped"}

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


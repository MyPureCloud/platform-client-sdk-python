# DownloadsApi

## PureCloudPlatformClientV2.DownloadsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_download**](#get_download) | Issues a redirect to a signed secure download URL for specified download|



## get_download

> [**UrlResponse**](UrlResponse) get_download(download_id, content_disposition=content_disposition, issue_redirect=issue_redirect, redirect_to_auth=redirect_to_auth)


Issues a redirect to a signed secure download URL for specified download

this method will issue a redirect to the url to the content

Wraps GET /api/v2/downloads/{downloadId} 

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
api_instance = PureCloudPlatformClientV2.DownloadsApi()
download_id = 'download_id_example' # str | Download ID
content_disposition = 'content_disposition_example' # str |  (optional)
issue_redirect = True # bool |  (optional) (default to True)
redirect_to_auth = True # bool |  (optional) (default to True)

try:
    # Issues a redirect to a signed secure download URL for specified download
    api_response = api_instance.get_download(download_id, content_disposition=content_disposition, issue_redirect=issue_redirect, redirect_to_auth=redirect_to_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadsApi->get_download: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **download_id** | **str**| Download ID |  |
| **content_disposition** | **str**|  | [optional]  |
| **issue_redirect** | **bool**|  | [optional] [default to True] |
| **redirect_to_auth** | **bool**|  | [optional] [default to True] |

### Return type

[**UrlResponse**](UrlResponse)


_PureCloudPlatformClientV2 226.0.0_

---
title: SignedDataApi
---

## PureCloudPlatformClientV2.SignedDataApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**post_signeddata**](SignedDataApi.html#post_signeddata) | Sign identifying information|
{: class="table table-striped"}

<a name="post_signeddata"></a>

## [**SignedData**](SignedData.html) post_signeddata(body=body)

Sign identifying information



Wraps POST /api/v2/signeddata 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SignedDataApi()
body = NULL # object |  (optional)

try:
    # Sign identifying information
    api_response = api_instance.post_signeddata(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SignedDataApi->post_signeddata: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | **object**|  | [optional]  |
{: class="table table-striped"}

### Return type

[**SignedData**](SignedData.html)


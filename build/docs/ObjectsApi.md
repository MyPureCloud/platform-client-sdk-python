---
title: ObjectsApi
---

## PureCloudPlatformClientV2.ObjectsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_authorization_divisions_limit**](ObjectsApi.html#get_authorization_divisions_limit) | Returns the maximum allowed number of divisions.|
{: class="table table-striped"}

<a name="get_authorization_divisions_limit"></a>

## int** get_authorization_divisions_limit()

Returns the maximum allowed number of divisions.



Wraps GET /api/v2/authorization/divisions/limit 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ObjectsApi()

try:
    # Returns the maximum allowed number of divisions.
    api_response = api_instance.get_authorization_divisions_limit()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ObjectsApi->get_authorization_divisions_limit: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

**int**


---
title: TokensApi
---

## PureCloudPlatformClientV2.TokensApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_tokens_me**](TokensApi.html#delete_tokens_me) | Delete  auth token used to make the request.|
|[**get_tokens_me**](TokensApi.html#get_tokens_me) | Fetch information about the current token|
{: class="table table-striped"}

<a name="delete_tokens_me"></a>

##  delete_tokens_me()



Delete  auth token used to make the request.



Wraps DELETE /api/v2/tokens/me 

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TokensApi()

try:
    # Delete  auth token used to make the request.
    api_instance.delete_tokens_me()
except ApiException as e:
    print "Exception when calling TokensApi->delete_tokens_me: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_tokens_me"></a>

## [**TokenInfo**](TokenInfo.html) get_tokens_me()



Fetch information about the current token



Wraps GET /api/v2/tokens/me 

Requires NO permissions: 



### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TokensApi()

try:
    # Fetch information about the current token
    api_response = api_instance.get_tokens_me()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TokensApi->get_tokens_me: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**TokenInfo**](TokenInfo.html)


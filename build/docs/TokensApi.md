---
title: TokensApi
---

## PureCloudPlatformClientV2.TokensApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_token**](TokensApi.html#delete_token) | Delete all auth tokens for the specified user.|
|[**delete_tokens_me**](TokensApi.html#delete_tokens_me) | Delete auth token used to make the request.|
|[**get_tokens_me**](TokensApi.html#get_tokens_me) | Fetch information about the current token|
|[**head_tokens_me**](TokensApi.html#head_tokens_me) | Verify user token|
{: class="table table-striped"}

<a name="delete_token"></a>

##  delete_token(user_id)



Delete all auth tokens for the specified user.



Wraps DELETE /api/v2/tokens/{userId} 

Requires ANY permissions: 

* oauth:token:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TokensApi()
user_id = 'user_id_example' # str | User ID

try:
    # Delete all auth tokens for the specified user.
    api_instance.delete_token(user_id)
except ApiException as e:
    print("Exception when calling TokensApi->delete_token: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_tokens_me"></a>

##  delete_tokens_me()



Delete auth token used to make the request.



Wraps DELETE /api/v2/tokens/me 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TokensApi()

try:
    # Delete auth token used to make the request.
    api_instance.delete_tokens_me()
except ApiException as e:
    print("Exception when calling TokensApi->delete_tokens_me: %s\n" % e)
```

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

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TokensApi()

try:
    # Fetch information about the current token
    api_response = api_instance.get_tokens_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->get_tokens_me: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**TokenInfo**](TokenInfo.html)

<a name="head_tokens_me"></a>

##  head_tokens_me()



Verify user token



Wraps HEAD /api/v2/tokens/me 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TokensApi()

try:
    # Verify user token
    api_instance.head_tokens_me()
except ApiException as e:
    print("Exception when calling TokensApi->head_tokens_me: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

void (empty response body)


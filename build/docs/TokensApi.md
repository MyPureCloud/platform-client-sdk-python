# TokensApi

## PureCloudPlatformClientV2.TokensApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_token**](#delete_token) | Delete all auth tokens for the specified user.|
|[**delete_tokens_me**](#delete_tokens_me) | Delete auth token used to make the request.|
|[**get_tokens_me**](#get_tokens_me) | Fetch information about the current token|
|[**get_tokens_timeout**](#get_tokens_timeout) | Get the current Idle Token Timeout Value|
|[**head_tokens_me**](#head_tokens_me) | Verify user token|
|[**put_tokens_timeout**](#put_tokens_timeout) | Update or Enable/Disable the Idle Token Timeout|



## delete_token

>  delete_token(user_id)


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

### Return type

void (empty response body)


## delete_tokens_me

>  delete_tokens_me()


Delete auth token used to make the request.

Wraps DELETE /api/v2/tokens/me 

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
api_instance = PureCloudPlatformClientV2.TokensApi()

try:
    # Delete auth token used to make the request.
    api_instance.delete_tokens_me()
except ApiException as e:
    print("Exception when calling TokensApi->delete_tokens_me: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

void (empty response body)


## get_tokens_me

> [**TokenInfo**](TokenInfo) get_tokens_me(preserve_idle_ttl=preserve_idle_ttl)


Fetch information about the current token

Wraps GET /api/v2/tokens/me 

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
api_instance = PureCloudPlatformClientV2.TokensApi()
preserve_idle_ttl = True # bool | preserveIdleTTL indicates whether the idle token timeout should be reset or preserved. If preserveIdleTTL is true, then TTL value is not reset. If unset or false, the value is reset. (optional)

try:
    # Fetch information about the current token
    api_response = api_instance.get_tokens_me(preserve_idle_ttl=preserve_idle_ttl)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->get_tokens_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **preserve_idle_ttl** | **bool**| preserveIdleTTL indicates whether the idle token timeout should be reset or preserved. If preserveIdleTTL is true, then TTL value is not reset. If unset or false, the value is reset. | [optional]  |

### Return type

[**TokenInfo**](TokenInfo)


## get_tokens_timeout

> [**IdleTokenTimeout**](IdleTokenTimeout) get_tokens_timeout()


Get the current Idle Token Timeout Value

Wraps GET /api/v2/tokens/timeout 

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
api_instance = PureCloudPlatformClientV2.TokensApi()

try:
    # Get the current Idle Token Timeout Value
    api_response = api_instance.get_tokens_timeout()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->get_tokens_timeout: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**IdleTokenTimeout**](IdleTokenTimeout)


## head_tokens_me

>  head_tokens_me()


Verify user token

Wraps HEAD /api/v2/tokens/me 

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
api_instance = PureCloudPlatformClientV2.TokensApi()

try:
    # Verify user token
    api_instance.head_tokens_me()
except ApiException as e:
    print("Exception when calling TokensApi->head_tokens_me: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

void (empty response body)


## put_tokens_timeout

> [**IdleTokenTimeout**](IdleTokenTimeout) put_tokens_timeout(body=body)


Update or Enable/Disable the Idle Token Timeout

Wraps PUT /api/v2/tokens/timeout 

Requires ANY permissions: 

* directory:organization:admin

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
body = PureCloudPlatformClientV2.IdleTokenTimeout() # IdleTokenTimeout |  (optional)

try:
    # Update or Enable/Disable the Idle Token Timeout
    api_response = api_instance.put_tokens_timeout(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->put_tokens_timeout: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**IdleTokenTimeout**](IdleTokenTimeout)|  | [optional]  |

### Return type

[**IdleTokenTimeout**](IdleTokenTimeout)


_PureCloudPlatformClientV2 235.0.0_

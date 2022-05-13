---
title: OAuthApi
---

## PureCloudPlatformClientV2.OAuthApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_oauth_client**](OAuthApi.html#delete_oauth_client) | Delete OAuth Client|
|[**get_oauth_authorization**](OAuthApi.html#get_oauth_authorization) | Get a client that is authorized by the resource owner|
|[**get_oauth_authorizations**](OAuthApi.html#get_oauth_authorizations) | List clients that have been authorized, requested, or revoked by the resource owner|
|[**get_oauth_client**](OAuthApi.html#get_oauth_client) | Get OAuth Client|
|[**get_oauth_client_usage_query_result**](OAuthApi.html#get_oauth_client_usage_query_result) | Get the results of a usage query|
|[**get_oauth_client_usage_summary**](OAuthApi.html#get_oauth_client_usage_summary) | Get a summary of OAuth client API usage|
|[**get_oauth_clients**](OAuthApi.html#get_oauth_clients) | The list of OAuth clients|
|[**get_oauth_scope**](OAuthApi.html#get_oauth_scope) | An OAuth scope|
|[**get_oauth_scopes**](OAuthApi.html#get_oauth_scopes) | The list of OAuth scopes|
|[**post_oauth_client_secret**](OAuthApi.html#post_oauth_client_secret) | Regenerate Client Secret|
|[**post_oauth_client_usage_query**](OAuthApi.html#post_oauth_client_usage_query) | Query for OAuth client API usage|
|[**post_oauth_clients**](OAuthApi.html#post_oauth_clients) | Create OAuth client|
|[**put_oauth_client**](OAuthApi.html#put_oauth_client) | Update OAuth Client|
{: class="table table-striped"}

<a name="delete_oauth_client"></a>

##  delete_oauth_client(client_id)



Delete OAuth Client



Wraps DELETE /api/v2/oauth/clients/{clientId} 

Requires ANY permissions: 

* oauth:client:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
client_id = 'client_id_example' # str | Client ID

try:
    # Delete OAuth Client
    api_instance.delete_oauth_client(client_id)
except ApiException as e:
    print("Exception when calling OAuthApi->delete_oauth_client: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client_id** | **str**| Client ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_oauth_authorization"></a>

## [**OAuthAuthorization**](OAuthAuthorization.html) get_oauth_authorization(client_id, accept_language=accept_language)



Get a client that is authorized by the resource owner



Wraps GET /api/v2/oauth/authorizations/{clientId} 

Requires ANY permissions: 

* oauth:client:authorize

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
client_id = 'client_id_example' # str | The ID of client
accept_language = ''en-us'' # str | The language in which to display the client descriptions. (optional) (default to 'en-us')

try:
    # Get a client that is authorized by the resource owner
    api_response = api_instance.get_oauth_authorization(client_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->get_oauth_authorization: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client_id** | **str**| The ID of client |  |
| **accept_language** | **str**| The language in which to display the client descriptions. | [optional] [default to &#39;en-us&#39;] |
{: class="table table-striped"}

### Return type

[**OAuthAuthorization**](OAuthAuthorization.html)

<a name="get_oauth_authorizations"></a>

## [**OAuthAuthorizationListing**](OAuthAuthorizationListing.html) get_oauth_authorizations(accept_language=accept_language)



List clients that have been authorized, requested, or revoked by the resource owner



Wraps GET /api/v2/oauth/authorizations 

Requires ANY permissions: 

* oauth:client:authorize

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
accept_language = ''en-us'' # str | The language in which to display the client descriptions. (optional) (default to 'en-us')

try:
    # List clients that have been authorized, requested, or revoked by the resource owner
    api_response = api_instance.get_oauth_authorizations(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->get_oauth_authorizations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accept_language** | **str**| The language in which to display the client descriptions. | [optional] [default to &#39;en-us&#39;] |
{: class="table table-striped"}

### Return type

[**OAuthAuthorizationListing**](OAuthAuthorizationListing.html)

<a name="get_oauth_client"></a>

## [**OAuthClient**](OAuthClient.html) get_oauth_client(client_id)



Get OAuth Client



Wraps GET /api/v2/oauth/clients/{clientId} 

Requires ANY permissions: 

* oauth:client:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
client_id = 'client_id_example' # str | Client ID

try:
    # Get OAuth Client
    api_response = api_instance.get_oauth_client(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->get_oauth_client: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client_id** | **str**| Client ID |  |
{: class="table table-striped"}

### Return type

[**OAuthClient**](OAuthClient.html)

<a name="get_oauth_client_usage_query_result"></a>

## [**ApiUsageQueryResult**](ApiUsageQueryResult.html) get_oauth_client_usage_query_result(execution_id, client_id)



Get the results of a usage query



Wraps GET /api/v2/oauth/clients/{clientId}/usage/query/results/{executionId} 

Requires ANY permissions: 

* oauth:client:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
execution_id = 'execution_id_example' # str | ID of the query execution
client_id = 'client_id_example' # str | Client ID

try:
    # Get the results of a usage query
    api_response = api_instance.get_oauth_client_usage_query_result(execution_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->get_oauth_client_usage_query_result: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **execution_id** | **str**| ID of the query execution |  |
| **client_id** | **str**| Client ID |  |
{: class="table table-striped"}

### Return type

[**ApiUsageQueryResult**](ApiUsageQueryResult.html)

<a name="get_oauth_client_usage_summary"></a>

## [**UsageExecutionResult**](UsageExecutionResult.html) get_oauth_client_usage_summary(client_id, days=days)



Get a summary of OAuth client API usage

After calling this method, you will then need to poll for the query results based on the returned execution Id



Wraps GET /api/v2/oauth/clients/{clientId}/usage/summary 

Requires ANY permissions: 

* oauth:client:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
client_id = 'client_id_example' # str | Client ID
days = ''7'' # str | Previous number of days to query (optional) (default to '7')

try:
    # Get a summary of OAuth client API usage
    api_response = api_instance.get_oauth_client_usage_summary(client_id, days=days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->get_oauth_client_usage_summary: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client_id** | **str**| Client ID |  |
| **days** | **str**| Previous number of days to query | [optional] [default to &#39;7&#39;] |
{: class="table table-striped"}

### Return type

[**UsageExecutionResult**](UsageExecutionResult.html)

<a name="get_oauth_clients"></a>

## [**OAuthClientEntityListing**](OAuthClientEntityListing.html) get_oauth_clients()



The list of OAuth clients



Wraps GET /api/v2/oauth/clients 

Requires ANY permissions: 

* oauth:client:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()

try:
    # The list of OAuth clients
    api_response = api_instance.get_oauth_clients()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->get_oauth_clients: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**OAuthClientEntityListing**](OAuthClientEntityListing.html)

<a name="get_oauth_scope"></a>

## [**OAuthScope**](OAuthScope.html) get_oauth_scope(scope_id, accept_language=accept_language)



An OAuth scope



Wraps GET /api/v2/oauth/scopes/{scopeId} 

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
api_instance = PureCloudPlatformClientV2.OAuthApi()
scope_id = 'scope_id_example' # str | Scope ID
accept_language = ''en-us'' # str | The language with which to display the scope description. (optional) (default to 'en-us')

try:
    # An OAuth scope
    api_response = api_instance.get_oauth_scope(scope_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->get_oauth_scope: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **scope_id** | **str**| Scope ID |  |
| **accept_language** | **str**| The language with which to display the scope description. | [optional] [default to &#39;en-us&#39;] |
{: class="table table-striped"}

### Return type

[**OAuthScope**](OAuthScope.html)

<a name="get_oauth_scopes"></a>

## [**OAuthScopeListing**](OAuthScopeListing.html) get_oauth_scopes(accept_language=accept_language)



The list of OAuth scopes



Wraps GET /api/v2/oauth/scopes 

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
api_instance = PureCloudPlatformClientV2.OAuthApi()
accept_language = ''en-us'' # str | The language with which to display the scope descriptions. (optional) (default to 'en-us')

try:
    # The list of OAuth scopes
    api_response = api_instance.get_oauth_scopes(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->get_oauth_scopes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accept_language** | **str**| The language with which to display the scope descriptions. | [optional] [default to &#39;en-us&#39;] |
{: class="table table-striped"}

### Return type

[**OAuthScopeListing**](OAuthScopeListing.html)

<a name="post_oauth_client_secret"></a>

## [**OAuthClient**](OAuthClient.html) post_oauth_client_secret(client_id)



Regenerate Client Secret

This operation will set the client secret to a randomly generated cryptographically random value. All clients must be updated with the new secret. This operation should be used with caution.



Wraps POST /api/v2/oauth/clients/{clientId}/secret 

Requires ANY permissions: 

* oauth:client:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
client_id = 'client_id_example' # str | Client ID

try:
    # Regenerate Client Secret
    api_response = api_instance.post_oauth_client_secret(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->post_oauth_client_secret: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client_id** | **str**| Client ID |  |
{: class="table table-striped"}

### Return type

[**OAuthClient**](OAuthClient.html)

<a name="post_oauth_client_usage_query"></a>

## [**UsageExecutionResult**](UsageExecutionResult.html) post_oauth_client_usage_query(client_id, body)



Query for OAuth client API usage

After calling this method, you will then need to poll for the query results based on the returned execution Id



Wraps POST /api/v2/oauth/clients/{clientId}/usage/query 

Requires ANY permissions: 

* oauth:client:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
client_id = 'client_id_example' # str | Client ID
body = PureCloudPlatformClientV2.ApiUsageQuery() # ApiUsageQuery | Query

try:
    # Query for OAuth client API usage
    api_response = api_instance.post_oauth_client_usage_query(client_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->post_oauth_client_usage_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client_id** | **str**| Client ID |  |
| **body** | [**ApiUsageQuery**](ApiUsageQuery.html)| Query |  |
{: class="table table-striped"}

### Return type

[**UsageExecutionResult**](UsageExecutionResult.html)

<a name="post_oauth_clients"></a>

## [**OAuthClient**](OAuthClient.html) post_oauth_clients(body)



Create OAuth client

The OAuth Grant/Client is required in order to create an authentication token and gain access to PureCloud.  The preferred authorizedGrantTypes is 'CODE' which requires applications to send a client ID and client secret. This is typically a web server.  If the client is unable to secure the client secret then the 'TOKEN' grant type aka IMPLICIT should be used. This is would be for browser or mobile apps.  If a client is to be used outside of the context of a user then the 'CLIENT-CREDENTIALS' grant may be used. In this case the client must be granted roles  via the 'roleIds' field.



Wraps POST /api/v2/oauth/clients 

Requires ANY permissions: 

* oauth:client:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
body = PureCloudPlatformClientV2.OAuthClientRequest() # OAuthClientRequest | Client

try:
    # Create OAuth client
    api_response = api_instance.post_oauth_clients(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->post_oauth_clients: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OAuthClientRequest**](OAuthClientRequest.html)| Client |  |
{: class="table table-striped"}

### Return type

[**OAuthClient**](OAuthClient.html)

<a name="put_oauth_client"></a>

## [**OAuthClient**](OAuthClient.html) put_oauth_client(client_id, body)



Update OAuth Client



Wraps PUT /api/v2/oauth/clients/{clientId} 

Requires ANY permissions: 

* oauth:client:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
client_id = 'client_id_example' # str | Client ID
body = PureCloudPlatformClientV2.OAuthClientRequest() # OAuthClientRequest | Client

try:
    # Update OAuth Client
    api_response = api_instance.put_oauth_client(client_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->put_oauth_client: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client_id** | **str**| Client ID |  |
| **body** | [**OAuthClientRequest**](OAuthClientRequest.html)| Client |  |
{: class="table table-striped"}

### Return type

[**OAuthClient**](OAuthClient.html)


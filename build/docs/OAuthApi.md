---
title: OAuthApi
---

## PureCloudPlatformClientV2.OAuthApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_oauth_client**](OAuthApi.html#delete_oauth_client) | Delete OAuth Client|
|[**get_oauth_client**](OAuthApi.html#get_oauth_client) | Get OAuth Client|
|[**get_oauth_clients**](OAuthApi.html#get_oauth_clients) | The list of OAuth clients|
|[**post_oauth_client_secret**](OAuthApi.html#post_oauth_client_secret) | Regenerate Client Secret|
|[**post_oauth_clients**](OAuthApi.html#post_oauth_clients) | Create OAuth client|
|[**put_oauth_client**](OAuthApi.html#put_oauth_client) | Update OAuth Client|
{: class="table table-striped"}

<a name="delete_oauth_client"></a>

##  delete_oauth_client(client_id)

Delete OAuth Client



Wraps DELETE /api/v2/oauth/clients/{clientId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
client_id = 'client_id_example' # str | Client ID

try:
    # Delete OAuth Client
    api_instance.delete_oauth_client(client_id)
except ApiException as e:
    print "Exception when calling OAuthApi->delete_oauth_client: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client_id** | **str**| Client ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_oauth_client"></a>

## [**OAuthClient**](OAuthClient.html) get_oauth_client(client_id)

Get OAuth Client



Wraps GET /api/v2/oauth/clients/{clientId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
client_id = 'client_id_example' # str | Client ID

try:
    # Get OAuth Client
    api_response = api_instance.get_oauth_client(client_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OAuthApi->get_oauth_client: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client_id** | **str**| Client ID |  |
{: class="table table-striped"}

### Return type

[**OAuthClient**](OAuthClient.html)

<a name="get_oauth_clients"></a>

## [**OAuthClientEntityListing**](OAuthClientEntityListing.html) get_oauth_clients()

The list of OAuth clients



Wraps GET /api/v2/oauth/clients 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()

try:
    # The list of OAuth clients
    api_response = api_instance.get_oauth_clients()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OAuthApi->get_oauth_clients: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**OAuthClientEntityListing**](OAuthClientEntityListing.html)

<a name="post_oauth_client_secret"></a>

## [**OAuthClient**](OAuthClient.html) post_oauth_client_secret(client_id)

Regenerate Client Secret

This operation will set the client secret to a randomly generated cryptographically random value. All clients must be updated with the new secret. This operation should be used with caution.

Wraps POST /api/v2/oauth/clients/{clientId}/secret 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
client_id = 'client_id_example' # str | Client ID

try:
    # Regenerate Client Secret
    api_response = api_instance.post_oauth_client_secret(client_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OAuthApi->post_oauth_client_secret: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client_id** | **str**| Client ID |  |
{: class="table table-striped"}

### Return type

[**OAuthClient**](OAuthClient.html)

<a name="post_oauth_clients"></a>

## [**OAuthClient**](OAuthClient.html) post_oauth_clients(body)

Create OAuth client

The OAuth Grant/Client is required in order to create an authentication token and gain access to PureCloud.  The preferred authorizedGrantTypes is 'CODE' which requires applications to send a client ID and client secret. This is typically a web server.  If the client is unable to secure the client secret then the 'TOKEN' grant type aka IMPLICIT should be used. This is would be for browser or mobile apps.  If a client is to be used outside of the context of a user then the 'CLIENT-CREDENTIALS' grant may be used. In this case the client must be granted roles  via the 'roleIds' field.

Wraps POST /api/v2/oauth/clients 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
body = PureCloudPlatformClientV2.OAuthClient() # OAuthClient | Client

try:
    # Create OAuth client
    api_response = api_instance.post_oauth_clients(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OAuthApi->post_oauth_clients: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OAuthClient**](OAuthClient.html)| Client |  |
{: class="table table-striped"}

### Return type

[**OAuthClient**](OAuthClient.html)

<a name="put_oauth_client"></a>

## [**OAuthClient**](OAuthClient.html) put_oauth_client(client_id, body)

Update OAuth Client



Wraps PUT /api/v2/oauth/clients/{clientId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OAuthApi()
client_id = 'client_id_example' # str | Client ID
body = PureCloudPlatformClientV2.OAuthClient() # OAuthClient | Client

try:
    # Update OAuth Client
    api_response = api_instance.put_oauth_client(client_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OAuthApi->put_oauth_client: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client_id** | **str**| Client ID |  |
| **body** | [**OAuthClient**](OAuthClient.html)| Client |  |
{: class="table table-striped"}

### Return type

[**OAuthClient**](OAuthClient.html)


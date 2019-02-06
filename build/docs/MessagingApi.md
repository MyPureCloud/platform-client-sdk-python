---
title: MessagingApi
---

## PureCloudPlatformClientV2.MessagingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_messaging_integrations_facebook_integration_id**](MessagingApi.html#delete_messaging_integrations_facebook_integration_id) | Delete a Facebook messaging integration|
|[**delete_messaging_integrations_line_integration_id**](MessagingApi.html#delete_messaging_integrations_line_integration_id) | Delete a LINE messenger integration|
|[**delete_messaging_integrations_twitter_integration_id**](MessagingApi.html#delete_messaging_integrations_twitter_integration_id) | Delete a Twitter messaging integration|
|[**get_messaging_integrations_facebook**](MessagingApi.html#get_messaging_integrations_facebook) | Get a list of Facebook Integrations|
|[**get_messaging_integrations_facebook_integration_id**](MessagingApi.html#get_messaging_integrations_facebook_integration_id) | Get a Facebook messaging integration|
|[**get_messaging_integrations_line**](MessagingApi.html#get_messaging_integrations_line) | Get a list of LINE messenger Integrations|
|[**get_messaging_integrations_line_integration_id**](MessagingApi.html#get_messaging_integrations_line_integration_id) | Get a LINE messenger integration|
|[**get_messaging_integrations_twitter**](MessagingApi.html#get_messaging_integrations_twitter) | Get a list of Twitter Integrations|
|[**get_messaging_integrations_twitter_integration_id**](MessagingApi.html#get_messaging_integrations_twitter_integration_id) | Get a Twitter messaging integration|
|[**get_messaging_sticker**](MessagingApi.html#get_messaging_sticker) | Get a list of Messaging Stickers|
|[**post_messaging_integrations_facebook**](MessagingApi.html#post_messaging_integrations_facebook) | Create a Facebook Integration|
|[**post_messaging_integrations_line**](MessagingApi.html#post_messaging_integrations_line) | Create a LINE messenger Integration|
|[**post_messaging_integrations_twitter**](MessagingApi.html#post_messaging_integrations_twitter) | Create a Twitter Integration|
|[**put_messaging_integrations_line_integration_id**](MessagingApi.html#put_messaging_integrations_line_integration_id) | Update a LINE messenger integration|
{: class="table table-striped"}

<a name="delete_messaging_integrations_facebook_integration_id"></a>

##  delete_messaging_integrations_facebook_integration_id(integration_id)



Delete a Facebook messaging integration



Wraps DELETE /api/v2/messaging/integrations/facebook/{integrationId} 

Requires ANY permissions: 

* messaging:integration:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
integration_id = 'integration_id_example' # str | Integration ID

try:
    # Delete a Facebook messaging integration
    api_instance.delete_messaging_integrations_facebook_integration_id(integration_id)
except ApiException as e:
    print "Exception when calling MessagingApi->delete_messaging_integrations_facebook_integration_id: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_messaging_integrations_line_integration_id"></a>

##  delete_messaging_integrations_line_integration_id(integration_id)



Delete a LINE messenger integration



Wraps DELETE /api/v2/messaging/integrations/line/{integrationId} 

Requires ANY permissions: 

* messaging:integration:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
integration_id = 'integration_id_example' # str | Integration ID

try:
    # Delete a LINE messenger integration
    api_instance.delete_messaging_integrations_line_integration_id(integration_id)
except ApiException as e:
    print "Exception when calling MessagingApi->delete_messaging_integrations_line_integration_id: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_messaging_integrations_twitter_integration_id"></a>

##  delete_messaging_integrations_twitter_integration_id(integration_id)



Delete a Twitter messaging integration



Wraps DELETE /api/v2/messaging/integrations/twitter/{integrationId} 

Requires ANY permissions: 

* messaging:integration:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
integration_id = 'integration_id_example' # str | Integration ID

try:
    # Delete a Twitter messaging integration
    api_instance.delete_messaging_integrations_twitter_integration_id(integration_id)
except ApiException as e:
    print "Exception when calling MessagingApi->delete_messaging_integrations_twitter_integration_id: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_messaging_integrations_facebook"></a>

## [**FacebookIntegrationEntityListing**](FacebookIntegrationEntityListing.html) get_messaging_integrations_facebook(page_size=page_size, page_number=page_number)



Get a list of Facebook Integrations



Wraps GET /api/v2/messaging/integrations/facebook 

Requires ANY permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of Facebook Integrations
    api_response = api_instance.get_messaging_integrations_facebook(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->get_messaging_integrations_facebook: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**FacebookIntegrationEntityListing**](FacebookIntegrationEntityListing.html)

<a name="get_messaging_integrations_facebook_integration_id"></a>

## [**FacebookIntegration**](FacebookIntegration.html) get_messaging_integrations_facebook_integration_id(integration_id)



Get a Facebook messaging integration



Wraps GET /api/v2/messaging/integrations/facebook/{integrationId} 

Requires ANY permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
integration_id = 'integration_id_example' # str | Integration ID

try:
    # Get a Facebook messaging integration
    api_response = api_instance.get_messaging_integrations_facebook_integration_id(integration_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->get_messaging_integrations_facebook_integration_id: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
{: class="table table-striped"}

### Return type

[**FacebookIntegration**](FacebookIntegration.html)

<a name="get_messaging_integrations_line"></a>

## [**LineIntegrationEntityListing**](LineIntegrationEntityListing.html) get_messaging_integrations_line(page_size=page_size, page_number=page_number)



Get a list of LINE messenger Integrations



Wraps GET /api/v2/messaging/integrations/line 

Requires ANY permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of LINE messenger Integrations
    api_response = api_instance.get_messaging_integrations_line(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->get_messaging_integrations_line: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**LineIntegrationEntityListing**](LineIntegrationEntityListing.html)

<a name="get_messaging_integrations_line_integration_id"></a>

## [**LineIntegration**](LineIntegration.html) get_messaging_integrations_line_integration_id(integration_id)



Get a LINE messenger integration



Wraps GET /api/v2/messaging/integrations/line/{integrationId} 

Requires ANY permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
integration_id = 'integration_id_example' # str | Integration ID

try:
    # Get a LINE messenger integration
    api_response = api_instance.get_messaging_integrations_line_integration_id(integration_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->get_messaging_integrations_line_integration_id: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
{: class="table table-striped"}

### Return type

[**LineIntegration**](LineIntegration.html)

<a name="get_messaging_integrations_twitter"></a>

## [**TwitterIntegrationEntityListing**](TwitterIntegrationEntityListing.html) get_messaging_integrations_twitter(page_size=page_size, page_number=page_number)



Get a list of Twitter Integrations



Wraps GET /api/v2/messaging/integrations/twitter 

Requires ANY permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of Twitter Integrations
    api_response = api_instance.get_messaging_integrations_twitter(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->get_messaging_integrations_twitter: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**TwitterIntegrationEntityListing**](TwitterIntegrationEntityListing.html)

<a name="get_messaging_integrations_twitter_integration_id"></a>

## [**TwitterIntegration**](TwitterIntegration.html) get_messaging_integrations_twitter_integration_id(integration_id)



Get a Twitter messaging integration



Wraps GET /api/v2/messaging/integrations/twitter/{integrationId} 

Requires ANY permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
integration_id = 'integration_id_example' # str | Integration ID

try:
    # Get a Twitter messaging integration
    api_response = api_instance.get_messaging_integrations_twitter_integration_id(integration_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->get_messaging_integrations_twitter_integration_id: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
{: class="table table-striped"}

### Return type

[**TwitterIntegration**](TwitterIntegration.html)

<a name="get_messaging_sticker"></a>

## [**MessagingStickerEntityListing**](MessagingStickerEntityListing.html) get_messaging_sticker(messenger_type, page_size=page_size, page_number=page_number)



Get a list of Messaging Stickers



Wraps GET /api/v2/messaging/stickers/{messengerType} 

Requires ANY permissions: 

* conversation:message:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
messenger_type = 'messenger_type_example' # str | Messenger Type
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of Messaging Stickers
    api_response = api_instance.get_messaging_sticker(messenger_type, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->get_messaging_sticker: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messenger_type** | **str**| Messenger Type |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**MessagingStickerEntityListing**](MessagingStickerEntityListing.html)

<a name="post_messaging_integrations_facebook"></a>

## [**FacebookIntegration**](FacebookIntegration.html) post_messaging_integrations_facebook(body)



Create a Facebook Integration



Wraps POST /api/v2/messaging/integrations/facebook 

Requires ANY permissions: 

* messaging:integration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
body = PureCloudPlatformClientV2.FacebookIntegrationRequest() # FacebookIntegrationRequest | FacebookIntegrationRequest

try:
    # Create a Facebook Integration
    api_response = api_instance.post_messaging_integrations_facebook(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->post_messaging_integrations_facebook: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FacebookIntegrationRequest**](FacebookIntegrationRequest.html)| FacebookIntegrationRequest |  |
{: class="table table-striped"}

### Return type

[**FacebookIntegration**](FacebookIntegration.html)

<a name="post_messaging_integrations_line"></a>

## [**LineIntegration**](LineIntegration.html) post_messaging_integrations_line(body)



Create a LINE messenger Integration



Wraps POST /api/v2/messaging/integrations/line 

Requires ANY permissions: 

* messaging:integration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
body = PureCloudPlatformClientV2.LineIntegrationRequest() # LineIntegrationRequest | LineIntegrationRequest

try:
    # Create a LINE messenger Integration
    api_response = api_instance.post_messaging_integrations_line(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->post_messaging_integrations_line: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LineIntegrationRequest**](LineIntegrationRequest.html)| LineIntegrationRequest |  |
{: class="table table-striped"}

### Return type

[**LineIntegration**](LineIntegration.html)

<a name="post_messaging_integrations_twitter"></a>

## [**TwitterIntegration**](TwitterIntegration.html) post_messaging_integrations_twitter(body)



Create a Twitter Integration



Wraps POST /api/v2/messaging/integrations/twitter 

Requires ANY permissions: 

* messaging:integration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
body = PureCloudPlatformClientV2.TwitterIntegrationRequest() # TwitterIntegrationRequest | TwitterIntegrationRequest

try:
    # Create a Twitter Integration
    api_response = api_instance.post_messaging_integrations_twitter(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->post_messaging_integrations_twitter: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TwitterIntegrationRequest**](TwitterIntegrationRequest.html)| TwitterIntegrationRequest |  |
{: class="table table-striped"}

### Return type

[**TwitterIntegration**](TwitterIntegration.html)

<a name="put_messaging_integrations_line_integration_id"></a>

## [**LineIntegration**](LineIntegration.html) put_messaging_integrations_line_integration_id(integration_id, body)



Update a LINE messenger integration



Wraps PUT /api/v2/messaging/integrations/line/{integrationId} 

Requires ANY permissions: 

* messaging:integration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.MessagingApi()
integration_id = 'integration_id_example' # str | Integration ID
body = PureCloudPlatformClientV2.LineIntegrationRequest() # LineIntegrationRequest | LineIntegrationRequest

try:
    # Update a LINE messenger integration
    api_response = api_instance.put_messaging_integrations_line_integration_id(integration_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->put_messaging_integrations_line_integration_id: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **body** | [**LineIntegrationRequest**](LineIntegrationRequest.html)| LineIntegrationRequest |  |
{: class="table table-striped"}

### Return type

[**LineIntegration**](LineIntegration.html)


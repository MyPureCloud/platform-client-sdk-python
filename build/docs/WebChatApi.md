---
title: WebChatApi
---

## PureCloudPlatformClientV2.WebChatApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_webchat_deployment**](WebChatApi.html#delete_webchat_deployment) | Delete a WebChat deployment|
|[**delete_webchat_settings**](WebChatApi.html#delete_webchat_settings) | Remove WebChat deployment settings|
|[**get_webchat_deployment**](WebChatApi.html#get_webchat_deployment) | Get a WebChat deployment|
|[**get_webchat_deployments**](WebChatApi.html#get_webchat_deployments) | List WebChat deployments|
|[**get_webchat_settings**](WebChatApi.html#get_webchat_settings) | Get WebChat deployment settings|
|[**post_webchat_deployments**](WebChatApi.html#post_webchat_deployments) | Create WebChat deployment|
|[**put_webchat_deployment**](WebChatApi.html#put_webchat_deployment) | Update a WebChat deployment|
|[**put_webchat_settings**](WebChatApi.html#put_webchat_settings) | Update WebChat deployment settings|
{: class="table table-striped"}

<a name="delete_webchat_deployment"></a>

##  delete_webchat_deployment(deployment_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Delete a WebChat deployment



Wraps DELETE /api/v2/webchat/deployments/{deploymentId} 

Requires ANY permissions: 

* webchat:deployment:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
deployment_id = 'deployment_id_example' # str | Deployment Id

try:
    # Delete a WebChat deployment
    api_instance.delete_webchat_deployment(deployment_id)
except ApiException as e:
    print "Exception when calling WebChatApi->delete_webchat_deployment: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| Deployment Id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_webchat_settings"></a>

##  delete_webchat_settings()



Remove WebChat deployment settings



Wraps DELETE /api/v2/webchat/settings 

Requires ANY permissions: 

* webchat:deployment:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()

try:
    # Remove WebChat deployment settings
    api_instance.delete_webchat_settings()
except ApiException as e:
    print "Exception when calling WebChatApi->delete_webchat_settings: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_webchat_deployment"></a>

## [**WebChatDeployment**](WebChatDeployment.html) get_webchat_deployment(deployment_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get a WebChat deployment



Wraps GET /api/v2/webchat/deployments/{deploymentId} 

Requires ANY permissions: 

* webchat:deployment:read

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
deployment_id = 'deployment_id_example' # str | Deployment Id

try:
    # Get a WebChat deployment
    api_response = api_instance.get_webchat_deployment(deployment_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebChatApi->get_webchat_deployment: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| Deployment Id |  |
{: class="table table-striped"}

### Return type

[**WebChatDeployment**](WebChatDeployment.html)

<a name="get_webchat_deployments"></a>

## [**WebChatDeploymentEntityListing**](WebChatDeploymentEntityListing.html) get_webchat_deployments()

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

List WebChat deployments



Wraps GET /api/v2/webchat/deployments 

Requires ANY permissions: 

* webchat:deployment:read

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()

try:
    # List WebChat deployments
    api_response = api_instance.get_webchat_deployments()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebChatApi->get_webchat_deployments: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**WebChatDeploymentEntityListing**](WebChatDeploymentEntityListing.html)

<a name="get_webchat_settings"></a>

## [**WebChatSettings**](WebChatSettings.html) get_webchat_settings()



Get WebChat deployment settings



Wraps GET /api/v2/webchat/settings 

Requires ANY permissions: 

* webchat:deployment:read

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()

try:
    # Get WebChat deployment settings
    api_response = api_instance.get_webchat_settings()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebChatApi->get_webchat_settings: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**WebChatSettings**](WebChatSettings.html)

<a name="post_webchat_deployments"></a>

## [**WebChatDeployment**](WebChatDeployment.html) post_webchat_deployments(body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Create WebChat deployment



Wraps POST /api/v2/webchat/deployments 

Requires ANY permissions: 

* webchat:deployment:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
body = PureCloudPlatformClientV2.WebChatDeployment() # WebChatDeployment | Deployment

try:
    # Create WebChat deployment
    api_response = api_instance.post_webchat_deployments(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebChatApi->post_webchat_deployments: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WebChatDeployment**](WebChatDeployment.html)| Deployment |  |
{: class="table table-striped"}

### Return type

[**WebChatDeployment**](WebChatDeployment.html)

<a name="put_webchat_deployment"></a>

## [**WebChatDeployment**](WebChatDeployment.html) put_webchat_deployment(deployment_id, body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update a WebChat deployment



Wraps PUT /api/v2/webchat/deployments/{deploymentId} 

Requires ANY permissions: 

* webchat:deployment:update

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
deployment_id = 'deployment_id_example' # str | Deployment Id
body = PureCloudPlatformClientV2.WebChatDeployment() # WebChatDeployment | Deployment

try:
    # Update a WebChat deployment
    api_response = api_instance.put_webchat_deployment(deployment_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebChatApi->put_webchat_deployment: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| Deployment Id |  |
| **body** | [**WebChatDeployment**](WebChatDeployment.html)| Deployment |  |
{: class="table table-striped"}

### Return type

[**WebChatDeployment**](WebChatDeployment.html)

<a name="put_webchat_settings"></a>

## [**WebChatSettings**](WebChatSettings.html) put_webchat_settings(body)



Update WebChat deployment settings



Wraps PUT /api/v2/webchat/settings 

Requires ANY permissions: 

* webchat:deployment:update

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebChatApi()
body = PureCloudPlatformClientV2.WebChatSettings() # WebChatSettings | webChatSettings

try:
    # Update WebChat deployment settings
    api_response = api_instance.put_webchat_settings(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebChatApi->put_webchat_settings: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WebChatSettings**](WebChatSettings.html)| webChatSettings |  |
{: class="table table-striped"}

### Return type

[**WebChatSettings**](WebChatSettings.html)


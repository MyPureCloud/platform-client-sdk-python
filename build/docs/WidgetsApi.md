---
title: WidgetsApi
---

## PureCloudPlatformClientV2.WidgetsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_widgets_deployment**](WidgetsApi.html#delete_widgets_deployment) | Delete a Widget deployment|
|[**get_widgets_deployment**](WidgetsApi.html#get_widgets_deployment) | Get a Widget deployment|
|[**get_widgets_deployments**](WidgetsApi.html#get_widgets_deployments) | List Widget deployments|
|[**post_widgets_deployments**](WidgetsApi.html#post_widgets_deployments) | Create Widget deployment|
|[**put_widgets_deployment**](WidgetsApi.html#put_widgets_deployment) | Update a Widget deployment|
{: class="table table-striped"}

<a name="delete_widgets_deployment"></a>

##  delete_widgets_deployment(deployment_id)



Delete a Widget deployment

Wraps DELETE /api/v2/widgets/deployments/{deploymentId} 

Requires ANY permissions: 

* widgets:deployment:delete
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
api_instance = PureCloudPlatformClientV2.WidgetsApi()
deployment_id = 'deployment_id_example' # str | Widget Config Id

try:
    # Delete a Widget deployment
    api_instance.delete_widgets_deployment(deployment_id)
except ApiException as e:
    print("Exception when calling WidgetsApi->delete_widgets_deployment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| Widget Config Id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_widgets_deployment"></a>

## [**WidgetDeployment**](WidgetDeployment.html) get_widgets_deployment(deployment_id)



Get a Widget deployment

Wraps GET /api/v2/widgets/deployments/{deploymentId} 

Requires ANY permissions: 

* widgets:deployment:view
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
api_instance = PureCloudPlatformClientV2.WidgetsApi()
deployment_id = 'deployment_id_example' # str | Widget Config Id

try:
    # Get a Widget deployment
    api_response = api_instance.get_widgets_deployment(deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->get_widgets_deployment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| Widget Config Id |  |
{: class="table table-striped"}

### Return type

[**WidgetDeployment**](WidgetDeployment.html)

<a name="get_widgets_deployments"></a>

## [**WidgetDeploymentEntityListing**](WidgetDeploymentEntityListing.html) get_widgets_deployments()



List Widget deployments

Wraps GET /api/v2/widgets/deployments 

Requires ANY permissions: 

* widgets:deployment:view
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
api_instance = PureCloudPlatformClientV2.WidgetsApi()

try:
    # List Widget deployments
    api_response = api_instance.get_widgets_deployments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->get_widgets_deployments: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**WidgetDeploymentEntityListing**](WidgetDeploymentEntityListing.html)

<a name="post_widgets_deployments"></a>

## [**WidgetDeployment**](WidgetDeployment.html) post_widgets_deployments(body)



Create Widget deployment

Wraps POST /api/v2/widgets/deployments 

Requires ANY permissions: 

* widgets:deployment:add
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
api_instance = PureCloudPlatformClientV2.WidgetsApi()
body = PureCloudPlatformClientV2.WidgetDeployment() # WidgetDeployment | Deployment

try:
    # Create Widget deployment
    api_response = api_instance.post_widgets_deployments(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->post_widgets_deployments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WidgetDeployment**](WidgetDeployment.html)| Deployment |  |
{: class="table table-striped"}

### Return type

[**WidgetDeployment**](WidgetDeployment.html)

<a name="put_widgets_deployment"></a>

## [**WidgetDeployment**](WidgetDeployment.html) put_widgets_deployment(deployment_id, body)



Update a Widget deployment

Wraps PUT /api/v2/widgets/deployments/{deploymentId} 

Requires ANY permissions: 

* widgets:deployment:edit
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
api_instance = PureCloudPlatformClientV2.WidgetsApi()
deployment_id = 'deployment_id_example' # str | Widget Config Id
body = PureCloudPlatformClientV2.WidgetDeployment() # WidgetDeployment | Deployment

try:
    # Update a Widget deployment
    api_response = api_instance.put_widgets_deployment(deployment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->put_widgets_deployment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| Widget Config Id |  |
| **body** | [**WidgetDeployment**](WidgetDeployment.html)| Deployment |  |
{: class="table table-striped"}

### Return type

[**WidgetDeployment**](WidgetDeployment.html)


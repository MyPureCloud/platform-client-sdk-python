# WidgetsApi

## PureCloudPlatformClientV2.WidgetsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_widgets_deployment**](#delete_widgets_deployment) | Delete a Widget deployment|
|[**get_widgets_deployment**](#get_widgets_deployment) | Get a Widget deployment|
|[**get_widgets_deployments**](#get_widgets_deployments) | List Widget deployments|
|[**post_widgets_deployments**](#post_widgets_deployments) | Create Widget deployment|
|[**put_widgets_deployment**](#put_widgets_deployment) | Update a Widget deployment|



## delete_widgets_deployment

>  delete_widgets_deployment(deployment_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Delete a Widget deployment

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-removal-of-acd-web-chat-version-2/. 

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

### Return type

void (empty response body)


## get_widgets_deployment

> [**WidgetDeployment**](WidgetDeployment) get_widgets_deployment(deployment_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get a Widget deployment

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-removal-of-acd-web-chat-version-2/. 

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

### Return type

[**WidgetDeployment**](WidgetDeployment)


## get_widgets_deployments

> [**WidgetDeploymentEntityListing**](WidgetDeploymentEntityListing) get_widgets_deployments()

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

List Widget deployments

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-removal-of-acd-web-chat-version-2/. 

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

[**WidgetDeploymentEntityListing**](WidgetDeploymentEntityListing)


## post_widgets_deployments

> [**WidgetDeployment**](WidgetDeployment) post_widgets_deployments(body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Create Widget deployment

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-removal-of-acd-web-chat-version-2/. 

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
| **body** | [**WidgetDeployment**](WidgetDeployment)| Deployment |  |

### Return type

[**WidgetDeployment**](WidgetDeployment)


## put_widgets_deployment

> [**WidgetDeployment**](WidgetDeployment) put_widgets_deployment(deployment_id, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Update a Widget deployment

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-removal-of-acd-web-chat-version-2/. 

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
| **body** | [**WidgetDeployment**](WidgetDeployment)| Deployment |  |

### Return type

[**WidgetDeployment**](WidgetDeployment)


_PureCloudPlatformClientV2 229.0.0_

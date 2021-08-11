---
title: WebDeploymentsApi
---

## PureCloudPlatformClientV2.WebDeploymentsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_webdeployments_configuration**](WebDeploymentsApi.html#delete_webdeployments_configuration) | Delete all versions of a configuration|
|[**delete_webdeployments_deployment**](WebDeploymentsApi.html#delete_webdeployments_deployment) | Delete a deployment|
|[**get_webdeployments_configuration_version**](WebDeploymentsApi.html#get_webdeployments_configuration_version) | Get a configuration version|
|[**get_webdeployments_configuration_versions**](WebDeploymentsApi.html#get_webdeployments_configuration_versions) | Get the versions of a configuration|
|[**get_webdeployments_configuration_versions_draft**](WebDeploymentsApi.html#get_webdeployments_configuration_versions_draft) | Get the configuration draft|
|[**get_webdeployments_configurations**](WebDeploymentsApi.html#get_webdeployments_configurations) | View configuration drafts|
|[**get_webdeployments_deployment**](WebDeploymentsApi.html#get_webdeployments_deployment) | Get a deployment|
|[**get_webdeployments_deployments**](WebDeploymentsApi.html#get_webdeployments_deployments) | Get deployments|
|[**post_webdeployments_configuration_versions_draft_publish**](WebDeploymentsApi.html#post_webdeployments_configuration_versions_draft_publish) | Publish the configuration draft and create a new version|
|[**post_webdeployments_configurations**](WebDeploymentsApi.html#post_webdeployments_configurations) | Create a configuration draft|
|[**post_webdeployments_deployments**](WebDeploymentsApi.html#post_webdeployments_deployments) | Create a deployment|
|[**put_webdeployments_configuration_versions_draft**](WebDeploymentsApi.html#put_webdeployments_configuration_versions_draft) | Update the configuration draft|
|[**put_webdeployments_deployment**](WebDeploymentsApi.html#put_webdeployments_deployment) | Update a deployment|
{: class="table table-striped"}

<a name="delete_webdeployments_configuration"></a>

##  delete_webdeployments_configuration(configuration_id)



Delete all versions of a configuration



Wraps DELETE /api/v2/webdeployments/configurations/{configurationId} 

Requires ALL permissions: 

* webDeployments:configuration:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
configuration_id = 'configuration_id_example' # str | The configuration version ID

try:
    # Delete all versions of a configuration
    api_instance.delete_webdeployments_configuration(configuration_id)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->delete_webdeployments_configuration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **configuration_id** | **str**| The configuration version ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_webdeployments_deployment"></a>

##  delete_webdeployments_deployment(deployment_id)



Delete a deployment



Wraps DELETE /api/v2/webdeployments/deployments/{deploymentId} 

Requires ALL permissions: 

* webDeployments:deployment:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
deployment_id = 'deployment_id_example' # str | The deployment ID

try:
    # Delete a deployment
    api_instance.delete_webdeployments_deployment(deployment_id)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->delete_webdeployments_deployment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| The deployment ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_webdeployments_configuration_version"></a>

## [**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion.html) get_webdeployments_configuration_version(configuration_id, version_id)



Get a configuration version



Wraps GET /api/v2/webdeployments/configurations/{configurationId}/versions/{versionId} 

Requires ALL permissions: 

* webDeployments:configuration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
configuration_id = 'configuration_id_example' # str | The configuration version ID
version_id = 'version_id_example' # str | The version of the configuration to get

try:
    # Get a configuration version
    api_response = api_instance.get_webdeployments_configuration_version(configuration_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->get_webdeployments_configuration_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **configuration_id** | **str**| The configuration version ID |  |
| **version_id** | **str**| The version of the configuration to get |  |
{: class="table table-striped"}

### Return type

[**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion.html)

<a name="get_webdeployments_configuration_versions"></a>

## [**WebDeploymentConfigurationVersionEntityListing**](WebDeploymentConfigurationVersionEntityListing.html) get_webdeployments_configuration_versions(configuration_id)



Get the versions of a configuration

This returns the 50 most recent versions for this configuration

Wraps GET /api/v2/webdeployments/configurations/{configurationId}/versions 

Requires ALL permissions: 

* webDeployments:configuration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
configuration_id = 'configuration_id_example' # str | The configuration version ID

try:
    # Get the versions of a configuration
    api_response = api_instance.get_webdeployments_configuration_versions(configuration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->get_webdeployments_configuration_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **configuration_id** | **str**| The configuration version ID |  |
{: class="table table-striped"}

### Return type

[**WebDeploymentConfigurationVersionEntityListing**](WebDeploymentConfigurationVersionEntityListing.html)

<a name="get_webdeployments_configuration_versions_draft"></a>

## [**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion.html) get_webdeployments_configuration_versions_draft(configuration_id)



Get the configuration draft



Wraps GET /api/v2/webdeployments/configurations/{configurationId}/versions/draft 

Requires ALL permissions: 

* webDeployments:configuration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
configuration_id = 'configuration_id_example' # str | The configuration version ID

try:
    # Get the configuration draft
    api_response = api_instance.get_webdeployments_configuration_versions_draft(configuration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->get_webdeployments_configuration_versions_draft: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **configuration_id** | **str**| The configuration version ID |  |
{: class="table table-striped"}

### Return type

[**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion.html)

<a name="get_webdeployments_configurations"></a>

## [**WebDeploymentConfigurationVersionEntityListing**](WebDeploymentConfigurationVersionEntityListing.html) get_webdeployments_configurations(show_only_published=show_only_published)



View configuration drafts



Wraps GET /api/v2/webdeployments/configurations 

Requires ALL permissions: 

* webDeployments:configuration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
show_only_published = false # bool | Get only configuration drafts with published versions (optional) (default to false)

try:
    # View configuration drafts
    api_response = api_instance.get_webdeployments_configurations(show_only_published=show_only_published)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->get_webdeployments_configurations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **show_only_published** | **bool**| Get only configuration drafts with published versions | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**WebDeploymentConfigurationVersionEntityListing**](WebDeploymentConfigurationVersionEntityListing.html)

<a name="get_webdeployments_deployment"></a>

## [**WebDeployment**](WebDeployment.html) get_webdeployments_deployment(deployment_id)



Get a deployment



Wraps GET /api/v2/webdeployments/deployments/{deploymentId} 

Requires ALL permissions: 

* webDeployments:deployment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
deployment_id = 'deployment_id_example' # str | The deployment ID

try:
    # Get a deployment
    api_response = api_instance.get_webdeployments_deployment(deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->get_webdeployments_deployment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| The deployment ID |  |
{: class="table table-striped"}

### Return type

[**WebDeployment**](WebDeployment.html)

<a name="get_webdeployments_deployments"></a>

## [**WebDeploymentEntityListing**](WebDeploymentEntityListing.html) get_webdeployments_deployments()



Get deployments



Wraps GET /api/v2/webdeployments/deployments 

Requires ALL permissions: 

* webDeployments:deployment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()

try:
    # Get deployments
    api_response = api_instance.get_webdeployments_deployments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->get_webdeployments_deployments: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**WebDeploymentEntityListing**](WebDeploymentEntityListing.html)

<a name="post_webdeployments_configuration_versions_draft_publish"></a>

## [**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion.html) post_webdeployments_configuration_versions_draft_publish(configuration_id)



Publish the configuration draft and create a new version



Wraps POST /api/v2/webdeployments/configurations/{configurationId}/versions/draft/publish 

Requires ALL permissions: 

* webDeployments:configuration:edit
* webDeployments:configuration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
configuration_id = 'configuration_id_example' # str | The configuration version ID

try:
    # Publish the configuration draft and create a new version
    api_response = api_instance.post_webdeployments_configuration_versions_draft_publish(configuration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->post_webdeployments_configuration_versions_draft_publish: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **configuration_id** | **str**| The configuration version ID |  |
{: class="table table-striped"}

### Return type

[**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion.html)

<a name="post_webdeployments_configurations"></a>

## [**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion.html) post_webdeployments_configurations(configuration_version)



Create a configuration draft



Wraps POST /api/v2/webdeployments/configurations 

Requires ALL permissions: 

* webDeployments:configuration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
configuration_version = PureCloudPlatformClientV2.WebDeploymentConfigurationVersion() # WebDeploymentConfigurationVersion | 

try:
    # Create a configuration draft
    api_response = api_instance.post_webdeployments_configurations(configuration_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->post_webdeployments_configurations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **configuration_version** | [**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion.html)|  |  |
{: class="table table-striped"}

### Return type

[**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion.html)

<a name="post_webdeployments_deployments"></a>

## [**WebDeployment**](WebDeployment.html) post_webdeployments_deployments(deployment)



Create a deployment



Wraps POST /api/v2/webdeployments/deployments 

Requires ALL permissions: 

* webDeployments:deployment:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
deployment = PureCloudPlatformClientV2.WebDeployment() # WebDeployment | 

try:
    # Create a deployment
    api_response = api_instance.post_webdeployments_deployments(deployment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->post_webdeployments_deployments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment** | [**WebDeployment**](WebDeployment.html)|  |  |
{: class="table table-striped"}

### Return type

[**WebDeployment**](WebDeployment.html)

<a name="put_webdeployments_configuration_versions_draft"></a>

## [**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion.html) put_webdeployments_configuration_versions_draft(configuration_id, configuration_version)



Update the configuration draft



Wraps PUT /api/v2/webdeployments/configurations/{configurationId}/versions/draft 

Requires ALL permissions: 

* webDeployments:configuration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
configuration_id = 'configuration_id_example' # str | The configuration version ID
configuration_version = PureCloudPlatformClientV2.WebDeploymentConfigurationVersion() # WebDeploymentConfigurationVersion | 

try:
    # Update the configuration draft
    api_response = api_instance.put_webdeployments_configuration_versions_draft(configuration_id, configuration_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->put_webdeployments_configuration_versions_draft: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **configuration_id** | **str**| The configuration version ID |  |
| **configuration_version** | [**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion.html)|  |  |
{: class="table table-striped"}

### Return type

[**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion.html)

<a name="put_webdeployments_deployment"></a>

## [**WebDeployment**](WebDeployment.html) put_webdeployments_deployment(deployment_id, deployment)



Update a deployment



Wraps PUT /api/v2/webdeployments/deployments/{deploymentId} 

Requires ALL permissions: 

* webDeployments:deployment:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
deployment_id = 'deployment_id_example' # str | The deployment ID
deployment = PureCloudPlatformClientV2.WebDeployment() # WebDeployment | 

try:
    # Update a deployment
    api_response = api_instance.put_webdeployments_deployment(deployment_id, deployment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->put_webdeployments_deployment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| The deployment ID |  |
| **deployment** | [**WebDeployment**](WebDeployment.html)|  |  |
{: class="table table-striped"}

### Return type

[**WebDeployment**](WebDeployment.html)


---
title: WebDeploymentsApi
---

## PureCloudPlatformClientV2.WebDeploymentsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_webdeployments_configuration**](WebDeploymentsApi.html#delete_webdeployments_configuration) | Delete all versions of a configuration|
|[**delete_webdeployments_deployment**](WebDeploymentsApi.html#delete_webdeployments_deployment) | Delete a deployment|
|[**delete_webdeployments_deployment_cobrowse_session_id**](WebDeploymentsApi.html#delete_webdeployments_deployment_cobrowse_session_id) | Deletes a cobrowse session|
|[**delete_webdeployments_token_revoke**](WebDeploymentsApi.html#delete_webdeployments_token_revoke) | Invalidate JWT|
|[**get_webdeployments_configuration_version**](WebDeploymentsApi.html#get_webdeployments_configuration_version) | Get a configuration version|
|[**get_webdeployments_configuration_versions**](WebDeploymentsApi.html#get_webdeployments_configuration_versions) | Get the versions of a configuration|
|[**get_webdeployments_configuration_versions_draft**](WebDeploymentsApi.html#get_webdeployments_configuration_versions_draft) | Get the configuration draft|
|[**get_webdeployments_configurations**](WebDeploymentsApi.html#get_webdeployments_configurations) | View configuration drafts|
|[**get_webdeployments_deployment**](WebDeploymentsApi.html#get_webdeployments_deployment) | Get a deployment|
|[**get_webdeployments_deployment_cobrowse_session_id**](WebDeploymentsApi.html#get_webdeployments_deployment_cobrowse_session_id) | Retrieves a cobrowse session|
|[**get_webdeployments_deployment_configurations**](WebDeploymentsApi.html#get_webdeployments_deployment_configurations) | Get active configuration for a given deployment|
|[**get_webdeployments_deployments**](WebDeploymentsApi.html#get_webdeployments_deployments) | Get deployments|
|[**post_webdeployments_configuration_versions_draft_publish**](WebDeploymentsApi.html#post_webdeployments_configuration_versions_draft_publish) | Publish the configuration draft and create a new version|
|[**post_webdeployments_configurations**](WebDeploymentsApi.html#post_webdeployments_configurations) | Create a configuration draft|
|[**post_webdeployments_deployments**](WebDeploymentsApi.html#post_webdeployments_deployments) | Create a deployment|
|[**post_webdeployments_token_oauthcodegrantjwtexchange**](WebDeploymentsApi.html#post_webdeployments_token_oauthcodegrantjwtexchange) | Exchange an oAuth code (obtained using the Authorization Code Flow) for a JWT that can be used by webdeployments.|
|[**post_webdeployments_token_refresh**](WebDeploymentsApi.html#post_webdeployments_token_refresh) | Refresh a JWT.|
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

<a name="delete_webdeployments_deployment_cobrowse_session_id"></a>

## object** delete_webdeployments_deployment_cobrowse_session_id(deployment_id, session_id)



Deletes a cobrowse session



Wraps DELETE /api/v2/webdeployments/deployments/{deploymentId}/cobrowse/{sessionId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
deployment_id = 'deployment_id_example' # str | WebMessaging deployment ID
session_id = 'session_id_example' # str | Cobrowse session id or join code

try:
    # Deletes a cobrowse session
    api_response = api_instance.delete_webdeployments_deployment_cobrowse_session_id(deployment_id, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->delete_webdeployments_deployment_cobrowse_session_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| WebMessaging deployment ID |  |
| **session_id** | **str**| Cobrowse session id or join code |  |
{: class="table table-striped"}

### Return type

**object**

<a name="delete_webdeployments_token_revoke"></a>

##  delete_webdeployments_token_revoke(x_journey_session_id=x_journey_session_id, x_journey_session_type=x_journey_session_type)



Invalidate JWT



Wraps DELETE /api/v2/webdeployments/token/revoke 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
x_journey_session_id = 'x_journey_session_id_example' # str | The Customer's journey sessionId. (optional)
x_journey_session_type = 'x_journey_session_type_example' # str | The Customer's journey session type. (optional)

try:
    # Invalidate JWT
    api_instance.delete_webdeployments_token_revoke(x_journey_session_id=x_journey_session_id, x_journey_session_type=x_journey_session_type)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->delete_webdeployments_token_revoke: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **x_journey_session_id** | **str**| The Customer&#39;s journey sessionId. | [optional]  |
| **x_journey_session_type** | **str**| The Customer&#39;s journey session type. | [optional]  |
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
show_only_published = False # bool | Get only configuration drafts with published versions (optional) (default to False)

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
| **show_only_published** | **bool**| Get only configuration drafts with published versions | [optional] [default to False] |
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

<a name="get_webdeployments_deployment_cobrowse_session_id"></a>

## [**CobrowseWebMessagingSession**](CobrowseWebMessagingSession.html) get_webdeployments_deployment_cobrowse_session_id(deployment_id, session_id)



Retrieves a cobrowse session



Wraps GET /api/v2/webdeployments/deployments/{deploymentId}/cobrowse/{sessionId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
deployment_id = 'deployment_id_example' # str | WebMessaging deployment ID
session_id = 'session_id_example' # str | Cobrowse session id or join code

try:
    # Retrieves a cobrowse session
    api_response = api_instance.get_webdeployments_deployment_cobrowse_session_id(deployment_id, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->get_webdeployments_deployment_cobrowse_session_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| WebMessaging deployment ID |  |
| **session_id** | **str**| Cobrowse session id or join code |  |
{: class="table table-striped"}

### Return type

[**CobrowseWebMessagingSession**](CobrowseWebMessagingSession.html)

<a name="get_webdeployments_deployment_configurations"></a>

## [**WebDeploymentActiveConfigurationOnDeployment**](WebDeploymentActiveConfigurationOnDeployment.html) get_webdeployments_deployment_configurations(deployment_id, type=type)



Get active configuration for a given deployment



Wraps GET /api/v2/webdeployments/deployments/{deploymentId}/configurations 

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
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
deployment_id = 'deployment_id_example' # str | The deployment ID
type = 'type_example' # str | Get active configuration on a deployment (optional)

try:
    # Get active configuration for a given deployment
    api_response = api_instance.get_webdeployments_deployment_configurations(deployment_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->get_webdeployments_deployment_configurations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| The deployment ID |  |
| **type** | **str**| Get active configuration on a deployment | [optional]  |
{: class="table table-striped"}

### Return type

[**WebDeploymentActiveConfigurationOnDeployment**](WebDeploymentActiveConfigurationOnDeployment.html)

<a name="get_webdeployments_deployments"></a>

## [**ExpandableWebDeploymentEntityListing**](ExpandableWebDeploymentEntityListing.html) get_webdeployments_deployments(expand=expand)



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
expand = ['expand_example'] # list[str] | The specified entity attributes will be filled. Comma separated values expected. Valid values: (optional)

try:
    # Get deployments
    api_response = api_instance.get_webdeployments_deployments(expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->get_webdeployments_deployments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| The specified entity attributes will be filled. Comma separated values expected. Valid values: | [optional] <br />**Values**: Configuration |
{: class="table table-striped"}

### Return type

[**ExpandableWebDeploymentEntityListing**](ExpandableWebDeploymentEntityListing.html)

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

<a name="post_webdeployments_token_oauthcodegrantjwtexchange"></a>

## [**WebDeploymentsAuthorizationResponse**](WebDeploymentsAuthorizationResponse.html) post_webdeployments_token_oauthcodegrantjwtexchange(body)



Exchange an oAuth code (obtained using the Authorization Code Flow) for a JWT that can be used by webdeployments.



Wraps POST /api/v2/webdeployments/token/oauthcodegrantjwtexchange 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
body = PureCloudPlatformClientV2.WebDeploymentsOAuthExchangeRequest() # WebDeploymentsOAuthExchangeRequest | webDeploymentsOAuthExchangeRequest

try:
    # Exchange an oAuth code (obtained using the Authorization Code Flow) for a JWT that can be used by webdeployments.
    api_response = api_instance.post_webdeployments_token_oauthcodegrantjwtexchange(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->post_webdeployments_token_oauthcodegrantjwtexchange: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WebDeploymentsOAuthExchangeRequest**](WebDeploymentsOAuthExchangeRequest.html)| webDeploymentsOAuthExchangeRequest |  |
{: class="table table-striped"}

### Return type

[**WebDeploymentsAuthorizationResponse**](WebDeploymentsAuthorizationResponse.html)

<a name="post_webdeployments_token_refresh"></a>

## [**SignedData**](SignedData.html) post_webdeployments_token_refresh(body=body)



Refresh a JWT.



Wraps POST /api/v2/webdeployments/token/refresh 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WebDeploymentsApi()
body = PureCloudPlatformClientV2.WebDeploymentsRefreshJWTRequest() # WebDeploymentsRefreshJWTRequest |  (optional)

try:
    # Refresh a JWT.
    api_response = api_instance.post_webdeployments_token_refresh(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->post_webdeployments_token_refresh: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WebDeploymentsRefreshJWTRequest**](WebDeploymentsRefreshJWTRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**SignedData**](SignedData.html)

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


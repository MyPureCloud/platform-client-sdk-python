# WebDeploymentsApi

## PureCloudPlatformClientV2.WebDeploymentsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_webdeployments_configuration**](#delete_webdeployments_configuration) | Delete all versions of a configuration|
|[**delete_webdeployments_deployment**](#delete_webdeployments_deployment) | Delete a deployment|
|[**delete_webdeployments_deployment_cobrowse_session_id**](#delete_webdeployments_deployment_cobrowse_session_id) | Deletes a cobrowse session|
|[**delete_webdeployments_token_revoke**](#delete_webdeployments_token_revoke) | Invalidate JWT|
|[**get_webdeployments_configuration_version**](#get_webdeployments_configuration_version) | Get a configuration version|
|[**get_webdeployments_configuration_versions**](#get_webdeployments_configuration_versions) | Get the versions of a configuration|
|[**get_webdeployments_configuration_versions_draft**](#get_webdeployments_configuration_versions_draft) | Get the configuration draft|
|[**get_webdeployments_configurations**](#get_webdeployments_configurations) | View configuration drafts|
|[**get_webdeployments_deployment**](#get_webdeployments_deployment) | Get a deployment|
|[**get_webdeployments_deployment_cobrowse_session_id**](#get_webdeployments_deployment_cobrowse_session_id) | Retrieves a cobrowse session|
|[**get_webdeployments_deployment_configurations**](#get_webdeployments_deployment_configurations) | Get active configuration for a given deployment|
|[**get_webdeployments_deployment_identityresolution**](#get_webdeployments_deployment_identityresolution) | Get a deployment identity resolution setting.|
|[**get_webdeployments_deployments**](#get_webdeployments_deployments) | Get deployments|
|[**post_webdeployments_configuration_versions_draft_publish**](#post_webdeployments_configuration_versions_draft_publish) | Publish the configuration draft and create a new version|
|[**post_webdeployments_configurations**](#post_webdeployments_configurations) | Create a configuration draft|
|[**post_webdeployments_deployments**](#post_webdeployments_deployments) | Create a deployment|
|[**post_webdeployments_token_oauthcodegrantjwtexchange**](#post_webdeployments_token_oauthcodegrantjwtexchange) | Exchange an oAuth code (obtained using the Authorization Code Flow or Implicit flow) for a JWT that can be used by webdeployments.|
|[**post_webdeployments_token_refresh**](#post_webdeployments_token_refresh) | Refresh a JWT.|
|[**put_webdeployments_configuration_versions_draft**](#put_webdeployments_configuration_versions_draft) | Update the configuration draft|
|[**put_webdeployments_deployment**](#put_webdeployments_deployment) | Update a deployment|
|[**put_webdeployments_deployment_identityresolution**](#put_webdeployments_deployment_identityresolution) | Update identity resolution settings for a deployment.|



## delete_webdeployments_configuration

>  delete_webdeployments_configuration(configuration_id)


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

### Return type

void (empty response body)


## delete_webdeployments_deployment

>  delete_webdeployments_deployment(deployment_id)


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

### Return type

void (empty response body)


## delete_webdeployments_deployment_cobrowse_session_id

> object** delete_webdeployments_deployment_cobrowse_session_id(deployment_id, session_id)


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

### Return type

**object**


## delete_webdeployments_token_revoke

>  delete_webdeployments_token_revoke(x_journey_session_id=x_journey_session_id, x_journey_session_type=x_journey_session_type)


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

### Return type

void (empty response body)


## get_webdeployments_configuration_version

> [**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion) get_webdeployments_configuration_version(configuration_id, version_id)


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

### Return type

[**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion)


## get_webdeployments_configuration_versions

> [**WebDeploymentConfigurationVersionEntityListing**](WebDeploymentConfigurationVersionEntityListing) get_webdeployments_configuration_versions(configuration_id)


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

### Return type

[**WebDeploymentConfigurationVersionEntityListing**](WebDeploymentConfigurationVersionEntityListing)


## get_webdeployments_configuration_versions_draft

> [**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion) get_webdeployments_configuration_versions_draft(configuration_id)


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

### Return type

[**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion)


## get_webdeployments_configurations

> [**WebDeploymentConfigurationVersionEntityListing**](WebDeploymentConfigurationVersionEntityListing) get_webdeployments_configurations(show_only_published=show_only_published)


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
show_only_published = True # bool | Filter by published status. (optional)

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
| **show_only_published** | **bool**| Filter by published status. | [optional]  |

### Return type

[**WebDeploymentConfigurationVersionEntityListing**](WebDeploymentConfigurationVersionEntityListing)


## get_webdeployments_deployment

> [**WebDeployment**](WebDeployment) get_webdeployments_deployment(deployment_id, expand=expand)


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
expand = ['expand_example'] # list[str] | The specified entity attributes will be filled. Comma separated values expected.  (optional)

try:
    # Get a deployment
    api_response = api_instance.get_webdeployments_deployment(deployment_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->get_webdeployments_deployment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| The deployment ID |  |
| **expand** | [**list[str]**](str)| The specified entity attributes will be filled. Comma separated values expected.  | [optional] <br />**Values**: supportedContent, flowDetails |

### Return type

[**WebDeployment**](WebDeployment)


## get_webdeployments_deployment_cobrowse_session_id

> [**CobrowseWebMessagingSession**](CobrowseWebMessagingSession) get_webdeployments_deployment_cobrowse_session_id(deployment_id, session_id)


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

### Return type

[**CobrowseWebMessagingSession**](CobrowseWebMessagingSession)


## get_webdeployments_deployment_configurations

> [**WebDeploymentActiveConfigurationOnDeployment**](WebDeploymentActiveConfigurationOnDeployment) get_webdeployments_deployment_configurations(deployment_id, type=type, expand=expand)


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
expand = ['expand_example'] # list[str] | Expand instructions for the return value (optional)

try:
    # Get active configuration for a given deployment
    api_response = api_instance.get_webdeployments_deployment_configurations(deployment_id, type=type, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->get_webdeployments_deployment_configurations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| The deployment ID |  |
| **type** | **str**| Get active configuration on a deployment | [optional]  |
| **expand** | [**list[str]**](str)| Expand instructions for the return value | [optional] <br />**Values**: supportedContent |

### Return type

[**WebDeploymentActiveConfigurationOnDeployment**](WebDeploymentActiveConfigurationOnDeployment)


## get_webdeployments_deployment_identityresolution

> [**DeploymentIdentityResolutionConfig**](DeploymentIdentityResolutionConfig) get_webdeployments_deployment_identityresolution(deployment_id)


Get a deployment identity resolution setting.

Wraps GET /api/v2/webdeployments/deployments/{deploymentId}/identityresolution 

Requires ALL permissions: 

* webDeployments:deployment:view
* webDeployments:identityResolution:view

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
    # Get a deployment identity resolution setting.
    api_response = api_instance.get_webdeployments_deployment_identityresolution(deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->get_webdeployments_deployment_identityresolution: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| The deployment ID |  |

### Return type

[**DeploymentIdentityResolutionConfig**](DeploymentIdentityResolutionConfig)


## get_webdeployments_deployments

> [**ExpandableWebDeploymentEntityListing**](ExpandableWebDeploymentEntityListing) get_webdeployments_deployments(expand=expand)


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
expand = ['expand_example'] # list[str] | The specified entity attributes will be filled. Comma separated values expected.  (optional)

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
| **expand** | [**list[str]**](str)| The specified entity attributes will be filled. Comma separated values expected.  | [optional] <br />**Values**: Configuration, SupportedContent, identityresolution |

### Return type

[**ExpandableWebDeploymentEntityListing**](ExpandableWebDeploymentEntityListing)


## post_webdeployments_configuration_versions_draft_publish

> [**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion) post_webdeployments_configuration_versions_draft_publish(configuration_id)


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

### Return type

[**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion)


## post_webdeployments_configurations

> [**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion) post_webdeployments_configurations(configuration_version)


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
| **configuration_version** | [**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion)|  |  |

### Return type

[**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion)


## post_webdeployments_deployments

> [**WebDeployment**](WebDeployment) post_webdeployments_deployments(deployment)


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
| **deployment** | [**WebDeployment**](WebDeployment)|  |  |

### Return type

[**WebDeployment**](WebDeployment)


## post_webdeployments_token_oauthcodegrantjwtexchange

> [**WebDeploymentsAuthorizationResponse**](WebDeploymentsAuthorizationResponse) post_webdeployments_token_oauthcodegrantjwtexchange(body)


Exchange an oAuth code (obtained using the Authorization Code Flow or Implicit flow) for a JWT that can be used by webdeployments.

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
    # Exchange an oAuth code (obtained using the Authorization Code Flow or Implicit flow) for a JWT that can be used by webdeployments.
    api_response = api_instance.post_webdeployments_token_oauthcodegrantjwtexchange(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->post_webdeployments_token_oauthcodegrantjwtexchange: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WebDeploymentsOAuthExchangeRequest**](WebDeploymentsOAuthExchangeRequest)| webDeploymentsOAuthExchangeRequest |  |

### Return type

[**WebDeploymentsAuthorizationResponse**](WebDeploymentsAuthorizationResponse)


## post_webdeployments_token_refresh

> [**SignedData**](SignedData) post_webdeployments_token_refresh(body=body)


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
| **body** | [**WebDeploymentsRefreshJWTRequest**](WebDeploymentsRefreshJWTRequest)|  | [optional]  |

### Return type

[**SignedData**](SignedData)


## put_webdeployments_configuration_versions_draft

> [**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion) put_webdeployments_configuration_versions_draft(configuration_id, configuration_version)


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
| **configuration_version** | [**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion)|  |  |

### Return type

[**WebDeploymentConfigurationVersion**](WebDeploymentConfigurationVersion)


## put_webdeployments_deployment

> [**WebDeployment**](WebDeployment) put_webdeployments_deployment(deployment_id, deployment)


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
| **deployment** | [**WebDeployment**](WebDeployment)|  |  |

### Return type

[**WebDeployment**](WebDeployment)


## put_webdeployments_deployment_identityresolution

> [**DeploymentIdentityResolutionConfig**](DeploymentIdentityResolutionConfig) put_webdeployments_deployment_identityresolution(deployment_id, body)


Update identity resolution settings for a deployment.

Wraps PUT /api/v2/webdeployments/deployments/{deploymentId}/identityresolution 

Requires ALL permissions: 

* webDeployments:deployment:edit
* webDeployments:identityResolution:edit

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
body = PureCloudPlatformClientV2.DeploymentIdentityResolutionConfig() # DeploymentIdentityResolutionConfig | 

try:
    # Update identity resolution settings for a deployment.
    api_response = api_instance.put_webdeployments_deployment_identityresolution(deployment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebDeploymentsApi->put_webdeployments_deployment_identityresolution: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deployment_id** | **str**| The deployment ID |  |
| **body** | [**DeploymentIdentityResolutionConfig**](DeploymentIdentityResolutionConfig)|  |  |

### Return type

[**DeploymentIdentityResolutionConfig**](DeploymentIdentityResolutionConfig)


_PureCloudPlatformClientV2 246.1.0_

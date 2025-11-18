# OrganizationApi

## PureCloudPlatformClientV2.OrganizationApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_fieldconfig**](#get_fieldconfig) | Fetch field config for an entity type|
|[**get_organizations_authentication_settings**](#get_organizations_authentication_settings) | Gets the organization&#39;s settings|
|[**get_organizations_embeddedintegration**](#get_organizations_embeddedintegration) | Get the list of domains that will be allowed to embed PureCloud applications|
|[**get_organizations_ipaddressauthentication**](#get_organizations_ipaddressauthentication) | Get organization IP address whitelist settings|
|[**get_organizations_limits_changerequest**](#get_organizations_limits_changerequest) | Get a limit change request|
|[**get_organizations_limits_changerequests**](#get_organizations_limits_changerequests) | Get the available limit change requests|
|[**get_organizations_limits_docs**](#get_organizations_limits_docs) | Get limit documentation|
|[**get_organizations_limits_docs_freetrial**](#get_organizations_limits_docs_freetrial) | Get free trial limit documentation|
|[**get_organizations_limits_namespace**](#get_organizations_limits_namespace) | Get the effective limits in a namespace for an organization|
|[**get_organizations_limits_namespace_defaults**](#get_organizations_limits_namespace_defaults) | Get the default limits in a namespace for an organization|
|[**get_organizations_limits_namespaces**](#get_organizations_limits_namespaces) | Get the available limit namespaces|
|[**get_organizations_me**](#get_organizations_me) | Get organization.|
|[**get_organizations_whitelist**](#get_organizations_whitelist) | This route is deprecated, please use /api/v2/organizations/authentication/settings instead|
|[**patch_organizations_authentication_settings**](#patch_organizations_authentication_settings) | Update the organization&#39;s settings|
|[**patch_organizations_feature**](#patch_organizations_feature) | Update organization|
|[**put_organizations_embeddedintegration**](#put_organizations_embeddedintegration) | Update the list of domains that will be allowed to embed PureCloud applications|
|[**put_organizations_ipaddressauthentication**](#put_organizations_ipaddressauthentication) | Update organization IP address whitelist settings|
|[**put_organizations_me**](#put_organizations_me) | Update organization.|
|[**put_organizations_whitelist**](#put_organizations_whitelist) | This route is deprecated, please use /api/v2/organizations/authentication/settings instead|



## get_fieldconfig

> [**FieldConfig**](FieldConfig) get_fieldconfig(type)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Fetch field config for an entity type

Wraps GET /api/v2/fieldconfig 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()
type = 'type_example' # str | Field type

try:
    # Fetch field config for an entity type
    api_response = api_instance.get_fieldconfig(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_fieldconfig: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | **str**| Field type | <br />**Values**: person, group, org |

### Return type

[**FieldConfig**](FieldConfig)


## get_organizations_authentication_settings

> [**OrgAuthSettings**](OrgAuthSettings) get_organizations_authentication_settings()


Gets the organization's settings

Wraps GET /api/v2/organizations/authentication/settings 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()

try:
    # Gets the organization's settings
    api_response = api_instance.get_organizations_authentication_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organizations_authentication_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**OrgAuthSettings**](OrgAuthSettings)


## get_organizations_embeddedintegration

> [**EmbeddedIntegration**](EmbeddedIntegration) get_organizations_embeddedintegration()

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get the list of domains that will be allowed to embed PureCloud applications

This route is deprecated, please use /api/v2/organizations/authentication/settings instead

Wraps GET /api/v2/organizations/embeddedintegration 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()

try:
    # Get the list of domains that will be allowed to embed PureCloud applications
    api_response = api_instance.get_organizations_embeddedintegration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organizations_embeddedintegration: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**EmbeddedIntegration**](EmbeddedIntegration)


## get_organizations_ipaddressauthentication

> [**IpAddressAuthentication**](IpAddressAuthentication) get_organizations_ipaddressauthentication()

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get organization IP address whitelist settings

This route is deprecated, please use /api/v2/organizations/authentication/settings instead

Wraps GET /api/v2/organizations/ipaddressauthentication 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()

try:
    # Get organization IP address whitelist settings
    api_response = api_instance.get_organizations_ipaddressauthentication()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organizations_ipaddressauthentication: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**IpAddressAuthentication**](IpAddressAuthentication)


## get_organizations_limits_changerequest

> [**LimitChangeRequestDetails**](LimitChangeRequestDetails) get_organizations_limits_changerequest(request_id)


Get a limit change request

Wraps GET /api/v2/organizations/limits/changerequests/{requestId} 

Requires ANY permissions: 

* limits:organization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationApi()
request_id = 'request_id_example' # str | Unique id for the limit change request

try:
    # Get a limit change request
    api_response = api_instance.get_organizations_limits_changerequest(request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organizations_limits_changerequest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **request_id** | **str**| Unique id for the limit change request |  |

### Return type

[**LimitChangeRequestDetails**](LimitChangeRequestDetails)


## get_organizations_limits_changerequests

> [**LimitChangeRequestsEntityListing**](LimitChangeRequestsEntityListing) get_organizations_limits_changerequests(after=after, before=before, status=status, page_size=page_size, expand=expand)


Get the available limit change requests

Timestamp interval defaults to the last 365 days if both query parameters are omitted. If only one parameter is omitted, the interval will default to a 180 day range in the specified direction.

Wraps GET /api/v2/organizations/limits/changerequests 

Requires ANY permissions: 

* limits:organization:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationApi()
after = 56 # int | Timestamp indicating the date to begin after when searching for requests. (optional)
before = 56 # int | Timestamp indicating the date to end before when searching for requests. (optional)
status = 'status_example' # str | Status of the request to be filtered by (optional)
page_size = 25 # int | Page Size (optional) (default to 25)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get the available limit change requests
    api_response = api_instance.get_organizations_limits_changerequests(after=after, before=before, status=status, page_size=page_size, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organizations_limits_changerequests: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **after** | **int**| Timestamp indicating the date to begin after when searching for requests. | [optional]  |
| **before** | **int**| Timestamp indicating the date to end before when searching for requests. | [optional]  |
| **status** | **str**| Status of the request to be filtered by | [optional] <br />**Values**: Approved, Rejected, Rollback, Pending, Open, SecondaryApprovalNamespacesAdded, ReviewerApproved, ReviewerRejected, ReviewerRollback, ImplementingChange, ChangeImplemented, ImplementingRollback, RollbackImplemented |
| **page_size** | **int**| Page Size | [optional] [default to 25] |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand. | [optional] <br />**Values**: statusHistory |

### Return type

[**LimitChangeRequestsEntityListing**](LimitChangeRequestsEntityListing)


## get_organizations_limits_docs

> [**LimitDocumentation**](LimitDocumentation) get_organizations_limits_docs()


Get limit documentation

Wraps GET /api/v2/organizations/limits/docs 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()

try:
    # Get limit documentation
    api_response = api_instance.get_organizations_limits_docs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organizations_limits_docs: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**LimitDocumentation**](LimitDocumentation)


## get_organizations_limits_docs_freetrial

> [**FreeTrialLimitDocs**](FreeTrialLimitDocs) get_organizations_limits_docs_freetrial()


Get free trial limit documentation

Wraps GET /api/v2/organizations/limits/docs/freetrial 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()

try:
    # Get free trial limit documentation
    api_response = api_instance.get_organizations_limits_docs_freetrial()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organizations_limits_docs_freetrial: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**FreeTrialLimitDocs**](FreeTrialLimitDocs)


## get_organizations_limits_namespace

> [**LimitsEntityListing**](LimitsEntityListing) get_organizations_limits_namespace(namespace_name)


Get the effective limits in a namespace for an organization

Wraps GET /api/v2/organizations/limits/namespaces/{namespaceName} 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()
namespace_name = 'namespace_name_example' # str | The namespace to fetch limits for

try:
    # Get the effective limits in a namespace for an organization
    api_response = api_instance.get_organizations_limits_namespace(namespace_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organizations_limits_namespace: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **namespace_name** | **str**| The namespace to fetch limits for |  |

### Return type

[**LimitsEntityListing**](LimitsEntityListing)


## get_organizations_limits_namespace_defaults

> [**LimitsEntityListing**](LimitsEntityListing) get_organizations_limits_namespace_defaults(namespace_name)


Get the default limits in a namespace for an organization

Wraps GET /api/v2/organizations/limits/namespaces/{namespaceName}/defaults 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()
namespace_name = 'namespace_name_example' # str | The namespace to fetch defaults limits for

try:
    # Get the default limits in a namespace for an organization
    api_response = api_instance.get_organizations_limits_namespace_defaults(namespace_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organizations_limits_namespace_defaults: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **namespace_name** | **str**| The namespace to fetch defaults limits for |  |

### Return type

[**LimitsEntityListing**](LimitsEntityListing)


## get_organizations_limits_namespaces

> object** get_organizations_limits_namespaces(page_size=page_size, page_number=page_number)


Get the available limit namespaces

Wraps GET /api/v2/organizations/limits/namespaces 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()
page_size = 100 # int | Page size (optional) (default to 100)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get the available limit namespaces
    api_response = api_instance.get_organizations_limits_namespaces(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organizations_limits_namespaces: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 100] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

**object**


## get_organizations_me

> [**Organization**](Organization) get_organizations_me()


Get organization.

Wraps GET /api/v2/organizations/me 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()

try:
    # Get organization.
    api_response = api_instance.get_organizations_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organizations_me: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**Organization**](Organization)


## get_organizations_whitelist

> [**OrgWhitelistSettings**](OrgWhitelistSettings) get_organizations_whitelist()

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

This route is deprecated, please use /api/v2/organizations/authentication/settings instead

Wraps GET /api/v2/organizations/whitelist 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()

try:
    # This route is deprecated, please use /api/v2/organizations/authentication/settings instead
    api_response = api_instance.get_organizations_whitelist()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organizations_whitelist: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**OrgWhitelistSettings**](OrgWhitelistSettings)


## patch_organizations_authentication_settings

> [**OrgAuthSettings**](OrgAuthSettings) patch_organizations_authentication_settings(body)


Update the organization's settings

Wraps PATCH /api/v2/organizations/authentication/settings 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()
body = PureCloudPlatformClientV2.OrgAuthSettings() # OrgAuthSettings | Org settings

try:
    # Update the organization's settings
    api_response = api_instance.patch_organizations_authentication_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->patch_organizations_authentication_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OrgAuthSettings**](OrgAuthSettings)| Org settings |  |

### Return type

[**OrgAuthSettings**](OrgAuthSettings)


## patch_organizations_feature

> [**OrganizationFeatures**](OrganizationFeatures) patch_organizations_feature(feature_name, enabled)


Update organization

Wraps PATCH /api/v2/organizations/features/{featureName} 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()
feature_name = 'feature_name_example' # str | Organization feature
enabled = PureCloudPlatformClientV2.FeatureState() # FeatureState | New state of feature

try:
    # Update organization
    api_response = api_instance.patch_organizations_feature(feature_name, enabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->patch_organizations_feature: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **feature_name** | **str**| Organization feature | <br />**Values**: realtimeCIC, purecloud, hipaa, ucEnabled, pci, purecloudVoice, xmppFederation, chat, informalPhotos, directory, contactCenter, unifiedCommunications, custserv |
| **enabled** | [**FeatureState**](FeatureState)| New state of feature |  |

### Return type

[**OrganizationFeatures**](OrganizationFeatures)


## put_organizations_embeddedintegration

> [**EmbeddedIntegration**](EmbeddedIntegration) put_organizations_embeddedintegration(body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Update the list of domains that will be allowed to embed PureCloud applications

This route is deprecated, please use /api/v2/organizations/authentication/settings instead

Wraps PUT /api/v2/organizations/embeddedintegration 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()
body = PureCloudPlatformClientV2.EmbeddedIntegration() # EmbeddedIntegration | Whitelist settings

try:
    # Update the list of domains that will be allowed to embed PureCloud applications
    api_response = api_instance.put_organizations_embeddedintegration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->put_organizations_embeddedintegration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EmbeddedIntegration**](EmbeddedIntegration)| Whitelist settings |  |

### Return type

[**EmbeddedIntegration**](EmbeddedIntegration)


## put_organizations_ipaddressauthentication

> [**IpAddressAuthentication**](IpAddressAuthentication) put_organizations_ipaddressauthentication(body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Update organization IP address whitelist settings

This route is deprecated, please use /api/v2/organizations/authentication/settings instead

Wraps PUT /api/v2/organizations/ipaddressauthentication 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()
body = PureCloudPlatformClientV2.IpAddressAuthentication() # IpAddressAuthentication | IP address Whitelist settings

try:
    # Update organization IP address whitelist settings
    api_response = api_instance.put_organizations_ipaddressauthentication(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->put_organizations_ipaddressauthentication: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**IpAddressAuthentication**](IpAddressAuthentication)| IP address Whitelist settings |  |

### Return type

[**IpAddressAuthentication**](IpAddressAuthentication)


## put_organizations_me

> [**Organization**](Organization) put_organizations_me(body=body)


Update organization.

Wraps PUT /api/v2/organizations/me 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()
body = PureCloudPlatformClientV2.Organization() # Organization | Organization (optional)

try:
    # Update organization.
    api_response = api_instance.put_organizations_me(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->put_organizations_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Organization**](Organization)| Organization | [optional]  |

### Return type

[**Organization**](Organization)


## put_organizations_whitelist

> [**OrgWhitelistSettings**](OrgWhitelistSettings) put_organizations_whitelist(body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

This route is deprecated, please use /api/v2/organizations/authentication/settings instead

Wraps PUT /api/v2/organizations/whitelist 

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
api_instance = PureCloudPlatformClientV2.OrganizationApi()
body = PureCloudPlatformClientV2.OrgWhitelistSettings() # OrgWhitelistSettings | Whitelist settings

try:
    # This route is deprecated, please use /api/v2/organizations/authentication/settings instead
    api_response = api_instance.put_organizations_whitelist(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->put_organizations_whitelist: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OrgWhitelistSettings**](OrgWhitelistSettings)| Whitelist settings |  |

### Return type

[**OrgWhitelistSettings**](OrgWhitelistSettings)


_PureCloudPlatformClientV2 243.0.0_

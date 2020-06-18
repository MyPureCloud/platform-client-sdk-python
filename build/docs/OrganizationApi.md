---
title: OrganizationApi
---

## PureCloudPlatformClientV2.OrganizationApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_fieldconfig**](OrganizationApi.html#get_fieldconfig) | Fetch field config for an entity type|
|[**get_organizations_embeddedintegration**](OrganizationApi.html#get_organizations_embeddedintegration) | Get the list of domains that will be allowed to embed PureCloud applications|
|[**get_organizations_ipaddressauthentication**](OrganizationApi.html#get_organizations_ipaddressauthentication) | Get organization IP address whitelist settings|
|[**get_organizations_me**](OrganizationApi.html#get_organizations_me) | Get organization.|
|[**get_organizations_whitelist**](OrganizationApi.html#get_organizations_whitelist) | Use PUT /api/v2/organizations/embeddedintegration instead|
|[**patch_organizations_feature**](OrganizationApi.html#patch_organizations_feature) | Update organization|
|[**put_organizations_embeddedintegration**](OrganizationApi.html#put_organizations_embeddedintegration) | Update the list of domains that will be allowed to embed PureCloud applications|
|[**put_organizations_ipaddressauthentication**](OrganizationApi.html#put_organizations_ipaddressauthentication) | Update organization IP address whitelist settings|
|[**put_organizations_me**](OrganizationApi.html#put_organizations_me) | Update organization.|
|[**put_organizations_whitelist**](OrganizationApi.html#put_organizations_whitelist) | Use PUT /api/v2/organizations/embeddedintegration instead|
{: class="table table-striped"}

<a name="get_fieldconfig"></a>

## [**FieldConfig**](FieldConfig.html) get_fieldconfig(type)



Fetch field config for an entity type



Wraps GET /api/v2/fieldconfig 

Requires NO permissions: 


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
    print "Exception when calling OrganizationApi->get_fieldconfig: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | **str**| Field type | <br />**Values**: person, group, org, externalContact |
{: class="table table-striped"}

### Return type

[**FieldConfig**](FieldConfig.html)

<a name="get_organizations_embeddedintegration"></a>

## [**EmbeddedIntegration**](EmbeddedIntegration.html) get_organizations_embeddedintegration()



Get the list of domains that will be allowed to embed PureCloud applications



Wraps GET /api/v2/organizations/embeddedintegration 

Requires NO permissions: 


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
    print "Exception when calling OrganizationApi->get_organizations_embeddedintegration: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**EmbeddedIntegration**](EmbeddedIntegration.html)

<a name="get_organizations_ipaddressauthentication"></a>

## [**IpAddressAuthentication**](IpAddressAuthentication.html) get_organizations_ipaddressauthentication()



Get organization IP address whitelist settings



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
    print "Exception when calling OrganizationApi->get_organizations_ipaddressauthentication: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**IpAddressAuthentication**](IpAddressAuthentication.html)

<a name="get_organizations_me"></a>

## [**Organization**](Organization.html) get_organizations_me()



Get organization.



Wraps GET /api/v2/organizations/me 

Requires NO permissions: 


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
    print "Exception when calling OrganizationApi->get_organizations_me: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Organization**](Organization.html)

<a name="get_organizations_whitelist"></a>

## [**OrgWhitelistSettings**](OrgWhitelistSettings.html) get_organizations_whitelist()

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Use PUT /api/v2/organizations/embeddedintegration instead



Wraps GET /api/v2/organizations/whitelist 

Requires NO permissions: 


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
    # Use PUT /api/v2/organizations/embeddedintegration instead
    api_response = api_instance.get_organizations_whitelist()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrganizationApi->get_organizations_whitelist: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**OrgWhitelistSettings**](OrgWhitelistSettings.html)

<a name="patch_organizations_feature"></a>

## [**OrganizationFeatures**](OrganizationFeatures.html) patch_organizations_feature(feature_name, enabled)



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
    print "Exception when calling OrganizationApi->patch_organizations_feature: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **feature_name** | **str**| Organization feature | <br />**Values**: realtimeCIC, purecloud, hipaa, ucEnabled, pci, purecloudVoice, xmppFederation, chat, informalPhotos, directory, contactCenter, unifiedCommunications, custserv |
| **enabled** | [**FeatureState**](FeatureState.html)| New state of feature |  |
{: class="table table-striped"}

### Return type

[**OrganizationFeatures**](OrganizationFeatures.html)

<a name="put_organizations_embeddedintegration"></a>

## [**EmbeddedIntegration**](EmbeddedIntegration.html) put_organizations_embeddedintegration(body)



Update the list of domains that will be allowed to embed PureCloud applications



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
    print "Exception when calling OrganizationApi->put_organizations_embeddedintegration: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EmbeddedIntegration**](EmbeddedIntegration.html)| Whitelist settings |  |
{: class="table table-striped"}

### Return type

[**EmbeddedIntegration**](EmbeddedIntegration.html)

<a name="put_organizations_ipaddressauthentication"></a>

## [**IpAddressAuthentication**](IpAddressAuthentication.html) put_organizations_ipaddressauthentication(body)



Update organization IP address whitelist settings



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
    print "Exception when calling OrganizationApi->put_organizations_ipaddressauthentication: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**IpAddressAuthentication**](IpAddressAuthentication.html)| IP address Whitelist settings |  |
{: class="table table-striped"}

### Return type

[**IpAddressAuthentication**](IpAddressAuthentication.html)

<a name="put_organizations_me"></a>

## [**Organization**](Organization.html) put_organizations_me(body=body)



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
    print "Exception when calling OrganizationApi->put_organizations_me: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Organization**](Organization.html)| Organization | [optional]  |
{: class="table table-striped"}

### Return type

[**Organization**](Organization.html)

<a name="put_organizations_whitelist"></a>

## [**OrgWhitelistSettings**](OrgWhitelistSettings.html) put_organizations_whitelist(body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Use PUT /api/v2/organizations/embeddedintegration instead



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
    # Use PUT /api/v2/organizations/embeddedintegration instead
    api_response = api_instance.put_organizations_whitelist(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrganizationApi->put_organizations_whitelist: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OrgWhitelistSettings**](OrgWhitelistSettings.html)| Whitelist settings |  |
{: class="table table-striped"}

### Return type

[**OrgWhitelistSettings**](OrgWhitelistSettings.html)


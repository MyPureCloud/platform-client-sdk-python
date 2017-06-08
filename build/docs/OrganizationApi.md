---
title: OrganizationApi
---

## PureCloudPlatformClientV2.OrganizationApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_fieldconfig**](OrganizationApi.html#get_fieldconfig) | Fetch field config for an entity type|
|[**get_organizations_me**](OrganizationApi.html#get_organizations_me) | Get organization.|
|[**patch_organizations_feature**](OrganizationApi.html#patch_organizations_feature) | Update organization|
|[**put_organizations_me**](OrganizationApi.html#put_organizations_me) | Update organization.|
{: class="table table-striped"}

<a name="get_fieldconfig"></a>

## [**FieldConfig**](FieldConfig.html) get_fieldconfig(type)

Fetch field config for an entity type



Wraps GET /api/v2/fieldconfig 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | **str**| Field type | <br />**Values**: person, group, org, externalContact |
{: class="table table-striped"}

### Return type

[**FieldConfig**](FieldConfig.html)

<a name="get_organizations_me"></a>

## [**Organization**](Organization.html) get_organizations_me()

Get organization.



Wraps GET /api/v2/organizations/me 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationApi()

try:
    # Get organization.
    api_response = api_instance.get_organizations_me()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrganizationApi->get_organizations_me: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Organization**](Organization.html)

<a name="patch_organizations_feature"></a>

## [**OrganizationFeatures**](OrganizationFeatures.html) patch_organizations_feature(feature_name, enabled)

Update organization



Wraps PATCH /api/v2/organizations/features/{featureName} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **feature_name** | **str**| Organization feature | <br />**Values**: realtimeCIC, purecloud, hipaa, ucEnabled, pci, purecloudVoice, xmppFederation, chat, informalPhotos, directory, contactCenter, unifiedCommunications, custserv |
| **enabled** | [**FeatureState**](FeatureState.html)| New state of feature |  |
{: class="table table-striped"}

### Return type

[**OrganizationFeatures**](OrganizationFeatures.html)

<a name="put_organizations_me"></a>

## [**Organization**](Organization.html) put_organizations_me(body=body)

Update organization.



Wraps PUT /api/v2/organizations/me 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Organization**](Organization.html)| Organization | [optional]  |
{: class="table table-striped"}

### Return type

[**Organization**](Organization.html)


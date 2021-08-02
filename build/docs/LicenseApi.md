---
title: LicenseApi
---

## PureCloudPlatformClientV2.LicenseApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_license_definition**](LicenseApi.html#get_license_definition) | Get PureCloud license definition.|
|[**get_license_definitions**](LicenseApi.html#get_license_definitions) | Get all PureCloud license definitions available for the organization.|
|[**get_license_toggle**](LicenseApi.html#get_license_toggle) | Get PureCloud license feature toggle value.|
|[**get_license_user**](LicenseApi.html#get_license_user) | Get licenses for specified user.|
|[**get_license_users**](LicenseApi.html#get_license_users) | Get a page of users and their licenses|
|[**post_license_infer**](LicenseApi.html#post_license_infer) | Get a list of licenses inferred based on a list of roleIds|
|[**post_license_organization**](LicenseApi.html#post_license_organization) | Update the organization&#39;s license assignments in a batch.|
|[**post_license_toggle**](LicenseApi.html#post_license_toggle) | Switch PureCloud license feature toggle value.|
|[**post_license_users**](LicenseApi.html#post_license_users) | Fetch user licenses in a batch.|
{: class="table table-striped"}

<a name="get_license_definition"></a>

## [**LicenseDefinition**](LicenseDefinition.html) get_license_definition(license_id)



Get PureCloud license definition.



Wraps GET /api/v2/license/definitions/{licenseId} 

Requires ANY permissions: 

* authorization:grant:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LicenseApi()
license_id = 'license_id_example' # str | ID

try:
    # Get PureCloud license definition.
    api_response = api_instance.get_license_definition(license_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_definition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **license_id** | **str**| ID |  |
{: class="table table-striped"}

### Return type

[**LicenseDefinition**](LicenseDefinition.html)

<a name="get_license_definitions"></a>

## [**list[LicenseDefinition]**](LicenseDefinition.html) get_license_definitions()



Get all PureCloud license definitions available for the organization.



Wraps GET /api/v2/license/definitions 

Requires ANY permissions: 

* authorization:grant:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LicenseApi()

try:
    # Get all PureCloud license definitions available for the organization.
    api_response = api_instance.get_license_definitions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_definitions: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**list[LicenseDefinition]**](LicenseDefinition.html)

<a name="get_license_toggle"></a>

## [**LicenseOrgToggle**](LicenseOrgToggle.html) get_license_toggle(feature_name)



Get PureCloud license feature toggle value.



Wraps GET /api/v2/license/toggles/{featureName} 

Requires ANY permissions: 

* authorization:grant:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LicenseApi()
feature_name = 'feature_name_example' # str | featureName

try:
    # Get PureCloud license feature toggle value.
    api_response = api_instance.get_license_toggle(feature_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_toggle: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **feature_name** | **str**| featureName |  |
{: class="table table-striped"}

### Return type

[**LicenseOrgToggle**](LicenseOrgToggle.html)

<a name="get_license_user"></a>

## [**LicenseUser**](LicenseUser.html) get_license_user(user_id)



Get licenses for specified user.



Wraps GET /api/v2/license/users/{userId} 

Requires ANY permissions: 

* authorization:grant:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LicenseApi()
user_id = 'user_id_example' # str | ID

try:
    # Get licenses for specified user.
    api_response = api_instance.get_license_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| ID |  |
{: class="table table-striped"}

### Return type

[**LicenseUser**](LicenseUser.html)

<a name="get_license_users"></a>

## [**UserLicensesEntityListing**](UserLicensesEntityListing.html) get_license_users(page_size=page_size, page_number=page_number)



Get a page of users and their licenses

Retrieve a page of users in an organization along with the licenses they possess.

Wraps GET /api/v2/license/users 

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
api_instance = PureCloudPlatformClientV2.LicenseApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a page of users and their licenses
    api_response = api_instance.get_license_users(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**UserLicensesEntityListing**](UserLicensesEntityListing.html)

<a name="post_license_infer"></a>

## list[str]** post_license_infer(body=body)



Get a list of licenses inferred based on a list of roleIds



Wraps POST /api/v2/license/infer 

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
api_instance = PureCloudPlatformClientV2.LicenseApi()
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | The roleIds to use while inferring licenses (optional)

try:
    # Get a list of licenses inferred based on a list of roleIds
    api_response = api_instance.post_license_infer(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->post_license_infer: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | **list[str]**| The roleIds to use while inferring licenses | [optional]  |
{: class="table table-striped"}

### Return type

**list[str]**

<a name="post_license_organization"></a>

## [**list[LicenseUpdateStatus]**](LicenseUpdateStatus.html) post_license_organization(body=body)



Update the organization's license assignments in a batch.



Wraps POST /api/v2/license/organization 

Requires ANY permissions: 

* authorization:grant:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LicenseApi()
body = PureCloudPlatformClientV2.LicenseBatchAssignmentRequest() # LicenseBatchAssignmentRequest | The license assignments to update. (optional)

try:
    # Update the organization's license assignments in a batch.
    api_response = api_instance.post_license_organization(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->post_license_organization: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LicenseBatchAssignmentRequest**](LicenseBatchAssignmentRequest.html)| The license assignments to update. | [optional]  |
{: class="table table-striped"}

### Return type

[**list[LicenseUpdateStatus]**](LicenseUpdateStatus.html)

<a name="post_license_toggle"></a>

## [**LicenseOrgToggle**](LicenseOrgToggle.html) post_license_toggle(feature_name)



Switch PureCloud license feature toggle value.



Wraps POST /api/v2/license/toggles/{featureName} 

Requires ANY permissions: 

* authorization:grant:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LicenseApi()
feature_name = 'feature_name_example' # str | featureName

try:
    # Switch PureCloud license feature toggle value.
    api_response = api_instance.post_license_toggle(feature_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->post_license_toggle: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **feature_name** | **str**| featureName |  |
{: class="table table-striped"}

### Return type

[**LicenseOrgToggle**](LicenseOrgToggle.html)

<a name="post_license_users"></a>

## [**dict(str, object)**](dict.html) post_license_users(body=body)



Fetch user licenses in a batch.



Wraps POST /api/v2/license/users 

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
api_instance = PureCloudPlatformClientV2.LicenseApi()
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | The user IDs to fetch. (optional)

try:
    # Fetch user licenses in a batch.
    api_response = api_instance.post_license_users(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->post_license_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | **list[str]**| The user IDs to fetch. | [optional]  |
{: class="table table-striped"}

### Return type

[**dict(str, object)**](dict.html)


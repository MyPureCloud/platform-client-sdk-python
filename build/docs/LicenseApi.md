# LicenseApi

## PureCloudPlatformClientV2.LicenseApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_license_definition**](#get_license_definition) | Get PureCloud license definition.|
|[**get_license_definitions**](#get_license_definitions) | Get all PureCloud license definitions available for the organization.|
|[**get_license_toggle**](#get_license_toggle) | Deprecated - no alternative required. This operation will always return &#39;true&#39; for requested toggles|
|[**get_license_user**](#get_license_user) | Get licenses for specified user.|
|[**get_license_users**](#get_license_users) | Get a page of users and their licenses|
|[**post_license_infer**](#post_license_infer) | Get a list of licenses inferred based on a list of roleIds|
|[**post_license_organization**](#post_license_organization) | Update the organization&#39;s license assignments in a batch.|
|[**post_license_toggle**](#post_license_toggle) | Deprecated. No alternative required - this endpoint has no effect|
|[**post_license_users**](#post_license_users) | Fetch user licenses in a batch.|



## get_license_definition

> [**LicenseDefinition**](LicenseDefinition) get_license_definition(license_id)


Get PureCloud license definition.

Wraps GET /api/v2/license/definitions/{licenseId} 

Requires ANY permissions: 

* authorization:grant:add
* authorization:license:view

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

### Return type

[**LicenseDefinition**](LicenseDefinition)


## get_license_definitions

> [**list[LicenseDefinition]**](LicenseDefinition) get_license_definitions()


Get all PureCloud license definitions available for the organization.

Wraps GET /api/v2/license/definitions 

Requires ANY permissions: 

* authorization:grant:add
* authorization:license:view

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

[**list[LicenseDefinition]**](LicenseDefinition)


## get_license_toggle

> [**LicenseOrgToggle**](LicenseOrgToggle) get_license_toggle(feature_name)


Deprecated - no alternative required. This operation will always return 'true' for requested toggles

Wraps GET /api/v2/license/toggles/{featureName} 

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
api_instance = PureCloudPlatformClientV2.LicenseApi()
feature_name = 'feature_name_example' # str | featureName

try:
    # Deprecated - no alternative required. This operation will always return 'true' for requested toggles
    api_response = api_instance.get_license_toggle(feature_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_toggle: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **feature_name** | **str**| featureName |  |

### Return type

[**LicenseOrgToggle**](LicenseOrgToggle)


## get_license_user

> [**LicenseUser**](LicenseUser) get_license_user(user_id)


Get licenses for specified user.

Wraps GET /api/v2/license/users/{userId} 

Requires ANY permissions: 

* authorization:grant:add
* authorization:license:view

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

### Return type

[**LicenseUser**](LicenseUser)


## get_license_users

> [**UserLicensesEntityListing**](UserLicensesEntityListing) get_license_users(page_size=page_size, page_number=page_number)


Get a page of users and their licenses

Retrieve a page of users in an organization along with the licenses they possess.

Wraps GET /api/v2/license/users 

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

### Return type

[**UserLicensesEntityListing**](UserLicensesEntityListing)


## post_license_infer

> list[str]** post_license_infer(body=body)


Get a list of licenses inferred based on a list of roleIds

Wraps POST /api/v2/license/infer 

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
api_instance = PureCloudPlatformClientV2.LicenseApi()
body = ['body_example'] # list[str] | The roleIds to use while inferring licenses (optional)

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
| **body** | [**list[str]**](str)| The roleIds to use while inferring licenses | [optional]  |

### Return type

**list[str]**


## post_license_organization

> [**list[LicenseUpdateStatus]**](LicenseUpdateStatus) post_license_organization(body=body)


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
| **body** | [**LicenseBatchAssignmentRequest**](LicenseBatchAssignmentRequest)| The license assignments to update. | [optional]  |

### Return type

[**list[LicenseUpdateStatus]**](LicenseUpdateStatus)


## post_license_toggle

> [**LicenseOrgToggle**](LicenseOrgToggle) post_license_toggle(feature_name)


Deprecated. No alternative required - this endpoint has no effect

Wraps POST /api/v2/license/toggles/{featureName} 

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
api_instance = PureCloudPlatformClientV2.LicenseApi()
feature_name = 'feature_name_example' # str | featureName

try:
    # Deprecated. No alternative required - this endpoint has no effect
    api_response = api_instance.post_license_toggle(feature_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->post_license_toggle: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **feature_name** | **str**| featureName |  |

### Return type

[**LicenseOrgToggle**](LicenseOrgToggle)


## post_license_users

> dict(str, object)** post_license_users(body=body)


Fetch user licenses in a batch.

Wraps POST /api/v2/license/users 

Requires ANY permissions: 

* authorization:grant:add
* authorization:license:view

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
body = ['body_example'] # list[str] | The user IDs to fetch. (optional)

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
| **body** | [**list[str]**](str)| The user IDs to fetch. | [optional]  |

### Return type

**dict(str, object)**


_PureCloudPlatformClientV2 238.0.0_

# OrganizationAuthorizationApi

## PureCloudPlatformClientV2.OrganizationAuthorizationApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_orgauthorization_trustee**](#delete_orgauthorization_trustee) | Delete Org Trust|
|[**delete_orgauthorization_trustee_cloneduser**](#delete_orgauthorization_trustee_cloneduser) | Deletes cloned user|
|[**delete_orgauthorization_trustee_group**](#delete_orgauthorization_trustee_group) | Delete Trustee Group|
|[**delete_orgauthorization_trustee_group_roles**](#delete_orgauthorization_trustee_group_roles) | Delete Trustee Group Roles|
|[**delete_orgauthorization_trustee_user**](#delete_orgauthorization_trustee_user) | Delete Trustee User|
|[**delete_orgauthorization_trustee_user_roles**](#delete_orgauthorization_trustee_user_roles) | Delete Trustee User Roles|
|[**delete_orgauthorization_trustees**](#delete_orgauthorization_trustees) | Delete Bulk Org Trustees|
|[**delete_orgauthorization_trustor**](#delete_orgauthorization_trustor) | Delete Org Trust|
|[**delete_orgauthorization_trustor_cloneduser**](#delete_orgauthorization_trustor_cloneduser) | Delete Cloned User|
|[**delete_orgauthorization_trustor_group**](#delete_orgauthorization_trustor_group) | Delete Trustee Group|
|[**delete_orgauthorization_trustor_user**](#delete_orgauthorization_trustor_user) | Delete Trustee User|
|[**delete_orgauthorization_trustors**](#delete_orgauthorization_trustors) | Delete Bulk Org Trustors|
|[**get_orgauthorization_pairing**](#get_orgauthorization_pairing) | Get Pairing Info|
|[**get_orgauthorization_trustee**](#get_orgauthorization_trustee) | Get Org Trust|
|[**get_orgauthorization_trustee_clonedusers**](#get_orgauthorization_trustee_clonedusers) | The list of cloned users from the trustee organization (i.e. users with a native user record).|
|[**get_orgauthorization_trustee_group**](#get_orgauthorization_trustee_group) | Get Trustee Group|
|[**get_orgauthorization_trustee_group_roles**](#get_orgauthorization_trustee_group_roles) | Get Trustee Group Roles|
|[**get_orgauthorization_trustee_groups**](#get_orgauthorization_trustee_groups) | The list of trustee groups for this organization (i.e. groups granted access to this organization).|
|[**get_orgauthorization_trustee_user**](#get_orgauthorization_trustee_user) | Get Trustee User|
|[**get_orgauthorization_trustee_user_roles**](#get_orgauthorization_trustee_user_roles) | Get Trustee User Roles|
|[**get_orgauthorization_trustee_users**](#get_orgauthorization_trustee_users) | The list of trustee users for this organization (i.e. users granted access to this organization).|
|[**get_orgauthorization_trustees**](#get_orgauthorization_trustees) | The list of trustees for this organization (i.e. organizations granted access to this organization).|
|[**get_orgauthorization_trustees_care**](#get_orgauthorization_trustees_care) | Get Customer Care organization ids.|
|[**get_orgauthorization_trustees_default**](#get_orgauthorization_trustees_default) | Get organization authorization trust with Customer Care, if one exists.|
|[**get_orgauthorization_trustor**](#get_orgauthorization_trustor) | Get Org Trust|
|[**get_orgauthorization_trustor_cloneduser**](#get_orgauthorization_trustor_cloneduser) | Get Cloned User|
|[**get_orgauthorization_trustor_clonedusers**](#get_orgauthorization_trustor_clonedusers) | The list of cloned users in the trustor organization (i.e. users with a native user record).|
|[**get_orgauthorization_trustor_group**](#get_orgauthorization_trustor_group) | Get Trustee Group|
|[**get_orgauthorization_trustor_groups**](#get_orgauthorization_trustor_groups) | The list of groups in the trustor organization (i.e. groups granted access).|
|[**get_orgauthorization_trustor_user**](#get_orgauthorization_trustor_user) | Get Trustee User|
|[**get_orgauthorization_trustor_users**](#get_orgauthorization_trustor_users) | The list of users in the trustor organization (i.e. users granted access).|
|[**get_orgauthorization_trustors**](#get_orgauthorization_trustors) | The list of organizations that have authorized/trusted your organization.|
|[**post_orgauthorization_pairings**](#post_orgauthorization_pairings) | A pairing id is created by the trustee and given to the trustor to create a trust.|
|[**post_orgauthorization_trustee_groups**](#post_orgauthorization_trustee_groups) | Add a group to the trust.|
|[**post_orgauthorization_trustee_users**](#post_orgauthorization_trustee_users) | Add a user to the trust.|
|[**post_orgauthorization_trustees**](#post_orgauthorization_trustees) | Create a new organization authorization trust. This is required to grant other organizations access to your organization.|
|[**post_orgauthorization_trustees_audits**](#post_orgauthorization_trustees_audits) | Get Org Trustee Audits|
|[**post_orgauthorization_trustees_care**](#post_orgauthorization_trustees_care) | Create a new organization authorization trust with Customer Care. This is required to grant your regional Customer Care organization access to your organization.|
|[**post_orgauthorization_trustees_default**](#post_orgauthorization_trustees_default) | Create a new organization authorization trust with Customer Care. This is required to grant your regional Customer Care organization access to your organization.|
|[**post_orgauthorization_trustor_audits**](#post_orgauthorization_trustor_audits) | Get Org Trustor Audits|
|[**put_orgauthorization_trustee**](#put_orgauthorization_trustee) | Update Org Trust|
|[**put_orgauthorization_trustee_group_roledivisions**](#put_orgauthorization_trustee_group_roledivisions) | Update Trustee Group Roles|
|[**put_orgauthorization_trustee_group_roles**](#put_orgauthorization_trustee_group_roles) | Update Trustee Group Roles|
|[**put_orgauthorization_trustee_user_roledivisions**](#put_orgauthorization_trustee_user_roledivisions) | Update Trustee User Roles|
|[**put_orgauthorization_trustee_user_roles**](#put_orgauthorization_trustee_user_roles) | Update Trustee User Roles|
|[**put_orgauthorization_trustor_cloneduser**](#put_orgauthorization_trustor_cloneduser) | Creates a clone of the trustee user in the trustor org.|
|[**put_orgauthorization_trustor_group**](#put_orgauthorization_trustor_group) | Add a Trustee Group to the trust.|
|[**put_orgauthorization_trustor_user**](#put_orgauthorization_trustor_user) | Add a Trustee user to the trust.|



## delete_orgauthorization_trustee

>  delete_orgauthorization_trustee(trustee_org_id)


Delete Org Trust

Wraps DELETE /api/v2/orgauthorization/trustees/{trusteeOrgId} 

Requires ANY permissions: 

* authorization:orgTrustee:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id

try:
    # Delete Org Trust
    api_instance.delete_orgauthorization_trustee(trustee_org_id)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustee: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |

### Return type

void (empty response body)


## delete_orgauthorization_trustee_cloneduser

>  delete_orgauthorization_trustee_cloneduser(trustee_org_id, trustee_user_id)


Deletes cloned user

Wraps DELETE /api/v2/orgauthorization/trustees/{trusteeOrgId}/clonedusers/{trusteeUserId} 

Requires ANY permissions: 

* directory:user:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
trustee_user_id = 'trustee_user_id_example' # str | Id of the cloned user to delete

try:
    # Deletes cloned user
    api_instance.delete_orgauthorization_trustee_cloneduser(trustee_org_id, trustee_user_id)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustee_cloneduser: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_user_id** | **str**| Id of the cloned user to delete |  |

### Return type

void (empty response body)


## delete_orgauthorization_trustee_group

>  delete_orgauthorization_trustee_group(trustee_org_id, trustee_group_id)


Delete Trustee Group

Wraps DELETE /api/v2/orgauthorization/trustees/{trusteeOrgId}/groups/{trusteeGroupId} 

Requires ANY permissions: 

* authorization:orgTrusteeGroup:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
trustee_group_id = 'trustee_group_id_example' # str | Trustee Group Id

try:
    # Delete Trustee Group
    api_instance.delete_orgauthorization_trustee_group(trustee_org_id, trustee_group_id)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustee_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_group_id** | **str**| Trustee Group Id |  |

### Return type

void (empty response body)


## delete_orgauthorization_trustee_group_roles

>  delete_orgauthorization_trustee_group_roles(trustee_org_id, trustee_group_id)


Delete Trustee Group Roles

Wraps DELETE /api/v2/orgauthorization/trustees/{trusteeOrgId}/groups/{trusteeGroupId}/roles 

Requires ANY permissions: 

* authorization:orgTrusteeGroup:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
trustee_group_id = 'trustee_group_id_example' # str | Trustee Group Id

try:
    # Delete Trustee Group Roles
    api_instance.delete_orgauthorization_trustee_group_roles(trustee_org_id, trustee_group_id)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustee_group_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_group_id** | **str**| Trustee Group Id |  |

### Return type

void (empty response body)


## delete_orgauthorization_trustee_user

>  delete_orgauthorization_trustee_user(trustee_org_id, trustee_user_id)


Delete Trustee User

Wraps DELETE /api/v2/orgauthorization/trustees/{trusteeOrgId}/users/{trusteeUserId} 

Requires ANY permissions: 

* authorization:orgTrusteeUser:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
trustee_user_id = 'trustee_user_id_example' # str | Trustee User Id

try:
    # Delete Trustee User
    api_instance.delete_orgauthorization_trustee_user(trustee_org_id, trustee_user_id)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustee_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |

### Return type

void (empty response body)


## delete_orgauthorization_trustee_user_roles

>  delete_orgauthorization_trustee_user_roles(trustee_org_id, trustee_user_id)


Delete Trustee User Roles

Wraps DELETE /api/v2/orgauthorization/trustees/{trusteeOrgId}/users/{trusteeUserId}/roles 

Requires ANY permissions: 

* authorization:orgTrusteeUser:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
trustee_user_id = 'trustee_user_id_example' # str | Trustee User Id

try:
    # Delete Trustee User Roles
    api_instance.delete_orgauthorization_trustee_user_roles(trustee_org_id, trustee_user_id)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustee_user_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |

### Return type

void (empty response body)


## delete_orgauthorization_trustees

>  delete_orgauthorization_trustees(id)


Delete Bulk Org Trustees

delete_orgauthorization_trustees is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/orgauthorization/trustees 

Requires ANY permissions: 

* authorization:orgTrustee:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
id = ['id_example'] # list[str] | Comma separated list of trustee ids to remove

try:
    # Delete Bulk Org Trustees
    api_instance.delete_orgauthorization_trustees(id)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustees: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str)| Comma separated list of trustee ids to remove |  |

### Return type

void (empty response body)


## delete_orgauthorization_trustor

>  delete_orgauthorization_trustor(trustor_org_id)


Delete Org Trust

Wraps DELETE /api/v2/orgauthorization/trustors/{trustorOrgId} 

Requires ANY permissions: 

* authorization:orgTrustor:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustor_org_id = 'trustor_org_id_example' # str | Trustor Organization Id

try:
    # Delete Org Trust
    api_instance.delete_orgauthorization_trustor(trustor_org_id)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustor: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |

### Return type

void (empty response body)


## delete_orgauthorization_trustor_cloneduser

>  delete_orgauthorization_trustor_cloneduser(trustor_org_id, trustee_user_id)


Delete Cloned User

Wraps DELETE /api/v2/orgauthorization/trustors/{trustorOrgId}/clonedusers/{trusteeUserId} 

Requires ANY permissions: 

* authorization:orgTrusteeUser:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustor_org_id = 'trustor_org_id_example' # str | Trustor Organization Id
trustee_user_id = 'trustee_user_id_example' # str | Trustee User Id

try:
    # Delete Cloned User
    api_instance.delete_orgauthorization_trustor_cloneduser(trustor_org_id, trustee_user_id)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustor_cloneduser: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |

### Return type

void (empty response body)


## delete_orgauthorization_trustor_group

>  delete_orgauthorization_trustor_group(trustor_org_id, trustor_group_id)


Delete Trustee Group

Wraps DELETE /api/v2/orgauthorization/trustors/{trustorOrgId}/groups/{trustorGroupId} 

Requires ANY permissions: 

* authorization:orgTrusteeGroup:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustor_org_id = 'trustor_org_id_example' # str | Trustor Organization Id
trustor_group_id = 'trustor_group_id_example' # str | Trustor Group Id

try:
    # Delete Trustee Group
    api_instance.delete_orgauthorization_trustor_group(trustor_org_id, trustor_group_id)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustor_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |
| **trustor_group_id** | **str**| Trustor Group Id |  |

### Return type

void (empty response body)


## delete_orgauthorization_trustor_user

>  delete_orgauthorization_trustor_user(trustor_org_id, trustee_user_id)


Delete Trustee User

Wraps DELETE /api/v2/orgauthorization/trustors/{trustorOrgId}/users/{trusteeUserId} 

Requires ANY permissions: 

* authorization:orgTrusteeUser:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustor_org_id = 'trustor_org_id_example' # str | Trustor Organization Id
trustee_user_id = 'trustee_user_id_example' # str | Trustee User Id

try:
    # Delete Trustee User
    api_instance.delete_orgauthorization_trustor_user(trustor_org_id, trustee_user_id)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustor_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |

### Return type

void (empty response body)


## delete_orgauthorization_trustors

>  delete_orgauthorization_trustors(id)


Delete Bulk Org Trustors

delete_orgauthorization_trustors is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/orgauthorization/trustors 

Requires ANY permissions: 

* authorization:orgTrustor:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
id = ['id_example'] # list[str] | Comma separated list of trustor ids to remove

try:
    # Delete Bulk Org Trustors
    api_instance.delete_orgauthorization_trustors(id)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustors: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str)| Comma separated list of trustor ids to remove |  |

### Return type

void (empty response body)


## get_orgauthorization_pairing

> [**TrustRequest**](TrustRequest) get_orgauthorization_pairing(pairing_id)


Get Pairing Info

Wraps GET /api/v2/orgauthorization/pairings/{pairingId} 

Requires ANY permissions: 

* authorization:orgTrustee:view
* authorization:orgTrustor:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
pairing_id = 'pairing_id_example' # str | Pairing Id

try:
    # Get Pairing Info
    api_response = api_instance.get_orgauthorization_pairing(pairing_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_pairing: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pairing_id** | **str**| Pairing Id |  |

### Return type

[**TrustRequest**](TrustRequest)


## get_orgauthorization_trustee

> [**Trustee**](Trustee) get_orgauthorization_trustee(trustee_org_id)


Get Org Trust

Wraps GET /api/v2/orgauthorization/trustees/{trusteeOrgId} 

Requires ANY permissions: 

* authorization:orgTrustee:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id

try:
    # Get Org Trust
    api_response = api_instance.get_orgauthorization_trustee(trustee_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustee: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |

### Return type

[**Trustee**](Trustee)


## get_orgauthorization_trustee_clonedusers

> [**ClonedUserEntityListing**](ClonedUserEntityListing) get_orgauthorization_trustee_clonedusers(trustee_org_id)


The list of cloned users from the trustee organization (i.e. users with a native user record).

There can be no more than 5 cloned users per organization, so results are represented as simple list and not paged

Wraps GET /api/v2/orgauthorization/trustees/{trusteeOrgId}/clonedusers 

Requires ANY permissions: 

* directory:user:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id

try:
    # The list of cloned users from the trustee organization (i.e. users with a native user record).
    api_response = api_instance.get_orgauthorization_trustee_clonedusers(trustee_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustee_clonedusers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |

### Return type

[**ClonedUserEntityListing**](ClonedUserEntityListing)


## get_orgauthorization_trustee_group

> [**TrustGroup**](TrustGroup) get_orgauthorization_trustee_group(trustee_org_id, trustee_group_id)


Get Trustee Group

Wraps GET /api/v2/orgauthorization/trustees/{trusteeOrgId}/groups/{trusteeGroupId} 

Requires ANY permissions: 

* authorization:orgTrusteeGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
trustee_group_id = 'trustee_group_id_example' # str | Trustee Group Id

try:
    # Get Trustee Group
    api_response = api_instance.get_orgauthorization_trustee_group(trustee_org_id, trustee_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustee_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_group_id** | **str**| Trustee Group Id |  |

### Return type

[**TrustGroup**](TrustGroup)


## get_orgauthorization_trustee_group_roles

> [**UserAuthorization**](UserAuthorization) get_orgauthorization_trustee_group_roles(trustee_org_id, trustee_group_id)


Get Trustee Group Roles

Wraps GET /api/v2/orgauthorization/trustees/{trusteeOrgId}/groups/{trusteeGroupId}/roles 

Requires ANY permissions: 

* authorization:orgTrusteeGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
trustee_group_id = 'trustee_group_id_example' # str | Trustee Group Id

try:
    # Get Trustee Group Roles
    api_response = api_instance.get_orgauthorization_trustee_group_roles(trustee_org_id, trustee_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustee_group_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_group_id** | **str**| Trustee Group Id |  |

### Return type

[**UserAuthorization**](UserAuthorization)


## get_orgauthorization_trustee_groups

> [**TrustGroupEntityListing**](TrustGroupEntityListing) get_orgauthorization_trustee_groups(trustee_org_id, page_size=page_size, page_number=page_number)


The list of trustee groups for this organization (i.e. groups granted access to this organization).

Wraps GET /api/v2/orgauthorization/trustees/{trusteeOrgId}/groups 

Requires ANY permissions: 

* authorization:orgTrusteeGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # The list of trustee groups for this organization (i.e. groups granted access to this organization).
    api_response = api_instance.get_orgauthorization_trustee_groups(trustee_org_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustee_groups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**TrustGroupEntityListing**](TrustGroupEntityListing)


## get_orgauthorization_trustee_user

> [**TrustUser**](TrustUser) get_orgauthorization_trustee_user(trustee_org_id, trustee_user_id)


Get Trustee User

Wraps GET /api/v2/orgauthorization/trustees/{trusteeOrgId}/users/{trusteeUserId} 

Requires ANY permissions: 

* authorization:orgTrusteeUser:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
trustee_user_id = 'trustee_user_id_example' # str | Trustee User Id

try:
    # Get Trustee User
    api_response = api_instance.get_orgauthorization_trustee_user(trustee_org_id, trustee_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustee_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |

### Return type

[**TrustUser**](TrustUser)


## get_orgauthorization_trustee_user_roles

> [**UserAuthorization**](UserAuthorization) get_orgauthorization_trustee_user_roles(trustee_org_id, trustee_user_id)


Get Trustee User Roles

Wraps GET /api/v2/orgauthorization/trustees/{trusteeOrgId}/users/{trusteeUserId}/roles 

Requires ANY permissions: 

* authorization:orgTrusteeUser:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
trustee_user_id = 'trustee_user_id_example' # str | Trustee User Id

try:
    # Get Trustee User Roles
    api_response = api_instance.get_orgauthorization_trustee_user_roles(trustee_org_id, trustee_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustee_user_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |

### Return type

[**UserAuthorization**](UserAuthorization)


## get_orgauthorization_trustee_users

> [**TrustUserEntityListing**](TrustUserEntityListing) get_orgauthorization_trustee_users(trustee_org_id, page_size=page_size, page_number=page_number)


The list of trustee users for this organization (i.e. users granted access to this organization).

Wraps GET /api/v2/orgauthorization/trustees/{trusteeOrgId}/users 

Requires ANY permissions: 

* authorization:orgTrusteeUser:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # The list of trustee users for this organization (i.e. users granted access to this organization).
    api_response = api_instance.get_orgauthorization_trustee_users(trustee_org_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustee_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**TrustUserEntityListing**](TrustUserEntityListing)


## get_orgauthorization_trustees

> [**TrustEntityListing**](TrustEntityListing) get_orgauthorization_trustees(page_size=page_size, page_number=page_number)


The list of trustees for this organization (i.e. organizations granted access to this organization).

Wraps GET /api/v2/orgauthorization/trustees 

Requires ANY permissions: 

* authorization:orgTrustee:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # The list of trustees for this organization (i.e. organizations granted access to this organization).
    api_response = api_instance.get_orgauthorization_trustees(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustees: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**TrustEntityListing**](TrustEntityListing)


## get_orgauthorization_trustees_care

> [**TrusteeReferenceList**](TrusteeReferenceList) get_orgauthorization_trustees_care()


Get Customer Care organization ids.

Wraps GET /api/v2/orgauthorization/trustees/care 

Requires ANY permissions: 

* authorization:orgTrustee:view
* authorization:orgTrusteeUser:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()

try:
    # Get Customer Care organization ids.
    api_response = api_instance.get_orgauthorization_trustees_care()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustees_care: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**TrusteeReferenceList**](TrusteeReferenceList)


## get_orgauthorization_trustees_default

> [**Trustee**](Trustee) get_orgauthorization_trustees_default()


Get organization authorization trust with Customer Care, if one exists.

Wraps GET /api/v2/orgauthorization/trustees/default 

Requires ANY permissions: 

* authorization:orgTrustee:view
* authorization:orgTrusteeUser:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()

try:
    # Get organization authorization trust with Customer Care, if one exists.
    api_response = api_instance.get_orgauthorization_trustees_default()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustees_default: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**Trustee**](Trustee)


## get_orgauthorization_trustor

> [**Trustor**](Trustor) get_orgauthorization_trustor(trustor_org_id)


Get Org Trust

Wraps GET /api/v2/orgauthorization/trustors/{trustorOrgId} 

Requires ANY permissions: 

* authorization:orgTrustor:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustor_org_id = 'trustor_org_id_example' # str | Trustor Organization Id

try:
    # Get Org Trust
    api_response = api_instance.get_orgauthorization_trustor(trustor_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustor: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |

### Return type

[**Trustor**](Trustor)


## get_orgauthorization_trustor_cloneduser

> [**ClonedUser**](ClonedUser) get_orgauthorization_trustor_cloneduser(trustor_org_id, trustee_user_id)


Get Cloned User

Wraps GET /api/v2/orgauthorization/trustors/{trustorOrgId}/clonedusers/{trusteeUserId} 

Requires ANY permissions: 

* authorization:orgTrusteeUser:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustor_org_id = 'trustor_org_id_example' # str | Trustor Organization Id
trustee_user_id = 'trustee_user_id_example' # str | Trustee User Id

try:
    # Get Cloned User
    api_response = api_instance.get_orgauthorization_trustor_cloneduser(trustor_org_id, trustee_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustor_cloneduser: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |

### Return type

[**ClonedUser**](ClonedUser)


## get_orgauthorization_trustor_clonedusers

> [**ClonedUserEntityListing**](ClonedUserEntityListing) get_orgauthorization_trustor_clonedusers(trustor_org_id)


The list of cloned users in the trustor organization (i.e. users with a native user record).

Wraps GET /api/v2/orgauthorization/trustors/{trustorOrgId}/clonedusers 

Requires ANY permissions: 

* authorization:orgTrusteeUser:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustor_org_id = 'trustor_org_id_example' # str | Trustor Organization Id

try:
    # The list of cloned users in the trustor organization (i.e. users with a native user record).
    api_response = api_instance.get_orgauthorization_trustor_clonedusers(trustor_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustor_clonedusers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |

### Return type

[**ClonedUserEntityListing**](ClonedUserEntityListing)


## get_orgauthorization_trustor_group

> [**TrustGroup**](TrustGroup) get_orgauthorization_trustor_group(trustor_org_id, trustor_group_id)


Get Trustee Group

Wraps GET /api/v2/orgauthorization/trustors/{trustorOrgId}/groups/{trustorGroupId} 

Requires ANY permissions: 

* authorization:orgTrusteeGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustor_org_id = 'trustor_org_id_example' # str | Trustor Organization Id
trustor_group_id = 'trustor_group_id_example' # str | Trustor Group Id

try:
    # Get Trustee Group
    api_response = api_instance.get_orgauthorization_trustor_group(trustor_org_id, trustor_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustor_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |
| **trustor_group_id** | **str**| Trustor Group Id |  |

### Return type

[**TrustGroup**](TrustGroup)


## get_orgauthorization_trustor_groups

> [**TrustGroupEntityListing**](TrustGroupEntityListing) get_orgauthorization_trustor_groups(trustor_org_id, page_size=page_size, page_number=page_number)


The list of groups in the trustor organization (i.e. groups granted access).

Wraps GET /api/v2/orgauthorization/trustors/{trustorOrgId}/groups 

Requires ANY permissions: 

* authorization:orgTrusteeGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustor_org_id = 'trustor_org_id_example' # str | Trustee Organization Id
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # The list of groups in the trustor organization (i.e. groups granted access).
    api_response = api_instance.get_orgauthorization_trustor_groups(trustor_org_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustor_groups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustee Organization Id |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**TrustGroupEntityListing**](TrustGroupEntityListing)


## get_orgauthorization_trustor_user

> [**TrustUser**](TrustUser) get_orgauthorization_trustor_user(trustor_org_id, trustee_user_id)


Get Trustee User

Wraps GET /api/v2/orgauthorization/trustors/{trustorOrgId}/users/{trusteeUserId} 

Requires ANY permissions: 

* authorization:orgTrusteeUser:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustor_org_id = 'trustor_org_id_example' # str | Trustor Organization Id
trustee_user_id = 'trustee_user_id_example' # str | Trustee User Id

try:
    # Get Trustee User
    api_response = api_instance.get_orgauthorization_trustor_user(trustor_org_id, trustee_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustor_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |

### Return type

[**TrustUser**](TrustUser)


## get_orgauthorization_trustor_users

> [**TrustUserEntityListing**](TrustUserEntityListing) get_orgauthorization_trustor_users(trustor_org_id, page_size=page_size, page_number=page_number)


The list of users in the trustor organization (i.e. users granted access).

Wraps GET /api/v2/orgauthorization/trustors/{trustorOrgId}/users 

Requires ANY permissions: 

* authorization:orgTrusteeUser:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustor_org_id = 'trustor_org_id_example' # str | Trustee Organization Id
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # The list of users in the trustor organization (i.e. users granted access).
    api_response = api_instance.get_orgauthorization_trustor_users(trustor_org_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustor_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustee Organization Id |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**TrustUserEntityListing**](TrustUserEntityListing)


## get_orgauthorization_trustors

> [**TrustorEntityListing**](TrustorEntityListing) get_orgauthorization_trustors(page_size=page_size, page_number=page_number)


The list of organizations that have authorized/trusted your organization.

Wraps GET /api/v2/orgauthorization/trustors 

Requires ANY permissions: 

* authorization:orgTrustor:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # The list of organizations that have authorized/trusted your organization.
    api_response = api_instance.get_orgauthorization_trustors(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustors: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**TrustorEntityListing**](TrustorEntityListing)


## post_orgauthorization_pairings

> [**TrustRequest**](TrustRequest) post_orgauthorization_pairings(body)


A pairing id is created by the trustee and given to the trustor to create a trust.

Wraps POST /api/v2/orgauthorization/pairings 

Requires ANY permissions: 

* authorization:orgTrustee:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
body = PureCloudPlatformClientV2.TrustRequestCreate() # TrustRequestCreate | Pairing Info

try:
    # A pairing id is created by the trustee and given to the trustor to create a trust.
    api_response = api_instance.post_orgauthorization_pairings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->post_orgauthorization_pairings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TrustRequestCreate**](TrustRequestCreate)| Pairing Info |  |

### Return type

[**TrustRequest**](TrustRequest)


## post_orgauthorization_trustee_groups

> [**TrustGroup**](TrustGroup) post_orgauthorization_trustee_groups(trustee_org_id, body)


Add a group to the trust.

Wraps POST /api/v2/orgauthorization/trustees/{trusteeOrgId}/groups 

Requires ANY permissions: 

* authorization:orgTrusteeGroup:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
body = PureCloudPlatformClientV2.TrustMemberCreate() # TrustMemberCreate | Trust

try:
    # Add a group to the trust.
    api_response = api_instance.post_orgauthorization_trustee_groups(trustee_org_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->post_orgauthorization_trustee_groups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **body** | [**TrustMemberCreate**](TrustMemberCreate)| Trust |  |

### Return type

[**TrustGroup**](TrustGroup)


## post_orgauthorization_trustee_users

> [**TrustUser**](TrustUser) post_orgauthorization_trustee_users(trustee_org_id, body)


Add a user to the trust.

Wraps POST /api/v2/orgauthorization/trustees/{trusteeOrgId}/users 

Requires ANY permissions: 

* authorization:orgTrusteeUser:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
body = PureCloudPlatformClientV2.TrustMemberCreate() # TrustMemberCreate | Trust

try:
    # Add a user to the trust.
    api_response = api_instance.post_orgauthorization_trustee_users(trustee_org_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->post_orgauthorization_trustee_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **body** | [**TrustMemberCreate**](TrustMemberCreate)| Trust |  |

### Return type

[**TrustUser**](TrustUser)


## post_orgauthorization_trustees

> [**Trustee**](Trustee) post_orgauthorization_trustees(body)


Create a new organization authorization trust. This is required to grant other organizations access to your organization.

Wraps POST /api/v2/orgauthorization/trustees 

Requires ALL permissions: 

* authorization:orgTrustee:add
* authorization:orgTrusteeUser:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
body = PureCloudPlatformClientV2.TrustCreate() # TrustCreate | Trust

try:
    # Create a new organization authorization trust. This is required to grant other organizations access to your organization.
    api_response = api_instance.post_orgauthorization_trustees(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->post_orgauthorization_trustees: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TrustCreate**](TrustCreate)| Trust |  |

### Return type

[**Trustee**](Trustee)


## post_orgauthorization_trustees_audits

> object** post_orgauthorization_trustees_audits(body, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)


Get Org Trustee Audits

Wraps POST /api/v2/orgauthorization/trustees/audits 

Requires ANY permissions: 

* authorization:audit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
body = PureCloudPlatformClientV2.TrusteeAuditQueryRequest() # TrusteeAuditQueryRequest | Values to scope the request.
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = ''timestamp'' # str | Sort by (optional) (default to 'timestamp')
sort_order = ''descending'' # str | Sort order (optional) (default to 'descending')

try:
    # Get Org Trustee Audits
    api_response = api_instance.post_orgauthorization_trustees_audits(body, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->post_orgauthorization_trustees_audits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TrusteeAuditQueryRequest**](TrusteeAuditQueryRequest)| Values to scope the request. |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;timestamp&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;descending&#39;] |

### Return type

**object**


## post_orgauthorization_trustees_care

> [**TrustEntityListing**](TrustEntityListing) post_orgauthorization_trustees_care(assign_default_role=assign_default_role, auto_expire=auto_expire, assign_full_access=assign_full_access, allow_trusted_user_access=allow_trusted_user_access)


Create a new organization authorization trust with Customer Care. This is required to grant your regional Customer Care organization access to your organization.

Wraps POST /api/v2/orgauthorization/trustees/care 

Requires ALL permissions: 

* authorization:orgTrustee:add
* authorization:orgTrusteeUser:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
assign_default_role = True # bool | Assign Admin role to default pairing with Customer Care (optional)
auto_expire = True # bool | Automatically expire pairing after 30 days (optional)
assign_full_access = True # bool | Grant Customer Care full access to the organization (optional)
allow_trusted_user_access = True # bool | Make Customer Care a Trusted User (optional)

try:
    # Create a new organization authorization trust with Customer Care. This is required to grant your regional Customer Care organization access to your organization.
    api_response = api_instance.post_orgauthorization_trustees_care(assign_default_role=assign_default_role, auto_expire=auto_expire, assign_full_access=assign_full_access, allow_trusted_user_access=allow_trusted_user_access)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->post_orgauthorization_trustees_care: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assign_default_role** | **bool**| Assign Admin role to default pairing with Customer Care | [optional]  |
| **auto_expire** | **bool**| Automatically expire pairing after 30 days | [optional]  |
| **assign_full_access** | **bool**| Grant Customer Care full access to the organization | [optional]  |
| **allow_trusted_user_access** | **bool**| Make Customer Care a Trusted User | [optional]  |

### Return type

[**TrustEntityListing**](TrustEntityListing)


## post_orgauthorization_trustees_default

> [**Trustee**](Trustee) post_orgauthorization_trustees_default(assign_default_role=assign_default_role, auto_expire=auto_expire)


Create a new organization authorization trust with Customer Care. This is required to grant your regional Customer Care organization access to your organization.

Wraps POST /api/v2/orgauthorization/trustees/default 

Requires ALL permissions: 

* authorization:orgTrustee:add
* authorization:orgTrusteeUser:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
assign_default_role = True # bool | Assign Admin role to default pairing with Customer Care (optional)
auto_expire = True # bool | Automatically expire pairing after 30 days (optional)

try:
    # Create a new organization authorization trust with Customer Care. This is required to grant your regional Customer Care organization access to your organization.
    api_response = api_instance.post_orgauthorization_trustees_default(assign_default_role=assign_default_role, auto_expire=auto_expire)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->post_orgauthorization_trustees_default: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assign_default_role** | **bool**| Assign Admin role to default pairing with Customer Care | [optional]  |
| **auto_expire** | **bool**| Automatically expire pairing after 30 days | [optional]  |

### Return type

[**Trustee**](Trustee)


## post_orgauthorization_trustor_audits

> object** post_orgauthorization_trustor_audits(body, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)


Get Org Trustor Audits

Wraps POST /api/v2/orgauthorization/trustor/audits 

Requires ANY permissions: 

* authorization:audit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
body = PureCloudPlatformClientV2.TrustorAuditQueryRequest() # TrustorAuditQueryRequest | Values to scope the request.
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = ''timestamp'' # str | Sort by (optional) (default to 'timestamp')
sort_order = ''descending'' # str | Sort order (optional) (default to 'descending')

try:
    # Get Org Trustor Audits
    api_response = api_instance.post_orgauthorization_trustor_audits(body, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->post_orgauthorization_trustor_audits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TrustorAuditQueryRequest**](TrustorAuditQueryRequest)| Values to scope the request. |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to &#39;timestamp&#39;] |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;descending&#39;] |

### Return type

**object**


## put_orgauthorization_trustee

> [**Trustee**](Trustee) put_orgauthorization_trustee(trustee_org_id, body)


Update Org Trust

Wraps PUT /api/v2/orgauthorization/trustees/{trusteeOrgId} 

Requires ANY permissions: 

* authorization:orgTrustee:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
body = PureCloudPlatformClientV2.TrustUpdate() # TrustUpdate | Client

try:
    # Update Org Trust
    api_response = api_instance.put_orgauthorization_trustee(trustee_org_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->put_orgauthorization_trustee: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **body** | [**TrustUpdate**](TrustUpdate)| Client |  |

### Return type

[**Trustee**](Trustee)


## put_orgauthorization_trustee_group_roledivisions

> [**UserAuthorization**](UserAuthorization) put_orgauthorization_trustee_group_roledivisions(trustee_org_id, trustee_group_id, body)


Update Trustee Group Roles

Wraps PUT /api/v2/orgauthorization/trustees/{trusteeOrgId}/groups/{trusteeGroupId}/roledivisions 

Requires ANY permissions: 

* authorization:orgTrusteeGroup:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
trustee_group_id = 'trustee_group_id_example' # str | Trustee Group Id
body = PureCloudPlatformClientV2.RoleDivisionGrants() # RoleDivisionGrants | Set of roles with corresponding divisions to apply

try:
    # Update Trustee Group Roles
    api_response = api_instance.put_orgauthorization_trustee_group_roledivisions(trustee_org_id, trustee_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->put_orgauthorization_trustee_group_roledivisions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_group_id** | **str**| Trustee Group Id |  |
| **body** | [**RoleDivisionGrants**](RoleDivisionGrants)| Set of roles with corresponding divisions to apply |  |

### Return type

[**UserAuthorization**](UserAuthorization)


## put_orgauthorization_trustee_group_roles

> [**UserAuthorization**](UserAuthorization) put_orgauthorization_trustee_group_roles(trustee_org_id, trustee_group_id, body)


Update Trustee Group Roles

Wraps PUT /api/v2/orgauthorization/trustees/{trusteeOrgId}/groups/{trusteeGroupId}/roles 

Requires ANY permissions: 

* authorization:orgTrusteeGroup:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
trustee_group_id = 'trustee_group_id_example' # str | Trustee Group Id
body = ['body_example'] # list[str] | List of roles

try:
    # Update Trustee Group Roles
    api_response = api_instance.put_orgauthorization_trustee_group_roles(trustee_org_id, trustee_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->put_orgauthorization_trustee_group_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_group_id** | **str**| Trustee Group Id |  |
| **body** | [**list[str]**](str)| List of roles |  |

### Return type

[**UserAuthorization**](UserAuthorization)


## put_orgauthorization_trustee_user_roledivisions

> [**UserAuthorization**](UserAuthorization) put_orgauthorization_trustee_user_roledivisions(trustee_org_id, trustee_user_id, body)


Update Trustee User Roles

Wraps PUT /api/v2/orgauthorization/trustees/{trusteeOrgId}/users/{trusteeUserId}/roledivisions 

Requires ANY permissions: 

* authorization:orgTrusteeUser:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
trustee_user_id = 'trustee_user_id_example' # str | Trustee User Id
body = PureCloudPlatformClientV2.RoleDivisionGrants() # RoleDivisionGrants | Set of roles with corresponding divisions to apply

try:
    # Update Trustee User Roles
    api_response = api_instance.put_orgauthorization_trustee_user_roledivisions(trustee_org_id, trustee_user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->put_orgauthorization_trustee_user_roledivisions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |
| **body** | [**RoleDivisionGrants**](RoleDivisionGrants)| Set of roles with corresponding divisions to apply |  |

### Return type

[**UserAuthorization**](UserAuthorization)


## put_orgauthorization_trustee_user_roles

> [**UserAuthorization**](UserAuthorization) put_orgauthorization_trustee_user_roles(trustee_org_id, trustee_user_id, body)


Update Trustee User Roles

Wraps PUT /api/v2/orgauthorization/trustees/{trusteeOrgId}/users/{trusteeUserId}/roles 

Requires ANY permissions: 

* authorization:orgTrusteeUser:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustee_org_id = 'trustee_org_id_example' # str | Trustee Organization Id
trustee_user_id = 'trustee_user_id_example' # str | Trustee User Id
body = ['body_example'] # list[str] | List of roles

try:
    # Update Trustee User Roles
    api_response = api_instance.put_orgauthorization_trustee_user_roles(trustee_org_id, trustee_user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->put_orgauthorization_trustee_user_roles: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |
| **body** | [**list[str]**](str)| List of roles |  |

### Return type

[**UserAuthorization**](UserAuthorization)


## put_orgauthorization_trustor_cloneduser

> [**ClonedUser**](ClonedUser) put_orgauthorization_trustor_cloneduser(trustor_org_id, trustee_user_id)


Creates a clone of the trustee user in the trustor org.

Wraps PUT /api/v2/orgauthorization/trustors/{trustorOrgId}/clonedusers/{trusteeUserId} 

Requires ALL permissions: 

* authorization:orgTrusteeUser:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustor_org_id = 'trustor_org_id_example' # str | Trustor Organization Id
trustee_user_id = 'trustee_user_id_example' # str | Trustee User Id

try:
    # Creates a clone of the trustee user in the trustor org.
    api_response = api_instance.put_orgauthorization_trustor_cloneduser(trustor_org_id, trustee_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->put_orgauthorization_trustor_cloneduser: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |

### Return type

[**ClonedUser**](ClonedUser)


## put_orgauthorization_trustor_group

> [**TrustGroup**](TrustGroup) put_orgauthorization_trustor_group(trustor_org_id, trustor_group_id)


Add a Trustee Group to the trust.

Wraps PUT /api/v2/orgauthorization/trustors/{trustorOrgId}/groups/{trustorGroupId} 

Requires ALL permissions: 

* authorization:orgTrusteeGroup:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustor_org_id = 'trustor_org_id_example' # str | Trustor Organization Id
trustor_group_id = 'trustor_group_id_example' # str | Trustor Group Id

try:
    # Add a Trustee Group to the trust.
    api_response = api_instance.put_orgauthorization_trustor_group(trustor_org_id, trustor_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->put_orgauthorization_trustor_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |
| **trustor_group_id** | **str**| Trustor Group Id |  |

### Return type

[**TrustGroup**](TrustGroup)


## put_orgauthorization_trustor_user

> [**TrustUser**](TrustUser) put_orgauthorization_trustor_user(trustor_org_id, trustee_user_id)


Add a Trustee user to the trust.

Wraps PUT /api/v2/orgauthorization/trustors/{trustorOrgId}/users/{trusteeUserId} 

Requires ALL permissions: 

* authorization:orgTrusteeUser:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OrganizationAuthorizationApi()
trustor_org_id = 'trustor_org_id_example' # str | Trustor Organization Id
trustee_user_id = 'trustee_user_id_example' # str | Trustee User Id

try:
    # Add a Trustee user to the trust.
    api_response = api_instance.put_orgauthorization_trustor_user(trustor_org_id, trustee_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationAuthorizationApi->put_orgauthorization_trustor_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |

### Return type

[**TrustUser**](TrustUser)


_PureCloudPlatformClientV2 222.0.0_

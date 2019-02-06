---
title: OrganizationAuthorizationApi
---

## PureCloudPlatformClientV2.OrganizationAuthorizationApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_orgauthorization_trustee**](OrganizationAuthorizationApi.html#delete_orgauthorization_trustee) | Delete Org Trust|
|[**delete_orgauthorization_trustee_user**](OrganizationAuthorizationApi.html#delete_orgauthorization_trustee_user) | Delete Trustee User|
|[**delete_orgauthorization_trustee_user_roles**](OrganizationAuthorizationApi.html#delete_orgauthorization_trustee_user_roles) | Delete Trustee User Roles|
|[**delete_orgauthorization_trustor**](OrganizationAuthorizationApi.html#delete_orgauthorization_trustor) | Delete Org Trust|
|[**delete_orgauthorization_trustor_user**](OrganizationAuthorizationApi.html#delete_orgauthorization_trustor_user) | Delete Trustee User|
|[**get_orgauthorization_pairing**](OrganizationAuthorizationApi.html#get_orgauthorization_pairing) | Get Pairing Info|
|[**get_orgauthorization_trustee**](OrganizationAuthorizationApi.html#get_orgauthorization_trustee) | Get Org Trust|
|[**get_orgauthorization_trustee_user**](OrganizationAuthorizationApi.html#get_orgauthorization_trustee_user) | Get Trustee User|
|[**get_orgauthorization_trustee_user_roles**](OrganizationAuthorizationApi.html#get_orgauthorization_trustee_user_roles) | Get Trustee User Roles|
|[**get_orgauthorization_trustee_users**](OrganizationAuthorizationApi.html#get_orgauthorization_trustee_users) | The list of trustee users for this organization (i.e. users granted access to this organization).|
|[**get_orgauthorization_trustees**](OrganizationAuthorizationApi.html#get_orgauthorization_trustees) | The list of trustees for this organization (i.e. organizations granted access to this organization).|
|[**get_orgauthorization_trustor**](OrganizationAuthorizationApi.html#get_orgauthorization_trustor) | Get Org Trust|
|[**get_orgauthorization_trustor_user**](OrganizationAuthorizationApi.html#get_orgauthorization_trustor_user) | Get Trustee User|
|[**get_orgauthorization_trustor_users**](OrganizationAuthorizationApi.html#get_orgauthorization_trustor_users) | The list of users in the trustor organization (i.e. users granted access).|
|[**get_orgauthorization_trustors**](OrganizationAuthorizationApi.html#get_orgauthorization_trustors) | The list of organizations that have authorized/trusted your organization.|
|[**post_orgauthorization_pairings**](OrganizationAuthorizationApi.html#post_orgauthorization_pairings) | A pairing id is created by the trustee and given to the trustor to create a trust.|
|[**post_orgauthorization_trustee_users**](OrganizationAuthorizationApi.html#post_orgauthorization_trustee_users) | Add a user to the trust.|
|[**post_orgauthorization_trustees**](OrganizationAuthorizationApi.html#post_orgauthorization_trustees) | Create a new organization authorization trust. This is required to grant other organizations access to your organization.|
|[**post_orgauthorization_trustees_audits**](OrganizationAuthorizationApi.html#post_orgauthorization_trustees_audits) | Get Org Trustee Audits|
|[**post_orgauthorization_trustor_audits**](OrganizationAuthorizationApi.html#post_orgauthorization_trustor_audits) | Get Org Trustor Audits|
|[**put_orgauthorization_trustee**](OrganizationAuthorizationApi.html#put_orgauthorization_trustee) | Update Org Trust|
|[**put_orgauthorization_trustee_user_roles**](OrganizationAuthorizationApi.html#put_orgauthorization_trustee_user_roles) | Update Trustee User Roles|
|[**put_orgauthorization_trustor_user**](OrganizationAuthorizationApi.html#put_orgauthorization_trustor_user) | Add a Trustee user to the trust.|
{: class="table table-striped"}

<a name="delete_orgauthorization_trustee"></a>

##  delete_orgauthorization_trustee(trustee_org_id)



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
    print "Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustee: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_orgauthorization_trustee_user"></a>

##  delete_orgauthorization_trustee_user(trustee_org_id, trustee_user_id)



Delete Trustee User



Wraps DELETE /api/v2/orgauthorization/trustees/{trusteeOrgId}/users/{trusteeUserId} 

Requires ANY permissions: 

* authorization:orgTrusteeUser:delete
* admin
* role_manager

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
    print "Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustee_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_orgauthorization_trustee_user_roles"></a>

##  delete_orgauthorization_trustee_user_roles(trustee_org_id, trustee_user_id)



Delete Trustee User Roles



Wraps DELETE /api/v2/orgauthorization/trustees/{trusteeOrgId}/users/{trusteeUserId}/roles 

Requires ANY permissions: 

* authorization:orgTrusteeUser:delete
* admin
* role_manager

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
    print "Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustee_user_roles: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_orgauthorization_trustor"></a>

##  delete_orgauthorization_trustor(trustor_org_id)



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
    print "Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustor: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_orgauthorization_trustor_user"></a>

##  delete_orgauthorization_trustor_user(trustor_org_id, trustee_user_id)



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
    print "Exception when calling OrganizationAuthorizationApi->delete_orgauthorization_trustor_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_orgauthorization_pairing"></a>

## [**TrustRequest**](TrustRequest.html) get_orgauthorization_pairing(pairing_id)



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
    print "Exception when calling OrganizationAuthorizationApi->get_orgauthorization_pairing: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pairing_id** | **str**| Pairing Id |  |
{: class="table table-striped"}

### Return type

[**TrustRequest**](TrustRequest.html)

<a name="get_orgauthorization_trustee"></a>

## [**Trustee**](Trustee.html) get_orgauthorization_trustee(trustee_org_id)



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
    print "Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustee: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
{: class="table table-striped"}

### Return type

[**Trustee**](Trustee.html)

<a name="get_orgauthorization_trustee_user"></a>

## [**TrustUser**](TrustUser.html) get_orgauthorization_trustee_user(trustee_org_id, trustee_user_id)



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
    print "Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustee_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |
{: class="table table-striped"}

### Return type

[**TrustUser**](TrustUser.html)

<a name="get_orgauthorization_trustee_user_roles"></a>

## [**UserAuthorization**](UserAuthorization.html) get_orgauthorization_trustee_user_roles(trustee_org_id, trustee_user_id)



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
    print "Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustee_user_roles: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |
{: class="table table-striped"}

### Return type

[**UserAuthorization**](UserAuthorization.html)

<a name="get_orgauthorization_trustee_users"></a>

## [**TrustUserEntityListing**](TrustUserEntityListing.html) get_orgauthorization_trustee_users(trustee_org_id, page_size=page_size, page_number=page_number)



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
    print "Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustee_users: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**TrustUserEntityListing**](TrustUserEntityListing.html)

<a name="get_orgauthorization_trustees"></a>

## [**TrustEntityListing**](TrustEntityListing.html) get_orgauthorization_trustees(page_size=page_size, page_number=page_number)



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
    print "Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustees: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**TrustEntityListing**](TrustEntityListing.html)

<a name="get_orgauthorization_trustor"></a>

## [**Trustor**](Trustor.html) get_orgauthorization_trustor(trustor_org_id)



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
    print "Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustor: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |
{: class="table table-striped"}

### Return type

[**Trustor**](Trustor.html)

<a name="get_orgauthorization_trustor_user"></a>

## [**TrustUser**](TrustUser.html) get_orgauthorization_trustor_user(trustor_org_id, trustee_user_id)



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
    print "Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustor_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |
{: class="table table-striped"}

### Return type

[**TrustUser**](TrustUser.html)

<a name="get_orgauthorization_trustor_users"></a>

## [**TrustUserEntityListing**](TrustUserEntityListing.html) get_orgauthorization_trustor_users(trustor_org_id, page_size=page_size, page_number=page_number)



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
    print "Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustor_users: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustee Organization Id |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**TrustUserEntityListing**](TrustUserEntityListing.html)

<a name="get_orgauthorization_trustors"></a>

## [**TrustorEntityListing**](TrustorEntityListing.html) get_orgauthorization_trustors(page_size=page_size, page_number=page_number)



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
    print "Exception when calling OrganizationAuthorizationApi->get_orgauthorization_trustors: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**TrustorEntityListing**](TrustorEntityListing.html)

<a name="post_orgauthorization_pairings"></a>

## [**TrustRequest**](TrustRequest.html) post_orgauthorization_pairings(body)



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
    print "Exception when calling OrganizationAuthorizationApi->post_orgauthorization_pairings: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TrustRequestCreate**](TrustRequestCreate.html)| Pairing Info |  |
{: class="table table-striped"}

### Return type

[**TrustRequest**](TrustRequest.html)

<a name="post_orgauthorization_trustee_users"></a>

## [**TrustUser**](TrustUser.html) post_orgauthorization_trustee_users(trustee_org_id, body)



Add a user to the trust.



Wraps POST /api/v2/orgauthorization/trustees/{trusteeOrgId}/users 

Requires ALL permissions: 

* authorization:orgTrusteeUser:add
* admin
* role_manager

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
    print "Exception when calling OrganizationAuthorizationApi->post_orgauthorization_trustee_users: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **body** | [**TrustMemberCreate**](TrustMemberCreate.html)| Trust |  |
{: class="table table-striped"}

### Return type

[**TrustUser**](TrustUser.html)

<a name="post_orgauthorization_trustees"></a>

## [**Trustee**](Trustee.html) post_orgauthorization_trustees(body)



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
    print "Exception when calling OrganizationAuthorizationApi->post_orgauthorization_trustees: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TrustCreate**](TrustCreate.html)| Trust |  |
{: class="table table-striped"}

### Return type

[**Trustee**](Trustee.html)

<a name="post_orgauthorization_trustees_audits"></a>

## [**AuditQueryResponse**](AuditQueryResponse.html) post_orgauthorization_trustees_audits(body, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)



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
sort_by = 'timestamp' # str | Sort by (optional) (default to timestamp)
sort_order = 'descending' # str | Sort order (optional) (default to descending)

try:
    # Get Org Trustee Audits
    api_response = api_instance.post_orgauthorization_trustees_audits(body, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrganizationAuthorizationApi->post_orgauthorization_trustees_audits: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TrusteeAuditQueryRequest**](TrusteeAuditQueryRequest.html)| Values to scope the request. |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to timestamp] |
| **sort_order** | **str**| Sort order | [optional] [default to descending] |
{: class="table table-striped"}

### Return type

[**AuditQueryResponse**](AuditQueryResponse.html)

<a name="post_orgauthorization_trustor_audits"></a>

## [**AuditQueryResponse**](AuditQueryResponse.html) post_orgauthorization_trustor_audits(body, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)



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
sort_by = 'timestamp' # str | Sort by (optional) (default to timestamp)
sort_order = 'descending' # str | Sort order (optional) (default to descending)

try:
    # Get Org Trustor Audits
    api_response = api_instance.post_orgauthorization_trustor_audits(body, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrganizationAuthorizationApi->post_orgauthorization_trustor_audits: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TrustorAuditQueryRequest**](TrustorAuditQueryRequest.html)| Values to scope the request. |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_by** | **str**| Sort by | [optional] [default to timestamp] |
| **sort_order** | **str**| Sort order | [optional] [default to descending] |
{: class="table table-striped"}

### Return type

[**AuditQueryResponse**](AuditQueryResponse.html)

<a name="put_orgauthorization_trustee"></a>

## [**Trustee**](Trustee.html) put_orgauthorization_trustee(trustee_org_id, body)



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
body = PureCloudPlatformClientV2.Trustee() # Trustee | Client

try:
    # Update Org Trust
    api_response = api_instance.put_orgauthorization_trustee(trustee_org_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrganizationAuthorizationApi->put_orgauthorization_trustee: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **body** | [**Trustee**](Trustee.html)| Client |  |
{: class="table table-striped"}

### Return type

[**Trustee**](Trustee.html)

<a name="put_orgauthorization_trustee_user_roles"></a>

## [**UserAuthorization**](UserAuthorization.html) put_orgauthorization_trustee_user_roles(trustee_org_id, trustee_user_id, body)



Update Trustee User Roles



Wraps PUT /api/v2/orgauthorization/trustees/{trusteeOrgId}/users/{trusteeUserId}/roles 

Requires ANY permissions: 

* authorization:orgTrusteeUser:edit
* admin
* role_manager

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
body = [PureCloudPlatformClientV2.list[str]()] # list[str] | List of roles

try:
    # Update Trustee User Roles
    api_response = api_instance.put_orgauthorization_trustee_user_roles(trustee_org_id, trustee_user_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrganizationAuthorizationApi->put_orgauthorization_trustee_user_roles: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustee_org_id** | **str**| Trustee Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |
| **body** | **list[str]**| List of roles |  |
{: class="table table-striped"}

### Return type

[**UserAuthorization**](UserAuthorization.html)

<a name="put_orgauthorization_trustor_user"></a>

## [**TrustUser**](TrustUser.html) put_orgauthorization_trustor_user(trustor_org_id, trustee_user_id)



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
    print "Exception when calling OrganizationAuthorizationApi->put_orgauthorization_trustor_user: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trustor_org_id** | **str**| Trustor Organization Id |  |
| **trustee_user_id** | **str**| Trustee User Id |  |
{: class="table table-striped"}

### Return type

[**TrustUser**](TrustUser.html)


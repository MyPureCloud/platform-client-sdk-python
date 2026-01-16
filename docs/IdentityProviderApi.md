# IdentityProviderApi

## PureCloudPlatformClientV2.IdentityProviderApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_identityprovider**](#delete_identityprovider) | Delete Identity Provider|
|[**delete_identityproviders_adfs**](#delete_identityproviders_adfs) | Delete ADFS Identity Provider|
|[**delete_identityproviders_cic**](#delete_identityproviders_cic) | Delete Customer Interaction Center (CIC) Identity Provider|
|[**delete_identityproviders_generic**](#delete_identityproviders_generic) | Delete Generic SAML Identity Provider|
|[**delete_identityproviders_gsuite**](#delete_identityproviders_gsuite) | Delete G Suite Identity Provider|
|[**delete_identityproviders_identitynow**](#delete_identityproviders_identitynow) | Delete IdentityNow Provider|
|[**delete_identityproviders_okta**](#delete_identityproviders_okta) | Delete Okta Identity Provider|
|[**delete_identityproviders_onelogin**](#delete_identityproviders_onelogin) | Delete OneLogin Identity Provider|
|[**delete_identityproviders_ping**](#delete_identityproviders_ping) | Delete Ping Identity Provider|
|[**delete_identityproviders_purecloud**](#delete_identityproviders_purecloud) | Delete PureCloud Identity Provider|
|[**delete_identityproviders_pureengage**](#delete_identityproviders_pureengage) | Delete PureEngage Identity Provider|
|[**delete_identityproviders_salesforce**](#delete_identityproviders_salesforce) | Delete Salesforce Identity Provider|
|[**get_identityprovider**](#get_identityprovider) | Get Identity Provider|
|[**get_identityproviders**](#get_identityproviders) | The list of identity providers|
|[**get_identityproviders_adfs**](#get_identityproviders_adfs) | Get ADFS Identity Provider|
|[**get_identityproviders_cic**](#get_identityproviders_cic) | Get Customer Interaction Center (CIC) Identity Provider|
|[**get_identityproviders_generic**](#get_identityproviders_generic) | Get Generic SAML Identity Provider|
|[**get_identityproviders_gsuite**](#get_identityproviders_gsuite) | Get G Suite Identity Provider|
|[**get_identityproviders_identitynow**](#get_identityproviders_identitynow) | Get IdentityNow Provider|
|[**get_identityproviders_okta**](#get_identityproviders_okta) | Get Okta Identity Provider|
|[**get_identityproviders_onelogin**](#get_identityproviders_onelogin) | Get OneLogin Identity Provider|
|[**get_identityproviders_ping**](#get_identityproviders_ping) | Get Ping Identity Provider|
|[**get_identityproviders_purecloud**](#get_identityproviders_purecloud) | Get PureCloud Identity Provider|
|[**get_identityproviders_pureengage**](#get_identityproviders_pureengage) | Get PureEngage Identity Provider|
|[**get_identityproviders_salesforce**](#get_identityproviders_salesforce) | Get Salesforce Identity Provider|
|[**post_identityproviders**](#post_identityproviders) | Create Identity Provider|
|[**put_identityprovider**](#put_identityprovider) | Update Identity Provider|
|[**put_identityproviders_adfs**](#put_identityproviders_adfs) | Update/Create ADFS Identity Provider|
|[**put_identityproviders_cic**](#put_identityproviders_cic) | Update/Create Customer Interaction Center (CIC) Identity Provider|
|[**put_identityproviders_generic**](#put_identityproviders_generic) | Update/Create Generic SAML Identity Provider|
|[**put_identityproviders_gsuite**](#put_identityproviders_gsuite) | Update/Create G Suite Identity Provider|
|[**put_identityproviders_identitynow**](#put_identityproviders_identitynow) | Update/Create IdentityNow Provider|
|[**put_identityproviders_okta**](#put_identityproviders_okta) | Update/Create Okta Identity Provider|
|[**put_identityproviders_onelogin**](#put_identityproviders_onelogin) | Update/Create OneLogin Identity Provider|
|[**put_identityproviders_ping**](#put_identityproviders_ping) | Update/Create Ping Identity Provider|
|[**put_identityproviders_purecloud**](#put_identityproviders_purecloud) | Update/Create PureCloud Identity Provider|
|[**put_identityproviders_pureengage**](#put_identityproviders_pureengage) | Update/Create PureEngage Identity Provider|
|[**put_identityproviders_salesforce**](#put_identityproviders_salesforce) | Update/Create Salesforce Identity Provider|



## delete_identityprovider

>  delete_identityprovider(provider_id)


Delete Identity Provider

Wraps DELETE /api/v2/identityproviders/{providerId} 

Requires ANY permissions: 

* sso:provider:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
provider_id = 'provider_id_example' # str | Provider ID

try:
    # Delete Identity Provider
    api_instance.delete_identityprovider(provider_id)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->delete_identityprovider: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **provider_id** | **str**| Provider ID |  |

### Return type

void (empty response body)


## delete_identityproviders_adfs

> object** delete_identityproviders_adfs()


Delete ADFS Identity Provider

Wraps DELETE /api/v2/identityproviders/adfs 

Requires ANY permissions: 

* sso:provider:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Delete ADFS Identity Provider
    api_response = api_instance.delete_identityproviders_adfs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->delete_identityproviders_adfs: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

**object**


## delete_identityproviders_cic

> object** delete_identityproviders_cic()


Delete Customer Interaction Center (CIC) Identity Provider

Wraps DELETE /api/v2/identityproviders/cic 

Requires ANY permissions: 

* sso:provider:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Delete Customer Interaction Center (CIC) Identity Provider
    api_response = api_instance.delete_identityproviders_cic()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->delete_identityproviders_cic: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

**object**


## delete_identityproviders_generic

> object** delete_identityproviders_generic()


Delete Generic SAML Identity Provider

Wraps DELETE /api/v2/identityproviders/generic 

Requires ANY permissions: 

* sso:provider:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Delete Generic SAML Identity Provider
    api_response = api_instance.delete_identityproviders_generic()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->delete_identityproviders_generic: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

**object**


## delete_identityproviders_gsuite

> object** delete_identityproviders_gsuite()


Delete G Suite Identity Provider

Wraps DELETE /api/v2/identityproviders/gsuite 

Requires ANY permissions: 

* sso:provider:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Delete G Suite Identity Provider
    api_response = api_instance.delete_identityproviders_gsuite()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->delete_identityproviders_gsuite: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

**object**


## delete_identityproviders_identitynow

> object** delete_identityproviders_identitynow()


Delete IdentityNow Provider

Wraps DELETE /api/v2/identityproviders/identitynow 

Requires ANY permissions: 

* sso:provider:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Delete IdentityNow Provider
    api_response = api_instance.delete_identityproviders_identitynow()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->delete_identityproviders_identitynow: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

**object**


## delete_identityproviders_okta

> object** delete_identityproviders_okta()


Delete Okta Identity Provider

Wraps DELETE /api/v2/identityproviders/okta 

Requires ANY permissions: 

* sso:provider:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Delete Okta Identity Provider
    api_response = api_instance.delete_identityproviders_okta()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->delete_identityproviders_okta: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

**object**


## delete_identityproviders_onelogin

> object** delete_identityproviders_onelogin()


Delete OneLogin Identity Provider

Wraps DELETE /api/v2/identityproviders/onelogin 

Requires ANY permissions: 

* sso:provider:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Delete OneLogin Identity Provider
    api_response = api_instance.delete_identityproviders_onelogin()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->delete_identityproviders_onelogin: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

**object**


## delete_identityproviders_ping

> object** delete_identityproviders_ping()


Delete Ping Identity Provider

Wraps DELETE /api/v2/identityproviders/ping 

Requires ANY permissions: 

* sso:provider:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Delete Ping Identity Provider
    api_response = api_instance.delete_identityproviders_ping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->delete_identityproviders_ping: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

**object**


## delete_identityproviders_purecloud

> object** delete_identityproviders_purecloud()


Delete PureCloud Identity Provider

Wraps DELETE /api/v2/identityproviders/purecloud 

Requires ANY permissions: 

* sso:provider:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Delete PureCloud Identity Provider
    api_response = api_instance.delete_identityproviders_purecloud()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->delete_identityproviders_purecloud: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

**object**


## delete_identityproviders_pureengage

> object** delete_identityproviders_pureengage()


Delete PureEngage Identity Provider

Wraps DELETE /api/v2/identityproviders/pureengage 

Requires ANY permissions: 

* sso:provider:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Delete PureEngage Identity Provider
    api_response = api_instance.delete_identityproviders_pureengage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->delete_identityproviders_pureengage: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

**object**


## delete_identityproviders_salesforce

> object** delete_identityproviders_salesforce()


Delete Salesforce Identity Provider

Wraps DELETE /api/v2/identityproviders/salesforce 

Requires ANY permissions: 

* sso:provider:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Delete Salesforce Identity Provider
    api_response = api_instance.delete_identityproviders_salesforce()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->delete_identityproviders_salesforce: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

**object**


## get_identityprovider

> [**CustomProvider**](CustomProvider) get_identityprovider(provider_id)


Get Identity Provider

Wraps GET /api/v2/identityproviders/{providerId} 

Requires ANY permissions: 

* sso:provider:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
provider_id = 'provider_id_example' # str | Provider ID

try:
    # Get Identity Provider
    api_response = api_instance.get_identityprovider(provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identityprovider: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **provider_id** | **str**| Provider ID |  |

### Return type

[**CustomProvider**](CustomProvider)


## get_identityproviders

> [**IdentityProviderEntityListing**](IdentityProviderEntityListing) get_identityproviders()


The list of identity providers

Wraps GET /api/v2/identityproviders 

Requires ANY permissions: 

* sso:provider:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # The list of identity providers
    api_response = api_instance.get_identityproviders()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identityproviders: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**IdentityProviderEntityListing**](IdentityProviderEntityListing)


## get_identityproviders_adfs

> [**ADFS**](ADFS) get_identityproviders_adfs()


Get ADFS Identity Provider

Wraps GET /api/v2/identityproviders/adfs 

Requires ANY permissions: 

* sso:provider:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Get ADFS Identity Provider
    api_response = api_instance.get_identityproviders_adfs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identityproviders_adfs: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**ADFS**](ADFS)


## get_identityproviders_cic

> [**CustomerInteractionCenter**](CustomerInteractionCenter) get_identityproviders_cic()


Get Customer Interaction Center (CIC) Identity Provider

Wraps GET /api/v2/identityproviders/cic 

Requires ANY permissions: 

* sso:provider:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Get Customer Interaction Center (CIC) Identity Provider
    api_response = api_instance.get_identityproviders_cic()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identityproviders_cic: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**CustomerInteractionCenter**](CustomerInteractionCenter)


## get_identityproviders_generic

> [**GenericSAML**](GenericSAML) get_identityproviders_generic()


Get Generic SAML Identity Provider

Wraps GET /api/v2/identityproviders/generic 

Requires ANY permissions: 

* sso:provider:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Get Generic SAML Identity Provider
    api_response = api_instance.get_identityproviders_generic()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identityproviders_generic: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**GenericSAML**](GenericSAML)


## get_identityproviders_gsuite

> [**GSuite**](GSuite) get_identityproviders_gsuite()


Get G Suite Identity Provider

Wraps GET /api/v2/identityproviders/gsuite 

Requires ANY permissions: 

* sso:provider:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Get G Suite Identity Provider
    api_response = api_instance.get_identityproviders_gsuite()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identityproviders_gsuite: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**GSuite**](GSuite)


## get_identityproviders_identitynow

> [**IdentityNow**](IdentityNow) get_identityproviders_identitynow()


Get IdentityNow Provider

Wraps GET /api/v2/identityproviders/identitynow 

Requires ANY permissions: 

* sso:provider:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Get IdentityNow Provider
    api_response = api_instance.get_identityproviders_identitynow()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identityproviders_identitynow: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**IdentityNow**](IdentityNow)


## get_identityproviders_okta

> [**Okta**](Okta) get_identityproviders_okta()


Get Okta Identity Provider

Wraps GET /api/v2/identityproviders/okta 

Requires ANY permissions: 

* sso:provider:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Get Okta Identity Provider
    api_response = api_instance.get_identityproviders_okta()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identityproviders_okta: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**Okta**](Okta)


## get_identityproviders_onelogin

> [**OneLogin**](OneLogin) get_identityproviders_onelogin()


Get OneLogin Identity Provider

Wraps GET /api/v2/identityproviders/onelogin 

Requires ANY permissions: 

* sso:provider:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Get OneLogin Identity Provider
    api_response = api_instance.get_identityproviders_onelogin()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identityproviders_onelogin: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**OneLogin**](OneLogin)


## get_identityproviders_ping

> [**PingIdentity**](PingIdentity) get_identityproviders_ping()


Get Ping Identity Provider

Wraps GET /api/v2/identityproviders/ping 

Requires ANY permissions: 

* sso:provider:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Get Ping Identity Provider
    api_response = api_instance.get_identityproviders_ping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identityproviders_ping: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**PingIdentity**](PingIdentity)


## get_identityproviders_purecloud

> [**PureCloud**](PureCloud) get_identityproviders_purecloud()


Get PureCloud Identity Provider

Wraps GET /api/v2/identityproviders/purecloud 

Requires ANY permissions: 

* sso:provider:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Get PureCloud Identity Provider
    api_response = api_instance.get_identityproviders_purecloud()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identityproviders_purecloud: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**PureCloud**](PureCloud)


## get_identityproviders_pureengage

> [**PureEngage**](PureEngage) get_identityproviders_pureengage()


Get PureEngage Identity Provider

Wraps GET /api/v2/identityproviders/pureengage 

Requires ANY permissions: 

* sso:provider:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Get PureEngage Identity Provider
    api_response = api_instance.get_identityproviders_pureengage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identityproviders_pureengage: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**PureEngage**](PureEngage)


## get_identityproviders_salesforce

> [**Salesforce**](Salesforce) get_identityproviders_salesforce()


Get Salesforce Identity Provider

Wraps GET /api/v2/identityproviders/salesforce 

Requires ANY permissions: 

* sso:provider:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()

try:
    # Get Salesforce Identity Provider
    api_response = api_instance.get_identityproviders_salesforce()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identityproviders_salesforce: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**Salesforce**](Salesforce)


## post_identityproviders

> [**CustomProvider**](CustomProvider) post_identityproviders(body)


Create Identity Provider

Wraps POST /api/v2/identityproviders 

Requires ANY permissions: 

* sso:provider:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
body = PureCloudPlatformClientV2.CustomProvider() # CustomProvider | Provider

try:
    # Create Identity Provider
    api_response = api_instance.post_identityproviders(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->post_identityproviders: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CustomProvider**](CustomProvider)| Provider |  |

### Return type

[**CustomProvider**](CustomProvider)


## put_identityprovider

> [**CustomProvider**](CustomProvider) put_identityprovider(provider_id, body)


Update Identity Provider

Wraps PUT /api/v2/identityproviders/{providerId} 

Requires ANY permissions: 

* sso:provider:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
provider_id = 'provider_id_example' # str | Provider ID
body = PureCloudPlatformClientV2.CustomProvider() # CustomProvider | Provider

try:
    # Update Identity Provider
    api_response = api_instance.put_identityprovider(provider_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->put_identityprovider: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **provider_id** | **str**| Provider ID |  |
| **body** | [**CustomProvider**](CustomProvider)| Provider |  |

### Return type

[**CustomProvider**](CustomProvider)


## put_identityproviders_adfs

> [**IdentityProvider**](IdentityProvider) put_identityproviders_adfs(body)


Update/Create ADFS Identity Provider

Wraps PUT /api/v2/identityproviders/adfs 

Requires ANY permissions: 

* sso:provider:add
* sso:provider:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
body = PureCloudPlatformClientV2.ADFS() # ADFS | Provider

try:
    # Update/Create ADFS Identity Provider
    api_response = api_instance.put_identityproviders_adfs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->put_identityproviders_adfs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ADFS**](ADFS)| Provider |  |

### Return type

[**IdentityProvider**](IdentityProvider)


## put_identityproviders_cic

> [**IdentityProvider**](IdentityProvider) put_identityproviders_cic(body)


Update/Create Customer Interaction Center (CIC) Identity Provider

Wraps PUT /api/v2/identityproviders/cic 

Requires ANY permissions: 

* sso:provider:add
* sso:provider:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
body = PureCloudPlatformClientV2.CustomerInteractionCenter() # CustomerInteractionCenter | Provider

try:
    # Update/Create Customer Interaction Center (CIC) Identity Provider
    api_response = api_instance.put_identityproviders_cic(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->put_identityproviders_cic: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CustomerInteractionCenter**](CustomerInteractionCenter)| Provider |  |

### Return type

[**IdentityProvider**](IdentityProvider)


## put_identityproviders_generic

> [**IdentityProvider**](IdentityProvider) put_identityproviders_generic(body)


Update/Create Generic SAML Identity Provider

Wraps PUT /api/v2/identityproviders/generic 

Requires ANY permissions: 

* sso:provider:add
* sso:provider:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
body = PureCloudPlatformClientV2.GenericSAML() # GenericSAML | Provider

try:
    # Update/Create Generic SAML Identity Provider
    api_response = api_instance.put_identityproviders_generic(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->put_identityproviders_generic: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GenericSAML**](GenericSAML)| Provider |  |

### Return type

[**IdentityProvider**](IdentityProvider)


## put_identityproviders_gsuite

> [**IdentityProvider**](IdentityProvider) put_identityproviders_gsuite(body)


Update/Create G Suite Identity Provider

Wraps PUT /api/v2/identityproviders/gsuite 

Requires ANY permissions: 

* sso:provider:add
* sso:provider:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
body = PureCloudPlatformClientV2.GSuite() # GSuite | Provider

try:
    # Update/Create G Suite Identity Provider
    api_response = api_instance.put_identityproviders_gsuite(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->put_identityproviders_gsuite: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GSuite**](GSuite)| Provider |  |

### Return type

[**IdentityProvider**](IdentityProvider)


## put_identityproviders_identitynow

> [**IdentityNow**](IdentityNow) put_identityproviders_identitynow(body)


Update/Create IdentityNow Provider

Wraps PUT /api/v2/identityproviders/identitynow 

Requires ANY permissions: 

* sso:provider:add
* sso:provider:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
body = PureCloudPlatformClientV2.IdentityNow() # IdentityNow | Provider

try:
    # Update/Create IdentityNow Provider
    api_response = api_instance.put_identityproviders_identitynow(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->put_identityproviders_identitynow: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**IdentityNow**](IdentityNow)| Provider |  |

### Return type

[**IdentityNow**](IdentityNow)


## put_identityproviders_okta

> [**IdentityProvider**](IdentityProvider) put_identityproviders_okta(body)


Update/Create Okta Identity Provider

Wraps PUT /api/v2/identityproviders/okta 

Requires ANY permissions: 

* sso:provider:add
* sso:provider:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
body = PureCloudPlatformClientV2.Okta() # Okta | Provider

try:
    # Update/Create Okta Identity Provider
    api_response = api_instance.put_identityproviders_okta(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->put_identityproviders_okta: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Okta**](Okta)| Provider |  |

### Return type

[**IdentityProvider**](IdentityProvider)


## put_identityproviders_onelogin

> [**IdentityProvider**](IdentityProvider) put_identityproviders_onelogin(body)


Update/Create OneLogin Identity Provider

Wraps PUT /api/v2/identityproviders/onelogin 

Requires ANY permissions: 

* sso:provider:add
* sso:provider:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
body = PureCloudPlatformClientV2.OneLogin() # OneLogin | Provider

try:
    # Update/Create OneLogin Identity Provider
    api_response = api_instance.put_identityproviders_onelogin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->put_identityproviders_onelogin: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OneLogin**](OneLogin)| Provider |  |

### Return type

[**IdentityProvider**](IdentityProvider)


## put_identityproviders_ping

> [**IdentityProvider**](IdentityProvider) put_identityproviders_ping(body)


Update/Create Ping Identity Provider

Wraps PUT /api/v2/identityproviders/ping 

Requires ANY permissions: 

* sso:provider:add
* sso:provider:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
body = PureCloudPlatformClientV2.PingIdentity() # PingIdentity | Provider

try:
    # Update/Create Ping Identity Provider
    api_response = api_instance.put_identityproviders_ping(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->put_identityproviders_ping: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PingIdentity**](PingIdentity)| Provider |  |

### Return type

[**IdentityProvider**](IdentityProvider)


## put_identityproviders_purecloud

> [**IdentityProvider**](IdentityProvider) put_identityproviders_purecloud(body)


Update/Create PureCloud Identity Provider

Wraps PUT /api/v2/identityproviders/purecloud 

Requires ANY permissions: 

* sso:provider:add
* sso:provider:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
body = PureCloudPlatformClientV2.PureCloud() # PureCloud | Provider

try:
    # Update/Create PureCloud Identity Provider
    api_response = api_instance.put_identityproviders_purecloud(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->put_identityproviders_purecloud: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PureCloud**](PureCloud)| Provider |  |

### Return type

[**IdentityProvider**](IdentityProvider)


## put_identityproviders_pureengage

> [**IdentityProvider**](IdentityProvider) put_identityproviders_pureengage(body)


Update/Create PureEngage Identity Provider

Wraps PUT /api/v2/identityproviders/pureengage 

Requires ANY permissions: 

* sso:provider:add
* sso:provider:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
body = PureCloudPlatformClientV2.PureEngage() # PureEngage | Provider

try:
    # Update/Create PureEngage Identity Provider
    api_response = api_instance.put_identityproviders_pureengage(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->put_identityproviders_pureengage: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PureEngage**](PureEngage)| Provider |  |

### Return type

[**IdentityProvider**](IdentityProvider)


## put_identityproviders_salesforce

> [**IdentityProvider**](IdentityProvider) put_identityproviders_salesforce(body)


Update/Create Salesforce Identity Provider

Wraps PUT /api/v2/identityproviders/salesforce 

Requires ANY permissions: 

* sso:provider:add
* sso:provider:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.IdentityProviderApi()
body = PureCloudPlatformClientV2.Salesforce() # Salesforce | Provider

try:
    # Update/Create Salesforce Identity Provider
    api_response = api_instance.put_identityproviders_salesforce(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->put_identityproviders_salesforce: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Salesforce**](Salesforce)| Provider |  |

### Return type

[**IdentityProvider**](IdentityProvider)


_PureCloudPlatformClientV2 248.0.0_

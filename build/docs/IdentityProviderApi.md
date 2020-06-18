---
title: IdentityProviderApi
---

## PureCloudPlatformClientV2.IdentityProviderApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_identityproviders_adfs**](IdentityProviderApi.html#delete_identityproviders_adfs) | Delete ADFS Identity Provider|
|[**delete_identityproviders_cic**](IdentityProviderApi.html#delete_identityproviders_cic) | Delete Customer Interaction Center (CIC) Identity Provider|
|[**delete_identityproviders_generic**](IdentityProviderApi.html#delete_identityproviders_generic) | Delete Generic SAML Identity Provider|
|[**delete_identityproviders_gsuite**](IdentityProviderApi.html#delete_identityproviders_gsuite) | Delete G Suite Identity Provider|
|[**delete_identityproviders_identitynow**](IdentityProviderApi.html#delete_identityproviders_identitynow) | Delete IdentityNow Provider|
|[**delete_identityproviders_okta**](IdentityProviderApi.html#delete_identityproviders_okta) | Delete Okta Identity Provider|
|[**delete_identityproviders_onelogin**](IdentityProviderApi.html#delete_identityproviders_onelogin) | Delete OneLogin Identity Provider|
|[**delete_identityproviders_ping**](IdentityProviderApi.html#delete_identityproviders_ping) | Delete Ping Identity Provider|
|[**delete_identityproviders_purecloud**](IdentityProviderApi.html#delete_identityproviders_purecloud) | Delete PureCloud Identity Provider|
|[**delete_identityproviders_pureengage**](IdentityProviderApi.html#delete_identityproviders_pureengage) | Delete PureEngage Identity Provider|
|[**delete_identityproviders_salesforce**](IdentityProviderApi.html#delete_identityproviders_salesforce) | Delete Salesforce Identity Provider|
|[**get_identityproviders**](IdentityProviderApi.html#get_identityproviders) | The list of identity providers|
|[**get_identityproviders_adfs**](IdentityProviderApi.html#get_identityproviders_adfs) | Get ADFS Identity Provider|
|[**get_identityproviders_cic**](IdentityProviderApi.html#get_identityproviders_cic) | Get Customer Interaction Center (CIC) Identity Provider|
|[**get_identityproviders_generic**](IdentityProviderApi.html#get_identityproviders_generic) | Get Generic SAML Identity Provider|
|[**get_identityproviders_gsuite**](IdentityProviderApi.html#get_identityproviders_gsuite) | Get G Suite Identity Provider|
|[**get_identityproviders_identitynow**](IdentityProviderApi.html#get_identityproviders_identitynow) | Get IdentityNow Provider|
|[**get_identityproviders_okta**](IdentityProviderApi.html#get_identityproviders_okta) | Get Okta Identity Provider|
|[**get_identityproviders_onelogin**](IdentityProviderApi.html#get_identityproviders_onelogin) | Get OneLogin Identity Provider|
|[**get_identityproviders_ping**](IdentityProviderApi.html#get_identityproviders_ping) | Get Ping Identity Provider|
|[**get_identityproviders_purecloud**](IdentityProviderApi.html#get_identityproviders_purecloud) | Get PureCloud Identity Provider|
|[**get_identityproviders_pureengage**](IdentityProviderApi.html#get_identityproviders_pureengage) | Get PureEngage Identity Provider|
|[**get_identityproviders_salesforce**](IdentityProviderApi.html#get_identityproviders_salesforce) | Get Salesforce Identity Provider|
|[**put_identityproviders_adfs**](IdentityProviderApi.html#put_identityproviders_adfs) | Update/Create ADFS Identity Provider|
|[**put_identityproviders_cic**](IdentityProviderApi.html#put_identityproviders_cic) | Update/Create Customer Interaction Center (CIC) Identity Provider|
|[**put_identityproviders_generic**](IdentityProviderApi.html#put_identityproviders_generic) | Update/Create Generic SAML Identity Provider|
|[**put_identityproviders_gsuite**](IdentityProviderApi.html#put_identityproviders_gsuite) | Update/Create G Suite Identity Provider|
|[**put_identityproviders_identitynow**](IdentityProviderApi.html#put_identityproviders_identitynow) | Update/Create IdentityNow Provider|
|[**put_identityproviders_okta**](IdentityProviderApi.html#put_identityproviders_okta) | Update/Create Okta Identity Provider|
|[**put_identityproviders_onelogin**](IdentityProviderApi.html#put_identityproviders_onelogin) | Update/Create OneLogin Identity Provider|
|[**put_identityproviders_ping**](IdentityProviderApi.html#put_identityproviders_ping) | Update/Create Ping Identity Provider|
|[**put_identityproviders_purecloud**](IdentityProviderApi.html#put_identityproviders_purecloud) | Update/Create PureCloud Identity Provider|
|[**put_identityproviders_pureengage**](IdentityProviderApi.html#put_identityproviders_pureengage) | Update/Create PureEngage Identity Provider|
|[**put_identityproviders_salesforce**](IdentityProviderApi.html#put_identityproviders_salesforce) | Update/Create Salesforce Identity Provider|
{: class="table table-striped"}

<a name="delete_identityproviders_adfs"></a>

## [**Empty**](Empty.html) delete_identityproviders_adfs()



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
    print "Exception when calling IdentityProviderApi->delete_identityproviders_adfs: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="delete_identityproviders_cic"></a>

## [**Empty**](Empty.html) delete_identityproviders_cic()



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
    print "Exception when calling IdentityProviderApi->delete_identityproviders_cic: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="delete_identityproviders_generic"></a>

## [**Empty**](Empty.html) delete_identityproviders_generic()



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
    print "Exception when calling IdentityProviderApi->delete_identityproviders_generic: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="delete_identityproviders_gsuite"></a>

## [**Empty**](Empty.html) delete_identityproviders_gsuite()



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
    print "Exception when calling IdentityProviderApi->delete_identityproviders_gsuite: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="delete_identityproviders_identitynow"></a>

## [**Empty**](Empty.html) delete_identityproviders_identitynow()



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
    print "Exception when calling IdentityProviderApi->delete_identityproviders_identitynow: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="delete_identityproviders_okta"></a>

## [**Empty**](Empty.html) delete_identityproviders_okta()



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
    print "Exception when calling IdentityProviderApi->delete_identityproviders_okta: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="delete_identityproviders_onelogin"></a>

## [**Empty**](Empty.html) delete_identityproviders_onelogin()



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
    print "Exception when calling IdentityProviderApi->delete_identityproviders_onelogin: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="delete_identityproviders_ping"></a>

## [**Empty**](Empty.html) delete_identityproviders_ping()



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
    print "Exception when calling IdentityProviderApi->delete_identityproviders_ping: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="delete_identityproviders_purecloud"></a>

## [**Empty**](Empty.html) delete_identityproviders_purecloud()



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
    print "Exception when calling IdentityProviderApi->delete_identityproviders_purecloud: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="delete_identityproviders_pureengage"></a>

## [**Empty**](Empty.html) delete_identityproviders_pureengage()



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
    print "Exception when calling IdentityProviderApi->delete_identityproviders_pureengage: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="delete_identityproviders_salesforce"></a>

## [**Empty**](Empty.html) delete_identityproviders_salesforce()



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
    print "Exception when calling IdentityProviderApi->delete_identityproviders_salesforce: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="get_identityproviders"></a>

## [**OAuthProviderEntityListing**](OAuthProviderEntityListing.html) get_identityproviders()



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
    print "Exception when calling IdentityProviderApi->get_identityproviders: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**OAuthProviderEntityListing**](OAuthProviderEntityListing.html)

<a name="get_identityproviders_adfs"></a>

## [**ADFS**](ADFS.html) get_identityproviders_adfs()



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
    print "Exception when calling IdentityProviderApi->get_identityproviders_adfs: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**ADFS**](ADFS.html)

<a name="get_identityproviders_cic"></a>

## [**CustomerInteractionCenter**](CustomerInteractionCenter.html) get_identityproviders_cic()



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
    print "Exception when calling IdentityProviderApi->get_identityproviders_cic: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**CustomerInteractionCenter**](CustomerInteractionCenter.html)

<a name="get_identityproviders_generic"></a>

## [**GenericSAML**](GenericSAML.html) get_identityproviders_generic()



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
    print "Exception when calling IdentityProviderApi->get_identityproviders_generic: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**GenericSAML**](GenericSAML.html)

<a name="get_identityproviders_gsuite"></a>

## [**GSuite**](GSuite.html) get_identityproviders_gsuite()



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
    print "Exception when calling IdentityProviderApi->get_identityproviders_gsuite: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**GSuite**](GSuite.html)

<a name="get_identityproviders_identitynow"></a>

## [**IdentityNow**](IdentityNow.html) get_identityproviders_identitynow()



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
    print "Exception when calling IdentityProviderApi->get_identityproviders_identitynow: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**IdentityNow**](IdentityNow.html)

<a name="get_identityproviders_okta"></a>

## [**Okta**](Okta.html) get_identityproviders_okta()



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
    print "Exception when calling IdentityProviderApi->get_identityproviders_okta: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Okta**](Okta.html)

<a name="get_identityproviders_onelogin"></a>

## [**OneLogin**](OneLogin.html) get_identityproviders_onelogin()



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
    print "Exception when calling IdentityProviderApi->get_identityproviders_onelogin: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**OneLogin**](OneLogin.html)

<a name="get_identityproviders_ping"></a>

## [**PingIdentity**](PingIdentity.html) get_identityproviders_ping()



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
    print "Exception when calling IdentityProviderApi->get_identityproviders_ping: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**PingIdentity**](PingIdentity.html)

<a name="get_identityproviders_purecloud"></a>

## [**PureCloud**](PureCloud.html) get_identityproviders_purecloud()



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
    print "Exception when calling IdentityProviderApi->get_identityproviders_purecloud: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**PureCloud**](PureCloud.html)

<a name="get_identityproviders_pureengage"></a>

## [**PureEngage**](PureEngage.html) get_identityproviders_pureengage()



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
    print "Exception when calling IdentityProviderApi->get_identityproviders_pureengage: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**PureEngage**](PureEngage.html)

<a name="get_identityproviders_salesforce"></a>

## [**Salesforce**](Salesforce.html) get_identityproviders_salesforce()



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
    print "Exception when calling IdentityProviderApi->get_identityproviders_salesforce: %s\n" % e
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Salesforce**](Salesforce.html)

<a name="put_identityproviders_adfs"></a>

## [**OAuthProvider**](OAuthProvider.html) put_identityproviders_adfs(body)



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
    print "Exception when calling IdentityProviderApi->put_identityproviders_adfs: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ADFS**](ADFS.html)| Provider |  |
{: class="table table-striped"}

### Return type

[**OAuthProvider**](OAuthProvider.html)

<a name="put_identityproviders_cic"></a>

## [**OAuthProvider**](OAuthProvider.html) put_identityproviders_cic(body)



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
    print "Exception when calling IdentityProviderApi->put_identityproviders_cic: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CustomerInteractionCenter**](CustomerInteractionCenter.html)| Provider |  |
{: class="table table-striped"}

### Return type

[**OAuthProvider**](OAuthProvider.html)

<a name="put_identityproviders_generic"></a>

## [**OAuthProvider**](OAuthProvider.html) put_identityproviders_generic(body)



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
    print "Exception when calling IdentityProviderApi->put_identityproviders_generic: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GenericSAML**](GenericSAML.html)| Provider |  |
{: class="table table-striped"}

### Return type

[**OAuthProvider**](OAuthProvider.html)

<a name="put_identityproviders_gsuite"></a>

## [**OAuthProvider**](OAuthProvider.html) put_identityproviders_gsuite(body)



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
    print "Exception when calling IdentityProviderApi->put_identityproviders_gsuite: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GSuite**](GSuite.html)| Provider |  |
{: class="table table-striped"}

### Return type

[**OAuthProvider**](OAuthProvider.html)

<a name="put_identityproviders_identitynow"></a>

## [**IdentityNow**](IdentityNow.html) put_identityproviders_identitynow(body)



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
    print "Exception when calling IdentityProviderApi->put_identityproviders_identitynow: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**IdentityNow**](IdentityNow.html)| Provider |  |
{: class="table table-striped"}

### Return type

[**IdentityNow**](IdentityNow.html)

<a name="put_identityproviders_okta"></a>

## [**OAuthProvider**](OAuthProvider.html) put_identityproviders_okta(body)



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
    print "Exception when calling IdentityProviderApi->put_identityproviders_okta: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Okta**](Okta.html)| Provider |  |
{: class="table table-striped"}

### Return type

[**OAuthProvider**](OAuthProvider.html)

<a name="put_identityproviders_onelogin"></a>

## [**OAuthProvider**](OAuthProvider.html) put_identityproviders_onelogin(body)



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
    print "Exception when calling IdentityProviderApi->put_identityproviders_onelogin: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OneLogin**](OneLogin.html)| Provider |  |
{: class="table table-striped"}

### Return type

[**OAuthProvider**](OAuthProvider.html)

<a name="put_identityproviders_ping"></a>

## [**OAuthProvider**](OAuthProvider.html) put_identityproviders_ping(body)



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
    print "Exception when calling IdentityProviderApi->put_identityproviders_ping: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PingIdentity**](PingIdentity.html)| Provider |  |
{: class="table table-striped"}

### Return type

[**OAuthProvider**](OAuthProvider.html)

<a name="put_identityproviders_purecloud"></a>

## [**OAuthProvider**](OAuthProvider.html) put_identityproviders_purecloud(body)



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
    print "Exception when calling IdentityProviderApi->put_identityproviders_purecloud: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PureCloud**](PureCloud.html)| Provider |  |
{: class="table table-striped"}

### Return type

[**OAuthProvider**](OAuthProvider.html)

<a name="put_identityproviders_pureengage"></a>

## [**OAuthProvider**](OAuthProvider.html) put_identityproviders_pureengage(body)



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
    print "Exception when calling IdentityProviderApi->put_identityproviders_pureengage: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PureEngage**](PureEngage.html)| Provider |  |
{: class="table table-striped"}

### Return type

[**OAuthProvider**](OAuthProvider.html)

<a name="put_identityproviders_salesforce"></a>

## [**OAuthProvider**](OAuthProvider.html) put_identityproviders_salesforce(body)



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
    print "Exception when calling IdentityProviderApi->put_identityproviders_salesforce: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Salesforce**](Salesforce.html)| Provider |  |
{: class="table table-striped"}

### Return type

[**OAuthProvider**](OAuthProvider.html)


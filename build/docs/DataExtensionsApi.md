# DataExtensionsApi

## PureCloudPlatformClientV2.DataExtensionsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_dataextensions_coretype**](#get_dataextensions_coretype) | Get a specific named core type.|
|[**get_dataextensions_coretypes**](#get_dataextensions_coretypes) | Get the core types from which all schemas are built.|
|[**get_dataextensions_limits**](#get_dataextensions_limits) | Get quantitative limits on schemas|



## get_dataextensions_coretype

> [**Coretype**](Coretype) get_dataextensions_coretype(coretype_name)


Get a specific named core type.

Wraps GET /api/v2/dataextensions/coretypes/{coretypeName} 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.DataExtensionsApi()
coretype_name = 'coretype_name_example' # str | The core type's name

try:
    # Get a specific named core type.
    api_response = api_instance.get_dataextensions_coretype(coretype_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExtensionsApi->get_dataextensions_coretype: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **coretype_name** | **str**| The core type&#39;s name | <br />**Values**: text, longtext, url, identifier, enum, date, datetime, integer, number, checkbox, tag |

### Return type

[**Coretype**](Coretype)


## get_dataextensions_coretypes

> [**CoretypeListing**](CoretypeListing) get_dataextensions_coretypes()


Get the core types from which all schemas are built.

Wraps GET /api/v2/dataextensions/coretypes 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.DataExtensionsApi()

try:
    # Get the core types from which all schemas are built.
    api_response = api_instance.get_dataextensions_coretypes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExtensionsApi->get_dataextensions_coretypes: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**CoretypeListing**](CoretypeListing)


## get_dataextensions_limits

> [**SchemaQuantityLimits**](SchemaQuantityLimits) get_dataextensions_limits()


Get quantitative limits on schemas

Wraps GET /api/v2/dataextensions/limits 

Requires ANY permissions: 

* externalContacts:customFields:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.DataExtensionsApi()

try:
    # Get quantitative limits on schemas
    api_response = api_instance.get_dataextensions_limits()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExtensionsApi->get_dataextensions_limits: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**SchemaQuantityLimits**](SchemaQuantityLimits)


_PureCloudPlatformClientV2 242.0.0_

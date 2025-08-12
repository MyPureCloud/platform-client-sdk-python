# ResponseManagementApi

## PureCloudPlatformClientV2.ResponseManagementApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_responsemanagement_library**](#delete_responsemanagement_library) | Delete an existing response library.|
|[**delete_responsemanagement_response**](#delete_responsemanagement_response) | Delete an existing response.|
|[**delete_responsemanagement_responseasset**](#delete_responsemanagement_responseasset) | Delete response asset|
|[**get_responsemanagement_libraries**](#get_responsemanagement_libraries) | Gets a list of existing response libraries.|
|[**get_responsemanagement_library**](#get_responsemanagement_library) | Get details about an existing response library.|
|[**get_responsemanagement_response**](#get_responsemanagement_response) | Get details about an existing response.|
|[**get_responsemanagement_responseasset**](#get_responsemanagement_responseasset) | Get response asset information|
|[**get_responsemanagement_responseassets_status_status_id**](#get_responsemanagement_responseassets_status_status_id) | Get response asset upload status|
|[**get_responsemanagement_responses**](#get_responsemanagement_responses) | Gets a list of existing responses.|
|[**post_responsemanagement_libraries**](#post_responsemanagement_libraries) | Create a response library.|
|[**post_responsemanagement_libraries_bulk**](#post_responsemanagement_libraries_bulk) | Get response libraries.|
|[**post_responsemanagement_responseassets_search**](#post_responsemanagement_responseassets_search) | Search response assets|
|[**post_responsemanagement_responseassets_uploads**](#post_responsemanagement_responseassets_uploads) | Creates pre-signed url for uploading response asset|
|[**post_responsemanagement_responses**](#post_responsemanagement_responses) | Create a response.|
|[**post_responsemanagement_responses_query**](#post_responsemanagement_responses_query) | Query responses|
|[**put_responsemanagement_library**](#put_responsemanagement_library) | Update an existing response library.|
|[**put_responsemanagement_response**](#put_responsemanagement_response) | Update an existing response.|
|[**put_responsemanagement_responseasset**](#put_responsemanagement_responseasset) | Update response asset|



## delete_responsemanagement_library

>  delete_responsemanagement_library(library_id)


Delete an existing response library.

This will remove any responses associated with the library.

Wraps DELETE /api/v2/responsemanagement/libraries/{libraryId} 

Requires ANY permissions: 

* responses:library:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
library_id = 'library_id_example' # str | Library ID

try:
    # Delete an existing response library.
    api_instance.delete_responsemanagement_library(library_id)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->delete_responsemanagement_library: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **library_id** | **str**| Library ID |  |

### Return type

void (empty response body)


## delete_responsemanagement_response

>  delete_responsemanagement_response(response_id)


Delete an existing response.

This will remove the response from any libraries associated with it.

Wraps DELETE /api/v2/responsemanagement/responses/{responseId} 

Requires ANY permissions: 

* responses:response:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
response_id = 'response_id_example' # str | Response ID

try:
    # Delete an existing response.
    api_instance.delete_responsemanagement_response(response_id)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->delete_responsemanagement_response: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **response_id** | **str**| Response ID |  |

### Return type

void (empty response body)


## delete_responsemanagement_responseasset

>  delete_responsemanagement_responseasset(response_asset_id)


Delete response asset

Wraps DELETE /api/v2/responsemanagement/responseassets/{responseAssetId} 

Requires ANY permissions: 

* responseAssets:asset:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
response_asset_id = 'response_asset_id_example' # str | Asset Id

try:
    # Delete response asset
    api_instance.delete_responsemanagement_responseasset(response_asset_id)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->delete_responsemanagement_responseasset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **response_asset_id** | **str**| Asset Id |  |

### Return type

void (empty response body)


## get_responsemanagement_libraries

> [**LibraryEntityListing**](LibraryEntityListing) get_responsemanagement_libraries(page_number=page_number, page_size=page_size, messaging_template_filter=messaging_template_filter, library_prefix=library_prefix)


Gets a list of existing response libraries.

Wraps GET /api/v2/responsemanagement/libraries 

Requires ANY permissions: 

* responses:library:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
messaging_template_filter = 'messaging_template_filter_example' # str | Returns a list of libraries that contain responses with at least one messaging template defined for a specific message channel (optional)
library_prefix = 'library_prefix_example' # str | Returns a list of libraries that contain the prefix provided (optional)

try:
    # Gets a list of existing response libraries.
    api_response = api_instance.get_responsemanagement_libraries(page_number=page_number, page_size=page_size, messaging_template_filter=messaging_template_filter, library_prefix=library_prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->get_responsemanagement_libraries: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **messaging_template_filter** | **str**| Returns a list of libraries that contain responses with at least one messaging template defined for a specific message channel | [optional] <br />**Values**: whatsapp |
| **library_prefix** | **str**| Returns a list of libraries that contain the prefix provided | [optional]  |

### Return type

[**LibraryEntityListing**](LibraryEntityListing)


## get_responsemanagement_library

> [**Library**](Library) get_responsemanagement_library(library_id)


Get details about an existing response library.

Wraps GET /api/v2/responsemanagement/libraries/{libraryId} 

Requires ANY permissions: 

* responses:library:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
library_id = 'library_id_example' # str | Library ID

try:
    # Get details about an existing response library.
    api_response = api_instance.get_responsemanagement_library(library_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->get_responsemanagement_library: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **library_id** | **str**| Library ID |  |

### Return type

[**Library**](Library)


## get_responsemanagement_response

> [**Response**](Response) get_responsemanagement_response(response_id, expand=expand)


Get details about an existing response.

Wraps GET /api/v2/responsemanagement/responses/{responseId} 

Requires ANY permissions: 

* responses:response:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
response_id = 'response_id_example' # str | Response ID
expand = 'expand_example' # str | Expand instructions for the return value. (optional)

try:
    # Get details about an existing response.
    api_response = api_instance.get_responsemanagement_response(response_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->get_responsemanagement_response: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **response_id** | **str**| Response ID |  |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: substitutionsSchema |

### Return type

[**Response**](Response)


## get_responsemanagement_responseasset

> [**ResponseAsset**](ResponseAsset) get_responsemanagement_responseasset(response_asset_id)


Get response asset information

Wraps GET /api/v2/responsemanagement/responseassets/{responseAssetId} 

Requires ANY permissions: 

* responseAssets:asset:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
response_asset_id = 'response_asset_id_example' # str | Asset Id

try:
    # Get response asset information
    api_response = api_instance.get_responsemanagement_responseasset(response_asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->get_responsemanagement_responseasset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **response_asset_id** | **str**| Asset Id |  |

### Return type

[**ResponseAsset**](ResponseAsset)


## get_responsemanagement_responseassets_status_status_id

> [**ResponseAssetStatus**](ResponseAssetStatus) get_responsemanagement_responseassets_status_status_id(status_id)


Get response asset upload status

Wraps GET /api/v2/responsemanagement/responseassets/status/{statusId} 

Requires ANY permissions: 

* responseAssets:asset:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
status_id = 'status_id_example' # str | Status Id

try:
    # Get response asset upload status
    api_response = api_instance.get_responsemanagement_responseassets_status_status_id(status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->get_responsemanagement_responseassets_status_status_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **status_id** | **str**| Status Id |  |

### Return type

[**ResponseAssetStatus**](ResponseAssetStatus)


## get_responsemanagement_responses

> [**ResponseEntityListing**](ResponseEntityListing) get_responsemanagement_responses(library_id, page_number=page_number, page_size=page_size, expand=expand)


Gets a list of existing responses.

Wraps GET /api/v2/responsemanagement/responses 

Requires ANY permissions: 

* responses:response:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
library_id = 'library_id_example' # str | Library ID
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
expand = 'expand_example' # str | Expand instructions for the return value. (optional)

try:
    # Gets a list of existing responses.
    api_response = api_instance.get_responsemanagement_responses(library_id, page_number=page_number, page_size=page_size, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->get_responsemanagement_responses: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **library_id** | **str**| Library ID |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: substitutionsSchema |

### Return type

[**ResponseEntityListing**](ResponseEntityListing)


## post_responsemanagement_libraries

> [**Library**](Library) post_responsemanagement_libraries(body)


Create a response library.

Wraps POST /api/v2/responsemanagement/libraries 

Requires ANY permissions: 

* responses:library:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
body = PureCloudPlatformClientV2.Library() # Library | Library

try:
    # Create a response library.
    api_response = api_instance.post_responsemanagement_libraries(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->post_responsemanagement_libraries: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Library**](Library)| Library |  |

### Return type

[**Library**](Library)


## post_responsemanagement_libraries_bulk

> [**LibraryEntityListing**](LibraryEntityListing) post_responsemanagement_libraries_bulk(body)


Get response libraries.

Wraps POST /api/v2/responsemanagement/libraries/bulk 

Requires ANY permissions: 

* responses:library:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
body = PureCloudPlatformClientV2.LibraryBatchRequest() # LibraryBatchRequest | LibraryIDs (max allowed 50)

try:
    # Get response libraries.
    api_response = api_instance.post_responsemanagement_libraries_bulk(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->post_responsemanagement_libraries_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LibraryBatchRequest**](LibraryBatchRequest)| LibraryIDs (max allowed 50) |  |

### Return type

[**LibraryEntityListing**](LibraryEntityListing)


## post_responsemanagement_responseassets_search

> [**ResponseAssetSearchResults**](ResponseAssetSearchResults) post_responsemanagement_responseassets_search(body, expand=expand)


Search response assets

Wraps POST /api/v2/responsemanagement/responseassets/search 

Requires ALL permissions: 

* responseAssets:asset:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
body = PureCloudPlatformClientV2.ResponseAssetSearchRequest() # ResponseAssetSearchRequest | request
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Search response assets
    api_response = api_instance.post_responsemanagement_responseassets_search(body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->post_responsemanagement_responseassets_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ResponseAssetSearchRequest**](ResponseAssetSearchRequest)| request |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: user, division |

### Return type

[**ResponseAssetSearchResults**](ResponseAssetSearchResults)


## post_responsemanagement_responseassets_uploads

> [**CreateResponseAssetResponse**](CreateResponseAssetResponse) post_responsemanagement_responseassets_uploads(body)


Creates pre-signed url for uploading response asset

Wraps POST /api/v2/responsemanagement/responseassets/uploads 

Requires ANY permissions: 

* responseAssets:asset:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
body = PureCloudPlatformClientV2.CreateResponseAssetRequest() # CreateResponseAssetRequest | request

try:
    # Creates pre-signed url for uploading response asset
    api_response = api_instance.post_responsemanagement_responseassets_uploads(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->post_responsemanagement_responseassets_uploads: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateResponseAssetRequest**](CreateResponseAssetRequest)| request |  |

### Return type

[**CreateResponseAssetResponse**](CreateResponseAssetResponse)


## post_responsemanagement_responses

> [**Response**](Response) post_responsemanagement_responses(body, expand=expand)


Create a response.

Wraps POST /api/v2/responsemanagement/responses 

Requires ANY permissions: 

* responses:response:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
body = PureCloudPlatformClientV2.Response() # Response | Response
expand = 'expand_example' # str | Expand instructions for the return value. (optional)

try:
    # Create a response.
    api_response = api_instance.post_responsemanagement_responses(body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->post_responsemanagement_responses: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Response**](Response)| Response |  |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: substitutionsSchema |

### Return type

[**Response**](Response)


## post_responsemanagement_responses_query

> [**ResponseQueryResults**](ResponseQueryResults) post_responsemanagement_responses_query(body)


Query responses

Wraps POST /api/v2/responsemanagement/responses/query 

Requires ANY permissions: 

* responses:response:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
body = PureCloudPlatformClientV2.ResponseQueryRequest() # ResponseQueryRequest | Response

try:
    # Query responses
    api_response = api_instance.post_responsemanagement_responses_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->post_responsemanagement_responses_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ResponseQueryRequest**](ResponseQueryRequest)| Response |  |

### Return type

[**ResponseQueryResults**](ResponseQueryResults)


## put_responsemanagement_library

> [**Library**](Library) put_responsemanagement_library(library_id, body)


Update an existing response library.

Fields that can be updated: name. The most recent version is required for updates.

Wraps PUT /api/v2/responsemanagement/libraries/{libraryId} 

Requires ANY permissions: 

* responses:library:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
library_id = 'library_id_example' # str | Library ID
body = PureCloudPlatformClientV2.Library() # Library | Library

try:
    # Update an existing response library.
    api_response = api_instance.put_responsemanagement_library(library_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->put_responsemanagement_library: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **library_id** | **str**| Library ID |  |
| **body** | [**Library**](Library)| Library |  |

### Return type

[**Library**](Library)


## put_responsemanagement_response

> [**Response**](Response) put_responsemanagement_response(response_id, body, expand=expand)


Update an existing response.

Fields that can be updated: name, libraries, and texts. The most recent version is required for updates.

Wraps PUT /api/v2/responsemanagement/responses/{responseId} 

Requires ANY permissions: 

* responses:response:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
response_id = 'response_id_example' # str | Response ID
body = PureCloudPlatformClientV2.Response() # Response | Response
expand = 'expand_example' # str | Expand instructions for the return value. (optional)

try:
    # Update an existing response.
    api_response = api_instance.put_responsemanagement_response(response_id, body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->put_responsemanagement_response: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **response_id** | **str**| Response ID |  |
| **body** | [**Response**](Response)| Response |  |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: substitutionsSchema |

### Return type

[**Response**](Response)


## put_responsemanagement_responseasset

> [**ResponseAsset**](ResponseAsset) put_responsemanagement_responseasset(response_asset_id, body)


Update response asset

Wraps PUT /api/v2/responsemanagement/responseassets/{responseAssetId} 

Requires ALL permissions: 

* responseAssets:asset:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
response_asset_id = 'response_asset_id_example' # str | Asset Id
body = PureCloudPlatformClientV2.ResponseAssetRequest() # ResponseAssetRequest | request

try:
    # Update response asset
    api_response = api_instance.put_responsemanagement_responseasset(response_asset_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseManagementApi->put_responsemanagement_responseasset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **response_asset_id** | **str**| Asset Id |  |
| **body** | [**ResponseAssetRequest**](ResponseAssetRequest)| request |  |

### Return type

[**ResponseAsset**](ResponseAsset)


_PureCloudPlatformClientV2 235.0.0_

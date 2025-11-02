# FaxApi

## PureCloudPlatformClientV2.FaxApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_fax_document**](#delete_fax_document) | Delete a fax document.|
|[**get_fax_document**](#get_fax_document) | Get a document.|
|[**get_fax_document_content**](#get_fax_document_content) | Download a fax document.|
|[**get_fax_documents**](#get_fax_documents) | Get a list of fax documents.|
|[**get_fax_settings**](#get_fax_settings) | Get organization config for given organization|
|[**get_fax_summary**](#get_fax_summary) | Get fax summary|
|[**put_fax_document**](#put_fax_document) | Update a fax document.|
|[**put_fax_settings**](#put_fax_settings) | Update/write organization config for given organization|



## delete_fax_document

>  delete_fax_document(document_id)


Delete a fax document.

Wraps DELETE /api/v2/fax/documents/{documentId} 

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
api_instance = PureCloudPlatformClientV2.FaxApi()
document_id = 'document_id_example' # str | Document ID

try:
    # Delete a fax document.
    api_instance.delete_fax_document(document_id)
except ApiException as e:
    print("Exception when calling FaxApi->delete_fax_document: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |

### Return type

void (empty response body)


## get_fax_document

> [**FaxDocument**](FaxDocument) get_fax_document(document_id)


Get a document.

Wraps GET /api/v2/fax/documents/{documentId} 

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
api_instance = PureCloudPlatformClientV2.FaxApi()
document_id = 'document_id_example' # str | Document ID

try:
    # Get a document.
    api_response = api_instance.get_fax_document(document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxApi->get_fax_document: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |

### Return type

[**FaxDocument**](FaxDocument)


## get_fax_document_content

> [**DownloadResponse**](DownloadResponse) get_fax_document_content(document_id)


Download a fax document.

Wraps GET /api/v2/fax/documents/{documentId}/content 

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
api_instance = PureCloudPlatformClientV2.FaxApi()
document_id = 'document_id_example' # str | Document ID

try:
    # Download a fax document.
    api_response = api_instance.get_fax_document_content(document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxApi->get_fax_document_content: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |

### Return type

[**DownloadResponse**](DownloadResponse)


## get_fax_documents

> [**FaxDocumentEntityListing**](FaxDocumentEntityListing) get_fax_documents(page_size=page_size, page_number=page_number)


Get a list of fax documents.

Wraps GET /api/v2/fax/documents 

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
api_instance = PureCloudPlatformClientV2.FaxApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of fax documents.
    api_response = api_instance.get_fax_documents(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxApi->get_fax_documents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**FaxDocumentEntityListing**](FaxDocumentEntityListing)


## get_fax_settings

> [**FaxConfig**](FaxConfig) get_fax_settings()


Get organization config for given organization

Wraps GET /api/v2/fax/settings 

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
api_instance = PureCloudPlatformClientV2.FaxApi()

try:
    # Get organization config for given organization
    api_response = api_instance.get_fax_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxApi->get_fax_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**FaxConfig**](FaxConfig)


## get_fax_summary

> [**FaxSummary**](FaxSummary) get_fax_summary()


Get fax summary

Wraps GET /api/v2/fax/summary 

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
api_instance = PureCloudPlatformClientV2.FaxApi()

try:
    # Get fax summary
    api_response = api_instance.get_fax_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxApi->get_fax_summary: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**FaxSummary**](FaxSummary)


## put_fax_document

> [**FaxDocument**](FaxDocument) put_fax_document(document_id, body)


Update a fax document.

Wraps PUT /api/v2/fax/documents/{documentId} 

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
api_instance = PureCloudPlatformClientV2.FaxApi()
document_id = 'document_id_example' # str | Document ID
body = PureCloudPlatformClientV2.FaxDocument() # FaxDocument | Document

try:
    # Update a fax document.
    api_response = api_instance.put_fax_document(document_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxApi->put_fax_document: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |
| **body** | [**FaxDocument**](FaxDocument)| Document |  |

### Return type

[**FaxDocument**](FaxDocument)


## put_fax_settings

> [**FaxConfig**](FaxConfig) put_fax_settings(body=body)


Update/write organization config for given organization

Wraps PUT /api/v2/fax/settings 

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
api_instance = PureCloudPlatformClientV2.FaxApi()
body = PureCloudPlatformClientV2.FaxConfig() # FaxConfig |  (optional)

try:
    # Update/write organization config for given organization
    api_response = api_instance.put_fax_settings(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxApi->put_fax_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FaxConfig**](FaxConfig)|  | [optional]  |

### Return type

[**FaxConfig**](FaxConfig)


_PureCloudPlatformClientV2 242.0.0_

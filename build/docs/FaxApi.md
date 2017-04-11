---
title: FaxApi
---

## PureCloudPlatformClientV2.FaxApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_fax_document**](FaxApi.html#delete_fax_document) | Delete a fax document.|
|[**get_fax_document**](FaxApi.html#get_fax_document) | Get a document.|
|[**get_fax_document_content**](FaxApi.html#get_fax_document_content) | Download a fax document.|
|[**get_fax_documents**](FaxApi.html#get_fax_documents) | Get a list of fax documents.|
|[**get_fax_summary**](FaxApi.html#get_fax_summary) | Get fax summary|
|[**put_fax_document**](FaxApi.html#put_fax_document) | Update a fax document.|
{: class="table table-striped"}

<a name="delete_fax_document"></a>

##  delete_fax_document(document_id)

Delete a fax document.



Wraps DELETE /api/v2/fax/documents/{documentId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.FaxApi()
document_id = 'document_id_example' # str | Document ID

try:
    # Delete a fax document.
    api_instance.delete_fax_document(document_id)
except ApiException as e:
    print "Exception when calling FaxApi->delete_fax_document: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_fax_document"></a>

## [**FaxDocument**](FaxDocument.html) get_fax_document(document_id)

Get a document.



Wraps GET /api/v2/fax/documents/{documentId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.FaxApi()
document_id = 'document_id_example' # str | Document ID

try:
    # Get a document.
    api_response = api_instance.get_fax_document(document_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FaxApi->get_fax_document: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID | |
{: class="table table-striped"}

### Return type

[**FaxDocument**](FaxDocument.html)

<a name="get_fax_document_content"></a>

## [**DownloadResponse**](DownloadResponse.html) get_fax_document_content(document_id)

Download a fax document.



Wraps GET /api/v2/fax/documents/{documentId}/content 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.FaxApi()
document_id = 'document_id_example' # str | Document ID

try:
    # Download a fax document.
    api_response = api_instance.get_fax_document_content(document_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FaxApi->get_fax_document_content: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID | |
{: class="table table-striped"}

### Return type

[**DownloadResponse**](DownloadResponse.html)

<a name="get_fax_documents"></a>

## [**FaxDocumentEntityListing**](FaxDocumentEntityListing.html) get_fax_documents(page_size=page_size, page_number=page_number)

Get a list of fax documents.



Wraps GET /api/v2/fax/documents 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling FaxApi->get_fax_documents: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **page_number** | **int**| Page number | [optional] [default to 1]|
{: class="table table-striped"}

### Return type

[**FaxDocumentEntityListing**](FaxDocumentEntityListing.html)

<a name="get_fax_summary"></a>

## [**FaxSummary**](FaxSummary.html) get_fax_summary()

Get fax summary



Wraps GET /api/v2/fax/summary 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.FaxApi()

try:
    # Get fax summary
    api_response = api_instance.get_fax_summary()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FaxApi->get_fax_summary: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**FaxSummary**](FaxSummary.html)

<a name="put_fax_document"></a>

## [**FaxDocument**](FaxDocument.html) put_fax_document(document_id, body)

Update a fax document.



Wraps PUT /api/v2/fax/documents/{documentId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling FaxApi->put_fax_document: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID | |
| **body** | [**FaxDocument**](FaxDocument.html)| Document | |
{: class="table table-striped"}

### Return type

[**FaxDocument**](FaxDocument.html)


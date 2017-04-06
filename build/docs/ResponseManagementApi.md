---
title: ResponseManagementApi
---

## PureCloudPlatformClientV2.ResponseManagementApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_responsemanagement_library**](ResponseManagementApi.html#delete_responsemanagement_library) | Delete an existing response library.|
|[**delete_responsemanagement_response**](ResponseManagementApi.html#delete_responsemanagement_response) | Delete an existing response.|
|[**get_responsemanagement_libraries**](ResponseManagementApi.html#get_responsemanagement_libraries) | Gets a list of existing response libraries.|
|[**get_responsemanagement_library**](ResponseManagementApi.html#get_responsemanagement_library) | Get details about an existing response library.|
|[**get_responsemanagement_response**](ResponseManagementApi.html#get_responsemanagement_response) | Get details about an existing response.|
|[**get_responsemanagement_responses**](ResponseManagementApi.html#get_responsemanagement_responses) | Gets a list of existing responses.|
|[**post_responsemanagement_libraries**](ResponseManagementApi.html#post_responsemanagement_libraries) | Create a response library.|
|[**post_responsemanagement_responses**](ResponseManagementApi.html#post_responsemanagement_responses) | Create a response.|
|[**post_responsemanagement_responses_query**](ResponseManagementApi.html#post_responsemanagement_responses_query) | Query responses|
|[**put_responsemanagement_library**](ResponseManagementApi.html#put_responsemanagement_library) | Update an existing response library.|
|[**put_responsemanagement_response**](ResponseManagementApi.html#put_responsemanagement_response) | Update an existing response.|
{: class="table table-striped"}

<a name="delete_responsemanagement_library"></a>

## delete_responsemanagement_library(library_id)

Delete an existing response library.

This will remove any responses associated with the library.

Wraps DELETE /api/v2/responsemanagement/libraries/{libraryId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
library_id = 'library_id_example' # str | Library ID

try:
    # Delete an existing response library.
    api_instance.delete_responsemanagement_library(library_id)
except ApiException as e:
    print "Exception when calling ResponseManagementApi->delete_responsemanagement_library: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **library_id** | **str**| Library ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_responsemanagement_response"></a>

## delete_responsemanagement_response(response_id)

Delete an existing response.

This will remove the response from any libraries associated with it.

Wraps DELETE /api/v2/responsemanagement/responses/{responseId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
response_id = 'response_id_example' # str | Response ID

try:
    # Delete an existing response.
    api_instance.delete_responsemanagement_response(response_id)
except ApiException as e:
    print "Exception when calling ResponseManagementApi->delete_responsemanagement_response: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **response_id** | **str**| Response ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_responsemanagement_libraries"></a>

## [**LibraryEntityListing**](LibraryEntityListing.html)get_responsemanagement_libraries(page_number=page_number, page_size=page_size)

Gets a list of existing response libraries.



Wraps GET /api/v2/responsemanagement/libraries 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Gets a list of existing response libraries.
    api_response = api_instance.get_responsemanagement_libraries(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResponseManagementApi->get_responsemanagement_libraries: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
{: class="table table-striped"}

### Return type

[**LibraryEntityListing**](LibraryEntityListing.html)

<a name="get_responsemanagement_library"></a>

## [**Library**](Library.html)get_responsemanagement_library(library_id)

Get details about an existing response library.



Wraps GET /api/v2/responsemanagement/libraries/{libraryId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
library_id = 'library_id_example' # str | Library ID

try:
    # Get details about an existing response library.
    api_response = api_instance.get_responsemanagement_library(library_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResponseManagementApi->get_responsemanagement_library: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **library_id** | **str**| Library ID | |
{: class="table table-striped"}

### Return type

[**Library**](Library.html)

<a name="get_responsemanagement_response"></a>

## [**Response**](Response.html)get_responsemanagement_response(response_id, expand=expand)

Get details about an existing response.



Wraps GET /api/v2/responsemanagement/responses/{responseId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ResponseManagementApi->get_responsemanagement_response: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **response_id** | **str**| Response ID | |
| **expand** | **str**| Expand instructions for the return value. | [optional] |
{: class="table table-striped"}

### Return type

[**Response**](Response.html)

<a name="get_responsemanagement_responses"></a>

## [**ResponseEntityListing**](ResponseEntityListing.html)get_responsemanagement_responses(library_id, page_number=page_number, page_size=page_size, expand=expand)

Gets a list of existing responses.



Wraps GET /api/v2/responsemanagement/responses 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ResponseManagementApi->get_responsemanagement_responses: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **library_id** | **str**| Library ID | |
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **expand** | **str**| Expand instructions for the return value. | [optional] |
{: class="table table-striped"}

### Return type

[**ResponseEntityListing**](ResponseEntityListing.html)

<a name="post_responsemanagement_libraries"></a>

## [**Library**](Library.html)post_responsemanagement_libraries(body)

Create a response library.



Wraps POST /api/v2/responsemanagement/libraries 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
body = PureCloudPlatformClientV2.Library() # Library | Library

try:
    # Create a response library.
    api_response = api_instance.post_responsemanagement_libraries(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResponseManagementApi->post_responsemanagement_libraries: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Library**](Library.html)| Library | |
{: class="table table-striped"}

### Return type

[**Library**](Library.html)

<a name="post_responsemanagement_responses"></a>

## [**Response**](Response.html)post_responsemanagement_responses(body, expand=expand)

Create a response.



Wraps POST /api/v2/responsemanagement/responses 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ResponseManagementApi->post_responsemanagement_responses: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Response**](Response.html)| Response | |
| **expand** | **str**| Expand instructions for the return value. | [optional] |
{: class="table table-striped"}

### Return type

[**Response**](Response.html)

<a name="post_responsemanagement_responses_query"></a>

## [**ResponseQueryResults**](ResponseQueryResults.html)post_responsemanagement_responses_query(body)

Query responses



Wraps POST /api/v2/responsemanagement/responses/query 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ResponseManagementApi()
body = PureCloudPlatformClientV2.ResponseQueryRequest() # ResponseQueryRequest | Response

try:
    # Query responses
    api_response = api_instance.post_responsemanagement_responses_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResponseManagementApi->post_responsemanagement_responses_query: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ResponseQueryRequest**](ResponseQueryRequest.html)| Response | |
{: class="table table-striped"}

### Return type

[**ResponseQueryResults**](ResponseQueryResults.html)

<a name="put_responsemanagement_library"></a>

## [**Library**](Library.html)put_responsemanagement_library(library_id, body)

Update an existing response library.

Fields that can be updated: name. The most recent version is required for updates.

Wraps PUT /api/v2/responsemanagement/libraries/{libraryId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ResponseManagementApi->put_responsemanagement_library: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **library_id** | **str**| Library ID | |
| **body** | [**Library**](Library.html)| Library | |
{: class="table table-striped"}

### Return type

[**Library**](Library.html)

<a name="put_responsemanagement_response"></a>

## [**Response**](Response.html)put_responsemanagement_response(response_id, body, expand=expand)

Update an existing response.

Fields that can be updated: name, libraries, and texts. The most recent version is required for updates.

Wraps PUT /api/v2/responsemanagement/responses/{responseId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
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
    print "Exception when calling ResponseManagementApi->put_responsemanagement_response: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **response_id** | **str**| Response ID | |
| **body** | [**Response**](Response.html)| Response | |
| **expand** | **str**| Expand instructions for the return value. | [optional] |
{: class="table table-striped"}

### Return type

[**Response**](Response.html)


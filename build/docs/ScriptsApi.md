---
title: ScriptsApi
---

## PureCloudPlatformClientV2.ScriptsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_script**](ScriptsApi.html#get_script) | Get a script|
|[**get_script_page**](ScriptsApi.html#get_script_page) | Get a page|
|[**get_script_pages**](ScriptsApi.html#get_script_pages) | Get the list of pages|
|[**get_scripts**](ScriptsApi.html#get_scripts) | Get the list of scripts|
|[**get_scripts_published**](ScriptsApi.html#get_scripts_published) | Get the published scripts.|
|[**get_scripts_published_script_id**](ScriptsApi.html#get_scripts_published_script_id) | Get the published script.|
|[**get_scripts_published_script_id_page**](ScriptsApi.html#get_scripts_published_script_id_page) | Get the published page.|
|[**get_scripts_published_script_id_pages**](ScriptsApi.html#get_scripts_published_script_id_pages) | Get the list of published pages|
|[**get_scripts_published_script_id_variables**](ScriptsApi.html#get_scripts_published_script_id_variables) | Get the published variables|
|[**get_scripts_upload_status**](ScriptsApi.html#get_scripts_upload_status) | Get the upload status of an imported script|
|[**post_script_export**](ScriptsApi.html#post_script_export) | Export a script via download service.|
{: class="table table-striped"}

<a name="get_script"></a>

## [**Script**](Script.html) get_script(script_id)



Get a script



Wraps GET /api/v2/scripts/{scriptId} 

Requires ANY permissions: 

* scripter:script:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
script_id = 'script_id_example' # str | Script ID

try:
    # Get a script
    api_response = api_instance.get_script(script_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_script: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
{: class="table table-striped"}

### Return type

[**Script**](Script.html)

<a name="get_script_page"></a>

## [**Page**](Page.html) get_script_page(script_id, page_id, script_data_version=script_data_version)



Get a page



Wraps GET /api/v2/scripts/{scriptId}/pages/{pageId} 

Requires ANY permissions: 

* scripter:script:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
script_id = 'script_id_example' # str | Script ID
page_id = 'page_id_example' # str | Page ID
script_data_version = 'script_data_version_example' # str | Advanced usage - controls the data version of the script (optional)

try:
    # Get a page
    api_response = api_instance.get_script_page(script_id, page_id, script_data_version=script_data_version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_script_page: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **page_id** | **str**| Page ID |  |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |
{: class="table table-striped"}

### Return type

[**Page**](Page.html)

<a name="get_script_pages"></a>

## [**list[Page]**](Page.html) get_script_pages(script_id, script_data_version=script_data_version)



Get the list of pages



Wraps GET /api/v2/scripts/{scriptId}/pages 

Requires ANY permissions: 

* scripter:script:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
script_id = 'script_id_example' # str | Script ID
script_data_version = 'script_data_version_example' # str | Advanced usage - controls the data version of the script (optional)

try:
    # Get the list of pages
    api_response = api_instance.get_script_pages(script_id, script_data_version=script_data_version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_script_pages: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |
{: class="table table-striped"}

### Return type

[**list[Page]**](Page.html)

<a name="get_scripts"></a>

## [**ScriptEntityListing**](ScriptEntityListing.html) get_scripts(page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id, sort_by=sort_by, sort_order=sort_order, script_data_version=script_data_version)



Get the list of scripts



Wraps GET /api/v2/scripts 

Requires ANY permissions: 

* scripter:script:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
expand = 'expand_example' # str | Expand (optional)
name = 'name_example' # str | Name filter (optional)
feature = 'feature_example' # str | Feature filter (optional)
flow_id = 'flow_id_example' # str | Secure flow id filter (optional)
sort_by = 'sort_by_example' # str | SortBy (optional)
sort_order = 'sort_order_example' # str | SortOrder (optional)
script_data_version = 'script_data_version_example' # str | Advanced usage - controls the data version of the script (optional)

try:
    # Get the list of scripts
    api_response = api_instance.get_scripts(page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id, sort_by=sort_by, sort_order=sort_order, script_data_version=script_data_version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_scripts: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | **str**| Expand | [optional]  |
| **name** | **str**| Name filter | [optional]  |
| **feature** | **str**| Feature filter | [optional]  |
| **flow_id** | **str**| Secure flow id filter | [optional]  |
| **sort_by** | **str**| SortBy | [optional] <br />**Values**: modifiedDate, createdDate |
| **sort_order** | **str**| SortOrder | [optional] <br />**Values**: ascending, descending |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |
{: class="table table-striped"}

### Return type

[**ScriptEntityListing**](ScriptEntityListing.html)

<a name="get_scripts_published"></a>

## [**ScriptEntityListing**](ScriptEntityListing.html) get_scripts_published(script_id, page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id, script_data_version=script_data_version)



Get the published scripts.



Wraps GET /api/v2/scripts/published 

Requires ANY permissions: 

* scripter:publishedScript:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
script_id = 'script_id_example' # str | Script ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
expand = 'expand_example' # str | Expand (optional)
name = 'name_example' # str | Name filter (optional)
feature = 'feature_example' # str | Feature filter (optional)
flow_id = 'flow_id_example' # str | Secure flow id filter (optional)
script_data_version = 'script_data_version_example' # str | Advanced usage - controls the data version of the script (optional)

try:
    # Get the published scripts.
    api_response = api_instance.get_scripts_published(script_id, page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id, script_data_version=script_data_version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_scripts_published: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | **str**| Expand | [optional]  |
| **name** | **str**| Name filter | [optional]  |
| **feature** | **str**| Feature filter | [optional]  |
| **flow_id** | **str**| Secure flow id filter | [optional]  |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |
{: class="table table-striped"}

### Return type

[**ScriptEntityListing**](ScriptEntityListing.html)

<a name="get_scripts_published_script_id"></a>

## [**Script**](Script.html) get_scripts_published_script_id(script_id, script_data_version=script_data_version)



Get the published script.



Wraps GET /api/v2/scripts/published/{scriptId} 

Requires ANY permissions: 

* scripter:publishedScript:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
script_id = 'script_id_example' # str | Script ID
script_data_version = 'script_data_version_example' # str | Advanced usage - controls the data version of the script (optional)

try:
    # Get the published script.
    api_response = api_instance.get_scripts_published_script_id(script_id, script_data_version=script_data_version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_scripts_published_script_id: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |
{: class="table table-striped"}

### Return type

[**Script**](Script.html)

<a name="get_scripts_published_script_id_page"></a>

## [**Page**](Page.html) get_scripts_published_script_id_page(script_id, page_id, script_data_version=script_data_version)



Get the published page.



Wraps GET /api/v2/scripts/published/{scriptId}/pages/{pageId} 

Requires ANY permissions: 

* scripter:publishedScript:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
script_id = 'script_id_example' # str | Script ID
page_id = 'page_id_example' # str | Page ID
script_data_version = 'script_data_version_example' # str | Advanced usage - controls the data version of the script (optional)

try:
    # Get the published page.
    api_response = api_instance.get_scripts_published_script_id_page(script_id, page_id, script_data_version=script_data_version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_scripts_published_script_id_page: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **page_id** | **str**| Page ID |  |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |
{: class="table table-striped"}

### Return type

[**Page**](Page.html)

<a name="get_scripts_published_script_id_pages"></a>

## [**list[Page]**](Page.html) get_scripts_published_script_id_pages(script_id, script_data_version=script_data_version)



Get the list of published pages



Wraps GET /api/v2/scripts/published/{scriptId}/pages 

Requires ANY permissions: 

* scripter:publishedScript:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
script_id = 'script_id_example' # str | Script ID
script_data_version = 'script_data_version_example' # str | Advanced usage - controls the data version of the script (optional)

try:
    # Get the list of published pages
    api_response = api_instance.get_scripts_published_script_id_pages(script_id, script_data_version=script_data_version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_scripts_published_script_id_pages: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |
{: class="table table-striped"}

### Return type

[**list[Page]**](Page.html)

<a name="get_scripts_published_script_id_variables"></a>

## object** get_scripts_published_script_id_variables(script_id, input=input, output=output, type=type, script_data_version=script_data_version)



Get the published variables



Wraps GET /api/v2/scripts/published/{scriptId}/variables 

Requires ANY permissions: 

* scripter:publishedScript:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
script_id = 'script_id_example' # str | Script ID
input = 'input_example' # str | input (optional)
output = 'output_example' # str | output (optional)
type = 'type_example' # str | type (optional)
script_data_version = 'script_data_version_example' # str | Advanced usage - controls the data version of the script (optional)

try:
    # Get the published variables
    api_response = api_instance.get_scripts_published_script_id_variables(script_id, input=input, output=output, type=type, script_data_version=script_data_version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_scripts_published_script_id_variables: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **input** | **str**| input | [optional]  |
| **output** | **str**| output | [optional]  |
| **type** | **str**| type | [optional]  |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |
{: class="table table-striped"}

### Return type

**object**

<a name="get_scripts_upload_status"></a>

## [**ImportScriptStatusResponse**](ImportScriptStatusResponse.html) get_scripts_upload_status(upload_id, long_poll=long_poll)



Get the upload status of an imported script



Wraps GET /api/v2/scripts/uploads/{uploadId}/status 

Requires ANY permissions: 

* scripter:script:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
upload_id = 'upload_id_example' # str | Upload ID
long_poll = false # bool | Enable longPolling endpoint (optional) (default to false)

try:
    # Get the upload status of an imported script
    api_response = api_instance.get_scripts_upload_status(upload_id, long_poll=long_poll)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_scripts_upload_status: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **upload_id** | **str**| Upload ID |  |
| **long_poll** | **bool**| Enable longPolling endpoint | [optional] [default to false] |
{: class="table table-striped"}

### Return type

[**ImportScriptStatusResponse**](ImportScriptStatusResponse.html)

<a name="post_script_export"></a>

## [**ExportScriptResponse**](ExportScriptResponse.html) post_script_export(script_id, body=body)



Export a script via download service.



Wraps POST /api/v2/scripts/{scriptId}/export 

Requires ANY permissions: 

* scripter:script:view

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
script_id = 'script_id_example' # str | Script ID
body = PureCloudPlatformClientV2.ExportScriptRequest() # ExportScriptRequest |  (optional)

try:
    # Export a script via download service.
    api_response = api_instance.post_script_export(script_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->post_script_export: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **body** | [**ExportScriptRequest**](ExportScriptRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**ExportScriptResponse**](ExportScriptResponse.html)


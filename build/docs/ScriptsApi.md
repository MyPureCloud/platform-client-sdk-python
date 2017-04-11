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
{: class="table table-striped"}

<a name="get_script"></a>

## [**Script**](Script.html) get_script(script_id)

Get a script



Wraps GET /api/v2/scripts/{scriptId} 

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
| **script_id** | **str**| Script ID | |
{: class="table table-striped"}

### Return type

[**Script**](Script.html)

<a name="get_script_page"></a>

## [**Page**](Page.html) get_script_page(script_id, page_id)

Get a page



Wraps GET /api/v2/scripts/{scriptId}/pages/{pageId} 

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

try:
    # Get a page
    api_response = api_instance.get_script_page(script_id, page_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_script_page: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID | |
| **page_id** | **str**| Page ID | |
{: class="table table-striped"}

### Return type

[**Page**](Page.html)

<a name="get_script_pages"></a>

## [**list[Page]**](Page.html) get_script_pages(script_id)

Get the list of pages



Wraps GET /api/v2/scripts/{scriptId}/pages 

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
    # Get the list of pages
    api_response = api_instance.get_script_pages(script_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_script_pages: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID | |
{: class="table table-striped"}

### Return type

[**list[Page]**](Page.html)

<a name="get_scripts"></a>

## [**ScriptEntityListing**](ScriptEntityListing.html) get_scripts(page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id, sort_by=sort_by, sort_order=sort_order)

Get the list of scripts



Wraps GET /api/v2/scripts 

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

try:
    # Get the list of scripts
    api_response = api_instance.get_scripts(page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_scripts: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **expand** | **str**| Expand | [optional] |
| **name** | **str**| Name filter | [optional] |
| **feature** | **str**| Feature filter | [optional] |
| **flow_id** | **str**| Secure flow id filter | [optional] |
| **sort_by** | **str**| SortBy | [optional] |
| **sort_order** | **str**| SortOrder | [optional] |
{: class="table table-striped"}

### Return type

[**ScriptEntityListing**](ScriptEntityListing.html)

<a name="get_scripts_published"></a>

## [**ScriptEntityListing**](ScriptEntityListing.html) get_scripts_published(page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id)

Get the published scripts.



Wraps GET /api/v2/scripts/published 

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

try:
    # Get the published scripts.
    api_response = api_instance.get_scripts_published(page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_scripts_published: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **expand** | **str**| Expand | [optional] |
| **name** | **str**| Name filter | [optional] |
| **feature** | **str**| Feature filter | [optional] |
| **flow_id** | **str**| Secure flow id filter | [optional] |
{: class="table table-striped"}

### Return type

[**ScriptEntityListing**](ScriptEntityListing.html)

<a name="get_scripts_published_script_id"></a>

## [**Script**](Script.html) get_scripts_published_script_id(script_id)

Get the published script.



Wraps GET /api/v2/scripts/published/{scriptId} 

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
    # Get the published script.
    api_response = api_instance.get_scripts_published_script_id(script_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_scripts_published_script_id: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID | |
{: class="table table-striped"}

### Return type

[**Script**](Script.html)

<a name="get_scripts_published_script_id_page"></a>

## [**Page**](Page.html) get_scripts_published_script_id_page(script_id, page_id)

Get the published page.



Wraps GET /api/v2/scripts/published/{scriptId}/pages/{pageId} 

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

try:
    # Get the published page.
    api_response = api_instance.get_scripts_published_script_id_page(script_id, page_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_scripts_published_script_id_page: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID | |
| **page_id** | **str**| Page ID | |
{: class="table table-striped"}

### Return type

[**Page**](Page.html)

<a name="get_scripts_published_script_id_pages"></a>

## [**list[Page]**](Page.html) get_scripts_published_script_id_pages(script_id)

Get the list of published pages



Wraps GET /api/v2/scripts/published/{scriptId}/pages 

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
    # Get the list of published pages
    api_response = api_instance.get_scripts_published_script_id_pages(script_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_scripts_published_script_id_pages: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID | |
{: class="table table-striped"}

### Return type

[**list[Page]**](Page.html)

<a name="get_scripts_published_script_id_variables"></a>

## object** get_scripts_published_script_id_variables(script_id, input=input, output=output, type=type)

Get the published variables



Wraps GET /api/v2/scripts/published/{scriptId}/variables 

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

try:
    # Get the published variables
    api_response = api_instance.get_scripts_published_script_id_variables(script_id, input=input, output=output, type=type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScriptsApi->get_scripts_published_script_id_variables: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID | |
| **input** | **str**| input | [optional] |
| **output** | **str**| output | [optional] |
| **type** | **str**| type | [optional] |
{: class="table table-striped"}

### Return type

**object**


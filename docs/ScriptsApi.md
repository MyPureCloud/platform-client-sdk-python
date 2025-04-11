# ScriptsApi

## PureCloudPlatformClientV2.ScriptsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_script**](#get_script) | Get a script|
|[**get_script_page**](#get_script_page) | Get a page|
|[**get_script_pages**](#get_script_pages) | Get the list of pages|
|[**get_scripts**](#get_scripts) | Get the list of scripts|
|[**get_scripts_divisionviews**](#get_scripts_divisionviews) | Get the metadata for a list of scripts|
|[**get_scripts_published**](#get_scripts_published) | Get the published scripts.|
|[**get_scripts_published_divisionviews**](#get_scripts_published_divisionviews) | Get the published scripts metadata.|
|[**get_scripts_published_script_id**](#get_scripts_published_script_id) | Get the published script.|
|[**get_scripts_published_script_id_page**](#get_scripts_published_script_id_page) | Get the published page.|
|[**get_scripts_published_script_id_pages**](#get_scripts_published_script_id_pages) | Get the list of published pages|
|[**get_scripts_published_script_id_variables**](#get_scripts_published_script_id_variables) | Get the published variables|
|[**get_scripts_upload_status**](#get_scripts_upload_status) | Get the upload status of an imported script|
|[**post_script_export**](#post_script_export) | Export a script via download service.|
|[**post_scripts_published**](#post_scripts_published) | Publish a script.|



## get_script

> [**Script**](Script) get_script(script_id)


Get a script

Wraps GET /api/v2/scripts/{scriptId} 

Requires ANY permissions: 

* scripter:script:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
script_id = 'script_id_example' # str | Script ID

try:
    # Get a script
    api_response = api_instance.get_script(script_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptsApi->get_script: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |

### Return type

[**Script**](Script)


## get_script_page

> [**Page**](Page) get_script_page(script_id, page_id, script_data_version=script_data_version)


Get a page

Wraps GET /api/v2/scripts/{scriptId}/pages/{pageId} 

Requires ANY permissions: 

* scripter:script:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ScriptsApi->get_script_page: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **page_id** | **str**| Page ID |  |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |

### Return type

[**Page**](Page)


## get_script_pages

> [**list[Page]**](Page) get_script_pages(script_id, script_data_version=script_data_version)


Get the list of pages

Wraps GET /api/v2/scripts/{scriptId}/pages 

Requires ANY permissions: 

* scripter:script:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ScriptsApi->get_script_pages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |

### Return type

[**list[Page]**](Page)


## get_scripts

> [**ScriptEntityListing**](ScriptEntityListing) get_scripts(page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id, sort_by=sort_by, sort_order=sort_order, script_data_version=script_data_version, division_ids=division_ids)


Get the list of scripts

Wraps GET /api/v2/scripts 

Requires ANY permissions: 

* scripter:script:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
division_ids = 'division_ids_example' # str | Filters scripts to requested divisionIds (optional)

try:
    # Get the list of scripts
    api_response = api_instance.get_scripts(page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id, sort_by=sort_by, sort_order=sort_order, script_data_version=script_data_version, division_ids=division_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptsApi->get_scripts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | **str**| Expand | [optional]  |
| **name** | **str**| Name filter | [optional]  |
| **feature** | **str**| Feature filter | [optional]  |
| **flow_id** | **str**| Secure flow id filter | [optional]  |
| **sort_by** | **str**| SortBy | [optional] <br />**Values**: modifiedDate, createdDate, name |
| **sort_order** | **str**| SortOrder | [optional] <br />**Values**: ascending, descending |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |
| **division_ids** | **str**| Filters scripts to requested divisionIds | [optional]  |

### Return type

[**ScriptEntityListing**](ScriptEntityListing)


## get_scripts_divisionviews

> [**ScriptEntityListing**](ScriptEntityListing) get_scripts_divisionviews(page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id, sort_by=sort_by, sort_order=sort_order, script_data_version=script_data_version, division_ids=division_ids)


Get the metadata for a list of scripts

Wraps GET /api/v2/scripts/divisionviews 

Requires ANY permissions: 

* scripter:script:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
division_ids = 'division_ids_example' # str | Filters scripts to requested divisionIds (optional)

try:
    # Get the metadata for a list of scripts
    api_response = api_instance.get_scripts_divisionviews(page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id, sort_by=sort_by, sort_order=sort_order, script_data_version=script_data_version, division_ids=division_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptsApi->get_scripts_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | **str**| Expand | [optional]  |
| **name** | **str**| Name filter | [optional]  |
| **feature** | **str**| Feature filter | [optional]  |
| **flow_id** | **str**| Secure flow id filter | [optional]  |
| **sort_by** | **str**| SortBy | [optional] <br />**Values**: modifiedDate, createdDate, name |
| **sort_order** | **str**| SortOrder | [optional] <br />**Values**: ascending, descending |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |
| **division_ids** | **str**| Filters scripts to requested divisionIds | [optional]  |

### Return type

[**ScriptEntityListing**](ScriptEntityListing)


## get_scripts_published

> [**ScriptEntityListing**](ScriptEntityListing) get_scripts_published(page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id, script_data_version=script_data_version, division_ids=division_ids)


Get the published scripts.

Wraps GET /api/v2/scripts/published 

Requires ANY permissions: 

* scripter:publishedScript:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
expand = 'expand_example' # str | Expand (optional)
name = 'name_example' # str | Name filter (optional)
feature = 'feature_example' # str | Feature filter (optional)
flow_id = 'flow_id_example' # str | Secure flow id filter (optional)
script_data_version = 'script_data_version_example' # str | Advanced usage - controls the data version of the script (optional)
division_ids = 'division_ids_example' # str | Filters scripts to requested divisionIds (optional)

try:
    # Get the published scripts.
    api_response = api_instance.get_scripts_published(page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id, script_data_version=script_data_version, division_ids=division_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptsApi->get_scripts_published: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | **str**| Expand | [optional]  |
| **name** | **str**| Name filter | [optional]  |
| **feature** | **str**| Feature filter | [optional]  |
| **flow_id** | **str**| Secure flow id filter | [optional]  |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |
| **division_ids** | **str**| Filters scripts to requested divisionIds | [optional]  |

### Return type

[**ScriptEntityListing**](ScriptEntityListing)


## get_scripts_published_divisionviews

> [**ScriptEntityListing**](ScriptEntityListing) get_scripts_published_divisionviews(page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id, script_data_version=script_data_version, division_ids=division_ids)


Get the published scripts metadata.

Wraps GET /api/v2/scripts/published/divisionviews 

Requires ANY permissions: 

* scripter:publishedScript:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
expand = 'expand_example' # str | Expand (optional)
name = 'name_example' # str | Name filter (optional)
feature = 'feature_example' # str | Feature filter (optional)
flow_id = 'flow_id_example' # str | Secure flow id filter (optional)
script_data_version = 'script_data_version_example' # str | Advanced usage - controls the data version of the script (optional)
division_ids = 'division_ids_example' # str | Filters scripts to requested divisionIds (optional)

try:
    # Get the published scripts metadata.
    api_response = api_instance.get_scripts_published_divisionviews(page_size=page_size, page_number=page_number, expand=expand, name=name, feature=feature, flow_id=flow_id, script_data_version=script_data_version, division_ids=division_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptsApi->get_scripts_published_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | **str**| Expand | [optional]  |
| **name** | **str**| Name filter | [optional]  |
| **feature** | **str**| Feature filter | [optional]  |
| **flow_id** | **str**| Secure flow id filter | [optional]  |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |
| **division_ids** | **str**| Filters scripts to requested divisionIds | [optional]  |

### Return type

[**ScriptEntityListing**](ScriptEntityListing)


## get_scripts_published_script_id

> [**Script**](Script) get_scripts_published_script_id(script_id, script_data_version=script_data_version)


Get the published script.

Wraps GET /api/v2/scripts/published/{scriptId} 

Requires ANY permissions: 

* scripter:publishedScript:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ScriptsApi->get_scripts_published_script_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |

### Return type

[**Script**](Script)


## get_scripts_published_script_id_page

> [**Page**](Page) get_scripts_published_script_id_page(script_id, page_id, script_data_version=script_data_version)


Get the published page.

Wraps GET /api/v2/scripts/published/{scriptId}/pages/{pageId} 

Requires ANY permissions: 

* scripter:publishedScript:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ScriptsApi->get_scripts_published_script_id_page: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **page_id** | **str**| Page ID |  |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |

### Return type

[**Page**](Page)


## get_scripts_published_script_id_pages

> [**list[Page]**](Page) get_scripts_published_script_id_pages(script_id, script_data_version=script_data_version)


Get the list of published pages

Wraps GET /api/v2/scripts/published/{scriptId}/pages 

Requires ANY permissions: 

* scripter:publishedScript:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ScriptsApi->get_scripts_published_script_id_pages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |

### Return type

[**list[Page]**](Page)


## get_scripts_published_script_id_variables

> object** get_scripts_published_script_id_variables(script_id, input=input, output=output, type=type, script_data_version=script_data_version)


Get the published variables

Wraps GET /api/v2/scripts/published/{scriptId}/variables 

Requires ANY permissions: 

* scripter:publishedScript:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ScriptsApi->get_scripts_published_script_id_variables: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **input** | **str**| input | [optional] <br />**Values**: true, false |
| **output** | **str**| output | [optional] <br />**Values**: true, false |
| **type** | **str**| type | [optional] <br />**Values**: string, number, boolean |
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |

### Return type

**object**


## get_scripts_upload_status

> [**ImportScriptStatusResponse**](ImportScriptStatusResponse) get_scripts_upload_status(upload_id, long_poll=long_poll)


Get the upload status of an imported script

Wraps GET /api/v2/scripts/uploads/{uploadId}/status 

Requires ANY permissions: 

* scripter:script:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
upload_id = 'upload_id_example' # str | Upload ID
long_poll = False # bool | Enable longPolling endpoint (optional) (default to False)

try:
    # Get the upload status of an imported script
    api_response = api_instance.get_scripts_upload_status(upload_id, long_poll=long_poll)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptsApi->get_scripts_upload_status: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **upload_id** | **str**| Upload ID |  |
| **long_poll** | **bool**| Enable longPolling endpoint | [optional] [default to False] |

### Return type

[**ImportScriptStatusResponse**](ImportScriptStatusResponse)


## post_script_export

> [**ExportScriptResponse**](ExportScriptResponse) post_script_export(script_id, body=body)


Export a script via download service.

Wraps POST /api/v2/scripts/{scriptId}/export 

Requires ANY permissions: 

* scripter:script:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
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
    print("Exception when calling ScriptsApi->post_script_export: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_id** | **str**| Script ID |  |
| **body** | [**ExportScriptRequest**](ExportScriptRequest)|  | [optional]  |

### Return type

[**ExportScriptResponse**](ExportScriptResponse)


## post_scripts_published

> [**Script**](Script) post_scripts_published(script_data_version=script_data_version, body=body)


Publish a script.

Wraps POST /api/v2/scripts/published 

Requires ANY permissions: 

* scripter:publishedScript:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScriptsApi()
script_data_version = 'script_data_version_example' # str | Advanced usage - controls the data version of the script (optional)
body = PureCloudPlatformClientV2.PublishScriptRequestData() # PublishScriptRequestData | body (optional)

try:
    # Publish a script.
    api_response = api_instance.post_scripts_published(script_data_version=script_data_version, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptsApi->post_scripts_published: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **script_data_version** | **str**| Advanced usage - controls the data version of the script | [optional]  |
| **body** | [**PublishScriptRequestData**](PublishScriptRequestData)| body | [optional]  |

### Return type

[**Script**](Script)


_PureCloudPlatformClientV2 226.0.0_

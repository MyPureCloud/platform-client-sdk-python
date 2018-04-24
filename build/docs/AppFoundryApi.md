---
title: AppFoundryApi
---

## PureCloudPlatformClientV2.AppFoundryApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_appfoundry_platform_name_categories**](AppFoundryApi.html#get_appfoundry_platform_name_categories) | Return a structured hierarchy of available listing categories|
|[**get_appfoundry_platform_name_category**](AppFoundryApi.html#get_appfoundry_platform_name_category) | Get listings that are part of the specified root category or a contained subcategory|
|[**get_appfoundry_platform_name_category_sub_category_name**](AppFoundryApi.html#get_appfoundry_platform_name_category_sub_category_name) | Get listings that are part of the specified subcategory|
{: class="table table-striped"}

<a name="get_appfoundry_platform_name_categories"></a>

## [**list[AppFoundryListingCategory]**](AppFoundryListingCategory.html) get_appfoundry_platform_name_categories(platform_name)

Return a structured hierarchy of available listing categories



Wraps GET /api/v2/appfoundry/{platformName}/categories 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AppFoundryApi()
platform_name = 'platform_name_example' # str | 

try:
    # Return a structured hierarchy of available listing categories
    api_response = api_instance.get_appfoundry_platform_name_categories(platform_name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AppFoundryApi->get_appfoundry_platform_name_categories: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **platform_name** | **str**|  |  |
{: class="table table-striped"}

### Return type

[**list[AppFoundryListingCategory]**](AppFoundryListingCategory.html)

<a name="get_appfoundry_platform_name_category"></a>

## [**PagedListingEntity**](PagedListingEntity.html) get_appfoundry_platform_name_category(platform_name, category_name, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)

Get listings that are part of the specified root category or a contained subcategory



Wraps GET /api/v2/appfoundry/{platformName}/categories/{categoryName} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AppFoundryApi()
platform_name = 'platform_name_example' # str | 
category_name = 'category_name_example' # str | Name of category to request listings from
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = NULL # list[object] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)

try:
    # Get listings that are part of the specified root category or a contained subcategory
    api_response = api_instance.get_appfoundry_platform_name_category(platform_name, category_name, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AppFoundryApi->get_appfoundry_platform_name_category: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **platform_name** | **str**|  |  |
| **category_name** | **str**| Name of category to request listings from |  |
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[object]**](object.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
{: class="table table-striped"}

### Return type

[**PagedListingEntity**](PagedListingEntity.html)

<a name="get_appfoundry_platform_name_category_sub_category_name"></a>

## [**PagedListingEntity**](PagedListingEntity.html) get_appfoundry_platform_name_category_sub_category_name(platform_name, category_name, sub_category_name, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)

Get listings that are part of the specified subcategory



Wraps GET /api/v2/appfoundry/{platformName}/categories/{categoryName}/{subCategoryName} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AppFoundryApi()
platform_name = 'platform_name_example' # str | 
category_name = 'category_name_example' # str | Name of category to request listings from
sub_category_name = 'sub_category_name_example' # str | Name of subcategory to request listings from
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = NULL # list[object] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)

try:
    # Get listings that are part of the specified subcategory
    api_response = api_instance.get_appfoundry_platform_name_category_sub_category_name(platform_name, category_name, sub_category_name, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AppFoundryApi->get_appfoundry_platform_name_category_sub_category_name: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **platform_name** | **str**|  |  |
| **category_name** | **str**| Name of category to request listings from |  |
| **sub_category_name** | **str**| Name of subcategory to request listings from |  |
| **page_size** | **int**| The total page size requested | [optional] [default to 25] |
| **page_number** | **int**| The page number requested | [optional] [default to 1] |
| **sort_by** | **str**| variable name requested to sort by | [optional]  |
| **expand** | [**list[object]**](object.html)| variable name requested by expand list | [optional]  |
| **next_page** | **str**| next page token | [optional]  |
| **previous_page** | **str**| Previous page token | [optional]  |
{: class="table table-striped"}

### Return type

[**PagedListingEntity**](PagedListingEntity.html)


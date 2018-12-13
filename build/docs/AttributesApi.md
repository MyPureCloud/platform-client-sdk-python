---
title: AttributesApi
---

## PureCloudPlatformClientV2.AttributesApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_attribute**](AttributesApi.html#delete_attribute) | Delete an existing Attribute.|
|[**get_attribute**](AttributesApi.html#get_attribute) | Get details about an existing attribute.|
|[**get_attributes**](AttributesApi.html#get_attributes) | Gets a list of existing attributes.|
|[**post_attributes**](AttributesApi.html#post_attributes) | Create an attribute.|
|[**post_attributes_query**](AttributesApi.html#post_attributes_query) | Query attributes|
|[**put_attribute**](AttributesApi.html#put_attribute) | Update an existing attribute.|
{: class="table table-striped"}

<a name="delete_attribute"></a>

##  delete_attribute(attribute_id)



Delete an existing Attribute.

This will remove attribute.

Wraps DELETE /api/v2/attributes/{attributeId} 

Requires NO permissions: 


### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AttributesApi()
attribute_id = 'attribute_id_example' # str | Attribute ID

try:
    # Delete an existing Attribute.
    api_instance.delete_attribute(attribute_id)
except ApiException as e:
    print "Exception when calling AttributesApi->delete_attribute: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **attribute_id** | **str**| Attribute ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_attribute"></a>

## [**Attribute**](Attribute.html) get_attribute(attribute_id)



Get details about an existing attribute.



Wraps GET /api/v2/attributes/{attributeId} 

Requires NO permissions: 


### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AttributesApi()
attribute_id = 'attribute_id_example' # str | Attribute ID

try:
    # Get details about an existing attribute.
    api_response = api_instance.get_attribute(attribute_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AttributesApi->get_attribute: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **attribute_id** | **str**| Attribute ID |  |
{: class="table table-striped"}

### Return type

[**Attribute**](Attribute.html)

<a name="get_attributes"></a>

## [**AttributeEntityListing**](AttributeEntityListing.html) get_attributes(page_number=page_number, page_size=page_size)



Gets a list of existing attributes.



Wraps GET /api/v2/attributes 

Requires NO permissions: 


### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AttributesApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Gets a list of existing attributes.
    api_response = api_instance.get_attributes(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AttributesApi->get_attributes: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**AttributeEntityListing**](AttributeEntityListing.html)

<a name="post_attributes"></a>

## [**Attribute**](Attribute.html) post_attributes(body)



Create an attribute.



Wraps POST /api/v2/attributes 

Requires NO permissions: 


### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AttributesApi()
body = PureCloudPlatformClientV2.Attribute() # Attribute | Attribute

try:
    # Create an attribute.
    api_response = api_instance.post_attributes(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AttributesApi->post_attributes: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Attribute**](Attribute.html)| Attribute |  |
{: class="table table-striped"}

### Return type

[**Attribute**](Attribute.html)

<a name="post_attributes_query"></a>

## [**AttributeEntityListing**](AttributeEntityListing.html) post_attributes_query(body)



Query attributes



Wraps POST /api/v2/attributes/query 

Requires NO permissions: 


### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AttributesApi()
body = PureCloudPlatformClientV2.AttributeQueryRequest() # AttributeQueryRequest | query

try:
    # Query attributes
    api_response = api_instance.post_attributes_query(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AttributesApi->post_attributes_query: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AttributeQueryRequest**](AttributeQueryRequest.html)| query |  |
{: class="table table-striped"}

### Return type

[**AttributeEntityListing**](AttributeEntityListing.html)

<a name="put_attribute"></a>

## [**Attribute**](Attribute.html) put_attribute(attribute_id, body)



Update an existing attribute.

Fields that can be updated: name, description. The most recent version is required for updates.

Wraps PUT /api/v2/attributes/{attributeId} 

Requires NO permissions: 


### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AttributesApi()
attribute_id = 'attribute_id_example' # str | Attribute ID
body = PureCloudPlatformClientV2.Attribute() # Attribute | Attribute

try:
    # Update an existing attribute.
    api_response = api_instance.put_attribute(attribute_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AttributesApi->put_attribute: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **attribute_id** | **str**| Attribute ID |  |
| **body** | [**Attribute**](Attribute.html)| Attribute |  |
{: class="table table-striped"}

### Return type

[**Attribute**](Attribute.html)


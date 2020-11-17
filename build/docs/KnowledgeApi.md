---
title: KnowledgeApi
---

## PureCloudPlatformClientV2.KnowledgeApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_knowledge_knowledgebase**](KnowledgeApi.html#delete_knowledge_knowledgebase) | Delete knowledge base|
|[**delete_knowledge_knowledgebase_language_category**](KnowledgeApi.html#delete_knowledge_knowledgebase_language_category) | Delete category|
|[**delete_knowledge_knowledgebase_language_document**](KnowledgeApi.html#delete_knowledge_knowledgebase_language_document) | Delete document|
|[**get_knowledge_knowledgebase**](KnowledgeApi.html#get_knowledge_knowledgebase) | Get knowledge base|
|[**get_knowledge_knowledgebase_language_categories**](KnowledgeApi.html#get_knowledge_knowledgebase_language_categories) | Get categories|
|[**get_knowledge_knowledgebase_language_category**](KnowledgeApi.html#get_knowledge_knowledgebase_language_category) | Get category|
|[**get_knowledge_knowledgebase_language_document**](KnowledgeApi.html#get_knowledge_knowledgebase_language_document) | Get document|
|[**get_knowledge_knowledgebase_language_documents**](KnowledgeApi.html#get_knowledge_knowledgebase_language_documents) | Get documents|
|[**get_knowledge_knowledgebase_language_training**](KnowledgeApi.html#get_knowledge_knowledgebase_language_training) | Get training detail|
|[**get_knowledge_knowledgebase_language_trainings**](KnowledgeApi.html#get_knowledge_knowledgebase_language_trainings) | Get all trainings information for a knowledgebase|
|[**get_knowledge_knowledgebases**](KnowledgeApi.html#get_knowledge_knowledgebases) | Get knowledge bases|
|[**patch_knowledge_knowledgebase**](KnowledgeApi.html#patch_knowledge_knowledgebase) | Update knowledge base|
|[**patch_knowledge_knowledgebase_language_category**](KnowledgeApi.html#patch_knowledge_knowledgebase_language_category) | Update category|
|[**patch_knowledge_knowledgebase_language_document**](KnowledgeApi.html#patch_knowledge_knowledgebase_language_document) | Update document|
|[**patch_knowledge_knowledgebase_language_documents**](KnowledgeApi.html#patch_knowledge_knowledgebase_language_documents) | Update documents collection|
|[**post_knowledge_knowledgebase_language_categories**](KnowledgeApi.html#post_knowledge_knowledgebase_language_categories) | Create new category|
|[**post_knowledge_knowledgebase_language_documents**](KnowledgeApi.html#post_knowledge_knowledgebase_language_documents) | Create document|
|[**post_knowledge_knowledgebase_language_training_promote**](KnowledgeApi.html#post_knowledge_knowledgebase_language_training_promote) | Promote trained documents from draft state to active.|
|[**post_knowledge_knowledgebase_language_trainings**](KnowledgeApi.html#post_knowledge_knowledgebase_language_trainings) | Trigger training|
|[**post_knowledge_knowledgebase_search**](KnowledgeApi.html#post_knowledge_knowledgebase_search) | Search Documents|
|[**post_knowledge_knowledgebases**](KnowledgeApi.html#post_knowledge_knowledgebases) | Create new knowledge base|
{: class="table table-striped"}

<a name="delete_knowledge_knowledgebase"></a>

## [**KnowledgeBase**](KnowledgeBase.html) delete_knowledge_knowledgebase(knowledge_base_id)



Delete knowledge base



Wraps DELETE /api/v2/knowledge/knowledgebases/{knowledgeBaseId} 

Requires ALL permissions: 

* knowledge:knowledgebase:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID

try:
    # Delete knowledge base
    api_response = api_instance.delete_knowledge_knowledgebase(knowledge_base_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->delete_knowledge_knowledgebase: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
{: class="table table-striped"}

### Return type

[**KnowledgeBase**](KnowledgeBase.html)

<a name="delete_knowledge_knowledgebase_language_category"></a>

## [**KnowledgeCategory**](KnowledgeCategory.html) delete_knowledge_knowledgebase_language_category(category_id, knowledge_base_id, language_code)



Delete category



Wraps DELETE /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/categories/{categoryId} 

Requires ALL permissions: 

* knowledge:category:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
category_id = 'category_id_example' # str | Category ID
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE

try:
    # Delete category
    api_response = api_instance.delete_knowledge_knowledgebase_language_category(category_id, knowledge_base_id, language_code)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->delete_knowledge_knowledgebase_language_category: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **category_id** | **str**| Category ID |  |
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
{: class="table table-striped"}

### Return type

[**KnowledgeCategory**](KnowledgeCategory.html)

<a name="delete_knowledge_knowledgebase_language_document"></a>

## [**KnowledgeDocument**](KnowledgeDocument.html) delete_knowledge_knowledgebase_language_document(document_id, knowledge_base_id, language_code)



Delete document



Wraps DELETE /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/{documentId} 

Requires ALL permissions: 

* knowledge:document:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
document_id = 'document_id_example' # str | Document ID
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE

try:
    # Delete document
    api_response = api_instance.delete_knowledge_knowledgebase_language_document(document_id, knowledge_base_id, language_code)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->delete_knowledge_knowledgebase_language_document: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
{: class="table table-striped"}

### Return type

[**KnowledgeDocument**](KnowledgeDocument.html)

<a name="get_knowledge_knowledgebase"></a>

## [**KnowledgeBase**](KnowledgeBase.html) get_knowledge_knowledgebase(knowledge_base_id)



Get knowledge base



Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId} 

Requires ALL permissions: 

* knowledge:knowledgebase:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID

try:
    # Get knowledge base
    api_response = api_instance.get_knowledge_knowledgebase(knowledge_base_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->get_knowledge_knowledgebase: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
{: class="table table-striped"}

### Return type

[**KnowledgeBase**](KnowledgeBase.html)

<a name="get_knowledge_knowledgebase_language_categories"></a>

## [**CategoryListing**](CategoryListing.html) get_knowledge_knowledgebase_language_categories(knowledge_base_id, language_code, before=before, after=after, limit=limit, page_size=page_size)



Get categories



Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/categories 

Requires ALL permissions: 

* knowledge:category:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
limit = 'limit_example' # str | Number of entities to return. Maximum of 200. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)

try:
    # Get categories
    api_response = api_instance.get_knowledge_knowledgebase_language_categories(knowledge_base_id, language_code, before=before, after=after, limit=limit, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->get_knowledge_knowledgebase_language_categories: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **limit** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
{: class="table table-striped"}

### Return type

[**CategoryListing**](CategoryListing.html)

<a name="get_knowledge_knowledgebase_language_category"></a>

## [**KnowledgeExtendedCategory**](KnowledgeExtendedCategory.html) get_knowledge_knowledgebase_language_category(category_id, knowledge_base_id, language_code)



Get category



Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/categories/{categoryId} 

Requires ALL permissions: 

* knowledge:category:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
category_id = 'category_id_example' # str | Category ID
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE

try:
    # Get category
    api_response = api_instance.get_knowledge_knowledgebase_language_category(category_id, knowledge_base_id, language_code)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->get_knowledge_knowledgebase_language_category: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **category_id** | **str**| Category ID |  |
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
{: class="table table-striped"}

### Return type

[**KnowledgeExtendedCategory**](KnowledgeExtendedCategory.html)

<a name="get_knowledge_knowledgebase_language_document"></a>

## [**KnowledgeDocument**](KnowledgeDocument.html) get_knowledge_knowledgebase_language_document(document_id, knowledge_base_id, language_code)



Get document



Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/{documentId} 

Requires ALL permissions: 

* knowledge:document:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
document_id = 'document_id_example' # str | Document ID
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE

try:
    # Get document
    api_response = api_instance.get_knowledge_knowledgebase_language_document(document_id, knowledge_base_id, language_code)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->get_knowledge_knowledgebase_language_document: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
{: class="table table-striped"}

### Return type

[**KnowledgeDocument**](KnowledgeDocument.html)

<a name="get_knowledge_knowledgebase_language_documents"></a>

## [**DocumentListing**](DocumentListing.html) get_knowledge_knowledgebase_language_documents(knowledge_base_id, language_code, before=before, after=after, limit=limit, page_size=page_size, categories=categories, title=title)



Get documents



Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents 

Requires ALL permissions: 

* knowledge:document:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
limit = 'limit_example' # str | Number of entities to return. Maximum of 200. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
categories = 'categories_example' # str | Filter by categories ids, comma separated values expected. (optional)
title = 'title_example' # str | Filter by document title. (optional)

try:
    # Get documents
    api_response = api_instance.get_knowledge_knowledgebase_language_documents(knowledge_base_id, language_code, before=before, after=after, limit=limit, page_size=page_size, categories=categories, title=title)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->get_knowledge_knowledgebase_language_documents: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **limit** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **categories** | **str**| Filter by categories ids, comma separated values expected. | [optional]  |
| **title** | **str**| Filter by document title. | [optional]  |
{: class="table table-striped"}

### Return type

[**DocumentListing**](DocumentListing.html)

<a name="get_knowledge_knowledgebase_language_training"></a>

## [**KnowledgeTraining**](KnowledgeTraining.html) get_knowledge_knowledgebase_language_training(knowledge_base_id, language_code, training_id)



Get training detail



Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/trainings/{trainingId} 

Requires ALL permissions: 

* knowledge:training:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE
training_id = 'training_id_example' # str | Training ID

try:
    # Get training detail
    api_response = api_instance.get_knowledge_knowledgebase_language_training(knowledge_base_id, language_code, training_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->get_knowledge_knowledgebase_language_training: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
| **training_id** | **str**| Training ID |  |
{: class="table table-striped"}

### Return type

[**KnowledgeTraining**](KnowledgeTraining.html)

<a name="get_knowledge_knowledgebase_language_trainings"></a>

## [**TrainingListing**](TrainingListing.html) get_knowledge_knowledgebase_language_trainings(knowledge_base_id, language_code, before=before, after=after, limit=limit, page_size=page_size, knowledge_documents_state=knowledge_documents_state)



Get all trainings information for a knowledgebase



Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/trainings 

Requires ALL permissions: 

* knowledge:training:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
limit = 'limit_example' # str | Number of entities to return. Maximum of 200. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
knowledge_documents_state = 'knowledge_documents_state_example' # str | Return the training with the specified state of the trained documents. (optional)

try:
    # Get all trainings information for a knowledgebase
    api_response = api_instance.get_knowledge_knowledgebase_language_trainings(knowledge_base_id, language_code, before=before, after=after, limit=limit, page_size=page_size, knowledge_documents_state=knowledge_documents_state)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->get_knowledge_knowledgebase_language_trainings: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **limit** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **knowledge_documents_state** | **str**| Return the training with the specified state of the trained documents. | [optional] <br />**Values**: Draft, Active, Discarded, Archived |
{: class="table table-striped"}

### Return type

[**TrainingListing**](TrainingListing.html)

<a name="get_knowledge_knowledgebases"></a>

## [**KnowledgeBaseListing**](KnowledgeBaseListing.html) get_knowledge_knowledgebases(before=before, after=after, limit=limit, page_size=page_size, name=name)



Get knowledge bases



Wraps GET /api/v2/knowledge/knowledgebases 

Requires ALL permissions: 

* knowledge:knowledgebase:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
limit = 'limit_example' # str | Number of entities to return. Maximum of 200. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
name = 'name_example' # str | Name of the KnowledgeBase to filter. (optional)

try:
    # Get knowledge bases
    api_response = api_instance.get_knowledge_knowledgebases(before=before, after=after, limit=limit, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->get_knowledge_knowledgebases: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **limit** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **name** | **str**| Name of the KnowledgeBase to filter. | [optional]  |
{: class="table table-striped"}

### Return type

[**KnowledgeBaseListing**](KnowledgeBaseListing.html)

<a name="patch_knowledge_knowledgebase"></a>

## [**KnowledgeBase**](KnowledgeBase.html) patch_knowledge_knowledgebase(knowledge_base_id, body)



Update knowledge base



Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId} 

Requires ALL permissions: 

* knowledge:knowledgebase:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
body = PureCloudPlatformClientV2.KnowledgeBase() # KnowledgeBase | 

try:
    # Update knowledge base
    api_response = api_instance.patch_knowledge_knowledgebase(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->patch_knowledge_knowledgebase: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeBase**](KnowledgeBase.html)|  |  |
{: class="table table-striped"}

### Return type

[**KnowledgeBase**](KnowledgeBase.html)

<a name="patch_knowledge_knowledgebase_language_category"></a>

## [**KnowledgeExtendedCategory**](KnowledgeExtendedCategory.html) patch_knowledge_knowledgebase_language_category(category_id, knowledge_base_id, language_code, body)



Update category



Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/categories/{categoryId} 

Requires ALL permissions: 

* knowledge:category:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
category_id = 'category_id_example' # str | Category ID
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE
body = PureCloudPlatformClientV2.KnowledgeCategoryRequest() # KnowledgeCategoryRequest | 

try:
    # Update category
    api_response = api_instance.patch_knowledge_knowledgebase_language_category(category_id, knowledge_base_id, language_code, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_language_category: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **category_id** | **str**| Category ID |  |
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
| **body** | [**KnowledgeCategoryRequest**](KnowledgeCategoryRequest.html)|  |  |
{: class="table table-striped"}

### Return type

[**KnowledgeExtendedCategory**](KnowledgeExtendedCategory.html)

<a name="patch_knowledge_knowledgebase_language_document"></a>

## [**KnowledgeDocument**](KnowledgeDocument.html) patch_knowledge_knowledgebase_language_document(document_id, knowledge_base_id, language_code, body)



Update document



Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/{documentId} 

Requires ALL permissions: 

* knowledge:document:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
document_id = 'document_id_example' # str | Document ID
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE
body = PureCloudPlatformClientV2.KnowledgeDocumentRequest() # KnowledgeDocumentRequest | 

try:
    # Update document
    api_response = api_instance.patch_knowledge_knowledgebase_language_document(document_id, knowledge_base_id, language_code, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_language_document: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
| **body** | [**KnowledgeDocumentRequest**](KnowledgeDocumentRequest.html)|  |  |
{: class="table table-striped"}

### Return type

[**KnowledgeDocument**](KnowledgeDocument.html)

<a name="patch_knowledge_knowledgebase_language_documents"></a>

## [**DocumentListing**](DocumentListing.html) patch_knowledge_knowledgebase_language_documents(knowledge_base_id, language_code, body)



Update documents collection



Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents 

Requires ALL permissions: 

* knowledge:document:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE
body = [PureCloudPlatformClientV2.KnowledgeDocumentBulkRequest()] # list[KnowledgeDocumentBulkRequest] | 

try:
    # Update documents collection
    api_response = api_instance.patch_knowledge_knowledgebase_language_documents(knowledge_base_id, language_code, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_language_documents: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
| **body** | [**list[KnowledgeDocumentBulkRequest]**](KnowledgeDocumentBulkRequest.html)|  |  |
{: class="table table-striped"}

### Return type

[**DocumentListing**](DocumentListing.html)

<a name="post_knowledge_knowledgebase_language_categories"></a>

## [**KnowledgeExtendedCategory**](KnowledgeExtendedCategory.html) post_knowledge_knowledgebase_language_categories(knowledge_base_id, language_code, body)



Create new category



Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/categories 

Requires ALL permissions: 

* knowledge:category:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE
body = PureCloudPlatformClientV2.KnowledgeCategoryRequest() # KnowledgeCategoryRequest | 

try:
    # Create new category
    api_response = api_instance.post_knowledge_knowledgebase_language_categories(knowledge_base_id, language_code, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->post_knowledge_knowledgebase_language_categories: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
| **body** | [**KnowledgeCategoryRequest**](KnowledgeCategoryRequest.html)|  |  |
{: class="table table-striped"}

### Return type

[**KnowledgeExtendedCategory**](KnowledgeExtendedCategory.html)

<a name="post_knowledge_knowledgebase_language_documents"></a>

## [**KnowledgeDocument**](KnowledgeDocument.html) post_knowledge_knowledgebase_language_documents(knowledge_base_id, language_code, body)



Create document



Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents 

Requires ALL permissions: 

* knowledge:document:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE
body = PureCloudPlatformClientV2.KnowledgeDocumentRequest() # KnowledgeDocumentRequest | 

try:
    # Create document
    api_response = api_instance.post_knowledge_knowledgebase_language_documents(knowledge_base_id, language_code, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->post_knowledge_knowledgebase_language_documents: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
| **body** | [**KnowledgeDocumentRequest**](KnowledgeDocumentRequest.html)|  |  |
{: class="table table-striped"}

### Return type

[**KnowledgeDocument**](KnowledgeDocument.html)

<a name="post_knowledge_knowledgebase_language_training_promote"></a>

## [**KnowledgeTraining**](KnowledgeTraining.html) post_knowledge_knowledgebase_language_training_promote(knowledge_base_id, language_code, training_id)



Promote trained documents from draft state to active.



Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/trainings/{trainingId}/promote 

Requires ALL permissions: 

* knowledge:training:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE
training_id = 'training_id_example' # str | Training ID

try:
    # Promote trained documents from draft state to active.
    api_response = api_instance.post_knowledge_knowledgebase_language_training_promote(knowledge_base_id, language_code, training_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->post_knowledge_knowledgebase_language_training_promote: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
| **training_id** | **str**| Training ID |  |
{: class="table table-striped"}

### Return type

[**KnowledgeTraining**](KnowledgeTraining.html)

<a name="post_knowledge_knowledgebase_language_trainings"></a>

## [**KnowledgeTraining**](KnowledgeTraining.html) post_knowledge_knowledgebase_language_trainings(knowledge_base_id, language_code)



Trigger training



Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/trainings 

Requires ALL permissions: 

* knowledge:training:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
language_code = 'en-US' # str | Language code, format: iso2-LOCALE

try:
    # Trigger training
    api_response = api_instance.post_knowledge_knowledgebase_language_trainings(knowledge_base_id, language_code)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->post_knowledge_knowledgebase_language_trainings: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, de-DE |
{: class="table table-striped"}

### Return type

[**KnowledgeTraining**](KnowledgeTraining.html)

<a name="post_knowledge_knowledgebase_search"></a>

## [**KnowledgeSearchResponse**](KnowledgeSearchResponse.html) post_knowledge_knowledgebase_search(knowledge_base_id, body=body)



Search Documents



Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/search 

Requires ALL permissions: 

* knowledge:knowledgebase:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
body = PureCloudPlatformClientV2.KnowledgeSearchRequest() # KnowledgeSearchRequest |  (optional)

try:
    # Search Documents
    api_response = api_instance.post_knowledge_knowledgebase_search(knowledge_base_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->post_knowledge_knowledgebase_search: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeSearchRequest**](KnowledgeSearchRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**KnowledgeSearchResponse**](KnowledgeSearchResponse.html)

<a name="post_knowledge_knowledgebases"></a>

## [**KnowledgeBase**](KnowledgeBase.html) post_knowledge_knowledgebases(body)



Create new knowledge base



Wraps POST /api/v2/knowledge/knowledgebases 

Requires ALL permissions: 

* knowledge:knowledgebase:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
body = PureCloudPlatformClientV2.KnowledgeBase() # KnowledgeBase | 

try:
    # Create new knowledge base
    api_response = api_instance.post_knowledge_knowledgebases(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KnowledgeApi->post_knowledge_knowledgebases: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**KnowledgeBase**](KnowledgeBase.html)|  |  |
{: class="table table-striped"}

### Return type

[**KnowledgeBase**](KnowledgeBase.html)


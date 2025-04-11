# KnowledgeApi

## PureCloudPlatformClientV2.KnowledgeApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_knowledge_knowledgebase**](#delete_knowledge_knowledgebase) | Delete knowledge base|
|[**delete_knowledge_knowledgebase_category**](#delete_knowledge_knowledgebase_category) | Delete category|
|[**delete_knowledge_knowledgebase_document**](#delete_knowledge_knowledgebase_document) | Delete document.|
|[**delete_knowledge_knowledgebase_document_variation**](#delete_knowledge_knowledgebase_document_variation) | Delete a variation for a document.|
|[**delete_knowledge_knowledgebase_export_job**](#delete_knowledge_knowledgebase_export_job) | Delete export job|
|[**delete_knowledge_knowledgebase_import_job**](#delete_knowledge_knowledgebase_import_job) | Delete import job|
|[**delete_knowledge_knowledgebase_label**](#delete_knowledge_knowledgebase_label) | Delete label|
|[**delete_knowledge_knowledgebase_language_category**](#delete_knowledge_knowledgebase_language_category) | Delete category|
|[**delete_knowledge_knowledgebase_language_document**](#delete_knowledge_knowledgebase_language_document) | Delete document|
|[**delete_knowledge_knowledgebase_language_documents_import**](#delete_knowledge_knowledgebase_language_documents_import) | Delete import operation|
|[**delete_knowledge_knowledgebase_sources_salesforce_source_id**](#delete_knowledge_knowledgebase_sources_salesforce_source_id) | Delete Salesforce Knowledge integration source|
|[**delete_knowledge_knowledgebase_sources_servicenow_source_id**](#delete_knowledge_knowledgebase_sources_servicenow_source_id) | Delete ServiceNow Knowledge integration source|
|[**delete_knowledge_knowledgebase_synchronize_job**](#delete_knowledge_knowledgebase_synchronize_job) | Delete synchronization job|
|[**get_knowledge_guest_session_categories**](#get_knowledge_guest_session_categories) | Get categories|
|[**get_knowledge_guest_session_document**](#get_knowledge_guest_session_document) | Get a knowledge document by ID.|
|[**get_knowledge_guest_session_documents**](#get_knowledge_guest_session_documents) | Get documents.|
|[**get_knowledge_integration_options**](#get_knowledge_integration_options) | Get sync options available for a knowledge-connect integration|
|[**get_knowledge_knowledgebase**](#get_knowledge_knowledgebase) | Get knowledge base|
|[**get_knowledge_knowledgebase_categories**](#get_knowledge_knowledgebase_categories) | Get categories|
|[**get_knowledge_knowledgebase_category**](#get_knowledge_knowledgebase_category) | Get category|
|[**get_knowledge_knowledgebase_document**](#get_knowledge_knowledgebase_document) | Get document.|
|[**get_knowledge_knowledgebase_document_feedback**](#get_knowledge_knowledgebase_document_feedback) | Get a list of feedback records given on a document|
|[**get_knowledge_knowledgebase_document_feedback_feedback_id**](#get_knowledge_knowledgebase_document_feedback_feedback_id) | Get a single feedback record given on a document|
|[**get_knowledge_knowledgebase_document_variation**](#get_knowledge_knowledgebase_document_variation) | Get a variation for a document.|
|[**get_knowledge_knowledgebase_document_variations**](#get_knowledge_knowledgebase_document_variations) | Get variations for a document.|
|[**get_knowledge_knowledgebase_document_version**](#get_knowledge_knowledgebase_document_version) | Get document version.|
|[**get_knowledge_knowledgebase_document_version_variation**](#get_knowledge_knowledgebase_document_version_variation) | Get variation for the given document version.|
|[**get_knowledge_knowledgebase_document_version_variations**](#get_knowledge_knowledgebase_document_version_variations) | Get variations for the given document version.|
|[**get_knowledge_knowledgebase_document_versions**](#get_knowledge_knowledgebase_document_versions) | Get document versions.|
|[**get_knowledge_knowledgebase_documents**](#get_knowledge_knowledgebase_documents) | Get documents.|
|[**get_knowledge_knowledgebase_export_job**](#get_knowledge_knowledgebase_export_job) | Get export job report|
|[**get_knowledge_knowledgebase_import_job**](#get_knowledge_knowledgebase_import_job) | Get import job report|
|[**get_knowledge_knowledgebase_label**](#get_knowledge_knowledgebase_label) | Get label|
|[**get_knowledge_knowledgebase_labels**](#get_knowledge_knowledgebase_labels) | Get labels|
|[**get_knowledge_knowledgebase_language_categories**](#get_knowledge_knowledgebase_language_categories) | Get categories|
|[**get_knowledge_knowledgebase_language_category**](#get_knowledge_knowledgebase_language_category) | Get category|
|[**get_knowledge_knowledgebase_language_document**](#get_knowledge_knowledgebase_language_document) | Get document|
|[**get_knowledge_knowledgebase_language_document_upload**](#get_knowledge_knowledgebase_language_document_upload) | Get document content upload status|
|[**get_knowledge_knowledgebase_language_documents**](#get_knowledge_knowledgebase_language_documents) | Get documents|
|[**get_knowledge_knowledgebase_language_documents_import**](#get_knowledge_knowledgebase_language_documents_import) | Get import operation report|
|[**get_knowledge_knowledgebase_language_training**](#get_knowledge_knowledgebase_language_training) | Get training detail|
|[**get_knowledge_knowledgebase_language_trainings**](#get_knowledge_knowledgebase_language_trainings) | Get all trainings information for a knowledgebase|
|[**get_knowledge_knowledgebase_operations**](#get_knowledge_knowledgebase_operations) | Get operations|
|[**get_knowledge_knowledgebase_operations_users_query**](#get_knowledge_knowledgebase_operations_users_query) | Get ids of operation creator users and oauth clients|
|[**get_knowledge_knowledgebase_parse_job**](#get_knowledge_knowledgebase_parse_job) | Get parse job report|
|[**get_knowledge_knowledgebase_sources**](#get_knowledge_knowledgebase_sources) | Get Knowledge integration sources|
|[**get_knowledge_knowledgebase_sources_salesforce_source_id**](#get_knowledge_knowledgebase_sources_salesforce_source_id) | Get Salesforce Knowledge integration source|
|[**get_knowledge_knowledgebase_sources_servicenow_source_id**](#get_knowledge_knowledgebase_sources_servicenow_source_id) | Get ServiceNow Knowledge integration source|
|[**get_knowledge_knowledgebase_synchronize_job**](#get_knowledge_knowledgebase_synchronize_job) | Get synchronization job report|
|[**get_knowledge_knowledgebase_unanswered_group**](#get_knowledge_knowledgebase_unanswered_group) | Get knowledge base unanswered group for a particular groupId|
|[**get_knowledge_knowledgebase_unanswered_group_phrasegroup**](#get_knowledge_knowledgebase_unanswered_group_phrasegroup) | Get knowledge base unanswered phrase group for a particular phraseGroupId|
|[**get_knowledge_knowledgebase_unanswered_groups**](#get_knowledge_knowledgebase_unanswered_groups) | Get knowledge base unanswered groups|
|[**get_knowledge_knowledgebase_uploads_urls_job**](#get_knowledge_knowledgebase_uploads_urls_job) | Get content upload from URL job status|
|[**get_knowledge_knowledgebases**](#get_knowledge_knowledgebases) | Get knowledge bases|
|[**patch_knowledge_guest_session_documents_search_search_id**](#patch_knowledge_guest_session_documents_search_search_id) | Update search result.|
|[**patch_knowledge_knowledgebase**](#patch_knowledge_knowledgebase) | Update knowledge base|
|[**patch_knowledge_knowledgebase_category**](#patch_knowledge_knowledgebase_category) | Update category|
|[**patch_knowledge_knowledgebase_document**](#patch_knowledge_knowledgebase_document) | Update document.|
|[**patch_knowledge_knowledgebase_document_feedback_feedback_id**](#patch_knowledge_knowledgebase_document_feedback_feedback_id) | Update feedback on a document|
|[**patch_knowledge_knowledgebase_document_variation**](#patch_knowledge_knowledgebase_document_variation) | Update a variation for a document.|
|[**patch_knowledge_knowledgebase_documents_search_search_id**](#patch_knowledge_knowledgebase_documents_search_search_id) | Update search result.|
|[**patch_knowledge_knowledgebase_import_job**](#patch_knowledge_knowledgebase_import_job) | Start import job|
|[**patch_knowledge_knowledgebase_label**](#patch_knowledge_knowledgebase_label) | Update label|
|[**patch_knowledge_knowledgebase_language_category**](#patch_knowledge_knowledgebase_language_category) | Update category|
|[**patch_knowledge_knowledgebase_language_document**](#patch_knowledge_knowledgebase_language_document) | Update document|
|[**patch_knowledge_knowledgebase_language_documents**](#patch_knowledge_knowledgebase_language_documents) | Update documents collection|
|[**patch_knowledge_knowledgebase_language_documents_import**](#patch_knowledge_knowledgebase_language_documents_import) | Start import operation|
|[**patch_knowledge_knowledgebase_parse_job**](#patch_knowledge_knowledgebase_parse_job) | Send update to the parse operation|
|[**patch_knowledge_knowledgebase_synchronize_job**](#patch_knowledge_knowledgebase_synchronize_job) | Update synchronization job|
|[**patch_knowledge_knowledgebase_unanswered_group_phrasegroup**](#patch_knowledge_knowledgebase_unanswered_group_phrasegroup) | Update a Knowledge base unanswered phrase group|
|[**post_knowledge_documentuploads**](#post_knowledge_documentuploads) | Creates a presigned URL for uploading a knowledge import file with a set of documents|
|[**post_knowledge_guest_session_document_copies**](#post_knowledge_guest_session_document_copies) | Indicate that the document was copied by the user.|
|[**post_knowledge_guest_session_document_feedback**](#post_knowledge_guest_session_document_feedback) | Give feedback on a document|
|[**post_knowledge_guest_session_document_views**](#post_knowledge_guest_session_document_views) | Create view event for a document.|
|[**post_knowledge_guest_session_documents_answers**](#post_knowledge_guest_session_documents_answers) | Answer documents.|
|[**post_knowledge_guest_session_documents_presentations**](#post_knowledge_guest_session_documents_presentations) | Indicate that documents were presented to the user.|
|[**post_knowledge_guest_session_documents_search**](#post_knowledge_guest_session_documents_search) | Search the documents in a guest session.|
|[**post_knowledge_guest_session_documents_search_suggestions**](#post_knowledge_guest_session_documents_search_suggestions) | Query the knowledge documents to provide suggestions for auto completion.|
|[**post_knowledge_guest_sessions**](#post_knowledge_guest_sessions) | Create guest session|
|[**post_knowledge_knowledgebase_categories**](#post_knowledge_knowledgebase_categories) | Create new category|
|[**post_knowledge_knowledgebase_document_copies**](#post_knowledge_knowledgebase_document_copies) | Indicate that the document was copied by the user.|
|[**post_knowledge_knowledgebase_document_feedback**](#post_knowledge_knowledgebase_document_feedback) | Give feedback on a document|
|[**post_knowledge_knowledgebase_document_variations**](#post_knowledge_knowledgebase_document_variations) | Create a variation for a document.|
|[**post_knowledge_knowledgebase_document_versions**](#post_knowledge_knowledgebase_document_versions) | Creates or restores a document version.|
|[**post_knowledge_knowledgebase_document_views**](#post_knowledge_knowledgebase_document_views) | Create view for a document.|
|[**post_knowledge_knowledgebase_documents**](#post_knowledge_knowledgebase_documents) | Create document.|
|[**post_knowledge_knowledgebase_documents_answers**](#post_knowledge_knowledgebase_documents_answers) | Answer documents.|
|[**post_knowledge_knowledgebase_documents_bulk_remove**](#post_knowledge_knowledgebase_documents_bulk_remove) | Bulk remove documents.|
|[**post_knowledge_knowledgebase_documents_bulk_update**](#post_knowledge_knowledgebase_documents_bulk_update) | Bulk update documents.|
|[**post_knowledge_knowledgebase_documents_presentations**](#post_knowledge_knowledgebase_documents_presentations) | Indicate that documents were presented to the user.|
|[**post_knowledge_knowledgebase_documents_query**](#post_knowledge_knowledgebase_documents_query) | Query for knowledge documents.|
|[**post_knowledge_knowledgebase_documents_search**](#post_knowledge_knowledgebase_documents_search) | Search the documents in a knowledge base.|
|[**post_knowledge_knowledgebase_documents_search_suggestions**](#post_knowledge_knowledgebase_documents_search_suggestions) | Query the knowledge documents to provide suggestions for auto completion.|
|[**post_knowledge_knowledgebase_documents_versions_bulk_add**](#post_knowledge_knowledgebase_documents_versions_bulk_add) | Bulk add document versions.|
|[**post_knowledge_knowledgebase_export_jobs**](#post_knowledge_knowledgebase_export_jobs) | Create export job|
|[**post_knowledge_knowledgebase_import_jobs**](#post_knowledge_knowledgebase_import_jobs) | Create import job|
|[**post_knowledge_knowledgebase_labels**](#post_knowledge_knowledgebase_labels) | Create new label|
|[**post_knowledge_knowledgebase_language_categories**](#post_knowledge_knowledgebase_language_categories) | Create new category|
|[**post_knowledge_knowledgebase_language_document_uploads**](#post_knowledge_knowledgebase_language_document_uploads) | Upload Article Content|
|[**post_knowledge_knowledgebase_language_documents**](#post_knowledge_knowledgebase_language_documents) | Create document|
|[**post_knowledge_knowledgebase_language_documents_imports**](#post_knowledge_knowledgebase_language_documents_imports) | Create import operation|
|[**post_knowledge_knowledgebase_language_training_promote**](#post_knowledge_knowledgebase_language_training_promote) | Promote trained documents from draft state to active.|
|[**post_knowledge_knowledgebase_language_trainings**](#post_knowledge_knowledgebase_language_trainings) | Trigger training|
|[**post_knowledge_knowledgebase_parse_job_import**](#post_knowledge_knowledgebase_parse_job_import) | Import the parsed articles|
|[**post_knowledge_knowledgebase_parse_jobs**](#post_knowledge_knowledgebase_parse_jobs) | Create parse job|
|[**post_knowledge_knowledgebase_search**](#post_knowledge_knowledgebase_search) | Search Documents|
|[**post_knowledge_knowledgebase_sources_salesforce**](#post_knowledge_knowledgebase_sources_salesforce) | Create Salesforce Knowledge integration source|
|[**post_knowledge_knowledgebase_sources_salesforce_source_id_sync**](#post_knowledge_knowledgebase_sources_salesforce_source_id_sync) | Start sync on Salesforce Knowledge integration source|
|[**post_knowledge_knowledgebase_sources_servicenow**](#post_knowledge_knowledgebase_sources_servicenow) | Create ServiceNow Knowledge integration source|
|[**post_knowledge_knowledgebase_sources_servicenow_source_id_sync**](#post_knowledge_knowledgebase_sources_servicenow_source_id_sync) | Start synchronization on ServiceNow Knowledge integration source|
|[**post_knowledge_knowledgebase_synchronize_jobs**](#post_knowledge_knowledgebase_synchronize_jobs) | Create synchronization job|
|[**post_knowledge_knowledgebase_uploads_urls_jobs**](#post_knowledge_knowledgebase_uploads_urls_jobs) | Create content upload from URL job|
|[**post_knowledge_knowledgebases**](#post_knowledge_knowledgebases) | Create new knowledge base|
|[**put_knowledge_knowledgebase_sources_salesforce_source_id**](#put_knowledge_knowledgebase_sources_salesforce_source_id) | Update Salesforce Knowledge integration source|
|[**put_knowledge_knowledgebase_sources_servicenow_source_id**](#put_knowledge_knowledgebase_sources_servicenow_source_id) | Update ServiceNow Knowledge integration source|



## delete_knowledge_knowledgebase

> [**KnowledgeBase**](KnowledgeBase) delete_knowledge_knowledgebase(knowledge_base_id)


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
    print("Exception when calling KnowledgeApi->delete_knowledge_knowledgebase: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |

### Return type

[**KnowledgeBase**](KnowledgeBase)


## delete_knowledge_knowledgebase_category

> [**CategoryResponse**](CategoryResponse) delete_knowledge_knowledgebase_category(knowledge_base_id, category_id)


Delete category

Wraps DELETE /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/categories/{categoryId} 

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
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
category_id = 'category_id_example' # str | Category ID

try:
    # Delete category
    api_response = api_instance.delete_knowledge_knowledgebase_category(knowledge_base_id, category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->delete_knowledge_knowledgebase_category: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **category_id** | **str**| Category ID |  |

### Return type

[**CategoryResponse**](CategoryResponse)


## delete_knowledge_knowledgebase_document

>  delete_knowledge_knowledgebase_document(knowledge_base_id, document_id)


Delete document.

Wraps DELETE /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId} 

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
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID.
document_id = 'document_id_example' # str | Document ID.

try:
    # Delete document.
    api_instance.delete_knowledge_knowledgebase_document(knowledge_base_id, document_id)
except ApiException as e:
    print("Exception when calling KnowledgeApi->delete_knowledge_knowledgebase_document: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID. |  |
| **document_id** | **str**| Document ID. |  |

### Return type

void (empty response body)


## delete_knowledge_knowledgebase_document_variation

>  delete_knowledge_knowledgebase_document_variation(document_variation_id, document_id, knowledge_base_id)


Delete a variation for a document.

Wraps DELETE /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/variations/{documentVariationId} 

Requires ANY permissions: 

* knowledge:document:delete
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
document_variation_id = 'document_variation_id_example' # str | Globally unique identifier for a document variation.
document_id = 'document_id_example' # str | Globally unique identifier for a document.
knowledge_base_id = 'knowledge_base_id_example' # str | Globally unique identifier for a knowledge base.

try:
    # Delete a variation for a document.
    api_instance.delete_knowledge_knowledgebase_document_variation(document_variation_id, document_id, knowledge_base_id)
except ApiException as e:
    print("Exception when calling KnowledgeApi->delete_knowledge_knowledgebase_document_variation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_variation_id** | **str**| Globally unique identifier for a document variation. |  |
| **document_id** | **str**| Globally unique identifier for a document. |  |
| **knowledge_base_id** | **str**| Globally unique identifier for a knowledge base. |  |

### Return type

void (empty response body)


## delete_knowledge_knowledgebase_export_job

>  delete_knowledge_knowledgebase_export_job(knowledge_base_id, export_job_id)


Delete export job

Wraps DELETE /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/export/jobs/{exportJobId} 

Requires ALL permissions: 

* knowledge:exportJob:delete

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
export_job_id = 'export_job_id_example' # str | Export job ID

try:
    # Delete export job
    api_instance.delete_knowledge_knowledgebase_export_job(knowledge_base_id, export_job_id)
except ApiException as e:
    print("Exception when calling KnowledgeApi->delete_knowledge_knowledgebase_export_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **export_job_id** | **str**| Export job ID |  |

### Return type

void (empty response body)


## delete_knowledge_knowledgebase_import_job

>  delete_knowledge_knowledgebase_import_job(knowledge_base_id, import_job_id)


Delete import job

Wraps DELETE /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/import/jobs/{importJobId} 

Requires ALL permissions: 

* knowledge:importJob:delete

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
import_job_id = 'import_job_id_example' # str | Import job ID

try:
    # Delete import job
    api_instance.delete_knowledge_knowledgebase_import_job(knowledge_base_id, import_job_id)
except ApiException as e:
    print("Exception when calling KnowledgeApi->delete_knowledge_knowledgebase_import_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **import_job_id** | **str**| Import job ID |  |

### Return type

void (empty response body)


## delete_knowledge_knowledgebase_label

> [**LabelResponse**](LabelResponse) delete_knowledge_knowledgebase_label(knowledge_base_id, label_id)


Delete label

Wraps DELETE /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/labels/{labelId} 

Requires ALL permissions: 

* knowledge:label:delete

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
label_id = 'label_id_example' # str | Label ID

try:
    # Delete label
    api_response = api_instance.delete_knowledge_knowledgebase_label(knowledge_base_id, label_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->delete_knowledge_knowledgebase_label: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **label_id** | **str**| Label ID |  |

### Return type

[**LabelResponse**](LabelResponse)


## delete_knowledge_knowledgebase_language_category

> [**KnowledgeCategory**](KnowledgeCategory) delete_knowledge_knowledgebase_language_category(category_id, knowledge_base_id, language_code)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
    print("Exception when calling KnowledgeApi->delete_knowledge_knowledgebase_language_category: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **category_id** | **str**| Category ID |  |
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |

### Return type

[**KnowledgeCategory**](KnowledgeCategory)


## delete_knowledge_knowledgebase_language_document

> [**KnowledgeDocument**](KnowledgeDocument) delete_knowledge_knowledgebase_language_document(document_id, knowledge_base_id, language_code)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
    print("Exception when calling KnowledgeApi->delete_knowledge_knowledgebase_language_document: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |

### Return type

[**KnowledgeDocument**](KnowledgeDocument)


## delete_knowledge_knowledgebase_language_documents_import

>  delete_knowledge_knowledgebase_language_documents_import(knowledge_base_id, language_code, import_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Delete import operation

Wraps DELETE /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/imports/{importId} 

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
import_id = 'import_id_example' # str | Import ID

try:
    # Delete import operation
    api_instance.delete_knowledge_knowledgebase_language_documents_import(knowledge_base_id, language_code, import_id)
except ApiException as e:
    print("Exception when calling KnowledgeApi->delete_knowledge_knowledgebase_language_documents_import: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **import_id** | **str**| Import ID |  |

### Return type

void (empty response body)


## delete_knowledge_knowledgebase_sources_salesforce_source_id

>  delete_knowledge_knowledgebase_sources_salesforce_source_id(knowledge_base_id, source_id)


Delete Salesforce Knowledge integration source

Wraps DELETE /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/salesforce/{sourceId} 

Requires ALL permissions: 

* knowledge:integrationSource:delete

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
source_id = 'source_id_example' # str | Source ID

try:
    # Delete Salesforce Knowledge integration source
    api_instance.delete_knowledge_knowledgebase_sources_salesforce_source_id(knowledge_base_id, source_id)
except ApiException as e:
    print("Exception when calling KnowledgeApi->delete_knowledge_knowledgebase_sources_salesforce_source_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **source_id** | **str**| Source ID |  |

### Return type

void (empty response body)


## delete_knowledge_knowledgebase_sources_servicenow_source_id

>  delete_knowledge_knowledgebase_sources_servicenow_source_id(knowledge_base_id, source_id)


Delete ServiceNow Knowledge integration source

Wraps DELETE /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/servicenow/{sourceId} 

Requires ALL permissions: 

* knowledge:integrationSource:delete

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
source_id = 'source_id_example' # str | Source ID

try:
    # Delete ServiceNow Knowledge integration source
    api_instance.delete_knowledge_knowledgebase_sources_servicenow_source_id(knowledge_base_id, source_id)
except ApiException as e:
    print("Exception when calling KnowledgeApi->delete_knowledge_knowledgebase_sources_servicenow_source_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **source_id** | **str**| Source ID |  |

### Return type

void (empty response body)


## delete_knowledge_knowledgebase_synchronize_job

>  delete_knowledge_knowledgebase_synchronize_job(knowledge_base_id, sync_job_id)


Delete synchronization job

Wraps DELETE /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/synchronize/jobs/{syncJobId} 

Requires ALL permissions: 

* knowledge:syncJob:delete

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
sync_job_id = 'sync_job_id_example' # str | Synchronization job ID

try:
    # Delete synchronization job
    api_instance.delete_knowledge_knowledgebase_synchronize_job(knowledge_base_id, sync_job_id)
except ApiException as e:
    print("Exception when calling KnowledgeApi->delete_knowledge_knowledgebase_synchronize_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **sync_job_id** | **str**| Synchronization job ID |  |

### Return type

void (empty response body)


## get_knowledge_guest_session_categories

> [**GuestCategoryResponseListing**](GuestCategoryResponseListing) get_knowledge_guest_session_categories(session_id, before=before, after=after, page_size=page_size, parent_id=parent_id, is_root=is_root, name=name, sort_by=sort_by, expand=expand, include_document_count=include_document_count)


Get categories

Wraps GET /api/v2/knowledge/guest/sessions/{sessionId}/categories 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
session_id = 'session_id_example' # str | Knowledge guest session ID.
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
parent_id = 'parent_id_example' # str | If specified, retrieves the children categories by parent category ID. (optional)
is_root = True # bool | If specified, retrieves only the root categories. (optional)
name = 'name_example' # str | Filter to return the categories that starts with the given category name. (optional)
sort_by = ''Name'' # str | Name: sort by category names alphabetically; Hierarchy: sort by the full path of hierarchical category names alphabetically (optional) (default to 'Name')
expand = 'expand_example' # str | The specified entity attribute will be filled. Supported value:\"Ancestors\": every ancestors will be filled via the parent attribute recursively,but only the id, name, parentId will be present for the ancestors. (optional)
include_document_count = True # bool | If specified, retrieves the number of documents related to category. (optional)

try:
    # Get categories
    api_response = api_instance.get_knowledge_guest_session_categories(session_id, before=before, after=after, page_size=page_size, parent_id=parent_id, is_root=is_root, name=name, sort_by=sort_by, expand=expand, include_document_count=include_document_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_guest_session_categories: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| Knowledge guest session ID. |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **parent_id** | **str**| If specified, retrieves the children categories by parent category ID. | [optional]  |
| **is_root** | **bool**| If specified, retrieves only the root categories. | [optional]  |
| **name** | **str**| Filter to return the categories that starts with the given category name. | [optional]  |
| **sort_by** | **str**| Name: sort by category names alphabetically; Hierarchy: sort by the full path of hierarchical category names alphabetically | [optional] [default to &#39;Name&#39;]<br />**Values**: Name, Hierarchy |
| **expand** | **str**| The specified entity attribute will be filled. Supported value:\&quot;Ancestors\&quot;: every ancestors will be filled via the parent attribute recursively,but only the id, name, parentId will be present for the ancestors. | [optional]  |
| **include_document_count** | **bool**| If specified, retrieves the number of documents related to category. | [optional]  |

### Return type

[**GuestCategoryResponseListing**](GuestCategoryResponseListing)


## get_knowledge_guest_session_document

> [**KnowledgeGuestDocumentResponse**](KnowledgeGuestDocumentResponse) get_knowledge_guest_session_document(session_id, document_id)


Get a knowledge document by ID.

Wraps GET /api/v2/knowledge/guest/sessions/{sessionId}/documents/{documentId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
session_id = 'session_id_example' # str | Knowledge guest session ID.
document_id = 'document_id_example' # str | Document ID

try:
    # Get a knowledge document by ID.
    api_response = api_instance.get_knowledge_guest_session_document(session_id, document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_guest_session_document: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| Knowledge guest session ID. |  |
| **document_id** | **str**| Document ID |  |

### Return type

[**KnowledgeGuestDocumentResponse**](KnowledgeGuestDocumentResponse)


## get_knowledge_guest_session_documents

> [**KnowledgeGuestDocumentResponseListing**](KnowledgeGuestDocumentResponseListing) get_knowledge_guest_session_documents(session_id, category_id=category_id, page_size=page_size)


Get documents.

Wraps GET /api/v2/knowledge/guest/sessions/{sessionId}/documents 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
session_id = 'session_id_example' # str | Knowledge guest session ID.
category_id = ['category_id_example'] # list[str] | If specified, retrieves documents associated with category ids, comma separated values expected. (optional)
page_size = 56 # int | Number of entities to return. Maximum of 200. (optional)

try:
    # Get documents.
    api_response = api_instance.get_knowledge_guest_session_documents(session_id, category_id=category_id, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_guest_session_documents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| Knowledge guest session ID. |  |
| **category_id** | [**list[str]**](str)| If specified, retrieves documents associated with category ids, comma separated values expected. | [optional]  |
| **page_size** | **int**| Number of entities to return. Maximum of 200. | [optional]  |

### Return type

[**KnowledgeGuestDocumentResponseListing**](KnowledgeGuestDocumentResponseListing)


## get_knowledge_integration_options

> [**KnowledgeIntegrationOptionsResponse**](KnowledgeIntegrationOptionsResponse) get_knowledge_integration_options(integration_id, knowledge_base_ids=knowledge_base_ids)


Get sync options available for a knowledge-connect integration

Wraps GET /api/v2/knowledge/integrations/{integrationId}/options 

Requires ALL permissions: 

* knowledge:integrationOptions:view

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
integration_id = 'integration_id_example' # str | Integration ID
knowledge_base_ids = ['knowledge_base_ids_example'] # list[str] | Narrowing down filtering option results by knowledge base. (optional)

try:
    # Get sync options available for a knowledge-connect integration
    api_response = api_instance.get_knowledge_integration_options(integration_id, knowledge_base_ids=knowledge_base_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_integration_options: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **knowledge_base_ids** | [**list[str]**](str)| Narrowing down filtering option results by knowledge base. | [optional]  |

### Return type

[**KnowledgeIntegrationOptionsResponse**](KnowledgeIntegrationOptionsResponse)


## get_knowledge_knowledgebase

> [**KnowledgeBase**](KnowledgeBase) get_knowledge_knowledgebase(knowledge_base_id)


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
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |

### Return type

[**KnowledgeBase**](KnowledgeBase)


## get_knowledge_knowledgebase_categories

> [**CategoryResponseListing**](CategoryResponseListing) get_knowledge_knowledgebase_categories(knowledge_base_id, before=before, after=after, page_size=page_size, parent_id=parent_id, is_root=is_root, name=name, sort_by=sort_by, expand=expand, include_document_count=include_document_count)


Get categories

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/categories 

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
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
parent_id = 'parent_id_example' # str | If specified, retrieves the children categories by parent category ID. (optional)
is_root = True # bool | If specified, retrieves only the root categories. (optional)
name = 'name_example' # str | Filter to return the categories that starts with the given category name. (optional)
sort_by = ''Name'' # str | Name: sort by category names alphabetically; Hierarchy: sort by the full path of hierarchical category names alphabetically (optional) (default to 'Name')
expand = 'expand_example' # str | The specified entity attribute will be filled. Supported value:\"Ancestors\": every ancestors will be filled via the parent attribute recursively,but only the id, name, parentId will be present for the ancestors. (optional)
include_document_count = True # bool | If specified, retrieves the number of documents related to category. (optional)

try:
    # Get categories
    api_response = api_instance.get_knowledge_knowledgebase_categories(knowledge_base_id, before=before, after=after, page_size=page_size, parent_id=parent_id, is_root=is_root, name=name, sort_by=sort_by, expand=expand, include_document_count=include_document_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_categories: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **parent_id** | **str**| If specified, retrieves the children categories by parent category ID. | [optional]  |
| **is_root** | **bool**| If specified, retrieves only the root categories. | [optional]  |
| **name** | **str**| Filter to return the categories that starts with the given category name. | [optional]  |
| **sort_by** | **str**| Name: sort by category names alphabetically; Hierarchy: sort by the full path of hierarchical category names alphabetically | [optional] [default to &#39;Name&#39;]<br />**Values**: Name, Hierarchy |
| **expand** | **str**| The specified entity attribute will be filled. Supported value:\&quot;Ancestors\&quot;: every ancestors will be filled via the parent attribute recursively,but only the id, name, parentId will be present for the ancestors. | [optional]  |
| **include_document_count** | **bool**| If specified, retrieves the number of documents related to category. | [optional]  |

### Return type

[**CategoryResponseListing**](CategoryResponseListing)


## get_knowledge_knowledgebase_category

> [**CategoryResponse**](CategoryResponse) get_knowledge_knowledgebase_category(knowledge_base_id, category_id)


Get category

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/categories/{categoryId} 

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
category_id = 'category_id_example' # str | Category ID

try:
    # Get category
    api_response = api_instance.get_knowledge_knowledgebase_category(knowledge_base_id, category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_category: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **category_id** | **str**| Category ID |  |

### Return type

[**CategoryResponse**](CategoryResponse)


## get_knowledge_knowledgebase_document

> [**KnowledgeDocumentResponse**](KnowledgeDocumentResponse) get_knowledge_knowledgebase_document(knowledge_base_id, document_id, expand=expand, state=state)


Get document.

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId} 

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
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID.
document_id = 'document_id_example' # str | Document ID.
expand = ['expand_example'] # list[str] | The specified entity attributes will be filled. Comma separated values expected. Max No. of variations that can be returned on expand is 20. (optional)
state = 'state_example' # str | \"when state is \"Draft\", draft version of the document is returned,otherwise by default published version is returned in the response. (optional)

try:
    # Get document.
    api_response = api_instance.get_knowledge_knowledgebase_document(knowledge_base_id, document_id, expand=expand, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_document: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID. |  |
| **document_id** | **str**| Document ID. |  |
| **expand** | [**list[str]**](str)| The specified entity attributes will be filled. Comma separated values expected. Max No. of variations that can be returned on expand is 20. | [optional] <br />**Values**: category, labels, variations |
| **state** | **str**| \&quot;when state is \&quot;Draft\&quot;, draft version of the document is returned,otherwise by default published version is returned in the response. | [optional] <br />**Values**: Draft, Published |

### Return type

[**KnowledgeDocumentResponse**](KnowledgeDocumentResponse)


## get_knowledge_knowledgebase_document_feedback

> [**KnowledgeDocumentFeedbackResponseListing**](KnowledgeDocumentFeedbackResponseListing) get_knowledge_knowledgebase_document_feedback(knowledge_base_id, document_id, before=before, after=after, page_size=page_size, only_commented=only_commented, document_version_id=document_version_id, document_variation_id=document_variation_id, app_type=app_type, query_type=query_type, user_id=user_id, queue_id=queue_id, state=state)


Get a list of feedback records given on a document

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/feedback 

Requires ANY permissions: 

* knowledge:feedback:view

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
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID.
document_id = 'document_id_example' # str | Document ID.
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
only_commented = True # bool | If true, only feedback records that have comment are returned. If false, feedback records with and without comment are returned. Default: false. (optional)
document_version_id = 'document_version_id_example' # str | Document version ID to filter by. Supported only if onlyCommented=true is set. (optional)
document_variation_id = 'document_variation_id_example' # str | Document variation ID to filter by. Supported only if onlyCommented=true is set. (optional)
app_type = 'app_type_example' # str | Application type to filter by. Supported only if onlyCommented=true is set. (optional)
query_type = 'query_type_example' # str | Query type to filter by. Supported only if onlyCommented=true is set. (optional)
user_id = 'user_id_example' # str | The ID of the user, who created the feedback, to filter by. Supported only if onlyCommented=true is set. (optional)
queue_id = 'queue_id_example' # str | Queue ID to filter by. Supported only if onlyCommented=true is set. (optional)
state = 'state_example' # str | State to filter by. Supported only if onlyCommented=true is set. Default: Final (optional)

try:
    # Get a list of feedback records given on a document
    api_response = api_instance.get_knowledge_knowledgebase_document_feedback(knowledge_base_id, document_id, before=before, after=after, page_size=page_size, only_commented=only_commented, document_version_id=document_version_id, document_variation_id=document_variation_id, app_type=app_type, query_type=query_type, user_id=user_id, queue_id=queue_id, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_document_feedback: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID. |  |
| **document_id** | **str**| Document ID. |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **only_commented** | **bool**| If true, only feedback records that have comment are returned. If false, feedback records with and without comment are returned. Default: false. | [optional]  |
| **document_version_id** | **str**| Document version ID to filter by. Supported only if onlyCommented&#x3D;true is set. | [optional]  |
| **document_variation_id** | **str**| Document variation ID to filter by. Supported only if onlyCommented&#x3D;true is set. | [optional]  |
| **app_type** | **str**| Application type to filter by. Supported only if onlyCommented&#x3D;true is set. | [optional] <br />**Values**: Assistant, BotFlow, MessengerKnowledgeApp, SmartAdvisor, SupportCenter |
| **query_type** | **str**| Query type to filter by. Supported only if onlyCommented&#x3D;true is set. | [optional] <br />**Values**: Unknown, Article, AutoSearch, Category, ManualSearch, Recommendation, Suggestion |
| **user_id** | **str**| The ID of the user, who created the feedback, to filter by. Supported only if onlyCommented&#x3D;true is set. | [optional]  |
| **queue_id** | **str**| Queue ID to filter by. Supported only if onlyCommented&#x3D;true is set. | [optional]  |
| **state** | **str**| State to filter by. Supported only if onlyCommented&#x3D;true is set. Default: Final | [optional] <br />**Values**: All, Draft, Final |

### Return type

[**KnowledgeDocumentFeedbackResponseListing**](KnowledgeDocumentFeedbackResponseListing)


## get_knowledge_knowledgebase_document_feedback_feedback_id

> [**KnowledgeDocumentFeedbackResponse**](KnowledgeDocumentFeedbackResponse) get_knowledge_knowledgebase_document_feedback_feedback_id(knowledge_base_id, document_id, feedback_id)


Get a single feedback record given on a document

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/feedback/{feedbackId} 

Requires ANY permissions: 

* knowledge:feedback:view

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
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID.
document_id = 'document_id_example' # str | Document ID.
feedback_id = 'feedback_id_example' # str | Feedback ID.

try:
    # Get a single feedback record given on a document
    api_response = api_instance.get_knowledge_knowledgebase_document_feedback_feedback_id(knowledge_base_id, document_id, feedback_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_document_feedback_feedback_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID. |  |
| **document_id** | **str**| Document ID. |  |
| **feedback_id** | **str**| Feedback ID. |  |

### Return type

[**KnowledgeDocumentFeedbackResponse**](KnowledgeDocumentFeedbackResponse)


## get_knowledge_knowledgebase_document_variation

> [**DocumentVariationResponse**](DocumentVariationResponse) get_knowledge_knowledgebase_document_variation(document_variation_id, document_id, knowledge_base_id, document_state=document_state, expand=expand)


Get a variation for a document.

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/variations/{documentVariationId} 

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
document_variation_id = 'document_variation_id_example' # str | Globally unique identifier for a document variation.
document_id = 'document_id_example' # str | Globally unique identifier for a document.
knowledge_base_id = 'knowledge_base_id_example' # str | Globally unique identifier for a knowledge base.
document_state = 'document_state_example' # str | The state of the document. (optional)
expand = ['expand_example'] # list[str] | The specified entity attributes will be filled. Comma separated values expected. (optional)

try:
    # Get a variation for a document.
    api_response = api_instance.get_knowledge_knowledgebase_document_variation(document_variation_id, document_id, knowledge_base_id, document_state=document_state, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_document_variation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_variation_id** | **str**| Globally unique identifier for a document variation. |  |
| **document_id** | **str**| Globally unique identifier for a document. |  |
| **knowledge_base_id** | **str**| Globally unique identifier for a knowledge base. |  |
| **document_state** | **str**| The state of the document. | [optional] <br />**Values**: Draft, Published |
| **expand** | [**list[str]**](str)| The specified entity attributes will be filled. Comma separated values expected. | [optional] <br />**Values**: contentUrl |

### Return type

[**DocumentVariationResponse**](DocumentVariationResponse)


## get_knowledge_knowledgebase_document_variations

> [**DocumentVariationResponseListing**](DocumentVariationResponseListing) get_knowledge_knowledgebase_document_variations(knowledge_base_id, document_id, before=before, after=after, page_size=page_size, document_state=document_state, expand=expand)


Get variations for a document.

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/variations 

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
knowledge_base_id = 'knowledge_base_id_example' # str | Globally unique identifier for the knowledge base.
document_id = 'document_id_example' # str | Globally unique identifier for the document.
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
document_state = 'document_state_example' # str | The state of the document. (optional)
expand = ['expand_example'] # list[str] | The specified entity attributes will be filled. Comma separated values expected. (optional)

try:
    # Get variations for a document.
    api_response = api_instance.get_knowledge_knowledgebase_document_variations(knowledge_base_id, document_id, before=before, after=after, page_size=page_size, document_state=document_state, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_document_variations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Globally unique identifier for the knowledge base. |  |
| **document_id** | **str**| Globally unique identifier for the document. |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **document_state** | **str**| The state of the document. | [optional] <br />**Values**: Draft, Published |
| **expand** | [**list[str]**](str)| The specified entity attributes will be filled. Comma separated values expected. | [optional] <br />**Values**: contentUrl |

### Return type

[**DocumentVariationResponseListing**](DocumentVariationResponseListing)


## get_knowledge_knowledgebase_document_version

> [**KnowledgeDocumentVersion**](KnowledgeDocumentVersion) get_knowledge_knowledgebase_document_version(knowledge_base_id, document_id, version_id, expand=expand)


Get document version.

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/versions/{versionId} 

Requires ALL permissions: 

* knowledge:documentVersion:view

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
knowledge_base_id = 'knowledge_base_id_example' # str | Globally unique identifier for the knowledge base.
document_id = 'document_id_example' # str | Globally unique identifier for the document.
version_id = 'version_id_example' # str | Globally unique identifier for the document version.
expand = ['expand_example'] # list[str] | The specified entity attributes will be filled. Comma separated values expected. (optional)

try:
    # Get document version.
    api_response = api_instance.get_knowledge_knowledgebase_document_version(knowledge_base_id, document_id, version_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_document_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Globally unique identifier for the knowledge base. |  |
| **document_id** | **str**| Globally unique identifier for the document. |  |
| **version_id** | **str**| Globally unique identifier for the document version. |  |
| **expand** | [**list[str]**](str)| The specified entity attributes will be filled. Comma separated values expected. | [optional] <br />**Values**: category, labels |

### Return type

[**KnowledgeDocumentVersion**](KnowledgeDocumentVersion)


## get_knowledge_knowledgebase_document_version_variation

> [**KnowledgeDocumentVersionVariation**](KnowledgeDocumentVersionVariation) get_knowledge_knowledgebase_document_version_variation(knowledge_base_id, document_id, version_id, variation_id)


Get variation for the given document version.

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/versions/{versionId}/variations/{variationId} 

Requires ALL permissions: 

* knowledge:documentVersion:view

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
knowledge_base_id = 'knowledge_base_id_example' # str | Globally unique identifier for the knowledge base.
document_id = 'document_id_example' # str | Globally unique identifier for the document.
version_id = 'version_id_example' # str | Globally unique identifier for the document version.
variation_id = 'variation_id_example' # str | Globally unique identifier for the document version variation.

try:
    # Get variation for the given document version.
    api_response = api_instance.get_knowledge_knowledgebase_document_version_variation(knowledge_base_id, document_id, version_id, variation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_document_version_variation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Globally unique identifier for the knowledge base. |  |
| **document_id** | **str**| Globally unique identifier for the document. |  |
| **version_id** | **str**| Globally unique identifier for the document version. |  |
| **variation_id** | **str**| Globally unique identifier for the document version variation. |  |

### Return type

[**KnowledgeDocumentVersionVariation**](KnowledgeDocumentVersionVariation)


## get_knowledge_knowledgebase_document_version_variations

> [**KnowledgeDocumentVersionVariationListing**](KnowledgeDocumentVersionVariationListing) get_knowledge_knowledgebase_document_version_variations(knowledge_base_id, document_id, version_id, before=before, after=after, page_size=page_size)


Get variations for the given document version.

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/versions/{versionId}/variations 

Requires ALL permissions: 

* knowledge:documentVersion:view

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
knowledge_base_id = 'knowledge_base_id_example' # str | Globally unique identifier for the knowledge base.
document_id = 'document_id_example' # str | Globally unique identifier for the document.
version_id = 'version_id_example' # str | Globally unique identifier for the document version.
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)

try:
    # Get variations for the given document version.
    api_response = api_instance.get_knowledge_knowledgebase_document_version_variations(knowledge_base_id, document_id, version_id, before=before, after=after, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_document_version_variations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Globally unique identifier for the knowledge base. |  |
| **document_id** | **str**| Globally unique identifier for the document. |  |
| **version_id** | **str**| Globally unique identifier for the document version. |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |

### Return type

[**KnowledgeDocumentVersionVariationListing**](KnowledgeDocumentVersionVariationListing)


## get_knowledge_knowledgebase_document_versions

> [**KnowledgeDocumentVersionListing**](KnowledgeDocumentVersionListing) get_knowledge_knowledgebase_document_versions(knowledge_base_id, document_id, before=before, after=after, page_size=page_size, expand=expand)


Get document versions.

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/versions 

Requires ALL permissions: 

* knowledge:documentVersion:view

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
knowledge_base_id = 'knowledge_base_id_example' # str | Globally unique identifier for the knowledge base.
document_id = 'document_id_example' # str | Globally unique identifier for the document.
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
expand = ['expand_example'] # list[str] | The specified entity attributes will be filled. Comma separated values expected. (optional)

try:
    # Get document versions.
    api_response = api_instance.get_knowledge_knowledgebase_document_versions(knowledge_base_id, document_id, before=before, after=after, page_size=page_size, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_document_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Globally unique identifier for the knowledge base. |  |
| **document_id** | **str**| Globally unique identifier for the document. |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **expand** | [**list[str]**](str)| The specified entity attributes will be filled. Comma separated values expected. | [optional] <br />**Values**: category, labels |

### Return type

[**KnowledgeDocumentVersionListing**](KnowledgeDocumentVersionListing)


## get_knowledge_knowledgebase_documents

> [**KnowledgeDocumentResponseListing**](KnowledgeDocumentResponseListing) get_knowledge_knowledgebase_documents(knowledge_base_id, before=before, after=after, page_size=page_size, interval=interval, document_id=document_id, category_id=category_id, include_subcategories=include_subcategories, include_drafts=include_drafts, label_ids=label_ids, expand=expand, external_ids=external_ids)


Get documents.

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents 

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
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
interval = 'interval_example' # str | Retrieves the documents modified in specified date and time range. If the after and before cursor parameters are within this interval, it would return valid data, otherwise it throws an error.The dates in the interval are represented in ISO-8601 format: YYYY-MM-DDThh:mm:ssZ/YYYY-MM-DDThh:mm:ssZ (optional)
document_id = ['document_id_example'] # list[str] | Retrieves the specified documents, comma separated values expected. (optional)
category_id = ['category_id_example'] # list[str] | If specified, retrieves documents associated with category ids, comma separated values expected. (optional)
include_subcategories = True # bool | Works along with 'categoryId' query parameter. If specified, retrieves documents associated with category ids and its children categories. (optional)
include_drafts = True # bool | If includeDrafts is true, Documents in the draft state are also returned in the response. (optional)
label_ids = ['label_ids_example'] # list[str] | If specified, retrieves documents associated with label ids, comma separated values expected. (optional)
expand = ['expand_example'] # list[str] | The specified entity attributes will be filled. Comma separated values expected. (optional)
external_ids = ['external_ids_example'] # list[str] | If specified, retrieves documents associated with external ids, comma separated values expected. (optional)

try:
    # Get documents.
    api_response = api_instance.get_knowledge_knowledgebase_documents(knowledge_base_id, before=before, after=after, page_size=page_size, interval=interval, document_id=document_id, category_id=category_id, include_subcategories=include_subcategories, include_drafts=include_drafts, label_ids=label_ids, expand=expand, external_ids=external_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_documents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **interval** | **str**| Retrieves the documents modified in specified date and time range. If the after and before cursor parameters are within this interval, it would return valid data, otherwise it throws an error.The dates in the interval are represented in ISO-8601 format: YYYY-MM-DDThh:mm:ssZ/YYYY-MM-DDThh:mm:ssZ | [optional]  |
| **document_id** | [**list[str]**](str)| Retrieves the specified documents, comma separated values expected. | [optional]  |
| **category_id** | [**list[str]**](str)| If specified, retrieves documents associated with category ids, comma separated values expected. | [optional]  |
| **include_subcategories** | **bool**| Works along with &#39;categoryId&#39; query parameter. If specified, retrieves documents associated with category ids and its children categories. | [optional]  |
| **include_drafts** | **bool**| If includeDrafts is true, Documents in the draft state are also returned in the response. | [optional]  |
| **label_ids** | [**list[str]**](str)| If specified, retrieves documents associated with label ids, comma separated values expected. | [optional]  |
| **expand** | [**list[str]**](str)| The specified entity attributes will be filled. Comma separated values expected. | [optional] <br />**Values**: category, labels, variations |
| **external_ids** | [**list[str]**](str)| If specified, retrieves documents associated with external ids, comma separated values expected. | [optional]  |

### Return type

[**KnowledgeDocumentResponseListing**](KnowledgeDocumentResponseListing)


## get_knowledge_knowledgebase_export_job

> [**KnowledgeExportJobResponse**](KnowledgeExportJobResponse) get_knowledge_knowledgebase_export_job(knowledge_base_id, export_job_id)


Get export job report

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/export/jobs/{exportJobId} 

Requires ALL permissions: 

* knowledge:exportJob:view

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
export_job_id = 'export_job_id_example' # str | Export job ID

try:
    # Get export job report
    api_response = api_instance.get_knowledge_knowledgebase_export_job(knowledge_base_id, export_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_export_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **export_job_id** | **str**| Export job ID |  |

### Return type

[**KnowledgeExportJobResponse**](KnowledgeExportJobResponse)


## get_knowledge_knowledgebase_import_job

> [**KnowledgeImportJobResponse**](KnowledgeImportJobResponse) get_knowledge_knowledgebase_import_job(knowledge_base_id, import_job_id, expand=expand)


Get import job report

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/import/jobs/{importJobId} 

Requires ALL permissions: 

* knowledge:importJob:view

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
import_job_id = 'import_job_id_example' # str | Import job ID
expand = ['expand_example'] # list[str] | If expand contains 'urls' downloadURL and failedEntitiesURL will be filled. (optional)

try:
    # Get import job report
    api_response = api_instance.get_knowledge_knowledgebase_import_job(knowledge_base_id, import_job_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_import_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **import_job_id** | **str**| Import job ID |  |
| **expand** | [**list[str]**](str)| If expand contains &#39;urls&#39; downloadURL and failedEntitiesURL will be filled. | [optional] <br />**Values**: urls |

### Return type

[**KnowledgeImportJobResponse**](KnowledgeImportJobResponse)


## get_knowledge_knowledgebase_label

> [**LabelResponse**](LabelResponse) get_knowledge_knowledgebase_label(knowledge_base_id, label_id)


Get label

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/labels/{labelId} 

Requires ALL permissions: 

* knowledge:label:view

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
label_id = 'label_id_example' # str | Label ID

try:
    # Get label
    api_response = api_instance.get_knowledge_knowledgebase_label(knowledge_base_id, label_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_label: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **label_id** | **str**| Label ID |  |

### Return type

[**LabelResponse**](LabelResponse)


## get_knowledge_knowledgebase_labels

> [**LabelListing**](LabelListing) get_knowledge_knowledgebase_labels(knowledge_base_id, before=before, after=after, page_size=page_size, name=name, include_document_count=include_document_count)


Get labels

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/labels 

Requires ALL permissions: 

* knowledge:label:view

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
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
name = 'name_example' # str | Filter to return the labels that contains the given phrase in the name. (optional)
include_document_count = True # bool | If specified, retrieves the number of documents related to label. (optional)

try:
    # Get labels
    api_response = api_instance.get_knowledge_knowledgebase_labels(knowledge_base_id, before=before, after=after, page_size=page_size, name=name, include_document_count=include_document_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_labels: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **name** | **str**| Filter to return the labels that contains the given phrase in the name. | [optional]  |
| **include_document_count** | **bool**| If specified, retrieves the number of documents related to label. | [optional]  |

### Return type

[**LabelListing**](LabelListing)


## get_knowledge_knowledgebase_language_categories

> [**CategoryListing**](CategoryListing) get_knowledge_knowledgebase_language_categories(knowledge_base_id, language_code, before=before, after=after, limit=limit, page_size=page_size, name=name)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
limit = 'limit_example' # str | Number of entities to return. Maximum of 200. Deprecated in favour of pageSize (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
name = 'name_example' # str | Filter to return the categories that starts with the given category name. (optional)

try:
    # Get categories
    api_response = api_instance.get_knowledge_knowledgebase_language_categories(knowledge_base_id, language_code, before=before, after=after, limit=limit, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_language_categories: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **limit** | **str**| Number of entities to return. Maximum of 200. Deprecated in favour of pageSize | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **name** | **str**| Filter to return the categories that starts with the given category name. | [optional]  |

### Return type

[**CategoryListing**](CategoryListing)


## get_knowledge_knowledgebase_language_category

> [**KnowledgeExtendedCategory**](KnowledgeExtendedCategory) get_knowledge_knowledgebase_language_category(category_id, knowledge_base_id, language_code)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_language_category: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **category_id** | **str**| Category ID |  |
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |

### Return type

[**KnowledgeExtendedCategory**](KnowledgeExtendedCategory)


## get_knowledge_knowledgebase_language_document

> [**KnowledgeDocument**](KnowledgeDocument) get_knowledge_knowledgebase_language_document(document_id, knowledge_base_id, language_code)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_language_document: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |

### Return type

[**KnowledgeDocument**](KnowledgeDocument)


## get_knowledge_knowledgebase_language_document_upload

> [**KnowledgeDocumentContentUpload**](KnowledgeDocumentContentUpload) get_knowledge_knowledgebase_language_document_upload(document_id, knowledge_base_id, language_code, upload_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get document content upload status

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/{documentId}/uploads/{uploadId} 

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
upload_id = 'upload_id_example' # str | UploadId

try:
    # Get document content upload status
    api_response = api_instance.get_knowledge_knowledgebase_language_document_upload(document_id, knowledge_base_id, language_code, upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_language_document_upload: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **upload_id** | **str**| UploadId |  |

### Return type

[**KnowledgeDocumentContentUpload**](KnowledgeDocumentContentUpload)


## get_knowledge_knowledgebase_language_documents

> [**DocumentListing**](DocumentListing) get_knowledge_knowledgebase_language_documents(knowledge_base_id, language_code, before=before, after=after, limit=limit, page_size=page_size, categories=categories, title=title, sort_by=sort_by, sort_order=sort_order, document_ids=document_ids)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
limit = 'limit_example' # str | Number of entities to return. Maximum of 200. Deprecated in favour of pageSize (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
categories = 'categories_example' # str | Filter by categories ids, comma separated values expected. (optional)
title = 'title_example' # str | Filter by document title. (optional)
sort_by = 'sort_by_example' # str | Sort by. (optional)
sort_order = 'sort_order_example' # str | Sort Order. (optional)
document_ids = ['document_ids_example'] # list[str] | Comma-separated list of document identifiers to fetch by. (optional)

try:
    # Get documents
    api_response = api_instance.get_knowledge_knowledgebase_language_documents(knowledge_base_id, language_code, before=before, after=after, limit=limit, page_size=page_size, categories=categories, title=title, sort_by=sort_by, sort_order=sort_order, document_ids=document_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_language_documents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **limit** | **str**| Number of entities to return. Maximum of 200. Deprecated in favour of pageSize | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **categories** | **str**| Filter by categories ids, comma separated values expected. | [optional]  |
| **title** | **str**| Filter by document title. | [optional]  |
| **sort_by** | **str**| Sort by. | [optional] <br />**Values**: Title, Date |
| **sort_order** | **str**| Sort Order. | [optional] <br />**Values**: ASC, ascending, DESC, descending |
| **document_ids** | [**list[str]**](str)| Comma-separated list of document identifiers to fetch by. | [optional]  |

### Return type

[**DocumentListing**](DocumentListing)


## get_knowledge_knowledgebase_language_documents_import

> [**KnowledgeImport**](KnowledgeImport) get_knowledge_knowledgebase_language_documents_import(knowledge_base_id, language_code, import_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get import operation report

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/imports/{importId} 

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
import_id = 'import_id_example' # str | Import ID

try:
    # Get import operation report
    api_response = api_instance.get_knowledge_knowledgebase_language_documents_import(knowledge_base_id, language_code, import_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_language_documents_import: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **import_id** | **str**| Import ID |  |

### Return type

[**KnowledgeImport**](KnowledgeImport)


## get_knowledge_knowledgebase_language_training

> [**KnowledgeTraining**](KnowledgeTraining) get_knowledge_knowledgebase_language_training(knowledge_base_id, language_code, training_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_language_training: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **training_id** | **str**| Training ID |  |

### Return type

[**KnowledgeTraining**](KnowledgeTraining)


## get_knowledge_knowledgebase_language_trainings

> [**TrainingListing**](TrainingListing) get_knowledge_knowledgebase_language_trainings(knowledge_base_id, language_code, before=before, after=after, limit=limit, page_size=page_size, knowledge_documents_state=knowledge_documents_state)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
limit = 'limit_example' # str | Number of entities to return. Maximum of 200. Deprecated in favour of pageSize (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
knowledge_documents_state = 'knowledge_documents_state_example' # str | Return the training with the specified state of the trained documents. (optional)

try:
    # Get all trainings information for a knowledgebase
    api_response = api_instance.get_knowledge_knowledgebase_language_trainings(knowledge_base_id, language_code, before=before, after=after, limit=limit, page_size=page_size, knowledge_documents_state=knowledge_documents_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_language_trainings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **limit** | **str**| Number of entities to return. Maximum of 200. Deprecated in favour of pageSize | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **knowledge_documents_state** | **str**| Return the training with the specified state of the trained documents. | [optional] <br />**Values**: Draft, Active, Discarded, Archived |

### Return type

[**TrainingListing**](TrainingListing)


## get_knowledge_knowledgebase_operations

> [**OperationListing**](OperationListing) get_knowledge_knowledgebase_operations(knowledge_base_id, before=before, after=after, page_size=page_size, user_id=user_id, type=type, status=status, interval=interval, source_id=source_id)


Get operations

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/operations 

Requires ALL permissions: 

* knowledge:importExportOperationsList:view

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
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
user_id = ['user_id_example'] # list[str] | If specified, retrieves operations associated with user ids, comma separated values expected. (optional)
type = ['type_example'] # list[str] | If specified, retrieves operations with specified operation type, comma separated values expected. (optional)
status = ['status_example'] # list[str] | If specified, retrieves operations with specified operation status, comma separated values expected. (optional)
interval = 'interval_example' # str | Retrieves the operations modified in specified date and time range. If the after and before cursor parameters are within this interval, it would return valid data, otherwise it throws an error.The dates in the interval are represented in ISO-8601 format: YYYY-MM-DDThh:mm:ssZ/YYYY-MM-DDThh:mm:ssZ (optional)
source_id = ['source_id_example'] # list[str] | If specified, retrieves operations associated with source ids, comma separated values expected. (optional)

try:
    # Get operations
    api_response = api_instance.get_knowledge_knowledgebase_operations(knowledge_base_id, before=before, after=after, page_size=page_size, user_id=user_id, type=type, status=status, interval=interval, source_id=source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_operations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **user_id** | [**list[str]**](str)| If specified, retrieves operations associated with user ids, comma separated values expected. | [optional]  |
| **type** | [**list[str]**](str)| If specified, retrieves operations with specified operation type, comma separated values expected. | [optional] <br />**Values**: Export, Import, Parse, Sync |
| **status** | [**list[str]**](str)| If specified, retrieves operations with specified operation status, comma separated values expected. | [optional]  |
| **interval** | **str**| Retrieves the operations modified in specified date and time range. If the after and before cursor parameters are within this interval, it would return valid data, otherwise it throws an error.The dates in the interval are represented in ISO-8601 format: YYYY-MM-DDThh:mm:ssZ/YYYY-MM-DDThh:mm:ssZ | [optional]  |
| **source_id** | [**list[str]**](str)| If specified, retrieves operations associated with source ids, comma separated values expected. | [optional]  |

### Return type

[**OperationListing**](OperationListing)


## get_knowledge_knowledgebase_operations_users_query

> [**OperationCreatorUserResponse**](OperationCreatorUserResponse) get_knowledge_knowledgebase_operations_users_query(knowledge_base_id)


Get ids of operation creator users and oauth clients

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/operations/users/query 

Requires ALL permissions: 

* knowledge:importExportOperationsList:view

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
    # Get ids of operation creator users and oauth clients
    api_response = api_instance.get_knowledge_knowledgebase_operations_users_query(knowledge_base_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_operations_users_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |

### Return type

[**OperationCreatorUserResponse**](OperationCreatorUserResponse)


## get_knowledge_knowledgebase_parse_job

> [**KnowledgeParseJobResponse**](KnowledgeParseJobResponse) get_knowledge_knowledgebase_parse_job(knowledge_base_id, parse_job_id, expand=expand)


Get parse job report

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/parse/jobs/{parseJobId} 

Requires ALL permissions: 

* knowledge:importJob:view

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
parse_job_id = 'parse_job_id_example' # str | Parse job ID
expand = ['expand_example'] # list[str] | If expand contains 'urls' downloadURL and failedEntitiesURL will be filled. (optional)

try:
    # Get parse job report
    api_response = api_instance.get_knowledge_knowledgebase_parse_job(knowledge_base_id, parse_job_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_parse_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **parse_job_id** | **str**| Parse job ID |  |
| **expand** | [**list[str]**](str)| If expand contains &#39;urls&#39; downloadURL and failedEntitiesURL will be filled. | [optional] <br />**Values**: urls |

### Return type

[**KnowledgeParseJobResponse**](KnowledgeParseJobResponse)


## get_knowledge_knowledgebase_sources

> [**list[SourceBaseResponse]**](SourceBaseResponse) get_knowledge_knowledgebase_sources(knowledge_base_id, type=type, expand=expand, ids=ids)


Get Knowledge integration sources

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources 

Requires ALL permissions: 

* knowledge:integrationSource:view

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
type = 'type_example' # str | If specified, retrieves integration sources with specified integration type. (optional)
expand = ['expand_example'] # list[str] | The specified entity attributes will be filled. Comma separated values expected. (optional)
ids = ['ids_example'] # list[str] | If specified, retrieves integration sources with specified IDs. (optional)

try:
    # Get Knowledge integration sources
    api_response = api_instance.get_knowledge_knowledgebase_sources(knowledge_base_id, type=type, expand=expand, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_sources: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **type** | **str**| If specified, retrieves integration sources with specified integration type. | [optional] <br />**Values**: Salesforce, ServiceNow |
| **expand** | [**list[str]**](str)| The specified entity attributes will be filled. Comma separated values expected. | [optional] <br />**Values**: lastsync |
| **ids** | [**list[str]**](str)| If specified, retrieves integration sources with specified IDs. | [optional]  |

### Return type

[**list[SourceBaseResponse]**](SourceBaseResponse)


## get_knowledge_knowledgebase_sources_salesforce_source_id

> [**SalesforceSourceResponse**](SalesforceSourceResponse) get_knowledge_knowledgebase_sources_salesforce_source_id(knowledge_base_id, source_id, expand=expand)


Get Salesforce Knowledge integration source

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/salesforce/{sourceId} 

Requires ALL permissions: 

* knowledge:integrationSource:view

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
source_id = 'source_id_example' # str | Source ID
expand = ['expand_example'] # list[str] | The specified entity attributes will be filled. Comma separated values expected. (optional)

try:
    # Get Salesforce Knowledge integration source
    api_response = api_instance.get_knowledge_knowledgebase_sources_salesforce_source_id(knowledge_base_id, source_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_sources_salesforce_source_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **source_id** | **str**| Source ID |  |
| **expand** | [**list[str]**](str)| The specified entity attributes will be filled. Comma separated values expected. | [optional] <br />**Values**: lastsync |

### Return type

[**SalesforceSourceResponse**](SalesforceSourceResponse)


## get_knowledge_knowledgebase_sources_servicenow_source_id

> [**ServiceNowSourceResponse**](ServiceNowSourceResponse) get_knowledge_knowledgebase_sources_servicenow_source_id(knowledge_base_id, source_id, expand=expand)


Get ServiceNow Knowledge integration source

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/servicenow/{sourceId} 

Requires ALL permissions: 

* knowledge:integrationSource:view

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
source_id = 'source_id_example' # str | Source ID
expand = ['expand_example'] # list[str] | The specified entity attributes will be filled. Comma separated values expected. (optional)

try:
    # Get ServiceNow Knowledge integration source
    api_response = api_instance.get_knowledge_knowledgebase_sources_servicenow_source_id(knowledge_base_id, source_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_sources_servicenow_source_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **source_id** | **str**| Source ID |  |
| **expand** | [**list[str]**](str)| The specified entity attributes will be filled. Comma separated values expected. | [optional] <br />**Values**: lastsync |

### Return type

[**ServiceNowSourceResponse**](ServiceNowSourceResponse)


## get_knowledge_knowledgebase_synchronize_job

> [**KnowledgeSyncJobResponse**](KnowledgeSyncJobResponse) get_knowledge_knowledgebase_synchronize_job(knowledge_base_id, sync_job_id)


Get synchronization job report

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/synchronize/jobs/{syncJobId} 

Requires ALL permissions: 

* knowledge:syncJob:view

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
sync_job_id = 'sync_job_id_example' # str | Synchronization job ID

try:
    # Get synchronization job report
    api_response = api_instance.get_knowledge_knowledgebase_synchronize_job(knowledge_base_id, sync_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_synchronize_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **sync_job_id** | **str**| Synchronization job ID |  |

### Return type

[**KnowledgeSyncJobResponse**](KnowledgeSyncJobResponse)


## get_knowledge_knowledgebase_unanswered_group

> [**UnansweredGroup**](UnansweredGroup) get_knowledge_knowledgebase_unanswered_group(knowledge_base_id, group_id, app=app, date_start=date_start, date_end=date_end)


Get knowledge base unanswered group for a particular groupId

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/unanswered/groups/{groupId} 

Requires ALL permissions: 

* knowledge:groups:view

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
group_id = 'group_id_example' # str | The ID of the group to be retrieved.
app = 'app_example' # str | The app value to be used for filtering phrases. (optional)
date_start = '2013-10-20' # date | The start date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
date_end = '2013-10-20' # date | The end date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)

try:
    # Get knowledge base unanswered group for a particular groupId
    api_response = api_instance.get_knowledge_knowledgebase_unanswered_group(knowledge_base_id, group_id, app=app, date_start=date_start, date_end=date_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_unanswered_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **group_id** | **str**| The ID of the group to be retrieved. |  |
| **app** | **str**| The app value to be used for filtering phrases. | [optional] <br />**Values**: SupportCenter, MessengerKnowledgeApp, BotFlow, Assistant, SmartAdvisor |
| **date_start** | **date**| The start date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **date_end** | **date**| The end date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |

### Return type

[**UnansweredGroup**](UnansweredGroup)


## get_knowledge_knowledgebase_unanswered_group_phrasegroup

> [**UnansweredPhraseGroup**](UnansweredPhraseGroup) get_knowledge_knowledgebase_unanswered_group_phrasegroup(knowledge_base_id, group_id, phrase_group_id, app=app, date_start=date_start, date_end=date_end)


Get knowledge base unanswered phrase group for a particular phraseGroupId

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/unanswered/groups/{groupId}/phrasegroups/{phraseGroupId} 

Requires ALL permissions: 

* knowledge:groups:view

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
group_id = 'group_id_example' # str | The ID of the group to be retrieved.
phrase_group_id = 'phrase_group_id_example' # str | The ID of the phraseGroup to be retrieved.
app = 'app_example' # str | The app value to be used for filtering phrases. (optional)
date_start = '2013-10-20' # date | The start date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
date_end = '2013-10-20' # date | The end date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)

try:
    # Get knowledge base unanswered phrase group for a particular phraseGroupId
    api_response = api_instance.get_knowledge_knowledgebase_unanswered_group_phrasegroup(knowledge_base_id, group_id, phrase_group_id, app=app, date_start=date_start, date_end=date_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_unanswered_group_phrasegroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **group_id** | **str**| The ID of the group to be retrieved. |  |
| **phrase_group_id** | **str**| The ID of the phraseGroup to be retrieved. |  |
| **app** | **str**| The app value to be used for filtering phrases. | [optional] <br />**Values**: SupportCenter, MessengerKnowledgeApp, BotFlow, Assistant, SmartAdvisor |
| **date_start** | **date**| The start date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **date_end** | **date**| The end date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |

### Return type

[**UnansweredPhraseGroup**](UnansweredPhraseGroup)


## get_knowledge_knowledgebase_unanswered_groups

> [**UnansweredGroups**](UnansweredGroups) get_knowledge_knowledgebase_unanswered_groups(knowledge_base_id, app=app, date_start=date_start, date_end=date_end)


Get knowledge base unanswered groups

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/unanswered/groups 

Requires ALL permissions: 

* knowledge:groups:view

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
app = 'app_example' # str | The app value to be used for filtering phrases. (optional)
date_start = '2013-10-20' # date | The start date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)
date_end = '2013-10-20' # date | The end date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (optional)

try:
    # Get knowledge base unanswered groups
    api_response = api_instance.get_knowledge_knowledgebase_unanswered_groups(knowledge_base_id, app=app, date_start=date_start, date_end=date_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_unanswered_groups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **app** | **str**| The app value to be used for filtering phrases. | [optional] <br />**Values**: SupportCenter, MessengerKnowledgeApp, BotFlow, Assistant, SmartAdvisor |
| **date_start** | **date**| The start date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |
| **date_end** | **date**| The end date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional]  |

### Return type

[**UnansweredGroups**](UnansweredGroups)


## get_knowledge_knowledgebase_uploads_urls_job

> [**GetUploadSourceUrlJobStatusResponse**](GetUploadSourceUrlJobStatusResponse) get_knowledge_knowledgebase_uploads_urls_job(knowledge_base_id, job_id)


Get content upload from URL job status

Wraps GET /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/uploads/urls/jobs/{jobId} 

Requires ALL permissions: 

* knowledge:uploadSourceUrlJob:view

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
job_id = 'job_id_example' # str | Upload job ID

try:
    # Get content upload from URL job status
    api_response = api_instance.get_knowledge_knowledgebase_uploads_urls_job(knowledge_base_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebase_uploads_urls_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **job_id** | **str**| Upload job ID |  |

### Return type

[**GetUploadSourceUrlJobStatusResponse**](GetUploadSourceUrlJobStatusResponse)


## get_knowledge_knowledgebases

> [**KnowledgeBaseListing**](KnowledgeBaseListing) get_knowledge_knowledgebases(before=before, after=after, limit=limit, page_size=page_size, name=name, core_language=core_language, published=published, sort_by=sort_by, sort_order=sort_order)


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
limit = 'limit_example' # str | Number of entities to return. Maximum of 100. Deprecated in favour of pageSize (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 100. (optional)
name = 'name_example' # str | Filter by Name. (optional)
core_language = 'core_language_example' # str | Filter by core language. (optional)
published = True # bool | Filter by published status. (optional)
sort_by = 'sort_by_example' # str | Sort by. (optional)
sort_order = 'sort_order_example' # str | Sort Order. (optional)

try:
    # Get knowledge bases
    api_response = api_instance.get_knowledge_knowledgebases(before=before, after=after, limit=limit, page_size=page_size, name=name, core_language=core_language, published=published, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->get_knowledge_knowledgebases: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **limit** | **str**| Number of entities to return. Maximum of 100. Deprecated in favour of pageSize | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 100. | [optional]  |
| **name** | **str**| Filter by Name. | [optional]  |
| **core_language** | **str**| Filter by core language. | [optional] <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **published** | **bool**| Filter by published status. | [optional]  |
| **sort_by** | **str**| Sort by. | [optional] <br />**Values**: Name, Date |
| **sort_order** | **str**| Sort Order. | [optional] <br />**Values**: ASC, ascending, DESC, descending |

### Return type

[**KnowledgeBaseListing**](KnowledgeBaseListing)


## patch_knowledge_guest_session_documents_search_search_id

>  patch_knowledge_guest_session_documents_search_search_id(session_id, search_id, body)


Update search result.

Wraps PATCH /api/v2/knowledge/guest/sessions/{sessionId}/documents/search/{searchId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
session_id = 'session_id_example' # str | Knowledge guest session ID.
search_id = 'search_id_example' # str | Search Result ID
body = PureCloudPlatformClientV2.SearchUpdateRequest() # SearchUpdateRequest | 

try:
    # Update search result.
    api_instance.patch_knowledge_guest_session_documents_search_search_id(session_id, search_id, body)
except ApiException as e:
    print("Exception when calling KnowledgeApi->patch_knowledge_guest_session_documents_search_search_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| Knowledge guest session ID. |  |
| **search_id** | **str**| Search Result ID |  |
| **body** | [**SearchUpdateRequest**](SearchUpdateRequest)|  |  |

### Return type

void (empty response body)


## patch_knowledge_knowledgebase

> [**KnowledgeBase**](KnowledgeBase) patch_knowledge_knowledgebase(knowledge_base_id, body)


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
body = PureCloudPlatformClientV2.KnowledgeBaseUpdateRequest() # KnowledgeBaseUpdateRequest | 

try:
    # Update knowledge base
    api_response = api_instance.patch_knowledge_knowledgebase(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeBaseUpdateRequest**](KnowledgeBaseUpdateRequest)|  |  |

### Return type

[**KnowledgeBase**](KnowledgeBase)


## patch_knowledge_knowledgebase_category

> [**CategoryResponse**](CategoryResponse) patch_knowledge_knowledgebase_category(knowledge_base_id, category_id, body)


Update category

Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/categories/{categoryId} 

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
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
category_id = 'category_id_example' # str | Category ID
body = PureCloudPlatformClientV2.CategoryUpdateRequest() # CategoryUpdateRequest | 

try:
    # Update category
    api_response = api_instance.patch_knowledge_knowledgebase_category(knowledge_base_id, category_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_category: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **category_id** | **str**| Category ID |  |
| **body** | [**CategoryUpdateRequest**](CategoryUpdateRequest)|  |  |

### Return type

[**CategoryResponse**](CategoryResponse)


## patch_knowledge_knowledgebase_document

> [**KnowledgeDocumentResponse**](KnowledgeDocumentResponse) patch_knowledge_knowledgebase_document(knowledge_base_id, document_id, body)


Update document.

Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId} 

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
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID.
document_id = 'document_id_example' # str | Document ID.
body = PureCloudPlatformClientV2.KnowledgeDocumentReq() # KnowledgeDocumentReq | 

try:
    # Update document.
    api_response = api_instance.patch_knowledge_knowledgebase_document(knowledge_base_id, document_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_document: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID. |  |
| **document_id** | **str**| Document ID. |  |
| **body** | [**KnowledgeDocumentReq**](KnowledgeDocumentReq)|  |  |

### Return type

[**KnowledgeDocumentResponse**](KnowledgeDocumentResponse)


## patch_knowledge_knowledgebase_document_feedback_feedback_id

> [**KnowledgeDocumentFeedbackResponse**](KnowledgeDocumentFeedbackResponse) patch_knowledge_knowledgebase_document_feedback_feedback_id(knowledge_base_id, document_id, feedback_id, body=body)


Update feedback on a document

Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/feedback/{feedbackId} 

Requires ANY permissions: 

* knowledge:feedback:edit

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
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID.
document_id = 'document_id_example' # str | Document ID.
feedback_id = 'feedback_id_example' # str | Feedback ID.
body = PureCloudPlatformClientV2.KnowledgeDocumentFeedbackUpdateRequest() # KnowledgeDocumentFeedbackUpdateRequest |  (optional)

try:
    # Update feedback on a document
    api_response = api_instance.patch_knowledge_knowledgebase_document_feedback_feedback_id(knowledge_base_id, document_id, feedback_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_document_feedback_feedback_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID. |  |
| **document_id** | **str**| Document ID. |  |
| **feedback_id** | **str**| Feedback ID. |  |
| **body** | [**KnowledgeDocumentFeedbackUpdateRequest**](KnowledgeDocumentFeedbackUpdateRequest)|  | [optional]  |

### Return type

[**KnowledgeDocumentFeedbackResponse**](KnowledgeDocumentFeedbackResponse)


## patch_knowledge_knowledgebase_document_variation

> [**DocumentVariationResponse**](DocumentVariationResponse) patch_knowledge_knowledgebase_document_variation(document_variation_id, document_id, knowledge_base_id, body)


Update a variation for a document.

Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/variations/{documentVariationId} 

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
document_variation_id = 'document_variation_id_example' # str | Globally unique identifier for a document variation.
document_id = 'document_id_example' # str | Globally unique identifier for a document.
knowledge_base_id = 'knowledge_base_id_example' # str | Globally unique identifier for a knowledge base.
body = PureCloudPlatformClientV2.DocumentVariationRequest() # DocumentVariationRequest | 

try:
    # Update a variation for a document.
    api_response = api_instance.patch_knowledge_knowledgebase_document_variation(document_variation_id, document_id, knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_document_variation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_variation_id** | **str**| Globally unique identifier for a document variation. |  |
| **document_id** | **str**| Globally unique identifier for a document. |  |
| **knowledge_base_id** | **str**| Globally unique identifier for a knowledge base. |  |
| **body** | [**DocumentVariationRequest**](DocumentVariationRequest)|  |  |

### Return type

[**DocumentVariationResponse**](DocumentVariationResponse)


## patch_knowledge_knowledgebase_documents_search_search_id

>  patch_knowledge_knowledgebase_documents_search_search_id(knowledge_base_id, search_id, body=body)


Update search result.

Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/search/{searchId} 

Requires ALL permissions: 

* knowledge:search:edit

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
knowledge_base_id = 'knowledge_base_id_example' # str | The ID of knowledge base containing the documents to query.
search_id = 'search_id_example' # str | Search Result ID
body = PureCloudPlatformClientV2.SearchUpdateRequest() # SearchUpdateRequest |  (optional)

try:
    # Update search result.
    api_instance.patch_knowledge_knowledgebase_documents_search_search_id(knowledge_base_id, search_id, body=body)
except ApiException as e:
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_documents_search_search_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| The ID of knowledge base containing the documents to query. |  |
| **search_id** | **str**| Search Result ID |  |
| **body** | [**SearchUpdateRequest**](SearchUpdateRequest)|  | [optional]  |

### Return type

void (empty response body)


## patch_knowledge_knowledgebase_import_job

> [**KnowledgeImportJobResponse**](KnowledgeImportJobResponse) patch_knowledge_knowledgebase_import_job(knowledge_base_id, import_job_id, body)


Start import job

Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/import/jobs/{importJobId} 

Requires ALL permissions: 

* knowledge:importJob:edit

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
import_job_id = 'import_job_id_example' # str | Import job ID
body = PureCloudPlatformClientV2.ImportStatusRequest() # ImportStatusRequest | 

try:
    # Start import job
    api_response = api_instance.patch_knowledge_knowledgebase_import_job(knowledge_base_id, import_job_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_import_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **import_job_id** | **str**| Import job ID |  |
| **body** | [**ImportStatusRequest**](ImportStatusRequest)|  |  |

### Return type

[**KnowledgeImportJobResponse**](KnowledgeImportJobResponse)


## patch_knowledge_knowledgebase_label

> [**LabelResponse**](LabelResponse) patch_knowledge_knowledgebase_label(knowledge_base_id, label_id, body)


Update label

Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/labels/{labelId} 

Requires ALL permissions: 

* knowledge:label:edit

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
label_id = 'label_id_example' # str | Label ID
body = PureCloudPlatformClientV2.LabelUpdateRequest() # LabelUpdateRequest | 

try:
    # Update label
    api_response = api_instance.patch_knowledge_knowledgebase_label(knowledge_base_id, label_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_label: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **label_id** | **str**| Label ID |  |
| **body** | [**LabelUpdateRequest**](LabelUpdateRequest)|  |  |

### Return type

[**LabelResponse**](LabelResponse)


## patch_knowledge_knowledgebase_language_category

> [**KnowledgeExtendedCategory**](KnowledgeExtendedCategory) patch_knowledge_knowledgebase_language_category(category_id, knowledge_base_id, language_code, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_language_category: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **category_id** | **str**| Category ID |  |
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **body** | [**KnowledgeCategoryRequest**](KnowledgeCategoryRequest)|  |  |

### Return type

[**KnowledgeExtendedCategory**](KnowledgeExtendedCategory)


## patch_knowledge_knowledgebase_language_document

> [**KnowledgeDocument**](KnowledgeDocument) patch_knowledge_knowledgebase_language_document(document_id, knowledge_base_id, language_code, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_language_document: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **body** | [**KnowledgeDocumentRequest**](KnowledgeDocumentRequest)|  |  |

### Return type

[**KnowledgeDocument**](KnowledgeDocument)


## patch_knowledge_knowledgebase_language_documents

> [**DocumentListing**](DocumentListing) patch_knowledge_knowledgebase_language_documents(knowledge_base_id, language_code, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_language_documents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **body** | [**list[KnowledgeDocumentBulkRequest]**](KnowledgeDocumentBulkRequest)|  |  |

### Return type

[**DocumentListing**](DocumentListing)


## patch_knowledge_knowledgebase_language_documents_import

> [**KnowledgeImport**](KnowledgeImport) patch_knowledge_knowledgebase_language_documents_import(knowledge_base_id, language_code, import_id, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Start import operation

Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/imports/{importId} 

Requires ALL permissions: 

* knowledge:document:edit
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
import_id = 'import_id_example' # str | Import ID
body = PureCloudPlatformClientV2.ImportStatusRequest() # ImportStatusRequest | 

try:
    # Start import operation
    api_response = api_instance.patch_knowledge_knowledgebase_language_documents_import(knowledge_base_id, language_code, import_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_language_documents_import: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **import_id** | **str**| Import ID |  |
| **body** | [**ImportStatusRequest**](ImportStatusRequest)|  |  |

### Return type

[**KnowledgeImport**](KnowledgeImport)


## patch_knowledge_knowledgebase_parse_job

>  patch_knowledge_knowledgebase_parse_job(knowledge_base_id, parse_job_id, body)


Send update to the parse operation

Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/parse/jobs/{parseJobId} 

Requires ALL permissions: 

* knowledge:importJob:edit

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
parse_job_id = 'parse_job_id_example' # str | Parse job ID
body = PureCloudPlatformClientV2.KnowledgeParseJobRequestPatch() # KnowledgeParseJobRequestPatch | 

try:
    # Send update to the parse operation
    api_instance.patch_knowledge_knowledgebase_parse_job(knowledge_base_id, parse_job_id, body)
except ApiException as e:
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_parse_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **parse_job_id** | **str**| Parse job ID |  |
| **body** | [**KnowledgeParseJobRequestPatch**](KnowledgeParseJobRequestPatch)|  |  |

### Return type

void (empty response body)


## patch_knowledge_knowledgebase_synchronize_job

> [**KnowledgeSyncJobResponse**](KnowledgeSyncJobResponse) patch_knowledge_knowledgebase_synchronize_job(knowledge_base_id, sync_job_id, body)


Update synchronization job

Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/synchronize/jobs/{syncJobId} 

Requires ALL permissions: 

* knowledge:syncJob:edit

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
sync_job_id = 'sync_job_id_example' # str | Synchronization job ID
body = PureCloudPlatformClientV2.SyncStatusRequest() # SyncStatusRequest | 

try:
    # Update synchronization job
    api_response = api_instance.patch_knowledge_knowledgebase_synchronize_job(knowledge_base_id, sync_job_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_synchronize_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **sync_job_id** | **str**| Synchronization job ID |  |
| **body** | [**SyncStatusRequest**](SyncStatusRequest)|  |  |

### Return type

[**KnowledgeSyncJobResponse**](KnowledgeSyncJobResponse)


## patch_knowledge_knowledgebase_unanswered_group_phrasegroup

> [**UnansweredPhraseGroupUpdateResponse**](UnansweredPhraseGroupUpdateResponse) patch_knowledge_knowledgebase_unanswered_group_phrasegroup(knowledge_base_id, group_id, phrase_group_id, body)


Update a Knowledge base unanswered phrase group

Wraps PATCH /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/unanswered/groups/{groupId}/phrasegroups/{phraseGroupId} 

Requires ALL permissions: 

* knowledge:groups:edit
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
group_id = 'group_id_example' # str | The ID of the group to be updated.
phrase_group_id = 'phrase_group_id_example' # str | The ID of the phraseGroup to be updated.
body = PureCloudPlatformClientV2.UnansweredPhraseGroupPatchRequestBody() # UnansweredPhraseGroupPatchRequestBody | Request body of the update unanswered group endpoint.

try:
    # Update a Knowledge base unanswered phrase group
    api_response = api_instance.patch_knowledge_knowledgebase_unanswered_group_phrasegroup(knowledge_base_id, group_id, phrase_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->patch_knowledge_knowledgebase_unanswered_group_phrasegroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **group_id** | **str**| The ID of the group to be updated. |  |
| **phrase_group_id** | **str**| The ID of the phraseGroup to be updated. |  |
| **body** | [**UnansweredPhraseGroupPatchRequestBody**](UnansweredPhraseGroupPatchRequestBody)| Request body of the update unanswered group endpoint. |  |

### Return type

[**UnansweredPhraseGroupUpdateResponse**](UnansweredPhraseGroupUpdateResponse)


## post_knowledge_documentuploads

> [**UploadUrlResponse**](UploadUrlResponse) post_knowledge_documentuploads(body)


Creates a presigned URL for uploading a knowledge import file with a set of documents

Wraps POST /api/v2/knowledge/documentuploads 

Requires ALL permissions: 

* knowledge:document:upload

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
body = PureCloudPlatformClientV2.UploadUrlRequest() # UploadUrlRequest | query

try:
    # Creates a presigned URL for uploading a knowledge import file with a set of documents
    api_response = api_instance.post_knowledge_documentuploads(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_documentuploads: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UploadUrlRequest**](UploadUrlRequest)| query |  |

### Return type

[**UploadUrlResponse**](UploadUrlResponse)


## post_knowledge_guest_session_document_copies

>  post_knowledge_guest_session_document_copies(session_id, document_id, body=body)


Indicate that the document was copied by the user.

Wraps POST /api/v2/knowledge/guest/sessions/{sessionId}/documents/{documentId}/copies 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
session_id = 'session_id_example' # str | Knowledge guest session ID.
document_id = 'document_id_example' # str | Document ID
body = PureCloudPlatformClientV2.KnowledgeGuestDocumentCopy() # KnowledgeGuestDocumentCopy |  (optional)

try:
    # Indicate that the document was copied by the user.
    api_instance.post_knowledge_guest_session_document_copies(session_id, document_id, body=body)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_guest_session_document_copies: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| Knowledge guest session ID. |  |
| **document_id** | **str**| Document ID |  |
| **body** | [**KnowledgeGuestDocumentCopy**](KnowledgeGuestDocumentCopy)|  | [optional]  |

### Return type

void (empty response body)


## post_knowledge_guest_session_document_feedback

> [**KnowledgeGuestDocumentFeedback**](KnowledgeGuestDocumentFeedback) post_knowledge_guest_session_document_feedback(session_id, document_id, body=body)


Give feedback on a document

Wraps POST /api/v2/knowledge/guest/sessions/{sessionId}/documents/{documentId}/feedback 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
session_id = 'session_id_example' # str | Knowledge guest session ID.
document_id = 'document_id_example' # str | Document ID.
body = PureCloudPlatformClientV2.KnowledgeGuestDocumentFeedback() # KnowledgeGuestDocumentFeedback |  (optional)

try:
    # Give feedback on a document
    api_response = api_instance.post_knowledge_guest_session_document_feedback(session_id, document_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_guest_session_document_feedback: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| Knowledge guest session ID. |  |
| **document_id** | **str**| Document ID. |  |
| **body** | [**KnowledgeGuestDocumentFeedback**](KnowledgeGuestDocumentFeedback)|  | [optional]  |

### Return type

[**KnowledgeGuestDocumentFeedback**](KnowledgeGuestDocumentFeedback)


## post_knowledge_guest_session_document_views

>  post_knowledge_guest_session_document_views(session_id, document_id, body=body)


Create view event for a document.

Wraps POST /api/v2/knowledge/guest/sessions/{sessionId}/documents/{documentId}/views 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
session_id = 'session_id_example' # str | Knowledge guest session ID.
document_id = 'document_id_example' # str | Document ID
body = PureCloudPlatformClientV2.KnowledgeGuestDocumentView() # KnowledgeGuestDocumentView |  (optional)

try:
    # Create view event for a document.
    api_instance.post_knowledge_guest_session_document_views(session_id, document_id, body=body)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_guest_session_document_views: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| Knowledge guest session ID. |  |
| **document_id** | **str**| Document ID |  |
| **body** | [**KnowledgeGuestDocumentView**](KnowledgeGuestDocumentView)|  | [optional]  |

### Return type

void (empty response body)


## post_knowledge_guest_session_documents_answers

> [**KnowledgeGuestAnswerDocumentsResponse**](KnowledgeGuestAnswerDocumentsResponse) post_knowledge_guest_session_documents_answers(session_id, body)


Answer documents.

Wraps POST /api/v2/knowledge/guest/sessions/{sessionId}/documents/answers 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
session_id = 'session_id_example' # str | Knowledge guest session ID.
body = PureCloudPlatformClientV2.KnowledgeDocumentsAnswerFilter() # KnowledgeDocumentsAnswerFilter | 

try:
    # Answer documents.
    api_response = api_instance.post_knowledge_guest_session_documents_answers(session_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_guest_session_documents_answers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| Knowledge guest session ID. |  |
| **body** | [**KnowledgeDocumentsAnswerFilter**](KnowledgeDocumentsAnswerFilter)|  |  |

### Return type

[**KnowledgeGuestAnswerDocumentsResponse**](KnowledgeGuestAnswerDocumentsResponse)


## post_knowledge_guest_session_documents_presentations

>  post_knowledge_guest_session_documents_presentations(session_id, body=body)


Indicate that documents were presented to the user.

Wraps POST /api/v2/knowledge/guest/sessions/{sessionId}/documents/presentations 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
session_id = 'session_id_example' # str | Knowledge guest session ID.
body = PureCloudPlatformClientV2.KnowledgeGuestDocumentPresentation() # KnowledgeGuestDocumentPresentation |  (optional)

try:
    # Indicate that documents were presented to the user.
    api_instance.post_knowledge_guest_session_documents_presentations(session_id, body=body)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_guest_session_documents_presentations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| Knowledge guest session ID. |  |
| **body** | [**KnowledgeGuestDocumentPresentation**](KnowledgeGuestDocumentPresentation)|  | [optional]  |

### Return type

void (empty response body)


## post_knowledge_guest_session_documents_search

> [**KnowledgeDocumentGuestSearch**](KnowledgeDocumentGuestSearch) post_knowledge_guest_session_documents_search(session_id, expand=expand, body=body)


Search the documents in a guest session.

Wraps POST /api/v2/knowledge/guest/sessions/{sessionId}/documents/search 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
session_id = 'session_id_example' # str | Knowledge guest session ID.
expand = ['expand_example'] # list[str] | Fields, if any, to expand for each document in the search result matching the query. (optional)
body = PureCloudPlatformClientV2.KnowledgeDocumentGuestSearchRequest() # KnowledgeDocumentGuestSearchRequest |  (optional)

try:
    # Search the documents in a guest session.
    api_response = api_instance.post_knowledge_guest_session_documents_search(session_id, expand=expand, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_guest_session_documents_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| Knowledge guest session ID. |  |
| **expand** | [**list[str]**](str)| Fields, if any, to expand for each document in the search result matching the query. | [optional] <br />**Values**: documentVariations, documentAlternatives, knowledgeBaseLanguageCode |
| **body** | [**KnowledgeDocumentGuestSearchRequest**](KnowledgeDocumentGuestSearchRequest)|  | [optional]  |

### Return type

[**KnowledgeDocumentGuestSearch**](KnowledgeDocumentGuestSearch)


## post_knowledge_guest_session_documents_search_suggestions

> [**KnowledgeGuestDocumentSuggestion**](KnowledgeGuestDocumentSuggestion) post_knowledge_guest_session_documents_search_suggestions(session_id, body=body)


Query the knowledge documents to provide suggestions for auto completion.

Wraps POST /api/v2/knowledge/guest/sessions/{sessionId}/documents/search/suggestions 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
session_id = 'session_id_example' # str | Knowledge guest session ID.
body = PureCloudPlatformClientV2.KnowledgeGuestDocumentSuggestionRequest() # KnowledgeGuestDocumentSuggestionRequest |  (optional)

try:
    # Query the knowledge documents to provide suggestions for auto completion.
    api_response = api_instance.post_knowledge_guest_session_documents_search_suggestions(session_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_guest_session_documents_search_suggestions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| Knowledge guest session ID. |  |
| **body** | [**KnowledgeGuestDocumentSuggestionRequest**](KnowledgeGuestDocumentSuggestionRequest)|  | [optional]  |

### Return type

[**KnowledgeGuestDocumentSuggestion**](KnowledgeGuestDocumentSuggestion)


## post_knowledge_guest_sessions

> [**KnowledgeGuestSession**](KnowledgeGuestSession) post_knowledge_guest_sessions(body)


Create guest session

Wraps POST /api/v2/knowledge/guest/sessions 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.KnowledgeApi()
body = PureCloudPlatformClientV2.KnowledgeGuestSession() # KnowledgeGuestSession | 

try:
    # Create guest session
    api_response = api_instance.post_knowledge_guest_sessions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_guest_sessions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**KnowledgeGuestSession**](KnowledgeGuestSession)|  |  |

### Return type

[**KnowledgeGuestSession**](KnowledgeGuestSession)


## post_knowledge_knowledgebase_categories

> [**CategoryResponse**](CategoryResponse) post_knowledge_knowledgebase_categories(knowledge_base_id, body)


Create new category

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/categories 

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
body = PureCloudPlatformClientV2.CategoryCreateRequest() # CategoryCreateRequest | 

try:
    # Create new category
    api_response = api_instance.post_knowledge_knowledgebase_categories(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_categories: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**CategoryCreateRequest**](CategoryCreateRequest)|  |  |

### Return type

[**CategoryResponse**](CategoryResponse)


## post_knowledge_knowledgebase_document_copies

>  post_knowledge_knowledgebase_document_copies(knowledge_base_id, document_id, body=body)


Indicate that the document was copied by the user.

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/copies 

Requires ALL permissions: 

* knowledge:documentCopy:add

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
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID.
document_id = 'document_id_example' # str | Document ID.
body = PureCloudPlatformClientV2.KnowledgeDocumentCopy() # KnowledgeDocumentCopy |  (optional)

try:
    # Indicate that the document was copied by the user.
    api_instance.post_knowledge_knowledgebase_document_copies(knowledge_base_id, document_id, body=body)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_document_copies: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID. |  |
| **document_id** | **str**| Document ID. |  |
| **body** | [**KnowledgeDocumentCopy**](KnowledgeDocumentCopy)|  | [optional]  |

### Return type

void (empty response body)


## post_knowledge_knowledgebase_document_feedback

> [**KnowledgeDocumentFeedbackResponse**](KnowledgeDocumentFeedbackResponse) post_knowledge_knowledgebase_document_feedback(knowledge_base_id, document_id, body=body)


Give feedback on a document

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/feedback 

Requires ANY permissions: 

* knowledge:feedback:create

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
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID.
document_id = 'document_id_example' # str | Document ID.
body = PureCloudPlatformClientV2.KnowledgeDocumentFeedback() # KnowledgeDocumentFeedback |  (optional)

try:
    # Give feedback on a document
    api_response = api_instance.post_knowledge_knowledgebase_document_feedback(knowledge_base_id, document_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_document_feedback: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID. |  |
| **document_id** | **str**| Document ID. |  |
| **body** | [**KnowledgeDocumentFeedback**](KnowledgeDocumentFeedback)|  | [optional]  |

### Return type

[**KnowledgeDocumentFeedbackResponse**](KnowledgeDocumentFeedbackResponse)


## post_knowledge_knowledgebase_document_variations

> [**DocumentVariationResponse**](DocumentVariationResponse) post_knowledge_knowledgebase_document_variations(knowledge_base_id, document_id, body)


Create a variation for a document.

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/variations 

Requires ANY permissions: 

* knowledge:document:add
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
knowledge_base_id = 'knowledge_base_id_example' # str | Globally unique identifier for the knowledge base.
document_id = 'document_id_example' # str | Globally unique identifier for the document.
body = PureCloudPlatformClientV2.DocumentVariationRequest() # DocumentVariationRequest | 

try:
    # Create a variation for a document.
    api_response = api_instance.post_knowledge_knowledgebase_document_variations(knowledge_base_id, document_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_document_variations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Globally unique identifier for the knowledge base. |  |
| **document_id** | **str**| Globally unique identifier for the document. |  |
| **body** | [**DocumentVariationRequest**](DocumentVariationRequest)|  |  |

### Return type

[**DocumentVariationResponse**](DocumentVariationResponse)


## post_knowledge_knowledgebase_document_versions

> [**KnowledgeDocumentVersion**](KnowledgeDocumentVersion) post_knowledge_knowledgebase_document_versions(knowledge_base_id, document_id, body)


Creates or restores a document version.

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/versions 

Requires ALL permissions: 

* knowledge:documentVersion:add

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
knowledge_base_id = 'knowledge_base_id_example' # str | Globally unique identifier for the knowledge base.
document_id = 'document_id_example' # str | Globally unique identifier for the document.
body = PureCloudPlatformClientV2.KnowledgeDocumentVersion() # KnowledgeDocumentVersion | 

try:
    # Creates or restores a document version.
    api_response = api_instance.post_knowledge_knowledgebase_document_versions(knowledge_base_id, document_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_document_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Globally unique identifier for the knowledge base. |  |
| **document_id** | **str**| Globally unique identifier for the document. |  |
| **body** | [**KnowledgeDocumentVersion**](KnowledgeDocumentVersion)|  |  |

### Return type

[**KnowledgeDocumentVersion**](KnowledgeDocumentVersion)


## post_knowledge_knowledgebase_document_views

>  post_knowledge_knowledgebase_document_views(knowledge_base_id, document_id, body=body)


Create view for a document.

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/views 

Requires ALL permissions: 

* knowledge:documentView:add

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
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID.
document_id = 'document_id_example' # str | Document ID.
body = PureCloudPlatformClientV2.KnowledgeDocumentView() # KnowledgeDocumentView |  (optional)

try:
    # Create view for a document.
    api_instance.post_knowledge_knowledgebase_document_views(knowledge_base_id, document_id, body=body)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_document_views: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID. |  |
| **document_id** | **str**| Document ID. |  |
| **body** | [**KnowledgeDocumentView**](KnowledgeDocumentView)|  | [optional]  |

### Return type

void (empty response body)


## post_knowledge_knowledgebase_documents

> [**KnowledgeDocumentResponse**](KnowledgeDocumentResponse) post_knowledge_knowledgebase_documents(knowledge_base_id, body)


Create document.

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents 

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
body = PureCloudPlatformClientV2.KnowledgeDocumentCreateRequest() # KnowledgeDocumentCreateRequest | 

try:
    # Create document.
    api_response = api_instance.post_knowledge_knowledgebase_documents(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_documents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeDocumentCreateRequest**](KnowledgeDocumentCreateRequest)|  |  |

### Return type

[**KnowledgeDocumentResponse**](KnowledgeDocumentResponse)


## post_knowledge_knowledgebase_documents_answers

> [**KnowledgeAnswerDocumentsResponse**](KnowledgeAnswerDocumentsResponse) post_knowledge_knowledgebase_documents_answers(knowledge_base_id, body)


Answer documents.

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/answers 

Requires ALL permissions: 

* knowledge:document:view
* knowledge:documentAnswer:view

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
body = PureCloudPlatformClientV2.KnowledgeDocumentsAnswerFilter() # KnowledgeDocumentsAnswerFilter | 

try:
    # Answer documents.
    api_response = api_instance.post_knowledge_knowledgebase_documents_answers(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_documents_answers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeDocumentsAnswerFilter**](KnowledgeDocumentsAnswerFilter)|  |  |

### Return type

[**KnowledgeAnswerDocumentsResponse**](KnowledgeAnswerDocumentsResponse)


## post_knowledge_knowledgebase_documents_bulk_remove

> [**BulkResponse**](BulkResponse) post_knowledge_knowledgebase_documents_bulk_remove(knowledge_base_id, body)


Bulk remove documents.

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/bulk/remove 

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
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
body = PureCloudPlatformClientV2.KnowledgeDocumentBulkRemoveRequest() # KnowledgeDocumentBulkRemoveRequest | 

try:
    # Bulk remove documents.
    api_response = api_instance.post_knowledge_knowledgebase_documents_bulk_remove(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_documents_bulk_remove: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeDocumentBulkRemoveRequest**](KnowledgeDocumentBulkRemoveRequest)|  |  |

### Return type

[**BulkResponse**](BulkResponse)


## post_knowledge_knowledgebase_documents_bulk_update

> [**BulkResponse**](BulkResponse) post_knowledge_knowledgebase_documents_bulk_update(knowledge_base_id, body)


Bulk update documents.

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/bulk/update 

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
body = PureCloudPlatformClientV2.KnowledgeDocumentBulkUpdateRequest() # KnowledgeDocumentBulkUpdateRequest | 

try:
    # Bulk update documents.
    api_response = api_instance.post_knowledge_knowledgebase_documents_bulk_update(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_documents_bulk_update: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeDocumentBulkUpdateRequest**](KnowledgeDocumentBulkUpdateRequest)|  |  |

### Return type

[**BulkResponse**](BulkResponse)


## post_knowledge_knowledgebase_documents_presentations

>  post_knowledge_knowledgebase_documents_presentations(knowledge_base_id, body=body)


Indicate that documents were presented to the user.

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/presentations 

Requires ALL permissions: 

* knowledge:documentPresentation:add

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
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID.
body = PureCloudPlatformClientV2.KnowledgeDocumentPresentation() # KnowledgeDocumentPresentation |  (optional)

try:
    # Indicate that documents were presented to the user.
    api_instance.post_knowledge_knowledgebase_documents_presentations(knowledge_base_id, body=body)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_documents_presentations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID. |  |
| **body** | [**KnowledgeDocumentPresentation**](KnowledgeDocumentPresentation)|  | [optional]  |

### Return type

void (empty response body)


## post_knowledge_knowledgebase_documents_query

> [**KnowledgeDocumentQueryResponse**](KnowledgeDocumentQueryResponse) post_knowledge_knowledgebase_documents_query(knowledge_base_id, expand=expand, body=body)


Query for knowledge documents.

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/query 

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
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge Base ID
expand = ['expand_example'] # list[str] | Fields, if any, to expand for each document in the search result matching the query. (optional)
body = PureCloudPlatformClientV2.KnowledgeDocumentQuery() # KnowledgeDocumentQuery |  (optional)

try:
    # Query for knowledge documents.
    api_response = api_instance.post_knowledge_knowledgebase_documents_query(knowledge_base_id, expand=expand, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_documents_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge Base ID |  |
| **expand** | [**list[str]**](str)| Fields, if any, to expand for each document in the search result matching the query. | [optional] <br />**Values**: documentVariations, documentAlternatives, knowledgeBaseLanguageCode |
| **body** | [**KnowledgeDocumentQuery**](KnowledgeDocumentQuery)|  | [optional]  |

### Return type

[**KnowledgeDocumentQueryResponse**](KnowledgeDocumentQueryResponse)


## post_knowledge_knowledgebase_documents_search

> [**KnowledgeDocumentSearch**](KnowledgeDocumentSearch) post_knowledge_knowledgebase_documents_search(knowledge_base_id, expand=expand, body=body)


Search the documents in a knowledge base.

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/search 

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
knowledge_base_id = 'knowledge_base_id_example' # str | The ID of knowledge base containing the documents to query.
expand = ['expand_example'] # list[str] | Fields, if any, to expand for each document in the search result matching the query. (optional)
body = PureCloudPlatformClientV2.KnowledgeDocumentSearchRequest() # KnowledgeDocumentSearchRequest |  (optional)

try:
    # Search the documents in a knowledge base.
    api_response = api_instance.post_knowledge_knowledgebase_documents_search(knowledge_base_id, expand=expand, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_documents_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| The ID of knowledge base containing the documents to query. |  |
| **expand** | [**list[str]**](str)| Fields, if any, to expand for each document in the search result matching the query. | [optional] <br />**Values**: documentVariations, documentAlternatives, knowledgeBaseLanguageCode |
| **body** | [**KnowledgeDocumentSearchRequest**](KnowledgeDocumentSearchRequest)|  | [optional]  |

### Return type

[**KnowledgeDocumentSearch**](KnowledgeDocumentSearch)


## post_knowledge_knowledgebase_documents_search_suggestions

> [**KnowledgeDocumentSuggestion**](KnowledgeDocumentSuggestion) post_knowledge_knowledgebase_documents_search_suggestions(knowledge_base_id, body=body)


Query the knowledge documents to provide suggestions for auto completion.

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/search/suggestions 

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
knowledge_base_id = 'knowledge_base_id_example' # str | The ID of knowledge base containing the documents to query.
body = PureCloudPlatformClientV2.KnowledgeDocumentSuggestionRequest() # KnowledgeDocumentSuggestionRequest |  (optional)

try:
    # Query the knowledge documents to provide suggestions for auto completion.
    api_response = api_instance.post_knowledge_knowledgebase_documents_search_suggestions(knowledge_base_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_documents_search_suggestions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| The ID of knowledge base containing the documents to query. |  |
| **body** | [**KnowledgeDocumentSuggestionRequest**](KnowledgeDocumentSuggestionRequest)|  | [optional]  |

### Return type

[**KnowledgeDocumentSuggestion**](KnowledgeDocumentSuggestion)


## post_knowledge_knowledgebase_documents_versions_bulk_add

> [**BulkResponse**](BulkResponse) post_knowledge_knowledgebase_documents_versions_bulk_add(knowledge_base_id, body)


Bulk add document versions.

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/versions/bulk/add 

Requires ALL permissions: 

* knowledge:documentVersion:add

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
body = PureCloudPlatformClientV2.KnowledgeDocumentBulkVersionAddRequest() # KnowledgeDocumentBulkVersionAddRequest | 

try:
    # Bulk add document versions.
    api_response = api_instance.post_knowledge_knowledgebase_documents_versions_bulk_add(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_documents_versions_bulk_add: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeDocumentBulkVersionAddRequest**](KnowledgeDocumentBulkVersionAddRequest)|  |  |

### Return type

[**BulkResponse**](BulkResponse)


## post_knowledge_knowledgebase_export_jobs

> [**KnowledgeExportJobResponse**](KnowledgeExportJobResponse) post_knowledge_knowledgebase_export_jobs(knowledge_base_id, body)


Create export job

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/export/jobs 

Requires ALL permissions: 

* knowledge:exportJob:add

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
body = PureCloudPlatformClientV2.KnowledgeExportJobRequest() # KnowledgeExportJobRequest | 

try:
    # Create export job
    api_response = api_instance.post_knowledge_knowledgebase_export_jobs(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_export_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeExportJobRequest**](KnowledgeExportJobRequest)|  |  |

### Return type

[**KnowledgeExportJobResponse**](KnowledgeExportJobResponse)


## post_knowledge_knowledgebase_import_jobs

> [**KnowledgeImportJobResponse**](KnowledgeImportJobResponse) post_knowledge_knowledgebase_import_jobs(knowledge_base_id, body)


Create import job

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/import/jobs 

Requires ALL permissions: 

* knowledge:importJob:add

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
body = PureCloudPlatformClientV2.KnowledgeImportJobRequest() # KnowledgeImportJobRequest | 

try:
    # Create import job
    api_response = api_instance.post_knowledge_knowledgebase_import_jobs(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_import_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeImportJobRequest**](KnowledgeImportJobRequest)|  |  |

### Return type

[**KnowledgeImportJobResponse**](KnowledgeImportJobResponse)


## post_knowledge_knowledgebase_labels

> [**LabelResponse**](LabelResponse) post_knowledge_knowledgebase_labels(knowledge_base_id, body)


Create new label

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/labels 

Requires ALL permissions: 

* knowledge:label:add

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
body = PureCloudPlatformClientV2.LabelCreateRequest() # LabelCreateRequest | 

try:
    # Create new label
    api_response = api_instance.post_knowledge_knowledgebase_labels(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_labels: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**LabelCreateRequest**](LabelCreateRequest)|  |  |

### Return type

[**LabelResponse**](LabelResponse)


## post_knowledge_knowledgebase_language_categories

> [**KnowledgeExtendedCategory**](KnowledgeExtendedCategory) post_knowledge_knowledgebase_language_categories(knowledge_base_id, language_code, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_language_categories: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **body** | [**KnowledgeCategoryRequest**](KnowledgeCategoryRequest)|  |  |

### Return type

[**KnowledgeExtendedCategory**](KnowledgeExtendedCategory)


## post_knowledge_knowledgebase_language_document_uploads

> [**KnowledgeDocumentContentUpload**](KnowledgeDocumentContentUpload) post_knowledge_knowledgebase_language_document_uploads(document_id, knowledge_base_id, language_code, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Upload Article Content

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/{documentId}/uploads 

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
body = PureCloudPlatformClientV2.KnowledgeDocumentContentUpload() # KnowledgeDocumentContentUpload | 

try:
    # Upload Article Content
    api_response = api_instance.post_knowledge_knowledgebase_language_document_uploads(document_id, knowledge_base_id, language_code, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_language_document_uploads: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **document_id** | **str**| Document ID |  |
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **body** | [**KnowledgeDocumentContentUpload**](KnowledgeDocumentContentUpload)|  |  |

### Return type

[**KnowledgeDocumentContentUpload**](KnowledgeDocumentContentUpload)


## post_knowledge_knowledgebase_language_documents

> [**KnowledgeDocument**](KnowledgeDocument) post_knowledge_knowledgebase_language_documents(knowledge_base_id, language_code, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_language_documents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **body** | [**KnowledgeDocumentRequest**](KnowledgeDocumentRequest)|  |  |

### Return type

[**KnowledgeDocument**](KnowledgeDocument)


## post_knowledge_knowledgebase_language_documents_imports

> [**KnowledgeImport**](KnowledgeImport) post_knowledge_knowledgebase_language_documents_imports(knowledge_base_id, language_code, body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Create import operation

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/imports 

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
body = PureCloudPlatformClientV2.KnowledgeImport() # KnowledgeImport | 

try:
    # Create import operation
    api_response = api_instance.post_knowledge_knowledgebase_language_documents_imports(knowledge_base_id, language_code, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_language_documents_imports: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **body** | [**KnowledgeImport**](KnowledgeImport)|  |  |

### Return type

[**KnowledgeImport**](KnowledgeImport)


## post_knowledge_knowledgebase_language_training_promote

> [**KnowledgeTraining**](KnowledgeTraining) post_knowledge_knowledgebase_language_training_promote(knowledge_base_id, language_code, training_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_language_training_promote: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |
| **training_id** | **str**| Training ID |  |

### Return type

[**KnowledgeTraining**](KnowledgeTraining)


## post_knowledge_knowledgebase_language_trainings

> [**KnowledgeTraining**](KnowledgeTraining) post_knowledge_knowledgebase_language_trainings(knowledge_base_id, language_code)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_language_trainings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **language_code** | **str**| Language code, format: iso2-LOCALE | <br />**Values**: en-US, en-UK, en-AU, en-CA, en-HK, en-IN, en-IE, en-NZ, en-PH, en-SG, en-ZA, de-DE, de-AT, de-CH, es-AR, es-CO, es-MX, es-US, es-ES, fr-FR, fr-BE, fr-CA, fr-CH, pt-BR, pt-PT, nl-NL, nl-BE, it-IT, ca-ES, tr-TR, sv-SE, fi-FI, nb-NO, da-DK, ja-JP, ar-AE, zh-CN, zh-TW, zh-HK, ko-KR, pl-PL, hi-IN, th-TH, hu-HU, vi-VN, uk-UA |

### Return type

[**KnowledgeTraining**](KnowledgeTraining)


## post_knowledge_knowledgebase_parse_job_import

>  post_knowledge_knowledgebase_parse_job_import(knowledge_base_id, parse_job_id, body)


Import the parsed articles

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/parse/jobs/{parseJobId}/import 

Requires ALL permissions: 

* knowledge:importJob:edit

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
parse_job_id = 'parse_job_id_example' # str | Parse job ID
body = PureCloudPlatformClientV2.KnowledgeParseJobRequestImport() # KnowledgeParseJobRequestImport | 

try:
    # Import the parsed articles
    api_instance.post_knowledge_knowledgebase_parse_job_import(knowledge_base_id, parse_job_id, body)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_parse_job_import: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **parse_job_id** | **str**| Parse job ID |  |
| **body** | [**KnowledgeParseJobRequestImport**](KnowledgeParseJobRequestImport)|  |  |

### Return type

void (empty response body)


## post_knowledge_knowledgebase_parse_jobs

> [**KnowledgeParseJobResponse**](KnowledgeParseJobResponse) post_knowledge_knowledgebase_parse_jobs(knowledge_base_id, body)


Create parse job

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/parse/jobs 

Requires ALL permissions: 

* knowledge:importJob:add

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
body = PureCloudPlatformClientV2.KnowledgeParseJobRequest() # KnowledgeParseJobRequest | 

try:
    # Create parse job
    api_response = api_instance.post_knowledge_knowledgebase_parse_jobs(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_parse_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeParseJobRequest**](KnowledgeParseJobRequest)|  |  |

### Return type

[**KnowledgeParseJobResponse**](KnowledgeParseJobResponse)


## post_knowledge_knowledgebase_search

> [**KnowledgeSearchResponse**](KnowledgeSearchResponse) post_knowledge_knowledgebase_search(knowledge_base_id, body=body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

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
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeSearchRequest**](KnowledgeSearchRequest)|  | [optional]  |

### Return type

[**KnowledgeSearchResponse**](KnowledgeSearchResponse)


## post_knowledge_knowledgebase_sources_salesforce

> [**KnowledgeSyncJobResponse**](KnowledgeSyncJobResponse) post_knowledge_knowledgebase_sources_salesforce(knowledge_base_id, body)


Create Salesforce Knowledge integration source

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/salesforce 

Requires ALL permissions: 

* knowledge:integrationSource:add

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
body = PureCloudPlatformClientV2.SalesforceSourceRequest() # SalesforceSourceRequest | 

try:
    # Create Salesforce Knowledge integration source
    api_response = api_instance.post_knowledge_knowledgebase_sources_salesforce(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_sources_salesforce: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**SalesforceSourceRequest**](SalesforceSourceRequest)|  |  |

### Return type

[**KnowledgeSyncJobResponse**](KnowledgeSyncJobResponse)


## post_knowledge_knowledgebase_sources_salesforce_source_id_sync

> [**SourceSyncResponse**](SourceSyncResponse) post_knowledge_knowledgebase_sources_salesforce_source_id_sync(knowledge_base_id, source_id, body=body)


Start sync on Salesforce Knowledge integration source

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/salesforce/{sourceId}/sync 

Requires ALL permissions: 

* knowledge:integrationSource:edit

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
source_id = 'source_id_example' # str | Source ID
body = NULL # object |  (optional)

try:
    # Start sync on Salesforce Knowledge integration source
    api_response = api_instance.post_knowledge_knowledgebase_sources_salesforce_source_id_sync(knowledge_base_id, source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_sources_salesforce_source_id_sync: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **source_id** | **str**| Source ID |  |
| **body** | **object**|  | [optional]  |

### Return type

[**SourceSyncResponse**](SourceSyncResponse)


## post_knowledge_knowledgebase_sources_servicenow

> [**KnowledgeSyncJobResponse**](KnowledgeSyncJobResponse) post_knowledge_knowledgebase_sources_servicenow(knowledge_base_id, body)


Create ServiceNow Knowledge integration source

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/servicenow 

Requires ALL permissions: 

* knowledge:integrationSource:add

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
body = PureCloudPlatformClientV2.ServiceNowSourceRequest() # ServiceNowSourceRequest | 

try:
    # Create ServiceNow Knowledge integration source
    api_response = api_instance.post_knowledge_knowledgebase_sources_servicenow(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_sources_servicenow: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**ServiceNowSourceRequest**](ServiceNowSourceRequest)|  |  |

### Return type

[**KnowledgeSyncJobResponse**](KnowledgeSyncJobResponse)


## post_knowledge_knowledgebase_sources_servicenow_source_id_sync

> [**SourceSyncResponse**](SourceSyncResponse) post_knowledge_knowledgebase_sources_servicenow_source_id_sync(knowledge_base_id, source_id, body=body)


Start synchronization on ServiceNow Knowledge integration source

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/servicenow/{sourceId}/sync 

Requires ALL permissions: 

* knowledge:integrationSource:edit

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
source_id = 'source_id_example' # str | Source ID
body = NULL # object |  (optional)

try:
    # Start synchronization on ServiceNow Knowledge integration source
    api_response = api_instance.post_knowledge_knowledgebase_sources_servicenow_source_id_sync(knowledge_base_id, source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_sources_servicenow_source_id_sync: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **source_id** | **str**| Source ID |  |
| **body** | **object**|  | [optional]  |

### Return type

[**SourceSyncResponse**](SourceSyncResponse)


## post_knowledge_knowledgebase_synchronize_jobs

> [**KnowledgeSyncJobResponse**](KnowledgeSyncJobResponse) post_knowledge_knowledgebase_synchronize_jobs(knowledge_base_id, body)


Create synchronization job

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/synchronize/jobs 

Requires ALL permissions: 

* knowledge:syncJob:add

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
body = PureCloudPlatformClientV2.KnowledgeSyncJobRequest() # KnowledgeSyncJobRequest | 

try:
    # Create synchronization job
    api_response = api_instance.post_knowledge_knowledgebase_synchronize_jobs(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_synchronize_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeSyncJobRequest**](KnowledgeSyncJobRequest)|  |  |

### Return type

[**KnowledgeSyncJobResponse**](KnowledgeSyncJobResponse)


## post_knowledge_knowledgebase_uploads_urls_jobs

> [**CreateUploadSourceUrlJobResponse**](CreateUploadSourceUrlJobResponse) post_knowledge_knowledgebase_uploads_urls_jobs(knowledge_base_id, body)


Create content upload from URL job

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/uploads/urls/jobs 

Requires ALL permissions: 

* knowledge:uploadSourceUrlJob:add

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
body = PureCloudPlatformClientV2.CreateUploadSourceUrlJobRequest() # CreateUploadSourceUrlJobRequest | uploadRequest

try:
    # Create content upload from URL job
    api_response = api_instance.post_knowledge_knowledgebase_uploads_urls_jobs(knowledge_base_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebase_uploads_urls_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**CreateUploadSourceUrlJobRequest**](CreateUploadSourceUrlJobRequest)| uploadRequest |  |

### Return type

[**CreateUploadSourceUrlJobResponse**](CreateUploadSourceUrlJobResponse)


## post_knowledge_knowledgebases

> [**KnowledgeBase**](KnowledgeBase) post_knowledge_knowledgebases(body)


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
body = PureCloudPlatformClientV2.KnowledgeBaseCreateRequest() # KnowledgeBaseCreateRequest | 

try:
    # Create new knowledge base
    api_response = api_instance.post_knowledge_knowledgebases(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->post_knowledge_knowledgebases: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**KnowledgeBaseCreateRequest**](KnowledgeBaseCreateRequest)|  |  |

### Return type

[**KnowledgeBase**](KnowledgeBase)


## put_knowledge_knowledgebase_sources_salesforce_source_id

> [**SalesforceSourceResponse**](SalesforceSourceResponse) put_knowledge_knowledgebase_sources_salesforce_source_id(knowledge_base_id, source_id, body)


Update Salesforce Knowledge integration source

Wraps PUT /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/salesforce/{sourceId} 

Requires ALL permissions: 

* knowledge:integrationSource:edit

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
source_id = 'source_id_example' # str | Source ID
body = PureCloudPlatformClientV2.SalesforceSourceRequest() # SalesforceSourceRequest | 

try:
    # Update Salesforce Knowledge integration source
    api_response = api_instance.put_knowledge_knowledgebase_sources_salesforce_source_id(knowledge_base_id, source_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->put_knowledge_knowledgebase_sources_salesforce_source_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **source_id** | **str**| Source ID |  |
| **body** | [**SalesforceSourceRequest**](SalesforceSourceRequest)|  |  |

### Return type

[**SalesforceSourceResponse**](SalesforceSourceResponse)


## put_knowledge_knowledgebase_sources_servicenow_source_id

> [**ServiceNowSourceResponse**](ServiceNowSourceResponse) put_knowledge_knowledgebase_sources_servicenow_source_id(knowledge_base_id, source_id, body)


Update ServiceNow Knowledge integration source

Wraps PUT /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/servicenow/{sourceId} 

Requires ALL permissions: 

* knowledge:integrationSource:edit

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
source_id = 'source_id_example' # str | Source ID
body = PureCloudPlatformClientV2.ServiceNowSourceRequest() # ServiceNowSourceRequest | 

try:
    # Update ServiceNow Knowledge integration source
    api_response = api_instance.put_knowledge_knowledgebase_sources_servicenow_source_id(knowledge_base_id, source_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->put_knowledge_knowledgebase_sources_servicenow_source_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **source_id** | **str**| Source ID |  |
| **body** | [**ServiceNowSourceRequest**](ServiceNowSourceRequest)|  |  |

### Return type

[**ServiceNowSourceResponse**](ServiceNowSourceResponse)


_PureCloudPlatformClientV2 226.0.0_

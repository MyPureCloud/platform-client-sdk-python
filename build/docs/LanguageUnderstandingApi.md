# LanguageUnderstandingApi

## PureCloudPlatformClientV2.LanguageUnderstandingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_languageunderstanding_domain**](#delete_languageunderstanding_domain) | Delete an NLU Domain.|
|[**delete_languageunderstanding_domain_feedback_feedback_id**](#delete_languageunderstanding_domain_feedback_feedback_id) | Delete the feedback on the NLU Domain Version.|
|[**delete_languageunderstanding_domain_version**](#delete_languageunderstanding_domain_version) | Delete an NLU Domain Version|
|[**delete_languageunderstanding_miner**](#delete_languageunderstanding_miner) | Delete a miner.|
|[**delete_languageunderstanding_miner_draft**](#delete_languageunderstanding_miner_draft) | Delete a draft|
|[**get_languageunderstanding_domain**](#get_languageunderstanding_domain) | Find an NLU Domain.|
|[**get_languageunderstanding_domain_feedback**](#get_languageunderstanding_domain_feedback) | Get all feedback in the given NLU Domain Version.|
|[**get_languageunderstanding_domain_feedback_feedback_id**](#get_languageunderstanding_domain_feedback_feedback_id) | Find a Feedback|
|[**get_languageunderstanding_domain_version**](#get_languageunderstanding_domain_version) | Find an NLU Domain Version.|
|[**get_languageunderstanding_domain_version_report**](#get_languageunderstanding_domain_version_report) | Retrieved quality report for the specified NLU Domain Version|
|[**get_languageunderstanding_domain_versions**](#get_languageunderstanding_domain_versions) | Get all NLU Domain Versions for a given Domain.|
|[**get_languageunderstanding_domains**](#get_languageunderstanding_domains) | Get all NLU Domains.|
|[**get_languageunderstanding_miner**](#get_languageunderstanding_miner) | Get information about a miner.|
|[**get_languageunderstanding_miner_draft**](#get_languageunderstanding_miner_draft) | Get information about a draft.|
|[**get_languageunderstanding_miner_drafts**](#get_languageunderstanding_miner_drafts) | Retrieve the list of drafts created.|
|[**get_languageunderstanding_miner_intent**](#get_languageunderstanding_miner_intent) | Get information about a mined intent|
|[**get_languageunderstanding_miner_intents**](#get_languageunderstanding_miner_intents) | Retrieve a list of mined intents.|
|[**get_languageunderstanding_miner_topic**](#get_languageunderstanding_miner_topic) | Retrieves details of a particular topic.|
|[**get_languageunderstanding_miner_topic_phrase**](#get_languageunderstanding_miner_topic_phrase) | Retrieves utterances related to a phrase in a topic.|
|[**get_languageunderstanding_miner_topics**](#get_languageunderstanding_miner_topics) | Retrieve a list of mined topics.|
|[**get_languageunderstanding_miners**](#get_languageunderstanding_miners) | Retrieve the list of miners created.|
|[**get_languageunderstanding_settings**](#get_languageunderstanding_settings) | Get Organization Configuration|
|[**patch_languageunderstanding_domain**](#patch_languageunderstanding_domain) | Update an NLU Domain.|
|[**patch_languageunderstanding_miner_draft**](#patch_languageunderstanding_miner_draft) | Save information for the draft. Either topic draft or intent draft should be sent.|
|[**post_languageunderstanding_domain_feedback**](#post_languageunderstanding_domain_feedback) | Create feedback for the NLU Domain Version.|
|[**post_languageunderstanding_domain_version_detect**](#post_languageunderstanding_domain_version_detect) | Detect intent, entities, etc. in the submitted text using the specified NLU domain version.|
|[**post_languageunderstanding_domain_version_publish**](#post_languageunderstanding_domain_version_publish) | Publish the draft NLU Domain Version.|
|[**post_languageunderstanding_domain_version_train**](#post_languageunderstanding_domain_version_train) | Train the draft NLU Domain Version.|
|[**post_languageunderstanding_domain_versions**](#post_languageunderstanding_domain_versions) | Create an NLU Domain Version.|
|[**post_languageunderstanding_domains**](#post_languageunderstanding_domains) | Create an NLU Domain.|
|[**post_languageunderstanding_miner_drafts**](#post_languageunderstanding_miner_drafts) | Create a new draft resource.|
|[**post_languageunderstanding_miner_execute**](#post_languageunderstanding_miner_execute) | Start the mining process. Specify date range pair with mediaType, queueIds, participantType for mining data from Genesys Cloud. Specify only uploadKey for mining through an external file.|
|[**post_languageunderstanding_miners**](#post_languageunderstanding_miners) | Create a unique miner.|
|[**put_languageunderstanding_domain_version**](#put_languageunderstanding_domain_version) | Update an NLU Domain Version.|



## delete_languageunderstanding_domain

>  delete_languageunderstanding_domain(domain_id)


Delete an NLU Domain.

Wraps DELETE /api/v2/languageunderstanding/domains/{domainId} 

Requires ANY permissions: 

* languageUnderstanding:nluDomain:delete
* dialog:bot:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.

try:
    # Delete an NLU Domain.
    api_instance.delete_languageunderstanding_domain(domain_id)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->delete_languageunderstanding_domain: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |

### Return type

void (empty response body)


## delete_languageunderstanding_domain_feedback_feedback_id

>  delete_languageunderstanding_domain_feedback_feedback_id(domain_id, feedback_id)


Delete the feedback on the NLU Domain Version.

Wraps DELETE /api/v2/languageunderstanding/domains/{domainId}/feedback/{feedbackId} 

Requires ANY permissions: 

* languageUnderstanding:feedback:delete
* dialog:bot:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.
feedback_id = 'feedback_id_example' # str | ID of the Feedback

try:
    # Delete the feedback on the NLU Domain Version.
    api_instance.delete_languageunderstanding_domain_feedback_feedback_id(domain_id, feedback_id)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->delete_languageunderstanding_domain_feedback_feedback_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **feedback_id** | **str**| ID of the Feedback |  |

### Return type

void (empty response body)


## delete_languageunderstanding_domain_version

>  delete_languageunderstanding_domain_version(domain_id, domain_version_id)


Delete an NLU Domain Version

Wraps DELETE /api/v2/languageunderstanding/domains/{domainId}/versions/{domainVersionId} 

Requires ANY permissions: 

* languageUnderstanding:nluDomainVersion:delete
* dialog:botVersion:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.
domain_version_id = 'domain_version_id_example' # str | ID of the NLU domain version.

try:
    # Delete an NLU Domain Version
    api_instance.delete_languageunderstanding_domain_version(domain_id, domain_version_id)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->delete_languageunderstanding_domain_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **domain_version_id** | **str**| ID of the NLU domain version. |  |

### Return type

void (empty response body)


## delete_languageunderstanding_miner

>  delete_languageunderstanding_miner(miner_id)


Delete a miner.

Wraps DELETE /api/v2/languageunderstanding/miners/{minerId} 

Requires ALL permissions: 

* languageUnderstanding:miner:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
miner_id = 'miner_id_example' # str | Miner ID

try:
    # Delete a miner.
    api_instance.delete_languageunderstanding_miner(miner_id)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->delete_languageunderstanding_miner: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_id** | **str**| Miner ID |  |

### Return type

void (empty response body)


## delete_languageunderstanding_miner_draft

>  delete_languageunderstanding_miner_draft(miner_id, draft_id)


Delete a draft

Wraps DELETE /api/v2/languageunderstanding/miners/{minerId}/drafts/{draftId} 

Requires ALL permissions: 

* languageUnderstanding:draft:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
miner_id = 'miner_id_example' # str | Miner ID
draft_id = 'draft_id_example' # str | Draft ID

try:
    # Delete a draft
    api_instance.delete_languageunderstanding_miner_draft(miner_id, draft_id)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->delete_languageunderstanding_miner_draft: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_id** | **str**| Miner ID |  |
| **draft_id** | **str**| Draft ID |  |

### Return type

void (empty response body)


## get_languageunderstanding_domain

> [**NluDomain**](NluDomain) get_languageunderstanding_domain(domain_id)


Find an NLU Domain.

Wraps GET /api/v2/languageunderstanding/domains/{domainId} 

Requires ANY permissions: 

* languageUnderstanding:nluDomain:view
* dialog:bot:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.

try:
    # Find an NLU Domain.
    api_response = api_instance.get_languageunderstanding_domain(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_domain: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |

### Return type

[**NluDomain**](NluDomain)


## get_languageunderstanding_domain_feedback

> [**NluFeedbackListing**](NluFeedbackListing) get_languageunderstanding_domain_feedback(domain_id, intent_name=intent_name, assessment=assessment, date_start=date_start, date_end=date_end, include_deleted=include_deleted, language=language, page_number=page_number, page_size=page_size, enable_cursor_pagination=enable_cursor_pagination, include_training_utterances=include_training_utterances, after=after, fields=fields)


Get all feedback in the given NLU Domain Version.

Wraps GET /api/v2/languageunderstanding/domains/{domainId}/feedback 

Requires ANY permissions: 

* languageUnderstanding:feedback:view
* dialog:bot:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.
intent_name = 'intent_name_example' # str | The top intent name to retrieve feedback for. (optional)
assessment = 'assessment_example' # str | The top assessment to retrieve feedback for. (optional)
date_start = '2013-10-20' # date | Begin of time window as ISO-8601 date. (optional)
date_end = '2013-10-20' # date | End of time window as ISO-8601 date. (optional)
include_deleted = True # bool | Whether to include soft-deleted items in the result. (optional)
language = 'language_example' # str | Whether to filter response based on the language, e.g. en-us, pt-br. (optional)
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
enable_cursor_pagination = False # bool | Enable Cursor Pagination (optional) (default to False)
include_training_utterances = True # bool | Include Training Utterances. By default they're included. (optional) (default to True)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. This is considered only when enableCursorPagination=true (optional)
fields = ['fields_example'] # list[str] | Fields and properties to get, comma-separated (optional)

try:
    # Get all feedback in the given NLU Domain Version.
    api_response = api_instance.get_languageunderstanding_domain_feedback(domain_id, intent_name=intent_name, assessment=assessment, date_start=date_start, date_end=date_end, include_deleted=include_deleted, language=language, page_number=page_number, page_size=page_size, enable_cursor_pagination=enable_cursor_pagination, include_training_utterances=include_training_utterances, after=after, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_domain_feedback: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **intent_name** | **str**| The top intent name to retrieve feedback for. | [optional]  |
| **assessment** | **str**| The top assessment to retrieve feedback for. | [optional] <br />**Values**: Incorrect, Correct, Unknown, Disabled |
| **date_start** | **date**| Begin of time window as ISO-8601 date. | [optional]  |
| **date_end** | **date**| End of time window as ISO-8601 date. | [optional]  |
| **include_deleted** | **bool**| Whether to include soft-deleted items in the result. | [optional]  |
| **language** | **str**| Whether to filter response based on the language, e.g. en-us, pt-br. | [optional]  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **enable_cursor_pagination** | **bool**| Enable Cursor Pagination | [optional] [default to False] |
| **include_training_utterances** | **bool**| Include Training Utterances. By default they&#39;re included. | [optional] [default to True] |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. This is considered only when enableCursorPagination&#x3D;true | [optional]  |
| **fields** | [**list[str]**](str)| Fields and properties to get, comma-separated | [optional] <br />**Values**: version, dateCreated, text, intents |

### Return type

[**NluFeedbackListing**](NluFeedbackListing)


## get_languageunderstanding_domain_feedback_feedback_id

> [**NluFeedbackResponse**](NluFeedbackResponse) get_languageunderstanding_domain_feedback_feedback_id(domain_id, feedback_id, fields=fields)


Find a Feedback

Wraps GET /api/v2/languageunderstanding/domains/{domainId}/feedback/{feedbackId} 

Requires ANY permissions: 

* languageUnderstanding:feedback:view
* dialog:bot:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.
feedback_id = 'feedback_id_example' # str | ID of the Feedback
fields = ['fields_example'] # list[str] | Fields and properties to get, comma-separated (optional)

try:
    # Find a Feedback
    api_response = api_instance.get_languageunderstanding_domain_feedback_feedback_id(domain_id, feedback_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_domain_feedback_feedback_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **feedback_id** | **str**| ID of the Feedback |  |
| **fields** | [**list[str]**](str)| Fields and properties to get, comma-separated | [optional] <br />**Values**: version, dateCreated, text, intents |

### Return type

[**NluFeedbackResponse**](NluFeedbackResponse)


## get_languageunderstanding_domain_version

> [**NluDomainVersion**](NluDomainVersion) get_languageunderstanding_domain_version(domain_id, domain_version_id, include_utterances=include_utterances)


Find an NLU Domain Version.

Wraps GET /api/v2/languageunderstanding/domains/{domainId}/versions/{domainVersionId} 

Requires ANY permissions: 

* languageUnderstanding:nluDomainVersion:view
* dialog:botVersion:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.
domain_version_id = 'domain_version_id_example' # str | ID of the NLU domain version.
include_utterances = True # bool | Whether utterances for intent definition should be included when marshalling response. (optional)

try:
    # Find an NLU Domain Version.
    api_response = api_instance.get_languageunderstanding_domain_version(domain_id, domain_version_id, include_utterances=include_utterances)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_domain_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **domain_version_id** | **str**| ID of the NLU domain version. |  |
| **include_utterances** | **bool**| Whether utterances for intent definition should be included when marshalling response. | [optional]  |

### Return type

[**NluDomainVersion**](NluDomainVersion)


## get_languageunderstanding_domain_version_report

> [**NluDomainVersionQualityReport**](NluDomainVersionQualityReport) get_languageunderstanding_domain_version_report(domain_id, domain_version_id)


Retrieved quality report for the specified NLU Domain Version

Wraps GET /api/v2/languageunderstanding/domains/{domainId}/versions/{domainVersionId}/report 

Requires ANY permissions: 

* languageUnderstanding:nluDomainVersion:view
* dialog:botVersion:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.
domain_version_id = 'domain_version_id_example' # str | ID of the NLU domain version.

try:
    # Retrieved quality report for the specified NLU Domain Version
    api_response = api_instance.get_languageunderstanding_domain_version_report(domain_id, domain_version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_domain_version_report: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **domain_version_id** | **str**| ID of the NLU domain version. |  |

### Return type

[**NluDomainVersionQualityReport**](NluDomainVersionQualityReport)


## get_languageunderstanding_domain_versions

> [**NluDomainVersionListing**](NluDomainVersionListing) get_languageunderstanding_domain_versions(domain_id, include_utterances=include_utterances, page_number=page_number, page_size=page_size)


Get all NLU Domain Versions for a given Domain.

Wraps GET /api/v2/languageunderstanding/domains/{domainId}/versions 

Requires ANY permissions: 

* languageUnderstanding:nluDomainVersion:view
* dialog:botVersion:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.
include_utterances = True # bool | Whether utterances for intent definition should be included when marshalling response. (optional)
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get all NLU Domain Versions for a given Domain.
    api_response = api_instance.get_languageunderstanding_domain_versions(domain_id, include_utterances=include_utterances, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_domain_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **include_utterances** | **bool**| Whether utterances for intent definition should be included when marshalling response. | [optional]  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**NluDomainVersionListing**](NluDomainVersionListing)


## get_languageunderstanding_domains

> [**NluDomainListing**](NluDomainListing) get_languageunderstanding_domains(page_number=page_number, page_size=page_size)


Get all NLU Domains.

Wraps GET /api/v2/languageunderstanding/domains 

Requires ANY permissions: 

* languageUnderstanding:nluDomain:view
* dialog:bot:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get all NLU Domains.
    api_response = api_instance.get_languageunderstanding_domains(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_domains: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**NluDomainListing**](NluDomainListing)


## get_languageunderstanding_miner

> [**Miner**](Miner) get_languageunderstanding_miner(miner_id)


Get information about a miner.

Wraps GET /api/v2/languageunderstanding/miners/{minerId} 

Requires ALL permissions: 

* languageUnderstanding:miner:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
miner_id = 'miner_id_example' # str | Miner ID

try:
    # Get information about a miner.
    api_response = api_instance.get_languageunderstanding_miner(miner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_miner: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_id** | **str**| Miner ID |  |

### Return type

[**Miner**](Miner)


## get_languageunderstanding_miner_draft

> [**Draft**](Draft) get_languageunderstanding_miner_draft(miner_id, draft_id, draft_intent_id=draft_intent_id, draft_topic_id=draft_topic_id)


Get information about a draft.

Wraps GET /api/v2/languageunderstanding/miners/{minerId}/drafts/{draftId} 

Requires ALL permissions: 

* languageUnderstanding:draft:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
miner_id = 'miner_id_example' # str | Miner ID
draft_id = 'draft_id_example' # str | Draft ID
draft_intent_id = 'draft_intent_id_example' # str | Parameter to filter a specific intent. (optional)
draft_topic_id = 'draft_topic_id_example' # str | Parameter to filter a specific topic. (optional)

try:
    # Get information about a draft.
    api_response = api_instance.get_languageunderstanding_miner_draft(miner_id, draft_id, draft_intent_id=draft_intent_id, draft_topic_id=draft_topic_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_miner_draft: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_id** | **str**| Miner ID |  |
| **draft_id** | **str**| Draft ID |  |
| **draft_intent_id** | **str**| Parameter to filter a specific intent. | [optional]  |
| **draft_topic_id** | **str**| Parameter to filter a specific topic. | [optional]  |

### Return type

[**Draft**](Draft)


## get_languageunderstanding_miner_drafts

> [**DraftListing**](DraftListing) get_languageunderstanding_miner_drafts(miner_id)


Retrieve the list of drafts created.

Wraps GET /api/v2/languageunderstanding/miners/{minerId}/drafts 

Requires ALL permissions: 

* languageUnderstanding:draft:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
miner_id = 'miner_id_example' # str | Miner ID

try:
    # Retrieve the list of drafts created.
    api_response = api_instance.get_languageunderstanding_miner_drafts(miner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_miner_drafts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_id** | **str**| Miner ID |  |

### Return type

[**DraftListing**](DraftListing)


## get_languageunderstanding_miner_intent

> [**MinerIntent**](MinerIntent) get_languageunderstanding_miner_intent(miner_id, intent_id, expand=expand)


Get information about a mined intent

Wraps GET /api/v2/languageunderstanding/miners/{minerId}/intents/{intentId} 

Requires ALL permissions: 

* languageUnderstanding:minerIntent:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
miner_id = 'miner_id_example' # str | Miner ID
intent_id = 'intent_id_example' # str | The ID of the intent to be retrieved.
expand = 'expand_example' # str | Option to fetch utterances (optional)

try:
    # Get information about a mined intent
    api_response = api_instance.get_languageunderstanding_miner_intent(miner_id, intent_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_miner_intent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_id** | **str**| Miner ID |  |
| **intent_id** | **str**| The ID of the intent to be retrieved. |  |
| **expand** | **str**| Option to fetch utterances | [optional] <br />**Values**: phrases, utterances |

### Return type

[**MinerIntent**](MinerIntent)


## get_languageunderstanding_miner_intents

> [**MinedIntentsListing**](MinedIntentsListing) get_languageunderstanding_miner_intents(miner_id, expand=expand)


Retrieve a list of mined intents.

Wraps GET /api/v2/languageunderstanding/miners/{minerId}/intents 

Requires ALL permissions: 

* languageUnderstanding:minerIntent:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
miner_id = 'miner_id_example' # str | Miner ID
expand = 'expand_example' # str | Option to fetch utterances. (optional)

try:
    # Retrieve a list of mined intents.
    api_response = api_instance.get_languageunderstanding_miner_intents(miner_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_miner_intents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_id** | **str**| Miner ID |  |
| **expand** | **str**| Option to fetch utterances. | [optional] <br />**Values**: phrases, utterances |

### Return type

[**MinedIntentsListing**](MinedIntentsListing)


## get_languageunderstanding_miner_topic

> [**MinerTopic**](MinerTopic) get_languageunderstanding_miner_topic(miner_id, topic_id, expand=expand)


Retrieves details of a particular topic.

Wraps GET /api/v2/languageunderstanding/miners/{minerId}/topics/{topicId} 

Requires ALL permissions: 

* languageUnderstanding:miner:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
miner_id = 'miner_id_example' # str | Miner ID
topic_id = 'topic_id_example' # str | The ID of the topic to be retrieved.
expand = 'expand_example' # str | Option to fetch phrases (optional)

try:
    # Retrieves details of a particular topic.
    api_response = api_instance.get_languageunderstanding_miner_topic(miner_id, topic_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_miner_topic: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_id** | **str**| Miner ID |  |
| **topic_id** | **str**| The ID of the topic to be retrieved. |  |
| **expand** | **str**| Option to fetch phrases | [optional] <br />**Values**: phrases, utterances |

### Return type

[**MinerTopic**](MinerTopic)


## get_languageunderstanding_miner_topic_phrase

> [**MinerTopicPhrase**](MinerTopicPhrase) get_languageunderstanding_miner_topic_phrase(miner_id, topic_id, phrase_id)


Retrieves utterances related to a phrase in a topic.

Wraps GET /api/v2/languageunderstanding/miners/{minerId}/topics/{topicId}/phrases/{phraseId} 

Requires ALL permissions: 

* languageUnderstanding:miner:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
miner_id = 'miner_id_example' # str | Miner ID
topic_id = 'topic_id_example' # str | The ID of the topic to be retrieved.
phrase_id = 'phrase_id_example' # str | The ID of the phrase to be retrieved.

try:
    # Retrieves utterances related to a phrase in a topic.
    api_response = api_instance.get_languageunderstanding_miner_topic_phrase(miner_id, topic_id, phrase_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_miner_topic_phrase: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_id** | **str**| Miner ID |  |
| **topic_id** | **str**| The ID of the topic to be retrieved. |  |
| **phrase_id** | **str**| The ID of the phrase to be retrieved. |  |

### Return type

[**MinerTopicPhrase**](MinerTopicPhrase)


## get_languageunderstanding_miner_topics

> [**MinerTopicsListing**](MinerTopicsListing) get_languageunderstanding_miner_topics(miner_id)


Retrieve a list of mined topics.

Wraps GET /api/v2/languageunderstanding/miners/{minerId}/topics 

Requires ALL permissions: 

* languageUnderstanding:miner:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
miner_id = 'miner_id_example' # str | Miner ID

try:
    # Retrieve a list of mined topics.
    api_response = api_instance.get_languageunderstanding_miner_topics(miner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_miner_topics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_id** | **str**| Miner ID |  |

### Return type

[**MinerTopicsListing**](MinerTopicsListing)


## get_languageunderstanding_miners

> [**MinerListing**](MinerListing) get_languageunderstanding_miners(miner_type=miner_type)


Retrieve the list of miners created.

Wraps GET /api/v2/languageunderstanding/miners 

Requires ALL permissions: 

* languageUnderstanding:miner:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
miner_type = 'miner_type_example' # str | Type of miner, either intent or topic (optional)

try:
    # Retrieve the list of miners created.
    api_response = api_instance.get_languageunderstanding_miners(miner_type=miner_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_miners: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_type** | **str**| Type of miner, either intent or topic | [optional]  |

### Return type

[**MinerListing**](MinerListing)


## get_languageunderstanding_settings

> [**NluOrganization**](NluOrganization) get_languageunderstanding_settings()


Get Organization Configuration

Wraps GET /api/v2/languageunderstanding/settings 

Requires ANY permissions: 

* languageUnderstanding:settings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()

try:
    # Get Organization Configuration
    api_response = api_instance.get_languageunderstanding_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->get_languageunderstanding_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**NluOrganization**](NluOrganization)


## patch_languageunderstanding_domain

> [**NluDomain**](NluDomain) patch_languageunderstanding_domain(domain_id, body)


Update an NLU Domain.

Wraps PATCH /api/v2/languageunderstanding/domains/{domainId} 

Requires ANY permissions: 

* languageUnderstanding:nluDomain:edit
* dialog:bot:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.
body = PureCloudPlatformClientV2.NluDomain() # NluDomain | The updated NLU Domain.

try:
    # Update an NLU Domain.
    api_response = api_instance.patch_languageunderstanding_domain(domain_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->patch_languageunderstanding_domain: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **body** | [**NluDomain**](NluDomain)| The updated NLU Domain. |  |

### Return type

[**NluDomain**](NluDomain)


## patch_languageunderstanding_miner_draft

> [**Draft**](Draft) patch_languageunderstanding_miner_draft(miner_id, draft_id, body=body)


Save information for the draft. Either topic draft or intent draft should be sent.

Wraps PATCH /api/v2/languageunderstanding/miners/{minerId}/drafts/{draftId} 

Requires ALL permissions: 

* languageUnderstanding:draft:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
miner_id = 'miner_id_example' # str | Miner ID
draft_id = 'draft_id_example' # str | Draft ID
body = PureCloudPlatformClientV2.DraftRequest() # DraftRequest |  (optional)

try:
    # Save information for the draft. Either topic draft or intent draft should be sent.
    api_response = api_instance.patch_languageunderstanding_miner_draft(miner_id, draft_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->patch_languageunderstanding_miner_draft: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_id** | **str**| Miner ID |  |
| **draft_id** | **str**| Draft ID |  |
| **body** | [**DraftRequest**](DraftRequest)|  | [optional]  |

### Return type

[**Draft**](Draft)


## post_languageunderstanding_domain_feedback

> [**NluFeedbackResponse**](NluFeedbackResponse) post_languageunderstanding_domain_feedback(domain_id, body)


Create feedback for the NLU Domain Version.

Wraps POST /api/v2/languageunderstanding/domains/{domainId}/feedback 

Requires ANY permissions: 

* languageUnderstanding:feedback:add
* dialog:bot:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.
body = PureCloudPlatformClientV2.NluFeedbackRequest() # NluFeedbackRequest | The Feedback to create.

try:
    # Create feedback for the NLU Domain Version.
    api_response = api_instance.post_languageunderstanding_domain_feedback(domain_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->post_languageunderstanding_domain_feedback: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **body** | [**NluFeedbackRequest**](NluFeedbackRequest)| The Feedback to create. |  |

### Return type

[**NluFeedbackResponse**](NluFeedbackResponse)


## post_languageunderstanding_domain_version_detect

> [**NluDetectionResponse**](NluDetectionResponse) post_languageunderstanding_domain_version_detect(domain_id, domain_version_id, body)


Detect intent, entities, etc. in the submitted text using the specified NLU domain version.

Wraps POST /api/v2/languageunderstanding/domains/{domainId}/versions/{domainVersionId}/detect 

Requires ANY permissions: 

* languageUnderstanding:nluDomainVersion:view
* dialog:botVersion:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.
domain_version_id = 'domain_version_id_example' # str | ID of the NLU domain version.
body = PureCloudPlatformClientV2.NluDetectionRequest() # NluDetectionRequest | The input data to perform detection on.

try:
    # Detect intent, entities, etc. in the submitted text using the specified NLU domain version.
    api_response = api_instance.post_languageunderstanding_domain_version_detect(domain_id, domain_version_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->post_languageunderstanding_domain_version_detect: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **domain_version_id** | **str**| ID of the NLU domain version. |  |
| **body** | [**NluDetectionRequest**](NluDetectionRequest)| The input data to perform detection on. |  |

### Return type

[**NluDetectionResponse**](NluDetectionResponse)


## post_languageunderstanding_domain_version_publish

> [**NluDomainVersion**](NluDomainVersion) post_languageunderstanding_domain_version_publish(domain_id, domain_version_id)


Publish the draft NLU Domain Version.

Wraps POST /api/v2/languageunderstanding/domains/{domainId}/versions/{domainVersionId}/publish 

Requires ANY permissions: 

* languageUnderstanding:nluDomainVersion:add
* dialog:botVersion:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.
domain_version_id = 'domain_version_id_example' # str | ID of the NLU domain version.

try:
    # Publish the draft NLU Domain Version.
    api_response = api_instance.post_languageunderstanding_domain_version_publish(domain_id, domain_version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->post_languageunderstanding_domain_version_publish: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **domain_version_id** | **str**| ID of the NLU domain version. |  |

### Return type

[**NluDomainVersion**](NluDomainVersion)


## post_languageunderstanding_domain_version_train

> [**NluDomainVersionTrainingResponse**](NluDomainVersionTrainingResponse) post_languageunderstanding_domain_version_train(domain_id, domain_version_id)


Train the draft NLU Domain Version.

Wraps POST /api/v2/languageunderstanding/domains/{domainId}/versions/{domainVersionId}/train 

Requires ANY permissions: 

* languageUnderstanding:nluDomainVersion:edit
* dialog:botVersion:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.
domain_version_id = 'domain_version_id_example' # str | ID of the NLU domain version.

try:
    # Train the draft NLU Domain Version.
    api_response = api_instance.post_languageunderstanding_domain_version_train(domain_id, domain_version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->post_languageunderstanding_domain_version_train: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **domain_version_id** | **str**| ID of the NLU domain version. |  |

### Return type

[**NluDomainVersionTrainingResponse**](NluDomainVersionTrainingResponse)


## post_languageunderstanding_domain_versions

> [**NluDomainVersion**](NluDomainVersion) post_languageunderstanding_domain_versions(domain_id, body, include_utterances=include_utterances)


Create an NLU Domain Version.

Wraps POST /api/v2/languageunderstanding/domains/{domainId}/versions 

Requires ANY permissions: 

* languageUnderstanding:nluDomainVersion:add
* dialog:botVersion:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.
body = PureCloudPlatformClientV2.NluDomainVersion() # NluDomainVersion | The NLU Domain Version to create.
include_utterances = True # bool | Whether utterances for intent definition should be included when marshalling response. (optional)

try:
    # Create an NLU Domain Version.
    api_response = api_instance.post_languageunderstanding_domain_versions(domain_id, body, include_utterances=include_utterances)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->post_languageunderstanding_domain_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **body** | [**NluDomainVersion**](NluDomainVersion)| The NLU Domain Version to create. |  |
| **include_utterances** | **bool**| Whether utterances for intent definition should be included when marshalling response. | [optional]  |

### Return type

[**NluDomainVersion**](NluDomainVersion)


## post_languageunderstanding_domains

> [**NluDomain**](NluDomain) post_languageunderstanding_domains(body)


Create an NLU Domain.

Wraps POST /api/v2/languageunderstanding/domains 

Requires ANY permissions: 

* languageUnderstanding:nluDomain:add
* dialog:bot:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
body = PureCloudPlatformClientV2.NluDomain() # NluDomain | The NLU Domain to create.

try:
    # Create an NLU Domain.
    api_response = api_instance.post_languageunderstanding_domains(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->post_languageunderstanding_domains: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**NluDomain**](NluDomain)| The NLU Domain to create. |  |

### Return type

[**NluDomain**](NluDomain)


## post_languageunderstanding_miner_drafts

> [**Draft**](Draft) post_languageunderstanding_miner_drafts(miner_id, body)


Create a new draft resource.

Wraps POST /api/v2/languageunderstanding/miners/{minerId}/drafts 

Requires ALL permissions: 

* languageUnderstanding:draft:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
miner_id = 'miner_id_example' # str | Miner ID
body = PureCloudPlatformClientV2.Draft() # Draft | Details for creating draft resource

try:
    # Create a new draft resource.
    api_response = api_instance.post_languageunderstanding_miner_drafts(miner_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->post_languageunderstanding_miner_drafts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_id** | **str**| Miner ID |  |
| **body** | [**Draft**](Draft)| Details for creating draft resource |  |

### Return type

[**Draft**](Draft)


## post_languageunderstanding_miner_execute

> [**Miner**](Miner) post_languageunderstanding_miner_execute(miner_id, body=body)


Start the mining process. Specify date range pair with mediaType, queueIds, participantType for mining data from Genesys Cloud. Specify only uploadKey for mining through an external file.

Wraps POST /api/v2/languageunderstanding/miners/{minerId}/execute 

Requires ALL permissions: 

* languageUnderstanding:miner:execute

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
miner_id = 'miner_id_example' # str | Miner ID
body = PureCloudPlatformClientV2.MinerExecuteRequest() # MinerExecuteRequest |  (optional)

try:
    # Start the mining process. Specify date range pair with mediaType, queueIds, participantType for mining data from Genesys Cloud. Specify only uploadKey for mining through an external file.
    api_response = api_instance.post_languageunderstanding_miner_execute(miner_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->post_languageunderstanding_miner_execute: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **miner_id** | **str**| Miner ID |  |
| **body** | [**MinerExecuteRequest**](MinerExecuteRequest)|  | [optional]  |

### Return type

[**Miner**](Miner)


## post_languageunderstanding_miners

> [**Miner**](Miner) post_languageunderstanding_miners(body)


Create a unique miner.

Wraps POST /api/v2/languageunderstanding/miners 

Requires ALL permissions: 

* languageUnderstanding:miner:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
body = PureCloudPlatformClientV2.Miner() # Miner | Details for creating a new miner resource.

try:
    # Create a unique miner.
    api_response = api_instance.post_languageunderstanding_miners(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->post_languageunderstanding_miners: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Miner**](Miner)| Details for creating a new miner resource. |  |

### Return type

[**Miner**](Miner)


## put_languageunderstanding_domain_version

> [**NluDomainVersion**](NluDomainVersion) put_languageunderstanding_domain_version(domain_id, domain_version_id, body)


Update an NLU Domain Version.

Wraps PUT /api/v2/languageunderstanding/domains/{domainId}/versions/{domainVersionId} 

Requires ANY permissions: 

* languageUnderstanding:nluDomainVersion:edit
* dialog:botVersion:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguageUnderstandingApi()
domain_id = 'domain_id_example' # str | ID of the NLU domain.
domain_version_id = 'domain_version_id_example' # str | ID of the NLU domain version.
body = PureCloudPlatformClientV2.NluDomainVersion() # NluDomainVersion | The updated NLU Domain Version.

try:
    # Update an NLU Domain Version.
    api_response = api_instance.put_languageunderstanding_domain_version(domain_id, domain_version_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->put_languageunderstanding_domain_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **domain_version_id** | **str**| ID of the NLU domain version. |  |
| **body** | [**NluDomainVersion**](NluDomainVersion)| The updated NLU Domain Version. |  |

### Return type

[**NluDomainVersion**](NluDomainVersion)


_PureCloudPlatformClientV2 231.0.0_

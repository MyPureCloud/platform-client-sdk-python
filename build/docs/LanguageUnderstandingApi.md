---
title: LanguageUnderstandingApi
---

## PureCloudPlatformClientV2.LanguageUnderstandingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_languageunderstanding_domain**](LanguageUnderstandingApi.html#delete_languageunderstanding_domain) | Delete an NLU Domain.|
|[**delete_languageunderstanding_domain_feedback_feedback_id**](LanguageUnderstandingApi.html#delete_languageunderstanding_domain_feedback_feedback_id) | Delete the feedback on the NLU Domain Version.|
|[**delete_languageunderstanding_domain_version**](LanguageUnderstandingApi.html#delete_languageunderstanding_domain_version) | Delete an NLU Domain Version|
|[**get_languageunderstanding_domain**](LanguageUnderstandingApi.html#get_languageunderstanding_domain) | Find an NLU Domain.|
|[**get_languageunderstanding_domain_feedback**](LanguageUnderstandingApi.html#get_languageunderstanding_domain_feedback) | Get all feedback in the given NLU Domain Version.|
|[**get_languageunderstanding_domain_feedback_feedback_id**](LanguageUnderstandingApi.html#get_languageunderstanding_domain_feedback_feedback_id) | Find a Feedback|
|[**get_languageunderstanding_domain_version**](LanguageUnderstandingApi.html#get_languageunderstanding_domain_version) | Find an NLU Domain Version.|
|[**get_languageunderstanding_domain_version_report**](LanguageUnderstandingApi.html#get_languageunderstanding_domain_version_report) | Retrieved quality report for the specified NLU Domain Version|
|[**get_languageunderstanding_domain_versions**](LanguageUnderstandingApi.html#get_languageunderstanding_domain_versions) | Get all NLU Domain Versions for a given Domain.|
|[**get_languageunderstanding_domains**](LanguageUnderstandingApi.html#get_languageunderstanding_domains) | Get all NLU Domains.|
|[**patch_languageunderstanding_domain**](LanguageUnderstandingApi.html#patch_languageunderstanding_domain) | Update an NLU Domain.|
|[**post_languageunderstanding_domain_feedback**](LanguageUnderstandingApi.html#post_languageunderstanding_domain_feedback) | Create feedback for the NLU Domain Version.|
|[**post_languageunderstanding_domain_version_detect**](LanguageUnderstandingApi.html#post_languageunderstanding_domain_version_detect) | Detect intent, entities, etc. in the submitted text using the specified NLU domain version.|
|[**post_languageunderstanding_domain_version_publish**](LanguageUnderstandingApi.html#post_languageunderstanding_domain_version_publish) | Publish the draft NLU Domain Version.|
|[**post_languageunderstanding_domain_version_train**](LanguageUnderstandingApi.html#post_languageunderstanding_domain_version_train) | Train the draft NLU Domain Version.|
|[**post_languageunderstanding_domain_versions**](LanguageUnderstandingApi.html#post_languageunderstanding_domain_versions) | Create an NLU Domain Version.|
|[**post_languageunderstanding_domains**](LanguageUnderstandingApi.html#post_languageunderstanding_domains) | Create an NLU Domain.|
|[**put_languageunderstanding_domain_version**](LanguageUnderstandingApi.html#put_languageunderstanding_domain_version) | Update an NLU Domain Version.|
{: class="table table-striped"}

<a name="delete_languageunderstanding_domain"></a>

##  delete_languageunderstanding_domain(domain_id)



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
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_languageunderstanding_domain_feedback_feedback_id"></a>

##  delete_languageunderstanding_domain_feedback_feedback_id(domain_id, feedback_id)



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
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_languageunderstanding_domain_version"></a>

##  delete_languageunderstanding_domain_version(domain_id, domain_version_id)



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
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_languageunderstanding_domain"></a>

## [**NluDomain**](NluDomain.html) get_languageunderstanding_domain(domain_id)



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
{: class="table table-striped"}

### Return type

[**NluDomain**](NluDomain.html)

<a name="get_languageunderstanding_domain_feedback"></a>

## [**NluFeedbackListing**](NluFeedbackListing.html) get_languageunderstanding_domain_feedback(domain_id, intent_name=intent_name, assessment=assessment, date_start=date_start, date_end=date_end, include_deleted=include_deleted, page_number=page_number, page_size=page_size, enable_cursor_pagination=enable_cursor_pagination, after=after, fields=fields)



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
include_deleted = true # bool | Whether to include soft-deleted items in the result. (optional)
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
enable_cursor_pagination = false # bool | Enable Cursor Pagination (optional) (default to false)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. This is considered only when enableCursorPagination=true (optional)
fields = ['fields_example'] # list[str] | Fields and properties to get, comma-separated (optional)

try:
    # Get all feedback in the given NLU Domain Version.
    api_response = api_instance.get_languageunderstanding_domain_feedback(domain_id, intent_name=intent_name, assessment=assessment, date_start=date_start, date_end=date_end, include_deleted=include_deleted, page_number=page_number, page_size=page_size, enable_cursor_pagination=enable_cursor_pagination, after=after, fields=fields)
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
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **enable_cursor_pagination** | **bool**| Enable Cursor Pagination | [optional] [default to false] |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. This is considered only when enableCursorPagination=true | [optional]  |
| **fields** | [**list[str]**](str.html)| Fields and properties to get, comma-separated | [optional] <br />**Values**: version, dateCreated, text, intents |
{: class="table table-striped"}

### Return type

[**NluFeedbackListing**](NluFeedbackListing.html)

<a name="get_languageunderstanding_domain_feedback_feedback_id"></a>

## [**NluFeedbackResponse**](NluFeedbackResponse.html) get_languageunderstanding_domain_feedback_feedback_id(domain_id, feedback_id, fields=fields)



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
| **fields** | [**list[str]**](str.html)| Fields and properties to get, comma-separated | [optional] <br />**Values**: version, dateCreated, text, intents |
{: class="table table-striped"}

### Return type

[**NluFeedbackResponse**](NluFeedbackResponse.html)

<a name="get_languageunderstanding_domain_version"></a>

## [**NluDomainVersion**](NluDomainVersion.html) get_languageunderstanding_domain_version(domain_id, domain_version_id, include_utterances=include_utterances)



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
include_utterances = true # bool | Whether utterances for intent definition should be included when marshalling response. (optional)

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
{: class="table table-striped"}

### Return type

[**NluDomainVersion**](NluDomainVersion.html)

<a name="get_languageunderstanding_domain_version_report"></a>

## [**NluDomainVersionQualityReport**](NluDomainVersionQualityReport.html) get_languageunderstanding_domain_version_report(domain_id, domain_version_id)



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
{: class="table table-striped"}

### Return type

[**NluDomainVersionQualityReport**](NluDomainVersionQualityReport.html)

<a name="get_languageunderstanding_domain_versions"></a>

## [**NluDomainVersionListing**](NluDomainVersionListing.html) get_languageunderstanding_domain_versions(domain_id, include_utterances=include_utterances, page_number=page_number, page_size=page_size)



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
include_utterances = true # bool | Whether utterances for intent definition should be included when marshalling response. (optional)
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
{: class="table table-striped"}

### Return type

[**NluDomainVersionListing**](NluDomainVersionListing.html)

<a name="get_languageunderstanding_domains"></a>

## [**NluDomainListing**](NluDomainListing.html) get_languageunderstanding_domains(page_number=page_number, page_size=page_size)



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
{: class="table table-striped"}

### Return type

[**NluDomainListing**](NluDomainListing.html)

<a name="patch_languageunderstanding_domain"></a>

## [**NluDomain**](NluDomain.html) patch_languageunderstanding_domain(domain_id, body)



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
| **body** | [**NluDomain**](NluDomain.html)| The updated NLU Domain. |  |
{: class="table table-striped"}

### Return type

[**NluDomain**](NluDomain.html)

<a name="post_languageunderstanding_domain_feedback"></a>

## [**NluFeedbackResponse**](NluFeedbackResponse.html) post_languageunderstanding_domain_feedback(domain_id, body)



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
| **body** | [**NluFeedbackRequest**](NluFeedbackRequest.html)| The Feedback to create. |  |
{: class="table table-striped"}

### Return type

[**NluFeedbackResponse**](NluFeedbackResponse.html)

<a name="post_languageunderstanding_domain_version_detect"></a>

## [**NluDetectionResponse**](NluDetectionResponse.html) post_languageunderstanding_domain_version_detect(domain_id, domain_version_id, body)



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
| **body** | [**NluDetectionRequest**](NluDetectionRequest.html)| The input data to perform detection on. |  |
{: class="table table-striped"}

### Return type

[**NluDetectionResponse**](NluDetectionResponse.html)

<a name="post_languageunderstanding_domain_version_publish"></a>

## [**NluDomainVersion**](NluDomainVersion.html) post_languageunderstanding_domain_version_publish(domain_id, domain_version_id)



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
{: class="table table-striped"}

### Return type

[**NluDomainVersion**](NluDomainVersion.html)

<a name="post_languageunderstanding_domain_version_train"></a>

## [**NluDomainVersionTrainingResponse**](NluDomainVersionTrainingResponse.html) post_languageunderstanding_domain_version_train(domain_id, domain_version_id)



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
{: class="table table-striped"}

### Return type

[**NluDomainVersionTrainingResponse**](NluDomainVersionTrainingResponse.html)

<a name="post_languageunderstanding_domain_versions"></a>

## [**NluDomainVersion**](NluDomainVersion.html) post_languageunderstanding_domain_versions(domain_id, body)



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

try:
    # Create an NLU Domain Version.
    api_response = api_instance.post_languageunderstanding_domain_versions(domain_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageUnderstandingApi->post_languageunderstanding_domain_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **domain_id** | **str**| ID of the NLU domain. |  |
| **body** | [**NluDomainVersion**](NluDomainVersion.html)| The NLU Domain Version to create. |  |
{: class="table table-striped"}

### Return type

[**NluDomainVersion**](NluDomainVersion.html)

<a name="post_languageunderstanding_domains"></a>

## [**NluDomain**](NluDomain.html) post_languageunderstanding_domains(body)



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
| **body** | [**NluDomain**](NluDomain.html)| The NLU Domain to create. |  |
{: class="table table-striped"}

### Return type

[**NluDomain**](NluDomain.html)

<a name="put_languageunderstanding_domain_version"></a>

## [**NluDomainVersion**](NluDomainVersion.html) put_languageunderstanding_domain_version(domain_id, domain_version_id, body)



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
| **body** | [**NluDomainVersion**](NluDomainVersion.html)| The updated NLU Domain Version. |  |
{: class="table table-striped"}

### Return type

[**NluDomainVersion**](NluDomainVersion.html)


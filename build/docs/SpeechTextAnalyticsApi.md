# SpeechTextAnalyticsApi

## PureCloudPlatformClientV2.SpeechTextAnalyticsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_speechandtextanalytics_category**](#delete_speechandtextanalytics_category) | Delete a Speech &amp; Text Analytics category by ID|
|[**delete_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id**](#delete_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id) | Delete a Speech &amp; Text Analytics DictionaryFeedback by Id|
|[**delete_speechandtextanalytics_program**](#delete_speechandtextanalytics_program) | Delete a Speech &amp; Text Analytics program by id|
|[**delete_speechandtextanalytics_reprocessing_job**](#delete_speechandtextanalytics_reprocessing_job) | Delete a Speech &amp; Text Analytics Reprocessing job by Id|
|[**delete_speechandtextanalytics_sentimentfeedback**](#delete_speechandtextanalytics_sentimentfeedback) | Delete All Speech &amp; Text Analytics SentimentFeedback|
|[**delete_speechandtextanalytics_sentimentfeedback_sentiment_feedback_id**](#delete_speechandtextanalytics_sentimentfeedback_sentiment_feedback_id) | Delete a Speech &amp; Text Analytics SentimentFeedback by Id|
|[**delete_speechandtextanalytics_topic**](#delete_speechandtextanalytics_topic) | Delete a Speech &amp; Text Analytics topic by id|
|[**get_speechandtextanalytics_categories**](#get_speechandtextanalytics_categories) | Get the list of Speech and Text Analytics categories|
|[**get_speechandtextanalytics_category**](#get_speechandtextanalytics_category) | Get a Speech &amp; Text Analytics Category by ID|
|[**get_speechandtextanalytics_conversation**](#get_speechandtextanalytics_conversation) | Get Speech and Text Analytics for a specific conversation|
|[**get_speechandtextanalytics_conversation_categories**](#get_speechandtextanalytics_conversation_categories) | Get the list of detected Speech and Text Analytics categories of conversation|
|[**get_speechandtextanalytics_conversation_communication_transcripturl**](#get_speechandtextanalytics_conversation_communication_transcripturl) | Get the pre-signed S3 URL for the transcript of a specific communication of a conversation|
|[**get_speechandtextanalytics_conversation_communication_transcripturls**](#get_speechandtextanalytics_conversation_communication_transcripturls) | Get the list of pre-signed S3 URL for the transcripts of a specific communication of a conversation|
|[**get_speechandtextanalytics_conversation_sentiments**](#get_speechandtextanalytics_conversation_sentiments) | Get sentiment data|
|[**get_speechandtextanalytics_conversation_summaries**](#get_speechandtextanalytics_conversation_summaries) | Get conversation summaries by conversation id.|
|[**get_speechandtextanalytics_dictionaryfeedback**](#get_speechandtextanalytics_dictionaryfeedback) | Get the list of Speech &amp; Text Analytics dictionary feedbacks|
|[**get_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id**](#get_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id) | Get a Speech &amp; Text Analytics dictionary feedback by id|
|[**get_speechandtextanalytics_program**](#get_speechandtextanalytics_program) | Get a Speech &amp; Text Analytics program by id|
|[**get_speechandtextanalytics_program_mappings**](#get_speechandtextanalytics_program_mappings) | Get Speech &amp; Text Analytics program mappings to queues and flows by id|
|[**get_speechandtextanalytics_program_settings_insights**](#get_speechandtextanalytics_program_settings_insights) | Get AI Insights settings of a program|
|[**get_speechandtextanalytics_program_transcriptionengines**](#get_speechandtextanalytics_program_transcriptionengines) | Get transcription engine settings of a program|
|[**get_speechandtextanalytics_programs**](#get_speechandtextanalytics_programs) | Get the list of Speech &amp; Text Analytics programs|
|[**get_speechandtextanalytics_programs_general_job**](#get_speechandtextanalytics_programs_general_job) | Get a Speech &amp; Text Analytics general program job by id|
|[**get_speechandtextanalytics_programs_mappings**](#get_speechandtextanalytics_programs_mappings) | Get the list of Speech &amp; Text Analytics programs mappings to queues and flows|
|[**get_speechandtextanalytics_programs_publishjob**](#get_speechandtextanalytics_programs_publishjob) | Get a Speech &amp; Text Analytics publish programs job by id|
|[**get_speechandtextanalytics_programs_settings_insights**](#get_speechandtextanalytics_programs_settings_insights) | Get the list of program AI Insights settings for the organization|
|[**get_speechandtextanalytics_programs_transcriptionengines_dialects**](#get_speechandtextanalytics_programs_transcriptionengines_dialects) | Get supported dialects for each transcription engine|
|[**get_speechandtextanalytics_programs_unpublished**](#get_speechandtextanalytics_programs_unpublished) | Get the list of Speech &amp; Text Analytics unpublished programs|
|[**get_speechandtextanalytics_reprocessing_job**](#get_speechandtextanalytics_reprocessing_job) | Get a Speech &amp; Text Analytics reprocess job by id|
|[**get_speechandtextanalytics_reprocessing_job_interactions**](#get_speechandtextanalytics_reprocessing_job_interactions) | Get a Speech &amp; Text Analytics Reprocessing interactions statuses by job id|
|[**get_speechandtextanalytics_reprocessing_jobs**](#get_speechandtextanalytics_reprocessing_jobs) | Get the list of Speech &amp; Text Analytics reprocess jobs|
|[**get_speechandtextanalytics_sentiment_dialects**](#get_speechandtextanalytics_sentiment_dialects) | Get the list of Speech &amp; Text Analytics sentiment supported dialects|
|[**get_speechandtextanalytics_sentimentfeedback**](#get_speechandtextanalytics_sentimentfeedback) | Get the list of Speech &amp; Text Analytics SentimentFeedback|
|[**get_speechandtextanalytics_settings**](#get_speechandtextanalytics_settings) | Get Speech And Text Analytics Settings|
|[**get_speechandtextanalytics_topic**](#get_speechandtextanalytics_topic) | Get a Speech &amp; Text Analytics topic by id|
|[**get_speechandtextanalytics_topics**](#get_speechandtextanalytics_topics) | Get the list of Speech &amp; Text Analytics topics|
|[**get_speechandtextanalytics_topics_dialects**](#get_speechandtextanalytics_topics_dialects) | Get list of supported Speech &amp; Text Analytics topics dialects|
|[**get_speechandtextanalytics_topics_general**](#get_speechandtextanalytics_topics_general) | Get the Speech &amp; Text Analytics general topics for a given dialect|
|[**get_speechandtextanalytics_topics_general_status**](#get_speechandtextanalytics_topics_general_status) | Get the list of general topics from the org and the system with their current status|
|[**get_speechandtextanalytics_topics_publishjob**](#get_speechandtextanalytics_topics_publishjob) | Get a Speech &amp; Text Analytics publish topics job by id|
|[**get_speechandtextanalytics_topics_testphrase_job**](#get_speechandtextanalytics_topics_testphrase_job) | Get a Speech &amp; Text Analytics test topics phrase job by id|
|[**get_speechandtextanalytics_translations_language_conversation**](#get_speechandtextanalytics_translations_language_conversation) | Translate a single interaction recording (or an email conversation)|
|[**get_speechandtextanalytics_translations_languages**](#get_speechandtextanalytics_translations_languages) | Get supported translation languages|
|[**patch_speechandtextanalytics_settings**](#patch_speechandtextanalytics_settings) | Patch Speech And Text Analytics Settings|
|[**post_speechandtextanalytics_categories**](#post_speechandtextanalytics_categories) | Create new Speech &amp; Text Analytics category|
|[**post_speechandtextanalytics_dictionaryfeedback**](#post_speechandtextanalytics_dictionaryfeedback) | Create a Speech &amp; Text Analytics DictionaryFeedback|
|[**post_speechandtextanalytics_programs**](#post_speechandtextanalytics_programs) | Create new Speech &amp; Text Analytics program|
|[**post_speechandtextanalytics_programs_general_jobs**](#post_speechandtextanalytics_programs_general_jobs) | Create new Speech &amp; Text Analytics general program job|
|[**post_speechandtextanalytics_programs_publishjobs**](#post_speechandtextanalytics_programs_publishjobs) | Create new Speech &amp; Text Analytics publish programs job|
|[**post_speechandtextanalytics_reprocessing_jobs**](#post_speechandtextanalytics_reprocessing_jobs) | Create a Speech &amp; Text Analytics reprocess job.|
|[**post_speechandtextanalytics_sentimentfeedback**](#post_speechandtextanalytics_sentimentfeedback) | Create a Speech &amp; Text Analytics SentimentFeedback|
|[**post_speechandtextanalytics_topics**](#post_speechandtextanalytics_topics) | Create new Speech &amp; Text Analytics topic|
|[**post_speechandtextanalytics_topics_publishjobs**](#post_speechandtextanalytics_topics_publishjobs) | Create new Speech &amp; Text Analytics publish topics job|
|[**post_speechandtextanalytics_topics_testphrase_jobs**](#post_speechandtextanalytics_topics_testphrase_jobs) | Create new Speech &amp; Text Analytics publish topics job|
|[**post_speechandtextanalytics_transcripts_search**](#post_speechandtextanalytics_transcripts_search) | Search resources.|
|[**put_speechandtextanalytics_category**](#put_speechandtextanalytics_category) | Update a Speech &amp; Text Analytics category by ID|
|[**put_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id**](#put_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id) | Update existing Speech &amp; Text Analytics dictionary feedback by id|
|[**put_speechandtextanalytics_program**](#put_speechandtextanalytics_program) | Update existing Speech &amp; Text Analytics program|
|[**put_speechandtextanalytics_program_mappings**](#put_speechandtextanalytics_program_mappings) | Set Speech &amp; Text Analytics program mappings to queues and flows|
|[**put_speechandtextanalytics_program_settings_insights**](#put_speechandtextanalytics_program_settings_insights) | Update AI Insights settings of a program|
|[**put_speechandtextanalytics_program_transcriptionengines**](#put_speechandtextanalytics_program_transcriptionengines) | Update transcription engine settings of a program|
|[**put_speechandtextanalytics_settings**](#put_speechandtextanalytics_settings) | Update Speech And Text Analytics Settings|
|[**put_speechandtextanalytics_topic**](#put_speechandtextanalytics_topic) | Update existing Speech &amp; Text Analytics topic|



## delete_speechandtextanalytics_category

>  delete_speechandtextanalytics_category(category_id)


Delete a Speech & Text Analytics category by ID

Wraps DELETE /api/v2/speechandtextanalytics/categories/{categoryId} 

Requires ALL permissions: 

* speechAndTextAnalytics:category:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
category_id = 'category_id_example' # str | The id of the category

try:
    # Delete a Speech & Text Analytics category by ID
    api_instance.delete_speechandtextanalytics_category(category_id)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->delete_speechandtextanalytics_category: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **category_id** | **str**| The id of the category |  |

### Return type

void (empty response body)


## delete_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id

>  delete_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id(dictionary_feedback_id)


Delete a Speech & Text Analytics DictionaryFeedback by Id

Wraps DELETE /api/v2/speechandtextanalytics/dictionaryfeedback/{dictionaryFeedbackId} 

Requires ALL permissions: 

* speechAndTextAnalytics:dictionaryterm:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
dictionary_feedback_id = 'dictionary_feedback_id_example' # str | The Id of the Dictionary Feedback

try:
    # Delete a Speech & Text Analytics DictionaryFeedback by Id
    api_instance.delete_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id(dictionary_feedback_id)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->delete_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dictionary_feedback_id** | **str**| The Id of the Dictionary Feedback |  |

### Return type

void (empty response body)


## delete_speechandtextanalytics_program

> [**DeleteProgramResponse**](DeleteProgramResponse) delete_speechandtextanalytics_program(program_id, force_delete=force_delete)


Delete a Speech & Text Analytics program by id

Wraps DELETE /api/v2/speechandtextanalytics/programs/{programId} 

Requires ALL permissions: 

* speechAndTextAnalytics:program:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
program_id = 'program_id_example' # str | The id of the program
force_delete = False # bool | Indicates whether the program is forced to be deleted or not. Required when the program to delete is the default program. (optional) (default to False)

try:
    # Delete a Speech & Text Analytics program by id
    api_response = api_instance.delete_speechandtextanalytics_program(program_id, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->delete_speechandtextanalytics_program: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **program_id** | **str**| The id of the program |  |
| **force_delete** | **bool**| Indicates whether the program is forced to be deleted or not. Required when the program to delete is the default program. | [optional] [default to False]<br />**Values**: true, false |

### Return type

[**DeleteProgramResponse**](DeleteProgramResponse)


## delete_speechandtextanalytics_reprocessing_job

>  delete_speechandtextanalytics_reprocessing_job(job_id)


Delete a Speech & Text Analytics Reprocessing job by Id

delete_speechandtextanalytics_reprocessing_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/speechandtextanalytics/reprocessing/jobs/{jobId} 

Requires ALL permissions: 

* speechAndTextAnalytics:reprocessInteractions:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
job_id = 'job_id_example' # str | The Id of the Reprocessing job

try:
    # Delete a Speech & Text Analytics Reprocessing job by Id
    api_instance.delete_speechandtextanalytics_reprocessing_job(job_id)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->delete_speechandtextanalytics_reprocessing_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The Id of the Reprocessing job |  |

### Return type

void (empty response body)


## delete_speechandtextanalytics_sentimentfeedback

>  delete_speechandtextanalytics_sentimentfeedback()


Delete All Speech & Text Analytics SentimentFeedback

Wraps DELETE /api/v2/speechandtextanalytics/sentimentfeedback 

Requires ALL permissions: 

* speechAndTextAnalytics:feedback:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()

try:
    # Delete All Speech & Text Analytics SentimentFeedback
    api_instance.delete_speechandtextanalytics_sentimentfeedback()
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->delete_speechandtextanalytics_sentimentfeedback: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

void (empty response body)


## delete_speechandtextanalytics_sentimentfeedback_sentiment_feedback_id

>  delete_speechandtextanalytics_sentimentfeedback_sentiment_feedback_id(sentiment_feedback_id)


Delete a Speech & Text Analytics SentimentFeedback by Id

Wraps DELETE /api/v2/speechandtextanalytics/sentimentfeedback/{sentimentFeedbackId} 

Requires ALL permissions: 

* speechAndTextAnalytics:feedback:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
sentiment_feedback_id = 'sentiment_feedback_id_example' # str | The Id of the SentimentFeedback

try:
    # Delete a Speech & Text Analytics SentimentFeedback by Id
    api_instance.delete_speechandtextanalytics_sentimentfeedback_sentiment_feedback_id(sentiment_feedback_id)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->delete_speechandtextanalytics_sentimentfeedback_sentiment_feedback_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sentiment_feedback_id** | **str**| The Id of the SentimentFeedback |  |

### Return type

void (empty response body)


## delete_speechandtextanalytics_topic

>  delete_speechandtextanalytics_topic(topic_id)


Delete a Speech & Text Analytics topic by id

Wraps DELETE /api/v2/speechandtextanalytics/topics/{topicId} 

Requires ALL permissions: 

* speechAndTextAnalytics:topic:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
topic_id = 'topic_id_example' # str | The id of the topic

try:
    # Delete a Speech & Text Analytics topic by id
    api_instance.delete_speechandtextanalytics_topic(topic_id)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->delete_speechandtextanalytics_topic: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| The id of the topic |  |

### Return type

void (empty response body)


## get_speechandtextanalytics_categories

> [**CategoriesEntityListing**](CategoriesEntityListing) get_speechandtextanalytics_categories(page_size=page_size, page_number=page_number, name=name, sort_order=sort_order, sort_by=sort_by, ids=ids)


Get the list of Speech and Text Analytics categories

Wraps GET /api/v2/speechandtextanalytics/categories 

Requires ALL permissions: 

* speechAndTextAnalytics:category:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
page_size = 25 # int | The page size for the listing. The max that will be returned is 25. (optional) (default to 25)
page_number = 1 # int | The page number for the listing (optional) (default to 1)
name = 'name_example' # str | The category name filter applied to the listing (optional)
sort_order = ''asc'' # str | The sort order for the listing (optional) (default to 'asc')
sort_by = ''name'' # str | The field to sort by for the listing (optional) (default to 'name')
ids = ['ids_example'] # list[str] | Comma separated Category IDs to filter by. Cannot be used with other filters. Maximum of 25 IDs allowed. (optional)

try:
    # Get the list of Speech and Text Analytics categories
    api_response = api_instance.get_speechandtextanalytics_categories(page_size=page_size, page_number=page_number, name=name, sort_order=sort_order, sort_by=sort_by, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_categories: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The page size for the listing. The max that will be returned is 25. | [optional] [default to 25] |
| **page_number** | **int**| The page number for the listing | [optional] [default to 1] |
| **name** | **str**| The category name filter applied to the listing | [optional]  |
| **sort_order** | **str**| The sort order for the listing | [optional] [default to &#39;asc&#39;]<br />**Values**: asc, desc |
| **sort_by** | **str**| The field to sort by for the listing | [optional] [default to &#39;name&#39;]<br />**Values**: name, description |
| **ids** | [**list[str]**](str)| Comma separated Category IDs to filter by. Cannot be used with other filters. Maximum of 25 IDs allowed. | [optional]  |

### Return type

[**CategoriesEntityListing**](CategoriesEntityListing)


## get_speechandtextanalytics_category

> [**StaCategory**](StaCategory) get_speechandtextanalytics_category(category_id)


Get a Speech & Text Analytics Category by ID

Wraps GET /api/v2/speechandtextanalytics/categories/{categoryId} 

Requires ALL permissions: 

* speechAndTextAnalytics:category:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
category_id = 'category_id_example' # str | The id of the category

try:
    # Get a Speech & Text Analytics Category by ID
    api_response = api_instance.get_speechandtextanalytics_category(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_category: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **category_id** | **str**| The id of the category |  |

### Return type

[**StaCategory**](StaCategory)


## get_speechandtextanalytics_conversation

> [**ConversationMetrics**](ConversationMetrics) get_speechandtextanalytics_conversation(conversation_id)


Get Speech and Text Analytics for a specific conversation

Wraps GET /api/v2/speechandtextanalytics/conversations/{conversationId} 

Requires ALL permissions: 

* recording:recording:view
* speechAndTextAnalytics:data:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
conversation_id = 'conversation_id_example' # str | Conversation Id

try:
    # Get Speech and Text Analytics for a specific conversation
    api_response = api_instance.get_speechandtextanalytics_conversation(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_conversation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation Id |  |

### Return type

[**ConversationMetrics**](ConversationMetrics)


## get_speechandtextanalytics_conversation_categories

> [**ConversationCategoriesEntityListing**](ConversationCategoriesEntityListing) get_speechandtextanalytics_conversation_categories(conversation_id, page_size=page_size, page_number=page_number)


Get the list of detected Speech and Text Analytics categories of conversation

Wraps GET /api/v2/speechandtextanalytics/conversations/{conversationId}/categories 

Requires ALL permissions: 

* speechAndTextAnalytics:data:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
conversation_id = 'conversation_id_example' # str | The id of the conversation
page_size = 25 # int | The page size for the listing. The max that will be returned is 50. (optional) (default to 25)
page_number = 1 # int | The page number for the listing (optional) (default to 1)

try:
    # Get the list of detected Speech and Text Analytics categories of conversation
    api_response = api_instance.get_speechandtextanalytics_conversation_categories(conversation_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_conversation_categories: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| The id of the conversation |  |
| **page_size** | **int**| The page size for the listing. The max that will be returned is 50. | [optional] [default to 25] |
| **page_number** | **int**| The page number for the listing | [optional] [default to 1] |

### Return type

[**ConversationCategoriesEntityListing**](ConversationCategoriesEntityListing)


## get_speechandtextanalytics_conversation_communication_transcripturl

> [**TranscriptUrl**](TranscriptUrl) get_speechandtextanalytics_conversation_communication_transcripturl(conversation_id, communication_id)


Get the pre-signed S3 URL for the transcript of a specific communication of a conversation

Wraps GET /api/v2/speechandtextanalytics/conversations/{conversationId}/communications/{communicationId}/transcripturl 

Requires ALL permissions: 

* recording:recording:view
* speechAndTextAnalytics:data:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
communication_id = 'communication_id_example' # str | Communication ID

try:
    # Get the pre-signed S3 URL for the transcript of a specific communication of a conversation
    api_response = api_instance.get_speechandtextanalytics_conversation_communication_transcripturl(conversation_id, communication_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_conversation_communication_transcripturl: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **communication_id** | **str**| Communication ID |  |

### Return type

[**TranscriptUrl**](TranscriptUrl)


## get_speechandtextanalytics_conversation_communication_transcripturls

> [**TranscriptUrls**](TranscriptUrls) get_speechandtextanalytics_conversation_communication_transcripturls(conversation_id, communication_id)


Get the list of pre-signed S3 URL for the transcripts of a specific communication of a conversation

Wraps GET /api/v2/speechandtextanalytics/conversations/{conversationId}/communications/{communicationId}/transcripturls 

Requires ANY permissions: 

* recording:recording:view
* recording:recordingSegment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
communication_id = 'communication_id_example' # str | Communication ID

try:
    # Get the list of pre-signed S3 URL for the transcripts of a specific communication of a conversation
    api_response = api_instance.get_speechandtextanalytics_conversation_communication_transcripturls(conversation_id, communication_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_conversation_communication_transcripturls: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **communication_id** | **str**| Communication ID |  |

### Return type

[**TranscriptUrls**](TranscriptUrls)


## get_speechandtextanalytics_conversation_sentiments

> [**SentimentData**](SentimentData) get_speechandtextanalytics_conversation_sentiments(conversation_id)


Get sentiment data

Wraps GET /api/v2/speechandtextanalytics/conversations/{conversationId}/sentiments 

Requires ALL permissions: 

* speechAndTextAnalytics:sentimentData:view
* speechAndTextAnalytics:data:view
* recording:recording:view
* recording:recording:viewSensitiveData

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
conversation_id = 'conversation_id_example' # str | The conversation ID of the sentiment data

try:
    # Get sentiment data
    api_response = api_instance.get_speechandtextanalytics_conversation_sentiments(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_conversation_sentiments: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| The conversation ID of the sentiment data |  |

### Return type

[**SentimentData**](SentimentData)


## get_speechandtextanalytics_conversation_summaries

> [**SpeechTextAnalyticsConversationSummaryListing**](SpeechTextAnalyticsConversationSummaryListing) get_speechandtextanalytics_conversation_summaries(conversation_id)


Get conversation summaries by conversation id.

Wraps GET /api/v2/speechandtextanalytics/conversations/{conversationId}/summaries 

Requires ALL permissions: 

* speechAndTextAnalytics:aiSummary:view
* recording:recording:view
* recording:recording:viewSensitiveData

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
conversation_id = 'conversation_id_example' # str | The conversation ID of the summaries

try:
    # Get conversation summaries by conversation id.
    api_response = api_instance.get_speechandtextanalytics_conversation_summaries(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_conversation_summaries: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| The conversation ID of the summaries |  |

### Return type

[**SpeechTextAnalyticsConversationSummaryListing**](SpeechTextAnalyticsConversationSummaryListing)


## get_speechandtextanalytics_dictionaryfeedback

> [**DictionaryFeedbackEntityListing**](DictionaryFeedbackEntityListing) get_speechandtextanalytics_dictionaryfeedback(dialect=dialect, next_page=next_page, page_size=page_size)


Get the list of Speech & Text Analytics dictionary feedbacks

Wraps GET /api/v2/speechandtextanalytics/dictionaryfeedback 

Requires ALL permissions: 

* speechAndTextAnalytics:dictionaryterm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
dialect = 'en-US' # str | The key for filter the listing by dialect, dialect format is {language}-{country} where language follows ISO 639-1 standard and country follows ISO 3166-1 alpha 2 standard (optional)
next_page = 'next_page_example' # str | The key for listing the next page (optional)
page_size = 500 # int | The page size for the listing (optional) (default to 500)

try:
    # Get the list of Speech & Text Analytics dictionary feedbacks
    api_response = api_instance.get_speechandtextanalytics_dictionaryfeedback(dialect=dialect, next_page=next_page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_dictionaryfeedback: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dialect** | **str**| The key for filter the listing by dialect, dialect format is {language}-{country} where language follows ISO 639-1 standard and country follows ISO 3166-1 alpha 2 standard | [optional]  |
| **next_page** | **str**| The key for listing the next page | [optional]  |
| **page_size** | **int**| The page size for the listing | [optional] [default to 500] |

### Return type

[**DictionaryFeedbackEntityListing**](DictionaryFeedbackEntityListing)


## get_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id

> [**DictionaryFeedback**](DictionaryFeedback) get_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id(dictionary_feedback_id)


Get a Speech & Text Analytics dictionary feedback by id

Wraps GET /api/v2/speechandtextanalytics/dictionaryfeedback/{dictionaryFeedbackId} 

Requires ALL permissions: 

* speechAndTextAnalytics:dictionaryterm:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
dictionary_feedback_id = 'dictionary_feedback_id_example' # str | The Id of the Dictionary Feedback

try:
    # Get a Speech & Text Analytics dictionary feedback by id
    api_response = api_instance.get_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id(dictionary_feedback_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dictionary_feedback_id** | **str**| The Id of the Dictionary Feedback |  |

### Return type

[**DictionaryFeedback**](DictionaryFeedback)


## get_speechandtextanalytics_program

> [**Program**](Program) get_speechandtextanalytics_program(program_id)


Get a Speech & Text Analytics program by id

Wraps GET /api/v2/speechandtextanalytics/programs/{programId} 

Requires ALL permissions: 

* speechAndTextAnalytics:program:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
program_id = 'program_id_example' # str | The id of the program

try:
    # Get a Speech & Text Analytics program by id
    api_response = api_instance.get_speechandtextanalytics_program(program_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_program: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **program_id** | **str**| The id of the program |  |

### Return type

[**Program**](Program)


## get_speechandtextanalytics_program_mappings

> [**ProgramMappings**](ProgramMappings) get_speechandtextanalytics_program_mappings(program_id)


Get Speech & Text Analytics program mappings to queues and flows by id

Wraps GET /api/v2/speechandtextanalytics/programs/{programId}/mappings 

Requires ALL permissions: 

* speechAndTextAnalytics:program:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
program_id = 'program_id_example' # str | The id of the program

try:
    # Get Speech & Text Analytics program mappings to queues and flows by id
    api_response = api_instance.get_speechandtextanalytics_program_mappings(program_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_program_mappings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **program_id** | **str**| The id of the program |  |

### Return type

[**ProgramMappings**](ProgramMappings)


## get_speechandtextanalytics_program_settings_insights

> [**ProgramInsightsSettings**](ProgramInsightsSettings) get_speechandtextanalytics_program_settings_insights(program_id)


Get AI Insights settings of a program

Wraps GET /api/v2/speechandtextanalytics/programs/{programId}/settings/insights 

Requires ALL permissions: 

* speechAndTextAnalytics:program:view
* speechAndTextAnalytics:insightsSettings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
program_id = 'program_id_example' # str | The id of the program

try:
    # Get AI Insights settings of a program
    api_response = api_instance.get_speechandtextanalytics_program_settings_insights(program_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_program_settings_insights: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **program_id** | **str**| The id of the program |  |

### Return type

[**ProgramInsightsSettings**](ProgramInsightsSettings)


## get_speechandtextanalytics_program_transcriptionengines

> [**ProgramTranscriptionEngines**](ProgramTranscriptionEngines) get_speechandtextanalytics_program_transcriptionengines(program_id)


Get transcription engine settings of a program

Wraps GET /api/v2/speechandtextanalytics/programs/{programId}/transcriptionengines 

Requires ALL permissions: 

* speechAndTextAnalytics:program:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
program_id = 'program_id_example' # str | The id of the program

try:
    # Get transcription engine settings of a program
    api_response = api_instance.get_speechandtextanalytics_program_transcriptionengines(program_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_program_transcriptionengines: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **program_id** | **str**| The id of the program |  |

### Return type

[**ProgramTranscriptionEngines**](ProgramTranscriptionEngines)


## get_speechandtextanalytics_programs

> [**ProgramsEntityListing**](ProgramsEntityListing) get_speechandtextanalytics_programs(next_page=next_page, page_size=page_size, state=state)


Get the list of Speech & Text Analytics programs

Wraps GET /api/v2/speechandtextanalytics/programs 

Requires ALL permissions: 

* speechAndTextAnalytics:program:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
next_page = 'next_page_example' # str | The key for listing the next page (optional)
page_size = 20 # int | The page size for the listing (optional) (default to 20)
state = 'state_example' # str | Program state. Defaults to Latest (optional)

try:
    # Get the list of Speech & Text Analytics programs
    api_response = api_instance.get_speechandtextanalytics_programs(next_page=next_page, page_size=page_size, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_programs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **next_page** | **str**| The key for listing the next page | [optional]  |
| **page_size** | **int**| The page size for the listing | [optional] [default to 20] |
| **state** | **str**| Program state. Defaults to Latest | [optional] <br />**Values**: Latest, Published |

### Return type

[**ProgramsEntityListing**](ProgramsEntityListing)


## get_speechandtextanalytics_programs_general_job

> [**GeneralProgramJob**](GeneralProgramJob) get_speechandtextanalytics_programs_general_job(job_id)


Get a Speech & Text Analytics general program job by id

Wraps GET /api/v2/speechandtextanalytics/programs/general/jobs/{jobId} 

Requires ALL permissions: 

* speechAndTextAnalytics:program:add
* speechAndTextAnalytics:program:edit
* speechAndTextAnalytics:topic:add
* speechAndTextAnalytics:topic:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
job_id = 'job_id_example' # str | The id of the publish programs job

try:
    # Get a Speech & Text Analytics general program job by id
    api_response = api_instance.get_speechandtextanalytics_programs_general_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_programs_general_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The id of the publish programs job |  |

### Return type

[**GeneralProgramJob**](GeneralProgramJob)


## get_speechandtextanalytics_programs_mappings

> [**ProgramsMappingsEntityListing**](ProgramsMappingsEntityListing) get_speechandtextanalytics_programs_mappings(next_page=next_page, page_size=page_size)


Get the list of Speech & Text Analytics programs mappings to queues and flows

Wraps GET /api/v2/speechandtextanalytics/programs/mappings 

Requires ALL permissions: 

* speechAndTextAnalytics:program:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
next_page = 'next_page_example' # str | The key for listing the next page (optional)
page_size = 20 # int | The page size for the listing (optional) (default to 20)

try:
    # Get the list of Speech & Text Analytics programs mappings to queues and flows
    api_response = api_instance.get_speechandtextanalytics_programs_mappings(next_page=next_page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_programs_mappings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **next_page** | **str**| The key for listing the next page | [optional]  |
| **page_size** | **int**| The page size for the listing | [optional] [default to 20] |

### Return type

[**ProgramsMappingsEntityListing**](ProgramsMappingsEntityListing)


## get_speechandtextanalytics_programs_publishjob

> [**ProgramJob**](ProgramJob) get_speechandtextanalytics_programs_publishjob(job_id)


Get a Speech & Text Analytics publish programs job by id

Wraps GET /api/v2/speechandtextanalytics/programs/publishjobs/{jobId} 

Requires ALL permissions: 

* speechAndTextAnalytics:program:publish

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
job_id = 'job_id_example' # str | The id of the publish programs job

try:
    # Get a Speech & Text Analytics publish programs job by id
    api_response = api_instance.get_speechandtextanalytics_programs_publishjob(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_programs_publishjob: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The id of the publish programs job |  |

### Return type

[**ProgramJob**](ProgramJob)


## get_speechandtextanalytics_programs_settings_insights

> [**ProgramInsightsSettingsEntityListing**](ProgramInsightsSettingsEntityListing) get_speechandtextanalytics_programs_settings_insights(page_size=page_size, page_number=page_number, program_ids=program_ids)


Get the list of program AI Insights settings for the organization

Wraps GET /api/v2/speechandtextanalytics/programs/settings/insights 

Requires ALL permissions: 

* speechAndTextAnalytics:program:view
* speechAndTextAnalytics:insightsSettings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
page_size = 100 # int | The page size for the listing. The max that will be returned is 100. (optional) (default to 100)
page_number = 1 # int | The page number for the listing (optional) (default to 1)
program_ids = ['program_ids_example'] # list[str] | Comma separated Program IDs to filter by. Maximum of 50 IDs allowed. (optional)

try:
    # Get the list of program AI Insights settings for the organization
    api_response = api_instance.get_speechandtextanalytics_programs_settings_insights(page_size=page_size, page_number=page_number, program_ids=program_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_programs_settings_insights: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The page size for the listing. The max that will be returned is 100. | [optional] [default to 100] |
| **page_number** | **int**| The page number for the listing | [optional] [default to 1] |
| **program_ids** | [**list[str]**](str)| Comma separated Program IDs to filter by. Maximum of 50 IDs allowed. | [optional]  |

### Return type

[**ProgramInsightsSettingsEntityListing**](ProgramInsightsSettingsEntityListing)


## get_speechandtextanalytics_programs_transcriptionengines_dialects

> [**SupportedDialectsEntityListing**](SupportedDialectsEntityListing) get_speechandtextanalytics_programs_transcriptionengines_dialects()


Get supported dialects for each transcription engine

Wraps GET /api/v2/speechandtextanalytics/programs/transcriptionengines/dialects 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()

try:
    # Get supported dialects for each transcription engine
    api_response = api_instance.get_speechandtextanalytics_programs_transcriptionengines_dialects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_programs_transcriptionengines_dialects: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**SupportedDialectsEntityListing**](SupportedDialectsEntityListing)


## get_speechandtextanalytics_programs_unpublished

> [**UnpublishedProgramsEntityListing**](UnpublishedProgramsEntityListing) get_speechandtextanalytics_programs_unpublished(next_page=next_page, page_size=page_size)


Get the list of Speech & Text Analytics unpublished programs

Wraps GET /api/v2/speechandtextanalytics/programs/unpublished 

Requires ALL permissions: 

* speechAndTextAnalytics:program:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
next_page = 'next_page_example' # str | The key for listing the next page (optional)
page_size = 20 # int | The page size for the listing (optional) (default to 20)

try:
    # Get the list of Speech & Text Analytics unpublished programs
    api_response = api_instance.get_speechandtextanalytics_programs_unpublished(next_page=next_page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_programs_unpublished: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **next_page** | **str**| The key for listing the next page | [optional]  |
| **page_size** | **int**| The page size for the listing | [optional] [default to 20] |

### Return type

[**UnpublishedProgramsEntityListing**](UnpublishedProgramsEntityListing)


## get_speechandtextanalytics_reprocessing_job

> [**ReprocessJobResponse**](ReprocessJobResponse) get_speechandtextanalytics_reprocessing_job(job_id)


Get a Speech & Text Analytics reprocess job by id

get_speechandtextanalytics_reprocessing_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/speechandtextanalytics/reprocessing/jobs/{jobId} 

Requires ALL permissions: 

* speechAndTextAnalytics:reprocessInteractions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
job_id = 'job_id_example' # str | The Id of the Reprocessing job

try:
    # Get a Speech & Text Analytics reprocess job by id
    api_response = api_instance.get_speechandtextanalytics_reprocessing_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_reprocessing_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The Id of the Reprocessing job |  |

### Return type

[**ReprocessJobResponse**](ReprocessJobResponse)


## get_speechandtextanalytics_reprocessing_job_interactions

> [**ReprocessInteractionsByJobIdResponse**](ReprocessInteractionsByJobIdResponse) get_speechandtextanalytics_reprocessing_job_interactions(job_id)


Get a Speech & Text Analytics Reprocessing interactions statuses by job id

get_speechandtextanalytics_reprocessing_job_interactions is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/speechandtextanalytics/reprocessing/jobs/{jobId}/interactions 

Requires ALL permissions: 

* speechAndTextAnalytics:reprocessInteractions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
job_id = 'job_id_example' # str | The Id of the Reprocessing job

try:
    # Get a Speech & Text Analytics Reprocessing interactions statuses by job id
    api_response = api_instance.get_speechandtextanalytics_reprocessing_job_interactions(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_reprocessing_job_interactions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The Id of the Reprocessing job |  |

### Return type

[**ReprocessInteractionsByJobIdResponse**](ReprocessInteractionsByJobIdResponse)


## get_speechandtextanalytics_reprocessing_jobs

> [**ReprocessJobEntityListingResponse**](ReprocessJobEntityListingResponse) get_speechandtextanalytics_reprocessing_jobs(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name)


Get the list of Speech & Text Analytics reprocess jobs

get_speechandtextanalytics_reprocessing_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/speechandtextanalytics/reprocessing/jobs 

Requires ALL permissions: 

* speechAndTextAnalytics:reprocessInteractions:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
page_size = 56 # int | The page size for the listing. The max that will be returned is 100. Default is 25. (optional)
page_number = 56 # int | The page number for the listing. Defaults to 1. (optional)
sort_order = 'sort_order_example' # str | Results are sorted by dateCreated. Please choose the sort order. The default is descending (desc). (optional)
name = 'name_example' # str | Case insensitive partial name to filter by. (optional)

try:
    # Get the list of Speech & Text Analytics reprocess jobs
    api_response = api_instance.get_speechandtextanalytics_reprocessing_jobs(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_reprocessing_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| The page size for the listing. The max that will be returned is 100. Default is 25. | [optional]  |
| **page_number** | **int**| The page number for the listing. Defaults to 1. | [optional]  |
| **sort_order** | **str**| Results are sorted by dateCreated. Please choose the sort order. The default is descending (desc). | [optional] <br />**Values**: asc, desc |
| **name** | **str**| Case insensitive partial name to filter by. | [optional]  |

### Return type

[**ReprocessJobEntityListingResponse**](ReprocessJobEntityListingResponse)


## get_speechandtextanalytics_sentiment_dialects

> [**EntityListing**](EntityListing) get_speechandtextanalytics_sentiment_dialects()


Get the list of Speech & Text Analytics sentiment supported dialects

Wraps GET /api/v2/speechandtextanalytics/sentiment/dialects 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()

try:
    # Get the list of Speech & Text Analytics sentiment supported dialects
    api_response = api_instance.get_speechandtextanalytics_sentiment_dialects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_sentiment_dialects: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**EntityListing**](EntityListing)


## get_speechandtextanalytics_sentimentfeedback

> [**SentimentFeedbackEntityListing**](SentimentFeedbackEntityListing) get_speechandtextanalytics_sentimentfeedback(dialect=dialect)


Get the list of Speech & Text Analytics SentimentFeedback

Wraps GET /api/v2/speechandtextanalytics/sentimentfeedback 

Requires ALL permissions: 

* speechAndTextAnalytics:feedback:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
dialect = 'en-US' # str | The key for filter the listing by dialect, dialect format is {language}-{country} where language follows ISO 639-1 standard and country follows ISO 3166-1 alpha 2 standard (optional)

try:
    # Get the list of Speech & Text Analytics SentimentFeedback
    api_response = api_instance.get_speechandtextanalytics_sentimentfeedback(dialect=dialect)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_sentimentfeedback: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dialect** | **str**| The key for filter the listing by dialect, dialect format is {language}-{country} where language follows ISO 639-1 standard and country follows ISO 3166-1 alpha 2 standard | [optional]  |

### Return type

[**SentimentFeedbackEntityListing**](SentimentFeedbackEntityListing)


## get_speechandtextanalytics_settings

> [**SpeechTextAnalyticsSettingsResponse**](SpeechTextAnalyticsSettingsResponse) get_speechandtextanalytics_settings()


Get Speech And Text Analytics Settings

Wraps GET /api/v2/speechandtextanalytics/settings 

Requires ALL permissions: 

* speechAndTextAnalytics:settings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()

try:
    # Get Speech And Text Analytics Settings
    api_response = api_instance.get_speechandtextanalytics_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**SpeechTextAnalyticsSettingsResponse**](SpeechTextAnalyticsSettingsResponse)


## get_speechandtextanalytics_topic

> [**Topic**](Topic) get_speechandtextanalytics_topic(topic_id)


Get a Speech & Text Analytics topic by id

Wraps GET /api/v2/speechandtextanalytics/topics/{topicId} 

Requires ALL permissions: 

* speechAndTextAnalytics:topic:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
topic_id = 'topic_id_example' # str | The id of the topic

try:
    # Get a Speech & Text Analytics topic by id
    api_response = api_instance.get_speechandtextanalytics_topic(topic_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_topic: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| The id of the topic |  |

### Return type

[**Topic**](Topic)


## get_speechandtextanalytics_topics

> [**TopicsEntityListing**](TopicsEntityListing) get_speechandtextanalytics_topics(next_page=next_page, page_size=page_size, page_number=page_number, state=state, name=name, ids=ids, dialects=dialects, sort_by=sort_by, sort_order=sort_order)


Get the list of Speech & Text Analytics topics

Wraps GET /api/v2/speechandtextanalytics/topics 

Requires ALL permissions: 

* speechAndTextAnalytics:topic:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
next_page = 'next_page_example' # str | The key for listing the next page (optional)
page_size = 20 # int | The page size for the listing. The max that will be returned is 500. (optional) (default to 20)
page_number = 56 # int | The page number for the listing (optional)
state = 'state_example' # str | Topic state. Defaults to latest (optional)
name = 'name_example' # str | Case insensitive partial name to filter by (optional)
ids = ['ids_example'] # list[str] | Comma separated Topic IDs to filter by. Cannot be used with other filters. Maximum of 50 IDs allowed. (optional)
dialects = ['dialects_example'] # list[str] | Comma separated dialect strings to filter by. Maximum of 15 dialects allowed. (optional)
sort_by = 'sort_by_example' # str | Sort results by. Defaults to name (optional)
sort_order = 'sort_order_example' # str | Sort order. Defaults to asc (optional)

try:
    # Get the list of Speech & Text Analytics topics
    api_response = api_instance.get_speechandtextanalytics_topics(next_page=next_page, page_size=page_size, page_number=page_number, state=state, name=name, ids=ids, dialects=dialects, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_topics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **next_page** | **str**| The key for listing the next page | [optional]  |
| **page_size** | **int**| The page size for the listing. The max that will be returned is 500. | [optional] [default to 20] |
| **page_number** | **int**| The page number for the listing | [optional]  |
| **state** | **str**| Topic state. Defaults to latest | [optional] <br />**Values**: latest, published |
| **name** | **str**| Case insensitive partial name to filter by | [optional]  |
| **ids** | [**list[str]**](str)| Comma separated Topic IDs to filter by. Cannot be used with other filters. Maximum of 50 IDs allowed. | [optional]  |
| **dialects** | [**list[str]**](str)| Comma separated dialect strings to filter by. Maximum of 15 dialects allowed. | [optional] <br />**Values**: en-US, es-US, en-AU, en-GB, en-ZA, es-ES, en-IN, fr-FR, fr-CA, it-IT, de-DE, pt-BR, pl-PL, pt-PT, nl-NL, ko-KR |
| **sort_by** | **str**| Sort results by. Defaults to name | [optional] <br />**Values**: name, matchingType |
| **sort_order** | **str**| Sort order. Defaults to asc | [optional] <br />**Values**: asc, desc |

### Return type

[**TopicsEntityListing**](TopicsEntityListing)


## get_speechandtextanalytics_topics_dialects

> [**EntityListing**](EntityListing) get_speechandtextanalytics_topics_dialects()


Get list of supported Speech & Text Analytics topics dialects

Wraps GET /api/v2/speechandtextanalytics/topics/dialects 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()

try:
    # Get list of supported Speech & Text Analytics topics dialects
    api_response = api_instance.get_speechandtextanalytics_topics_dialects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_topics_dialects: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**EntityListing**](EntityListing)


## get_speechandtextanalytics_topics_general

> [**GeneralTopicsEntityListing**](GeneralTopicsEntityListing) get_speechandtextanalytics_topics_general(dialect=dialect)


Get the Speech & Text Analytics general topics for a given dialect

Wraps GET /api/v2/speechandtextanalytics/topics/general 

Requires ALL permissions: 

* speechAndTextAnalytics:topic:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
dialect = 'dialect_example' # str | The dialect of the general topics, dialect format is {language}-{country} where language follows ISO 639-1 standard and country follows ISO 3166-1 alpha 2 standard (optional)

try:
    # Get the Speech & Text Analytics general topics for a given dialect
    api_response = api_instance.get_speechandtextanalytics_topics_general(dialect=dialect)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_topics_general: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dialect** | **str**| The dialect of the general topics, dialect format is {language}-{country} where language follows ISO 639-1 standard and country follows ISO 3166-1 alpha 2 standard | [optional] <br />**Values**: ar-001, ar-AE, ar-BH, ar-EG, ar-IL, ar-SA, ar-TN, da-DK, de-CH, de-DE, en-AU, en-GB, en-HK, en-IE, en-IN, en-NZ, en-SG, en-US, en-ZA, es-ES, es-US, fi-FI, fr-CA, fr-FR, he-IL, hi-IN, it-IT, ja-JP, ko-KR, nb-NO, nl-NL, pl-PL, pt-BR, pt-PT, sv-SE, tr-TR, zh-CN, zh-HK, zh-TW, zu-ZA |

### Return type

[**GeneralTopicsEntityListing**](GeneralTopicsEntityListing)


## get_speechandtextanalytics_topics_general_status

> [**UnifiedGeneralTopicEntityListing**](UnifiedGeneralTopicEntityListing) get_speechandtextanalytics_topics_general_status(dialect=dialect)


Get the list of general topics from the org and the system with their current status

Wraps GET /api/v2/speechandtextanalytics/topics/general/status 

Requires ALL permissions: 

* speechAndTextAnalytics:topic:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
dialect = 'dialect_example' # str | The dialect of the general topics, dialect format is {language}-{country} where language follows ISO 639-1 standard and country follows ISO 3166-1 alpha 2 standard (optional)

try:
    # Get the list of general topics from the org and the system with their current status
    api_response = api_instance.get_speechandtextanalytics_topics_general_status(dialect=dialect)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_topics_general_status: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dialect** | **str**| The dialect of the general topics, dialect format is {language}-{country} where language follows ISO 639-1 standard and country follows ISO 3166-1 alpha 2 standard | [optional] <br />**Values**: ar-001, ar-AE, ar-BH, ar-EG, ar-IL, ar-SA, ar-TN, da-DK, de-CH, de-DE, en-AU, en-GB, en-HK, en-IE, en-IN, en-NZ, en-SG, en-US, en-ZA, es-ES, es-US, fi-FI, fr-CA, fr-FR, he-IL, hi-IN, it-IT, ja-JP, ko-KR, nb-NO, nl-NL, pl-PL, pt-BR, pt-PT, sv-SE, tr-TR, zh-CN, zh-HK, zh-TW, zu-ZA |

### Return type

[**UnifiedGeneralTopicEntityListing**](UnifiedGeneralTopicEntityListing)


## get_speechandtextanalytics_topics_publishjob

> [**TopicJob**](TopicJob) get_speechandtextanalytics_topics_publishjob(job_id)


Get a Speech & Text Analytics publish topics job by id

Wraps GET /api/v2/speechandtextanalytics/topics/publishjobs/{jobId} 

Requires ALL permissions: 

* speechAndTextAnalytics:topic:publish

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
job_id = 'job_id_example' # str | The id of the publish topics job

try:
    # Get a Speech & Text Analytics publish topics job by id
    api_response = api_instance.get_speechandtextanalytics_topics_publishjob(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_topics_publishjob: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The id of the publish topics job |  |

### Return type

[**TopicJob**](TopicJob)


## get_speechandtextanalytics_topics_testphrase_job

> [**TestTopicPhraseJob**](TestTopicPhraseJob) get_speechandtextanalytics_topics_testphrase_job(job_id)


Get a Speech & Text Analytics test topics phrase job by id

Wraps GET /api/v2/speechandtextanalytics/topics/testphrase/jobs/{jobId} 

Requires ALL permissions: 

* speechAndTextAnalytics:topic:testPhrase

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
job_id = 'job_id_example' # str | the id of the test topic phrase job

try:
    # Get a Speech & Text Analytics test topics phrase job by id
    api_response = api_instance.get_speechandtextanalytics_topics_testphrase_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_topics_testphrase_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| the id of the test topic phrase job |  |

### Return type

[**TestTopicPhraseJob**](TestTopicPhraseJob)


## get_speechandtextanalytics_translations_language_conversation

> [**CommunicationTranslationList**](CommunicationTranslationList) get_speechandtextanalytics_translations_language_conversation(language_id, conversation_id, communication_id=communication_id, recording_id=recording_id)


Translate a single interaction recording (or an email conversation)

Wraps GET /api/v2/speechandtextanalytics/translations/languages/{languageId}/conversations/{conversationId} 

Requires ALL permissions: 

* speechAndTextAnalytics:translation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
language_id = 'language_id_example' # str | Target translation language
conversation_id = 'conversation_id_example' # str | Conversation id
communication_id = 'communication_id_example' # str | Communication id associated with the conversation. Please provide a valid communicationId when requesting non-email interactions. (optional)
recording_id = 'recording_id_example' # str | Recording id associated with the communication. Please provide a valid recordingId when requesting voice interactions. (optional)

try:
    # Translate a single interaction recording (or an email conversation)
    api_response = api_instance.get_speechandtextanalytics_translations_language_conversation(language_id, conversation_id, communication_id=communication_id, recording_id=recording_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_translations_language_conversation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language_id** | **str**| Target translation language |  |
| **conversation_id** | **str**| Conversation id |  |
| **communication_id** | **str**| Communication id associated with the conversation. Please provide a valid communicationId when requesting non-email interactions. | [optional]  |
| **recording_id** | **str**| Recording id associated with the communication. Please provide a valid recordingId when requesting voice interactions. | [optional]  |

### Return type

[**CommunicationTranslationList**](CommunicationTranslationList)


## get_speechandtextanalytics_translations_languages

> [**TranslateSupportedLanguageList**](TranslateSupportedLanguageList) get_speechandtextanalytics_translations_languages()


Get supported translation languages

Wraps GET /api/v2/speechandtextanalytics/translations/languages 

Requires ALL permissions: 

* speechAndTextAnalytics:translation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()

try:
    # Get supported translation languages
    api_response = api_instance.get_speechandtextanalytics_translations_languages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_translations_languages: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**TranslateSupportedLanguageList**](TranslateSupportedLanguageList)


## patch_speechandtextanalytics_settings

> [**SpeechTextAnalyticsSettingsResponse**](SpeechTextAnalyticsSettingsResponse) patch_speechandtextanalytics_settings(body)


Patch Speech And Text Analytics Settings

Wraps PATCH /api/v2/speechandtextanalytics/settings 

Requires ALL permissions: 

* speechAndTextAnalytics:settings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
body = PureCloudPlatformClientV2.SpeechTextAnalyticsSettingsRequest() # SpeechTextAnalyticsSettingsRequest | Speech And Text Analytics Settings

try:
    # Patch Speech And Text Analytics Settings
    api_response = api_instance.patch_speechandtextanalytics_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->patch_speechandtextanalytics_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SpeechTextAnalyticsSettingsRequest**](SpeechTextAnalyticsSettingsRequest)| Speech And Text Analytics Settings |  |

### Return type

[**SpeechTextAnalyticsSettingsResponse**](SpeechTextAnalyticsSettingsResponse)


## post_speechandtextanalytics_categories

> [**StaCategory**](StaCategory) post_speechandtextanalytics_categories(body)


Create new Speech & Text Analytics category

Wraps POST /api/v2/speechandtextanalytics/categories 

Requires ALL permissions: 

* speechAndTextAnalytics:category:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
body = PureCloudPlatformClientV2.CategoryRequest() # CategoryRequest | The category to create

try:
    # Create new Speech & Text Analytics category
    api_response = api_instance.post_speechandtextanalytics_categories(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->post_speechandtextanalytics_categories: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CategoryRequest**](CategoryRequest)| The category to create |  |

### Return type

[**StaCategory**](StaCategory)


## post_speechandtextanalytics_dictionaryfeedback

> [**DictionaryFeedback**](DictionaryFeedback) post_speechandtextanalytics_dictionaryfeedback(body)


Create a Speech & Text Analytics DictionaryFeedback

Wraps POST /api/v2/speechandtextanalytics/dictionaryfeedback 

Requires ALL permissions: 

* speechAndTextAnalytics:dictionaryterm:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
body = PureCloudPlatformClientV2.DictionaryFeedback() # DictionaryFeedback | The DictionaryFeedback to create

try:
    # Create a Speech & Text Analytics DictionaryFeedback
    api_response = api_instance.post_speechandtextanalytics_dictionaryfeedback(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->post_speechandtextanalytics_dictionaryfeedback: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DictionaryFeedback**](DictionaryFeedback)| The DictionaryFeedback to create |  |

### Return type

[**DictionaryFeedback**](DictionaryFeedback)


## post_speechandtextanalytics_programs

> [**Program**](Program) post_speechandtextanalytics_programs(body)


Create new Speech & Text Analytics program

Wraps POST /api/v2/speechandtextanalytics/programs 

Requires ALL permissions: 

* speechAndTextAnalytics:program:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
body = PureCloudPlatformClientV2.ProgramRequest() # ProgramRequest | The program to create

try:
    # Create new Speech & Text Analytics program
    api_response = api_instance.post_speechandtextanalytics_programs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->post_speechandtextanalytics_programs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ProgramRequest**](ProgramRequest)| The program to create |  |

### Return type

[**Program**](Program)


## post_speechandtextanalytics_programs_general_jobs

> [**GeneralProgramJob**](GeneralProgramJob) post_speechandtextanalytics_programs_general_jobs(body)


Create new Speech & Text Analytics general program job

Wraps POST /api/v2/speechandtextanalytics/programs/general/jobs 

Requires ALL permissions: 

* speechAndTextAnalytics:program:add
* speechAndTextAnalytics:program:edit
* speechAndTextAnalytics:topic:add
* speechAndTextAnalytics:topic:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
body = PureCloudPlatformClientV2.GeneralProgramJobRequest() # GeneralProgramJobRequest | The general programs job to create

try:
    # Create new Speech & Text Analytics general program job
    api_response = api_instance.post_speechandtextanalytics_programs_general_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->post_speechandtextanalytics_programs_general_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GeneralProgramJobRequest**](GeneralProgramJobRequest)| The general programs job to create |  |

### Return type

[**GeneralProgramJob**](GeneralProgramJob)


## post_speechandtextanalytics_programs_publishjobs

> [**ProgramJob**](ProgramJob) post_speechandtextanalytics_programs_publishjobs(body)


Create new Speech & Text Analytics publish programs job

Wraps POST /api/v2/speechandtextanalytics/programs/publishjobs 

Requires ALL permissions: 

* speechAndTextAnalytics:program:publish

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
body = PureCloudPlatformClientV2.ProgramJobRequest() # ProgramJobRequest | The publish programs job to create

try:
    # Create new Speech & Text Analytics publish programs job
    api_response = api_instance.post_speechandtextanalytics_programs_publishjobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->post_speechandtextanalytics_programs_publishjobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ProgramJobRequest**](ProgramJobRequest)| The publish programs job to create |  |

### Return type

[**ProgramJob**](ProgramJob)


## post_speechandtextanalytics_reprocessing_jobs

> [**ReprocessJobResponse**](ReprocessJobResponse) post_speechandtextanalytics_reprocessing_jobs(body)


Create a Speech & Text Analytics reprocess job.

post_speechandtextanalytics_reprocessing_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/speechandtextanalytics/reprocessing/jobs 

Requires ALL permissions: 

* speechAndTextAnalytics:reprocessInteractions:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
body = PureCloudPlatformClientV2.CreateReprocessJobRequest() # CreateReprocessJobRequest | The ReprocessJob to create

try:
    # Create a Speech & Text Analytics reprocess job.
    api_response = api_instance.post_speechandtextanalytics_reprocessing_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->post_speechandtextanalytics_reprocessing_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateReprocessJobRequest**](CreateReprocessJobRequest)| The ReprocessJob to create |  |

### Return type

[**ReprocessJobResponse**](ReprocessJobResponse)


## post_speechandtextanalytics_sentimentfeedback

> [**SentimentFeedback**](SentimentFeedback) post_speechandtextanalytics_sentimentfeedback(body)


Create a Speech & Text Analytics SentimentFeedback

Wraps POST /api/v2/speechandtextanalytics/sentimentfeedback 

Requires ALL permissions: 

* speechAndTextAnalytics:feedback:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
body = PureCloudPlatformClientV2.SentimentFeedback() # SentimentFeedback | The SentimentFeedback to create

try:
    # Create a Speech & Text Analytics SentimentFeedback
    api_response = api_instance.post_speechandtextanalytics_sentimentfeedback(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->post_speechandtextanalytics_sentimentfeedback: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SentimentFeedback**](SentimentFeedback)| The SentimentFeedback to create |  |

### Return type

[**SentimentFeedback**](SentimentFeedback)


## post_speechandtextanalytics_topics

> [**Topic**](Topic) post_speechandtextanalytics_topics(body)


Create new Speech & Text Analytics topic

Wraps POST /api/v2/speechandtextanalytics/topics 

Requires ALL permissions: 

* speechAndTextAnalytics:topic:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
body = PureCloudPlatformClientV2.TopicRequest() # TopicRequest | The topic to create

try:
    # Create new Speech & Text Analytics topic
    api_response = api_instance.post_speechandtextanalytics_topics(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->post_speechandtextanalytics_topics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TopicRequest**](TopicRequest)| The topic to create |  |

### Return type

[**Topic**](Topic)


## post_speechandtextanalytics_topics_publishjobs

> [**TopicJob**](TopicJob) post_speechandtextanalytics_topics_publishjobs(body)


Create new Speech & Text Analytics publish topics job

Wraps POST /api/v2/speechandtextanalytics/topics/publishjobs 

Requires ALL permissions: 

* speechAndTextAnalytics:topic:publish

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
body = PureCloudPlatformClientV2.TopicJobRequest() # TopicJobRequest | The publish topics job to create

try:
    # Create new Speech & Text Analytics publish topics job
    api_response = api_instance.post_speechandtextanalytics_topics_publishjobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->post_speechandtextanalytics_topics_publishjobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TopicJobRequest**](TopicJobRequest)| The publish topics job to create |  |

### Return type

[**TopicJob**](TopicJob)


## post_speechandtextanalytics_topics_testphrase_jobs

> [**TestTopicPhraseJobs**](TestTopicPhraseJobs) post_speechandtextanalytics_topics_testphrase_jobs(body)


Create new Speech & Text Analytics publish topics job

Wraps POST /api/v2/speechandtextanalytics/topics/testphrase/jobs 

Requires ALL permissions: 

* speechAndTextAnalytics:topic:testPhrase

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
body = PureCloudPlatformClientV2.TestTopicPhraseJobRequest() # TestTopicPhraseJobRequest | The publish test topic phrase job to create

try:
    # Create new Speech & Text Analytics publish topics job
    api_response = api_instance.post_speechandtextanalytics_topics_testphrase_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->post_speechandtextanalytics_topics_testphrase_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TestTopicPhraseJobRequest**](TestTopicPhraseJobRequest)| The publish test topic phrase job to create |  |

### Return type

[**TestTopicPhraseJobs**](TestTopicPhraseJobs)


## post_speechandtextanalytics_transcripts_search

> [**JsonSearchResponse**](JsonSearchResponse) post_speechandtextanalytics_transcripts_search(body)


Search resources.

Wraps POST /api/v2/speechandtextanalytics/transcripts/search 

Requires ANY permissions: 

* analytics:conversationDetail:view
* recording:recording:view
* recording:recordingSegment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
body = PureCloudPlatformClientV2.TranscriptSearchRequest() # TranscriptSearchRequest | Search request options

try:
    # Search resources.
    api_response = api_instance.post_speechandtextanalytics_transcripts_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->post_speechandtextanalytics_transcripts_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TranscriptSearchRequest**](TranscriptSearchRequest)| Search request options |  |

### Return type

[**JsonSearchResponse**](JsonSearchResponse)


## put_speechandtextanalytics_category

> [**StaCategory**](StaCategory) put_speechandtextanalytics_category(category_id, body)


Update a Speech & Text Analytics category by ID

Wraps PUT /api/v2/speechandtextanalytics/categories/{categoryId} 

Requires ALL permissions: 

* speechAndTextAnalytics:category:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
category_id = 'category_id_example' # str | The id of the category
body = PureCloudPlatformClientV2.CategoryRequest() # CategoryRequest | The updated category

try:
    # Update a Speech & Text Analytics category by ID
    api_response = api_instance.put_speechandtextanalytics_category(category_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->put_speechandtextanalytics_category: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **category_id** | **str**| The id of the category |  |
| **body** | [**CategoryRequest**](CategoryRequest)| The updated category |  |

### Return type

[**StaCategory**](StaCategory)


## put_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id

> [**DictionaryFeedback**](DictionaryFeedback) put_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id(dictionary_feedback_id, body=body)


Update existing Speech & Text Analytics dictionary feedback by id

Wraps PUT /api/v2/speechandtextanalytics/dictionaryfeedback/{dictionaryFeedbackId} 

Requires ALL permissions: 

* speechAndTextAnalytics:dictionaryterm:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
dictionary_feedback_id = 'dictionary_feedback_id_example' # str | The Id of the Dictionary Feedback
body = PureCloudPlatformClientV2.DictionaryFeedback() # DictionaryFeedback |  (optional)

try:
    # Update existing Speech & Text Analytics dictionary feedback by id
    api_response = api_instance.put_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id(dictionary_feedback_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->put_speechandtextanalytics_dictionaryfeedback_dictionary_feedback_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dictionary_feedback_id** | **str**| The Id of the Dictionary Feedback |  |
| **body** | [**DictionaryFeedback**](DictionaryFeedback)|  | [optional]  |

### Return type

[**DictionaryFeedback**](DictionaryFeedback)


## put_speechandtextanalytics_program

> [**Program**](Program) put_speechandtextanalytics_program(program_id, body)


Update existing Speech & Text Analytics program

Wraps PUT /api/v2/speechandtextanalytics/programs/{programId} 

Requires ALL permissions: 

* speechAndTextAnalytics:program:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
program_id = 'program_id_example' # str | The id of the program
body = PureCloudPlatformClientV2.ProgramRequest() # ProgramRequest | The program to update

try:
    # Update existing Speech & Text Analytics program
    api_response = api_instance.put_speechandtextanalytics_program(program_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->put_speechandtextanalytics_program: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **program_id** | **str**| The id of the program |  |
| **body** | [**ProgramRequest**](ProgramRequest)| The program to update |  |

### Return type

[**Program**](Program)


## put_speechandtextanalytics_program_mappings

> [**ProgramMappings**](ProgramMappings) put_speechandtextanalytics_program_mappings(program_id, body)


Set Speech & Text Analytics program mappings to queues and flows

Wraps PUT /api/v2/speechandtextanalytics/programs/{programId}/mappings 

Requires ALL permissions: 

* speechAndTextAnalytics:program:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
program_id = 'program_id_example' # str | The id of the program
body = PureCloudPlatformClientV2.ProgramMappingsRequest() # ProgramMappingsRequest | The program to set mappings for

try:
    # Set Speech & Text Analytics program mappings to queues and flows
    api_response = api_instance.put_speechandtextanalytics_program_mappings(program_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->put_speechandtextanalytics_program_mappings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **program_id** | **str**| The id of the program |  |
| **body** | [**ProgramMappingsRequest**](ProgramMappingsRequest)| The program to set mappings for |  |

### Return type

[**ProgramMappings**](ProgramMappings)


## put_speechandtextanalytics_program_settings_insights

> [**ProgramInsightsSettings**](ProgramInsightsSettings) put_speechandtextanalytics_program_settings_insights(program_id, body)


Update AI Insights settings of a program

Wraps PUT /api/v2/speechandtextanalytics/programs/{programId}/settings/insights 

Requires ALL permissions: 

* speechAndTextAnalytics:program:edit
* speechAndTextAnalytics:insightsSettings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
program_id = 'program_id_example' # str | The id of the program
body = PureCloudPlatformClientV2.InsightsSettingsRequest() # InsightsSettingsRequest | Program AI Insights setting

try:
    # Update AI Insights settings of a program
    api_response = api_instance.put_speechandtextanalytics_program_settings_insights(program_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->put_speechandtextanalytics_program_settings_insights: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **program_id** | **str**| The id of the program |  |
| **body** | [**InsightsSettingsRequest**](InsightsSettingsRequest)| Program AI Insights setting |  |

### Return type

[**ProgramInsightsSettings**](ProgramInsightsSettings)


## put_speechandtextanalytics_program_transcriptionengines

> [**ProgramTranscriptionEngines**](ProgramTranscriptionEngines) put_speechandtextanalytics_program_transcriptionengines(program_id, body)


Update transcription engine settings of a program

Wraps PUT /api/v2/speechandtextanalytics/programs/{programId}/transcriptionengines 

Requires ALL permissions: 

* speechAndTextAnalytics:program:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
program_id = 'program_id_example' # str | The id of the program
body = PureCloudPlatformClientV2.TranscriptionEnginesRequest() # TranscriptionEnginesRequest | Program transcription engine setting

try:
    # Update transcription engine settings of a program
    api_response = api_instance.put_speechandtextanalytics_program_transcriptionengines(program_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->put_speechandtextanalytics_program_transcriptionengines: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **program_id** | **str**| The id of the program |  |
| **body** | [**TranscriptionEnginesRequest**](TranscriptionEnginesRequest)| Program transcription engine setting |  |

### Return type

[**ProgramTranscriptionEngines**](ProgramTranscriptionEngines)


## put_speechandtextanalytics_settings

> [**SpeechTextAnalyticsSettingsResponse**](SpeechTextAnalyticsSettingsResponse) put_speechandtextanalytics_settings(body)


Update Speech And Text Analytics Settings

Wraps PUT /api/v2/speechandtextanalytics/settings 

Requires ALL permissions: 

* speechAndTextAnalytics:settings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
body = PureCloudPlatformClientV2.SpeechTextAnalyticsSettingsRequest() # SpeechTextAnalyticsSettingsRequest | Speech And Text Analytics Settings

try:
    # Update Speech And Text Analytics Settings
    api_response = api_instance.put_speechandtextanalytics_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->put_speechandtextanalytics_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SpeechTextAnalyticsSettingsRequest**](SpeechTextAnalyticsSettingsRequest)| Speech And Text Analytics Settings |  |

### Return type

[**SpeechTextAnalyticsSettingsResponse**](SpeechTextAnalyticsSettingsResponse)


## put_speechandtextanalytics_topic

> [**Topic**](Topic) put_speechandtextanalytics_topic(topic_id, body)


Update existing Speech & Text Analytics topic

Wraps PUT /api/v2/speechandtextanalytics/topics/{topicId} 

Requires ALL permissions: 

* speechAndTextAnalytics:topic:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SpeechTextAnalyticsApi()
topic_id = 'topic_id_example' # str | The id of the topic
body = PureCloudPlatformClientV2.TopicRequest() # TopicRequest | The topic to update

try:
    # Update existing Speech & Text Analytics topic
    api_response = api_instance.put_speechandtextanalytics_topic(topic_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->put_speechandtextanalytics_topic: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| The id of the topic |  |
| **body** | [**TopicRequest**](TopicRequest)| The topic to update |  |

### Return type

[**Topic**](Topic)


_PureCloudPlatformClientV2 247.0.0_

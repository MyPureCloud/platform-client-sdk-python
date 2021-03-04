---
title: SpeechTextAnalyticsApi
---

## PureCloudPlatformClientV2.SpeechTextAnalyticsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_speechandtextanalytics_program**](SpeechTextAnalyticsApi.html#delete_speechandtextanalytics_program) | Delete a Speech &amp; Text Analytics program by id|
|[**delete_speechandtextanalytics_topic**](SpeechTextAnalyticsApi.html#delete_speechandtextanalytics_topic) | Delete a Speech &amp; Text Analytics topic by id|
|[**get_speechandtextanalytics_conversation**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_conversation) | Get Speech and Text Analytics for a specific conversation|
|[**get_speechandtextanalytics_conversation_communication_transcripturl**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_conversation_communication_transcripturl) | Get the pre-signed S3 URL for the transcript of a specific communication of a conversation|
|[**get_speechandtextanalytics_dialects**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_dialects) | Get list of supported Speech &amp; Text Analytics dialects|
|[**get_speechandtextanalytics_program**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_program) | Get a Speech &amp; Text Analytics program by id|
|[**get_speechandtextanalytics_programs**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_programs) | Get the list of Speech &amp; Text Analytics programs|
|[**get_speechandtextanalytics_programs_general_job**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_programs_general_job) | Get a Speech &amp; Text Analytics general program job by id|
|[**get_speechandtextanalytics_programs_publishjob**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_programs_publishjob) | Get a Speech &amp; Text Analytics publish programs job by id|
|[**get_speechandtextanalytics_programs_unpublished**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_programs_unpublished) | Get the list of Speech &amp; Text Analytics unpublished programs|
|[**get_speechandtextanalytics_settings**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_settings) | Get Speech And Text Analytics Settings|
|[**get_speechandtextanalytics_topic**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_topic) | Get a Speech &amp; Text Analytics topic by id|
|[**get_speechandtextanalytics_topics**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_topics) | Get the list of Speech &amp; Text Analytics topics|
|[**get_speechandtextanalytics_topics_general**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_topics_general) | Get the Speech &amp; Text Analytics general topics for a given dialect|
|[**get_speechandtextanalytics_topics_publishjob**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_topics_publishjob) | Get a Speech &amp; Text Analytics publish topics job by id|
|[**patch_speechandtextanalytics_settings**](SpeechTextAnalyticsApi.html#patch_speechandtextanalytics_settings) | Patch Speech And Text Analytics Settings|
|[**post_speechandtextanalytics_programs**](SpeechTextAnalyticsApi.html#post_speechandtextanalytics_programs) | Create new Speech &amp; Text Analytics program|
|[**post_speechandtextanalytics_programs_general_jobs**](SpeechTextAnalyticsApi.html#post_speechandtextanalytics_programs_general_jobs) | Create new Speech &amp; Text Analytics general program job|
|[**post_speechandtextanalytics_programs_publishjobs**](SpeechTextAnalyticsApi.html#post_speechandtextanalytics_programs_publishjobs) | Create new Speech &amp; Text Analytics publish programs job|
|[**post_speechandtextanalytics_topics**](SpeechTextAnalyticsApi.html#post_speechandtextanalytics_topics) | Create new Speech &amp; Text Analytics topic|
|[**post_speechandtextanalytics_topics_publishjobs**](SpeechTextAnalyticsApi.html#post_speechandtextanalytics_topics_publishjobs) | Create new Speech &amp; Text Analytics publish topics job|
|[**post_speechandtextanalytics_transcripts_search**](SpeechTextAnalyticsApi.html#post_speechandtextanalytics_transcripts_search) | Search resources.|
|[**put_speechandtextanalytics_program**](SpeechTextAnalyticsApi.html#put_speechandtextanalytics_program) | Update existing Speech &amp; Text Analytics program|
|[**put_speechandtextanalytics_topic**](SpeechTextAnalyticsApi.html#put_speechandtextanalytics_topic) | Update existing Speech &amp; Text Analytics topic|
{: class="table table-striped"}

<a name="delete_speechandtextanalytics_program"></a>

##  delete_speechandtextanalytics_program(program_id, force_delete=force_delete)



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
force_delete = false # bool | Indicates whether the program is forced to be deleted or not. Required when the program to delete is the default program. (optional) (default to false)

try:
    # Delete a Speech & Text Analytics program by id
    api_instance.delete_speechandtextanalytics_program(program_id, force_delete=force_delete)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->delete_speechandtextanalytics_program: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **program_id** | **str**| The id of the program |  |
| **force_delete** | **bool**| Indicates whether the program is forced to be deleted or not. Required when the program to delete is the default program. | [optional] [default to false] |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_speechandtextanalytics_topic"></a>

##  delete_speechandtextanalytics_topic(topic_id)



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
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_speechandtextanalytics_conversation"></a>

## [**ConversationMetrics**](ConversationMetrics.html) get_speechandtextanalytics_conversation(conversation_id)



Get Speech and Text Analytics for a specific conversation



Wraps GET /api/v2/speechandtextanalytics/conversations/{conversationId} 

Requires ANY permissions: 

* recording:recording:view

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
{: class="table table-striped"}

### Return type

[**ConversationMetrics**](ConversationMetrics.html)

<a name="get_speechandtextanalytics_conversation_communication_transcripturl"></a>

## [**TranscriptUrl**](TranscriptUrl.html) get_speechandtextanalytics_conversation_communication_transcripturl(conversation_id, communication_id)



Get the pre-signed S3 URL for the transcript of a specific communication of a conversation



Wraps GET /api/v2/speechandtextanalytics/conversations/{conversationId}/communications/{communicationId}/transcripturl 

Requires ANY permissions: 

* recording:recording:view

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
{: class="table table-striped"}

### Return type

[**TranscriptUrl**](TranscriptUrl.html)

<a name="get_speechandtextanalytics_dialects"></a>

## list[object]** get_speechandtextanalytics_dialects()



Get list of supported Speech & Text Analytics dialects



Wraps GET /api/v2/speechandtextanalytics/dialects 

Requires NO permissions: 


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
    # Get list of supported Speech & Text Analytics dialects
    api_response = api_instance.get_speechandtextanalytics_dialects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_dialects: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

**list[object]**

<a name="get_speechandtextanalytics_program"></a>

## [**Program**](Program.html) get_speechandtextanalytics_program(program_id)



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
{: class="table table-striped"}

### Return type

[**Program**](Program.html)

<a name="get_speechandtextanalytics_programs"></a>

## [**ProgramsEntityListing**](ProgramsEntityListing.html) get_speechandtextanalytics_programs(next_page=next_page, page_size=page_size)



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

try:
    # Get the list of Speech & Text Analytics programs
    api_response = api_instance.get_speechandtextanalytics_programs(next_page=next_page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_programs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **next_page** | **str**| The key for listing the next page | [optional]  |
| **page_size** | **int**| The page size for the listing | [optional] [default to 20] |
{: class="table table-striped"}

### Return type

[**ProgramsEntityListing**](ProgramsEntityListing.html)

<a name="get_speechandtextanalytics_programs_general_job"></a>

## [**GeneralProgramJob**](GeneralProgramJob.html) get_speechandtextanalytics_programs_general_job(job_id)



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
{: class="table table-striped"}

### Return type

[**GeneralProgramJob**](GeneralProgramJob.html)

<a name="get_speechandtextanalytics_programs_publishjob"></a>

## [**ProgramJob**](ProgramJob.html) get_speechandtextanalytics_programs_publishjob(job_id)



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
{: class="table table-striped"}

### Return type

[**ProgramJob**](ProgramJob.html)

<a name="get_speechandtextanalytics_programs_unpublished"></a>

## [**UnpublishedProgramsEntityListing**](UnpublishedProgramsEntityListing.html) get_speechandtextanalytics_programs_unpublished(next_page=next_page, page_size=page_size)



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
{: class="table table-striped"}

### Return type

[**UnpublishedProgramsEntityListing**](UnpublishedProgramsEntityListing.html)

<a name="get_speechandtextanalytics_settings"></a>

## [**SpeechTextAnalyticsSettingsResponse**](SpeechTextAnalyticsSettingsResponse.html) get_speechandtextanalytics_settings()



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

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**SpeechTextAnalyticsSettingsResponse**](SpeechTextAnalyticsSettingsResponse.html)

<a name="get_speechandtextanalytics_topic"></a>

## [**Topic**](Topic.html) get_speechandtextanalytics_topic(topic_id)



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
{: class="table table-striped"}

### Return type

[**Topic**](Topic.html)

<a name="get_speechandtextanalytics_topics"></a>

## [**TopicsEntityListing**](TopicsEntityListing.html) get_speechandtextanalytics_topics(next_page=next_page, page_size=page_size)



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
page_size = 20 # int | The page size for the listing (optional) (default to 20)

try:
    # Get the list of Speech & Text Analytics topics
    api_response = api_instance.get_speechandtextanalytics_topics(next_page=next_page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_topics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **next_page** | **str**| The key for listing the next page | [optional]  |
| **page_size** | **int**| The page size for the listing | [optional] [default to 20] |
{: class="table table-striped"}

### Return type

[**TopicsEntityListing**](TopicsEntityListing.html)

<a name="get_speechandtextanalytics_topics_general"></a>

## [**GeneralTopicsEntityListing**](GeneralTopicsEntityListing.html) get_speechandtextanalytics_topics_general(dialect=dialect)



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
| **dialect** | **str**| The dialect of the general topics, dialect format is {language}-{country} where language follows ISO 639-1 standard and country follows ISO 3166-1 alpha 2 standard | [optional] <br />**Values**: en-US, es-US |
{: class="table table-striped"}

### Return type

[**GeneralTopicsEntityListing**](GeneralTopicsEntityListing.html)

<a name="get_speechandtextanalytics_topics_publishjob"></a>

## [**TopicJob**](TopicJob.html) get_speechandtextanalytics_topics_publishjob(job_id)



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
{: class="table table-striped"}

### Return type

[**TopicJob**](TopicJob.html)

<a name="patch_speechandtextanalytics_settings"></a>

## [**SpeechTextAnalyticsSettingsResponse**](SpeechTextAnalyticsSettingsResponse.html) patch_speechandtextanalytics_settings(body)



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
| **body** | [**SpeechTextAnalyticsSettingsRequest**](SpeechTextAnalyticsSettingsRequest.html)| Speech And Text Analytics Settings |  |
{: class="table table-striped"}

### Return type

[**SpeechTextAnalyticsSettingsResponse**](SpeechTextAnalyticsSettingsResponse.html)

<a name="post_speechandtextanalytics_programs"></a>

## [**Program**](Program.html) post_speechandtextanalytics_programs(body)



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
| **body** | [**ProgramRequest**](ProgramRequest.html)| The program to create |  |
{: class="table table-striped"}

### Return type

[**Program**](Program.html)

<a name="post_speechandtextanalytics_programs_general_jobs"></a>

## [**GeneralProgramJob**](GeneralProgramJob.html) post_speechandtextanalytics_programs_general_jobs(body)



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
| **body** | [**GeneralProgramJobRequest**](GeneralProgramJobRequest.html)| The general programs job to create |  |
{: class="table table-striped"}

### Return type

[**GeneralProgramJob**](GeneralProgramJob.html)

<a name="post_speechandtextanalytics_programs_publishjobs"></a>

## [**ProgramJob**](ProgramJob.html) post_speechandtextanalytics_programs_publishjobs(body)



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
| **body** | [**ProgramJobRequest**](ProgramJobRequest.html)| The publish programs job to create |  |
{: class="table table-striped"}

### Return type

[**ProgramJob**](ProgramJob.html)

<a name="post_speechandtextanalytics_topics"></a>

## [**Topic**](Topic.html) post_speechandtextanalytics_topics(body)



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
| **body** | [**TopicRequest**](TopicRequest.html)| The topic to create |  |
{: class="table table-striped"}

### Return type

[**Topic**](Topic.html)

<a name="post_speechandtextanalytics_topics_publishjobs"></a>

## [**TopicJob**](TopicJob.html) post_speechandtextanalytics_topics_publishjobs(body)



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
| **body** | [**TopicJobRequest**](TopicJobRequest.html)| The publish topics job to create |  |
{: class="table table-striped"}

### Return type

[**TopicJob**](TopicJob.html)

<a name="post_speechandtextanalytics_transcripts_search"></a>

## [**JsonSearchResponse**](JsonSearchResponse.html) post_speechandtextanalytics_transcripts_search(body)



Search resources.



Wraps POST /api/v2/speechandtextanalytics/transcripts/search 

Requires ANY permissions: 

* analytics:conversationDetail:view
* recording:recording:view

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
| **body** | [**TranscriptSearchRequest**](TranscriptSearchRequest.html)| Search request options |  |
{: class="table table-striped"}

### Return type

[**JsonSearchResponse**](JsonSearchResponse.html)

<a name="put_speechandtextanalytics_program"></a>

## [**Program**](Program.html) put_speechandtextanalytics_program(program_id, body)



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
| **body** | [**ProgramRequest**](ProgramRequest.html)| The program to update |  |
{: class="table table-striped"}

### Return type

[**Program**](Program.html)

<a name="put_speechandtextanalytics_topic"></a>

## [**Topic**](Topic.html) put_speechandtextanalytics_topic(topic_id, body)



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
| **body** | [**TopicRequest**](TopicRequest.html)| The topic to update |  |
{: class="table table-striped"}

### Return type

[**Topic**](Topic.html)


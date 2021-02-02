---
title: SpeechTextAnalyticsApi
---

## PureCloudPlatformClientV2.SpeechTextAnalyticsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_speechandtextanalytics_conversation**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_conversation) | Get Speech and Text Analytics for a specific conversation|
|[**get_speechandtextanalytics_conversation_communication_transcripturl**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_conversation_communication_transcripturl) | Get the pre-signed S3 URL for the transcript of a specific communication of a conversation|
|[**get_speechandtextanalytics_settings**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_settings) | Get Speech And Text Analytics Settings|
|[**patch_speechandtextanalytics_settings**](SpeechTextAnalyticsApi.html#patch_speechandtextanalytics_settings) | Patch Speech And Text Analytics Settings|
|[**post_speechandtextanalytics_transcripts_search**](SpeechTextAnalyticsApi.html#post_speechandtextanalytics_transcripts_search) | Search resources.|
{: class="table table-striped"}

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


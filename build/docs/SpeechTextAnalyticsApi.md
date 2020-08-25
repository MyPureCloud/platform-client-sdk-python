---
title: SpeechTextAnalyticsApi
---

## PureCloudPlatformClientV2.SpeechTextAnalyticsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_speechandtextanalytics_conversation_communication_transcripturl**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_conversation_communication_transcripturl) | Get the pre-signed S3 URL for the transcript of a specific communication of a conversation|
{: class="table table-striped"}

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
    print "Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_conversation_communication_transcripturl: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **communication_id** | **str**| Communication ID |  |
{: class="table table-striped"}

### Return type

[**TranscriptUrl**](TranscriptUrl.html)


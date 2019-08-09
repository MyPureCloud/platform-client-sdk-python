---
title: SpeechTextAnalyticsApi
---

## PureCloudPlatformClientV2.SpeechTextAnalyticsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_speechandtextanalytics_program**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_program) | Get a Speech &amp; Text Analytics program by id|
|[**get_speechandtextanalytics_topic**](SpeechTextAnalyticsApi.html#get_speechandtextanalytics_topic) | Get a Speech &amp; Text Analytics topic by id|
|[**post_speechandtextanalytics_topics**](SpeechTextAnalyticsApi.html#post_speechandtextanalytics_topics) | Create new Speech &amp; Text Analytics topic|
{: class="table table-striped"}

<a name="get_speechandtextanalytics_program"></a>

## [**Program**](Program.html) get_speechandtextanalytics_program(program_id)



Get a Speech & Text Analytics program by id



Wraps GET /api/v2/speechandtextanalytics/programs/{programId} 

Requires ANY permissions: 

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
program_id = 'program_id_example' # str | The id of the topic to get

try:
    # Get a Speech & Text Analytics program by id
    api_response = api_instance.get_speechandtextanalytics_program(program_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_program: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **program_id** | **str**| The id of the topic to get |  |
{: class="table table-striped"}

### Return type

[**Program**](Program.html)

<a name="get_speechandtextanalytics_topic"></a>

## [**Topic**](Topic.html) get_speechandtextanalytics_topic(topic_id)



Get a Speech & Text Analytics topic by id



Wraps GET /api/v2/speechandtextanalytics/topics/{topicId} 

Requires ANY permissions: 

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
topic_id = 'topic_id_example' # str | The id of the topic to get

try:
    # Get a Speech & Text Analytics topic by id
    api_response = api_instance.get_speechandtextanalytics_topic(topic_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SpeechTextAnalyticsApi->get_speechandtextanalytics_topic: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| The id of the topic to get |  |
{: class="table table-striped"}

### Return type

[**Topic**](Topic.html)

<a name="post_speechandtextanalytics_topics"></a>

## [**Topic**](Topic.html) post_speechandtextanalytics_topics(body)



Create new Speech & Text Analytics topic



Wraps POST /api/v2/speechandtextanalytics/topics 

Requires ANY permissions: 

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
body = PureCloudPlatformClientV2.CreateTopicRequest() # CreateTopicRequest | The topic to create

try:
    # Create new Speech & Text Analytics topic
    api_response = api_instance.post_speechandtextanalytics_topics(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SpeechTextAnalyticsApi->post_speechandtextanalytics_topics: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateTopicRequest**](CreateTopicRequest.html)| The topic to create |  |
{: class="table table-striped"}

### Return type

[**Topic**](Topic.html)


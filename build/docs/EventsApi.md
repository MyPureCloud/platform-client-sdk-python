---
title: EventsApi
---

## PureCloudPlatformClientV2.EventsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**post_events_conversations**](EventsApi.html#post_events_conversations) | Publish Conversation Batch Events|
|[**post_events_users_presence**](EventsApi.html#post_events_users_presence) | Publish User Presence Status Batch Events|
|[**post_events_users_routingstatus**](EventsApi.html#post_events_users_routingstatus) | Publish Agent Routing Status Batch Events|
{: class="table table-striped"}

<a name="post_events_conversations"></a>

## [**BatchEventResponse**](BatchEventResponse.html) post_events_conversations(body)



Publish Conversation Batch Events



Wraps POST /api/v2/events/conversations 

Requires ANY permissions: 

* conversation:conversation:inject

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.EventsApi()
body = PureCloudPlatformClientV2.BatchConversationEventRequest() # BatchConversationEventRequest | batchRequest

try:
    # Publish Conversation Batch Events
    api_response = api_instance.post_events_conversations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->post_events_conversations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BatchConversationEventRequest**](BatchConversationEventRequest.html)| batchRequest |  |
{: class="table table-striped"}

### Return type

[**BatchEventResponse**](BatchEventResponse.html)

<a name="post_events_users_presence"></a>

## [**BatchEventResponse**](BatchEventResponse.html) post_events_users_presence(body)



Publish User Presence Status Batch Events



Wraps POST /api/v2/events/users/presence 

Requires ANY permissions: 

* presence:userPresence:inject

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.EventsApi()
body = PureCloudPlatformClientV2.BatchUserPresenceEventRequest() # BatchUserPresenceEventRequest | batchRequest

try:
    # Publish User Presence Status Batch Events
    api_response = api_instance.post_events_users_presence(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->post_events_users_presence: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BatchUserPresenceEventRequest**](BatchUserPresenceEventRequest.html)| batchRequest |  |
{: class="table table-striped"}

### Return type

[**BatchEventResponse**](BatchEventResponse.html)

<a name="post_events_users_routingstatus"></a>

## [**BatchEventResponse**](BatchEventResponse.html) post_events_users_routingstatus(body)



Publish Agent Routing Status Batch Events



Wraps POST /api/v2/events/users/routingstatus 

Requires ANY permissions: 

* routing:routingstatus:inject

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.EventsApi()
body = PureCloudPlatformClientV2.BatchUserRoutingStatusEventRequest() # BatchUserRoutingStatusEventRequest | batchRequest

try:
    # Publish Agent Routing Status Batch Events
    api_response = api_instance.post_events_users_routingstatus(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->post_events_users_routingstatus: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BatchUserRoutingStatusEventRequest**](BatchUserRoutingStatusEventRequest.html)| batchRequest |  |
{: class="table table-striped"}

### Return type

[**BatchEventResponse**](BatchEventResponse.html)


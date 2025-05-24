# AgentAssistantsApi

## PureCloudPlatformClientV2.AgentAssistantsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_assistant**](#delete_assistant) | Delete an assistant.|
|[**delete_assistant_queue**](#delete_assistant_queue) | Disassociate a queue from an assistant.|
|[**delete_assistant_queues**](#delete_assistant_queues) | Disassociate the queues from an assistant for the given assistant ID and queue IDs.|
|[**get_assistant**](#get_assistant) | Get an assistant.|
|[**get_assistant_queue**](#get_assistant_queue) | Get queue Information for an assistant.|
|[**get_assistant_queues**](#get_assistant_queues) | Get all the queues associated with an assistant.|
|[**get_assistants**](#get_assistants) | Get all assistants.|
|[**get_assistants_queues**](#get_assistants_queues) | Get all queues assigned to any assistant.|
|[**patch_assistant**](#patch_assistant) | Update an assistant.|
|[**patch_assistant_queues**](#patch_assistant_queues) | Update Queues for an Assistant.|
|[**post_assistants**](#post_assistants) | Create an Assistant.|
|[**put_assistant_queue**](#put_assistant_queue) | Create a queue assistant association.|



## delete_assistant

>  delete_assistant(assistant_id)


Delete an assistant.

Wraps DELETE /api/v2/assistants/{assistantId} 

Requires ALL permissions: 

* assistants:assistant:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentAssistantsApi()
assistant_id = 'assistant_id_example' # str | Assistant ID

try:
    # Delete an assistant.
    api_instance.delete_assistant(assistant_id)
except ApiException as e:
    print("Exception when calling AgentAssistantsApi->delete_assistant: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |

### Return type

void (empty response body)


## delete_assistant_queue

>  delete_assistant_queue(assistant_id, queue_id)


Disassociate a queue from an assistant.

Wraps DELETE /api/v2/assistants/{assistantId}/queues/{queueId} 

Requires ALL permissions: 

* assistants:queue:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentAssistantsApi()
assistant_id = 'assistant_id_example' # str | Assistant ID
queue_id = 'queue_id_example' # str | Queue ID

try:
    # Disassociate a queue from an assistant.
    api_instance.delete_assistant_queue(assistant_id, queue_id)
except ApiException as e:
    print("Exception when calling AgentAssistantsApi->delete_assistant_queue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |
| **queue_id** | **str**| Queue ID |  |

### Return type

void (empty response body)


## delete_assistant_queues

>  delete_assistant_queues(assistant_id, queue_ids=queue_ids)


Disassociate the queues from an assistant for the given assistant ID and queue IDs.

Wraps DELETE /api/v2/assistants/{assistantId}/queues 

Requires ALL permissions: 

* assistants:queue:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentAssistantsApi()
assistant_id = 'assistant_id_example' # str | Assistant ID
queue_ids = 'queue_ids_example' # str | Comma-separated identifiers of the queues that need to be deleted. (optional)

try:
    # Disassociate the queues from an assistant for the given assistant ID and queue IDs.
    api_instance.delete_assistant_queues(assistant_id, queue_ids=queue_ids)
except ApiException as e:
    print("Exception when calling AgentAssistantsApi->delete_assistant_queues: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |
| **queue_ids** | **str**| Comma-separated identifiers of the queues that need to be deleted. | [optional]  |

### Return type

void (empty response body)


## get_assistant

> [**Assistant**](Assistant) get_assistant(assistant_id, expand=expand)


Get an assistant.

Wraps GET /api/v2/assistants/{assistantId} 

Requires ALL permissions: 

* assistants:assistant:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentAssistantsApi()
assistant_id = 'assistant_id_example' # str | Assistant ID
expand = 'expand_example' # str | Which fields, if any, to expand. (optional)

try:
    # Get an assistant.
    api_response = api_instance.get_assistant(assistant_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentAssistantsApi->get_assistant: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |
| **expand** | **str**| Which fields, if any, to expand. | [optional] <br />**Values**: copilot |

### Return type

[**Assistant**](Assistant)


## get_assistant_queue

> [**AssistantQueue**](AssistantQueue) get_assistant_queue(assistant_id, queue_id, expand=expand)


Get queue Information for an assistant.

Wraps GET /api/v2/assistants/{assistantId}/queues/{queueId} 

Requires ALL permissions: 

* assistants:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentAssistantsApi()
assistant_id = 'assistant_id_example' # str | Assistant ID
queue_id = 'queue_id_example' # str | Queue ID
expand = 'expand_example' # str | Which fields, if any, to expand. (optional)

try:
    # Get queue Information for an assistant.
    api_response = api_instance.get_assistant_queue(assistant_id, queue_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentAssistantsApi->get_assistant_queue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |
| **queue_id** | **str**| Queue ID |  |
| **expand** | **str**| Which fields, if any, to expand. | [optional] <br />**Values**: assistant |

### Return type

[**AssistantQueue**](AssistantQueue)


## get_assistant_queues

> [**AssistantQueueListing**](AssistantQueueListing) get_assistant_queues(assistant_id, before=before, after=after, page_size=page_size, expand=expand)


Get all the queues associated with an assistant.

Wraps GET /api/v2/assistants/{assistantId}/queues 

Requires ALL permissions: 

* assistants:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentAssistantsApi()
assistant_id = 'assistant_id_example' # str | Assistant ID
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
expand = 'expand_example' # str | Which fields, if any, to expand. (optional)

try:
    # Get all the queues associated with an assistant.
    api_response = api_instance.get_assistant_queues(assistant_id, before=before, after=after, page_size=page_size, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentAssistantsApi->get_assistant_queues: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **expand** | **str**| Which fields, if any, to expand. | [optional] <br />**Values**: assistant |

### Return type

[**AssistantQueueListing**](AssistantQueueListing)


## get_assistants

> [**AssistantListing**](AssistantListing) get_assistants(before=before, after=after, limit=limit, page_size=page_size, name=name)


Get all assistants.

Wraps GET /api/v2/assistants 

Requires ALL permissions: 

* assistants:assistant:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentAssistantsApi()
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
limit = 'limit_example' # str | Number of entities to return. Maximum of 200. Deprecated in favour of pageSize (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
name = 'name_example' # str | Return the assistant by the given name. (optional)

try:
    # Get all assistants.
    api_response = api_instance.get_assistants(before=before, after=after, limit=limit, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentAssistantsApi->get_assistants: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **limit** | **str**| Number of entities to return. Maximum of 200. Deprecated in favour of pageSize | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **name** | **str**| Return the assistant by the given name. | [optional]  |

### Return type

[**AssistantListing**](AssistantListing)


## get_assistants_queues

> [**AssistantQueueListing**](AssistantQueueListing) get_assistants_queues(before=before, after=after, page_size=page_size, queue_ids=queue_ids, expand=expand)


Get all queues assigned to any assistant.

Wraps GET /api/v2/assistants/queues 

Requires ALL permissions: 

* assistants:queue:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentAssistantsApi()
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
queue_ids = 'queue_ids_example' # str | Comma-separated identifiers of the queues that need to be retrieved. (optional)
expand = 'expand_example' # str | Which fields, if any, to expand. (optional)

try:
    # Get all queues assigned to any assistant.
    api_response = api_instance.get_assistants_queues(before=before, after=after, page_size=page_size, queue_ids=queue_ids, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentAssistantsApi->get_assistants_queues: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **queue_ids** | **str**| Comma-separated identifiers of the queues that need to be retrieved. | [optional]  |
| **expand** | **str**| Which fields, if any, to expand. | [optional] <br />**Values**: assistant |

### Return type

[**AssistantQueueListing**](AssistantQueueListing)


## patch_assistant

> [**Assistant**](Assistant) patch_assistant(assistant_id, body)


Update an assistant.

Wraps PATCH /api/v2/assistants/{assistantId} 

Requires ALL permissions: 

* assistants:assistant:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentAssistantsApi()
assistant_id = 'assistant_id_example' # str | Assistant ID
body = PureCloudPlatformClientV2.Assistant() # Assistant | 

try:
    # Update an assistant.
    api_response = api_instance.patch_assistant(assistant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentAssistantsApi->patch_assistant: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |
| **body** | [**Assistant**](Assistant)|  |  |

### Return type

[**Assistant**](Assistant)


## patch_assistant_queues

> [**AssistantQueueListing**](AssistantQueueListing) patch_assistant_queues(assistant_id, body)


Update Queues for an Assistant.

Wraps PATCH /api/v2/assistants/{assistantId}/queues 

Requires ALL permissions: 

* assistants:queue:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentAssistantsApi()
assistant_id = 'assistant_id_example' # str | Assistant ID
body = [PureCloudPlatformClientV2.AssistantQueue()] # list[AssistantQueue] | 

try:
    # Update Queues for an Assistant.
    api_response = api_instance.patch_assistant_queues(assistant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentAssistantsApi->patch_assistant_queues: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |
| **body** | [**list[AssistantQueue]**](AssistantQueue)|  |  |

### Return type

[**AssistantQueueListing**](AssistantQueueListing)


## post_assistants

> [**Assistant**](Assistant) post_assistants(body)


Create an Assistant.

Wraps POST /api/v2/assistants 

Requires ALL permissions: 

* assistants:assistant:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentAssistantsApi()
body = PureCloudPlatformClientV2.Assistant() # Assistant | 

try:
    # Create an Assistant.
    api_response = api_instance.post_assistants(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentAssistantsApi->post_assistants: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Assistant**](Assistant)|  |  |

### Return type

[**Assistant**](Assistant)


## put_assistant_queue

> [**AssistantQueue**](AssistantQueue) put_assistant_queue(assistant_id, queue_id, body)


Create a queue assistant association.

Wraps PUT /api/v2/assistants/{assistantId}/queues/{queueId} 

Requires ALL permissions: 

* assistants:queue:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AgentAssistantsApi()
assistant_id = 'assistant_id_example' # str | Assistant ID
queue_id = 'queue_id_example' # str | Queue ID
body = PureCloudPlatformClientV2.AssistantQueue() # AssistantQueue | 

try:
    # Create a queue assistant association.
    api_response = api_instance.put_assistant_queue(assistant_id, queue_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentAssistantsApi->put_assistant_queue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **assistant_id** | **str**| Assistant ID |  |
| **queue_id** | **str**| Queue ID |  |
| **body** | [**AssistantQueue**](AssistantQueue)|  |  |

### Return type

[**AssistantQueue**](AssistantQueue)


_PureCloudPlatformClientV2 229.0.0_

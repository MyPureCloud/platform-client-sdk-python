# ProcessAutomationApi

## PureCloudPlatformClientV2.ProcessAutomationApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_processautomation_trigger**](#delete_processautomation_trigger) | Delete a Trigger|
|[**get_processautomation_trigger**](#get_processautomation_trigger) | Retrieve a single Trigger matching id|
|[**get_processautomation_triggers**](#get_processautomation_triggers) | Retrieves all triggers, optionally filtered by query parameters.|
|[**get_processautomation_triggers_topics**](#get_processautomation_triggers_topics) | Get topics available for organization|
|[**post_processautomation_trigger_test**](#post_processautomation_trigger_test) | Test the matching of a Trigger based on provided event body|
|[**post_processautomation_triggers**](#post_processautomation_triggers) | Create a Trigger|
|[**post_processautomation_triggers_topic_test**](#post_processautomation_triggers_topic_test) | Test the matching of all organization Triggers on given topic using provided event body|
|[**put_processautomation_trigger**](#put_processautomation_trigger) | Update a Trigger|



## delete_processautomation_trigger

>  delete_processautomation_trigger(trigger_id)


Delete a Trigger

Wraps DELETE /api/v2/processautomation/triggers/{triggerId} 

Requires ANY permissions: 

* processautomation:trigger:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ProcessAutomationApi()
trigger_id = 'trigger_id_example' # str | triggerId

try:
    # Delete a Trigger
    api_instance.delete_processautomation_trigger(trigger_id)
except ApiException as e:
    print("Exception when calling ProcessAutomationApi->delete_processautomation_trigger: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trigger_id** | **str**| triggerId |  |

### Return type

void (empty response body)


## get_processautomation_trigger

> [**Trigger**](Trigger) get_processautomation_trigger(trigger_id)


Retrieve a single Trigger matching id

Wraps GET /api/v2/processautomation/triggers/{triggerId} 

Requires ANY permissions: 

* processautomation:trigger:edit
* processautomation:trigger:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ProcessAutomationApi()
trigger_id = 'trigger_id_example' # str | triggerId

try:
    # Retrieve a single Trigger matching id
    api_response = api_instance.get_processautomation_trigger(trigger_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessAutomationApi->get_processautomation_trigger: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trigger_id** | **str**| triggerId |  |

### Return type

[**Trigger**](Trigger)


## get_processautomation_triggers

> [**TriggerEntityListing**](TriggerEntityListing) get_processautomation_triggers(before=before, after=after, page_size=page_size, topic_name=topic_name, enabled=enabled, has_delay_by=has_delay_by)


Retrieves all triggers, optionally filtered by query parameters.

Wraps GET /api/v2/processautomation/triggers 

Requires ANY permissions: 

* processautomation:trigger:edit
* processautomation:trigger:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ProcessAutomationApi()
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
topic_name = 'topic_name_example' # str | Topic name(s). Separated by commas (optional)
enabled = True # bool | Boolean indicating desired enabled state of triggers (optional)
has_delay_by = True # bool | Boolean to filter based on delayBySeconds being set in triggers. Default returns all, true returns only those with delayBySeconds set, false returns those without delayBySeconds set. (optional)

try:
    # Retrieves all triggers, optionally filtered by query parameters.
    api_response = api_instance.get_processautomation_triggers(before=before, after=after, page_size=page_size, topic_name=topic_name, enabled=enabled, has_delay_by=has_delay_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessAutomationApi->get_processautomation_triggers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **topic_name** | **str**| Topic name(s). Separated by commas | [optional]  |
| **enabled** | **bool**| Boolean indicating desired enabled state of triggers | [optional]  |
| **has_delay_by** | **bool**| Boolean to filter based on delayBySeconds being set in triggers. Default returns all, true returns only those with delayBySeconds set, false returns those without delayBySeconds set. | [optional]  |

### Return type

[**TriggerEntityListing**](TriggerEntityListing)


## get_processautomation_triggers_topics

> [**TopicCursorEntityListing**](TopicCursorEntityListing) get_processautomation_triggers_topics(before=before, after=after, page_size=page_size)


Get topics available for organization

Wraps GET /api/v2/processautomation/triggers/topics 

Requires ANY permissions: 

* processautomation:trigger:edit
* processautomation:trigger:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ProcessAutomationApi()
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)

try:
    # Get topics available for organization
    api_response = api_instance.get_processautomation_triggers_topics(before=before, after=after, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessAutomationApi->get_processautomation_triggers_topics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |

### Return type

[**TopicCursorEntityListing**](TopicCursorEntityListing)


## post_processautomation_trigger_test

> [**TestModeResults**](TestModeResults) post_processautomation_trigger_test(trigger_id, body=body)


Test the matching of a Trigger based on provided event body

Wraps POST /api/v2/processautomation/triggers/{triggerId}/test 

Requires ANY permissions: 

* processautomation:trigger:test

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ProcessAutomationApi()
trigger_id = 'trigger_id_example' # str | triggerId
body = 'body_example' # str | eventBody (optional)

try:
    # Test the matching of a Trigger based on provided event body
    api_response = api_instance.post_processautomation_trigger_test(trigger_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessAutomationApi->post_processautomation_trigger_test: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trigger_id** | **str**| triggerId |  |
| **body** | **str**| eventBody | [optional]  |

### Return type

[**TestModeResults**](TestModeResults)


## post_processautomation_triggers

> [**Trigger**](Trigger) post_processautomation_triggers(body)


Create a Trigger

Wraps POST /api/v2/processautomation/triggers 

Requires ANY permissions: 

* processautomation:trigger:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ProcessAutomationApi()
body = PureCloudPlatformClientV2.CreateTriggerRequest() # CreateTriggerRequest | Input used to create a Trigger.

try:
    # Create a Trigger
    api_response = api_instance.post_processautomation_triggers(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessAutomationApi->post_processautomation_triggers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateTriggerRequest**](CreateTriggerRequest)| Input used to create a Trigger. |  |

### Return type

[**Trigger**](Trigger)


## post_processautomation_triggers_topic_test

> [**TestModeEventResults**](TestModeEventResults) post_processautomation_triggers_topic_test(topic_name, body=body)


Test the matching of all organization Triggers on given topic using provided event body

Wraps POST /api/v2/processautomation/triggers/topics/{topicName}/test 

Requires ANY permissions: 

* processautomation:trigger:test

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ProcessAutomationApi()
topic_name = 'topic_name_example' # str | topicName
body = 'body_example' # str | eventBody (optional)

try:
    # Test the matching of all organization Triggers on given topic using provided event body
    api_response = api_instance.post_processautomation_triggers_topic_test(topic_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessAutomationApi->post_processautomation_triggers_topic_test: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_name** | **str**| topicName |  |
| **body** | **str**| eventBody | [optional]  |

### Return type

[**TestModeEventResults**](TestModeEventResults)


## put_processautomation_trigger

> [**Trigger**](Trigger) put_processautomation_trigger(trigger_id, body)


Update a Trigger

Wraps PUT /api/v2/processautomation/triggers/{triggerId} 

Requires ANY permissions: 

* processautomation:trigger:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ProcessAutomationApi()
trigger_id = 'trigger_id_example' # str | triggerId
body = PureCloudPlatformClientV2.UpdateTriggerRequest() # UpdateTriggerRequest | Input to update Trigger. (topicName cannot be updated, a new trigger must be created to use a new topicName)

try:
    # Update a Trigger
    api_response = api_instance.put_processautomation_trigger(trigger_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessAutomationApi->put_processautomation_trigger: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trigger_id** | **str**| triggerId |  |
| **body** | [**UpdateTriggerRequest**](UpdateTriggerRequest)| Input to update Trigger. (topicName cannot be updated, a new trigger must be created to use a new topicName) |  |

### Return type

[**Trigger**](Trigger)


_PureCloudPlatformClientV2 245.0.0_

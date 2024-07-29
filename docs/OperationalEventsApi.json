---
title: OperationalEventsApi
---

## PureCloudPlatformClientV2.OperationalEventsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_usage_events_definition**](OperationalEventsApi.html#get_usage_events_definition) | Get an operational event definition by its id|
|[**get_usage_events_definitions**](OperationalEventsApi.html#get_usage_events_definitions) | Get all operational event definitions|
{: class="table table-striped"}

<a name="get_usage_events_definition"></a>

## [**EventDefinition**](EventDefinition.html) get_usage_events_definition(event_definition_id)



Get an operational event definition by its id

Wraps GET /api/v2/usage/events/definitions/{eventDefinitionId} 

Requires ALL permissions: 

* usage:events:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OperationalEventsApi()
event_definition_id = 'event_definition_id_example' # str | EventDefinition id

try:
    # Get an operational event definition by its id
    api_response = api_instance.get_usage_events_definition(event_definition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationalEventsApi->get_usage_events_definition: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **event_definition_id** | **str**| EventDefinition id |  |
{: class="table table-striped"}

### Return type

[**EventDefinition**](EventDefinition.html)

<a name="get_usage_events_definitions"></a>

## [**EventDefinitionListing**](EventDefinitionListing.html) get_usage_events_definitions()



Get all operational event definitions

Wraps GET /api/v2/usage/events/definitions 

Requires ALL permissions: 

* usage:events:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.OperationalEventsApi()

try:
    # Get all operational event definitions
    api_response = api_instance.get_usage_events_definitions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationalEventsApi->get_usage_events_definitions: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**EventDefinitionListing**](EventDefinitionListing.html)


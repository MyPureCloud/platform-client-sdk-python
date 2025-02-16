# OperationalEventsApi

## PureCloudPlatformClientV2.OperationalEventsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_usage_events_definition**](#get_usage_events_definition) | Get an operational event definition by its id|
|[**get_usage_events_definitions**](#get_usage_events_definitions) | Get all operational event definitions|
|[**post_usage_events_aggregates_query**](#post_usage_events_aggregates_query) | Get aggregates for operational events in a timeframe.|
|[**post_usage_events_query**](#post_usage_events_query) | Query operational events in a timeframe.|



## get_usage_events_definition

> [**EventDefinition**](EventDefinition) get_usage_events_definition(event_definition_id)


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

### Return type

[**EventDefinition**](EventDefinition)


## get_usage_events_definitions

> [**EventDefinitionListing**](EventDefinitionListing) get_usage_events_definitions()


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

[**EventDefinitionListing**](EventDefinitionListing)


## post_usage_events_aggregates_query

> [**EventAggregatesResponse**](EventAggregatesResponse) post_usage_events_aggregates_query(body=body)


Get aggregates for operational events in a timeframe.

Wraps POST /api/v2/usage/events/aggregates/query 

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
body = PureCloudPlatformClientV2.EventAggregatesQueryRequest() # EventAggregatesQueryRequest |  (optional)

try:
    # Get aggregates for operational events in a timeframe.
    api_response = api_instance.post_usage_events_aggregates_query(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationalEventsApi->post_usage_events_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EventAggregatesQueryRequest**](EventAggregatesQueryRequest)|  | [optional]  |

### Return type

[**EventAggregatesResponse**](EventAggregatesResponse)


## post_usage_events_query

> [**EventQueryResponse**](EventQueryResponse) post_usage_events_query(before=before, after=after, page_size=page_size, body=body)


Query operational events in a timeframe.

Wraps POST /api/v2/usage/events/query 

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
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
body = PureCloudPlatformClientV2.EventQueryRequest() # EventQueryRequest |  (optional)

try:
    # Query operational events in a timeframe.
    api_response = api_instance.post_usage_events_query(before=before, after=after, page_size=page_size, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationalEventsApi->post_usage_events_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **body** | [**EventQueryRequest**](EventQueryRequest)|  | [optional]  |

### Return type

[**EventQueryResponse**](EventQueryResponse)


_PureCloudPlatformClientV2 222.0.0_

---
title: JourneyApi
---

## PureCloudPlatformClientV2.JourneyApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_journey_session_events**](JourneyApi.html#get_journey_session_events) | Retrieve all events for a given session.|
{: class="table table-striped"}

<a name="get_journey_session_events"></a>

## [**EventListing**](EventListing.html) get_journey_session_events(session_id, before=before, after=after, limit=limit)



Retrieve all events for a given session.



Wraps GET /api/v2/journey/sessions/{sessionId}/events 

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
api_instance = PureCloudPlatformClientV2.JourneyApi()
session_id = 'session_id_example' # str | System-generated UUID that represents the session the event is a part of.
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
limit = 'limit_example' # str | Number of entities to return. Maximum of 200. (optional)

try:
    # Retrieve all events for a given session.
    api_response = api_instance.get_journey_session_events(session_id, before=before, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JourneyApi->get_journey_session_events: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **session_id** | **str**| System-generated UUID that represents the session the event is a part of. |  |
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **limit** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
{: class="table table-striped"}

### Return type

[**EventListing**](EventListing.html)


# ScreenMonitoringApi

## PureCloudPlatformClientV2.ScreenMonitoringApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_conversation_participant_screenmonitors_session**](#delete_conversation_participant_screenmonitors_session) | Stop a conversation-level screen monitoring session.|
|[**delete_user_screenmonitors_session**](#delete_user_screenmonitors_session) | Stop an agent-level screen monitoring session.|
|[**get_conversation_participant_screenmonitors_session**](#get_conversation_participant_screenmonitors_session) | Get a conversation-level screen monitoring session object using the supplied screenMonitoringId.|
|[**get_screenmonitors_sessions_details**](#get_screenmonitors_sessions_details) | Get the details of all screen monitoring sessions for the current organization.|
|[**get_screenmonitors_settings**](#get_screenmonitors_settings) | Get the Screen Monitor Settings for the Organization|
|[**get_screenmonitors_user_sessions**](#get_screenmonitors_user_sessions) | Get all screen monitoring sessions for the supplied userId.|
|[**get_user_screenmonitors_session**](#get_user_screenmonitors_session) | Get an agent-level screen monitoring session object using the supplied screenMonitoringId.|
|[**post_conversation_participant_screenmonitors_sessions**](#post_conversation_participant_screenmonitors_sessions) | Start a conversation-level screen monitoring session.|
|[**post_screenmonitors_sessions_users_details**](#post_screenmonitors_sessions_users_details) | Get screen monitor session details for one or more users.|
|[**post_user_screenmonitors_sessions**](#post_user_screenmonitors_sessions) | Start an agent-level screen monitoring session.|
|[**put_screenmonitors_settings**](#put_screenmonitors_settings) | Update the Screen Monitor Settings for the Organization|



## delete_conversation_participant_screenmonitors_session

>  delete_conversation_participant_screenmonitors_session(conversation_id, participant_id, screen_monitoring_id)


Stop a conversation-level screen monitoring session.

Wraps DELETE /api/v2/conversations/{conversationId}/participants/{participantId}/screenmonitors/sessions/{screenMonitoringId} 

Requires ANY permissions: 

* realtimeMonitor:screen:monitorConversation

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScreenMonitoringApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
participant_id = 'participant_id_example' # str | Participant ID
screen_monitoring_id = 'screen_monitoring_id_example' # str | Screen Monitoring ID

try:
    # Stop a conversation-level screen monitoring session.
    api_instance.delete_conversation_participant_screenmonitors_session(conversation_id, participant_id, screen_monitoring_id)
except ApiException as e:
    print("Exception when calling ScreenMonitoringApi->delete_conversation_participant_screenmonitors_session: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **participant_id** | **str**| Participant ID |  |
| **screen_monitoring_id** | **str**| Screen Monitoring ID |  |

### Return type

void (empty response body)


## delete_user_screenmonitors_session

>  delete_user_screenmonitors_session(user_id, screen_monitoring_id)


Stop an agent-level screen monitoring session.

Wraps DELETE /api/v2/users/{userId}/screenmonitors/sessions/{screenMonitoringId} 

Requires ANY permissions: 

* realtimeMonitor:screen:monitorAgent

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScreenMonitoringApi()
user_id = 'user_id_example' # str | User ID
screen_monitoring_id = 'screen_monitoring_id_example' # str | Screen Monitoring ID

try:
    # Stop an agent-level screen monitoring session.
    api_instance.delete_user_screenmonitors_session(user_id, screen_monitoring_id)
except ApiException as e:
    print("Exception when calling ScreenMonitoringApi->delete_user_screenmonitors_session: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **screen_monitoring_id** | **str**| Screen Monitoring ID |  |

### Return type

void (empty response body)


## get_conversation_participant_screenmonitors_session

> [**ScreenMonitoringSession**](ScreenMonitoringSession) get_conversation_participant_screenmonitors_session(conversation_id, participant_id, screen_monitoring_id)


Get a conversation-level screen monitoring session object using the supplied screenMonitoringId.

Wraps GET /api/v2/conversations/{conversationId}/participants/{participantId}/screenmonitors/sessions/{screenMonitoringId} 

Requires ANY permissions: 

* realtimeMonitor:screen:monitorConversation

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScreenMonitoringApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
participant_id = 'participant_id_example' # str | Participant ID
screen_monitoring_id = 'screen_monitoring_id_example' # str | Screen Monitoring ID

try:
    # Get a conversation-level screen monitoring session object using the supplied screenMonitoringId.
    api_response = api_instance.get_conversation_participant_screenmonitors_session(conversation_id, participant_id, screen_monitoring_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenMonitoringApi->get_conversation_participant_screenmonitors_session: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **participant_id** | **str**| Participant ID |  |
| **screen_monitoring_id** | **str**| Screen Monitoring ID |  |

### Return type

[**ScreenMonitoringSession**](ScreenMonitoringSession)


## get_screenmonitors_sessions_details

> [**ScreenMonitoringDetails**](ScreenMonitoringDetails) get_screenmonitors_sessions_details()


Get the details of all screen monitoring sessions for the current organization.

Wraps GET /api/v2/screenmonitors/sessions/details 

Requires ANY permissions: 

* realtimeMonitor:screenSession:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScreenMonitoringApi()

try:
    # Get the details of all screen monitoring sessions for the current organization.
    api_response = api_instance.get_screenmonitors_sessions_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenMonitoringApi->get_screenmonitors_sessions_details: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**ScreenMonitoringDetails**](ScreenMonitoringDetails)


## get_screenmonitors_settings

> [**ScreenMonitorSettings**](ScreenMonitorSettings) get_screenmonitors_settings()


Get the Screen Monitor Settings for the Organization

Wraps GET /api/v2/screenmonitors/settings 

Requires ANY permissions: 

* realtimeMonitor:settings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScreenMonitoringApi()

try:
    # Get the Screen Monitor Settings for the Organization
    api_response = api_instance.get_screenmonitors_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenMonitoringApi->get_screenmonitors_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**ScreenMonitorSettings**](ScreenMonitorSettings)


## get_screenmonitors_user_sessions

> [**ScreenMonitoringSessionEntityListing**](ScreenMonitoringSessionEntityListing) get_screenmonitors_user_sessions(user_id)


Get all screen monitoring sessions for the supplied userId.

Wraps GET /api/v2/screenmonitors/users/{userId}/sessions 

Requires ANY permissions: 

* realtimeMonitor:screen:monitorConversation
* realtimeMonitor:screen:monitorAgent

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScreenMonitoringApi()
user_id = 'user_id_example' # str | User ID

try:
    # Get all screen monitoring sessions for the supplied userId.
    api_response = api_instance.get_screenmonitors_user_sessions(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenMonitoringApi->get_screenmonitors_user_sessions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |

### Return type

[**ScreenMonitoringSessionEntityListing**](ScreenMonitoringSessionEntityListing)


## get_user_screenmonitors_session

> [**ScreenMonitoringSession**](ScreenMonitoringSession) get_user_screenmonitors_session(user_id, screen_monitoring_id)


Get an agent-level screen monitoring session object using the supplied screenMonitoringId.

Wraps GET /api/v2/users/{userId}/screenmonitors/sessions/{screenMonitoringId} 

Requires ANY permissions: 

* realtimeMonitor:screen:monitorAgent

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScreenMonitoringApi()
user_id = 'user_id_example' # str | User ID
screen_monitoring_id = 'screen_monitoring_id_example' # str | Screen Monitoring ID

try:
    # Get an agent-level screen monitoring session object using the supplied screenMonitoringId.
    api_response = api_instance.get_user_screenmonitors_session(user_id, screen_monitoring_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenMonitoringApi->get_user_screenmonitors_session: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **screen_monitoring_id** | **str**| Screen Monitoring ID |  |

### Return type

[**ScreenMonitoringSession**](ScreenMonitoringSession)


## post_conversation_participant_screenmonitors_sessions

> [**StartScreenMonitorResponseBody**](StartScreenMonitorResponseBody) post_conversation_participant_screenmonitors_sessions(conversation_id, participant_id)


Start a conversation-level screen monitoring session.

Wraps POST /api/v2/conversations/{conversationId}/participants/{participantId}/screenmonitors/sessions 

Requires ANY permissions: 

* realtimeMonitor:screen:monitorConversation

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScreenMonitoringApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
participant_id = 'participant_id_example' # str | Participant ID

try:
    # Start a conversation-level screen monitoring session.
    api_response = api_instance.post_conversation_participant_screenmonitors_sessions(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenMonitoringApi->post_conversation_participant_screenmonitors_sessions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **participant_id** | **str**| Participant ID |  |

### Return type

[**StartScreenMonitorResponseBody**](StartScreenMonitorResponseBody)


## post_screenmonitors_sessions_users_details

> [**ScreenMonitoringUserDetailsEntityListing**](ScreenMonitoringUserDetailsEntityListing) post_screenmonitors_sessions_users_details(body)


Get screen monitor session details for one or more users.

Wraps POST /api/v2/screenmonitors/sessions/users/details 

Requires ANY permissions: 

* realtimeMonitor:screenSession:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScreenMonitoringApi()
body = ['body_example'] # list[str] | List of target user IDs

try:
    # Get screen monitor session details for one or more users.
    api_response = api_instance.post_screenmonitors_sessions_users_details(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenMonitoringApi->post_screenmonitors_sessions_users_details: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**list[str]**](str)| List of target user IDs |  |

### Return type

[**ScreenMonitoringUserDetailsEntityListing**](ScreenMonitoringUserDetailsEntityListing)


## post_user_screenmonitors_sessions

> [**StartScreenMonitorResponseBody**](StartScreenMonitorResponseBody) post_user_screenmonitors_sessions(user_id)


Start an agent-level screen monitoring session.

Wraps POST /api/v2/users/{userId}/screenmonitors/sessions 

Requires ANY permissions: 

* realtimeMonitor:screen:monitorAgent

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScreenMonitoringApi()
user_id = 'user_id_example' # str | User ID

try:
    # Start an agent-level screen monitoring session.
    api_response = api_instance.post_user_screenmonitors_sessions(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenMonitoringApi->post_user_screenmonitors_sessions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |

### Return type

[**StartScreenMonitorResponseBody**](StartScreenMonitorResponseBody)


## put_screenmonitors_settings

>  put_screenmonitors_settings(body)


Update the Screen Monitor Settings for the Organization

Wraps PUT /api/v2/screenmonitors/settings 

Requires ANY permissions: 

* realtimeMonitor:settings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ScreenMonitoringApi()
body = PureCloudPlatformClientV2.ScreenMonitorSettings() # ScreenMonitorSettings | Screen Monitor settings

try:
    # Update the Screen Monitor Settings for the Organization
    api_instance.put_screenmonitors_settings(body)
except ApiException as e:
    print("Exception when calling ScreenMonitoringApi->put_screenmonitors_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ScreenMonitorSettings**](ScreenMonitorSettings)| Screen Monitor settings |  |

### Return type

void (empty response body)


_PureCloudPlatformClientV2 264.0.0_

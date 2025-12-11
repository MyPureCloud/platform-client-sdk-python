# TelephonyApi

## PureCloudPlatformClientV2.TelephonyApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_telephony_agent_greetings**](#get_telephony_agent_greetings) | Get an agent&#39;s greetings.|
|[**get_telephony_agents_greetings_me**](#get_telephony_agents_greetings_me) | Get the agent&#39;s own greetings.|
|[**get_telephony_mediaregions**](#get_telephony_mediaregions) | Retrieve the list of AWS regions media can stream through.|
|[**get_telephony_sipmessages_conversation**](#get_telephony_sipmessages_conversation) | Get a SIP message.|
|[**get_telephony_sipmessages_conversation_headers**](#get_telephony_sipmessages_conversation_headers) | Get SIP headers.|
|[**get_telephony_siptraces**](#get_telephony_siptraces) | Fetch SIP metadata|
|[**get_telephony_siptraces_download_download_id**](#get_telephony_siptraces_download_download_id) | Get signed S3 URL for a pcap download|
|[**post_telephony_siptraces_download**](#post_telephony_siptraces_download) | Request a download of a pcap file to S3|
|[**put_telephony_agent_greetings**](#put_telephony_agent_greetings) | Updates an agent&#39;s greetings.|
|[**put_telephony_agents_greetings_me**](#put_telephony_agents_greetings_me) | Updates the agent&#39;s own greetings.|



## get_telephony_agent_greetings

> [**AgentGreeting**](AgentGreeting) get_telephony_agent_greetings(agent_id)


Get an agent's greetings.

get_telephony_agent_greetings is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/telephony/agents/{agentId}/greetings 

Requires ANY permissions: 

* telephony:otherAgentGreeting:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
agent_id = 'agent_id_example' # str | User ID

try:
    # Get an agent's greetings.
    api_response = api_instance.get_telephony_agent_greetings(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_agent_greetings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| User ID |  |

### Return type

[**AgentGreeting**](AgentGreeting)


## get_telephony_agents_greetings_me

> [**SelfAgentGreeting**](SelfAgentGreeting) get_telephony_agents_greetings_me()


Get the agent's own greetings.

get_telephony_agents_greetings_me is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/telephony/agents/greetings/me 

Requires ANY permissions: 

* telephony:selfAgentGreeting:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()

try:
    # Get the agent's own greetings.
    api_response = api_instance.get_telephony_agents_greetings_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_agents_greetings_me: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**SelfAgentGreeting**](SelfAgentGreeting)


## get_telephony_mediaregions

> [**MediaRegions**](MediaRegions) get_telephony_mediaregions()


Retrieve the list of AWS regions media can stream through.

Wraps GET /api/v2/telephony/mediaregions 

Requires ANY permissions: 

* telephony:plugin:all

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()

try:
    # Retrieve the list of AWS regions media can stream through.
    api_response = api_instance.get_telephony_mediaregions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_mediaregions: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**MediaRegions**](MediaRegions)


## get_telephony_sipmessages_conversation

> [**Callmessage**](Callmessage) get_telephony_sipmessages_conversation(conversation_id)


Get a SIP message.

Get the raw form of the SIP message

Wraps GET /api/v2/telephony/sipmessages/conversations/{conversationId} 

Requires ALL permissions: 

* telephony:pcap:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
conversation_id = 'conversation_id_example' # str | Conversation id

try:
    # Get a SIP message.
    api_response = api_instance.get_telephony_sipmessages_conversation(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_sipmessages_conversation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation id |  |

### Return type

[**Callmessage**](Callmessage)


## get_telephony_sipmessages_conversation_headers

> [**Callheader**](Callheader) get_telephony_sipmessages_conversation_headers(conversation_id, keys=keys)


Get SIP headers.

Get parsed SIP headers. Returns specific headers if key query parameters are added.

Wraps GET /api/v2/telephony/sipmessages/conversations/{conversationId}/headers 

Requires ALL permissions: 

* telephony:pcap:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
conversation_id = 'conversation_id_example' # str | Conversation id
keys = ['keys_example'] # list[str] | comma-separated list of header identifiers to query. e.g. ruri,to,from (optional)

try:
    # Get SIP headers.
    api_response = api_instance.get_telephony_sipmessages_conversation_headers(conversation_id, keys=keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_sipmessages_conversation_headers: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation id |  |
| **keys** | [**list[str]**](str)| comma-separated list of header identifiers to query. e.g. ruri,to,from | [optional]  |

### Return type

[**Callheader**](Callheader)


## get_telephony_siptraces

> [**SipSearchResult**](SipSearchResult) get_telephony_siptraces(date_start, date_end, call_id=call_id, to_user=to_user, from_user=from_user, conversation_id=conversation_id)


Fetch SIP metadata

Fetch SIP metadata that matches a given parameter. If exactMatch is passed as a parameter only sip records that have exactly that value will be returned. For example, some records contain conversationId but not all relevant records for that call may contain the conversationId so only a partial view of the call will be reflected

Wraps GET /api/v2/telephony/siptraces 

Requires ALL permissions: 

* telephony:pcap:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
date_start = '2013-10-20T19:20:30+01:00' # datetime | Start date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
date_end = '2013-10-20T19:20:30+01:00' # datetime | End date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
call_id = 'call_id_example' # str | unique identification of the placed call (optional)
to_user = 'to_user_example' # str | User to who the call was placed (optional)
from_user = 'from_user_example' # str | user who placed the call (optional)
conversation_id = 'conversation_id_example' # str | Unique identification of the conversation (optional)

try:
    # Fetch SIP metadata
    api_response = api_instance.get_telephony_siptraces(date_start, date_end, call_id=call_id, to_user=to_user, from_user=from_user, conversation_id=conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_siptraces: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **date_start** | **datetime**| Start date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z |  |
| **date_end** | **datetime**| End date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z |  |
| **call_id** | **str**| unique identification of the placed call | [optional]  |
| **to_user** | **str**| User to who the call was placed | [optional]  |
| **from_user** | **str**| user who placed the call | [optional]  |
| **conversation_id** | **str**| Unique identification of the conversation | [optional]  |

### Return type

[**SipSearchResult**](SipSearchResult)


## get_telephony_siptraces_download_download_id

> [**SignedUrlResponse**](SignedUrlResponse) get_telephony_siptraces_download_download_id(download_id)


Get signed S3 URL for a pcap download

Wraps GET /api/v2/telephony/siptraces/download/{downloadId} 

Requires ALL permissions: 

* telephony:pcap:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
download_id = 'download_id_example' # str | unique id for the downloaded file in S3

try:
    # Get signed S3 URL for a pcap download
    api_response = api_instance.get_telephony_siptraces_download_download_id(download_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_siptraces_download_download_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **download_id** | **str**| unique id for the downloaded file in S3 |  |

### Return type

[**SignedUrlResponse**](SignedUrlResponse)


## post_telephony_siptraces_download

> [**SipDownloadResponse**](SipDownloadResponse) post_telephony_siptraces_download(sip_search_public_request)


Request a download of a pcap file to S3

Wraps POST /api/v2/telephony/siptraces/download 

Requires ALL permissions: 

* telephony:pcap:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
sip_search_public_request = PureCloudPlatformClientV2.SIPSearchPublicRequest() # SIPSearchPublicRequest | 

try:
    # Request a download of a pcap file to S3
    api_response = api_instance.post_telephony_siptraces_download(sip_search_public_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->post_telephony_siptraces_download: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sip_search_public_request** | [**SIPSearchPublicRequest**](SIPSearchPublicRequest)|  |  |

### Return type

[**SipDownloadResponse**](SipDownloadResponse)


## put_telephony_agent_greetings

> [**AgentGreeting**](AgentGreeting) put_telephony_agent_greetings(agent_id, body)


Updates an agent's greetings.

put_telephony_agent_greetings is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PUT /api/v2/telephony/agents/{agentId}/greetings 

Requires ANY permissions: 

* telephony:otherAgentGreeting:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
agent_id = 'agent_id_example' # str | User ID
body = PureCloudPlatformClientV2.AgentGreeting() # AgentGreeting | Agent Greeting

try:
    # Updates an agent's greetings.
    api_response = api_instance.put_telephony_agent_greetings(agent_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->put_telephony_agent_greetings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| User ID |  |
| **body** | [**AgentGreeting**](AgentGreeting)| Agent Greeting |  |

### Return type

[**AgentGreeting**](AgentGreeting)


## put_telephony_agents_greetings_me

> [**SelfAgentGreeting**](SelfAgentGreeting) put_telephony_agents_greetings_me(body)


Updates the agent's own greetings.

put_telephony_agents_greetings_me is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PUT /api/v2/telephony/agents/greetings/me 

Requires ANY permissions: 

* telephony:selfAgentGreeting:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
body = PureCloudPlatformClientV2.SelfAgentGreeting() # SelfAgentGreeting | Agent Greeting

try:
    # Updates the agent's own greetings.
    api_response = api_instance.put_telephony_agents_greetings_me(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->put_telephony_agents_greetings_me: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SelfAgentGreeting**](SelfAgentGreeting)| Agent Greeting |  |

### Return type

[**SelfAgentGreeting**](SelfAgentGreeting)


_PureCloudPlatformClientV2 246.0.0_

# TelephonyApi

## PureCloudPlatformClientV2.TelephonyApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_telephony_organization_link_target_organization_id**](#delete_telephony_organization_link_target_organization_id) | Delete a link|
|[**get_telephony_agent_greetings**](#get_telephony_agent_greetings) | Get an agent&#39;s greetings.|
|[**get_telephony_agents_greetings_me**](#get_telephony_agents_greetings_me) | Get the agent&#39;s own greetings.|
|[**get_telephony_calls_metrics**](#get_telephony_calls_metrics) | Get the concurrent call metrics for a given organization.|
|[**get_telephony_mediaregions**](#get_telephony_mediaregions) | Retrieve the list of AWS regions media can stream through.|
|[**get_telephony_numbers_routing**](#get_telephony_numbers_routing) | Get Number Routings by organizationId|
|[**get_telephony_organization_link**](#get_telephony_organization_link) | Get organization links|
|[**get_telephony_organization_link_regions**](#get_telephony_organization_link_regions) | Get all the replica regions by primary region|
|[**get_telephony_settings**](#get_telephony_settings) | Get the global telephony configuration.|
|[**get_telephony_sipmessages_conversation**](#get_telephony_sipmessages_conversation) | Get a SIP message.|
|[**get_telephony_sipmessages_conversation_headers**](#get_telephony_sipmessages_conversation_headers) | Get SIP headers.|
|[**get_telephony_siptraces**](#get_telephony_siptraces) | Fetch SIP metadata|
|[**get_telephony_siptraces_download_download_id**](#get_telephony_siptraces_download_download_id) | Get signed S3 URL for a pcap download|
|[**patch_telephony_organization_link_approve_requesting_organization_id**](#patch_telephony_organization_link_approve_requesting_organization_id) | Approving a requested link|
|[**post_telephony_numbers_routing**](#post_telephony_numbers_routing) | Update the routing of numbers for one or multiple organizations|
|[**post_telephony_numbers_routing_all**](#post_telephony_numbers_routing_all) | Re-route all numbers on an organization|
|[**post_telephony_numbers_routing_reset**](#post_telephony_numbers_routing_reset) | Reset routing for organization|
|[**post_telephony_organization_link**](#post_telephony_organization_link) | Create a link with an organization|
|[**post_telephony_siptraces_download**](#post_telephony_siptraces_download) | Request a download of a pcap file to S3|
|[**put_telephony_agent_greetings**](#put_telephony_agent_greetings) | Updates an agent&#39;s greetings.|
|[**put_telephony_agents_greetings_me**](#put_telephony_agents_greetings_me) | Updates the agent&#39;s own greetings.|
|[**put_telephony_settings**](#put_telephony_settings) | Update the global telephony configuration.|



## delete_telephony_organization_link_target_organization_id

>  delete_telephony_organization_link_target_organization_id(target_organization_id)


Delete a link

Wraps DELETE /api/v2/telephony/organization/link/{targetOrganizationId} 

Requires ALL permissions: 

* telephony:organizationLink:delete

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
target_organization_id = 'target_organization_id_example' # str | targetOrganizationId

try:
    # Delete a link
    api_instance.delete_telephony_organization_link_target_organization_id(target_organization_id)
except ApiException as e:
    print("Exception when calling TelephonyApi->delete_telephony_organization_link_target_organization_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **target_organization_id** | **str**| targetOrganizationId |  |

### Return type

void (empty response body)


## get_telephony_agent_greetings

> [**AgentGreeting**](AgentGreeting) get_telephony_agent_greetings(agent_id)


Get an agent's greetings.

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


## get_telephony_calls_metrics

> [**OrganizationCallMetrics**](OrganizationCallMetrics) get_telephony_calls_metrics(metric_type=metric_type)


Get the concurrent call metrics for a given organization.

Wraps GET /api/v2/telephony/calls/metrics 

Requires ANY permissions: 

* telephony:callMetrics:view

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
metric_type = ''cloud'' # str | Flag to indicate metric type to fetch. (optional) (default to 'cloud')

try:
    # Get the concurrent call metrics for a given organization.
    api_response = api_instance.get_telephony_calls_metrics(metric_type=metric_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_calls_metrics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **metric_type** | **str**| Flag to indicate metric type to fetch. | [optional] [default to &#39;cloud&#39;]<br />**Values**: cloud, premises |

### Return type

[**OrganizationCallMetrics**](OrganizationCallMetrics)


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


## get_telephony_numbers_routing

> [**NumberRoutingListing**](NumberRoutingListing) get_telephony_numbers_routing(before=before, after=after, page_size=page_size, number_id=number_id, active_routing_organization_id=active_routing_organization_id, owner_organization_id=owner_organization_id, status=status)


Get Number Routings by organizationId

Wraps GET /api/v2/telephony/numbers/routing 

Requires ALL permissions: 

* telephony:numberRouting:view

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
before = 'before_example' # str | The cursor that points to the start of the set of entities that has been returned. (optional)
after = 'after_example' # str | The cursor that points to the end of the set of entities that has been returned. (optional)
page_size = 'page_size_example' # str | Number of entities to return. Maximum of 200. (optional)
number_id = 'number_id_example' # str | numberId (optional)
active_routing_organization_id = 'active_routing_organization_id_example' # str | activeRoutingOrganizationId (optional)
owner_organization_id = 'owner_organization_id_example' # str | ownerOrganizationId (optional)
status = 'status_example' # str | status (optional)

try:
    # Get Number Routings by organizationId
    api_response = api_instance.get_telephony_numbers_routing(before=before, after=after, page_size=page_size, number_id=number_id, active_routing_organization_id=active_routing_organization_id, owner_organization_id=owner_organization_id, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_numbers_routing: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **before** | **str**| The cursor that points to the start of the set of entities that has been returned. | [optional]  |
| **after** | **str**| The cursor that points to the end of the set of entities that has been returned. | [optional]  |
| **page_size** | **str**| Number of entities to return. Maximum of 200. | [optional]  |
| **number_id** | **str**| numberId | [optional]  |
| **active_routing_organization_id** | **str**| activeRoutingOrganizationId | [optional]  |
| **owner_organization_id** | **str**| ownerOrganizationId | [optional]  |
| **status** | **str**| status | [optional] <br />**Values**: Normal, Redirected, Pending |

### Return type

[**NumberRoutingListing**](NumberRoutingListing)


## get_telephony_organization_link

> [**list[OrganizationLinkResponse]**](OrganizationLinkResponse) get_telephony_organization_link()


Get organization links

Wraps GET /api/v2/telephony/organization/link 

Requires ALL permissions: 

* telephony:organizationLink:view

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
    # Get organization links
    api_response = api_instance.get_telephony_organization_link()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_organization_link: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**list[OrganizationLinkResponse]**](OrganizationLinkResponse)


## get_telephony_organization_link_regions

> [**list[RegionResponse]**](RegionResponse) get_telephony_organization_link_regions()


Get all the replica regions by primary region

Wraps GET /api/v2/telephony/organization/link/regions 

Requires ALL permissions: 

* telephony:organizationLink:view

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
    # Get all the replica regions by primary region
    api_response = api_instance.get_telephony_organization_link_regions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_organization_link_regions: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**list[RegionResponse]**](RegionResponse)


## get_telephony_settings

> [**TelephonySettings**](TelephonySettings) get_telephony_settings()


Get the global telephony configuration.

Wraps GET /api/v2/telephony/settings 

Requires ANY permissions: 

* telephony:settings:view

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
    # Get the global telephony configuration.
    api_response = api_instance.get_telephony_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**TelephonySettings**](TelephonySettings)


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


## patch_telephony_organization_link_approve_requesting_organization_id

>  patch_telephony_organization_link_approve_requesting_organization_id(requesting_organization_id, body)


Approving a requested link

Wraps PATCH /api/v2/telephony/organization/link/approve/{requestingOrganizationId} 

Requires ALL permissions: 

* telephony:organizationLink:edit

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
requesting_organization_id = 'requesting_organization_id_example' # str | requestingOrganizationId
body = PureCloudPlatformClientV2.OrganizationLinkApprovalRequest() # OrganizationLinkApprovalRequest | Approval request body

try:
    # Approving a requested link
    api_instance.patch_telephony_organization_link_approve_requesting_organization_id(requesting_organization_id, body)
except ApiException as e:
    print("Exception when calling TelephonyApi->patch_telephony_organization_link_approve_requesting_organization_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **requesting_organization_id** | **str**| requestingOrganizationId |  |
| **body** | [**OrganizationLinkApprovalRequest**](OrganizationLinkApprovalRequest)| Approval request body |  |

### Return type

void (empty response body)


## post_telephony_numbers_routing

>  post_telephony_numbers_routing(body)


Update the routing of numbers for one or multiple organizations

Wraps POST /api/v2/telephony/numbers/routing 

Requires ALL permissions: 

* telephony:numberRouting:edit

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
body = [PureCloudPlatformClientV2.NumberRoutingRequest()] # list[NumberRoutingRequest] | drRoutingList

try:
    # Update the routing of numbers for one or multiple organizations
    api_instance.post_telephony_numbers_routing(body)
except ApiException as e:
    print("Exception when calling TelephonyApi->post_telephony_numbers_routing: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**list[NumberRoutingRequest]**](NumberRoutingRequest)| drRoutingList |  |

### Return type

void (empty response body)


## post_telephony_numbers_routing_all

>  post_telephony_numbers_routing_all(body)


Re-route all numbers on an organization

Wraps POST /api/v2/telephony/numbers/routing/all 

Requires ALL permissions: 

* telephony:numberRouting:edit

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
body = PureCloudPlatformClientV2.DisasterRecoveryAllRoutingRequest() # DisasterRecoveryAllRoutingRequest | Value for all routing request body

try:
    # Re-route all numbers on an organization
    api_instance.post_telephony_numbers_routing_all(body)
except ApiException as e:
    print("Exception when calling TelephonyApi->post_telephony_numbers_routing_all: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DisasterRecoveryAllRoutingRequest**](DisasterRecoveryAllRoutingRequest)| Value for all routing request body |  |

### Return type

void (empty response body)


## post_telephony_numbers_routing_reset

>  post_telephony_numbers_routing_reset(body)


Reset routing for organization

Wraps POST /api/v2/telephony/numbers/routing/reset 

Requires ALL permissions: 

* telephony:numberRouting:edit

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
body = PureCloudPlatformClientV2.NumberRoutingResetOrganizationRequest() # NumberRoutingResetOrganizationRequest | Value for bulk routing request body

try:
    # Reset routing for organization
    api_instance.post_telephony_numbers_routing_reset(body)
except ApiException as e:
    print("Exception when calling TelephonyApi->post_telephony_numbers_routing_reset: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**NumberRoutingResetOrganizationRequest**](NumberRoutingResetOrganizationRequest)| Value for bulk routing request body |  |

### Return type

void (empty response body)


## post_telephony_organization_link

> [**OrganizationLink**](OrganizationLink) post_telephony_organization_link(body)


Create a link with an organization

Wraps POST /api/v2/telephony/organization/link 

Requires ALL permissions: 

* telephony:organizationLink:add

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
body = PureCloudPlatformClientV2.CreateOrganizationLink() # CreateOrganizationLink | CreateLinkOrg body

try:
    # Create a link with an organization
    api_response = api_instance.post_telephony_organization_link(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->post_telephony_organization_link: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateOrganizationLink**](CreateOrganizationLink)| CreateLinkOrg body |  |

### Return type

[**OrganizationLink**](OrganizationLink)


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


## put_telephony_settings

> [**TelephonySettings**](TelephonySettings) put_telephony_settings(body)


Update the global telephony configuration.

Wraps PUT /api/v2/telephony/settings 

Requires ANY permissions: 

* telephony:settings:edit

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
body = PureCloudPlatformClientV2.TelephonySettings() # TelephonySettings | Telephony

try:
    # Update the global telephony configuration.
    api_response = api_instance.put_telephony_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->put_telephony_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TelephonySettings**](TelephonySettings)| Telephony |  |

### Return type

[**TelephonySettings**](TelephonySettings)


_PureCloudPlatformClientV2 262.0.0_

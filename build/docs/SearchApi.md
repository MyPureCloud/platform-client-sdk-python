# SearchApi

## PureCloudPlatformClientV2.SearchApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_documentation_gkn_search**](#get_documentation_gkn_search) | Search gkn documentation using the q64 value returned from a previous search|
|[**get_documentation_search**](#get_documentation_search) | Search documentation using the q64 value returned from a previous search|
|[**get_groups_search**](#get_groups_search) | Search groups using the q64 value returned from a previous search|
|[**get_locations_search**](#get_locations_search) | Search locations using the q64 value returned from a previous search|
|[**get_search**](#get_search) | Search using the q64 value returned from a previous search.|
|[**get_search_suggest**](#get_search_suggest) | Suggest resources using the q64 value returned from a previous suggest query.|
|[**get_telephony_providers_edges_sites_search**](#get_telephony_providers_edges_sites_search) | Search sites using the q64 value returned from a previous search|
|[**get_users_search**](#get_users_search) | Search users using the q64 value returned from a previous search|
|[**get_voicemail_search**](#get_voicemail_search) | Search voicemails using the q64 value returned from a previous search|
|[**post_analytics_conversations_transcripts_query**](#post_analytics_conversations_transcripts_query) | Search resources.|
|[**post_conversations_participants_attributes_search**](#post_conversations_participants_attributes_search) | Search conversations|
|[**post_documentation_all_search**](#post_documentation_all_search) | Search all documents|
|[**post_documentation_gkn_search**](#post_documentation_gkn_search) | Search gkn documentation|
|[**post_documentation_search**](#post_documentation_search) | Search documentation|
|[**post_groups_search**](#post_groups_search) | Search groups|
|[**post_knowledge_knowledgebase_search**](#post_knowledge_knowledgebase_search) | Search Documents|
|[**post_locations_search**](#post_locations_search) | Search locations|
|[**post_search**](#post_search) | Search resources.|
|[**post_search_suggest**](#post_search_suggest) | Suggest resources.|
|[**post_speechandtextanalytics_transcripts_search**](#post_speechandtextanalytics_transcripts_search) | Search resources.|
|[**post_teams_search**](#post_teams_search) | Search resources.|
|[**post_telephony_providers_edges_sites_search**](#post_telephony_providers_edges_sites_search) | Search sites|
|[**post_users_search**](#post_users_search) | Search users|
|[**post_users_search_conversation_target**](#post_users_search_conversation_target) | Search users as conversation targets|
|[**post_users_search_queuemembers_manage**](#post_users_search_queuemembers_manage) | Search manage queue member|
|[**post_users_search_teams_assign**](#post_users_search_teams_assign) | Search users assigned to teams|
|[**post_voicemail_search**](#post_voicemail_search) | Search voicemails|



## get_documentation_gkn_search

> [**GKNDocumentationSearchResponse**](GKNDocumentationSearchResponse) get_documentation_gkn_search(q64)


Search gkn documentation using the q64 value returned from a previous search

Wraps GET /api/v2/documentation/gkn/search 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64

try:
    # Search gkn documentation using the q64 value returned from a previous search
    api_response = api_instance.get_documentation_gkn_search(q64)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_documentation_gkn_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |

### Return type

[**GKNDocumentationSearchResponse**](GKNDocumentationSearchResponse)


## get_documentation_search

> [**DocumentationSearchResponse**](DocumentationSearchResponse) get_documentation_search(q64)


Search documentation using the q64 value returned from a previous search

Wraps GET /api/v2/documentation/search 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64

try:
    # Search documentation using the q64 value returned from a previous search
    api_response = api_instance.get_documentation_search(q64)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_documentation_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |

### Return type

[**DocumentationSearchResponse**](DocumentationSearchResponse)


## get_groups_search

> [**GroupsSearchResponse**](GroupsSearchResponse) get_groups_search(q64, expand=expand)


Search groups using the q64 value returned from a previous search

Wraps GET /api/v2/groups/search 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | expand (optional)

try:
    # Search groups using the q64 value returned from a previous search
    api_response = api_instance.get_groups_search(q64, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_groups_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str)| expand | [optional]  |

### Return type

[**GroupsSearchResponse**](GroupsSearchResponse)


## get_locations_search

> [**LocationsSearchResponse**](LocationsSearchResponse) get_locations_search(q64, expand=expand)


Search locations using the q64 value returned from a previous search

Wraps GET /api/v2/locations/search 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | Provides more details about a specified resource (optional)

try:
    # Search locations using the q64 value returned from a previous search
    api_response = api_instance.get_locations_search(q64, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_locations_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str)| Provides more details about a specified resource | [optional] <br />**Values**: images, addressVerificationDetails |

### Return type

[**LocationsSearchResponse**](LocationsSearchResponse)


## get_search

> [**JsonNodeSearchResponse**](JsonNodeSearchResponse) get_search(q64, expand=expand, profile=profile)


Search using the q64 value returned from a previous search.

Wraps GET /api/v2/search 

Requires ANY permissions: 

* directory:user:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
profile = True # bool | profile (optional) (default to True)

try:
    # Search using the q64 value returned from a previous search.
    api_response = api_instance.get_search(q64, expand=expand, profile=profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, groups, profileSkills, certifications, locations, skills, languages, languagePreference, employerInfo, biography, dateLastLogin, dateWelcomeSent, callerUser.routingStatus, callerUser.primaryPresence, callerUser.conversationSummary, callerUser.outOfOffice, callerUser.geolocation, conversations, transcription, images, addressVerificationDetails |
| **profile** | **bool**| profile | [optional] [default to True] |

### Return type

[**JsonNodeSearchResponse**](JsonNodeSearchResponse)


## get_search_suggest

> [**JsonNodeSearchResponse**](JsonNodeSearchResponse) get_search_suggest(q64, expand=expand, profile=profile)


Suggest resources using the q64 value returned from a previous suggest query.

Wraps GET /api/v2/search/suggest 

Requires ANY permissions: 

* directory:user:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
profile = True # bool | profile (optional) (default to True)

try:
    # Suggest resources using the q64 value returned from a previous suggest query.
    api_response = api_instance.get_search_suggest(q64, expand=expand, profile=profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_search_suggest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, groups, profileSkills, certifications, locations, skills, languages, languagePreference, employerInfo, biography, dateLastLogin, dateWelcomeSent, callerUser.routingStatus, callerUser.primaryPresence, callerUser.conversationSummary, callerUser.outOfOffice, callerUser.geolocation, conversations, transcription, images, addressVerificationDetails |
| **profile** | **bool**| profile | [optional] [default to True] |

### Return type

[**JsonNodeSearchResponse**](JsonNodeSearchResponse)


## get_telephony_providers_edges_sites_search

> [**SitesSearchResponse**](SitesSearchResponse) get_telephony_providers_edges_sites_search(q64, expand=expand)


Search sites using the q64 value returned from a previous search

Wraps GET /api/v2/telephony/providers/edges/sites/search 

Requires ANY permissions: 

* telephony:plugin:all
* telephony:sites:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | expand (optional)

try:
    # Search sites using the q64 value returned from a previous search
    api_response = api_instance.get_telephony_providers_edges_sites_search(q64, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_telephony_providers_edges_sites_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str)| expand | [optional]  |

### Return type

[**SitesSearchResponse**](SitesSearchResponse)


## get_users_search

> [**UsersSearchResponse**](UsersSearchResponse) get_users_search(q64, expand=expand, integration_presence_source=integration_presence_source)


Search users using the q64 value returned from a previous search

Wraps GET /api/v2/users/search 

Requires ANY permissions: 

* directory:user:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | expand (optional)
integration_presence_source = 'integration_presence_source_example' # str | integrationPresenceSource (optional)

try:
    # Search users using the q64 value returned from a previous search
    api_response = api_instance.get_users_search(q64, expand=expand, integration_presence_source=integration_presence_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_users_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str)| expand | [optional]  |
| **integration_presence_source** | **str**| integrationPresenceSource | [optional] <br />**Values**: MicrosoftTeams, ZoomPhone, EightByEight |

### Return type

[**UsersSearchResponse**](UsersSearchResponse)


## get_voicemail_search

> [**VoicemailsSearchResponse**](VoicemailsSearchResponse) get_voicemail_search(q64, expand=expand)


Search voicemails using the q64 value returned from a previous search

Wraps GET /api/v2/voicemail/search 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | expand (optional)

try:
    # Search voicemails using the q64 value returned from a previous search
    api_response = api_instance.get_voicemail_search(q64, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_voicemail_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str)| expand | [optional]  |

### Return type

[**VoicemailsSearchResponse**](VoicemailsSearchResponse)


## post_analytics_conversations_transcripts_query

> [**AnalyticsConversationWithoutAttributesMultiGetResponse**](AnalyticsConversationWithoutAttributesMultiGetResponse) post_analytics_conversations_transcripts_query(body)


Search resources.

Wraps POST /api/v2/analytics/conversations/transcripts/query 

Requires ANY permissions: 

* analytics:conversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.TranscriptConversationDetailSearchRequest() # TranscriptConversationDetailSearchRequest | Search request options

try:
    # Search resources.
    api_response = api_instance.post_analytics_conversations_transcripts_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_analytics_conversations_transcripts_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TranscriptConversationDetailSearchRequest**](TranscriptConversationDetailSearchRequest)| Search request options |  |

### Return type

[**AnalyticsConversationWithoutAttributesMultiGetResponse**](AnalyticsConversationWithoutAttributesMultiGetResponse)


## post_conversations_participants_attributes_search

> [**JsonCursorSearchResponse**](JsonCursorSearchResponse) post_conversations_participants_attributes_search(body)


Search conversations

Wraps POST /api/v2/conversations/participants/attributes/search 

Requires ANY permissions: 

* conversation:participant:attributesview

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.ConversationParticipantSearchRequest() # ConversationParticipantSearchRequest | Search request options

try:
    # Search conversations
    api_response = api_instance.post_conversations_participants_attributes_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_conversations_participants_attributes_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationParticipantSearchRequest**](ConversationParticipantSearchRequest)| Search request options |  |

### Return type

[**JsonCursorSearchResponse**](JsonCursorSearchResponse)


## post_documentation_all_search

> [**JsonNodeSearchResponse**](JsonNodeSearchResponse) post_documentation_all_search(body)


Search all documents

post_documentation_all_search is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/documentation/all/search 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.DocumentationV2SearchRequest() # DocumentationV2SearchRequest | Search request options

try:
    # Search all documents
    api_response = api_instance.post_documentation_all_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_documentation_all_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DocumentationV2SearchRequest**](DocumentationV2SearchRequest)| Search request options |  |

### Return type

[**JsonNodeSearchResponse**](JsonNodeSearchResponse)


## post_documentation_gkn_search

> [**GKNDocumentationSearchResponse**](GKNDocumentationSearchResponse) post_documentation_gkn_search(body)


Search gkn documentation

Wraps POST /api/v2/documentation/gkn/search 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.GKNDocumentationSearchRequest() # GKNDocumentationSearchRequest | Search request options

try:
    # Search gkn documentation
    api_response = api_instance.post_documentation_gkn_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_documentation_gkn_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GKNDocumentationSearchRequest**](GKNDocumentationSearchRequest)| Search request options |  |

### Return type

[**GKNDocumentationSearchResponse**](GKNDocumentationSearchResponse)


## post_documentation_search

> [**DocumentationSearchResponse**](DocumentationSearchResponse) post_documentation_search(body)


Search documentation

Wraps POST /api/v2/documentation/search 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.DocumentationSearchRequest() # DocumentationSearchRequest | Search request options

try:
    # Search documentation
    api_response = api_instance.post_documentation_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_documentation_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DocumentationSearchRequest**](DocumentationSearchRequest)| Search request options |  |

### Return type

[**DocumentationSearchResponse**](DocumentationSearchResponse)


## post_groups_search

> [**GroupsSearchResponse**](GroupsSearchResponse) post_groups_search(body)


Search groups

Wraps POST /api/v2/groups/search 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.GroupSearchRequest() # GroupSearchRequest | Search request options

try:
    # Search groups
    api_response = api_instance.post_groups_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_groups_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GroupSearchRequest**](GroupSearchRequest)| Search request options |  |

### Return type

[**GroupsSearchResponse**](GroupsSearchResponse)


## post_knowledge_knowledgebase_search

> [**KnowledgeSearchResponse**](KnowledgeSearchResponse) post_knowledge_knowledgebase_search(knowledge_base_id, body=body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Search Documents

Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/search 

Requires ALL permissions: 

* knowledge:knowledgebase:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
body = PureCloudPlatformClientV2.KnowledgeSearchRequest() # KnowledgeSearchRequest |  (optional)

try:
    # Search Documents
    api_response = api_instance.post_knowledge_knowledgebase_search(knowledge_base_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_knowledge_knowledgebase_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeSearchRequest**](KnowledgeSearchRequest)|  | [optional]  |

### Return type

[**KnowledgeSearchResponse**](KnowledgeSearchResponse)


## post_locations_search

> [**LocationsSearchResponse**](LocationsSearchResponse) post_locations_search(body)


Search locations

Wraps POST /api/v2/locations/search 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.LocationSearchRequest() # LocationSearchRequest | Search request options

try:
    # Search locations
    api_response = api_instance.post_locations_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_locations_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LocationSearchRequest**](LocationSearchRequest)| Search request options |  |

### Return type

[**LocationsSearchResponse**](LocationsSearchResponse)


## post_search

> [**JsonNodeSearchResponse**](JsonNodeSearchResponse) post_search(body, profile=profile)


Search resources.

Wraps POST /api/v2/search 

Requires ANY permissions: 

* directory:user:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.SearchRequest() # SearchRequest | Search request options
profile = True # bool | profile (optional) (default to True)

try:
    # Search resources.
    api_response = api_instance.post_search(body, profile=profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SearchRequest**](SearchRequest)| Search request options |  |
| **profile** | **bool**| profile | [optional] [default to True] |

### Return type

[**JsonNodeSearchResponse**](JsonNodeSearchResponse)


## post_search_suggest

> [**JsonNodeSearchResponse**](JsonNodeSearchResponse) post_search_suggest(body, profile=profile)


Suggest resources.

Wraps POST /api/v2/search/suggest 

Requires ANY permissions: 

* directory:user:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.SuggestSearchRequest() # SuggestSearchRequest | Search request options
profile = True # bool | profile (optional) (default to True)

try:
    # Suggest resources.
    api_response = api_instance.post_search_suggest(body, profile=profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_search_suggest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SuggestSearchRequest**](SuggestSearchRequest)| Search request options |  |
| **profile** | **bool**| profile | [optional] [default to True] |

### Return type

[**JsonNodeSearchResponse**](JsonNodeSearchResponse)


## post_speechandtextanalytics_transcripts_search

> [**JsonSearchResponse**](JsonSearchResponse) post_speechandtextanalytics_transcripts_search(body)


Search resources.

Wraps POST /api/v2/speechandtextanalytics/transcripts/search 

Requires ANY permissions: 

* analytics:conversationDetail:view
* recording:recording:view
* recording:recordingSegment:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.TranscriptSearchRequest() # TranscriptSearchRequest | Search request options

try:
    # Search resources.
    api_response = api_instance.post_speechandtextanalytics_transcripts_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_speechandtextanalytics_transcripts_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TranscriptSearchRequest**](TranscriptSearchRequest)| Search request options |  |

### Return type

[**JsonSearchResponse**](JsonSearchResponse)


## post_teams_search

> [**TeamsSearchResponse**](TeamsSearchResponse) post_teams_search(body)


Search resources.

Wraps POST /api/v2/teams/search 

Requires ANY permissions: 

* groups:team:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.TeamSearchRequest() # TeamSearchRequest | Search request options

try:
    # Search resources.
    api_response = api_instance.post_teams_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_teams_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TeamSearchRequest**](TeamSearchRequest)| Search request options |  |

### Return type

[**TeamsSearchResponse**](TeamsSearchResponse)


## post_telephony_providers_edges_sites_search

> [**SitesSearchResponse**](SitesSearchResponse) post_telephony_providers_edges_sites_search(body)


Search sites

Wraps POST /api/v2/telephony/providers/edges/sites/search 

Requires ANY permissions: 

* telephony:plugin:all
* telephony:sites:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.SiteSearchRequest() # SiteSearchRequest | Search request options

try:
    # Search sites
    api_response = api_instance.post_telephony_providers_edges_sites_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_telephony_providers_edges_sites_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SiteSearchRequest**](SiteSearchRequest)| Search request options |  |

### Return type

[**SitesSearchResponse**](SitesSearchResponse)


## post_users_search

> [**UsersSearchResponse**](UsersSearchResponse) post_users_search(body)


Search users

Wraps POST /api/v2/users/search 

Requires ANY permissions: 

* directory:user:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.UserSearchRequest() # UserSearchRequest | Search request options

try:
    # Search users
    api_response = api_instance.post_users_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_users_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserSearchRequest**](UserSearchRequest)| Search request options |  |

### Return type

[**UsersSearchResponse**](UsersSearchResponse)


## post_users_search_conversation_target

> [**UsersSearchResponse**](UsersSearchResponse) post_users_search_conversation_target(body)


Search users as conversation targets

post_users_search_conversation_target is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/users/search/conversation/target 

Requires ANY permissions: 

* conversation:communication:target

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.UserSearchRequest() # UserSearchRequest | Search request options

try:
    # Search users as conversation targets
    api_response = api_instance.post_users_search_conversation_target(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_users_search_conversation_target: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserSearchRequest**](UserSearchRequest)| Search request options |  |

### Return type

[**UsersSearchResponse**](UsersSearchResponse)


## post_users_search_queuemembers_manage

> [**UsersSearchResponse**](UsersSearchResponse) post_users_search_queuemembers_manage(body)


Search manage queue member

post_users_search_queuemembers_manage is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/users/search/queuemembers/manage 

Requires ANY permissions: 

* routing:queueMember:manage
* routing:queue:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.UserSearchRequest() # UserSearchRequest | Search request options

try:
    # Search manage queue member
    api_response = api_instance.post_users_search_queuemembers_manage(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_users_search_queuemembers_manage: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserSearchRequest**](UserSearchRequest)| Search request options |  |

### Return type

[**UsersSearchResponse**](UsersSearchResponse)


## post_users_search_teams_assign

> [**UsersSearchResponse**](UsersSearchResponse) post_users_search_teams_assign(body)


Search users assigned to teams

Wraps POST /api/v2/users/search/teams/assign 

Requires ANY permissions: 

* groups:team:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.UserSearchRequest() # UserSearchRequest | Search request options

try:
    # Search users assigned to teams
    api_response = api_instance.post_users_search_teams_assign(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_users_search_teams_assign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserSearchRequest**](UserSearchRequest)| Search request options |  |

### Return type

[**UsersSearchResponse**](UsersSearchResponse)


## post_voicemail_search

> [**VoicemailsSearchResponse**](VoicemailsSearchResponse) post_voicemail_search(body)


Search voicemails

Wraps POST /api/v2/voicemail/search 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.VoicemailSearchRequest() # VoicemailSearchRequest | Search request options

try:
    # Search voicemails
    api_response = api_instance.post_voicemail_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_voicemail_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**VoicemailSearchRequest**](VoicemailSearchRequest)| Search request options |  |

### Return type

[**VoicemailsSearchResponse**](VoicemailsSearchResponse)


_PureCloudPlatformClientV2 231.0.0_

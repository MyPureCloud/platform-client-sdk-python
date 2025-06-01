# SuggestApi

## PureCloudPlatformClientV2.SuggestApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_search**](#get_search) | Search using the q64 value returned from a previous search.|
|[**get_search_suggest**](#get_search_suggest) | Suggest resources using the q64 value returned from a previous suggest query.|
|[**post_search**](#post_search) | Search resources.|
|[**post_search_suggest**](#post_search_suggest) | Suggest resources.|



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
api_instance = PureCloudPlatformClientV2.SuggestApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
profile = True # bool | profile (optional) (default to True)

try:
    # Search using the q64 value returned from a previous search.
    api_response = api_instance.get_search(q64, expand=expand, profile=profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuggestApi->get_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, dateLastLogin, dateWelcomeSent, callerUser.routingStatus, callerUser.primaryPresence, callerUser.conversationSummary, callerUser.outOfOffice, callerUser.geolocation, conversations, transcription, images, addressVerificationDetails |
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
api_instance = PureCloudPlatformClientV2.SuggestApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
profile = True # bool | profile (optional) (default to True)

try:
    # Suggest resources using the q64 value returned from a previous suggest query.
    api_response = api_instance.get_search_suggest(q64, expand=expand, profile=profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuggestApi->get_search_suggest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, integrationPresence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, workPlanBidRanks, externalContactsSettings, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, dateLastLogin, dateWelcomeSent, callerUser.routingStatus, callerUser.primaryPresence, callerUser.conversationSummary, callerUser.outOfOffice, callerUser.geolocation, conversations, transcription, images, addressVerificationDetails |
| **profile** | **bool**| profile | [optional] [default to True] |

### Return type

[**JsonNodeSearchResponse**](JsonNodeSearchResponse)


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
api_instance = PureCloudPlatformClientV2.SuggestApi()
body = PureCloudPlatformClientV2.SearchRequest() # SearchRequest | Search request options
profile = True # bool | profile (optional) (default to True)

try:
    # Search resources.
    api_response = api_instance.post_search(body, profile=profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuggestApi->post_search: %s\n" % e)
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
api_instance = PureCloudPlatformClientV2.SuggestApi()
body = PureCloudPlatformClientV2.SuggestSearchRequest() # SuggestSearchRequest | Search request options
profile = True # bool | profile (optional) (default to True)

try:
    # Suggest resources.
    api_response = api_instance.post_search_suggest(body, profile=profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuggestApi->post_search_suggest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SuggestSearchRequest**](SuggestSearchRequest)| Search request options |  |
| **profile** | **bool**| profile | [optional] [default to True] |

### Return type

[**JsonNodeSearchResponse**](JsonNodeSearchResponse)


_PureCloudPlatformClientV2 230.0.0_

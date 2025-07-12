# GreetingsApi

## PureCloudPlatformClientV2.GreetingsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_greeting**](#delete_greeting) | Deletes a Greeting with the given GreetingId|
|[**get_greeting**](#get_greeting) | Get a Greeting with the given GreetingId|
|[**get_greeting_downloads**](#get_greeting_downloads) | Download a organization greeting recording|
|[**get_greeting_groups_downloads**](#get_greeting_groups_downloads) | Download a group greeting recording|
|[**get_greeting_media**](#get_greeting_media) | Get media playback URI for this greeting|
|[**get_greeting_users_downloads**](#get_greeting_users_downloads) | Download a user greeting recording|
|[**get_greetings**](#get_greetings) | Gets an Organization&#39;s Greetings|
|[**get_greetings_defaults**](#get_greetings_defaults) | Get an Organization&#39;s DefaultGreetingList|
|[**get_group_greetings**](#get_group_greetings) | Get a list of the Group&#39;s Greetings|
|[**get_group_greetings_defaults**](#get_group_greetings_defaults) | Grabs the list of Default Greetings given a Group&#39;s ID|
|[**get_user_greetings**](#get_user_greetings) | Get a list of the User&#39;s Greetings|
|[**get_user_greetings_defaults**](#get_user_greetings_defaults) | Grabs the list of Default Greetings given a User&#39;s ID|
|[**post_greetings**](#post_greetings) | Create a Greeting for an Organization|
|[**post_group_greetings**](#post_group_greetings) | Creates a Greeting for a Group|
|[**post_user_greetings**](#post_user_greetings) | Creates a Greeting for a User|
|[**put_greeting**](#put_greeting) | Updates the Greeting with the given GreetingId|
|[**put_greetings_defaults**](#put_greetings_defaults) | Update an Organization&#39;s DefaultGreetingList|
|[**put_group_greetings_defaults**](#put_group_greetings_defaults) | Updates the DefaultGreetingList of the specified Group|
|[**put_user_greetings_defaults**](#put_user_greetings_defaults) | Updates the DefaultGreetingList of the specified User|



## delete_greeting

>  delete_greeting(greeting_id)


Deletes a Greeting with the given GreetingId

Wraps DELETE /api/v2/greetings/{greetingId} 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
greeting_id = 'greeting_id_example' # str | Greeting ID

try:
    # Deletes a Greeting with the given GreetingId
    api_instance.delete_greeting(greeting_id)
except ApiException as e:
    print("Exception when calling GreetingsApi->delete_greeting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **greeting_id** | **str**| Greeting ID |  |

### Return type

void (empty response body)


## get_greeting

> [**Greeting**](Greeting) get_greeting(greeting_id)


Get a Greeting with the given GreetingId

Wraps GET /api/v2/greetings/{greetingId} 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
greeting_id = 'greeting_id_example' # str | Greeting ID

try:
    # Get a Greeting with the given GreetingId
    api_response = api_instance.get_greeting(greeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->get_greeting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **greeting_id** | **str**| Greeting ID |  |

### Return type

[**Greeting**](Greeting)


## get_greeting_downloads

> [**GreetingMediaInfo**](GreetingMediaInfo) get_greeting_downloads(greeting_id, format_id=format_id)


Download a organization greeting recording

Wraps GET /api/v2/greetings/{greetingId}/downloads 

Requires ANY permissions: 

* greetings:greeting:download

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GreetingsApi()
greeting_id = 'greeting_id_example' # str | Greeting ID
format_id = ''WAV'' # str | The desired media format. (optional) (default to 'WAV')

try:
    # Download a organization greeting recording
    api_response = api_instance.get_greeting_downloads(greeting_id, format_id=format_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->get_greeting_downloads: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **greeting_id** | **str**| Greeting ID |  |
| **format_id** | **str**| The desired media format. | [optional] [default to &#39;WAV&#39;]<br />**Values**: WAV, WEBM, WAV_ULAW, OGG_VORBIS, OGG_OPUS, MP3, NONE |

### Return type

[**GreetingMediaInfo**](GreetingMediaInfo)


## get_greeting_groups_downloads

> [**GreetingMediaInfo**](GreetingMediaInfo) get_greeting_groups_downloads(greeting_id, format_id=format_id)


Download a group greeting recording

Wraps GET /api/v2/greetings/{greetingId}/groups/downloads 

Requires ANY permissions: 

* greetings:groupGreeting:download

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GreetingsApi()
greeting_id = 'greeting_id_example' # str | Greeting ID
format_id = ''WAV'' # str | The desired media format. (optional) (default to 'WAV')

try:
    # Download a group greeting recording
    api_response = api_instance.get_greeting_groups_downloads(greeting_id, format_id=format_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->get_greeting_groups_downloads: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **greeting_id** | **str**| Greeting ID |  |
| **format_id** | **str**| The desired media format. | [optional] [default to &#39;WAV&#39;]<br />**Values**: WAV, WEBM, WAV_ULAW, OGG_VORBIS, OGG_OPUS, MP3, NONE |

### Return type

[**GreetingMediaInfo**](GreetingMediaInfo)


## get_greeting_media

> [**GreetingMediaInfo**](GreetingMediaInfo) get_greeting_media(greeting_id, format_id=format_id)


Get media playback URI for this greeting

API should migrate to use GET api/v2/greetings/{greetingId}/downloads

Wraps GET /api/v2/greetings/{greetingId}/media 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
greeting_id = 'greeting_id_example' # str | Greeting ID
format_id = ''WAV'' # str | The desired media format. (optional) (default to 'WAV')

try:
    # Get media playback URI for this greeting
    api_response = api_instance.get_greeting_media(greeting_id, format_id=format_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->get_greeting_media: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **greeting_id** | **str**| Greeting ID |  |
| **format_id** | **str**| The desired media format. | [optional] [default to &#39;WAV&#39;]<br />**Values**: WAV, WEBM, WAV_ULAW, OGG_VORBIS, OGG_OPUS, MP3, NONE |

### Return type

[**GreetingMediaInfo**](GreetingMediaInfo)


## get_greeting_users_downloads

> [**GreetingMediaInfo**](GreetingMediaInfo) get_greeting_users_downloads(greeting_id, format_id=format_id)


Download a user greeting recording

Wraps GET /api/v2/greetings/{greetingId}/users/downloads 

Requires ANY permissions: 

* greetings:greeting:download

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GreetingsApi()
greeting_id = 'greeting_id_example' # str | Greeting ID
format_id = ''WAV'' # str | The desired media format. (optional) (default to 'WAV')

try:
    # Download a user greeting recording
    api_response = api_instance.get_greeting_users_downloads(greeting_id, format_id=format_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->get_greeting_users_downloads: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **greeting_id** | **str**| Greeting ID |  |
| **format_id** | **str**| The desired media format. | [optional] [default to &#39;WAV&#39;]<br />**Values**: WAV, WEBM, WAV_ULAW, OGG_VORBIS, OGG_OPUS, MP3, NONE |

### Return type

[**GreetingMediaInfo**](GreetingMediaInfo)


## get_greetings

> [**DomainEntityListing**](DomainEntityListing) get_greetings(page_size=page_size, page_number=page_number)


Gets an Organization's Greetings

Wraps GET /api/v2/greetings 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Gets an Organization's Greetings
    api_response = api_instance.get_greetings(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->get_greetings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**DomainEntityListing**](DomainEntityListing)


## get_greetings_defaults

> [**DefaultGreetingList**](DefaultGreetingList) get_greetings_defaults()


Get an Organization's DefaultGreetingList

Wraps GET /api/v2/greetings/defaults 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()

try:
    # Get an Organization's DefaultGreetingList
    api_response = api_instance.get_greetings_defaults()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->get_greetings_defaults: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**DefaultGreetingList**](DefaultGreetingList)


## get_group_greetings

> [**GreetingListing**](GreetingListing) get_group_greetings(group_id, page_size=page_size, page_number=page_number)


Get a list of the Group's Greetings

Wraps GET /api/v2/groups/{groupId}/greetings 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
group_id = 'group_id_example' # str | Group ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of the Group's Greetings
    api_response = api_instance.get_group_greetings(group_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->get_group_greetings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**GreetingListing**](GreetingListing)


## get_group_greetings_defaults

> [**DefaultGreetingList**](DefaultGreetingList) get_group_greetings_defaults(group_id)


Grabs the list of Default Greetings given a Group's ID

Wraps GET /api/v2/groups/{groupId}/greetings/defaults 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
group_id = 'group_id_example' # str | Group ID

try:
    # Grabs the list of Default Greetings given a Group's ID
    api_response = api_instance.get_group_greetings_defaults(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->get_group_greetings_defaults: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |

### Return type

[**DefaultGreetingList**](DefaultGreetingList)


## get_user_greetings

> [**DomainEntityListing**](DomainEntityListing) get_user_greetings(user_id, page_size=page_size, page_number=page_number)


Get a list of the User's Greetings

Wraps GET /api/v2/users/{userId}/greetings 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
user_id = 'user_id_example' # str | User ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of the User's Greetings
    api_response = api_instance.get_user_greetings(user_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->get_user_greetings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |

### Return type

[**DomainEntityListing**](DomainEntityListing)


## get_user_greetings_defaults

> [**DefaultGreetingList**](DefaultGreetingList) get_user_greetings_defaults(user_id)


Grabs the list of Default Greetings given a User's ID

Wraps GET /api/v2/users/{userId}/greetings/defaults 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
user_id = 'user_id_example' # str | User ID

try:
    # Grabs the list of Default Greetings given a User's ID
    api_response = api_instance.get_user_greetings_defaults(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->get_user_greetings_defaults: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |

### Return type

[**DefaultGreetingList**](DefaultGreetingList)


## post_greetings

> [**Greeting**](Greeting) post_greetings(body)


Create a Greeting for an Organization

Wraps POST /api/v2/greetings 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
body = PureCloudPlatformClientV2.Greeting() # Greeting | The Greeting to create

try:
    # Create a Greeting for an Organization
    api_response = api_instance.post_greetings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->post_greetings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Greeting**](Greeting)| The Greeting to create |  |

### Return type

[**Greeting**](Greeting)


## post_group_greetings

> [**Greeting**](Greeting) post_group_greetings(group_id, body)


Creates a Greeting for a Group

Wraps POST /api/v2/groups/{groupId}/greetings 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
group_id = 'group_id_example' # str | Group ID
body = PureCloudPlatformClientV2.Greeting() # Greeting | The Greeting to create

try:
    # Creates a Greeting for a Group
    api_response = api_instance.post_group_greetings(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->post_group_greetings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |
| **body** | [**Greeting**](Greeting)| The Greeting to create |  |

### Return type

[**Greeting**](Greeting)


## post_user_greetings

> [**Greeting**](Greeting) post_user_greetings(user_id, body)


Creates a Greeting for a User

Wraps POST /api/v2/users/{userId}/greetings 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.Greeting() # Greeting | The Greeting to create

try:
    # Creates a Greeting for a User
    api_response = api_instance.post_user_greetings(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->post_user_greetings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**Greeting**](Greeting)| The Greeting to create |  |

### Return type

[**Greeting**](Greeting)


## put_greeting

> [**Greeting**](Greeting) put_greeting(greeting_id, body)


Updates the Greeting with the given GreetingId

Wraps PUT /api/v2/greetings/{greetingId} 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
greeting_id = 'greeting_id_example' # str | Greeting ID
body = PureCloudPlatformClientV2.Greeting() # Greeting | The updated Greeting

try:
    # Updates the Greeting with the given GreetingId
    api_response = api_instance.put_greeting(greeting_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->put_greeting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **greeting_id** | **str**| Greeting ID |  |
| **body** | [**Greeting**](Greeting)| The updated Greeting |  |

### Return type

[**Greeting**](Greeting)


## put_greetings_defaults

> [**DefaultGreetingList**](DefaultGreetingList) put_greetings_defaults(body)


Update an Organization's DefaultGreetingList

Wraps PUT /api/v2/greetings/defaults 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
body = PureCloudPlatformClientV2.DefaultGreetingList() # DefaultGreetingList | The updated defaultGreetingList

try:
    # Update an Organization's DefaultGreetingList
    api_response = api_instance.put_greetings_defaults(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->put_greetings_defaults: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DefaultGreetingList**](DefaultGreetingList)| The updated defaultGreetingList |  |

### Return type

[**DefaultGreetingList**](DefaultGreetingList)


## put_group_greetings_defaults

> [**DefaultGreetingList**](DefaultGreetingList) put_group_greetings_defaults(group_id, body)


Updates the DefaultGreetingList of the specified Group

Wraps PUT /api/v2/groups/{groupId}/greetings/defaults 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
group_id = 'group_id_example' # str | Group ID
body = PureCloudPlatformClientV2.DefaultGreetingList() # DefaultGreetingList | The updated defaultGreetingList

try:
    # Updates the DefaultGreetingList of the specified Group
    api_response = api_instance.put_group_greetings_defaults(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->put_group_greetings_defaults: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID |  |
| **body** | [**DefaultGreetingList**](DefaultGreetingList)| The updated defaultGreetingList |  |

### Return type

[**DefaultGreetingList**](DefaultGreetingList)


## put_user_greetings_defaults

> [**DefaultGreetingList**](DefaultGreetingList) put_user_greetings_defaults(user_id, body)


Updates the DefaultGreetingList of the specified User

Wraps PUT /api/v2/users/{userId}/greetings/defaults 

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
api_instance = PureCloudPlatformClientV2.GreetingsApi()
user_id = 'user_id_example' # str | User ID
body = PureCloudPlatformClientV2.DefaultGreetingList() # DefaultGreetingList | The updated defaultGreetingList

try:
    # Updates the DefaultGreetingList of the specified User
    api_response = api_instance.put_user_greetings_defaults(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GreetingsApi->put_user_greetings_defaults: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| User ID |  |
| **body** | [**DefaultGreetingList**](DefaultGreetingList)| The updated defaultGreetingList |  |

### Return type

[**DefaultGreetingList**](DefaultGreetingList)


_PureCloudPlatformClientV2 233.0.0_

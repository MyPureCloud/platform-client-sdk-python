---
title: GreetingsApi
---

## PureCloudPlatformClientV2.GreetingsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_greeting**](GreetingsApi.html#delete_greeting) | Deletes a Greeting with the given GreetingId|
|[**get_greeting**](GreetingsApi.html#get_greeting) | Get a Greeting with the given GreetingId|
|[**get_greeting_media**](GreetingsApi.html#get_greeting_media) | Get media playback URI for this greeting|
|[**get_greetings**](GreetingsApi.html#get_greetings) | Gets an Organization&#39;s Greetings|
|[**get_greetings_defaults**](GreetingsApi.html#get_greetings_defaults) | Get an Organization&#39;s DefaultGreetingList|
|[**get_group_greetings**](GreetingsApi.html#get_group_greetings) | Get a list of the Group&#39;s Greetings|
|[**get_group_greetings_defaults**](GreetingsApi.html#get_group_greetings_defaults) | Grabs the list of Default Greetings given a Group&#39;s ID|
|[**get_user_greetings**](GreetingsApi.html#get_user_greetings) | Get a list of the User&#39;s Greetings|
|[**get_user_greetings_defaults**](GreetingsApi.html#get_user_greetings_defaults) | Grabs the list of Default Greetings given a User&#39;s ID|
|[**post_greetings**](GreetingsApi.html#post_greetings) | Create a Greeting for an Organization|
|[**post_group_greetings**](GreetingsApi.html#post_group_greetings) | Creates a Greeting for a Group|
|[**post_user_greetings**](GreetingsApi.html#post_user_greetings) | Creates a Greeting for a User|
|[**put_greeting**](GreetingsApi.html#put_greeting) | Updates the Greeting with the given GreetingId|
|[**put_greetings_defaults**](GreetingsApi.html#put_greetings_defaults) | Update an Organization&#39;s DefaultGreetingList|
|[**put_group_greetings_defaults**](GreetingsApi.html#put_group_greetings_defaults) | Updates the DefaultGreetingList of the specified Group|
|[**put_user_greetings_defaults**](GreetingsApi.html#put_user_greetings_defaults) | Updates the DefaultGreetingList of the specified User|
{: class="table table-striped"}

<a name="delete_greeting"></a>

##  delete_greeting(greeting_id)



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
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_greeting"></a>

## [**Greeting**](Greeting.html) get_greeting(greeting_id)



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
{: class="table table-striped"}

### Return type

[**Greeting**](Greeting.html)

<a name="get_greeting_media"></a>

## [**GreetingMediaInfo**](GreetingMediaInfo.html) get_greeting_media(greeting_id, format_id=format_id)



Get media playback URI for this greeting

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
{: class="table table-striped"}

### Return type

[**GreetingMediaInfo**](GreetingMediaInfo.html)

<a name="get_greetings"></a>

## [**DomainEntityListing**](DomainEntityListing.html) get_greetings(page_size=page_size, page_number=page_number)



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
{: class="table table-striped"}

### Return type

[**DomainEntityListing**](DomainEntityListing.html)

<a name="get_greetings_defaults"></a>

## [**DefaultGreetingList**](DefaultGreetingList.html) get_greetings_defaults()



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

[**DefaultGreetingList**](DefaultGreetingList.html)

<a name="get_group_greetings"></a>

## [**GreetingListing**](GreetingListing.html) get_group_greetings(group_id, page_size=page_size, page_number=page_number)



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
{: class="table table-striped"}

### Return type

[**GreetingListing**](GreetingListing.html)

<a name="get_group_greetings_defaults"></a>

## [**DefaultGreetingList**](DefaultGreetingList.html) get_group_greetings_defaults(group_id)



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
{: class="table table-striped"}

### Return type

[**DefaultGreetingList**](DefaultGreetingList.html)

<a name="get_user_greetings"></a>

## [**DomainEntityListing**](DomainEntityListing.html) get_user_greetings(user_id, page_size=page_size, page_number=page_number)



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
{: class="table table-striped"}

### Return type

[**DomainEntityListing**](DomainEntityListing.html)

<a name="get_user_greetings_defaults"></a>

## [**DefaultGreetingList**](DefaultGreetingList.html) get_user_greetings_defaults(user_id)



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
{: class="table table-striped"}

### Return type

[**DefaultGreetingList**](DefaultGreetingList.html)

<a name="post_greetings"></a>

## [**Greeting**](Greeting.html) post_greetings(body)



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
| **body** | [**Greeting**](Greeting.html)| The Greeting to create |  |
{: class="table table-striped"}

### Return type

[**Greeting**](Greeting.html)

<a name="post_group_greetings"></a>

## [**Greeting**](Greeting.html) post_group_greetings(group_id, body)



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
| **body** | [**Greeting**](Greeting.html)| The Greeting to create |  |
{: class="table table-striped"}

### Return type

[**Greeting**](Greeting.html)

<a name="post_user_greetings"></a>

## [**Greeting**](Greeting.html) post_user_greetings(user_id, body)



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
| **body** | [**Greeting**](Greeting.html)| The Greeting to create |  |
{: class="table table-striped"}

### Return type

[**Greeting**](Greeting.html)

<a name="put_greeting"></a>

## [**Greeting**](Greeting.html) put_greeting(greeting_id, body)



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
| **body** | [**Greeting**](Greeting.html)| The updated Greeting |  |
{: class="table table-striped"}

### Return type

[**Greeting**](Greeting.html)

<a name="put_greetings_defaults"></a>

## [**DefaultGreetingList**](DefaultGreetingList.html) put_greetings_defaults(body)



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
| **body** | [**DefaultGreetingList**](DefaultGreetingList.html)| The updated defaultGreetingList |  |
{: class="table table-striped"}

### Return type

[**DefaultGreetingList**](DefaultGreetingList.html)

<a name="put_group_greetings_defaults"></a>

## [**DefaultGreetingList**](DefaultGreetingList.html) put_group_greetings_defaults(group_id, body)



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
| **body** | [**DefaultGreetingList**](DefaultGreetingList.html)| The updated defaultGreetingList |  |
{: class="table table-striped"}

### Return type

[**DefaultGreetingList**](DefaultGreetingList.html)

<a name="put_user_greetings_defaults"></a>

## [**DefaultGreetingList**](DefaultGreetingList.html) put_user_greetings_defaults(user_id, body)



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
| **body** | [**DefaultGreetingList**](DefaultGreetingList.html)| The updated defaultGreetingList |  |
{: class="table table-striped"}

### Return type

[**DefaultGreetingList**](DefaultGreetingList.html)


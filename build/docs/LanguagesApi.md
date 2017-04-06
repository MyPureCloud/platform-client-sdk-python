---
title: LanguagesApi
---

## PureCloudPlatformClientV2.LanguagesApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_language**](LanguagesApi.html#delete_language) | Delete Language (Deprecated)|
|[**delete_routing_language**](LanguagesApi.html#delete_routing_language) | Delete Language|
|[**get_language**](LanguagesApi.html#get_language) | Get language (Deprecated)|
|[**get_languages**](LanguagesApi.html#get_languages) | Get the list of supported languages. (Deprecated)|
|[**get_languages_translations**](LanguagesApi.html#get_languages_translations) | Get all available languages for translation|
|[**get_languages_translations_builtin**](LanguagesApi.html#get_languages_translations_builtin) | Get the builtin translation for a language|
|[**get_languages_translations_organization**](LanguagesApi.html#get_languages_translations_organization) | Get effective translation for an organization by language|
|[**get_languages_translations_user**](LanguagesApi.html#get_languages_translations_user) | Get effective language translation for a user|
|[**get_routing_language**](LanguagesApi.html#get_routing_language) | Get language|
|[**post_languages**](LanguagesApi.html#post_languages) | Create Language (Deprecated)|
{: class="table table-striped"}

<a name="delete_language"></a>

## delete_language(language_id)

Delete Language (Deprecated)

This endpoint is deprecated. It has been moved to /routing/languages/{languageId}

Wraps DELETE /api/v2/languages/{languageId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguagesApi()
language_id = 'language_id_example' # str | Language ID

try:
    # Delete Language (Deprecated)
    api_instance.delete_language(language_id)
except ApiException as e:
    print "Exception when calling LanguagesApi->delete_language: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language_id** | **str**| Language ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_routing_language"></a>

## delete_routing_language(language_id)

Delete Language



Wraps DELETE /api/v2/routing/languages/{languageId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguagesApi()
language_id = 'language_id_example' # str | Language ID

try:
    # Delete Language
    api_instance.delete_routing_language(language_id)
except ApiException as e:
    print "Exception when calling LanguagesApi->delete_routing_language: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language_id** | **str**| Language ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_language"></a>

## [**Language**](Language.html)get_language(language_id)

Get language (Deprecated)

This endpoint is deprecated. It has been moved to /routing/languages/{languageId}

Wraps GET /api/v2/languages/{languageId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguagesApi()
language_id = 'language_id_example' # str | Language ID

try:
    # Get language (Deprecated)
    api_response = api_instance.get_language(language_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LanguagesApi->get_language: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language_id** | **str**| Language ID | |
{: class="table table-striped"}

### Return type

[**Language**](Language.html)

<a name="get_languages"></a>

## [**LanguageEntityListing**](LanguageEntityListing.html)get_languages(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name)

Get the list of supported languages. (Deprecated)

This endpoint is deprecated. It has been moved to /routing/languages

Wraps GET /api/v2/languages 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguagesApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'ASC' # str | Ascending or descending sort order (optional) (default to ASC)
name = 'name_example' # str | Name (optional)

try:
    # Get the list of supported languages. (Deprecated)
    api_response = api_instance.get_languages(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LanguagesApi->get_languages: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to ASC]|
| **name** | **str**| Name | [optional] |
{: class="table table-striped"}

### Return type

[**LanguageEntityListing**](LanguageEntityListing.html)

<a name="get_languages_translations"></a>

## [**AvailableTranslations**](AvailableTranslations.html)get_languages_translations()

Get all available languages for translation



Wraps GET /api/v2/languages/translations 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguagesApi()

try:
    # Get all available languages for translation
    api_response = api_instance.get_languages_translations()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LanguagesApi->get_languages_translations: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**AvailableTranslations**](AvailableTranslations.html)

<a name="get_languages_translations_builtin"></a>

## [**dict(str, object)**](dict.html)get_languages_translations_builtin(language)

Get the builtin translation for a language



Wraps GET /api/v2/languages/translations/builtin 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguagesApi()
language = 'language_example' # str | The language of the builtin translation to retrieve

try:
    # Get the builtin translation for a language
    api_response = api_instance.get_languages_translations_builtin(language)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LanguagesApi->get_languages_translations_builtin: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language** | **str**| The language of the builtin translation to retrieve | |
{: class="table table-striped"}

### Return type

[**dict(str, object)**](dict.html)

<a name="get_languages_translations_organization"></a>

## [**dict(str, object)**](dict.html)get_languages_translations_organization(language)

Get effective translation for an organization by language



Wraps GET /api/v2/languages/translations/organization 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguagesApi()
language = 'language_example' # str | The language of the translation to retrieve for the organization

try:
    # Get effective translation for an organization by language
    api_response = api_instance.get_languages_translations_organization(language)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LanguagesApi->get_languages_translations_organization: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language** | **str**| The language of the translation to retrieve for the organization | |
{: class="table table-striped"}

### Return type

[**dict(str, object)**](dict.html)

<a name="get_languages_translations_user"></a>

## [**dict(str, object)**](dict.html)get_languages_translations_user(user_id)

Get effective language translation for a user



Wraps GET /api/v2/languages/translations/users/{userId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguagesApi()
user_id = 'user_id_example' # str | The user id

try:
    # Get effective language translation for a user
    api_response = api_instance.get_languages_translations_user(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LanguagesApi->get_languages_translations_user: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The user id | |
{: class="table table-striped"}

### Return type

[**dict(str, object)**](dict.html)

<a name="get_routing_language"></a>

## [**Language**](Language.html)get_routing_language(language_id)

Get language



Wraps GET /api/v2/routing/languages/{languageId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguagesApi()
language_id = 'language_id_example' # str | Language ID

try:
    # Get language
    api_response = api_instance.get_routing_language(language_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LanguagesApi->get_routing_language: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language_id** | **str**| Language ID | |
{: class="table table-striped"}

### Return type

[**Language**](Language.html)

<a name="post_languages"></a>

## [**Language**](Language.html)post_languages(body)

Create Language (Deprecated)

This endpoint is deprecated. It has been moved to /routing/languages

Wraps POST /api/v2/languages 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguagesApi()
body = PureCloudPlatformClientV2.Language() # Language | Language

try:
    # Create Language (Deprecated)
    api_response = api_instance.post_languages(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LanguagesApi->post_languages: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Language**](Language.html)| Language | |
{: class="table table-striped"}

### Return type

[**Language**](Language.html)


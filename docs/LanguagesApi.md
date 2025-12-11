# LanguagesApi

## PureCloudPlatformClientV2.LanguagesApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_language**](#delete_language) | Delete Language (Deprecated)|
|[**get_language**](#get_language) | Get Language (Deprecated)|
|[**get_languages**](#get_languages) | Get the list of supported languages. (Deprecated)|
|[**get_languages_translations**](#get_languages_translations) | Get all available languages for translation|
|[**get_languages_translations_builtin**](#get_languages_translations_builtin) | Get the builtin translation for a language|
|[**get_languages_translations_organization**](#get_languages_translations_organization) | Get effective translation for an organization by language|
|[**get_languages_translations_user**](#get_languages_translations_user) | Get effective language translation for a user|
|[**post_languages**](#post_languages) | Create Language (Deprecated)|



## delete_language

>  delete_language(language_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Delete Language (Deprecated)

This endpoint is deprecated. Please see the Routing API (DELETE /api/v2/routing/languages/{languageId})

Wraps DELETE /api/v2/languages/{languageId} 

Requires ANY permissions: 

* routing:skill:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguagesApi()
language_id = 'language_id_example' # str | Language ID

try:
    # Delete Language (Deprecated)
    api_instance.delete_language(language_id)
except ApiException as e:
    print("Exception when calling LanguagesApi->delete_language: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language_id** | **str**| Language ID |  |

### Return type

void (empty response body)


## get_language

> [**Language**](Language) get_language(language_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get Language (Deprecated)

This endpoint is deprecated. Please see the Routing API (GET /api/v2/routing/languages/{languageId})

Wraps GET /api/v2/languages/{languageId} 

Requires ANY permissions: 

* routing:skill:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguagesApi()
language_id = 'language_id_example' # str | Language ID

try:
    # Get Language (Deprecated)
    api_response = api_instance.get_language(language_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->get_language: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language_id** | **str**| Language ID |  |

### Return type

[**Language**](Language)


## get_languages

> [**LanguageEntityListing**](LanguageEntityListing) get_languages(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get the list of supported languages. (Deprecated)

This endpoint is deprecated. Please see the Routing API (GET /api/v2/routing/languages)

Wraps GET /api/v2/languages 

Requires ANY permissions: 

* routing:skill:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguagesApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = ''ASC'' # str | Ascending or descending sort order (optional) (default to 'ASC')
name = 'name_example' # str | Name (optional)

try:
    # Get the list of supported languages. (Deprecated)
    api_response = api_instance.get_languages(page_size=page_size, page_number=page_number, sort_order=sort_order, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->get_languages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to &#39;ASC&#39;]<br />**Values**: ascending, descending |
| **name** | **str**| Name | [optional]  |

### Return type

[**LanguageEntityListing**](LanguageEntityListing)


## get_languages_translations

> [**AvailableTranslations**](AvailableTranslations) get_languages_translations()


Get all available languages for translation

Wraps GET /api/v2/languages/translations 

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
api_instance = PureCloudPlatformClientV2.LanguagesApi()

try:
    # Get all available languages for translation
    api_response = api_instance.get_languages_translations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->get_languages_translations: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**AvailableTranslations**](AvailableTranslations)


## get_languages_translations_builtin

> dict(str, object)** get_languages_translations_builtin(language)


Get the builtin translation for a language

Wraps GET /api/v2/languages/translations/builtin 

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
api_instance = PureCloudPlatformClientV2.LanguagesApi()
language = 'language_example' # str | The language of the builtin translation to retrieve

try:
    # Get the builtin translation for a language
    api_response = api_instance.get_languages_translations_builtin(language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->get_languages_translations_builtin: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language** | **str**| The language of the builtin translation to retrieve |  |

### Return type

**dict(str, object)**


## get_languages_translations_organization

> dict(str, object)** get_languages_translations_organization(language)


Get effective translation for an organization by language

Wraps GET /api/v2/languages/translations/organization 

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
api_instance = PureCloudPlatformClientV2.LanguagesApi()
language = 'language_example' # str | The language of the translation to retrieve for the organization

try:
    # Get effective translation for an organization by language
    api_response = api_instance.get_languages_translations_organization(language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->get_languages_translations_organization: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language** | **str**| The language of the translation to retrieve for the organization |  |

### Return type

**dict(str, object)**


## get_languages_translations_user

> dict(str, object)** get_languages_translations_user(user_id)


Get effective language translation for a user

Wraps GET /api/v2/languages/translations/users/{userId} 

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
api_instance = PureCloudPlatformClientV2.LanguagesApi()
user_id = 'user_id_example' # str | The user id

try:
    # Get effective language translation for a user
    api_response = api_instance.get_languages_translations_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->get_languages_translations_user: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The user id |  |

### Return type

**dict(str, object)**


## post_languages

> [**Language**](Language) post_languages(body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Create Language (Deprecated)

This endpoint is deprecated. Please see the Routing API. (POST /api/v2/routing/languages

Wraps POST /api/v2/languages 

Requires ANY permissions: 

* routing:skill:manage

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LanguagesApi()
body = PureCloudPlatformClientV2.Language() # Language | Language

try:
    # Create Language (Deprecated)
    api_response = api_instance.post_languages(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->post_languages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Language**](Language)| Language |  |

### Return type

[**Language**](Language)


_PureCloudPlatformClientV2 246.0.0_

# SocialMediaApi

## PureCloudPlatformClientV2.SocialMediaApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_socialmedia_topic**](#delete_socialmedia_topic) | Delete a social topic.|
|[**delete_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id**](#delete_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id) | Delete a Facebook data ingestion rule.|
|[**delete_socialmedia_topic_dataingestionrules_open_open_id**](#delete_socialmedia_topic_dataingestionrules_open_open_id) | Delete a open data ingestion rule.|
|[**delete_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id**](#delete_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id) | Delete a X (formally Twitter) data ingestion rule.|
|[**get_socialmedia_topic**](#get_socialmedia_topic) | Get a single social topic.|
|[**get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id**](#get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id) | Get a single Facebook data ingestion rule.|
|[**get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_version**](#get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_version) | Get a single Facebook data ingestion rule version.|
|[**get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_versions**](#get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_versions) | Get the Facebook data ingestion rule versions.|
|[**get_socialmedia_topic_dataingestionrules_open_open_id**](#get_socialmedia_topic_dataingestionrules_open_open_id) | Get a single open data ingestion rule.|
|[**get_socialmedia_topic_dataingestionrules_open_open_id_version**](#get_socialmedia_topic_dataingestionrules_open_open_id_version) | Get a single Open data ingestion rule version.|
|[**get_socialmedia_topic_dataingestionrules_open_open_id_versions**](#get_socialmedia_topic_dataingestionrules_open_open_id_versions) | Get the Open data ingestion rule versions.|
|[**get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id**](#get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id) | Get a single X (formally Twitter) data ingestion rule.|
|[**get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_version**](#get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_version) | Get a single X (formally Twitter) data ingestion rule version.|
|[**get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_versions**](#get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_versions) | Get the Open data ingestion rule versions.|
|[**get_socialmedia_topics**](#get_socialmedia_topics) | Retrieve all social topics.|
|[**patch_socialmedia_topic**](#patch_socialmedia_topic) | Update a social topic.|
|[**patch_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id**](#patch_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id) | Update the status of a Facebook data ingestion rule.|
|[**patch_socialmedia_topic_dataingestionrules_open_open_id**](#patch_socialmedia_topic_dataingestionrules_open_open_id) | Update the status of a open data ingestion rule.|
|[**patch_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id**](#patch_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id) | Update the status of a X (formally Twitter) data ingestion rule.|
|[**post_socialmedia_topic_dataingestionrules_facebook**](#post_socialmedia_topic_dataingestionrules_facebook) | Create an Facebook data ingestion rule.|
|[**post_socialmedia_topic_dataingestionrules_open**](#post_socialmedia_topic_dataingestionrules_open) | Create an open data ingestion rule.|
|[**post_socialmedia_topic_dataingestionrules_twitter**](#post_socialmedia_topic_dataingestionrules_twitter) | Create an twitter data ingestion rule.|
|[**post_socialmedia_topics**](#post_socialmedia_topics) | Create a social topic.|
|[**put_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id**](#put_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id) | Update the Facebook data ingestion rule.|
|[**put_socialmedia_topic_dataingestionrules_open_open_id**](#put_socialmedia_topic_dataingestionrules_open_open_id) | Update the open data ingestion rule.|
|[**put_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id**](#put_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id) | Update the X (formally Twitter) data ingestion rule.|



## delete_socialmedia_topic

>  delete_socialmedia_topic(topic_id, hard_delete=hard_delete)


Delete a social topic.

delete_socialmedia_topic is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/socialmedia/topics/{topicId} 

Requires ANY permissions: 

* socialmedia:topic:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
hard_delete = True # bool | Determines whether a Social topic should be soft-deleted or hard-deleted (permanently removed). Set to false (soft-delete) by default. (optional)

try:
    # Delete a social topic.
    api_instance.delete_socialmedia_topic(topic_id, hard_delete=hard_delete)
except ApiException as e:
    print("Exception when calling SocialMediaApi->delete_socialmedia_topic: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **hard_delete** | **bool**| Determines whether a Social topic should be soft-deleted or hard-deleted (permanently removed). Set to false (soft-delete) by default. | [optional]  |

### Return type

void (empty response body)


## delete_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id

>  delete_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id(topic_id, facebook_ingestion_rule_id, hard_delete=hard_delete)


Delete a Facebook data ingestion rule.

delete_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/socialmedia/topics/{topicId}/dataingestionrules/facebook/{facebookIngestionRuleId} 

Requires ANY permissions: 

* socialmedia:facebookDataIngestionRule:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
facebook_ingestion_rule_id = 'facebook_ingestion_rule_id_example' # str | facebookIngestionRuleId
hard_delete = False # bool | Determines whether a Facebook data ingestion rule should be soft-deleted (have it's state set to deleted) or hard-deleted (permanently removed). Set to false (soft-delete) by default. (optional) (default to False)

try:
    # Delete a Facebook data ingestion rule.
    api_instance.delete_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id(topic_id, facebook_ingestion_rule_id, hard_delete=hard_delete)
except ApiException as e:
    print("Exception when calling SocialMediaApi->delete_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **facebook_ingestion_rule_id** | **str**| facebookIngestionRuleId |  |
| **hard_delete** | **bool**| Determines whether a Facebook data ingestion rule should be soft-deleted (have it&#39;s state set to deleted) or hard-deleted (permanently removed). Set to false (soft-delete) by default. | [optional] [default to False] |

### Return type

void (empty response body)


## delete_socialmedia_topic_dataingestionrules_open_open_id

>  delete_socialmedia_topic_dataingestionrules_open_open_id(topic_id, open_id, hard_delete=hard_delete)


Delete a open data ingestion rule.

delete_socialmedia_topic_dataingestionrules_open_open_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/socialmedia/topics/{topicId}/dataingestionrules/open/{openId} 

Requires ANY permissions: 

* socialmedia:openDataIngestionRule:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
open_id = 'open_id_example' # str | openId
hard_delete = False # bool | Determines whether a open data ingestion rule should be soft-deleted (have it's state set to deleted) or hard-deleted (permanently removed). Set to false (soft-delete) by default. (optional) (default to False)

try:
    # Delete a open data ingestion rule.
    api_instance.delete_socialmedia_topic_dataingestionrules_open_open_id(topic_id, open_id, hard_delete=hard_delete)
except ApiException as e:
    print("Exception when calling SocialMediaApi->delete_socialmedia_topic_dataingestionrules_open_open_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **open_id** | **str**| openId |  |
| **hard_delete** | **bool**| Determines whether a open data ingestion rule should be soft-deleted (have it&#39;s state set to deleted) or hard-deleted (permanently removed). Set to false (soft-delete) by default. | [optional] [default to False] |

### Return type

void (empty response body)


## delete_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id

>  delete_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id(topic_id, twitter_ingestion_rule_id, hard_delete=hard_delete)


Delete a X (formally Twitter) data ingestion rule.

delete_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/socialmedia/topics/{topicId}/dataingestionrules/twitter/{twitterIngestionRuleId} 

Requires ANY permissions: 

* socialmedia:twitterDataIngestionRule:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
twitter_ingestion_rule_id = 'twitter_ingestion_rule_id_example' # str | twitterIngestionRuleId
hard_delete = False # bool | Determines whether a X (formally Twitter) data ingestion rule should be soft-deleted (have it's state set to deleted) or hard-deleted (permanently removed). Set to false (soft-delete) by default. (optional) (default to False)

try:
    # Delete a X (formally Twitter) data ingestion rule.
    api_instance.delete_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id(topic_id, twitter_ingestion_rule_id, hard_delete=hard_delete)
except ApiException as e:
    print("Exception when calling SocialMediaApi->delete_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **twitter_ingestion_rule_id** | **str**| twitterIngestionRuleId |  |
| **hard_delete** | **bool**| Determines whether a X (formally Twitter) data ingestion rule should be soft-deleted (have it&#39;s state set to deleted) or hard-deleted (permanently removed). Set to false (soft-delete) by default. | [optional] [default to False] |

### Return type

void (empty response body)


## get_socialmedia_topic

> [**SocialTopicResponse**](SocialTopicResponse) get_socialmedia_topic(topic_id, include_deleted=include_deleted)


Get a single social topic.

get_socialmedia_topic is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/socialmedia/topics/{topicId} 

Requires ANY permissions: 

* socialmedia:topic:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
include_deleted = True # bool | Determines whether to include soft-deleted items in the result. (optional)

try:
    # Get a single social topic.
    api_response = api_instance.get_socialmedia_topic(topic_id, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topic: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **include_deleted** | **bool**| Determines whether to include soft-deleted items in the result. | [optional]  |

### Return type

[**SocialTopicResponse**](SocialTopicResponse)


## get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id

> [**FacebookDataIngestionRuleResponse**](FacebookDataIngestionRuleResponse) get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id(topic_id, facebook_ingestion_rule_id, include_deleted=include_deleted)


Get a single Facebook data ingestion rule.

get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/socialmedia/topics/{topicId}/dataingestionrules/facebook/{facebookIngestionRuleId} 

Requires ALL permissions: 

* socialmedia:facebookDataIngestionRule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
facebook_ingestion_rule_id = 'facebook_ingestion_rule_id_example' # str | facebookIngestionRuleId
include_deleted = True # bool | Determines whether to include soft-deleted items in the result. (optional)

try:
    # Get a single Facebook data ingestion rule.
    api_response = api_instance.get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id(topic_id, facebook_ingestion_rule_id, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **facebook_ingestion_rule_id** | **str**| facebookIngestionRuleId |  |
| **include_deleted** | **bool**| Determines whether to include soft-deleted items in the result. | [optional]  |

### Return type

[**FacebookDataIngestionRuleResponse**](FacebookDataIngestionRuleResponse)


## get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_version

> [**FacebookDataIngestionRuleVersionResponse**](FacebookDataIngestionRuleVersionResponse) get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_version(topic_id, facebook_ingestion_rule_id, data_ingestion_rule_version, include_deleted=include_deleted)


Get a single Facebook data ingestion rule version.

get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_version is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/socialmedia/topics/{topicId}/dataingestionrules/facebook/{facebookIngestionRuleId}/versions/{dataIngestionRuleVersion} 

Requires ALL permissions: 

* socialmedia:facebookDataIngestionRule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
facebook_ingestion_rule_id = 'facebook_ingestion_rule_id_example' # str | facebookIngestionRuleId
data_ingestion_rule_version = 'data_ingestion_rule_version_example' # str | version
include_deleted = True # bool | Determines whether to include soft-deleted item in the result. (optional)

try:
    # Get a single Facebook data ingestion rule version.
    api_response = api_instance.get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_version(topic_id, facebook_ingestion_rule_id, data_ingestion_rule_version, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **facebook_ingestion_rule_id** | **str**| facebookIngestionRuleId |  |
| **data_ingestion_rule_version** | **str**| version |  |
| **include_deleted** | **bool**| Determines whether to include soft-deleted item in the result. | [optional]  |

### Return type

[**FacebookDataIngestionRuleVersionResponse**](FacebookDataIngestionRuleVersionResponse)


## get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_versions

> [**FacebookDataIngestionRuleVersionResponseEntityListing**](FacebookDataIngestionRuleVersionResponseEntityListing) get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_versions(topic_id, facebook_ingestion_rule_id, page_number=page_number, page_size=page_size, include_deleted=include_deleted)


Get the Facebook data ingestion rule versions.

get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_versions is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/socialmedia/topics/{topicId}/dataingestionrules/facebook/{facebookIngestionRuleId}/versions 

Requires ALL permissions: 

* socialmedia:facebookDataIngestionRule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
facebook_ingestion_rule_id = 'facebook_ingestion_rule_id_example' # str | facebookIngestionRuleId
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
include_deleted = True # bool | Determines whether to include soft-deleted items in the result. (optional)

try:
    # Get the Facebook data ingestion rule versions.
    api_response = api_instance.get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_versions(topic_id, facebook_ingestion_rule_id, page_number=page_number, page_size=page_size, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **facebook_ingestion_rule_id** | **str**| facebookIngestionRuleId |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **include_deleted** | **bool**| Determines whether to include soft-deleted items in the result. | [optional]  |

### Return type

[**FacebookDataIngestionRuleVersionResponseEntityListing**](FacebookDataIngestionRuleVersionResponseEntityListing)


## get_socialmedia_topic_dataingestionrules_open_open_id

> [**OpenDataIngestionRuleResponse**](OpenDataIngestionRuleResponse) get_socialmedia_topic_dataingestionrules_open_open_id(topic_id, open_id, include_deleted=include_deleted)


Get a single open data ingestion rule.

get_socialmedia_topic_dataingestionrules_open_open_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/socialmedia/topics/{topicId}/dataingestionrules/open/{openId} 

Requires ALL permissions: 

* socialmedia:openDataIngestionRule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
open_id = 'open_id_example' # str | openId
include_deleted = True # bool | Determines whether to include soft-deleted items in the result. (optional)

try:
    # Get a single open data ingestion rule.
    api_response = api_instance.get_socialmedia_topic_dataingestionrules_open_open_id(topic_id, open_id, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topic_dataingestionrules_open_open_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **open_id** | **str**| openId |  |
| **include_deleted** | **bool**| Determines whether to include soft-deleted items in the result. | [optional]  |

### Return type

[**OpenDataIngestionRuleResponse**](OpenDataIngestionRuleResponse)


## get_socialmedia_topic_dataingestionrules_open_open_id_version

> [**OpenDataIngestionRuleVersionResponse**](OpenDataIngestionRuleVersionResponse) get_socialmedia_topic_dataingestionrules_open_open_id_version(topic_id, open_id, data_ingestion_rule_version, include_deleted=include_deleted)


Get a single Open data ingestion rule version.

get_socialmedia_topic_dataingestionrules_open_open_id_version is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/socialmedia/topics/{topicId}/dataingestionrules/open/{openId}/versions/{dataIngestionRuleVersion} 

Requires ALL permissions: 

* socialmedia:openDataIngestionRule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
open_id = 'open_id_example' # str | openId
data_ingestion_rule_version = 'data_ingestion_rule_version_example' # str | version
include_deleted = True # bool | Determines whether to include soft-deleted item in the result. (optional)

try:
    # Get a single Open data ingestion rule version.
    api_response = api_instance.get_socialmedia_topic_dataingestionrules_open_open_id_version(topic_id, open_id, data_ingestion_rule_version, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topic_dataingestionrules_open_open_id_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **open_id** | **str**| openId |  |
| **data_ingestion_rule_version** | **str**| version |  |
| **include_deleted** | **bool**| Determines whether to include soft-deleted item in the result. | [optional]  |

### Return type

[**OpenDataIngestionRuleVersionResponse**](OpenDataIngestionRuleVersionResponse)


## get_socialmedia_topic_dataingestionrules_open_open_id_versions

> [**OpenDataIngestionRuleVersionResponseEntityListing**](OpenDataIngestionRuleVersionResponseEntityListing) get_socialmedia_topic_dataingestionrules_open_open_id_versions(topic_id, open_id, page_number=page_number, page_size=page_size, include_deleted=include_deleted)


Get the Open data ingestion rule versions.

get_socialmedia_topic_dataingestionrules_open_open_id_versions is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/socialmedia/topics/{topicId}/dataingestionrules/open/{openId}/versions 

Requires ALL permissions: 

* socialmedia:openDataIngestionRule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
open_id = 'open_id_example' # str | openId
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
include_deleted = True # bool | Determines whether to include soft-deleted items in the result. (optional)

try:
    # Get the Open data ingestion rule versions.
    api_response = api_instance.get_socialmedia_topic_dataingestionrules_open_open_id_versions(topic_id, open_id, page_number=page_number, page_size=page_size, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topic_dataingestionrules_open_open_id_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **open_id** | **str**| openId |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **include_deleted** | **bool**| Determines whether to include soft-deleted items in the result. | [optional]  |

### Return type

[**OpenDataIngestionRuleVersionResponseEntityListing**](OpenDataIngestionRuleVersionResponseEntityListing)


## get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id

> [**TwitterDataIngestionRuleResponse**](TwitterDataIngestionRuleResponse) get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id(topic_id, twitter_ingestion_rule_id, include_deleted=include_deleted)


Get a single X (formally Twitter) data ingestion rule.

get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/socialmedia/topics/{topicId}/dataingestionrules/twitter/{twitterIngestionRuleId} 

Requires ALL permissions: 

* socialmedia:twitterDataIngestionRule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
twitter_ingestion_rule_id = 'twitter_ingestion_rule_id_example' # str | twitterIngestionRuleId
include_deleted = True # bool | Determines whether to include soft-deleted items in the result. (optional)

try:
    # Get a single X (formally Twitter) data ingestion rule.
    api_response = api_instance.get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id(topic_id, twitter_ingestion_rule_id, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **twitter_ingestion_rule_id** | **str**| twitterIngestionRuleId |  |
| **include_deleted** | **bool**| Determines whether to include soft-deleted items in the result. | [optional]  |

### Return type

[**TwitterDataIngestionRuleResponse**](TwitterDataIngestionRuleResponse)


## get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_version

> [**TwitterDataIngestionRuleVersionResponse**](TwitterDataIngestionRuleVersionResponse) get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_version(topic_id, twitter_ingestion_rule_id, data_ingestion_rule_version, include_deleted=include_deleted)


Get a single X (formally Twitter) data ingestion rule version.

get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_version is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/socialmedia/topics/{topicId}/dataingestionrules/twitter/{twitterIngestionRuleId}/versions/{dataIngestionRuleVersion} 

Requires ALL permissions: 

* socialmedia:twitterDataIngestionRule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
twitter_ingestion_rule_id = 'twitter_ingestion_rule_id_example' # str | twitterIngestionRuleId
data_ingestion_rule_version = 'data_ingestion_rule_version_example' # str | version
include_deleted = True # bool | Determines whether to include soft-deleted item in the result. (optional)

try:
    # Get a single X (formally Twitter) data ingestion rule version.
    api_response = api_instance.get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_version(topic_id, twitter_ingestion_rule_id, data_ingestion_rule_version, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **twitter_ingestion_rule_id** | **str**| twitterIngestionRuleId |  |
| **data_ingestion_rule_version** | **str**| version |  |
| **include_deleted** | **bool**| Determines whether to include soft-deleted item in the result. | [optional]  |

### Return type

[**TwitterDataIngestionRuleVersionResponse**](TwitterDataIngestionRuleVersionResponse)


## get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_versions

> [**TwitterDataIngestionRuleVersionResponseEntityListing**](TwitterDataIngestionRuleVersionResponseEntityListing) get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_versions(topic_id, twitter_ingestion_rule_id, page_number=page_number, page_size=page_size, include_deleted=include_deleted)


Get the Open data ingestion rule versions.

get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_versions is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/socialmedia/topics/{topicId}/dataingestionrules/twitter/{twitterIngestionRuleId}/versions 

Requires ALL permissions: 

* socialmedia:twitterDataIngestionRule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
twitter_ingestion_rule_id = 'twitter_ingestion_rule_id_example' # str | twitterIngestionRuleId
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
include_deleted = True # bool | Determines whether to include soft-deleted items in the result. (optional)

try:
    # Get the Open data ingestion rule versions.
    api_response = api_instance.get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_versions(topic_id, twitter_ingestion_rule_id, page_number=page_number, page_size=page_size, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **twitter_ingestion_rule_id** | **str**| twitterIngestionRuleId |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **include_deleted** | **bool**| Determines whether to include soft-deleted items in the result. | [optional]  |

### Return type

[**TwitterDataIngestionRuleVersionResponseEntityListing**](TwitterDataIngestionRuleVersionResponseEntityListing)


## get_socialmedia_topics

> [**SocialTopicResponseEntityListing**](SocialTopicResponseEntityListing) get_socialmedia_topics(page_number=page_number, page_size=page_size, division_ids=division_ids, include_deleted=include_deleted)


Retrieve all social topics.

get_socialmedia_topics is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/socialmedia/topics 

Requires ANY permissions: 

* socialmedia:topic:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
division_ids = ['division_ids_example'] # list[str] | One or more division IDs. If nothing is provided, the social topics associated withthe list of divisions that the user has access to will be returned. (optional)
include_deleted = True # bool | Determines whether to include soft-deleted items in the result. (optional)

try:
    # Retrieve all social topics.
    api_response = api_instance.get_socialmedia_topics(page_number=page_number, page_size=page_size, division_ids=division_ids, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **division_ids** | [**list[str]**](str)| One or more division IDs. If nothing is provided, the social topics associated withthe list of divisions that the user has access to will be returned. | [optional]  |
| **include_deleted** | **bool**| Determines whether to include soft-deleted items in the result. | [optional]  |

### Return type

[**SocialTopicResponseEntityListing**](SocialTopicResponseEntityListing)


## patch_socialmedia_topic

> [**SocialTopicResponse**](SocialTopicResponse) patch_socialmedia_topic(topic_id, body=body)


Update a social topic.

patch_socialmedia_topic is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/socialmedia/topics/{topicId} 

Requires ALL permissions: 

* socialmedia:topic:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
body = PureCloudPlatformClientV2.SocialTopicPatchRequest() # SocialTopicPatchRequest |  (optional)

try:
    # Update a social topic.
    api_response = api_instance.patch_socialmedia_topic(topic_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->patch_socialmedia_topic: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **body** | [**SocialTopicPatchRequest**](SocialTopicPatchRequest)|  | [optional]  |

### Return type

[**SocialTopicResponse**](SocialTopicResponse)


## patch_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id

> [**FacebookDataIngestionRuleResponse**](FacebookDataIngestionRuleResponse) patch_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id(topic_id, facebook_ingestion_rule_id, body=body)


Update the status of a Facebook data ingestion rule.

patch_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/socialmedia/topics/{topicId}/dataingestionrules/facebook/{facebookIngestionRuleId} 

Requires ALL permissions: 

* socialmedia:facebookDataIngestionRule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
facebook_ingestion_rule_id = 'facebook_ingestion_rule_id_example' # str | facebookIngestionRuleId
body = PureCloudPlatformClientV2.DataIngestionRuleStatusPatchRequest() # DataIngestionRuleStatusPatchRequest |  (optional)

try:
    # Update the status of a Facebook data ingestion rule.
    api_response = api_instance.patch_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id(topic_id, facebook_ingestion_rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->patch_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **facebook_ingestion_rule_id** | **str**| facebookIngestionRuleId |  |
| **body** | [**DataIngestionRuleStatusPatchRequest**](DataIngestionRuleStatusPatchRequest)|  | [optional]  |

### Return type

[**FacebookDataIngestionRuleResponse**](FacebookDataIngestionRuleResponse)


## patch_socialmedia_topic_dataingestionrules_open_open_id

> [**OpenDataIngestionRuleResponse**](OpenDataIngestionRuleResponse) patch_socialmedia_topic_dataingestionrules_open_open_id(topic_id, open_id, body=body)


Update the status of a open data ingestion rule.

patch_socialmedia_topic_dataingestionrules_open_open_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/socialmedia/topics/{topicId}/dataingestionrules/open/{openId} 

Requires ALL permissions: 

* socialmedia:openDataIngestionRule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
open_id = 'open_id_example' # str | openId
body = PureCloudPlatformClientV2.DataIngestionRuleStatusPatchRequest() # DataIngestionRuleStatusPatchRequest |  (optional)

try:
    # Update the status of a open data ingestion rule.
    api_response = api_instance.patch_socialmedia_topic_dataingestionrules_open_open_id(topic_id, open_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->patch_socialmedia_topic_dataingestionrules_open_open_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **open_id** | **str**| openId |  |
| **body** | [**DataIngestionRuleStatusPatchRequest**](DataIngestionRuleStatusPatchRequest)|  | [optional]  |

### Return type

[**OpenDataIngestionRuleResponse**](OpenDataIngestionRuleResponse)


## patch_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id

> [**TwitterDataIngestionRuleResponse**](TwitterDataIngestionRuleResponse) patch_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id(topic_id, twitter_ingestion_rule_id, body=body)


Update the status of a X (formally Twitter) data ingestion rule.

patch_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/socialmedia/topics/{topicId}/dataingestionrules/twitter/{twitterIngestionRuleId} 

Requires ALL permissions: 

* socialmedia:twitterDataIngestionRule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
twitter_ingestion_rule_id = 'twitter_ingestion_rule_id_example' # str | twitterIngestionRuleId
body = PureCloudPlatformClientV2.DataIngestionRuleStatusPatchRequest() # DataIngestionRuleStatusPatchRequest |  (optional)

try:
    # Update the status of a X (formally Twitter) data ingestion rule.
    api_response = api_instance.patch_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id(topic_id, twitter_ingestion_rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->patch_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **twitter_ingestion_rule_id** | **str**| twitterIngestionRuleId |  |
| **body** | [**DataIngestionRuleStatusPatchRequest**](DataIngestionRuleStatusPatchRequest)|  | [optional]  |

### Return type

[**TwitterDataIngestionRuleResponse**](TwitterDataIngestionRuleResponse)


## post_socialmedia_topic_dataingestionrules_facebook

> [**FacebookDataIngestionRuleResponse**](FacebookDataIngestionRuleResponse) post_socialmedia_topic_dataingestionrules_facebook(topic_id, body=body)


Create an Facebook data ingestion rule.

post_socialmedia_topic_dataingestionrules_facebook is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/socialmedia/topics/{topicId}/dataingestionrules/facebook 

Requires ANY permissions: 

* socialmedia:facebookDataIngestionRule:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
body = PureCloudPlatformClientV2.FacebookDataIngestionRuleRequest() # FacebookDataIngestionRuleRequest |  (optional)

try:
    # Create an Facebook data ingestion rule.
    api_response = api_instance.post_socialmedia_topic_dataingestionrules_facebook(topic_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->post_socialmedia_topic_dataingestionrules_facebook: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **body** | [**FacebookDataIngestionRuleRequest**](FacebookDataIngestionRuleRequest)|  | [optional]  |

### Return type

[**FacebookDataIngestionRuleResponse**](FacebookDataIngestionRuleResponse)


## post_socialmedia_topic_dataingestionrules_open

> [**OpenDataIngestionRuleResponse**](OpenDataIngestionRuleResponse) post_socialmedia_topic_dataingestionrules_open(topic_id, body=body)


Create an open data ingestion rule.

post_socialmedia_topic_dataingestionrules_open is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/socialmedia/topics/{topicId}/dataingestionrules/open 

Requires ANY permissions: 

* socialmedia:openDataIngestionRule:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
body = PureCloudPlatformClientV2.OpenDataIngestionRuleRequest() # OpenDataIngestionRuleRequest |  (optional)

try:
    # Create an open data ingestion rule.
    api_response = api_instance.post_socialmedia_topic_dataingestionrules_open(topic_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->post_socialmedia_topic_dataingestionrules_open: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **body** | [**OpenDataIngestionRuleRequest**](OpenDataIngestionRuleRequest)|  | [optional]  |

### Return type

[**OpenDataIngestionRuleResponse**](OpenDataIngestionRuleResponse)


## post_socialmedia_topic_dataingestionrules_twitter

> [**TwitterDataIngestionRuleResponse**](TwitterDataIngestionRuleResponse) post_socialmedia_topic_dataingestionrules_twitter(topic_id, body=body)


Create an twitter data ingestion rule.

post_socialmedia_topic_dataingestionrules_twitter is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/socialmedia/topics/{topicId}/dataingestionrules/twitter 

Requires ANY permissions: 

* socialmedia:twitterDataIngestionRule:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
body = PureCloudPlatformClientV2.TwitterDataIngestionRuleRequest() # TwitterDataIngestionRuleRequest |  (optional)

try:
    # Create an twitter data ingestion rule.
    api_response = api_instance.post_socialmedia_topic_dataingestionrules_twitter(topic_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->post_socialmedia_topic_dataingestionrules_twitter: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **body** | [**TwitterDataIngestionRuleRequest**](TwitterDataIngestionRuleRequest)|  | [optional]  |

### Return type

[**TwitterDataIngestionRuleResponse**](TwitterDataIngestionRuleResponse)


## post_socialmedia_topics

> [**SocialTopicResponse**](SocialTopicResponse) post_socialmedia_topics(body=body)


Create a social topic.

post_socialmedia_topics is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/socialmedia/topics 

Requires ANY permissions: 

* socialmedia:topic:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
body = PureCloudPlatformClientV2.SocialTopicRequest() # SocialTopicRequest |  (optional)

try:
    # Create a social topic.
    api_response = api_instance.post_socialmedia_topics(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->post_socialmedia_topics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SocialTopicRequest**](SocialTopicRequest)|  | [optional]  |

### Return type

[**SocialTopicResponse**](SocialTopicResponse)


## put_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id

> [**FacebookDataIngestionRuleResponse**](FacebookDataIngestionRuleResponse) put_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id(topic_id, facebook_ingestion_rule_id, body=body)


Update the Facebook data ingestion rule.

put_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PUT /api/v2/socialmedia/topics/{topicId}/dataingestionrules/facebook/{facebookIngestionRuleId} 

Requires ALL permissions: 

* socialmedia:facebookDataIngestionRule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
facebook_ingestion_rule_id = 'facebook_ingestion_rule_id_example' # str | facebookIngestionRuleId
body = PureCloudPlatformClientV2.FacebookDataIngestionRuleRequest() # FacebookDataIngestionRuleRequest |  (optional)

try:
    # Update the Facebook data ingestion rule.
    api_response = api_instance.put_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id(topic_id, facebook_ingestion_rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->put_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **facebook_ingestion_rule_id** | **str**| facebookIngestionRuleId |  |
| **body** | [**FacebookDataIngestionRuleRequest**](FacebookDataIngestionRuleRequest)|  | [optional]  |

### Return type

[**FacebookDataIngestionRuleResponse**](FacebookDataIngestionRuleResponse)


## put_socialmedia_topic_dataingestionrules_open_open_id

> [**OpenDataIngestionRuleResponse**](OpenDataIngestionRuleResponse) put_socialmedia_topic_dataingestionrules_open_open_id(topic_id, open_id, body=body)


Update the open data ingestion rule.

put_socialmedia_topic_dataingestionrules_open_open_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PUT /api/v2/socialmedia/topics/{topicId}/dataingestionrules/open/{openId} 

Requires ALL permissions: 

* socialmedia:openDataIngestionRule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
open_id = 'open_id_example' # str | openId
body = PureCloudPlatformClientV2.OpenDataIngestionRuleRequest() # OpenDataIngestionRuleRequest |  (optional)

try:
    # Update the open data ingestion rule.
    api_response = api_instance.put_socialmedia_topic_dataingestionrules_open_open_id(topic_id, open_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->put_socialmedia_topic_dataingestionrules_open_open_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **open_id** | **str**| openId |  |
| **body** | [**OpenDataIngestionRuleRequest**](OpenDataIngestionRuleRequest)|  | [optional]  |

### Return type

[**OpenDataIngestionRuleResponse**](OpenDataIngestionRuleResponse)


## put_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id

> [**TwitterDataIngestionRuleResponse**](TwitterDataIngestionRuleResponse) put_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id(topic_id, twitter_ingestion_rule_id, body=body)


Update the X (formally Twitter) data ingestion rule.

put_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PUT /api/v2/socialmedia/topics/{topicId}/dataingestionrules/twitter/{twitterIngestionRuleId} 

Requires ALL permissions: 

* socialmedia:twitterDataIngestionRule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SocialMediaApi()
topic_id = 'topic_id_example' # str | topicId
twitter_ingestion_rule_id = 'twitter_ingestion_rule_id_example' # str | twitterIngestionRuleId
body = PureCloudPlatformClientV2.TwitterDataIngestionRuleRequest() # TwitterDataIngestionRuleRequest |  (optional)

try:
    # Update the X (formally Twitter) data ingestion rule.
    api_response = api_instance.put_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id(topic_id, twitter_ingestion_rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->put_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **twitter_ingestion_rule_id** | **str**| twitterIngestionRuleId |  |
| **body** | [**TwitterDataIngestionRuleRequest**](TwitterDataIngestionRuleRequest)|  | [optional]  |

### Return type

[**TwitterDataIngestionRuleResponse**](TwitterDataIngestionRuleResponse)


_PureCloudPlatformClientV2 221.0.0_

# SocialMediaApi

## PureCloudPlatformClientV2.SocialMediaApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_socialmedia_escalationrule**](#delete_socialmedia_escalationrule) | Delete an escalation rule.|
|[**delete_socialmedia_message**](#delete_socialmedia_message) | Delete a social media message.|
|[**delete_socialmedia_topic**](#delete_socialmedia_topic) | Delete a social topic.|
|[**delete_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id**](#delete_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id) | Delete a Facebook data ingestion rule.|
|[**delete_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id**](#delete_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id) | Delete a Instagram data ingestion rule.|
|[**delete_socialmedia_topic_dataingestionrules_open_open_id**](#delete_socialmedia_topic_dataingestionrules_open_open_id) | Delete a open data ingestion rule.|
|[**delete_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id**](#delete_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id) | Delete a X (formally Twitter) data ingestion rule.|
|[**get_socialmedia_analytics_aggregates_job**](#get_socialmedia_analytics_aggregates_job) | Get status for async query for social media aggregates|
|[**get_socialmedia_analytics_aggregates_job_results**](#get_socialmedia_analytics_aggregates_job_results) | Fetch a page of results for an async social media query|
|[**get_socialmedia_analytics_messages_job**](#get_socialmedia_analytics_messages_job) | Get status for async query for social media messages job|
|[**get_socialmedia_analytics_messages_job_results**](#get_socialmedia_analytics_messages_job_results) | Fetch a page of results for an async social media messages query|
|[**get_socialmedia_escalationrule**](#get_socialmedia_escalationrule) | Get a single escalation rule.|
|[**get_socialmedia_escalationrules**](#get_socialmedia_escalationrules) | Retrieve all escalation rules for a division.|
|[**get_socialmedia_topic**](#get_socialmedia_topic) | Get a single social topic.|
|[**get_socialmedia_topic_dataingestionrules**](#get_socialmedia_topic_dataingestionrules) | Retrieve all social topic data ingestion rules with pagination.|
|[**get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id**](#get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id) | Get a single Facebook data ingestion rule.|
|[**get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_version**](#get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_version) | Get a single Facebook data ingestion rule version.|
|[**get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_versions**](#get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id_versions) | Get the Facebook data ingestion rule versions.|
|[**get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id**](#get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id) | Get a single Instagram data ingestion rule.|
|[**get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id_version**](#get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id_version) | Get a single Instagram data ingestion rule version.|
|[**get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id_versions**](#get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id_versions) | Get the Instagram data ingestion rule versions.|
|[**get_socialmedia_topic_dataingestionrules_open_open_id**](#get_socialmedia_topic_dataingestionrules_open_open_id) | Get a single open data ingestion rule.|
|[**get_socialmedia_topic_dataingestionrules_open_open_id_version**](#get_socialmedia_topic_dataingestionrules_open_open_id_version) | Get a single Open data ingestion rule version.|
|[**get_socialmedia_topic_dataingestionrules_open_open_id_versions**](#get_socialmedia_topic_dataingestionrules_open_open_id_versions) | Get the Open data ingestion rule versions.|
|[**get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id**](#get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id) | Get a single X (formally Twitter) data ingestion rule.|
|[**get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_version**](#get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_version) | Get a single X (formally Twitter) data ingestion rule version.|
|[**get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_versions**](#get_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id_versions) | Get the Open data ingestion rule versions.|
|[**get_socialmedia_topics**](#get_socialmedia_topics) | Retrieve all social topics.|
|[**patch_socialmedia_topic**](#patch_socialmedia_topic) | Update a social topic.|
|[**patch_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id**](#patch_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id) | Update the status of a Facebook data ingestion rule.|
|[**patch_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id**](#patch_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id) | Update the status of a Instagram data ingestion rule.|
|[**patch_socialmedia_topic_dataingestionrules_open_open_id**](#patch_socialmedia_topic_dataingestionrules_open_open_id) | Update the status of a open data ingestion rule.|
|[**patch_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id**](#patch_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id) | Update the status of a X (formally Twitter) data ingestion rule.|
|[**post_socialmedia_analytics_aggregates_jobs**](#post_socialmedia_analytics_aggregates_jobs) | Query for social media aggregates asynchronously|
|[**post_socialmedia_analytics_messages_jobs**](#post_socialmedia_analytics_messages_jobs) | Query for social media messages asynchronously|
|[**post_socialmedia_escalationrules**](#post_socialmedia_escalationrules) | Create an escalation rule.|
|[**post_socialmedia_escalations_messages**](#post_socialmedia_escalations_messages) | Escalate message to a conversation manually|
|[**post_socialmedia_topic_dataingestionrules_facebook**](#post_socialmedia_topic_dataingestionrules_facebook) | Create an Facebook data ingestion rule.|
|[**post_socialmedia_topic_dataingestionrules_instagram**](#post_socialmedia_topic_dataingestionrules_instagram) | Create an Instagram data ingestion rule.|
|[**post_socialmedia_topic_dataingestionrules_open**](#post_socialmedia_topic_dataingestionrules_open) | Create an open data ingestion rule.|
|[**post_socialmedia_topic_dataingestionrules_open_rule_id_messages_bulk**](#post_socialmedia_topic_dataingestionrules_open_rule_id_messages_bulk) | Ingest a list of Open Social Messages|
|[**post_socialmedia_topic_dataingestionrules_open_rule_id_reactions_bulk**](#post_socialmedia_topic_dataingestionrules_open_rule_id_reactions_bulk) | Ingest a list of Open Social Reactions|
|[**post_socialmedia_topic_dataingestionrules_twitter**](#post_socialmedia_topic_dataingestionrules_twitter) | Create an twitter data ingestion rule.|
|[**post_socialmedia_topics**](#post_socialmedia_topics) | Create a social topic.|
|[**post_socialmedia_twitter_historical_tweets**](#post_socialmedia_twitter_historical_tweets) | Retrieves historical tweet count for search terms, optional countries list and the current limit and usage for the organization.|
|[**put_socialmedia_escalationrule**](#put_socialmedia_escalationrule) | Update the escalation rule.|
|[**put_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id**](#put_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id) | Update the Facebook data ingestion rule.|
|[**put_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id**](#put_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id) | Update the Instagram data ingestion rule.|
|[**put_socialmedia_topic_dataingestionrules_open_open_id**](#put_socialmedia_topic_dataingestionrules_open_open_id) | Update the open data ingestion rule.|
|[**put_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id**](#put_socialmedia_topic_dataingestionrules_twitter_twitter_ingestion_rule_id) | Update the X (formally Twitter) data ingestion rule.|



## delete_socialmedia_escalationrule

>  delete_socialmedia_escalationrule(escalation_rule_id)


Delete an escalation rule.

Wraps DELETE /api/v2/socialmedia/escalationrules/{escalationRuleId} 

Requires ANY permissions: 

* socialmedia:escalationRules:delete

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
escalation_rule_id = 'escalation_rule_id_example' # str | escalationRuleId

try:
    # Delete an escalation rule.
    api_instance.delete_socialmedia_escalationrule(escalation_rule_id)
except ApiException as e:
    print("Exception when calling SocialMediaApi->delete_socialmedia_escalationrule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **escalation_rule_id** | **str**| escalationRuleId |  |

### Return type

void (empty response body)


## delete_socialmedia_message

>  delete_socialmedia_message(message_id)


Delete a social media message.

delete_socialmedia_message is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps DELETE /api/v2/socialmedia/messages/{messageId} 

Requires ANY permissions: 

* socialmedia:message:delete

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
message_id = 'message_id_example' # str | messageId

try:
    # Delete a social media message.
    api_instance.delete_socialmedia_message(message_id)
except ApiException as e:
    print("Exception when calling SocialMediaApi->delete_socialmedia_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_id** | **str**| messageId |  |

### Return type

void (empty response body)


## delete_socialmedia_topic

>  delete_socialmedia_topic(topic_id, hard_delete=hard_delete)


Delete a social topic.

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


## delete_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id

>  delete_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id(topic_id, instagram_ingestion_rule_id, hard_delete=hard_delete)


Delete a Instagram data ingestion rule.

Wraps DELETE /api/v2/socialmedia/topics/{topicId}/dataingestionrules/instagram/{instagramIngestionRuleId} 

Requires ANY permissions: 

* socialmedia:instagramDataIngestionRule:delete

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
instagram_ingestion_rule_id = 'instagram_ingestion_rule_id_example' # str | instagramIngestionRuleId
hard_delete = False # bool | Determines whether a Instagram data ingestion rule should be soft-deleted (have it's state set to deleted) or hard-deleted (permanently removed). Set to false (soft-delete) by default. (optional) (default to False)

try:
    # Delete a Instagram data ingestion rule.
    api_instance.delete_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id(topic_id, instagram_ingestion_rule_id, hard_delete=hard_delete)
except ApiException as e:
    print("Exception when calling SocialMediaApi->delete_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **instagram_ingestion_rule_id** | **str**| instagramIngestionRuleId |  |
| **hard_delete** | **bool**| Determines whether a Instagram data ingestion rule should be soft-deleted (have it&#39;s state set to deleted) or hard-deleted (permanently removed). Set to false (soft-delete) by default. | [optional] [default to False] |

### Return type

void (empty response body)


## delete_socialmedia_topic_dataingestionrules_open_open_id

>  delete_socialmedia_topic_dataingestionrules_open_open_id(topic_id, open_id, hard_delete=hard_delete)


Delete a open data ingestion rule.

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


## get_socialmedia_analytics_aggregates_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_socialmedia_analytics_aggregates_job(job_id)


Get status for async query for social media aggregates

Wraps GET /api/v2/socialmedia/analytics/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* socialmedia:postAggregate:view

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
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for social media aggregates
    api_response = api_instance.get_socialmedia_analytics_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_analytics_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_socialmedia_analytics_aggregates_job_results

> [**SocialMediaAsyncAggregateQueryResponse**](SocialMediaAsyncAggregateQueryResponse) get_socialmedia_analytics_aggregates_job_results(job_id, cursor=cursor)


Fetch a page of results for an async social media query

Wraps GET /api/v2/socialmedia/analytics/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* socialmedia:postAggregate:view

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
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async social media query
    api_response = api_instance.get_socialmedia_analytics_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_analytics_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**SocialMediaAsyncAggregateQueryResponse**](SocialMediaAsyncAggregateQueryResponse)


## get_socialmedia_analytics_messages_job

> [**AsyncQueryStatus**](AsyncQueryStatus) get_socialmedia_analytics_messages_job(job_id)


Get status for async query for social media messages job

Wraps GET /api/v2/socialmedia/analytics/messages/jobs/{jobId} 

Requires ANY permissions: 

* socialmedia:postDetail:view

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
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for social media messages job
    api_response = api_instance.get_socialmedia_analytics_messages_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_analytics_messages_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus)


## get_socialmedia_analytics_messages_job_results

> [**SocialMediaAsyncDetailQueryResponse**](SocialMediaAsyncDetailQueryResponse) get_socialmedia_analytics_messages_job_results(job_id, cursor=cursor)


Fetch a page of results for an async social media messages query

Wraps GET /api/v2/socialmedia/analytics/messages/jobs/{jobId}/results 

Requires ANY permissions: 

* socialmedia:postDetail:view

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
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async social media messages query
    api_response = api_instance.get_socialmedia_analytics_messages_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_analytics_messages_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |

### Return type

[**SocialMediaAsyncDetailQueryResponse**](SocialMediaAsyncDetailQueryResponse)


## get_socialmedia_escalationrule

> [**EscalationRuleResponse**](EscalationRuleResponse) get_socialmedia_escalationrule(escalation_rule_id, expand=expand)


Get a single escalation rule.

Wraps GET /api/v2/socialmedia/escalationrules/{escalationRuleId} 

Requires ALL permissions: 

* socialmedia:escalationRules:view

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
escalation_rule_id = 'escalation_rule_id_example' # str | escalationRuleId
expand = 'expand_example' # str | which fields, if any, to expand (optional)

try:
    # Get a single escalation rule.
    api_response = api_instance.get_socialmedia_escalationrule(escalation_rule_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_escalationrule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **escalation_rule_id** | **str**| escalationRuleId |  |
| **expand** | **str**| which fields, if any, to expand | [optional] <br />**Values**: dataIngestionRule |

### Return type

[**EscalationRuleResponse**](EscalationRuleResponse)


## get_socialmedia_escalationrules

> [**SocialEscalationResponseEntityListing**](SocialEscalationResponseEntityListing) get_socialmedia_escalationrules(division_id, page_number=page_number, page_size=page_size)


Retrieve all escalation rules for a division.

Wraps GET /api/v2/socialmedia/escalationrules 

Requires ANY permissions: 

* socialmedia:escalationRules:view

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
division_id = 'division_id_example' # str | One division ID
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Retrieve all escalation rules for a division.
    api_response = api_instance.get_socialmedia_escalationrules(division_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_escalationrules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | **str**| One division ID |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |

### Return type

[**SocialEscalationResponseEntityListing**](SocialEscalationResponseEntityListing)


## get_socialmedia_topic

> [**SocialTopicWithDataIngestionRuleMetadataResponse**](SocialTopicWithDataIngestionRuleMetadataResponse) get_socialmedia_topic(topic_id, include_deleted=include_deleted)


Get a single social topic.

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

[**SocialTopicWithDataIngestionRuleMetadataResponse**](SocialTopicWithDataIngestionRuleMetadataResponse)


## get_socialmedia_topic_dataingestionrules

> [**DataIngestionRuleResponseEntityListing**](DataIngestionRuleResponseEntityListing) get_socialmedia_topic_dataingestionrules(topic_id, page_number=page_number, page_size=page_size, include_deleted=include_deleted)


Retrieve all social topic data ingestion rules with pagination.

Wraps GET /api/v2/socialmedia/topics/{topicId}/dataingestionrules 

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
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
include_deleted = True # bool | Determines whether to include soft-deleted items in the result. (optional)

try:
    # Retrieve all social topic data ingestion rules with pagination.
    api_response = api_instance.get_socialmedia_topic_dataingestionrules(topic_id, page_number=page_number, page_size=page_size, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topic_dataingestionrules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **include_deleted** | **bool**| Determines whether to include soft-deleted items in the result. | [optional]  |

### Return type

[**DataIngestionRuleResponseEntityListing**](DataIngestionRuleResponseEntityListing)


## get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id

> [**FacebookDataIngestionRuleResponse**](FacebookDataIngestionRuleResponse) get_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id(topic_id, facebook_ingestion_rule_id, include_deleted=include_deleted)


Get a single Facebook data ingestion rule.

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


## get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id

> [**InstagramDataIngestionRuleResponse**](InstagramDataIngestionRuleResponse) get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id(topic_id, instagram_ingestion_rule_id, include_deleted=include_deleted)


Get a single Instagram data ingestion rule.

Wraps GET /api/v2/socialmedia/topics/{topicId}/dataingestionrules/instagram/{instagramIngestionRuleId} 

Requires ALL permissions: 

* socialmedia:instagramDataIngestionRule:view

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
instagram_ingestion_rule_id = 'instagram_ingestion_rule_id_example' # str | instagramIngestionRuleId
include_deleted = True # bool | Determines whether to include soft-deleted items in the result. (optional)

try:
    # Get a single Instagram data ingestion rule.
    api_response = api_instance.get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id(topic_id, instagram_ingestion_rule_id, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **instagram_ingestion_rule_id** | **str**| instagramIngestionRuleId |  |
| **include_deleted** | **bool**| Determines whether to include soft-deleted items in the result. | [optional]  |

### Return type

[**InstagramDataIngestionRuleResponse**](InstagramDataIngestionRuleResponse)


## get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id_version

> [**InstagramDataIngestionRuleVersionResponse**](InstagramDataIngestionRuleVersionResponse) get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id_version(topic_id, instagram_ingestion_rule_id, data_ingestion_rule_version, include_deleted=include_deleted)


Get a single Instagram data ingestion rule version.

Wraps GET /api/v2/socialmedia/topics/{topicId}/dataingestionrules/instagram/{instagramIngestionRuleId}/versions/{dataIngestionRuleVersion} 

Requires ALL permissions: 

* socialmedia:instagramDataIngestionRule:view

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
instagram_ingestion_rule_id = 'instagram_ingestion_rule_id_example' # str | instagramIngestionRuleId
data_ingestion_rule_version = 'data_ingestion_rule_version_example' # str | version
include_deleted = True # bool | Determines whether to include soft-deleted item in the result. (optional)

try:
    # Get a single Instagram data ingestion rule version.
    api_response = api_instance.get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id_version(topic_id, instagram_ingestion_rule_id, data_ingestion_rule_version, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id_version: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **instagram_ingestion_rule_id** | **str**| instagramIngestionRuleId |  |
| **data_ingestion_rule_version** | **str**| version |  |
| **include_deleted** | **bool**| Determines whether to include soft-deleted item in the result. | [optional]  |

### Return type

[**InstagramDataIngestionRuleVersionResponse**](InstagramDataIngestionRuleVersionResponse)


## get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id_versions

> [**InstagramDataIngestionRuleVersionResponseEntityListing**](InstagramDataIngestionRuleVersionResponseEntityListing) get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id_versions(topic_id, instagram_ingestion_rule_id, page_number=page_number, page_size=page_size, include_deleted=include_deleted)


Get the Instagram data ingestion rule versions.

Wraps GET /api/v2/socialmedia/topics/{topicId}/dataingestionrules/instagram/{instagramIngestionRuleId}/versions 

Requires ALL permissions: 

* socialmedia:instagramDataIngestionRule:view

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
instagram_ingestion_rule_id = 'instagram_ingestion_rule_id_example' # str | instagramIngestionRuleId
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
include_deleted = True # bool | Determines whether to include soft-deleted items in the result. (optional)

try:
    # Get the Instagram data ingestion rule versions.
    api_response = api_instance.get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id_versions(topic_id, instagram_ingestion_rule_id, page_number=page_number, page_size=page_size, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id_versions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **instagram_ingestion_rule_id** | **str**| instagramIngestionRuleId |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **include_deleted** | **bool**| Determines whether to include soft-deleted items in the result. | [optional]  |

### Return type

[**InstagramDataIngestionRuleVersionResponseEntityListing**](InstagramDataIngestionRuleVersionResponseEntityListing)


## get_socialmedia_topic_dataingestionrules_open_open_id

> [**OpenDataIngestionRuleResponse**](OpenDataIngestionRuleResponse) get_socialmedia_topic_dataingestionrules_open_open_id(topic_id, open_id, include_deleted=include_deleted)


Get a single open data ingestion rule.

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

> [**SocialTopicResponseEntityListing**](SocialTopicResponseEntityListing) get_socialmedia_topics(page_number=page_number, page_size=page_size, division_ids=division_ids, include_deleted=include_deleted, name=name)


Retrieve all social topics.

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
name = 'name_example' # str | Search for topic by name that contains the given search string, search is case insensitive (optional)

try:
    # Retrieve all social topics.
    api_response = api_instance.get_socialmedia_topics(page_number=page_number, page_size=page_size, division_ids=division_ids, include_deleted=include_deleted, name=name)
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
| **name** | **str**| Search for topic by name that contains the given search string, search is case insensitive | [optional]  |

### Return type

[**SocialTopicResponseEntityListing**](SocialTopicResponseEntityListing)


## patch_socialmedia_topic

> [**SocialTopicResponse**](SocialTopicResponse) patch_socialmedia_topic(topic_id, body=body)


Update a social topic.

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


## patch_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id

> [**InstagramDataIngestionRuleResponse**](InstagramDataIngestionRuleResponse) patch_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id(topic_id, instagram_ingestion_rule_id, body=body)


Update the status of a Instagram data ingestion rule.

Wraps PATCH /api/v2/socialmedia/topics/{topicId}/dataingestionrules/instagram/{instagramIngestionRuleId} 

Requires ALL permissions: 

* socialmedia:instagramDataIngestionRule:edit

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
instagram_ingestion_rule_id = 'instagram_ingestion_rule_id_example' # str | instagramIngestionRuleId
body = PureCloudPlatformClientV2.DataIngestionRuleStatusPatchRequest() # DataIngestionRuleStatusPatchRequest |  (optional)

try:
    # Update the status of a Instagram data ingestion rule.
    api_response = api_instance.patch_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id(topic_id, instagram_ingestion_rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->patch_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **instagram_ingestion_rule_id** | **str**| instagramIngestionRuleId |  |
| **body** | [**DataIngestionRuleStatusPatchRequest**](DataIngestionRuleStatusPatchRequest)|  | [optional]  |

### Return type

[**InstagramDataIngestionRuleResponse**](InstagramDataIngestionRuleResponse)


## patch_socialmedia_topic_dataingestionrules_open_open_id

> [**OpenDataIngestionRuleResponse**](OpenDataIngestionRuleResponse) patch_socialmedia_topic_dataingestionrules_open_open_id(topic_id, open_id, body=body)


Update the status of a open data ingestion rule.

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


## post_socialmedia_analytics_aggregates_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_socialmedia_analytics_aggregates_jobs(body)


Query for social media aggregates asynchronously

Wraps POST /api/v2/socialmedia/analytics/aggregates/jobs 

Requires ANY permissions: 

* socialmedia:postAggregate:view

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
body = PureCloudPlatformClientV2.SocialMediaAsyncAggregationQuery() # SocialMediaAsyncAggregationQuery | query

try:
    # Query for social media aggregates asynchronously
    api_response = api_instance.post_socialmedia_analytics_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->post_socialmedia_analytics_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SocialMediaAsyncAggregationQuery**](SocialMediaAsyncAggregationQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_socialmedia_analytics_messages_jobs

> [**AsyncQueryResponse**](AsyncQueryResponse) post_socialmedia_analytics_messages_jobs(body)


Query for social media messages asynchronously

Wraps POST /api/v2/socialmedia/analytics/messages/jobs 

Requires ANY permissions: 

* socialmedia:postDetail:view

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
body = PureCloudPlatformClientV2.SocialMediaAsyncDetailQuery() # SocialMediaAsyncDetailQuery | query

try:
    # Query for social media messages asynchronously
    api_response = api_instance.post_socialmedia_analytics_messages_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->post_socialmedia_analytics_messages_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SocialMediaAsyncDetailQuery**](SocialMediaAsyncDetailQuery)| query |  |

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse)


## post_socialmedia_escalationrules

> [**EscalationRuleResponse**](EscalationRuleResponse) post_socialmedia_escalationrules(body=body)


Create an escalation rule.

Wraps POST /api/v2/socialmedia/escalationrules 

Requires ANY permissions: 

* socialmedia:escalationRules:add

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
body = PureCloudPlatformClientV2.EscalationRuleRequest() # EscalationRuleRequest |  (optional)

try:
    # Create an escalation rule.
    api_response = api_instance.post_socialmedia_escalationrules(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->post_socialmedia_escalationrules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EscalationRuleRequest**](EscalationRuleRequest)|  | [optional]  |

### Return type

[**EscalationRuleResponse**](EscalationRuleResponse)


## post_socialmedia_escalations_messages

> [**ManualEscalationResponse**](ManualEscalationResponse) post_socialmedia_escalations_messages(division_id, body=body)


Escalate message to a conversation manually

Wraps POST /api/v2/socialmedia/escalations/messages 

Requires ANY permissions: 

* socialmedia:message:escalate

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
division_id = 'division_id_example' # str | One division ID
body = PureCloudPlatformClientV2.ManualEscalationRequest() # ManualEscalationRequest |  (optional)

try:
    # Escalate message to a conversation manually
    api_response = api_instance.post_socialmedia_escalations_messages(division_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->post_socialmedia_escalations_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | **str**| One division ID |  |
| **body** | [**ManualEscalationRequest**](ManualEscalationRequest)|  | [optional]  |

### Return type

[**ManualEscalationResponse**](ManualEscalationResponse)


## post_socialmedia_topic_dataingestionrules_facebook

> [**FacebookDataIngestionRuleResponse**](FacebookDataIngestionRuleResponse) post_socialmedia_topic_dataingestionrules_facebook(topic_id, body=body)


Create an Facebook data ingestion rule.

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


## post_socialmedia_topic_dataingestionrules_instagram

> [**InstagramDataIngestionRuleResponse**](InstagramDataIngestionRuleResponse) post_socialmedia_topic_dataingestionrules_instagram(topic_id, body=body)


Create an Instagram data ingestion rule.

Wraps POST /api/v2/socialmedia/topics/{topicId}/dataingestionrules/instagram 

Requires ANY permissions: 

* socialmedia:instagramDataIngestionRule:add

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
body = PureCloudPlatformClientV2.InstagramDataIngestionRuleRequest() # InstagramDataIngestionRuleRequest |  (optional)

try:
    # Create an Instagram data ingestion rule.
    api_response = api_instance.post_socialmedia_topic_dataingestionrules_instagram(topic_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->post_socialmedia_topic_dataingestionrules_instagram: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **body** | [**InstagramDataIngestionRuleRequest**](InstagramDataIngestionRuleRequest)|  | [optional]  |

### Return type

[**InstagramDataIngestionRuleResponse**](InstagramDataIngestionRuleResponse)


## post_socialmedia_topic_dataingestionrules_open

> [**OpenDataIngestionRuleResponse**](OpenDataIngestionRuleResponse) post_socialmedia_topic_dataingestionrules_open(topic_id, body=body)


Create an open data ingestion rule.

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


## post_socialmedia_topic_dataingestionrules_open_rule_id_messages_bulk

> [**OpenSocialNormalizedMessageEntityListing**](OpenSocialNormalizedMessageEntityListing) post_socialmedia_topic_dataingestionrules_open_rule_id_messages_bulk(topic_id, rule_id, body)


Ingest a list of Open Social Messages

Ingest a list of open social messages to an ingestion rule on a topic. This endpoint will ingest and enrich these messages.  In order to call this endpoint you will need OAuth token generated using OAuth client credentials authorized with at least social scope.

Wraps POST /api/v2/socialmedia/topics/{topicId}/dataingestionrules/open/{ruleId}/messages/bulk 

Requires ALL permissions: 

* socialmedia:message:receive

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
topic_id = 'topic_id_example' # str | Topic ID
rule_id = 'rule_id_example' # str | Data Ingestion Rule ID
body = [PureCloudPlatformClientV2.OpenSocialMediaNormalizedMessage()] # list[OpenSocialMediaNormalizedMessage] | NormalizedMessage

try:
    # Ingest a list of Open Social Messages
    api_response = api_instance.post_socialmedia_topic_dataingestionrules_open_rule_id_messages_bulk(topic_id, rule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->post_socialmedia_topic_dataingestionrules_open_rule_id_messages_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| Topic ID |  |
| **rule_id** | **str**| Data Ingestion Rule ID |  |
| **body** | [**list[OpenSocialMediaNormalizedMessage]**](OpenSocialMediaNormalizedMessage)| NormalizedMessage |  |

### Return type

[**OpenSocialNormalizedMessageEntityListing**](OpenSocialNormalizedMessageEntityListing)


## post_socialmedia_topic_dataingestionrules_open_rule_id_reactions_bulk

> [**OpenSocialReactionsNormalizedEventEntityListing**](OpenSocialReactionsNormalizedEventEntityListing) post_socialmedia_topic_dataingestionrules_open_rule_id_reactions_bulk(topic_id, rule_id, body)


Ingest a list of Open Social Reactions

Ingest a list of open social reactions to an ingestion rule on a topic. This endpoint will ingest these reactions.  In order to call this endpoint you will need OAuth token generated using OAuth client credentials authorized with at least social scope.

Wraps POST /api/v2/socialmedia/topics/{topicId}/dataingestionrules/open/{ruleId}/reactions/bulk 

Requires ALL permissions: 

* socialmedia:reaction:receive

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
topic_id = 'topic_id_example' # str | Topic ID
rule_id = 'rule_id_example' # str | Data Ingestion Rule ID
body = PureCloudPlatformClientV2.OpenSocialMediaReactionsRequest() # OpenSocialMediaReactionsRequest | NormalizedEvent

try:
    # Ingest a list of Open Social Reactions
    api_response = api_instance.post_socialmedia_topic_dataingestionrules_open_rule_id_reactions_bulk(topic_id, rule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->post_socialmedia_topic_dataingestionrules_open_rule_id_reactions_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| Topic ID |  |
| **rule_id** | **str**| Data Ingestion Rule ID |  |
| **body** | [**OpenSocialMediaReactionsRequest**](OpenSocialMediaReactionsRequest)| NormalizedEvent |  |

### Return type

[**OpenSocialReactionsNormalizedEventEntityListing**](OpenSocialReactionsNormalizedEventEntityListing)


## post_socialmedia_topic_dataingestionrules_twitter

> [**TwitterDataIngestionRuleResponse**](TwitterDataIngestionRuleResponse) post_socialmedia_topic_dataingestionrules_twitter(topic_id, body=body)


Create an twitter data ingestion rule.

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


## post_socialmedia_twitter_historical_tweets

> [**TwitterDataHistoricalTweetResponse**](TwitterDataHistoricalTweetResponse) post_socialmedia_twitter_historical_tweets(body)


Retrieves historical tweet count for search terms, optional countries list and the current limit and usage for the organization.

Wraps POST /api/v2/socialmedia/twitter/historical/tweets 

Requires ALL permissions: 

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
body = PureCloudPlatformClientV2.TwitterDataHistoricalTweetRequest() # TwitterDataHistoricalTweetRequest | TwitterDataHistoricalTweetRequest

try:
    # Retrieves historical tweet count for search terms, optional countries list and the current limit and usage for the organization.
    api_response = api_instance.post_socialmedia_twitter_historical_tweets(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->post_socialmedia_twitter_historical_tweets: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TwitterDataHistoricalTweetRequest**](TwitterDataHistoricalTweetRequest)| TwitterDataHistoricalTweetRequest |  |

### Return type

[**TwitterDataHistoricalTweetResponse**](TwitterDataHistoricalTweetResponse)


## put_socialmedia_escalationrule

> [**EscalationRuleResponse**](EscalationRuleResponse) put_socialmedia_escalationrule(escalation_rule_id, body=body)


Update the escalation rule.

Wraps PUT /api/v2/socialmedia/escalationrules/{escalationRuleId} 

Requires ALL permissions: 

* socialmedia:escalationRules:edit

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
escalation_rule_id = 'escalation_rule_id_example' # str | escalationRuleId
body = PureCloudPlatformClientV2.EscalationRuleRequest() # EscalationRuleRequest |  (optional)

try:
    # Update the escalation rule.
    api_response = api_instance.put_socialmedia_escalationrule(escalation_rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->put_socialmedia_escalationrule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **escalation_rule_id** | **str**| escalationRuleId |  |
| **body** | [**EscalationRuleRequest**](EscalationRuleRequest)|  | [optional]  |

### Return type

[**EscalationRuleResponse**](EscalationRuleResponse)


## put_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id

> [**FacebookDataIngestionRuleResponse**](FacebookDataIngestionRuleResponse) put_socialmedia_topic_dataingestionrules_facebook_facebook_ingestion_rule_id(topic_id, facebook_ingestion_rule_id, body=body)


Update the Facebook data ingestion rule.

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


## put_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id

> [**InstagramDataIngestionRuleResponse**](InstagramDataIngestionRuleResponse) put_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id(topic_id, instagram_ingestion_rule_id, body=body)


Update the Instagram data ingestion rule.

Wraps PUT /api/v2/socialmedia/topics/{topicId}/dataingestionrules/instagram/{instagramIngestionRuleId} 

Requires ALL permissions: 

* socialmedia:instagramDataIngestionRule:edit

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
instagram_ingestion_rule_id = 'instagram_ingestion_rule_id_example' # str | instagramIngestionRuleId
body = PureCloudPlatformClientV2.InstagramDataIngestionRuleRequest() # InstagramDataIngestionRuleRequest |  (optional)

try:
    # Update the Instagram data ingestion rule.
    api_response = api_instance.put_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id(topic_id, instagram_ingestion_rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->put_socialmedia_topic_dataingestionrules_instagram_instagram_ingestion_rule_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **topic_id** | **str**| topicId |  |
| **instagram_ingestion_rule_id** | **str**| instagramIngestionRuleId |  |
| **body** | [**InstagramDataIngestionRuleRequest**](InstagramDataIngestionRuleRequest)|  | [optional]  |

### Return type

[**InstagramDataIngestionRuleResponse**](InstagramDataIngestionRuleResponse)


## put_socialmedia_topic_dataingestionrules_open_open_id

> [**OpenDataIngestionRuleResponse**](OpenDataIngestionRuleResponse) put_socialmedia_topic_dataingestionrules_open_open_id(topic_id, open_id, body=body)


Update the open data ingestion rule.

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


_PureCloudPlatformClientV2 246.1.0_

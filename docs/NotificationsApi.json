---
title: NotificationsApi
---

## PureCloudPlatformClientV2.NotificationsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_notifications_channel_subscriptions**](NotificationsApi.html#delete_notifications_channel_subscriptions) | Remove all subscriptions|
|[**get_notifications_availabletopics**](NotificationsApi.html#get_notifications_availabletopics) | Get available notification topics.|
|[**get_notifications_channel_subscriptions**](NotificationsApi.html#get_notifications_channel_subscriptions) | The list of all subscriptions for this channel|
|[**get_notifications_channels**](NotificationsApi.html#get_notifications_channels) | The list of existing channels|
|[**head_notifications_channel**](NotificationsApi.html#head_notifications_channel) | Verify a channel still exists and is valid|
|[**post_notifications_channel_subscriptions**](NotificationsApi.html#post_notifications_channel_subscriptions) | Add a list of subscriptions to the existing list of subscriptions|
|[**post_notifications_channels**](NotificationsApi.html#post_notifications_channels) | Create a new channel|
|[**put_notifications_channel_subscriptions**](NotificationsApi.html#put_notifications_channel_subscriptions) | Replace the current list of subscriptions with a new list.|
{: class="table table-striped"}

<a name="delete_notifications_channel_subscriptions"></a>

##  delete_notifications_channel_subscriptions(channel_id)



Remove all subscriptions

Wraps DELETE /api/v2/notifications/channels/{channelId}/subscriptions 

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
api_instance = PureCloudPlatformClientV2.NotificationsApi()
channel_id = 'channel_id_example' # str | Channel ID

try:
    # Remove all subscriptions
    api_instance.delete_notifications_channel_subscriptions(channel_id)
except ApiException as e:
    print("Exception when calling NotificationsApi->delete_notifications_channel_subscriptions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **channel_id** | **str**| Channel ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_notifications_availabletopics"></a>

## [**AvailableTopicEntityListing**](AvailableTopicEntityListing.html) get_notifications_availabletopics(expand=expand, include_preview=include_preview)



Get available notification topics.

Wraps GET /api/v2/notifications/availabletopics 

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
api_instance = PureCloudPlatformClientV2.NotificationsApi()
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
include_preview = True # bool | Whether or not to include Preview topics (optional) (default to True)

try:
    # Get available notification topics.
    api_response = api_instance.get_notifications_availabletopics(expand=expand, include_preview=include_preview)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_notifications_availabletopics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: description, enforced, schema, visibility, transports, publicApiTemplateUriPaths, requiresPermissions, permissionDetails, topicParameters |
| **include_preview** | **bool**| Whether or not to include Preview topics | [optional] [default to True] |
{: class="table table-striped"}

### Return type

[**AvailableTopicEntityListing**](AvailableTopicEntityListing.html)

<a name="get_notifications_channel_subscriptions"></a>

## [**ChannelTopicEntityListing**](ChannelTopicEntityListing.html) get_notifications_channel_subscriptions(channel_id)



The list of all subscriptions for this channel

Wraps GET /api/v2/notifications/channels/{channelId}/subscriptions 

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
api_instance = PureCloudPlatformClientV2.NotificationsApi()
channel_id = 'channel_id_example' # str | Channel ID

try:
    # The list of all subscriptions for this channel
    api_response = api_instance.get_notifications_channel_subscriptions(channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_notifications_channel_subscriptions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **channel_id** | **str**| Channel ID |  |
{: class="table table-striped"}

### Return type

[**ChannelTopicEntityListing**](ChannelTopicEntityListing.html)

<a name="get_notifications_channels"></a>

## [**ChannelEntityListing**](ChannelEntityListing.html) get_notifications_channels(includechannels=includechannels)



The list of existing channels

Wraps GET /api/v2/notifications/channels 

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
api_instance = PureCloudPlatformClientV2.NotificationsApi()
includechannels = ''token'' # str | Show user's channels for this specific token or across all tokens for this user and app.  Channel Ids for other access tokens will not be shown, but will be presented to show their existence. (optional) (default to 'token')

try:
    # The list of existing channels
    api_response = api_instance.get_notifications_channels(includechannels=includechannels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_notifications_channels: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **includechannels** | **str**| Show user&#39;s channels for this specific token or across all tokens for this user and app.  Channel Ids for other access tokens will not be shown, but will be presented to show their existence. | [optional] [default to &#39;token&#39;]<br />**Values**: token, oauthclient |
{: class="table table-striped"}

### Return type

[**ChannelEntityListing**](ChannelEntityListing.html)

<a name="head_notifications_channel"></a>

##  head_notifications_channel(channel_id)



Verify a channel still exists and is valid

Returns a 200 OK if channel exists, and a 404 Not Found if it doesn't

Wraps HEAD /api/v2/notifications/channels/{channelId} 

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
api_instance = PureCloudPlatformClientV2.NotificationsApi()
channel_id = 'channel_id_example' # str | Channel ID

try:
    # Verify a channel still exists and is valid
    api_instance.head_notifications_channel(channel_id)
except ApiException as e:
    print("Exception when calling NotificationsApi->head_notifications_channel: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **channel_id** | **str**| Channel ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_notifications_channel_subscriptions"></a>

## [**ChannelTopicEntityListing**](ChannelTopicEntityListing.html) post_notifications_channel_subscriptions(channel_id, body, ignore_errors=ignore_errors)



Add a list of subscriptions to the existing list of subscriptions

Wraps POST /api/v2/notifications/channels/{channelId}/subscriptions 

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
api_instance = PureCloudPlatformClientV2.NotificationsApi()
channel_id = 'channel_id_example' # str | Channel ID
body = [PureCloudPlatformClientV2.ChannelTopic()] # list[ChannelTopic] | Body
ignore_errors = False # bool | Optionally prevent throwing of errors for failed permissions checks. (optional) (default to False)

try:
    # Add a list of subscriptions to the existing list of subscriptions
    api_response = api_instance.post_notifications_channel_subscriptions(channel_id, body, ignore_errors=ignore_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->post_notifications_channel_subscriptions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **channel_id** | **str**| Channel ID |  |
| **body** | [**list[ChannelTopic]**](ChannelTopic.html)| Body |  |
| **ignore_errors** | **bool**| Optionally prevent throwing of errors for failed permissions checks. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**ChannelTopicEntityListing**](ChannelTopicEntityListing.html)

<a name="post_notifications_channels"></a>

## [**Channel**](Channel.html) post_notifications_channels()



Create a new channel

There is a limit of 20 channels per user/app combination. Creating a 21st channel will remove the channel with oldest last used date. Channels without an active connection will be removed first.

Wraps POST /api/v2/notifications/channels 

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
api_instance = PureCloudPlatformClientV2.NotificationsApi()

try:
    # Create a new channel
    api_response = api_instance.post_notifications_channels()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->post_notifications_channels: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**Channel**](Channel.html)

<a name="put_notifications_channel_subscriptions"></a>

## [**ChannelTopicEntityListing**](ChannelTopicEntityListing.html) put_notifications_channel_subscriptions(channel_id, body, ignore_errors=ignore_errors)



Replace the current list of subscriptions with a new list.

Wraps PUT /api/v2/notifications/channels/{channelId}/subscriptions 

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
api_instance = PureCloudPlatformClientV2.NotificationsApi()
channel_id = 'channel_id_example' # str | Channel ID
body = [PureCloudPlatformClientV2.ChannelTopic()] # list[ChannelTopic] | Body
ignore_errors = False # bool | Optionally prevent throwing of errors for failed permissions checks. (optional) (default to False)

try:
    # Replace the current list of subscriptions with a new list.
    api_response = api_instance.put_notifications_channel_subscriptions(channel_id, body, ignore_errors=ignore_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->put_notifications_channel_subscriptions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **channel_id** | **str**| Channel ID |  |
| **body** | [**list[ChannelTopic]**](ChannelTopic.html)| Body |  |
| **ignore_errors** | **bool**| Optionally prevent throwing of errors for failed permissions checks. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**ChannelTopicEntityListing**](ChannelTopicEntityListing.html)


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
|[**post_notifications_channel_subscriptions**](NotificationsApi.html#post_notifications_channel_subscriptions) | Add a list of subscriptions to the existing list of subscriptions|
|[**post_notifications_channels**](NotificationsApi.html#post_notifications_channels) | Create a new channel|
|[**put_notifications_channel_subscriptions**](NotificationsApi.html#put_notifications_channel_subscriptions) | Replace the current list of subscriptions with a new list.|
{: class="table table-striped"}

<a name="delete_notifications_channel_subscriptions"></a>

##  delete_notifications_channel_subscriptions(channel_id)



Remove all subscriptions



Wraps DELETE /api/v2/notifications/channels/{channelId}/subscriptions 

Requires NO permissions: 


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

## [**AvailableTopicEntityListing**](AvailableTopicEntityListing.html) get_notifications_availabletopics(expand=expand)



Get available notification topics.



Wraps GET /api/v2/notifications/availabletopics 

Requires NO permissions: 


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

try:
    # Get available notification topics.
    api_response = api_instance.get_notifications_availabletopics(expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_notifications_availabletopics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: description, requiresPermissions, schema, transports, publicApiTemplateUriPaths |
{: class="table table-striped"}

### Return type

[**AvailableTopicEntityListing**](AvailableTopicEntityListing.html)

<a name="get_notifications_channel_subscriptions"></a>

## [**ChannelTopicEntityListing**](ChannelTopicEntityListing.html) get_notifications_channel_subscriptions(channel_id)



The list of all subscriptions for this channel



Wraps GET /api/v2/notifications/channels/{channelId}/subscriptions 

Requires NO permissions: 


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

Requires NO permissions: 


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
includechannels = 'token' # str | Show user's channels for this specific token or across all tokens for this user and app.  Channel Ids for other access tokens will not be shown, but will be presented to show their existence. (optional) (default to token)

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
| **includechannels** | **str**| Show user&#39;s channels for this specific token or across all tokens for this user and app.  Channel Ids for other access tokens will not be shown, but will be presented to show their existence. | [optional] [default to token]<br />**Values**: token, oauthclient |
{: class="table table-striped"}

### Return type

[**ChannelEntityListing**](ChannelEntityListing.html)

<a name="post_notifications_channel_subscriptions"></a>

## [**ChannelTopicEntityListing**](ChannelTopicEntityListing.html) post_notifications_channel_subscriptions(channel_id, body)



Add a list of subscriptions to the existing list of subscriptions



Wraps POST /api/v2/notifications/channels/{channelId}/subscriptions 

Requires NO permissions: 


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

try:
    # Add a list of subscriptions to the existing list of subscriptions
    api_response = api_instance.post_notifications_channel_subscriptions(channel_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->post_notifications_channel_subscriptions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **channel_id** | **str**| Channel ID |  |
| **body** | [**list[ChannelTopic]**](ChannelTopic.html)| Body |  |
{: class="table table-striped"}

### Return type

[**ChannelTopicEntityListing**](ChannelTopicEntityListing.html)

<a name="post_notifications_channels"></a>

## [**Channel**](Channel.html) post_notifications_channels()



Create a new channel

There is a limit of 20 channels per user/app combination. Creating a 21st channel will remove the channel with oldest last used date. Channels without an active connection will be removed first.

Wraps POST /api/v2/notifications/channels 

Requires NO permissions: 


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

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**Channel**](Channel.html)

<a name="put_notifications_channel_subscriptions"></a>

## [**ChannelTopicEntityListing**](ChannelTopicEntityListing.html) put_notifications_channel_subscriptions(channel_id, body)



Replace the current list of subscriptions with a new list.



Wraps PUT /api/v2/notifications/channels/{channelId}/subscriptions 

Requires NO permissions: 


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

try:
    # Replace the current list of subscriptions with a new list.
    api_response = api_instance.put_notifications_channel_subscriptions(channel_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->put_notifications_channel_subscriptions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **channel_id** | **str**| Channel ID |  |
| **body** | [**list[ChannelTopic]**](ChannelTopic.html)| Body |  |
{: class="table table-striped"}

### Return type

[**ChannelTopicEntityListing**](ChannelTopicEntityListing.html)


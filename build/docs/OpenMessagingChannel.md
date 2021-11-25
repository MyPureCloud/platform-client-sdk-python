---
title: OpenMessagingChannel
---
## OpenMessagingChannel

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The Messaging Platform integration ID. | [optional] |
| **platform** | **str** | The provider type. | [optional] |
| **type** | **str** | Specifies if this message is part of a private or public conversation. | [optional] |
| **message_id** | **str** | Unique provider ID of the message such as a Facebook message ID. | |
| **to** | [**OpenMessagingToRecipient**](OpenMessagingToRecipient.html) | Information about the recipient the message is sent to. | |
| **pcFrom** | [**OpenMessagingFromRecipient**](OpenMessagingFromRecipient.html) | Information about the recipient the message is received from. | |
| **time** | **datetime** | Original time of the event. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **metadata** | [**ChannelMetadata**](ChannelMetadata.html) | Information about the channel. | [optional] |
{: class="table table-striped"}



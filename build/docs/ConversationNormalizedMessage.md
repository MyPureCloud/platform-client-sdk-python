---
title: ConversationNormalizedMessage
---
## ConversationNormalizedMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Unique ID of the message. Message receipts will have the same ID as the message they reference. | [optional] |
| **channel** | [**ConversationMessagingChannel**](ConversationMessagingChannel.html) | Channel-specific information that describes the message and the message channel/provider. | [optional] |
| **type** | **str** | Message type. | |
| **text** | **str** | Message text. | [optional] |
| **content** | [**list[ConversationMessageContent]**](ConversationMessageContent.html) | List of content elements. | [optional] |
| **events** | [**list[ConversationMessageEvent]**](ConversationMessageEvent.html) | List of event elements. | [optional] |
| **status** | **str** | Message receipt status, only used with type Receipt. | [optional] |
| **reasons** | [**list[ConversationReason]**](ConversationReason.html) | List of reasons for a message receipt that indicates the message has failed. Only used with Failed status. | [optional] |
| **originating_entity** | **str** | Specifies if this message was sent by a human agent or bot. The platform may use this to apply appropriate provider policies. | [optional] |
| **is_final_receipt** | **bool** | Indicates if this is the last message receipt for this message, or if another message receipt can be expected. | [optional] |
| **direction** | **str** | The direction of the message. | [optional] |
| **metadata** | **dict(str, str)** | Additional metadata about this message. | [optional] |
{: class="table table-striped"}



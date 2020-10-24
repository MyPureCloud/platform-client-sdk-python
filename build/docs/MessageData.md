---
title: MessageData
---
## MessageData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **provider_message_id** | **str** | The unique identifier of the message from provider | [optional] |
| **timestamp** | **datetime** | The time when the message was received or sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **from_address** | **str** | The sender of the text message. | [optional] |
| **to_address** | **str** | The recipient of the text message. | [optional] |
| **direction** | **str** | The direction of the message. | [optional] |
| **messenger_type** | **str** | Type of text messenger. | [optional] |
| **text_body** | **str** | The body of the text message. | |
| **status** | **str** | The status of the message. | |
| **media** | [**list[MessageMedia]**](MessageMedia.html) | The media details associated to a message. | [optional] |
| **stickers** | [**list[MessageSticker]**](MessageSticker.html) | The sticker details associated to a message. | [optional] |
| **created_by** | [**User**](User.html) | User who sent this message. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



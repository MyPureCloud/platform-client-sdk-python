---
title: RecordingMessagingMessage
---
## RecordingMessagingMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **pcFrom** | **str** | The message sender session id. | [optional] |
| **from_user** | [**User**](User.html) | The user who sent this message. | [optional] |
| **from_external_contact** | [**ExternalContact**](ExternalContact.html) | The PureCloud external contact sender details. | [optional] |
| **to** | **str** | The message recipient. | [optional] |
| **timestamp** | **datetime** | The time when the message was sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **id** | **str** | A globally unique identifier for this communication. | [optional] |
| **message_text** | **str** | The content of this message. | [optional] |
| **message_media_attachments** | [**list[MessageMediaAttachment]**](MessageMediaAttachment.html) | List of media objects attached  with this message. | [optional] |
| **message_sticker_attachments** | [**list[MessageStickerAttachment]**](MessageStickerAttachment.html) | List of message stickers attached with this message. | [optional] |
| **quick_replies** | [**list[QuickReply]**](QuickReply.html) | List of quick reply options offered with this message. | [optional] |
| **button_response** | [**ButtonResponse**](ButtonResponse.html) | Button Response selected by user for this message. | [optional] |
| **story** | [**RecordingContentStory**](RecordingContentStory.html) | Ephemeral story content. | [optional] |
{: class="table table-striped"}



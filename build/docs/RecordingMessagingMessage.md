# RecordingMessagingMessage

## RecordingMessagingMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **pcFrom** | str | The message sender session id. | [optional] |
| **from_user** | [User](User) | The user who sent this message. | [optional] |
| **from_external_contact** | [ExternalContact](ExternalContact) | The PureCloud external contact sender details. | [optional] |
| **to** | str | The message recipient. | [optional] |
| **timestamp** | datetime | The time when the message was sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **purpose** | str | A well known string that specifies the purpose or type of the participant on this communication. | [optional] |
| **participant_id** | str | A globally unique identifier for the participant on this communication. | [optional] |
| **queue** | [AddressableEntityRef](AddressableEntityRef) | A globally unique identifier for the queue involved in this communication. | [optional] |
| **workflow** | [AddressableEntityRef](AddressableEntityRef) | A globally unique identifier for the workflow involved in this communication. | [optional] |
| **message_text** | str | The content of this message. | [optional] |
| **message_media_attachments** | [list[MessageMediaAttachment]](MessageMediaAttachment) | List of media objects attached  with this message. | [optional] |
| **message_sticker_attachments** | [list[MessageStickerAttachment]](MessageStickerAttachment) | List of message stickers attached with this message. | [optional] |
| **quick_replies** | [list[QuickReply]](QuickReply) | List of quick reply options offered with this message. | [optional] |
| **button_response** | [ButtonResponse](ButtonResponse) | Button Response selected by user for this message. | [optional] |
| **story** | [RecordingContentStory](RecordingContentStory) | Ephemeral story content. | [optional] |
| **cards** | [list[Card]](Card) | List of cards offered for this message | [optional] |
| **notification_template** | [RecordingNotificationTemplate](RecordingNotificationTemplate) | Template notification content. | [optional] |
| **content_type** | str | Indicates the content type for this message | [optional] |
| **events** | [list[ConversationMessageEvent]](ConversationMessageEvent) | List of event elements | [optional] |



_PureCloudPlatformClientV2 224.1.0_

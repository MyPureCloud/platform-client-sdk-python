# ConversationEventTopicMessageDetails

## ConversationEventTopicMessageDetails

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **message_id** | str | UUID identifying the message media. | [optional] |
| **message_time** | datetime | The time when the message was sent or received. | [optional] |
| **message_status** | str | Indicates the delivery status of the message. | [optional] |
| **message_segment_count** | int | The message segment count, greater than 1 if the message content was split into multiple parts for this message type, e.g. SMS character limits. | [optional] |
| **media** | [list[ConversationEventTopicMessageMedia]](ConversationEventTopicMessageMedia) | The media (images, files, etc) associated with this message, if any | [optional] |
| **error_info** | [ConversationEventTopicErrorDetails](ConversationEventTopicErrorDetails) | Detailed information about an error response. | [optional] |
| **stickers** | [list[ConversationEventTopicMessageSticker]](ConversationEventTopicMessageSticker) | A list of stickers included in the message | [optional] |
| **message_metadata** | [ConversationEventTopicMessageMetadata](ConversationEventTopicMessageMetadata) |  | [optional] |
| **social_visibility** | str | For social media messages, the visibility of the message in the originating social platform | [optional] |



_PureCloudPlatformClientV2 235.1.0_

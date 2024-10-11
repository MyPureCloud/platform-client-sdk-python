# QueueConversationSocialExpressionEventTopicMessageDetails

## QueueConversationSocialExpressionEventTopicMessageDetails

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **message_id** | str | UUID identifying the message media. | [optional] |
| **message_time** | datetime | The time when the message was sent or received. | [optional] |
| **message_status** | str | Indicates the delivery status of the message. | [optional] |
| **message_segment_count** | int | The message segment count, greater than 1 if the message content was split into multiple parts for this message type, e.g. SMS character limits. | [optional] |
| **media** | [list[QueueConversationSocialExpressionEventTopicMessageMedia]](QueueConversationSocialExpressionEventTopicMessageMedia) | The media (images, files, etc) associated with this message, if any | [optional] |
| **error_info** | [QueueConversationSocialExpressionEventTopicErrorDetails](QueueConversationSocialExpressionEventTopicErrorDetails) | Detailed information about an error response. | [optional] |
| **stickers** | [list[QueueConversationSocialExpressionEventTopicMessageSticker]](QueueConversationSocialExpressionEventTopicMessageSticker) | A list of stickers included in the message | [optional] |
| **message_metadata** | [QueueConversationSocialExpressionEventTopicMessageMetadata](QueueConversationSocialExpressionEventTopicMessageMetadata) |  | [optional] |
| **social_visibility** | str | For social media messages, the visibility of the message in the originating social platform | [optional] |



_PureCloudPlatformClientV2 213.0.0_

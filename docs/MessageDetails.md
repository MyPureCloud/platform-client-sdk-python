# MessageDetails

## MessageDetails

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **message_id** | str | UUID identifying the message media. | [optional] |
| **message_uri** | str | A URI for this message entity. | [optional] |
| **message_status** | str | Indicates the delivery status of the message. | [optional] |
| **message_segment_count** | int | The message segment count, greater than 1 if the message content was split into multiple parts for this message type, e.g. SMS character limits. | [optional] |
| **message_time** | datetime | The time when the message was sent or received. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **media** | [list[MessageMedia]](MessageMedia) | The media (images, files, etc) associated with this message, if any | [optional] |
| **stickers** | [list[MessageSticker]](MessageSticker) | One or more stickers associated with this message, if any | [optional] |
| **message_metadata** | [ConversationMessageMetadata](ConversationMessageMetadata) | Information that describes the content of the message, if any | [optional] |
| **social_visibility** | str | For social media messages, the visibility of the message in the originating social platform | [optional] |
| **error_info** | [ErrorBody](ErrorBody) | Provider specific error information for a communication. | [optional] |



_PureCloudPlatformClientV2 225.0.0_

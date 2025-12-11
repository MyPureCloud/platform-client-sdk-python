# ConversationMessagingChannel

## ConversationMessagingChannel

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The integration ID. | [optional] |
| **platform** | str | The provider type. | [optional] |
| **type** | str | Specifies if this message is part of a private or public conversation. | [optional] |
| **message_id** | str | Unique provider ID of the message such as a Facebook message ID. | [optional] |
| **to** | [ConversationMessagingToRecipient](ConversationMessagingToRecipient) | Information about the recipient the message is sent to. | [optional] |
| **pcFrom** | [ConversationMessagingFromRecipient](ConversationMessagingFromRecipient) | Information about the recipient the message is received from. | [optional] |
| **time** | datetime | Original time of the event. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Time the message was edited. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_deleted** | datetime | Time the message was deleted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **public_metadata** | [ConversationPublicMetadata](ConversationPublicMetadata) | Information about a public message. | [optional] |



_PureCloudPlatformClientV2 246.0.0_

# InternalMessageData

## InternalMessageData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **conversation** | [AddressableEntityRef](AddressableEntityRef) | The conversation of this message. | [optional] |
| **communication_id** | str | The id of the communication of this message. | [optional] |
| **timestamp** | datetime | The time when the message was received or sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **sender** | [UserReference](UserReference) | The sender of the text message. | [optional] |
| **recipient** | [UserReference](UserReference) | The recipient of the text message. | [optional] |
| **normalized_message** | [ConversationNormalizedMessage](ConversationNormalizedMessage) | The message into normalized format | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 247.0.0_

# AgentlessEmailSendResponseDto

## AgentlessEmailSendResponseDto

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **conversation_id** | str | The identifier of the conversation. | |
| **sender_type** | str | The identifier of the external participant of the given conversation. | |
| **from_address** | [EmailAddress](EmailAddress) | The sender of the message. | |
| **to_addresses** | [list[EmailAddress]](EmailAddress) | The recipient of the message. We currently support one recipient only. | |
| **reply_to_address** | [EmailAddress](EmailAddress) | The address to use for reply. | [optional] |
| **subject** | str | The subject of the message. | [optional] |
| **date_created** | datetime | The message creation timestamp. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 245.0.0_

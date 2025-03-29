# AgentlessEmailSendRequestDto

## AgentlessEmailSendRequestDto

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **sender_type** | str | The direction of the message. | |
| **conversation_id** | str | The identifier of the conversation. This must be an email interaction. | [optional] |
| **from_address** | [EmailAddress](EmailAddress) | The sender of the message. | |
| **to_addresses** | [list[EmailAddress]](EmailAddress) | The recipient of the message. We currently support one recipient only. | |
| **reply_to_address** | [EmailAddress](EmailAddress) | The address to use for reply. | [optional] |
| **subject** | str | The subject of the message. | [optional] |
| **text_body** | str | The Content of the message, in plain text. | [optional] |
| **html_body** | str | The Content of the message, in HTML. Links, images and styles are allowed | [optional] |



_PureCloudPlatformClientV2 224.1.0_

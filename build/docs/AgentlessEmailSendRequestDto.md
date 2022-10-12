---
title: AgentlessEmailSendRequestDto
---
## AgentlessEmailSendRequestDto

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **sender_type** | **str** | The direction of the message. | |
| **conversation_id** | **str** | The identifier of the conversation. | [optional] |
| **from_address** | [**EmailAddress**](EmailAddress.html) | The sender of the message. | |
| **to_addresses** | [**list[EmailAddress]**](EmailAddress.html) | The recipient(s) of the message. | |
| **reply_to_address** | [**EmailAddress**](EmailAddress.html) | The address to use for reply. | [optional] |
| **subject** | **str** | The subject of the message. | [optional] |
| **text_body** | **str** | The Content of the message, in plain text. | [optional] |
| **html_body** | **str** | The Content of the message, in HTML. Links, images and styles are allowed | [optional] |
{: class="table table-striped"}



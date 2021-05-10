---
title: SendAgentlessOutboundMessageRequest
---
## SendAgentlessOutboundMessageRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **from_address** | **str** | The messaging address of the sender of the message. For an SMS messenger type, this must be a currently provisioned SMS phone number. For a WhatsApp messenger type use the provisioned WhatsApp integration’s ID | |
| **to_address** | **str** | The messaging address of the recipient of the message. For an SMS messenger type, the phone number address must be in E.164 format. E.g. +13175555555 or +34234234234. | |
| **to_address_messenger_type** | **str** | The recipient messaging address messenger type. Currently SMS is the only one supported. WhatsApp will be supported in a future release. | |
| **text_body** | **str** | The text of the message to send. This field is required in the case of SMS messenger type | [optional] |
| **messaging_template** | [**MessagingTemplateRequest**](MessagingTemplateRequest.html) | The messaging template to use in the case of WhatsApp messenger type. This field is required when using WhatsApp messenger type | [optional] |
{: class="table table-striped"}



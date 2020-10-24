---
title: SendAgentlessOutboundMessageResponse
---
## SendAgentlessOutboundMessageResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **conversation_id** | **str** | The identifier of the conversation. | [optional] |
| **from_address** | **str** | The sender of the text message. | [optional] |
| **to_address** | **str** | The recipient of the text message. | [optional] |
| **messenger_type** | **str** | Type of text messenger. | [optional] |
| **text_body** | **str** | The body of the text message. | [optional] |
| **timestamp** | **datetime** | The time when the message was sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
| **user** | [**AddressableEntityRef**](AddressableEntityRef.html) | Details of the user created the job | [optional] |
{: class="table table-striped"}



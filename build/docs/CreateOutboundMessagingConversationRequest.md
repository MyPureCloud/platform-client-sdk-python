---
title: CreateOutboundMessagingConversationRequest
---
## CreateOutboundMessagingConversationRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue_id** | **str** | The ID of the queue to be associated with the message. This will determine the fromAddress of the message. | |
| **to_address** | **str** | The messaging address of the recipient of the message. For an SMS messenger type, the phone number address must be in E.164 format. E.g. +13175555555 or +34234234234 | |
| **to_address_messenger_type** | **str** | The messaging address messenger type. | |
| **use_existing_conversation** | **bool** | An override to use an existing conversation.  If set to true, an existing conversation will be used if there is one within the conversation window.  If set to false, create request fails if there is a conversation within the conversation window. | [optional] |
| **external_contact_id** | **str** | The external contact with which the message will be associated. | [optional] |
{: class="table table-striped"}



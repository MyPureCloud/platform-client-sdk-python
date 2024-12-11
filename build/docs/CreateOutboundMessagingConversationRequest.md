# CreateOutboundMessagingConversationRequest

## CreateOutboundMessagingConversationRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue_id** | str | The ID of the queue to be associated with the message. This will determine the fromAddress of the message, unless useUserFromAddress is true and the queue is configured to use the agent&#39;s Direct Routing address as the fromAddress. | |
| **to_address** | str | The messaging address of the recipient of the message. For an SMS messenger type, the phone number address must be in E.164 format. E.g. +13175555555 or +34234234234.  For open messenger type, any string within the outbound.open.messaging.to.address.characters.max limit can be used. For whatsapp messenger type, use a Whatsapp ID of a phone number. E.g for a E.164 formatted phone number &#x60;+13175555555&#x60;, a Whatsapp ID would be 13175555555 | |
| **to_address_messenger_type** | str | The messaging address messenger type. | |
| **use_existing_conversation** | bool | An override to use an existing conversation.  If set to true, an existing conversation will be used if there is one within the conversation window.  If set to false, create request fails if there is a conversation within the conversation window. | [optional] |
| **external_contact_id** | str | The external contact with which the message will be associated. | [optional] |
| **use_user_from_address** | bool | An override to attempt to use the user&#39;s configured direct routing address as the fromAddress.  If set to true, users configured address with &#39;directrouting&#39; integration will be used as fromAddress.  If set to false or not set, the queueId will be used for determining fromAddress. | [optional] |



_PureCloudPlatformClientV2 218.0.0_

# SendAgentlessOutboundMessageResponse

## SendAgentlessOutboundMessageResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **conversation_id** | str | The identifier of the conversation. | [optional] |
| **from_address** | str | The sender of the message. | [optional] |
| **to_address** | str | The recipient of the message. | [optional] |
| **messenger_type** | str | Type of messenger. | [optional] |
| **text_body** | str | The body of the text message. (Deprecated - Instead use message.normalizedMessage.text) | [optional] |
| **messaging_template** | [SendMessagingTemplateRequest](SendMessagingTemplateRequest) | The messaging template sent. (Deprecated - Instead use message.normalizedMessage.content[#].template) | [optional] |
| **use_existing_active_conversation** | bool | Use an existing active conversation to send the agentless outbound message. Set this parameter to &#39;true&#39; to use active conversation. Default value: false | [optional] |
| **message** | [MessageData](MessageData) | Sent agentless outbound message in normalized format | [optional] |
| **timestamp** | datetime | The time when the message was sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **user** | [AddressableEntityRef](AddressableEntityRef) | Details of the user created the job | [optional] |



_PureCloudPlatformClientV2 233.0.0_

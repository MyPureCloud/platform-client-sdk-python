# GuideSessionTurnRequestContext

## GuideSessionTurnRequestContext

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **custom_conversation_attributes** | [list[CustomConversationAttributeInput]](CustomConversationAttributeInput) | The Conversation Custom Attributes schemas and records available for this turn. | [optional] |
| **messages** | [list[GuideSessionMessage]](GuideSessionMessage) | The conversation history that occurred before this guide session. | [optional] |
| **knowledge_query_detected** | bool | Whether a knowledge query was detected in the previous conversation turns. | [optional] |



_PureCloudPlatformClientV2 269.0.0_

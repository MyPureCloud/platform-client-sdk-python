# KnowledgeSourcesSearchRequest

## KnowledgeSourcesSearchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **query** | str | Input query to search content on the knowledge setting. | |
| **knowledge_setting_id** | str | Knowledge Setting Id to use for search request. | |
| **application** | [V3KnowledgeSearchClientApplication](V3KnowledgeSearchClientApplication) | The client application details from which search requested. | [optional] |
| **conversation_context** | [KnowledgeV3ConversationContext](KnowledgeV3ConversationContext) | Conversation context information if the search is initiated in the context of a conversation. | [optional] |
| **session_id** | str | The session id for search request. | [optional] |
| **query_type** | str | The type of the query that initiates the search. | [optional] |
| **generation_language** | str | The language to use for answer generation. | [optional] |
| **conversation_turns** | [list[KnowledgeConversationTurn]](KnowledgeConversationTurn) | List of conversation turns to use for stateful search. | [optional] |



_PureCloudPlatformClientV2 256.0.0_

# KnowledgeSourcesSearchResponse

## KnowledgeSourcesSearchResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **query** | str | Query to search content in the knowledge base. | [optional] |
| **search_id** | str | The globally unique identifier for the search. | [optional] |
| **session_id** | str | The sessionId for search request. | [optional] |
| **result** | [KnowledgeSearchResult](KnowledgeSearchResult) | Content matching the search query. | [optional] |
| **knowledge_setting_id** | str | Knowledge Setting Id used for the search request. | [optional] |
| **conversation_context** | [KnowledgeV3ConversationContextResponse](KnowledgeV3ConversationContextResponse) | Conversation context information if the search is initiated in the context of a conversation. | [optional] |
| **application** | [V3KnowledgeSearchClientApplication](V3KnowledgeSearchClientApplication) | The client application details from which search happened. | [optional] |
| **query_type** | str | The type of the query that initiates the search. | [optional] |
| **generation_language** | str | The language used for answer generation. | [optional] |
| **answer_generation** | bool | Indicates if answer generation was enabled for the setting. | [optional] |



_PureCloudPlatformClientV2 256.0.0_

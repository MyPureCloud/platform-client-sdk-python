# KnowledgeSearchPreviewResponse

## KnowledgeSearchPreviewResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **query** | str | Query to search content in the knowledge base. | [optional] |
| **search_id** | str | The globally unique identifier for the search. | [optional] |
| **session_id** | str | The sessionId for search request. | [optional] |
| **result** | [KnowledgeSearchResult](KnowledgeSearchResult) | Content matching the search query. | [optional] |
| **application** | [V3KnowledgeSearchPreviewClientApplication](V3KnowledgeSearchPreviewClientApplication) | The touchpoint application used for the preview. | [optional] |
| **conversation_context** | [KnowledgeV3PreviewConversationContext](KnowledgeV3PreviewConversationContext) | The channel context used for the preview. | [optional] |



_PureCloudPlatformClientV2 263.0.0_

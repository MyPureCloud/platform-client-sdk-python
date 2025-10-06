# KnowledgeDocumentView

## KnowledgeDocumentView

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **document_variation_id** | str | The variation of the viewed document. | |
| **document_version_id** | str | The version of the viewed document. | |
| **search_id** | str | The search that surfaced the viewed document. | [optional] |
| **query_type** | str | The type of the query that surfaced the document. | [optional] |
| **surfacing_method** | str | The method how knowledge was surfaced. Article: Full article was shown. Snippet: A snippet from the article was shown. Highlight: A highlighted answer in a snippet was shown.Generative: A generated answer in a snippet was shown. | [optional] |
| **application** | [KnowledgeSearchClientApplication](KnowledgeSearchClientApplication) | The client application from which the document was viewed. | |
| **session_id** | str | The unique identifier of the knowledge session in which the document was viewed. | [optional] |
| **conversation_context** | [KnowledgeConversationContext](KnowledgeConversationContext) | Conversation context information if the document was viewed in the context of a conversation. | [optional] |



_PureCloudPlatformClientV2 240.0.0_

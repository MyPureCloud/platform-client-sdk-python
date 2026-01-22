# KnowledgeDocumentChunkRequest

## KnowledgeDocumentChunkRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **query** | str | Query to search chunks in the knowledge base. | |
| **page_size** | int | Page size of the returned results. | [optional] |
| **page_number** | int | Page number of the returned results. | [optional] |
| **filter** | [DocumentQuery](DocumentQuery) | Filter for the document chunks. | [optional] |
| **query_type** | str | The type of the query that initiates the chunks search. | [optional] |
| **preprocess_query** | bool | Indicates whether the chunks search query should be preprocessed. | [optional] |
| **include_draft_documents** | bool | Indicates whether the chunk results would also include draft documents. | [optional] |
| **application** | [KnowledgeSearchClientApplication](KnowledgeSearchClientApplication) | The client application details from which chunks request was sent. | [optional] |
| **conversation_context** | [KnowledgeConversationContext](KnowledgeConversationContext) | Conversation context information if the chunks search is initiated in the context of a conversation. | [optional] |
| **confidence_threshold** | float | The confidence threshold for the chunk results. If applied, the returned results will have an equal or higher confidence than the threshold. The value should be between 0 to 1. | [optional] |



_PureCloudPlatformClientV2 249.0.0_

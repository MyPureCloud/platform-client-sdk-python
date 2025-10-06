# KnowledgeDocumentChunkResponse

## KnowledgeDocumentChunkResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **query** | str | Query to search chunks in the knowledge base. | [optional] |
| **total** | int | The total number of chunks matching the query. | [optional] |
| **page_count** | int | Number of pages returned in the result calculated according to the pageSize and the total | [optional] |
| **page_size** | int | Page size of the returned results. | [optional] |
| **page_number** | int | Page number of the returned results. | [optional] |
| **query_type** | str | The type of the query that initiates the chunks search. | [optional] |
| **search_id** | str | The globally unique identifier for the chunks search. | [optional] |
| **preprocess_query** | bool | Indicates whether the chunks search query should be preprocessed. | [optional] |
| **confidence_threshold** | float | The confidence threshold for the chunk results. If applied, the returned results will have an equal or higher chunk confidence than the threshold. | [optional] |
| **results** | [list[DocumentChunkBlock]](DocumentChunkBlock) | Chunks matching the search query. | [optional] |
| **application** | [KnowledgeSearchClientApplication](KnowledgeSearchClientApplication) | The client application details from which chunks search happened. | [optional] |
| **conversation_context** | [KnowledgeConversationContextResponse](KnowledgeConversationContextResponse) | Conversation context information if the chunks search is initiated in the context of a conversation. | [optional] |



_PureCloudPlatformClientV2 240.0.0_

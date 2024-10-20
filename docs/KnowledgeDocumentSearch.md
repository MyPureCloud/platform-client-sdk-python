# KnowledgeDocumentSearch

## KnowledgeDocumentSearch

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **query** | str | Query to search content in the knowledge base. Maximum of 30 records per query can be fetched. | |
| **page_size** | int | Page size of the returned results. | [optional] |
| **page_number** | int | Page number of the returned results. | [optional] |
| **search_id** | str | The globally unique identifier for the search. | [optional] |
| **total** | int | The total number of documents matching the query. | [optional] |
| **page_count** | int | Number of pages returned in the result calculated according to the pageSize and the total | [optional] |
| **query_type** | str | The type of the query that initiates the search. | [optional] |
| **results** | [list[KnowledgeDocumentSearchResult]](KnowledgeDocumentSearchResult) | Documents matching the search query. | [optional] |
| **application** | [KnowledgeSearchClientApplication](KnowledgeSearchClientApplication) | The client application details from which search happened. | [optional] |
| **conversation_context** | [KnowledgeConversationContextResponse](KnowledgeConversationContextResponse) | Conversation context information if the search is initiated in the context of a conversation. | [optional] |
| **confidence_threshold** | float | The confidence threshold for the search results. If applied, the returned results will have an equal or higher confidence than the threshold. | [optional] |
| **answer_generation** | [KnowledgeAnswerGenerationResponse](KnowledgeAnswerGenerationResponse) | The results with AI-generated answer if the answerMode request property contains \&quot;AnswerGeneration\&quot;. | [optional] |



_PureCloudPlatformClientV2 214.0.0_

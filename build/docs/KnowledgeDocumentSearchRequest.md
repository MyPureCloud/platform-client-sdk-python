# KnowledgeDocumentSearchRequest

## KnowledgeDocumentSearchRequest

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
| **include_draft_documents** | bool | Indicates whether the search results would also include draft documents. | [optional] |
| **interval** | [DocumentQueryInterval](DocumentQueryInterval) | Retrieves the documents created/modified/published in specified date and time range. | [optional] |
| **filter** | [DocumentQuery](DocumentQuery) | Filter for the document search. | [optional] |
| **sort_order** | str | The sort order for search results. | [optional] |
| **sort_by** | str | The field in the documents that you want to sort the search results by. | [optional] |
| **application** | [KnowledgeSearchClientApplication](KnowledgeSearchClientApplication) | The client application details from which search request was sent. | [optional] |
| **conversation_context** | [KnowledgeConversationContext](KnowledgeConversationContext) | Conversation context information if the search is initiated in the context of a conversation. | [optional] |
| **confidence_threshold** | float | The confidence threshold for the search results. If applied, the returned results will have an equal or higher confidence than the threshold. The value should be between 0 to 1. | [optional] |
| **answer_highlight_top_results** | int | The number of articles to be sent for answer-highlighting. Can range from 1-5. | [optional] |
| **answer_mode** | list[str] | Allows extracted answers from an article (AnswerHighlight) and/or AI-generated answers (AnswerGeneration). Default mode: AnswerHighlight. Use this property with answerHighlightTopResults. | [optional] |
| **preprocess_query** | bool | Indicates whether the search query should be preprocessed. | [optional] |



_PureCloudPlatformClientV2 242.0.0_

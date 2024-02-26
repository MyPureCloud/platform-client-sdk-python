---
title: KnowledgeDocumentSearch
---
## KnowledgeDocumentSearch

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **query** | **str** | Query to search content in the knowledge base. Maximum of 30 records per query can be fetched. | |
| **page_size** | **int** | Page size of the returned results. | [optional] |
| **page_number** | **int** | Page number of the returned results. | [optional] |
| **search_id** | **str** | The globally unique identifier for the search. | [optional] |
| **total** | **int** | The total number of documents matching the query. | [optional] |
| **page_count** | **int** | Number of pages returned in the result calculated according to the pageSize and the total | [optional] |
| **query_type** | **str** | The type of the query that initiates the search. | [optional] |
| **results** | [**list[KnowledgeDocumentSearchResult]**](KnowledgeDocumentSearchResult.html) | Documents matching the search query. | [optional] |
| **application** | [**KnowledgeSearchClientApplication**](KnowledgeSearchClientApplication.html) | The client application details from which search happened. | [optional] |
| **conversation_context** | [**KnowledgeConversationContextResponse**](KnowledgeConversationContextResponse.html) | Conversation context information if the search is initiated in the context of a conversation. | [optional] |
| **confidence_threshold** | **float** | The confidence threshold for the search results. If applied, the returned results will have an equal or higher confidence than the threshold. | [optional] |
{: class="table table-striped"}



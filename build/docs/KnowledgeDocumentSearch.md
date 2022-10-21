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
| **results** | [**list[KnowledgeDocumentSearchResult]**](KnowledgeDocumentSearchResult.html) | Documents matching the search query. | [optional] |
| **application** | [**KnowledgeSearchClientApplication**](KnowledgeSearchClientApplication.html) | The client application details from which search happened. | [optional] |
{: class="table table-striped"}



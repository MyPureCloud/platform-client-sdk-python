---
title: KnowledgeDocumentSearchRequest
---
## KnowledgeDocumentSearchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **query** | **str** | Query to search content in the knowledge base. Maximum of 30 records per query can be fetched. | |
| **page_size** | **int** | Page size of the returned results. | [optional] |
| **page_number** | **int** | Page number of the returned results. | [optional] |
| **search_id** | **str** | The globally unique identifier for the search. | [optional] |
| **total** | **int** | The total number of documents matching the query. | [optional] |
| **page_count** | **int** | Number of pages returned in the result calculated according to the pageSize and the total | [optional] |
| **include_draft_documents** | **bool** | Indicates whether the search results would also include draft documents. | [optional] |
{: class="table table-striped"}


# KnowledgeDocumentGuestSearchRequest

## KnowledgeDocumentGuestSearchRequest

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
| **session_id** | str | Session ID of the search. | [optional] |
| **answer_highlight_top_results** | int | The number of articles to be sent for answer-highlighting. Can range from 1-5. | [optional] |
| **include_draft_documents** | bool | Indicates whether the search results would also include draft documents. | [optional] |



_PureCloudPlatformClientV2 221.0.0_

# KnowledgeDocumentQueryResponse

## KnowledgeDocumentQueryResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **page_size** | int | Page size of the returned results. | [optional] |
| **page_number** | int | Page number of the returned results. | [optional] |
| **total** | int | The total number of documents matching the query. | [optional] |
| **page_count** | int | The total number of pages of results, calculated according to the pageSize and the total matching documents. | [optional] |
| **results** | [list[KnowledgeDocumentResponse]](KnowledgeDocumentResponse) | Documents matching the query. | [optional] |



_PureCloudPlatformClientV2 227.0.0_

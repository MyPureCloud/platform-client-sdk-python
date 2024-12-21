# KnowledgeDocumentBulkRequest

## KnowledgeDocumentBulkRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | str | Document type according to assigned template | |
| **external_url** | str | External Url to the document | [optional] |
| **faq** | [DocumentFaq](DocumentFaq) | Faq document details | [optional] |
| **categories** | [list[DocumentCategoryInput]](DocumentCategoryInput) | Document categories | [optional] |
| **article** | [DocumentArticle](DocumentArticle) | Article details | [optional] |
| **id** | str | Identifier of document for update. Omit for create new Document. | [optional] |



_PureCloudPlatformClientV2 219.0.0_

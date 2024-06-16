---
title: KnowledgeSearchDocumentResponse
---
## KnowledgeSearchDocumentResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **title** | **str** | Document title, having a limit of 500 words. | [optional] |
| **visible** | **bool** | Indicates if the knowledge document should be included in search results. | [optional] |
| **alternatives** | [**list[KnowledgeDocumentAlternative]**](KnowledgeDocumentAlternative.html) | List of alternate phrases related to the title which improves search results. | [optional] |
| **state** | **str** | State of the document. | [optional] |
| **date_created** | **datetime** | Document creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | Document last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_imported** | **datetime** | Document import date-time, or null if was not imported. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **last_published_version_number** | **int** | The last published version number of the document. | [optional] |
| **date_published** | **datetime** | The date on which the document was last published. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [**UserReference**](UserReference.html) | The user who created the document. | [optional] |
| **modified_by** | [**UserReference**](UserReference.html) | The user who modified the document. | [optional] |
| **document_version** | [**AddressableEntityRef**](AddressableEntityRef.html) | The version of the document. | [optional] |
| **category** | [**CategoryResponse**](CategoryResponse.html) | The reference to category associated with the document. | [optional] |
| **labels** | [**list[LabelResponse]**](LabelResponse.html) | The references to labels associated with the document. | [optional] |
| **knowledge_base** | [**KnowledgeBaseReference**](KnowledgeBaseReference.html) | Knowledge base to which the document belongs to. | [optional] |
| **external_id** | **str** | The reference to external id associated with the document. | [optional] |
| **source** | [**AddressableEntityRef**](AddressableEntityRef.html) | The reference to source associated with the document. | [optional] |
| **readonly** | **bool** | Whether the document is read-only. | [optional] |
| **variations** | [**list[DocumentVariationAnswer]**](DocumentVariationAnswer.html) | Variations of the document. | [optional] |
| **answer** | **str** | The answer to the query. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



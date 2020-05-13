---
title: KnowledgeDocument
---
## KnowledgeDocument

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **language_code** | **str** | Language of the document | |
| **type** | **str** | Document type | |
| **faq** | [**DocumentFaq**](DocumentFaq.html) | FAQ document details | [optional] |
| **date_created** | **datetime** | Document creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Document last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **categories** | [**list[KnowledgeCategory]**](KnowledgeCategory.html) | Document categories | [optional] |
| **knowledge_base** | [**KnowledgeBase**](KnowledgeBase.html) | Knowledge base which document does belong to | [optional] |
| **external_url** | **str** | External URL to the document | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



---
title: CategoryResponse
---
## CategoryResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the category. | |
| **description** | **str** | The description for the category. | [optional] |
| **date_created** | **datetime** | The creation date-time for the category. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | The last modification date-time for the category. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **parent_category** | [**CategoryReference**](CategoryReference.html) | The reference to category to which this category belongs to. | [optional] |
| **document_count** | **int** | Number of documents assigned to this category. | [optional] |
| **knowledge_base** | [**KnowledgeBaseReference**](KnowledgeBaseReference.html) | The reference to knowledge base to which the category belongs to. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



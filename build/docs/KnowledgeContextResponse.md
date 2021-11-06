---
title: KnowledgeContextResponse
---
## KnowledgeContextResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Context ID. | [optional] |
| **name** | **str** | Context name. | |
| **description** | **str** | Context description. | [optional] |
| **date_created** | **datetime** | The date when the context was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **date_modified** | **datetime** | The date when the context was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **values** | [**list[KnowledgeContextValueResponse]**](KnowledgeContextValueResponse.html) | Knowledge context values. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



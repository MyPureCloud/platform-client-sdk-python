# CategoryResponse

## CategoryResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the category. | |
| **description** | str |  | [optional] |
| **external_id** | str |  | [optional] |
| **date_created** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **parent_category** | [CategoryReference](CategoryReference) | The reference to category to which this category belongs to. | [optional] |
| **document_count** | int | Number of documents assigned to this category. | [optional] |
| **knowledge_base** | [KnowledgeBaseReference](KnowledgeBaseReference) | The reference to knowledge base to which the category belongs to. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 211.0.0_

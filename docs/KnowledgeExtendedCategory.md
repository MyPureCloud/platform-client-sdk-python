# KnowledgeExtendedCategory

## KnowledgeExtendedCategory

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | Category name | |
| **description** | str | Category description | [optional] |
| **knowledge_base** | [KnowledgeBase](KnowledgeBase) | Knowledge base which category does belong to | [optional] |
| **language_code** | str | Actual language of the category | [optional] |
| **date_created** | datetime | Category creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Category last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **parent** | [KnowledgeCategory](KnowledgeCategory) | Category parent | [optional] |
| **children** | [list[KnowledgeCategory]](KnowledgeCategory) | Category children | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 211.0.0_

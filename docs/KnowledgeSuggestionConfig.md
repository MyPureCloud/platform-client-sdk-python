# KnowledgeSuggestionConfig

## KnowledgeSuggestionConfig

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **vendor_name** | str | The name of vendor used for knowledge suggestions. | |
| **knowledge_base** | [KnowledgeBaseReference](KnowledgeBaseReference) | The ID of knowledge base to query when Genesys is the knowledge suggestions provider. | [optional] |
| **knowledge_bases** | [list[KnowledgeBaseWithDialectReference]](KnowledgeBaseWithDialectReference) | The knowledge bases to query based on dialect, when Genesys is the knowledge suggestions provider. | [optional] |
| **receive_segmented_articles** | bool | Include segmented articles in knowledge suggestions. | [optional] |



_PureCloudPlatformClientV2 246.1.0_

---
title: KnowledgeSuggestionConfig
---
## KnowledgeSuggestionConfig

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **vendor_name** | **str** | The name of vendor used for knowledge suggestions. | |
| **knowledge_base** | [**KnowledgeBaseReference**](KnowledgeBaseReference.html) | The ID of knowledge base to query when Genesys is the knowledge suggestions provider. | [optional] |
| **knowledge_bases** | [**list[KnowledgeBaseWithDialectReference]**](KnowledgeBaseWithDialectReference.html) | The knowledge bases to query based on dialect, when Genesys is the knowledge suggestions provider. | [optional] |
{: class="table table-striped"}



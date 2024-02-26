---
title: KnowledgeDocumentPresentation
---
## KnowledgeDocumentPresentation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **documents** | [**list[KnowledgeDocumentVersionVariationReference]**](KnowledgeDocumentVersionVariationReference.html) | The presented documents | |
| **search_id** | **str** | The search that surfaced the documents that were presented. | [optional] |
| **query_type** | **str** | The type of the query that surfaced the documents. | [optional] |
| **session_id** | **str** | Knowledge session ID. | [optional] |
| **conversation_context** | [**KnowledgeConversationContext**](KnowledgeConversationContext.html) | Conversation context information if the documents were presented in the context of a conversation. | [optional] |
| **application** | [**KnowledgeSearchClientApplication**](KnowledgeSearchClientApplication.html) | The client application in which the documents were presented. | |
{: class="table table-striped"}



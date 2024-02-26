---
title: KnowledgeDocumentCopy
---
## KnowledgeDocumentCopy

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **document_variation_id** | **str** | The variation of the document whose content was copied. | |
| **document_version_id** | **str** | The version of the document whose content was copied. | |
| **search_id** | **str** | The search that surfaced the document whose content was copied. | [optional] |
| **query_type** | **str** | The type of the query that surfaced the document. | [optional] |
| **session_id** | **str** | Knowledge session ID. | [optional] |
| **conversation_context** | [**KnowledgeConversationContext**](KnowledgeConversationContext.html) | Conversation context information, if the document content is copied in the context of a conversation. | [optional] |
| **application** | [**KnowledgeSearchClientApplication**](KnowledgeSearchClientApplication.html) | The client application in which the document content was copied. | |
{: class="table table-striped"}



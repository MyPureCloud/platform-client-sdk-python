---
title: KnowledgeDocumentView
---
## KnowledgeDocumentView

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **document_variation_id** | **str** | The variation of the viewed document. | |
| **document_version_id** | **str** | The version of the viewed document. | |
| **search_id** | **str** | The search that surfaced the viewed document. | [optional] |
| **query_type** | **str** | The type of the query that surfaced the document. | [optional] |
| **application** | [**KnowledgeSearchClientApplication**](KnowledgeSearchClientApplication.html) | The client application from which the document was viewed. | |
| **session_id** | **str** | The unique identifier of the knowledge session in which the document was viewed. | [optional] |
| **conversation_context** | [**KnowledgeConversationContext**](KnowledgeConversationContext.html) | Conversation context information if the document was viewed in the context of a conversation. | [optional] |
{: class="table table-striped"}



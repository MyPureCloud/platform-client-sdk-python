# KnowledgeGuestDocumentPresentation

## KnowledgeGuestDocumentPresentation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **documents** | [list[PresentedKnowledgeDocument]](PresentedKnowledgeDocument) | The presented documents | |
| **search_id** | str | The search that surfaced the documents that were presented. | [optional] |
| **query_type** | str | The type of the query that surfaced the documents. | [optional] |
| **surfacing_method** | str | The method how knowledge was surfaced. Article: Full article was shown. Snippet: A snippet from the article was shown. Highlight: A highlighted answer in a snippet was shown.Generative: A generated answer in a snippet was shown. | [optional] |
| **session_id** | str | Knowledge session ID. | [optional] |
| **application** | [KnowledgeGuestSearchClientApplication](KnowledgeGuestSearchClientApplication) | The client application in which the documents were presented. | [optional] |



_PureCloudPlatformClientV2 230.0.0_

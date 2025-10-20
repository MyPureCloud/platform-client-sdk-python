# KnowledgeGuestDocumentCopy

## KnowledgeGuestDocumentCopy

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **document_variation_id** | str | The variation of the document whose content was copied. | |
| **document_version_id** | str | The version of the document whose content was copied. | |
| **search_id** | str | The search that surfaced the document whose content was copied. | [optional] |
| **query_type** | str | The type of the query that surfaced the document. | [optional] |
| **surfacing_method** | str | The method how knowledge was surfaced. Article: Full article was shown. Snippet: A snippet from the article was shown. Highlight: A highlighted answer in a snippet was shown.Generative: A generated answer in a snippet was shown. | [optional] |
| **session_id** | str | Knowledge session ID. | [optional] |
| **application** | [KnowledgeGuestSearchClientApplication](KnowledgeGuestSearchClientApplication) | The client application in which the document content was copied. | [optional] |



_PureCloudPlatformClientV2 241.0.0_

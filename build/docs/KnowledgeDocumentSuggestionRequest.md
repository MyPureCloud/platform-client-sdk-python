# KnowledgeDocumentSuggestionRequest

## KnowledgeDocumentSuggestionRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **query** | str | Query to get autocomplete suggestions for the matching knowledge documents. | |
| **page_size** | int | Page size of the returned results. | [optional] |
| **include_draft_documents** | bool | Indicates whether the suggestion results would also include draft documents. | [optional] |
| **interval** | [DocumentQueryInterval](DocumentQueryInterval) | Retrieves the documents created/modified/published in specified date and time range. | [optional] |
| **filter** | [DocumentQuery](DocumentQuery) | Filter for the document suggestions. | [optional] |



_PureCloudPlatformClientV2 233.0.0_

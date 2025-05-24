# KnowledgeDocumentQuery

## KnowledgeDocumentQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **page_size** | int | Page size of the returned results. | [optional] |
| **page_number** | int | Page number of the returned results. | [optional] |
| **include_draft_documents** | bool | Indicates whether the results would also include draft documents. | [optional] |
| **interval** | [DocumentQueryInterval](DocumentQueryInterval) | Retrieves the documents created/modified/published in specified date and time range. | [optional] |
| **filter** | [DocumentQuery](DocumentQuery) | Filter for the document query. | |
| **include_variations** | str | Indicates which document variations to include in returned documents. All: all variations regardless of the filter expression; AllMatching: all variations that match the filter expression; SingleMostRelevant: single variation that matches the filter expression and has the highest priority. The default is All. | [optional] |
| **sort_order** | str | The sort order for results. | [optional] |
| **sort_by** | str | The field in the documents that you want to sort the results by. | [optional] |



_PureCloudPlatformClientV2 229.0.0_

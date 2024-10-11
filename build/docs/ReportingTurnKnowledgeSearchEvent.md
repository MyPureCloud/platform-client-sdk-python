# ReportingTurnKnowledgeSearchEvent

## ReportingTurnKnowledgeSearchEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **search_id** | str | The ID of this knowledge search. | [optional] |
| **knowledge_base_id** | str | The Knowledge Base ID that the captured knowledge data relates to. | [optional] |
| **documents** | [list[ReportingTurnKnowledgeDocument]](ReportingTurnKnowledgeDocument) | The list of search documents that the feedback applies to. | [optional] |
| **search_query** | str | The search query that was used to search the Knowledge Base documents for a matching question. | [optional] |
| **answer_document_id** | str | The document ID of the search answer. | [optional] |



_PureCloudPlatformClientV2 213.0.0_

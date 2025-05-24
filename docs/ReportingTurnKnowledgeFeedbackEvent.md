# ReportingTurnKnowledgeFeedbackEvent

## ReportingTurnKnowledgeFeedbackEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **search_id** | str | The ID of this knowledge search. | [optional] |
| **knowledge_base_id** | str | The Knowledge Base ID that the captured knowledge data relates to. | [optional] |
| **documents** | [list[ReportingTurnKnowledgeDocument]](ReportingTurnKnowledgeDocument) | The list of search documents that the feedback applies to. | [optional] |
| **feedback_rating** | int | The feedback rating for the search (1.0 - 5.0). 1 &#x3D; Negative, 5 &#x3D; Positive. | [optional] |
| **document_variation_id** | str | The variation of the document. | [optional] |
| **document_version_id** | str | The version of the document. | [optional] |



_PureCloudPlatformClientV2 229.0.0_

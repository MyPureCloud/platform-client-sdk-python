# ReportingTurnKnowledgeMetadata

## ReportingTurnKnowledgeMetadata

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **knowledge_id** | str | The ID of the knowledge setting or knowledge base | [optional] |
| **knowledge_name** | str | The name of the knowledge setting or knowledge base | [optional] |
| **search_id** | str | SearchID used in the attempted search | [optional] |
| **query** | str | The query used in the knowledge query | [optional] |
| **retrieval_status** | str | The result of the knowledge search | [optional] |
| **answer_generation_status** | str | The result of the knowledge generation | [optional] |
| **generated_answer** | str | The generated answer | [optional] |
| **failure_reason** | str | Failure reason if knowledge query failed | [optional] |
| **top_confidence** | float | Highest confidence score of returned knowledgeSources | [optional] |
| **retrieved_sources** | [list[KnowledgeSource]](KnowledgeSource) | List of the sources retrieved by the knowledge search | [optional] |



_PureCloudPlatformClientV2 266.0.0_

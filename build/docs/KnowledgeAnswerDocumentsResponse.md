# KnowledgeAnswerDocumentsResponse

## KnowledgeAnswerDocumentsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **results** | [list[KnowledgeAnswerDocumentResponse]](KnowledgeAnswerDocumentResponse) | The results with answers if the answerMode request property is not set or contains \&quot;AnswerHighlight\&quot;. Empty array otherwise. | [optional] |
| **answer_generation** | [KnowledgeAnswerGenerationResponse](KnowledgeAnswerGenerationResponse) | The results with AI-generated answer if the answerMode request property contains \&quot;AnswerGeneration\&quot;. | [optional] |



_PureCloudPlatformClientV2 224.1.0_

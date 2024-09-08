---
title: KnowledgeAnswerDocumentsResponse
---
## KnowledgeAnswerDocumentsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **results** | [**list[KnowledgeAnswerDocumentResponse]**](KnowledgeAnswerDocumentResponse.html) | The results with answers if the answerMode request property is not set or contains \&quot;AnswerHighlight\&quot;. Empty array otherwise. | [optional] |
| **answer_generation** | [**KnowledgeAnswerGenerationResponse**](KnowledgeAnswerGenerationResponse.html) | The results with AI-generated answer if the answerMode request property contains \&quot;AnswerGeneration\&quot;. | [optional] |
{: class="table table-striped"}



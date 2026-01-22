# EvaluationSearchSubAggregationDTO

## EvaluationSearchSubAggregationDTO

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the aggregation | |
| **field** | str | The field to aggregate on.ALLOWED FIELDS BY AGGREGATION TYPE:TERM/COUNT: evaluationStatus, aiScoringFailureType, questionAiAnswerFailureType,TERM: formId, formIdReleased, contextId, questionGroupId, questionId, questionAnswerId, released, questionGroupMarkedNA, questionMarkedNA, questionAiScored, questionEaScored,SUM/AVERAGE/STATS/RANGE: totalScore, totalCriticalScore, questionGroupScorePercentage,criticalQuestionGroupScorePercentage, questionScore,SUM: disputeCount, rescoreCount, eaSuggestionCount, eaAcceptedSuggestionCount,aiSuggestionCount, aiAcceptedSuggestionCount,DATE_HISTOGRAM: conversationDate, createdDate, submittedDate, releaseDate | |
| **type** | str | The Type of Aggregation to Perform | |
| **size** | int | The size limit for term aggregations, 100 size limit for all fields | [optional] |
| **calendar_interval** | str | The calendar interval for date histogram aggregations | [optional] |
| **format** | str | The format for date histogram aggregations | [optional] |
| **ranges** | [list[QueryApiSearchAggregationRange]](QueryApiSearchAggregationRange) | The ranges for range aggregations | [optional] |
| **sub_aggregations** | [list[EvaluationSearchSubAggregationDTO]](EvaluationSearchSubAggregationDTO) | Sub-aggregations to be computed within this aggregation | [optional] |



_PureCloudPlatformClientV2 249.0.0_

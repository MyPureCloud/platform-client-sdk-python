# AssessmentQuestionGroupScore

## AssessmentQuestionGroupScore

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **question_group_id** | str | The ID of the question group | |
| **total_score** | float | The total score for the questions | [optional] |
| **max_total_score** | float | The maximum total score for the questions | [optional] |
| **marked_na** | bool | True if this question group is marked NA | [optional] |
| **system_marked_na** | bool | If markedNA is true, systemMarkedNA indicates whether it was marked by a user or by the system due to visibility conditions. Always false if markedNA is false. | [optional] |
| **total_critical_score** | float | The total score for the critical questions | [optional] |
| **max_total_critical_score** | float | The maximum total score for the critical questions | [optional] |
| **total_non_critical_score** | float | The total score for the non-critical questions | [optional] |
| **max_total_non_critical_score** | float | The maximum total score for the non-critical questions | [optional] |
| **total_score_unweighted** | float | The unweighted total score for this question group | [optional] |
| **max_total_score_unweighted** | float | The maximum unweighted total score for this question group | [optional] |
| **total_critical_score_unweighted** | float | The unweighted total score for the critical questions | [optional] |
| **max_total_critical_score_unweighted** | float | The maximum unweighted total score for the critical questions | [optional] |
| **total_non_critical_score_unweighted** | float | The total unweighted score for the non-critical questions | [optional] |
| **max_total_non_critical_score_unweighted** | float | The maximum unweighted total score for the non-critical questions | [optional] |
| **question_scores** | [list[AssessmentQuestionScore]](AssessmentQuestionScore) | The individual question scores | [optional] |



_PureCloudPlatformClientV2 219.0.0_

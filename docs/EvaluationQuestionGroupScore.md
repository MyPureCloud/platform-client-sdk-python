# EvaluationQuestionGroupScore

## EvaluationQuestionGroupScore

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **question_group_id** | str |  | [optional] |
| **total_score** | float | Score of all questions in the group | [optional] |
| **max_total_score** | float | Maximum possible score of all questions in the group | [optional] |
| **marked_na** | bool | True when the evaluation is submitted with a question group that does not have any answers. Only allowed when naEnabled is true or if set by the system | [optional] |
| **system_marked_na** | bool | If markedNA is true, systemMarkedNA indicates whether it was marked by a user or by the system due to visibility conditions. Always false if markedNA is false. | [optional] |
| **total_critical_score** | float | Score of only the critical questions in the group | [optional] |
| **max_total_critical_score** | float | Maximum possible score of only the critical questions in the group | [optional] |
| **total_non_critical_score** | float | Score of only the non critical questions in the group | [optional] |
| **max_total_non_critical_score** | float | Maximum possible score of only the non critical questions in the group | [optional] |
| **total_score_unweighted** | float | Unweighted score of all questions in the group | [optional] |
| **max_total_score_unweighted** | float | Maximum possible unweighted score of all questions in the group | [optional] |
| **total_critical_score_unweighted** | float | Unweighted score of only the critical questions in the group | [optional] |
| **max_total_critical_score_unweighted** | float | Maximum possible unweighted score of only the critical questions in the group | [optional] |
| **total_non_critical_score_unweighted** | float | Unweighted score of only the non critical questions in the group | [optional] |
| **max_total_non_critical_score_unweighted** | float | Maximum possible unweighted score of only the non critical questions in the group | [optional] |
| **question_scores** | [list[EvaluationQuestionScore]](EvaluationQuestionScore) |  | [optional] |



_PureCloudPlatformClientV2 246.0.0_

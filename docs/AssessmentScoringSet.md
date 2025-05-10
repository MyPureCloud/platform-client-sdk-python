# AssessmentScoringSet

## AssessmentScoringSet

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **total_score** | float | The total score of the answers | [optional] |
| **total_critical_score** | float | The total score for the critical questions | [optional] |
| **total_non_critical_score** | float | The total score for the non-critical questions | [optional] |
| **question_group_scores** | [list[AssessmentQuestionGroupScore]](AssessmentQuestionGroupScore) | The individual scores for each question group | |
| **failure_reasons** | list[str] | If the assessment was not passed, the reasons for failure. | [optional] |
| **comments** | str | Comments provided for these answers. | [optional] |
| **agent_comments** | str | Comments provided by agent. | [optional] |
| **is_passed** | bool | True if the assessment was passed | [optional] |



_PureCloudPlatformClientV2 228.0.0_

# SurveyQuestionGroupScore

## SurveyQuestionGroupScore

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **question_group_id** | str |  | [optional] |
| **total_score** | float | Score of all questions in the group | [optional] |
| **max_total_score** | float | Maximum possible score of all questions in the group | [optional] |
| **marked_na** | bool | True when the evaluation is submitted with a question group that does not have any answers. Only allowed when naEnabled is true or if set by the system | [optional] |
| **system_marked_na** | bool | If markedNA is true, systemMarkedNA indicates whether it was marked by a user or by the system due to visibility conditions. Always false if markedNA is false. | [optional] |
| **question_scores** | [list[SurveyQuestionScore]](SurveyQuestionScore) |  | [optional] |



_PureCloudPlatformClientV2 234.0.0_

# SurveyQuestionScore

## SurveyQuestionScore

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **question_id** | str |  | [optional] |
| **answer_id** | str |  | [optional] |
| **score** | int | Unweighted score of the question | [optional] |
| **marked_na** | bool | True when the evaluation is submitted with a question that does not have an answer. Only allowed when naEnabled is true or if set by the system | [optional] |
| **system_marked_na** | bool | If markedNA is true, systemMarkedNA indicates whether it was marked by a user or by the system due to visibility conditions. Always false if markedNA is false. | [optional] |
| **assisted_answer_id** | str | AnswerId found with evaluation assistance conditions | [optional] |
| **nps_score** | int |  | [optional] |
| **nps_text_answer** | str |  | [optional] |
| **free_text_answer** | str |  | [optional] |



_PureCloudPlatformClientV2 227.0.0_

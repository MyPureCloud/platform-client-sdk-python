# EvaluationQuestionScore

## EvaluationQuestionScore

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **question_id** | str |  | [optional] |
| **answer_id** | str |  | [optional] |
| **score** | int | Unweighted score of the question | [optional] |
| **marked_na** | bool | True when the evaluation is submitted with a question that does not have an answer. Only allowed when naEnabled is true or if set by the system | [optional] |
| **system_marked_na** | bool | If markedNA is true, systemMarkedNA indicates whether it was marked by a user or by the system due to visibility conditions. Always false if markedNA is false. | [optional] |
| **assisted_answer_id** | str | AnswerId found with evaluation assistance conditions | [optional] |
| **failed_kill_question** | bool | Applicable only on fatal questions. Indicates that the answer selected was not the highest score available for the question | [optional] |
| **comments** | str | Comments from the evaluator specific to this question | [optional] |



_PureCloudPlatformClientV2 218.0.0_

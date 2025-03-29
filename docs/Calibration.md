# Calibration

## Calibration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **calibrator** | [User](User) |  | [optional] |
| **agent** | [User](User) |  | [optional] |
| **conversation** | [ConversationReference](ConversationReference) |  | [optional] |
| **evaluation_form** | [EvaluationForm](EvaluationForm) |  | [optional] |
| **context_id** | str |  | [optional] |
| **average_score** | int |  | [optional] |
| **high_score** | int |  | [optional] |
| **low_score** | int |  | [optional] |
| **created_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **evaluations** | [list[Evaluation]](Evaluation) |  | [optional] |
| **evaluators** | [list[User]](User) |  | [optional] |
| **scoring_index** | [Evaluation](Evaluation) |  | [optional] |
| **expert_evaluator** | [User](User) |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 224.1.0_

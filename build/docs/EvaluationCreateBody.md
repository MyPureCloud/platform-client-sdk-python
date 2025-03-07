# EvaluationCreateBody

## EvaluationCreateBody

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **evaluation_form** | [EvaluationCreateEvalForm](EvaluationCreateEvalForm) | Evaluation form used for evaluation (must be included for a successful request) | [optional] |
| **evaluator** | [EvaluationCreateUser](EvaluationCreateUser) | User ID of the evaluator (must be included for a successful request) | [optional] |
| **agent** | [EvaluationCreateUser](EvaluationCreateUser) | User ID of the agent (must be included for a successful request) | [optional] |
| **agent_has_read** | bool |  | [optional] |
| **answers** | [EvaluationScoringSet](EvaluationScoringSet) |  | [optional] |
| **calibration** | [EvaluationCreateCalibration](EvaluationCreateCalibration) |  | [optional] |
| **evaluation_context_id** | str |  | [optional] |
| **conversation** | [EvaluationCreateConversation](EvaluationCreateConversation) |  | [optional] |
| **resource_type** | str |  | [optional] |
| **evaluation_source** | [EvaluationSource](EvaluationSource) |  | [optional] |
| **rescore** | bool |  | [optional] |
| **queue** | [EvaluationCreateQueue](EvaluationCreateQueue) |  | [optional] |
| **release_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **status** | str |  | [optional] |
| **never_release** | bool |  | [optional] |
| **date_assignee_changed** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **assignee** | [EvaluationCreateUser](EvaluationCreateUser) |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 223.0.0_

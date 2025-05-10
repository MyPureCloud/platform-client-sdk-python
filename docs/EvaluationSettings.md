# EvaluationSettings

## EvaluationSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **revisions_enabled** | bool | Whether revisions are allowed for evaluations. When enabled, rescoring creates a new version of the evaluation and retracts the existing evaluation version. Does not apply for calibration evaluations. | [optional] |
| **disputes_enabled** | bool | Whether disputes are allowed for evaluations. Does not apply for calibration evaluations. | [optional] |
| **disputes_allowed_per_evaluation** | int | The maximum number of disputes allowed for an evaluation. | [optional] |
| **disputes_assignees** | [list[EvaluationSettingsAssignee]](EvaluationSettingsAssignee) | A list of assignees responsible for handling each dispute. This list size needs to be equal to disputesAllowedPerEvaluation. | [optional] |



_PureCloudPlatformClientV2 228.0.0_

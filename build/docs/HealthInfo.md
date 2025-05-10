# HealthInfo

## HealthInfo

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **status** | str | Status of health computation for this intent. | [optional] |
| **error_info** | [FlowHealthErrorInfo](FlowHealthErrorInfo) | Error details for the intent, if any. | [optional] |
| **overall_score** | float | Overall health score for the intent ranged between 0 and 100 as 100 is the perfect health score. | [optional] |
| **issue_count** | int | Number of issues found in the intent. | [optional] |
| **static_validation_results** | list[str] | Validation results for the intent. | [optional] |
| **utterances** | [list[FlowHealthIntentUtterance]](FlowHealthIntentUtterance) | Utterances for this intent. | [optional] |



_PureCloudPlatformClientV2 228.0.0_

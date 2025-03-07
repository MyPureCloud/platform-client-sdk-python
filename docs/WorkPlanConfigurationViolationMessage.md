# WorkPlanConfigurationViolationMessage

## WorkPlanConfigurationViolationMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | str | Type of configuration violation message for this work plan | [optional] |
| **arguments** | [list[WorkPlanValidationMessageArgument]](WorkPlanValidationMessageArgument) | Arguments of the message that provide information about the misconfigured value or the threshold that is exceeded by the misconfigured value | [optional] |
| **severity** | str | Severity of the message. A message with Error severity indicates the scheduler won&#39;t be able to produce schedules and thus the work plan is invalid. | [optional] |



_PureCloudPlatformClientV2 223.0.0_

# ValidateWorkPlanMessages

## ValidateWorkPlanMessages

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **violation_messages** | [list[WorkPlanConfigurationViolationMessage]](WorkPlanConfigurationViolationMessage) | Messages for work plan violating some rules such as no shifts in a work plan | [optional] |
| **constraint_conflict_message** | [ConstraintConflictMessage](ConstraintConflictMessage) | This field is not null when there is a set of work plan constraints that conflict thus agent schedules cannot be generated | [optional] |



_PureCloudPlatformClientV2 224.1.0_

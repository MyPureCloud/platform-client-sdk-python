# ScheduleSetError

## ScheduleSetError

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **error_code** | str | Error code that indicates why schedule set optimization failed. At least one of workPlans or workPlanRotations is set if there is an error during optimization | |
| **work_plans** | [list[WorkPlanReference]](WorkPlanReference) | Work plans involved in the optimization failure | [optional] |
| **work_plan_rotations** | [list[WorkPlanRotationReference]](WorkPlanRotationReference) | Work plan rotations involved in the optimization failure | [optional] |



_PureCloudPlatformClientV2 261.0.0_

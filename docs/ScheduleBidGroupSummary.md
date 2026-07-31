# ScheduleBidGroupSummary

## ScheduleBidGroupSummary

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | |
| **name** | str | The name assigned to this bid group | |
| **management_unit** | [ManagementUnitReference](ManagementUnitReference) | The management unit to which this bid group belongs | |
| **agent_count** | int | The number of agents in this bid group | |
| **work_plan_count** | int | The number of work plans in this bid group or the number of work plans in rotations | |
| **work_plan_rotation_count** | int | The number of work plan rotations used in this bid group | |
| **planning_group_count** | int | The number of planning groups in this bid group | |
| **schedule_set_error** | [ScheduleSetError](ScheduleSetError) | Schedule set optimization error details for this bid group. Present only when optimization fails | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 263.0.0_

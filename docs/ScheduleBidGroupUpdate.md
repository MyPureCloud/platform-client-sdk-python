# ScheduleBidGroupUpdate

## ScheduleBidGroupUpdate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the schedule bid group | [optional] |
| **management_unit_id** | str | The ID of the management unit to which this bid group belongs | [optional] |
| **agent_ids** | [SetWrapperString](SetWrapperString) | The IDs of the agents who participate in this bid group | [optional] |
| **work_plan_ids** | [SetWrapperString](SetWrapperString) | The IDs of the work plans used in this bid group | [optional] |
| **work_plan_rotations** | [ListWrapperBidGroupWorkPlanRotationRequest](ListWrapperBidGroupWorkPlanRotationRequest) | The work plan rotations used in this bid group | [optional] |
| **planning_group_ids** | [SetWrapperString](SetWrapperString) | The IDs of the planning groups selected in this bid group | [optional] |
| **schedule_sets** | [ListWrapperScheduleSetRequest](ListWrapperScheduleSetRequest) | The schedule sets generated for this bid group | [optional] |



_PureCloudPlatformClientV2 260.0.0_

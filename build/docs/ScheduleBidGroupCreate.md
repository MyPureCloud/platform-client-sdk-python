# ScheduleBidGroupCreate

## ScheduleBidGroupCreate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the schedule bid group | |
| **management_unit_id** | str | The ID of the management unit to which this bid group belongs | |
| **agent_ids** | list[str] | The IDs of the agents who participate in this bid group | |
| **work_plan_ids** | list[str] | The IDs of the work plans used in this bid group | [optional] |
| **work_plan_rotations** | [list[BidGroupWorkPlanRotationRequest]](BidGroupWorkPlanRotationRequest) | The work plan rotations used in this bid group | [optional] |
| **planning_group_ids** | list[str] | The IDs of the planning groups selected in this bid group | |



_PureCloudPlatformClientV2 263.0.0_

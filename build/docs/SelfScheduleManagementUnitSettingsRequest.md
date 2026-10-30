# SelfScheduleManagementUnitSettingsRequest

## SelfScheduleManagementUnitSettingsRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enabled** | bool | Whether agent self-scheduling is enabled for this management unit | [optional] |
| **check_work_plan_constraints** | bool | Whether self-scheduling is further restricted by work plan constraints | [optional] |
| **minimum_minutes_before_earliest_schedule_change** | int | The minimum number of minutes before the new activity start time to which the agent is allowed to self-schedule | [optional] |
| **movable_activity_categories** | [SetWrapperActivityCategory](SetWrapperActivityCategory) | Movable activity categories enabled for self-scheduling | [optional] |
| **movable_activity_code_ids** | [SetWrapperString](SetWrapperString) | Movable activity codes enabled for self-scheduling | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for this management unit&#39;s self-scheduling settings | |



_PureCloudPlatformClientV2 270.0.0_

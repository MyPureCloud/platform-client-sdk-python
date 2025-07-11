# BuUpdateAgentScheduleUploadSchema

## BuUpdateAgentScheduleUploadSchema

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user_id** | str | The ID of the user to whom this agent schedule applies | |
| **work_plan_id** | [ValueWrapperString](ValueWrapperString) | The ID of the work plan for this user.  Mutually exclusive with workPlanIdsPerWeek | [optional] |
| **work_plan_ids_per_week** | [ListWrapperString](ListWrapperString) | The IDs of the work plans per week for this user.  Mutually exclusive with workPlanId | [optional] |
| **shifts** | [list[BuUpdateAgentScheduleShift]](BuUpdateAgentScheduleShift) | The shift definitions for this agent schedule | [optional] |
| **full_day_time_off_markers** | [list[BuFullDayTimeOffMarker]](BuFullDayTimeOffMarker) | Any full day time off markers that apply to this agent schedule | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for this agent schedule. Required if updating or deleting an existing agent schedule, otherwise should be omitted | [optional] |
| **delete** | bool | Whether to delete this agent&#39;s schedule. Defaults to false if not set | [optional] |



_PureCloudPlatformClientV2 233.0.0_

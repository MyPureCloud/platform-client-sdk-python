# BuImportAgentScheduleUploadSchema

## BuImportAgentScheduleUploadSchema

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user_id** | str | The ID of the user to whom this agent schedule applies | |
| **work_plan_id** | [ValueWrapperString](ValueWrapperString) | The ID of the work plan for this user.  Mutually exclusive with workPlanIdsPerWeek | [optional] |
| **work_plan_ids_per_week** | [ListWrapperString](ListWrapperString) | The IDs of the work plans per week for this user.  Mutually exclusive with workPlanId | [optional] |
| **shifts** | [list[BuAgentScheduleShiftRequest]](BuAgentScheduleShiftRequest) | The shift definitions for this agent schedule | [optional] |
| **full_day_time_off_markers** | [list[BuFullDayTimeOffMarker]](BuFullDayTimeOffMarker) | Any full day time off markers that apply to this agent schedule | [optional] |



_PureCloudPlatformClientV2 247.0.0_

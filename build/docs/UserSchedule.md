# UserSchedule

## UserSchedule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **shifts** | [list[UserScheduleShift]](UserScheduleShift) | The shifts that belong to this schedule | [optional] |
| **full_day_time_off_markers** | [list[UserScheduleFullDayTimeOffMarker]](UserScheduleFullDayTimeOffMarker) | Markers to indicate a full day time off request, relative to the management unit time zone | [optional] |
| **delete** | bool | If marked true for updating an existing user schedule, it will be deleted | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for this schedule | |
| **work_plan_id** | str | ID of the work plan associated with the user during schedule creation | [optional] |



_PureCloudPlatformClientV2 211.1.0_

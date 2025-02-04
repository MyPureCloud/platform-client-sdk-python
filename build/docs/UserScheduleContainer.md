# UserScheduleContainer

## UserScheduleContainer

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **management_unit_time_zone** | str | The reference time zone used for the management unit | [optional] |
| **published_schedules** | [list[WeekScheduleReference]](WeekScheduleReference) | References to all published week schedules overlapping the start/end date query parameters | [optional] |
| **user_schedules** | [dict(str, UserSchedule)](UserSchedule) | Map of user id to user schedule | [optional] |



_PureCloudPlatformClientV2 221.0.0_

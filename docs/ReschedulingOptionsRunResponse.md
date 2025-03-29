# ReschedulingOptionsRunResponse

## ReschedulingOptionsRunResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **existing_schedule** | [BuScheduleReference](BuScheduleReference) | The existing schedule to which this reschedule run applies | [optional] |
| **start_date** | datetime | The start date of the period to reschedule. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **end_date** | datetime | The end date of the period to reschedule. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **management_units** | [list[ReschedulingManagementUnitResponse]](ReschedulingManagementUnitResponse) | Per-management unit rescheduling options | [optional] |
| **agent_count** | int | The number of agents to be considered in the reschedule | [optional] |
| **activity_code_ids** | list[str] | The IDs of the activity codes being considered for reschedule | [optional] |
| **do_not_change_weekly_paid_time** | bool | Whether weekly paid time is allowed to be changed | [optional] |
| **do_not_change_daily_paid_time** | bool | Whether daily paid time is allowed to be changed | [optional] |
| **do_not_change_shift_start_times** | bool | Whether shift start times are allowed to be changed | [optional] |
| **do_not_change_manually_edited_shifts** | bool | Whether manually edited shifts are allowed to be changed | [optional] |



_PureCloudPlatformClientV2 224.1.0_

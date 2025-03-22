# BuRescheduleRequest

## BuRescheduleRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | datetime | The start of the range to reschedule.  Defaults to the beginning of the schedule. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **end_date** | datetime | The end of the range to reschedule.  Defaults the the end of the schedule. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **agent_ids** | list[str] | The IDs of the agents to consider for rescheduling.  Omit to consider all agents in the specified management units.Agents not in the specified management units will be ignored | [optional] |
| **activity_code_ids** | list[str] | The IDs of the activity codes to consider for rescheduling.  Omit to consider all activity codes | [optional] |
| **management_unit_ids** | list[str] | The IDs of the management units to reschedule | |
| **do_not_change_weekly_paid_time** | bool | Instructs the scheduler whether it is allowed to change weekly paid time | |
| **do_not_change_daily_paid_time** | bool | Instructs the scheduler whether it is allowed to change daily paid time | |
| **do_not_change_shift_start_times** | bool | Instructs the scheduler whether it is allowed to change shift start times | |
| **do_not_change_manually_edited_shifts** | bool | Instructs the scheduler whether it is allowed to change manually edited shifts | |
| **activity_smoothing_type** | str | Overrides the default BU level activity smoothing type for this reschedule run | [optional] |
| **induce_schedule_variability** | bool | Overrides the default BU level induce schedule variability setting for this reschedule run | [optional] |



_PureCloudPlatformClientV2 224.0.0_

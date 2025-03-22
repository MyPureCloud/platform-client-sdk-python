# BuScheduleRun

## BuScheduleRun

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **scheduler_run_id** | str | The scheduler run ID.  Reference this value for support | [optional] |
| **intraday_rescheduling** | bool | Whether this is an intraday rescheduling run | [optional] |
| **state** | str | The state of the generation run | [optional] |
| **week_count** | int | The number of weeks spanned by the schedule | [optional] |
| **percent_complete** | float | Percent completion of the schedule run | [optional] |
| **target_week** | date | The start date of the target week. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **schedule** | [BuScheduleReference](BuScheduleReference) | The generated schedule.  Null unless the schedule run is complete | [optional] |
| **schedule_description** | str | The description of the generated schedule | [optional] |
| **scheduling_start_time** | datetime | When the schedule generation run started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **scheduling_started_by** | [UserReference](UserReference) | The user who started the scheduling run | [optional] |
| **scheduling_canceled_by** | [UserReference](UserReference) | The user who canceled the scheduling run, if applicable | [optional] |
| **scheduling_completed_time** | datetime | When the scheduling run was completed, if applicable. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **message_count** | int | The number of schedule generation messages for this schedule generation run | [optional] |
| **message_severity_counts** | [list[SchedulerMessageSeverityCount]](SchedulerMessageSeverityCount) | The list of schedule generation message counts by severity for this schedule generation run | [optional] |
| **rescheduling_options** | [ReschedulingOptionsRunResponse](ReschedulingOptionsRunResponse) | Rescheduling options for this run.  Null unless intradayRescheduling is true | [optional] |
| **rescheduling_result_expiration** | datetime | When the reschedule result will expire.  Null unless intradayRescheduling is true. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 224.0.0_

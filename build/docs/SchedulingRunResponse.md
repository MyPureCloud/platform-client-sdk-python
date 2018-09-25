---
title: SchedulingRunResponse
---
## SchedulingRunResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **run_id** | **str** | ID of the schedule run | [optional] |
| **scheduler_run_id** | **str** | The runId from scheduler service.  Useful for debugging schedule errors | [optional] |
| **intraday_rescheduling** | **bool** | Whether this is the result of a rescheduling request | [optional] |
| **state** | **str** | Status of the schedule run | [optional] |
| **percent_complete** | **float** | Completion percentage of the schedule run | [optional] |
| **target_week** | **str** | The start date of the week for which the scheduling is done in yyyy-MM-dd format | [optional] |
| **schedule_id** | **str** | ID of the schedule. Does not apply to reschedule, see reschedulingOptions.existingScheduleId | [optional] |
| **schedule_description** | **str** | Description of the schedule | [optional] |
| **scheduling_start_time** | **datetime** | Start time of the schedule run. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **scheduling_started_by** | [**UserReference**](UserReference.html) | User that started the schedule run | [optional] |
| **scheduling_canceled_by** | [**UserReference**](UserReference.html) | User that canceled the schedule run | [optional] |
| **scheduling_completed_time** | **datetime** | Time at which the scheduling run was completed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **rescheduling_options** | [**ReschedulingOptionsResponse**](ReschedulingOptionsResponse.html) | The selected options for the reschedule request. Will always be null if intradayRescheduling is false | [optional] |
| **rescheduling_result_expiration** | **datetime** | When the rescheduling result data will expire. Results are kept temporarily as they should be applied as soon as possible after the run finishes.  Will always be null if intradayRescheduling is false. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **applied** | **bool** | Whether the rescheduling run has been marked applied | [optional] |
| **unscheduled_agents** | [**list[UnscheduledAgentWarning]**](UnscheduledAgentWarning.html) | Agents that were not scheduled in the rescheduling operation. Will always be null if intradayRescheduling is false | [optional] |
{: class="table table-striped"}



---
title: ImportWeekScheduleRequest
---
## ImportWeekScheduleRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **description** | **str** | Description for the schedule | |
| **user_schedules** | [**dict(str, UserSchedule)**](UserSchedule.html) | User schedules | [optional] |
| **published** | **bool** | Whether the schedule is published | [optional] |
| **short_term_forecast_id** | **str** | Short term forecast that should be associated with this schedule | [optional] |
| **partial_upload_ids** | **list[str]** | IDs of partial uploads of user schedules to import week schedule. It is applicable only for large schedules where activity count in schedule is greater than 17500 | [optional] |
{: class="table table-striped"}



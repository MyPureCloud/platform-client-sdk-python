---
title: UserScheduleShift
---
## UserScheduleShift

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **week_schedule** | [**WeekScheduleReference**](WeekScheduleReference.html) | The schedule to which this shift belongs | [optional] |
| **id** | **str** | ID of the schedule shift. This is only for the case of updating and deleting an existing shift | [optional] |
| **start_date** | **datetime** | Start time in UTC for this shift. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **length_in_minutes** | **int** | Length of this shift in minutes | [optional] |
| **activities** | [**list[UserScheduleActivity]**](UserScheduleActivity.html) | List of activities in this shift | [optional] |
| **delete** | **bool** | If marked true for updating this schedule shift, it will be deleted | [optional] |
| **manually_edited** | **bool** | Whether the shift was set as manually edited | [optional] |
{: class="table table-striped"}



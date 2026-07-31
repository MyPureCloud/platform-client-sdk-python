# ScheduleBidScheduledShift

## ScheduleBidScheduledShift

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **work_plan_shift_id** | str | The ID of the work plan shift that was used in schedule generation | [optional] |
| **work_plan_id** | str | The ID of the work plan from which the shift comes | [optional] |
| **start_date** | datetime | The start date of the scheduled shift. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **length_minutes** | int | The length of the shift in minutes | |
| **activities** | [list[ScheduleBidScheduledActivity]](ScheduleBidScheduledActivity) | The activities associated with this shift | |



_PureCloudPlatformClientV2 263.0.0_

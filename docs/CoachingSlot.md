# CoachingSlot

## CoachingSlot

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date_start** | datetime | Start date and time of scheduled coaching appointment slot. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **length_in_minutes** | int | Length of coaching appointment slot in minutes | [optional] |
| **staffing_difference** | float | Difference between scheduled and forecast headcount for this slot after scheduling the coaching appointment | [optional] |
| **difference_rating** | str | Rating based on the staffing difference for scheduled slot | [optional] |
| **wfm_schedule** | [WfmScheduleReference](WfmScheduleReference) | Workforce Management schedule information associated with the slot | [optional] |



_PureCloudPlatformClientV2 211.0.0_

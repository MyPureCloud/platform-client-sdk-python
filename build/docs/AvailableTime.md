# AvailableTime

## AvailableTime

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date_start** | datetime | Start of the availability period. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **length_in_minutes** | int | Length of availability period in minutes | [optional] |
| **is_paid** | bool | Indicates if this availability period is paid in Workforce Management schedule | [optional] |
| **activity_category** | str | Workforce Management activity category for this availability period | [optional] |
| **wfm_schedule** | [WfmScheduleReference](WfmScheduleReference) | Workforce Management schedule information associated with the available time | [optional] |



_PureCloudPlatformClientV2 211.1.0_

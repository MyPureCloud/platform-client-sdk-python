# BuTimeOffLimitRange

## BuTimeOffLimitRange

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | date | Start date of the range. The end date is determined by the size of &#39;limitMinutesPerDay&#39;. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **limit_minutes_per_day** | list[int] | The list of time-off limit values in minutes per day. If &#39;null&#39; is specified, then the day-specific value is cleared. Such a day will have a value of 0 | |



_PureCloudPlatformClientV2 222.0.0_

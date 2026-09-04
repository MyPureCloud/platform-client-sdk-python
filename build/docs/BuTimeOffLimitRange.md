# BuTimeOffLimitRange

## BuTimeOffLimitRange

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | date | Start date of the range. The end date is determined by the size of &#39;limitMinutesPerDay&#39;. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **limit_minutes_per_fifteen_minutes** | list[int] | The list of time-off limit values in minutes per fifteen minute interval. It must be set if &#39;granularity&#39; on time-off limit is fifteen minutes. If count of limit minutes array exceeds a day for given &#39;startDate&#39;, the slots overflowing into next day, should not be duplicated in another range entry with next day as &#39;startDate&#39;.For example startDate 03/01/2026 - limitMinutesPerFifteenMinutes with 120 intervals, 03/02/2026 - limitMinutesPerFifteenMinutes with 20 intervals has overlap and not allowed | [optional] |
| **limit_minutes_per_day** | list[int] | The list of time-off limit values in minutes per day. If &#39;null&#39; is specified, then the day-specific value is cleared. Such a day will have a value of 0 | [optional] |



_PureCloudPlatformClientV2 266.0.0_

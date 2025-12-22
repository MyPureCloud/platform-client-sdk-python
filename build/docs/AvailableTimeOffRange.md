# AvailableTimeOffRange

## AvailableTimeOffRange

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **time_off_limit** | [TimeOffLimitReference](TimeOffLimitReference) | The time off limit | [optional] |
| **start_date** | date | Start date of the requested date range. The end date is determined by the size of interval list. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **granularity** | str | Granularity choice for time off limit | [optional] |
| **available_minutes_per_interval** | list[int] | The list of available time off values in minutes per granularity interval | [optional] |
| **waitlisted_requests_per_interval** | list[int] | The current number of waitlisted time off requests for every interval per granularity | [optional] |
| **waitlist_enabled** | bool | Whether the time off request can be waitlisted | [optional] |



_PureCloudPlatformClientV2 246.1.0_

# DailyPossibleShift

## DailyPossibleShift

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **day_of_week** | str | Day of the shift | [optional] |
| **earliest_shift_start_minutes_from_midnight** | int | Minutes of the earliest shift start from midnight. Note that midnight is 12:00 am in the time zone specified in the timeZone field (in the top level of the response) | [optional] |
| **required** | bool | Whether this is a required shift | [optional] |
| **minimum_paid_time_minutes** | int | Minimum paid time in minutes of this daily shift | [optional] |
| **maximum_paid_time_minutes** | int | Maximum paid time in minutes of this daily shift | [optional] |
| **interval_schedule_probabilities** | list[int] | The percentage of being scheduled in each interval between the earliest shift start and latest shift end. Range of the values: [0, 100]. | [optional] |



_PureCloudPlatformClientV2 234.0.0_

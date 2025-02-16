# HistoricalAdherenceDayMetrics

## HistoricalAdherenceDayMetrics

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **day_start_offset_secs** | int | Start of day offset in seconds relative to query start time | [optional] |
| **adherence_schedule_secs** | int | Duration of schedule in seconds included for adherence percentage calculation | [optional] |
| **conformance_schedule_secs** | int | Total scheduled duration in seconds for OnQueue activities | [optional] |
| **conformance_actual_secs** | int | Total actually worked duration in seconds for OnQueue activities | [optional] |
| **exception_count** | int | Total number of adherence exceptions for this user | [optional] |
| **exception_duration_secs** | int | Total duration in seconds of adherence exceptions for this user | [optional] |
| **impact_seconds** | int | The impact duration in seconds of current adherence state for this user | [optional] |
| **schedule_length_secs** | int | Total duration in seconds for all scheduled activities | [optional] |
| **actual_length_secs** | int | Total duration in seconds for all actually worked activities | [optional] |
| **adherence_percentage** | float | Total adherence percentage for this user, in the scale of 0 - 100 | [optional] |
| **conformance_percentage** | float | Total conformance percentage for this user, in the scale of 0 - 100. Conformance percentage can be greater than 100 when the actual on queue time is greater than the scheduled on queue time for the same period. | [optional] |



_PureCloudPlatformClientV2 222.0.0_

# EstimateAvailableFullDayTimeOffResponse

## EstimateAvailableFullDayTimeOffResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date** | date | Date in yyyy-MM-dd format for full day request. Should be interpreted in the business unit&#39;s configured time zone. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **duration_minutes** | int | An estimation of time off request length in minutes | |
| **payable_minutes** | int | An estimation of payable part of time off request in minutes | |
| **flexible** | bool | Whether there is flexibility for a user to choose different hours than the system estimated | |
| **override_date_type** | str | The override date type, if the requested day is an override date | [optional] |
| **earliest_start_offset_minutes** | int | Earliest start time in minutes from midnight for full day request. Value may be null when time-off estimation is disabled | [optional] |
| **latest_end_offset_minutes** | int | Latest end time in minutes from midnight for full day request. Value may be null when time-off estimation is disabled | [optional] |



_PureCloudPlatformClientV2 263.0.0_

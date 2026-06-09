# EstimateAvailablePartialDayTimeOffResponse

## EstimateAvailablePartialDayTimeOffResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date** | datetime | Start date-time in ISO-8601 format for partial day request | |
| **duration_minutes** | int | An estimation of time off request length in minutes | |
| **payable_minutes** | int | An estimation of payable part of time off request in minutes | |
| **flexible** | bool | Whether there is flexibility for a user to choose different hours than the system estimated | |
| **override_date_type** | str | The override date type, if the partial day request overlaps with an override date | [optional] |



_PureCloudPlatformClientV2 259.0.0_

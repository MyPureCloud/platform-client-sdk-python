# EstimateAvailableFullDayTimeOffResponse

## EstimateAvailableFullDayTimeOffResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date** | date | Date in yyyy-MM-dd format for full day request. Should be interpreted in the business unit&#39;s configured time zone. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **duration_minutes** | int | An estimation of time off request length in minutes | |
| **payable_minutes** | int | An estimation of payable part of time off request in minutes | |
| **flexible** | bool | Whether there is flexibility for a user to choose different hours than the system estimated | |



_PureCloudPlatformClientV2 239.0.0_

# BuRescheduleAgentScheduleResult

## BuRescheduleAgentScheduleResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **management_unit** | [ManagementUnitReference](ManagementUnitReference) | The management unit to which this part of the result applies | [optional] |
| **download_result** | [MuRescheduleResultWrapper](MuRescheduleResultWrapper) | The agent schedules.  Result will always come via the downloadUrl; however the schema is included for documentation | [optional] |
| **download_url** | str | The download URL from which to fetch the result | [optional] |



_PureCloudPlatformClientV2 233.0.0_

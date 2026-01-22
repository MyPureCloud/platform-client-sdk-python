# UpdateUnavailableTime

## UpdateUnavailableTime

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the unavailable time span. Should be specified to update or delete an existing unavailable time span or set to null when creating a new one | [optional] |
| **time_span** | [UnavailableTimesTimeSpan](UnavailableTimesTimeSpan) | Exact date, time and length of the unavailability time in granularity of minutes. Must be specified when creating a new unavailable time span | [optional] |
| **notes** | str | Comments explaining the unavailability time span | [optional] |
| **delete** | bool | Whether the unavailable time should be deleted | [optional] |



_PureCloudPlatformClientV2 249.0.0_

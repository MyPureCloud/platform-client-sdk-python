# TimeOffLimitValueRange

## TimeOffLimitValueRange

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **time_off_limit** | [TimeOffLimitReference](TimeOffLimitReference) | The ID of the time off limit | [optional] |
| **start_date** | date | Start date of the requested date range, in ISO-8601 format. The end date is determined by the size of interval lists | |
| **granularity** | str | Granularity choice for time off limit | |
| **limit_minutes_per_interval** | list[int] | A list of time off limit values in minutes per granularity interval | [optional] |
| **allocated_minutes_per_interval** | list[int] | A list of allocated time off minutes per granularity interval | [optional] |
| **waitlisted_minutes_per_interval** | list[int] | A list of waitlisted time off minutes per granularity interval | [optional] |
| **waitlisted_requests_per_interval** | list[int] | The current number of waitlisted time off requests for every interval per granularity | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for the time off limit | [optional] |



_PureCloudPlatformClientV2 231.0.0_

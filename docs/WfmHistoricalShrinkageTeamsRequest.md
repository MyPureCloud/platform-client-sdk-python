# WfmHistoricalShrinkageTeamsRequest

## WfmHistoricalShrinkageTeamsRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | datetime | Beginning of the date range to query in ISO-8601 format | |
| **end_date** | datetime | End of the date range to query in ISO-8601 format. If it is not set, end date will be set to current time | [optional] |
| **time_zone** | str | The time zone, in olson format, to use in defining days when computing shrinkage for requested granularity. The results will be returned as UTC timestamps regardless of the time zone input. | |
| **granularity** | str | Shrinkage aggregation interval granularity | [optional] |



_PureCloudPlatformClientV2 246.1.0_

# BuIntradayResponse

## BuIntradayResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | datetime | The start of the date range for which this data applies.  This is also the start reference point for the intervals represented in the various arrays. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **end_date** | datetime | The end of the date range for which this data applies. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **interval_length_minutes** | int | The aggregation period in minutes, which determines the interval duration of the returned data | [optional] |
| **no_data_reason** | str | If not null, the reason there was no data for the request | [optional] |
| **categories** | list[str] | The categories to which this data corresponds | [optional] |
| **short_term_forecast** | [BuShortTermForecastReference](BuShortTermForecastReference) | Short term forecast reference | [optional] |
| **schedule** | [BuScheduleReference](BuScheduleReference) | Schedule reference | [optional] |
| **intraday_data_groupings** | [list[BuIntradayDataGroup]](BuIntradayDataGroup) | Intraday data grouped by a single media type and set of planning group IDs | [optional] |



_PureCloudPlatformClientV2 225.0.0_

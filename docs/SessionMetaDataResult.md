# SessionMetaDataResult

## SessionMetaDataResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **session_info** | [SessionInfo](SessionInfo) | Information about the continuous forecast session | [optional] |
| **snapshots** | [list[Snapshots]](Snapshots) | Captured snapshots | [optional] |
| **date_forecast_start** | datetime | Start date of the forecast. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_historical_start** | datetime | Start date of the oldest available historical week. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **aggregate_offered_historical_availability** | [AggregateHistoricalAvailability](AggregateHistoricalAvailability) | Total historical availability for offered metric across all planning groups | [optional] |
| **aggregate_average_handle_time_historical_availability** | [AggregateHistoricalAvailability](AggregateHistoricalAvailability) | Total historical availability for average handle time metric across all planning groups | [optional] |



_PureCloudPlatformClientV2 244.0.0_

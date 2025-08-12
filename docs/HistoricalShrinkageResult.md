# HistoricalShrinkageResult

## HistoricalShrinkageResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | datetime | Beginning of the date range that was queried, in ISO-8601 format | [optional] |
| **end_date** | datetime | End of the date range that was queried, in ISO-8601 format. If it was not set, end date will be set to the queried time | [optional] |
| **total_scheduled_duration_seconds** | int | Total duration in seconds for which agents in the management unit are scheduled | [optional] |
| **total_logged_in_duration_seconds** | int | Total duration in seconds for which agents in the management unit are actually logged-in | [optional] |
| **aggregated_shrinkage** | [HistoricalShrinkageAggregateResponse](HistoricalShrinkageAggregateResponse) | Aggregated shrinkage data for all the activity categories | [optional] |
| **shrinkage_for_activity_categories** | [list[HistoricalShrinkageActivityCategoryResponse]](HistoricalShrinkageActivityCategoryResponse) | Shrinkage for activity categories | [optional] |
| **business_unit_ids** | list[str] | List of all business units of all the agents in response | [optional] |



_PureCloudPlatformClientV2 235.0.0_

# WorkdayPointsTrend

## WorkdayPointsTrend

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date_start_workday** | date | The start workday for the query range for the gamification points trend. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_end_workday** | date | The end workday for the query range for the gamification points trend. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **user** | [UserReference](UserReference) | The targeted user for the query | [optional] |
| **day_of_week** | str | Aggregated for same day comparison | [optional] |
| **average_points** | float | The total average points | [optional] |
| **trend** | [list[WorkdayPointsTrendItem]](WorkdayPointsTrendItem) | Daily points trends | [optional] |



_PureCloudPlatformClientV2 221.0.0_

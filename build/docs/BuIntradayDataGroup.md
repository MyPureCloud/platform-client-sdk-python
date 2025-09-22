# BuIntradayDataGroup

## BuIntradayDataGroup

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **media_type** | str | The media type associated with this intraday group | [optional] |
| **forecast_data_summary** | [BuIntradayForecastData](BuIntradayForecastData) | Forecast data summary for this date range | [optional] |
| **forecast_data_per_interval** | [list[BuIntradayForecastData]](BuIntradayForecastData) | Forecast data per interval for this date range | [optional] |
| **schedule_data_summary** | [BuIntradayScheduleData](BuIntradayScheduleData) | Schedule data summary for this date range | [optional] |
| **schedule_data_per_interval** | [list[BuIntradayScheduleData]](BuIntradayScheduleData) | Schedule data per interval for this date range | [optional] |
| **performance_prediction_data_summary** | [IntradayPerformancePredictionData](IntradayPerformancePredictionData) | Performance prediction data summary for this date range | [optional] |
| **performance_prediction_data_per_interval** | [list[IntradayPerformancePredictionData]](IntradayPerformancePredictionData) | Performance prediction data per interval for this date range | [optional] |



_PureCloudPlatformClientV2 237.0.0_

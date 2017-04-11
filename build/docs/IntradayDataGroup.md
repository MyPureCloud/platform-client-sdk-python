---
title: IntradayDataGroup
---
## IntradayDataGroup

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **media_type** | **str** | The media type associated with this intraday group | [optional] |
| **forecast_data_per_interval** | [**list[IntradayForecastData]**](IntradayForecastData.html) | Forecast data for this date range | [optional] |
| **schedule_data_per_interval** | [**list[IntradayScheduleData]**](IntradayScheduleData.html) | Schedule data for this date range | [optional] |
| **historical_agent_data_per_interval** | [**list[IntradayHistoricalAgentData]**](IntradayHistoricalAgentData.html) | Historical agent data for this date range | [optional] |
| **historical_queue_data_per_interval** | [**list[IntradayHistoricalQueueData]**](IntradayHistoricalQueueData.html) | Historical queue data for this date range | [optional] |
| **performance_prediction_agent_data_per_interval** | [**list[IntradayPerformancePredictionAgentData]**](IntradayPerformancePredictionAgentData.html) | Performance prediction data for this date range | [optional] |
| **performance_prediction_queue_data_per_interval** | [**list[IntradayPerformancePredictionQueueData]**](IntradayPerformancePredictionQueueData.html) | Performance prediction data for this date range | [optional] |
{: class="table table-striped"}



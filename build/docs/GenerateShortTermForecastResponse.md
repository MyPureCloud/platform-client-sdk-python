---
title: GenerateShortTermForecastResponse
---
## GenerateShortTermForecastResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **status** | **str** | The status of the request | [optional] |
| **result** | [**ShortTermForecast**](ShortTermForecast.html) | The resulting forecast.  May be sent asynchronously via notification depending on the complexity of the forecast | [optional] |
| **operation_id** | **str** | The operation id to watch for on the notification topic | [optional] |
| **progress** | **int** | Percent progress.  Subscribe to the corresponding notification to view progress and await the result | [optional] |
{: class="table table-striped"}



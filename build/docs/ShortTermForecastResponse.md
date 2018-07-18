---
title: ShortTermForecastResponse
---
## ShortTermForecastResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **status** | **str** | The status of the request | [optional] |
| **result** | [**ShortTermForecast**](ShortTermForecast.html) | The resulting forecast.  May be sent asynchronously via notification depending on the complexity of the forecast | [optional] |
| **operation_id** | **str** | The operation id to watch for on the notification topic | [optional] |
{: class="table table-striped"}



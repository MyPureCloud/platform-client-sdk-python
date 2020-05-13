---
title: AsyncForecastOperationResult
---
## AsyncForecastOperationResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **status** | **str** | The status of the operation | [optional] |
| **operation_id** | **str** | The ID for the operation | [optional] |
| **result** | [**BuShortTermForecast**](BuShortTermForecast.html) | The result of the operation.  Null unless status == Complete | [optional] |
| **progress** | **int** | Percent progress for the operation | [optional] |
{: class="table table-striped"}



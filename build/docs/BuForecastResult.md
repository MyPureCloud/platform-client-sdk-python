---
title: BuForecastResult
---
## BuForecastResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **reference_start_date** | **datetime** | The reference start date for interval-based data for this forecast. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **planning_groups** | [**list[ForecastPlanningGroupData]**](ForecastPlanningGroupData.html) | The forecast data broken up by planning group | [optional] |
| **week_number** | **int** | The week number represented by this response | [optional] |
| **week_count** | **int** | The number of weeks in this forecast | [optional] |
{: class="table table-striped"}



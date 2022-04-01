---
title: ImportScheduleUploadSchema
---
## ImportScheduleUploadSchema

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **description** | **str** | The description for the imported schedule | |
| **week_count** | **int** | The number of weeks the imported schedule will cover | |
| **published** | **bool** | Whether the imported schedule should be immediately published | [optional] |
| **short_term_forecast** | [**BuShortTermForecastReference**](BuShortTermForecastReference.html) | The short term forecast to associate with the imported schedule | [optional] |
| **headcount_forecast** | [**BuHeadcountForecast**](BuHeadcountForecast.html) | The headcount forecast to associate with the imported schedule | [optional] |
| **agent_schedules** | [**list[BuImportAgentScheduleUploadSchema]**](BuImportAgentScheduleUploadSchema.html) | Individual agent schedules | [optional] |
{: class="table table-striped"}



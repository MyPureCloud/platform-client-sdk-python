# ImportScheduleUploadSchema

## ImportScheduleUploadSchema

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **description** | str | The description for the imported schedule | |
| **week_count** | int | The number of weeks the imported schedule will cover | |
| **published** | bool | Whether the imported schedule should be immediately published | [optional] |
| **short_term_forecast** | [BuShortTermForecastReference](BuShortTermForecastReference) | The short term forecast to associate with the imported schedule | [optional] |
| **headcount_forecast** | [BuHeadcountForecast](BuHeadcountForecast) | The headcount forecast to associate with the imported schedule | [optional] |
| **agent_schedules** | [list[BuImportAgentScheduleUploadSchema]](BuImportAgentScheduleUploadSchema) | Individual agent schedules | [optional] |



_PureCloudPlatformClientV2 223.0.0_

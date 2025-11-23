# BuRescheduleResult

## BuRescheduleResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **generation_results** | [ScheduleGenerationResult](ScheduleGenerationResult) | The generation results.  Note the result will always be delivered via the generationResultsDownloadUrl; however the schema is included for documentation | [optional] |
| **generation_results_download_url** | str | The download URL from which to fetch the generation results for the rescheduling run | [optional] |
| **headcount_forecast** | [BuHeadcountForecastBuPlanningGroupHeadcountForecastResult](BuHeadcountForecastBuPlanningGroupHeadcountForecastResult) | The headcount forecast. Note the result will always be delivered via the headcountForecastDownloadUrl; however the schema is included for documentation | [optional] |
| **headcount_forecast_download_url** | str | The download URL from which to fetch the headcount forecast for the rescheduling run | [optional] |
| **agent_schedules** | [list[BuRescheduleAgentScheduleResult]](BuRescheduleAgentScheduleResult) | List of download links for agent schedules produced by the rescheduling run | [optional] |



_PureCloudPlatformClientV2 244.0.0_

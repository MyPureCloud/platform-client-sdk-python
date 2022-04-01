---
title: UpdateScheduleUploadSchema
---
## UpdateScheduleUploadSchema

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **description** | **str** | The description to set for the schedule | [optional] |
| **published** | **bool** | Whether to publish the schedule. Note: a schedule cannot be un-published unless another schedule is published over it | [optional] |
| **short_term_forecast** | [**BuShortTermForecastReference**](BuShortTermForecastReference.html) | The short term forecast to associate with the schedule | [optional] |
| **headcount_forecast** | [**BuHeadcountForecast**](BuHeadcountForecast.html) | The headcount forecast to associate with the schedule | [optional] |
| **agent_schedules** | [**list[BuUpdateAgentScheduleUploadSchema]**](BuUpdateAgentScheduleUploadSchema.html) | Individual agent schedules | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Version metadata for this schedule | |
{: class="table table-striped"}



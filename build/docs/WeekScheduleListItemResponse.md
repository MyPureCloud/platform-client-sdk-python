---
title: WeekScheduleListItemResponse
---
## WeekScheduleListItemResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **week_date** | **str** | First day of this week schedule in week in yyyy-MM-dd format | [optional] |
| **description** | **str** | Description of the week schedule | [optional] |
| **published** | **bool** | Whether the week schedule is published | [optional] |
| **generation_results** | [**WeekScheduleGenerationResult**](WeekScheduleGenerationResult.html) | Summary of the results from the schedule run | [optional] |
| **short_term_forecast** | [**ShortTermForecastReference**](ShortTermForecastReference.html) | Short term forecast associated with this schedule | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Version metadata for this work plan | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



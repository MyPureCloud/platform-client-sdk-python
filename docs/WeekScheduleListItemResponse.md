# WeekScheduleListItemResponse

## WeekScheduleListItemResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **week_date** | str | First day of this week schedule in yyyy-MM-dd format | [optional] |
| **description** | str | Description of the week schedule | [optional] |
| **published** | bool | Whether the week schedule is published | [optional] |
| **generation_results** | [WeekScheduleGenerationResult](WeekScheduleGenerationResult) | Summary of the results from the schedule run | [optional] |
| **short_term_forecast** | [ShortTermForecastReference](ShortTermForecastReference) | Short term forecast associated with this schedule | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for this work plan | [optional] |



_PureCloudPlatformClientV2 240.0.0_

# BuScheduleListItem

## BuScheduleListItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **week_date** | date | The start week date for this schedule. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **week_count** | int | The number of weeks spanned by this schedule | [optional] |
| **description** | str | The description of this schedule | [optional] |
| **published** | bool | Whether this schedule is published | [optional] |
| **short_term_forecast** | [BuShortTermForecastReference](BuShortTermForecastReference) | The forecast used for this schedule, if applicable | [optional] |
| **generation_results** | [ScheduleGenerationResultSummary](ScheduleGenerationResultSummary) | Generation result summary for this schedule, if applicable | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for this schedule | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 217.0.0_
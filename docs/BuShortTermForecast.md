# BuShortTermForecast

## BuShortTermForecast

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **week_date** | date | The start week date of this forecast in yyyy-MM-dd.  Must fall on the start day of week for the associated business unit. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **week_count** | int | The number of weeks this forecast covers | [optional] |
| **creation_method** | str | The method by which this forecast was created | [optional] |
| **description** | str | The description of this forecast | [optional] |
| **legacy** | bool | Whether this forecast contains modifications on legacy metrics | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Metadata for this forecast | [optional] |
| **can_use_for_scheduling** | bool | Whether this forecast can be used for scheduling | [optional] |
| **reference_start_date** | datetime | The reference start date for interval-based data for this forecast. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **source_days** | [list[ForecastSourceDayPointer]](ForecastSourceDayPointer) | The source day pointers for this forecast | [optional] |
| **modifications** | [list[BuForecastModificationResponse]](BuForecastModificationResponse) | Any manual modifications applied to this forecast | [optional] |
| **generation_results** | [BuForecastGenerationResult](BuForecastGenerationResult) | Generation result metadata | [optional] |
| **time_zone** | str | The time zone for this forecast | [optional] |
| **planning_groups_version** | int | The version of the planning groups that was used for this forecast | [optional] |
| **planning_groups** | [ForecastPlanningGroupsResponse](ForecastPlanningGroupsResponse) | A snapshot of the planning groups used for this forecast as of the version number indicated | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 227.1.0_

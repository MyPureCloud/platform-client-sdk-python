# BuForecastModificationResponse

## BuForecastModificationResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | str | The type of the modification | |
| **start_interval_index** | int | The number of intervals past referenceStartDate representing the first interval to which this modification applies | [optional] |
| **end_interval_index** | int | The number of intervals past referenceStartDate representing the last interval to which this modification applies | [optional] |
| **metric** | str | The metric to which this modification applies | |
| **legacy_metric** | str | The legacy metric to which this modification applies if applicable | [optional] |
| **value** | float | The value of the modification | [optional] |
| **values** | [list[WfmForecastModificationIntervalOffsetValue]](WfmForecastModificationIntervalOffsetValue) | The list of modification values. Only applicable for grid-type modifications | |
| **secondary_values** | [list[WfmForecastModificationIntervalOffsetValue]](WfmForecastModificationIntervalOffsetValue) | The list of modification secondary values. Only applicable for multi granularity modifications | [optional] |
| **display_granularity** | str | The client side display granularity of the modification, expressed in the ISO-8601 duration format. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H | |
| **granularity** | str | The actual granularity of the modification as stored behind the scenes, expressed in the ISO-8601 duration format. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H | |
| **secondary_granularity** | str | The granularity of the &#39;secondaryValues&#39; modification as stored behind the scenes, expressed in the ISO-8601 duration format. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H | [optional] |
| **enabled** | bool | Whether the modification is enabled for the forecast | |
| **planning_group_ids** | list[str] | The IDs of the planning groups to which this forecast modification applies | |



_PureCloudPlatformClientV2 229.0.0_

---
title: BuForecastModification
---
## BuForecastModification

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | **str** | The type of the modification | |
| **start_interval_index** | **int** | The number of 15 minute intervals past referenceStartDate representing the first interval to which to apply this modification. Must be null if values is populated | [optional] |
| **end_interval_index** | **int** | The number of 15 minute intervals past referenceStartDate representing the last interval to which to apply this modification.  Must be null if values is populated | [optional] |
| **metric** | **str** | The metric to which this modification applies | |
| **legacy_metric** | **str** | The legacy metric to which this modification applies if applicable | [optional] |
| **value** | **float** | The value of the modification.  Must be null if \&quot;values\&quot; is populated | [optional] |
| **values** | [**list[WfmForecastModificationIntervalOffsetValue]**](WfmForecastModificationIntervalOffsetValue.html) | The list of values to update.  Only applicable for grid-type modifications. Must be null if \&quot;value\&quot; is populated | [optional] |
| **display_granularity** | **str** | The client side display granularity of the modification, expressed in the ISO-8601 duration format. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H | |
| **granularity** | **str** | The actual granularity of the modification as stored behind the scenes, expressed in the ISO-8601 duration format. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H | [optional] |
| **enabled** | **bool** | Whether the modification is enabled for the forecast | |
| **planning_group_ids** | **list[str]** | The IDs of the planning groups to which this forecast modification applies.  Leave empty to apply to all | [optional] |
{: class="table table-striped"}



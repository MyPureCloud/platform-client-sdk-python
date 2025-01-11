# FlowActivityData

## FlowActivityData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **group** | dict(str, str) | A mapping from grouping dimension to value | [optional] |
| **data** | [list[FlowActivityMetricValue]](FlowActivityMetricValue) | Data for metrics | [optional] |
| **truncated** | bool | Flag for a truncated list of entities. If truncated, the first half of the list of entities will contain the oldest entities and the second half the newest entities. | [optional] |
| **entities** | [list[FlowActivityEntityData]](FlowActivityEntityData) | Details for active entities | [optional] |



_PureCloudPlatformClientV2 219.1.0_

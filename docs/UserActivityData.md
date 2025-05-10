# UserActivityData

## UserActivityData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **group** | dict(str, str) | A mapping from grouping dimension to value | [optional] |
| **data** | [list[UserActivityMetricValue]](UserActivityMetricValue) | Data for metrics | [optional] |
| **truncated** | bool | Flag for a truncated list of entities. If truncated, the first half of the list of entities will contain the oldest entities and the second half the newest entities. | [optional] |
| **entities** | [list[UserActivityEntityData]](UserActivityEntityData) | Details for active entities | [optional] |



_PureCloudPlatformClientV2 228.0.0_

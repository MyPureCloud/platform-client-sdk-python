# ConversationActivityData

## ConversationActivityData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **group** | dict(str, str) | A mapping from grouping dimension to value | [optional] |
| **data** | [list[ConversationActivityMetricValue]](ConversationActivityMetricValue) | Data for metrics | [optional] |
| **truncated** | bool | Flag for a truncated list of entities. If truncated, the first half of the list of entities will contain the oldest entities and the second half the newest entities. | [optional] |
| **entities** | [list[ConversationActivityEntityData]](ConversationActivityEntityData) | Details for active entities | [optional] |



_PureCloudPlatformClientV2 240.0.0_

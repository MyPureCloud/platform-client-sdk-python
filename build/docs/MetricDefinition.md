# MetricDefinition

## MetricDefinition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **unit_type** | str | The type of associated metric unit | [optional] |
| **short_name** | str | An alternate name for this metric definition, often abbreviation | [optional] |
| **dividend_metrics** | list[str] | Metric names used as dividend | [optional] |
| **divisor_metrics** | list[str] | Metric names used as divisor | [optional] |
| **default_objective** | [DefaultObjective](DefaultObjective) | A predefined default objective for this metric | [optional] |
| **lock_template_id** | str | An optional field to specify if this metric definition is locked to certain template. e.g. punctuality | [optional] |
| **media_type_filtering_allowed** | bool | Flag to indicate if this metricDefinition allows filter based on media types | [optional] |
| **initial_direction_filtering_allowed** | bool | Flag to indicate if this metricDefinition allows filter based on initial direction | [optional] |
| **queue_filtering_allowed** | bool | Flag to indicate if this metricDefinition allows filter based on queues | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 248.0.0_

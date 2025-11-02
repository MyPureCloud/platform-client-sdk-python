# CreateMetric

## CreateMetric

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **metric_definition_id** | str | The id of associated metric definition | [optional] |
| **external_metric_definition_id** | str | The id of associated external metric definition | [optional] |
| **objective** | [CreateObjective](CreateObjective) | Associated objective for this metric | [optional] |
| **performance_profile_id** | str | Performance profile id of this metric | [optional] |
| **name** | str | The name of this metric | |
| **precision** | int | The precision of the metric, must be between 0 and 5 | [optional] |
| **time_display_unit** | str | The time unit in which the metric should be displayed -- this parameter is ignored when displaying non-time values | [optional] |



_PureCloudPlatformClientV2 242.0.0_

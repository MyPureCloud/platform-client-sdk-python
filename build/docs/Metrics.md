# Metrics

## Metrics

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **order** | int | The order of metric within a performance profile | [optional] |
| **metric_definition_name** | str | The name of associated metric definition | [optional] |
| **metric_definition_id** | str | The id of associated metric definition | [optional] |
| **external_metric_definition_id** | str | The id of associated external metric definition | [optional] |
| **unit_type** | str | Corresponding unit type for this metric | [optional] |
| **enabled** | bool | A flag for whether this metric is enabled for a performance profile | [optional] |
| **template_name** | str | The name of associated objective template | [optional] |
| **max_points** | int | Achievable maximum points for this metric | [optional] |
| **performance_profile_id** | str | Performance profile id of this metric | [optional] |
| **linked_metric** | [AddressableEntityRef](AddressableEntityRef) | The linked metric entity reference | [optional] |
| **date_created** | datetime | The created date of this metric. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_unlinked** | date | The unlinked workday for this metric if this metric was ever unlinked. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **source_performance_profile** | [PerformanceProfile](PerformanceProfile) | The source performance profile when this metric is linked | [optional] |
| **unit_definition** | str | Unit definition of linked external metric | [optional] |
| **precision** | int | Precision of linked external metric | [optional] |
| **time_display_unit** | str | The time unit in which the metric should be displayed -- this parameter is ignored when displaying non-time values | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 230.0.0_

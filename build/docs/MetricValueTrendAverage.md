# MetricValueTrendAverage

## MetricValueTrendAverage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date_start_workday** | date | The targeted start workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_end_workday** | date | The targeted end workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_reference_workday** | date | The targeted reference workday. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **division** | [Division](Division) | The targeted division for the metrics | [optional] |
| **user** | [UserReference](UserReference) | The targeted user for the metrics | [optional] |
| **timezone** | str | The time zone used for aggregating metric values | [optional] |
| **result** | [WorkdayValuesMetricItem](WorkdayValuesMetricItem) | The metric value trend and average | [optional] |
| **performance_profile** | [AddressableEntityRef](AddressableEntityRef) | The targeted performance profile for the average points | [optional] |
| **metric** | [AddressableEntityRef](AddressableEntityRef) | The targeted performance profile for the average points | [optional] |



_PureCloudPlatformClientV2 239.0.0_

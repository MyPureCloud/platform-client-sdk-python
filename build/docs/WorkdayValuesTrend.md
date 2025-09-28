# WorkdayValuesTrend

## WorkdayValuesTrend

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date_start_workday** | date | The start workday for the query range for the metric value trend. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_end_workday** | date | The end workday for the query range for the metric value trend. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_reference_workday** | date | The reference workday used to determine the metric definition. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **division** | [Division](Division) | The targeted division for the query | [optional] |
| **user** | [UserReference](UserReference) | The targeted user for the query | [optional] |
| **timezone** | str | The time zone used for aggregating metric values | [optional] |
| **results** | [list[WorkdayValuesMetricItem]](WorkdayValuesMetricItem) | The metric value trends | [optional] |
| **performance_profile** | [AddressableEntityRef](AddressableEntityRef) | The targeted performance profile for the average points | [optional] |
| **metric** | [AddressableEntityRef](AddressableEntityRef) | The targeted metric for the average points | [optional] |



_PureCloudPlatformClientV2 238.0.0_

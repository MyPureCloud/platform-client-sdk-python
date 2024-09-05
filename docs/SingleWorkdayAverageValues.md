# SingleWorkdayAverageValues

## SingleWorkdayAverageValues

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date_workday** | date | The targeted workday for average value query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **division** | [Division](Division) | The targeted division for the metrics | [optional] |
| **user** | [UserReference](UserReference) | The targeted user for the metrics | [optional] |
| **timezone** | str | The time zone used for aggregating metric values | [optional] |
| **results** | [list[WorkdayValuesMetricItem]](WorkdayValuesMetricItem) | The metric value averages | [optional] |
| **performance_profile** | [AddressableEntityRef](AddressableEntityRef) | The targeted performance profile for the average points | [optional] |



_PureCloudPlatformClientV2 210.0.0_

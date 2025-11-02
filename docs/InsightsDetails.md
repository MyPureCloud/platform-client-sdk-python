# InsightsDetails

## InsightsDetails

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **performance_profile** | [AddressableEntityRef](AddressableEntityRef) | The performance profile | [optional] |
| **division** | [DivisionReference](DivisionReference) | The division | [optional] |
| **granularity** | str | Granularity | [optional] |
| **comparative_period** | [WorkdayPeriod](WorkdayPeriod) | The comparative period work day date range | [optional] |
| **primary_period** | [WorkdayPeriod](WorkdayPeriod) | The primary period work day date range | [optional] |
| **user** | [UserReference](UserReference) | The query user | [optional] |
| **metric_data** | [list[InsightsDetailsMetricItem]](InsightsDetailsMetricItem) | The list of insights data for each metric of the user | [optional] |
| **overall_data** | [InsightsDetailsOverallItem](InsightsDetailsOverallItem) | Overall insights data of the user | [optional] |



_PureCloudPlatformClientV2 242.0.0_

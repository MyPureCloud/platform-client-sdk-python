# UserInsightsTrend

## UserInsightsTrend

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **performance_profile** | [AddressableEntityRef](AddressableEntityRef) | The performance profile | [optional] |
| **division** | [DivisionReference](DivisionReference) | The division | [optional] |
| **granularity** | str | Granularity | [optional] |
| **comparative_period** | [WorkdayPeriod](WorkdayPeriod) | The comparative period work day date range | [optional] |
| **primary_period** | [WorkdayPeriod](WorkdayPeriod) | The primary period work day date range | [optional] |
| **user** | [UserReference](UserReference) | The query user | [optional] |
| **entities** | [list[UserInsightsTrendMetricItem]](UserInsightsTrendMetricItem) | The list of insights trend for each metric | [optional] |
| **total** | [UserInsightsTrendTotalItem](UserInsightsTrendTotalItem) | The insights trend in total | [optional] |



_PureCloudPlatformClientV2 215.0.0_

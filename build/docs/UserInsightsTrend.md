---
title: UserInsightsTrend
---
## UserInsightsTrend

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **performance_profile** | [**AddressableEntityRef**](AddressableEntityRef.html) | The performance profile | [optional] |
| **division** | [**DivisionReference**](DivisionReference.html) | The division | [optional] |
| **granularity** | **str** | Granularity | [optional] |
| **comparative_period** | [**WorkdayPeriod**](WorkdayPeriod.html) | The comparative period work day date range | [optional] |
| **primary_period** | [**WorkdayPeriod**](WorkdayPeriod.html) | The primary period work day date range | [optional] |
| **user** | [**UserReference**](UserReference.html) | The query user | [optional] |
| **entities** | [**list[UserInsightsTrendMetricItem]**](UserInsightsTrendMetricItem.html) | The list of insights trend for each metric | [optional] |
| **total** | [**UserInsightsTrendTotalItem**](UserInsightsTrendTotalItem.html) | The insights trend in total | [optional] |
{: class="table table-striped"}



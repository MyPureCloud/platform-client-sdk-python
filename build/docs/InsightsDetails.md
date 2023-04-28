---
title: InsightsDetails
---
## InsightsDetails

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **performance_profile** | [**AddressableEntityRef**](AddressableEntityRef.html) | The performance profile | [optional] |
| **division** | [**DivisionReference**](DivisionReference.html) | The division | [optional] |
| **granularity** | **str** | Granularity | [optional] |
| **comparative_period** | [**WorkdayPeriod**](WorkdayPeriod.html) | The comparative period work day date range | [optional] |
| **primary_period** | [**WorkdayPeriod**](WorkdayPeriod.html) | The primary period work day date range | [optional] |
| **user** | [**UserReference**](UserReference.html) | The query user | [optional] |
| **metric_data** | [**list[InsightsDetailsMetricItem]**](InsightsDetailsMetricItem.html) | The list of insights data for each metric of the user | [optional] |
| **overall_data** | [**InsightsDetailsOverallItem**](InsightsDetailsOverallItem.html) | Overall insights data of the user | [optional] |
{: class="table table-striped"}



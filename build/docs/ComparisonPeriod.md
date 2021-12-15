---
title: ComparisonPeriod
---
## ComparisonPeriod

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **kpi** | **str** | Key Performance Indicator optimised during the comparison period. | [optional] |
| **date_started** | **datetime** | Start date of the comparison period. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_ended** | **datetime** | End date of the comparison period. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **kpi_total_on** | **int** | Absolute metric (in which the KPI is based) total for the interactions handled by predictive routing (GPR was on) | [optional] |
| **kpi_total_off** | **int** | Absolute metric (in which the KPI is based) total for the interactions not routed by predictive routing (GPR was off) | [optional] |
| **interaction_count_on** | **int** | Total interactions handled by predictive routing (GPR was on) | [optional] |
| **interaction_count_off** | **int** | Total interactions not routed by predictive routing (GPR was off) | [optional] |
| **kpi_results** | [**list[KpiResult]**](KpiResult.html) | KPI results for each metric | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



---
title: FlowObservationQuery
---
## FlowObservationQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **filter** | [**FlowObservationQueryFilter**](FlowObservationQueryFilter.html) | Filter to return a subset of observations. Expresses boolean logical predicates as well as dimensional filters | |
| **metrics** | **list[str]** | Behaves like a SQL SELECT clause. Only named metrics will be retrieved. | |
| **detail_metrics** | **list[str]** | Metrics for which to include additional detailed observations | [optional] |
{: class="table table-striped"}



---
title: Metric
---
## Metric

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of this metric | |
| **metric_definition_id** | **str** | The id of associated metric definition | [optional] |
| **external_metric_definition_id** | **str** | The id of associated external metric definition | [optional] |
| **objective** | [**Objective**](Objective.html) | Associated objective for this metric | [optional] |
| **performance_profile_id** | **str** | Performance profile id of this metric | [optional] |
| **linked_metric** | [**AddressableEntityRef**](AddressableEntityRef.html) | The linked metric entity reference | [optional] |
| **date_created** | **int** | The created date of this metric | [optional] |
| **date_unlinked** | **date** | The unlinked workday for this metric if this metric was ever unlinked. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **source_performance_profile** | [**PerformanceProfile**](PerformanceProfile.html) | The source performance profile when this metric is linked | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



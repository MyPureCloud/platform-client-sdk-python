---
title: RoutingActivityData
---
## RoutingActivityData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **group** | **dict(str, str)** | A mapping from grouping dimension to value | [optional] |
| **data** | [**list[RoutingActivityMetricValue]**](RoutingActivityMetricValue.html) | Data for metrics | [optional] |
| **truncated** | **bool** | Flag for a truncated list of entities. If truncated, the first half of the list of entities will contain the oldest entities and the second half the newest entities. | [optional] |
| **entities** | [**list[RoutingActivityEntityData]**](RoutingActivityEntityData.html) | Details for active entities | [optional] |
{: class="table table-striped"}



---
title: TeamActivityData
---
## TeamActivityData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **group** | **dict(str, str)** | A mapping from grouping dimension to value | [optional] |
| **data** | [**list[TeamActivityMetricValue]**](TeamActivityMetricValue.html) | Data for metrics | [optional] |
| **truncated** | **bool** | Flag for a truncated list of entities. If truncated, the first half of the list of entities will contain the oldest entities and the second half the newest entities. | [optional] |
| **entities** | [**list[TeamActivityEntityData]**](TeamActivityEntityData.html) | Details for active entities | [optional] |
{: class="table table-striped"}



---
title: DocumentationV2SearchRequest
---
## DocumentationV2SearchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **sort_order** | **str** | The sort order for results | [optional] |
| **sort_by** | **str** | The field in the resource that you want to sort the results by | [optional] |
| **page_size** | **int** | The number of results per page | [optional] |
| **page_number** | **int** | The page of resources you want to retrieve | [optional] |
| **sort** | [**list[SearchSort]**](SearchSort.html) | Multi-value sort order, list of multiple sort values | [optional] |
| **types** | **list[str]** | Resource domain type to search | |
| **query** | [**list[DocumentationV2SearchCriteria]**](DocumentationV2SearchCriteria.html) | The search criteria | [optional] |
| **aggregations** | [**list[DocumentationV2SearchAggregation]**](DocumentationV2SearchAggregation.html) | Aggregation criteria | [optional] |
{: class="table table-striped"}



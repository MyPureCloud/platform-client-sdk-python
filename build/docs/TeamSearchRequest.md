---
title: TeamSearchRequest
---
## TeamSearchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **sort_order** | **str** | The sort order for results | [optional] |
| **sort_by** | **str** | The field in the resource that you want to sort the results by | [optional] |
| **page_size** | **int** | The number of results per page | [optional] |
| **page_number** | **int** | The page of resources you want to retrieve | [optional] |
| **sort** | [**list[SearchSort]**](SearchSort.html) | Multi-value sort order, list of multiple sort values | [optional] |
| **query** | [**list[TeamSearchCriteria]**](TeamSearchCriteria.html) | Team Search Criteria | |
{: class="table table-striped"}



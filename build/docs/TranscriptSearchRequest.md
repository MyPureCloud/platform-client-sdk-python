---
title: TranscriptSearchRequest
---
## TranscriptSearchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **sort_order** | **str** | The sort order for results | [optional] |
| **sort_by** | **str** | The field in the resource that you want to sort the results by | [optional] |
| **page_size** | **int** | The number of results per page | [optional] |
| **page_number** | **int** | The page of resources you want to retrieve | [optional] |
| **sort** | [**list[SearchSort]**](SearchSort.html) | Multi-value sort order, list of multiple sort values | [optional] |
| **return_fields** | **list[str]** |  | [optional] |
| **types** | **list[str]** | Resource domain type to search | |
| **query** | [**list[TranscriptSearchCriteria]**](TranscriptSearchCriteria.html) | The search criteria | [optional] |
{: class="table table-striped"}



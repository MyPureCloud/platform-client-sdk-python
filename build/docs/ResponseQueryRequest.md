---
title: ResponseQueryRequest
---
## ResponseQueryRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **query_phrase** | **str** | Query phrase to search response text and name. If not set will match all. | [optional] |
| **page_size** | **int** | The maximum number of hits to return. Default: 25, Maximum: 500. | [optional] |
| **page_number** | **int** | Page Number | [optional] |
| **filters** | [**list[ResponseFilter]**](ResponseFilter.html) | Filter the query results. | [optional] |
{: class="table table-striped"}



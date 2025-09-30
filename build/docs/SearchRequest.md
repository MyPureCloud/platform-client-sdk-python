# SearchRequest

## SearchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **sort_order** | str | The sort order for results | [optional] |
| **sort_by** | str | The field in the resource that you want to sort the results by | [optional] |
| **page_size** | int | The number of results per page | [optional] |
| **page_number** | int | The page of resources you want to retrieve | [optional] |
| **sort** | [list[SearchSort]](SearchSort) | Multi-value sort order, list of multiple sort values | [optional] |
| **return_fields** | list[str] | A List of strings.  Possible values are any field in the resource you are searching on.  The other option is to use ALL_FIELDS, when this is provided all fields in the resource will be returned in the search results. | [optional] |
| **expand** | list[str] | Provides more details about a specified resource | [optional] |
| **types** | list[str] | Resource domain type to search | |
| **query** | [list[SearchCriteria]](SearchCriteria) | The search criteria | [optional] |
| **aggregations** | [list[SearchAggregation]](SearchAggregation) | Aggregation criteria | [optional] |



_PureCloudPlatformClientV2 239.0.0_

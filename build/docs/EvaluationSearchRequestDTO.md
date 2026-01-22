# EvaluationSearchRequestDTO

## EvaluationSearchRequestDTO

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **query** | [list[EvaluationSearchCriteriaDTO]](EvaluationSearchCriteriaDTO) |  | |
| **aggregations** | [list[EvaluationSearchAggregationDTO]](EvaluationSearchAggregationDTO) | Aggregations to compute on the search results | [optional] |
| **page_size** | int | The number of results per page. For aggregation requests, must be omitted or 0. | [optional] |
| **page_number** | int | The page of resources you want to retrieve | |
| **sort_order** | str | The sort order for results. Include with sortBy. | [optional] |
| **sort_by** | str | The field in the resource that you want to sort the results by. Include with sortOrder. | [optional] |
| **system_submitted** | bool | Filter for automated evaluations submitted by virtual supervisor. Defaults to false. | [optional] |



_PureCloudPlatformClientV2 249.0.0_

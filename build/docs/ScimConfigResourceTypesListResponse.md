# ScimConfigResourceTypesListResponse

## ScimConfigResourceTypesListResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **schemas** | list[str] | The list of supported schemas. | [optional] |
| **total_results** | int | The total number of results. | [optional] |
| **start_index** | int | The 1-based index of the first result returned by this request. Add this to \&quot;itemsPerPage\&quot; when requesting the next page of results. | [optional] |
| **items_per_page** | int | The number of resources returned per page. | [optional] |
| **resources** | [list[ScimConfigResourceType]](ScimConfigResourceType) | The list of requested resources. | [optional] |



_PureCloudPlatformClientV2 233.0.0_

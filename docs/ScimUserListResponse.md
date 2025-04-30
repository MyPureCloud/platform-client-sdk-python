# ScimUserListResponse

## ScimUserListResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **schemas** | list[str] | The list of supported schemas. | [optional] |
| **total_results** | int | The total number of results. | [optional] |
| **start_index** | int | The 1-based index of the first result returned by this request. Add this to \&quot;itemsPerPage\&quot; when requesting the next page of results. | [optional] |
| **items_per_page** | int | The number of resources returned per page. | [optional] |
| **resources** | [list[ScimV2User]](ScimV2User) | The list of requested resources. If \&quot;count\&quot; is 0, then the list will be empty. | [optional] |



_PureCloudPlatformClientV2 227.0.0_

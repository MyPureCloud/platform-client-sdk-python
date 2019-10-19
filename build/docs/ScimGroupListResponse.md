---
title: ScimGroupListResponse
---
## ScimGroupListResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **total_results** | **int** | The total number of results. | [optional] |
| **start_index** | **int** | The 1-based index of the first result returned by this request. Add this to \&quot;itemsPerPage\&quot; when requesting the next page of results. | [optional] |
| **items_per_page** | **int** | The number of resources returned per page. | [optional] |
| **resources** | [**list[ScimV2Group]**](ScimV2Group.html) | The list of requested resources. If \&quot;count\&quot; is 0, then the list will be empty. | [optional] |
| **schemas** | **list[str]** | The list of supported schemas. | [optional] |
{: class="table table-striped"}



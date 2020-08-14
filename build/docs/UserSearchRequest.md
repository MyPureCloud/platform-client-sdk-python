---
title: UserSearchRequest
---
## UserSearchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **sort_order** | **str** | The sort order for results | [optional] |
| **sort_by** | **str** | The field in the resource that you want to sort the results by | [optional] |
| **page_size** | **int** | The number of results per page | [optional] |
| **page_number** | **int** | The page of resources you want to retrieve | [optional] |
| **sort** | [**list[SearchSort]**](SearchSort.html) | Multi-value sort order, list of multiple sort values | [optional] |
| **expand** | **list[str]** | Provides more details about a specified resource | [optional] |
| **query** | [**list[UserSearchCriteria]**](UserSearchCriteria.html) |  | [optional] |
| **integration_presence_source** | **str** | Gets an integration presence for users instead of their defaults. This parameter will only be used when presence is provided as an \&quot;expand\&quot;. When using this parameter the maximum number of users that can be returned is 10. | [optional] |
{: class="table table-striped"}



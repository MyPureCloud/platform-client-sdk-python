---
title: UserSearchCriteria
---
## UserSearchCriteria

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **end_value** | **str** | The end value of the range. This field is used for range search types. | [optional] |
| **values** | **list[str]** | A list of values for the search to match against | [optional] |
| **start_value** | **str** | The start value of the range. This field is used for range search types. | [optional] |
| **fields** | **list[str]** | Field names to search against | [optional] |
| **value** | **str** | A value for the search to match against | [optional] |
| **operator** | **str** | How to apply this search criteria against other criteria | [optional] |
| **group** | [**list[UserSearchCriteria]**](UserSearchCriteria.html) | Groups multiple conditions | [optional] |
| **type** | **str** | Search Type | |
{: class="table table-striped"}



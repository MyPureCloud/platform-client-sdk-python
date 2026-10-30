# CaseQueryJobCreate

## CaseQueryJobCreate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **page_size** | int | The total page size requested (default 25). | [optional] |
| **page_number** | int | The requested page number. | [optional] |
| **filters** | [list[CaseQueryJobFilter]](CaseQueryJobFilter) | List of filter objects to be used in the search. Use an empty list to run the query with no filters. | |
| **filter_groups** | [list[CaseQueryJobFilterGroup]](CaseQueryJobFilterGroup) | List of filter groups to be used in the search. The filters within a group are combined using the group operator; groups are combined with each other and with the top-level filters using AND.  | [optional] |
| **sort** | [CaseQueryJobSort](CaseQueryJobSort) | Sort order for results. | [optional] |
| **attributes** | list[str] | List of entity attributes to be retrieved in the result. | [optional] |
| **expands** | list[str] | Attributes to expand on each case in the job results. Expands are stored on the job and enriched by PubAPI when results are fetched. | [optional] |



_PureCloudPlatformClientV2 270.0.0_

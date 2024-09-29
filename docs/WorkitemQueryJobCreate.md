# WorkitemQueryJobCreate

## WorkitemQueryJobCreate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **page_size** | int | The total page size requested. Default 25 | [optional] |
| **page_number** | int | The page number requested | [optional] |
| **filters** | [list[WorkitemQueryJobFilter]](WorkitemQueryJobFilter) | List of filter objects to be used in the search. | |
| **expands** | list[str] | List of entity attributes to be expanded in the result. | [optional] |
| **attributes** | list[str] | List of entity attributes to be retrieved in the result. | [optional] |
| **sort** | [WorkitemQueryJobSort](WorkitemQueryJobSort) | Sort | [optional] |



_PureCloudPlatformClientV2 212.0.0_

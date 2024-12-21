# WorkitemQueryJobCreate

## WorkitemQueryJobCreate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **page_size** | int | The total page size requested. Default 25 | [optional] |
| **page_number** | int | The page number requested | [optional] |
| **filters** | [list[WorkitemQueryJobFilter]](WorkitemQueryJobFilter) | List of filter objects to be used in the search. | |
| **query_filters** | [list[WorkitemQueryJobQueryFilters]](WorkitemQueryJobQueryFilters) | Query filters for nested attributes. | [optional] |
| **expands** | list[str] | List of entity attributes to be expanded in the result. | [optional] |
| **attributes** | list[str] | List of entity attributes to be retrieved in the result. | [optional] |
| **sort** | [WorkitemQueryJobSort](WorkitemQueryJobSort) | Sort | [optional] |
| **date_interval_start** | datetime | Interval start date to use to filter results based on create date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_interval_end** | datetime | Interval end date to use to filter results based on create date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 219.0.0_

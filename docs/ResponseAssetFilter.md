# ResponseAssetFilter

## ResponseAssetFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **end_value** | str | The end value of the range. This field is used for range search types. Accepts numbers and date in ISO8601 format | [optional] |
| **values** | list[str] | A list of values for the search to match against | [optional] |
| **start_value** | str | The start value of the range. This field is used for range search types. Accepts numbers and date in ISO8601 format | [optional] |
| **fields** | list[str] | Field name to search against. Allowed Values: divisionId, name, contentLength, contentType, dateCreated | [optional] |
| **value** | str | A value for the search to match against | [optional] |
| **type** | str | How to apply this search criteria against other criteria. Filter type supported for each field:- name:[STARTS_WITH, TERM], divisionId:[TERM, TERMS], contentLength:[RANGE, GREATER_THAN_EQUAL_TO, LESS_THAN_EQUAL_TO], contentType:[STARTS_WITH, TERM] dateCreated:[DATE_RANGE] | [optional] |



_PureCloudPlatformClientV2 246.1.0_

# GKNDocumentationSearchCriteria

## GKNDocumentationSearchCriteria

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **end_value** | str | The end value of the range. This field is used for range search types. | [optional] |
| **values** | list[str] | A list of values for the search to match against | [optional] |
| **start_value** | str | The start value of the range. This field is used for range search types. | [optional] |
| **value** | str | A value for the search to match against | [optional] |
| **operator** | str | How to apply this search criteria against other criteria | [optional] |
| **group** | [list[GKNDocumentationSearchCriteria]](GKNDocumentationSearchCriteria) | Groups multiple conditions | [optional] |
| **date_format** | str | Set date format for criteria values when using date range search type.  Supports Java date format syntax, example yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSX. | [optional] |
| **type** | str | Search Type | |
| **fields** | list[str] | Field names to search against | [optional] |



_PureCloudPlatformClientV2 232.0.0_

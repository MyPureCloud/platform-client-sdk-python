# EvaluationSearchCriteriaDTO

## EvaluationSearchCriteriaDTO

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | str | The type of query Operation to Perform | |
| **field** | str | Field name to search against | |
| **end_value** | str | The end value of the range. This field is used for range search types. Date values must be in the format yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;. | [optional] |
| **values** | list[str] | A list of values for the search to match against. Only for Type: EXACT | [optional] |
| **start_value** | str | The start value of the range. This field is used for range search types. Date values must be in the format yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;. | [optional] |
| **value** | str | A value for the search to match against | [optional] |
| **operator** | str | How to apply this search criteria against other criteria | [optional] |



_PureCloudPlatformClientV2 249.0.0_

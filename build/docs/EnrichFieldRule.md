# EnrichFieldRule

## EnrichFieldRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **field** | str | A restricted JSONPath naming the specific field this combining behavior should apply to. Only dot notation with alphanumeric characters and underscores (e.g., $.address.address1, $.externalOrganization, $.tickers) are allowed. Bracket notation, array indexing, wildcards, sublists, and filter expressions are not permitted. | [optional] |
| **action** | str | The behavior for how to combine data from the request body and the database. | [optional] |
| **array_action** | str | The behavior for how to combine items in array field from the request body and the database. | [optional] |



_PureCloudPlatformClientV2 248.0.0_

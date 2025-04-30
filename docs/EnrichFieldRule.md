# EnrichFieldRule

## EnrichFieldRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **field** | str | A restricted JSONPath naming the specific field this combining behavior should apply to. You may use dot-notation for named fields, and array indexing for lists, but nothing more sophisticated (e.g. wildcards, sublists, filter expressions, etc). For example, to target the &#x60;firstName&#x60; field of a Contact, this should be \&quot;$.firstName\&quot;. | [optional] |
| **action** | str | The behavior for how to combine data from the request body and the database. | [optional] |
| **array_action** | str | The behavior for how to combine items in array field from the request body and the database. | [optional] |



_PureCloudPlatformClientV2 227.0.0_

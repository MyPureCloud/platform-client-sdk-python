# EnrichFieldRules

## EnrichFieldRules

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **default_action** | str | Default behavior for combining data from the submitted request with any entity found in the database. The default behavior if unspecified is &#x60;PreferProvided&#x60;, meaning any non-null fields in the submitted request will override data in the database, but all null fields will remain unchanged. Omitting a field in the request payload means that it will be treated as null. | [optional] |
| **rules** | [list[EnrichFieldRule]](EnrichFieldRule) | Field-specific behaviors for how to combine data from different sources. For example, you can set a &#x60;defaultAction&#x60; of &#x60;PreferProvided&#x60;, but use different behaviors such as &#x60;AlwaysUseProvided&#x60; or &#x60;PreferExisting&#x60; for specific fields. | [optional] |
| **default_array_action** | str | Default behavior for combining items in array field from the submitted request with any array entity found in the database. The default behavior if unspecified is &#x60;fill&#x60;, meaning the field value will always be the partial concatenation of both the array in the Database and the array in the contact body, up to the size limit of the array | [optional] |



_PureCloudPlatformClientV2 235.1.0_

# ContactsExportFilter

## ContactsExportFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **eq** | [ContactsExportFieldFilter](ContactsExportFieldFilter) | Filtered field should have the same value | [optional] |
| **pcIn** | [ContactsExportFieldListFilter](ContactsExportFieldListFilter) | Filtered field should match one of the listed values | [optional] |
| **pcAnd** | [list[ContactsExportFilter]](ContactsExportFilter) | Boolean AND combination of filters | [optional] |
| **pcOr** | [list[ContactsExportFilter]](ContactsExportFilter) | Boolean OR combination of filters | [optional] |
| **pcNot** | [ContactsExportFilter](ContactsExportFilter) | Boolean negation of filters | [optional] |



_PureCloudPlatformClientV2 241.0.0_

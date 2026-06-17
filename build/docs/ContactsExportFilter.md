# ContactsExportFilter

## ContactsExportFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **eq** | [ContactsExportFieldFilter](ContactsExportFieldFilter) | Filtered field should have the same value | [optional] |
| **pcIn** | [ContactsExportFieldListFilter](ContactsExportFieldListFilter) | Filtered field should match one of the listed values | [optional] |
| **lte** | [ContactsExportComparisonFieldFilter](ContactsExportComparisonFieldFilter) | Filtered field should be less than or equal to the value | [optional] |
| **gte** | [ContactsExportComparisonFieldFilter](ContactsExportComparisonFieldFilter) | Filtered field should be greater than or equal to the value | [optional] |
| **pcAnd** | [list[ContactsExportFilter]](ContactsExportFilter) | Boolean AND combination of filters | [optional] |
| **pcOr** | [list[ContactsExportFilter]](ContactsExportFilter) | Boolean OR combination of filters | [optional] |
| **pcNot** | [ContactsExportFilter](ContactsExportFilter) | Boolean negation of filters | [optional] |



_PureCloudPlatformClientV2 260.0.0_

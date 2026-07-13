# OrganizationsExportFilter

## OrganizationsExportFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **eq** | [OrganizationsExportFieldFilter](OrganizationsExportFieldFilter) | Filtered field should have the same value | [optional] |
| **pcIn** | [OrganizationsExportFieldListFilter](OrganizationsExportFieldListFilter) | Filtered field should match one of the listed values | [optional] |
| **lte** | [OrganizationsExportComparisonFieldFilter](OrganizationsExportComparisonFieldFilter) | Filtered field should be less than or equal to the value | [optional] |
| **gte** | [OrganizationsExportComparisonFieldFilter](OrganizationsExportComparisonFieldFilter) | Filtered field should be greater than or equal to the value | [optional] |
| **pcAnd** | [list[OrganizationsExportFilter]](OrganizationsExportFilter) | Boolean AND combination of filters | [optional] |
| **pcOr** | [list[OrganizationsExportFilter]](OrganizationsExportFilter) | Boolean OR combination of filters | [optional] |
| **pcNot** | [OrganizationsExportFilter](OrganizationsExportFilter) | Boolean negation of filters | [optional] |



_PureCloudPlatformClientV2 262.0.0_

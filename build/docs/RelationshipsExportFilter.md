# RelationshipsExportFilter

## RelationshipsExportFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **eq** | [RelationshipsExportFieldFilter](RelationshipsExportFieldFilter) | Filtered field should have the same value | [optional] |
| **pcIn** | [RelationshipsExportFieldListFilter](RelationshipsExportFieldListFilter) | Filtered field should match one of the listed values | [optional] |
| **lte** | [RelationshipsExportComparisonFieldFilter](RelationshipsExportComparisonFieldFilter) | Filtered field should be less than or equal to the value | [optional] |
| **gte** | [RelationshipsExportComparisonFieldFilter](RelationshipsExportComparisonFieldFilter) | Filtered field should be greater than or equal to the value | [optional] |
| **pcAnd** | [list[RelationshipsExportFilter]](RelationshipsExportFilter) | Boolean AND combination of filters | [optional] |
| **pcOr** | [list[RelationshipsExportFilter]](RelationshipsExportFilter) | Boolean OR combination of filters | [optional] |
| **pcNot** | [RelationshipsExportFilter](RelationshipsExportFilter) | Boolean negation of filters | [optional] |



_PureCloudPlatformClientV2 264.0.0_

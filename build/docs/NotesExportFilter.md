# NotesExportFilter

## NotesExportFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **eq** | [NotesExportFieldFilter](NotesExportFieldFilter) | Filtered field should have the same value | [optional] |
| **pcIn** | [NotesExportFieldListFilter](NotesExportFieldListFilter) | Filtered field should match one of the listed values | [optional] |
| **lte** | [NotesExportComparisonFieldFilter](NotesExportComparisonFieldFilter) | Filtered field should be less than or equal to the value | [optional] |
| **gte** | [NotesExportComparisonFieldFilter](NotesExportComparisonFieldFilter) | Filtered field should be greater than or equal to the value | [optional] |
| **pcAnd** | [list[NotesExportFilter]](NotesExportFilter) | Boolean AND combination of filters | [optional] |
| **pcOr** | [list[NotesExportFilter]](NotesExportFilter) | Boolean OR combination of filters | [optional] |
| **pcNot** | [NotesExportFilter](NotesExportFilter) | Boolean negation of filters | [optional] |



_PureCloudPlatformClientV2 266.0.0_

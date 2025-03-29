# ReportingExportMetadataJobResponse

## ReportingExportMetadataJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **view_type** | str | The view type of the export metadata | [optional] |
| **date_limitations** | str | The date limitations of the export metadata | [optional] |
| **required_filters** | list[str] | The list of required filters for the export metadata | [optional] |
| **supported_filters** | list[str] | The list of supported filters for the export metadata | [optional] |
| **required_column_ids** | list[str] | The list of required column ids for the export metadata | [optional] |
| **dependent_column_ids** | dict(str, list[str]) | The list of dependent column ids for the export metadata | [optional] |
| **available_column_ids** | list[str] | The list of available column ids for the export metadata | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 224.1.0_

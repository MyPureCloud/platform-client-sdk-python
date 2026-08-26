# AggregatedSnapshotExportJobStatus

## AggregatedSnapshotExportJobStatus

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | |
| **status** | str | The status of the export job | |
| **download_url** | str | The download URL for the completed export. Populated when status is Complete | [optional] |
| **error** | [CsvExportErrorDetails](CsvExportErrorDetails) | Error details if the export failed. Populated when status is Error | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 265.0.0_

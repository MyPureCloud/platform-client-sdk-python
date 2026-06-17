# DecisionTableExportJob

## DecisionTableExportJob

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **table_version** | int | The version of the decision table that was exported. | [optional] |
| **status** | str | Current status of the export job. | [optional] |
| **created_by** | [AddressableEntityRef](AddressableEntityRef) | The user who created the export job. | [optional] |
| **date_created** | datetime | Date when this export job was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date when this export job was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **file_name** | str | Name of the exported file. | [optional] |
| **download** | [AddressableEntityRef](AddressableEntityRef) | Reference to the download resource for obtaining the exported file. | [optional] |
| **date_download_expires** | datetime | Date when the download link expires. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **export_type** | str | The type of export that was performed. | [optional] |
| **total_rows** | int | Total number of rows to export (set when row loading begins). | [optional] |
| **rows_exported** | int | The number of rows exported. | [optional] |
| **format** | str | The format of the exported file. | [optional] |
| **error** | [DecisionTableExportJobError](DecisionTableExportJobError) | Error details if the export job failed. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 260.0.0_

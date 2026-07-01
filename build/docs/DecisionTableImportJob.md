# DecisionTableImportJob

## DecisionTableImportJob

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **table_version** | int | The table version to be replaced by this import | [optional] |
| **status** | str | Current status of the import job | |
| **upload_url** | str | Pre-signed URL to upload the import file (PUT) | [optional] |
| **upload_headers** | dict(str, str) | Headers required when uploading file with data to be imported to uploadUrl | [optional] |
| **import_mode** | str | Whether rows are appended to existing rows or rows are replaced | |
| **file_name** | str | Original file name supplied when the job was created, including the file extension | [optional] |
| **created_by** | [AddressableEntityRef](AddressableEntityRef) | The user who created the job | [optional] |
| **date_created** | datetime | When the job was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | When the job was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_completed** | datetime | When processing finished, successfully or not. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_expires** | datetime | When upload credentials expire. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **row_metrics** | [DecisionTableImportRowMetrics](DecisionTableImportRowMetrics) | Row-level metrics populated incrementally during import processing | [optional] |
| **error** | [DecisionTableImportJobError](DecisionTableImportJobError) | Present when the import job could not be successfully finished | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 261.0.0_

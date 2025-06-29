# ContactsBulkOperationJob

## ContactsBulkOperationJob

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique job identifier. | [optional] |
| **state** | str | The job state. | [optional] |
| **type** | str | The job type. | [optional] |
| **total_records** | int | Total records that will be impacted by the bulk operation. | [optional] |
| **completed_records** | int | Amount of records that have been impacted by the bulk operation. | [optional] |
| **percent_complete** | int | Percentage of records that have been impacted by the bulk operation. | [optional] |
| **failure_reason** | [ErrorInfo](ErrorInfo) | Information on failure reason. | [optional] |
| **download_uri** | str | URI to download the original backup contacts. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 232.0.0_

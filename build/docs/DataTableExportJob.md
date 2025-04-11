# DataTableExportJob

## DataTableExportJob

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **owner** | [AddressableEntityRef](AddressableEntityRef) | The PureCloud user who started the export job | [optional] |
| **status** | str | The status of the export job | |
| **date_created** | datetime | The timestamp of when the export began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_completed** | datetime | The timestamp of when the export stopped (either successfully or unsuccessfully). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **download_uri** | str | The URL of the location at which the caller can download the export file, when available | [optional] |
| **error_information** | [ErrorBody](ErrorBody) | Any error information, or null of the processing is not in an error state | [optional] |
| **count_records_processed** | int | The current count of the number of records processed | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 226.0.0_

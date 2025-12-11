# DataTableImportJob

## DataTableImportJob

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **owner** | [AddressableEntityRef](AddressableEntityRef) | The PureCloud user who started the import job | [optional] |
| **status** | str | The status of the import job | |
| **date_created** | datetime | The timestamp of when the import began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_completed** | datetime | The timestamp of when the import stopped (either successfully or unsuccessfully). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **upload_uri** | str | The URL of the location at which the caller can upload the file to be imported | [optional] |
| **import_mode** | str | The indication of whether the processing should remove rows that don&#39;t appear in the import file | [optional] |
| **error_information** | [ErrorBody](ErrorBody) | Any error information, or null of the processing is not in an error state | [optional] |
| **count_records_updated** | int | The current count of the number of records processed | [optional] |
| **count_records_deleted** | int | The current count of the number of records deleted | [optional] |
| **count_records_failed** | int | The current count of the number of records that failed to import | [optional] |
| **upload_headers** | dict(str, str) | Required headers when uploading a file through PUT request to the URL in the &#39;uploadURI&#39; field | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.0.0_

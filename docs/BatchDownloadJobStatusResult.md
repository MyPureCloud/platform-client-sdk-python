# BatchDownloadJobStatusResult

## BatchDownloadJobStatusResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **job_id** | str | JobId returned when job was initially submitted. | [optional] |
| **expected_result_count** | int | Number of results expected when job is completed, this includes both success and error results. This number could change as recordings are being discovered and processed. | [optional] |
| **result_count** | int | Current number of results available, this includes both success and error results. | [optional] |
| **error_count** | int | Current number of error results. | [optional] |
| **results** | [list[BatchDownloadJobResult]](BatchDownloadJobResult) | Current set of results for the job. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 214.0.0_

---
title: BatchDownloadJobStatusResult
---
## BatchDownloadJobStatusResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **job_id** | **str** | JobId returned when job was initially submitted | [optional] |
| **expected_result_count** | **int** | Number of results expected when job is completed | [optional] |
| **result_count** | **int** | Current number of results available | [optional] |
| **error_count** | **int** | Number of error results produced so far | [optional] |
| **results** | [**list[BatchDownloadJobResult]**](BatchDownloadJobResult.html) | Current set of results for the job | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



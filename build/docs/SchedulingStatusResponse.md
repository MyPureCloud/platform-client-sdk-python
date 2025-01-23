# SchedulingStatusResponse

## SchedulingStatusResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID generated for the scheduling job.  Use to GET result when job is completed. | [optional] |
| **status** | str | The status of the scheduling job. | [optional] |
| **error_details** | [list[SchedulingProcessingError]](SchedulingProcessingError) | If the request could not be properly processed, error details will be given here. | [optional] |
| **scheduling_result_uri** | str | The uri of the scheduling result. It has a value if the status is &#39;Success&#39;. | [optional] |
| **percent_complete** | int | The percentage of the job that is complete. | [optional] |



_PureCloudPlatformClientV2 220.0.0_

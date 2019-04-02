---
title: ModelingStatusResponse
---
## ModelingStatusResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The ID generated for the modeling job.  Use to GET result when job is completed. | [optional] |
| **status** | **str** | The status of the modeling job. | [optional] |
| **error_details** | [**list[ModelingProcessingError]**](ModelingProcessingError.html) | If the request could not be properly processed, error details will be given here. | [optional] |
| **modeling_result_uri** | **str** | The uri of the modeling result. It has a value if the status is either &#39;Success&#39;, &#39;PartialFailure&#39;, or &#39;Failed&#39;. | [optional] |
{: class="table table-striped"}



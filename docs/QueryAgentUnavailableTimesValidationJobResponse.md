# QueryAgentUnavailableTimesValidationJobResponse

## QueryAgentUnavailableTimesValidationJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **agent** | [UserReference](UserReference) | The agent who started the job | |
| **status** | str | Status of the job | |
| **result** | [UnavailableTimesValidationResult](UnavailableTimesValidationResult) | Validation results if status &#x3D;&#x3D; &#39;Complete&#39; | [optional] |
| **error** | [ErrorBody](ErrorBody) | Error details if status &#x3D;&#x3D; &#39;Error&#39;. The error occurs if the validation job has failed | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 247.0.0_

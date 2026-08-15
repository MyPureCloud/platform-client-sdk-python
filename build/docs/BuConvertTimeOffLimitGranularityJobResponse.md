# BuConvertTimeOffLimitGranularityJobResponse

## BuConvertTimeOffLimitGranularityJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | |
| **time_off_limit** | [BuTimeOffLimitReference](BuTimeOffLimitReference) | The time-off limit associated with this job | |
| **status** | str | The status of the job | |
| **progress** | [BuConvertTimeOffLimitGranularityJobProgress](BuConvertTimeOffLimitGranularityJobProgress) | Progress of time-off limit granularity conversion | [optional] |
| **error** | [ErrorBody](ErrorBody) | Error information. Set only when status is Error | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 264.0.0_

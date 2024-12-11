# ContactImportJobResponse

## ContactImportJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **status** | str |  | [optional] |
| **status_details** | str | Detailed description for JobStatus. | [optional] |
| **execution_step** | str | Detailed description for the Job execution state | [optional] |
| **metadata** | [ContactImportJobMetadata](ContactImportJobMetadata) | Metadata for the job | [optional] |
| **date_created** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **settings** | [AddressableEntityRef](AddressableEntityRef) | Settings | |



_PureCloudPlatformClientV2 218.0.0_

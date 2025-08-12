# OrphanRecording

## OrphanRecording

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **created_time** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **recovered_time** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **provider_type** | str |  | [optional] |
| **media_size_bytes** | int |  | [optional] |
| **media_type** | str |  | [optional] |
| **media_subtype** | str |  | [optional] |
| **media_subject** | str |  | [optional] |
| **file_state** | str |  | [optional] |
| **provider_endpoint** | [Endpoint](Endpoint) |  | [optional] |
| **recording** | [Recording](Recording) |  | [optional] |
| **orphan_status** | str | The status of the orphaned recording&#39;s conversation. | [optional] |
| **source_orphaning_id** | str | An identifier used during recovery operations by the supplying hybrid platform to track back and determine which interaction this recording is associated with | [optional] |
| **region** | str |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.0.0_

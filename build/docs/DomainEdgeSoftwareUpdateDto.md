# DomainEdgeSoftwareUpdateDto

## DomainEdgeSoftwareUpdateDto

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **version** | [DomainEdgeSoftwareVersionDto](DomainEdgeSoftwareVersionDto) | Version | |
| **max_download_rate** | int |  | [optional] |
| **download_start_time** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **execute_start_time** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **execute_stop_time** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **execute_on_idle** | bool |  | [optional] |
| **status** | str |  | [optional] |
| **edge_uri** | str |  | [optional] |
| **call_draining_wait_time_seconds** | int |  | [optional] |
| **current** | bool |  | [optional] |



_PureCloudPlatformClientV2 216.0.0_

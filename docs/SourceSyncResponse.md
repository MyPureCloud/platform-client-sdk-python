# SourceSyncResponse

## SourceSyncResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | str | Sync state. | [optional] |
| **error** | [ErrorBody](ErrorBody) | Sync error. | [optional] |
| **date_created** | datetime | Synchronization creation date-time for this source. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Synchronization last modification date-time for this source. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **knowledge_base** | [AddressableEntityRef](AddressableEntityRef) | Knowledge base to which this synchronization belongs. | [optional] |
| **source** | [AddressableEntityRef](AddressableEntityRef) | Source to which this synchronization belongs. | [optional] |



_PureCloudPlatformClientV2 236.0.0_

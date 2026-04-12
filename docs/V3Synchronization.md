# V3Synchronization

## V3Synchronization

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **type** | str | The type of the synchronization. | [optional] |
| **created_by** | [UserReference](UserReference) | The user who started the synchronization if the source is manually synchronized or the user who created the source for scheduled synchronization. | [optional] |
| **source** | [V3SourceRef](V3SourceRef) | The source of the synchronization. | [optional] |
| **date_start** | datetime | The start time of the synchronization. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_end** | datetime | The end time of the synchronization. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_source_interval_start** | datetime | The start time of the interval to be synchronized from the source. Source item changes during that interval are included in this synchronization. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_source_interval_end** | datetime | The end time of the interval to be synchronized from the source. Source item changes during that interval are included in this synchronization. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **trigger_type** | str | The trigger type of the synchronization. | [optional] |
| **status** | str | The status of the synchronization. | [optional] |
| **statistics** | [V3SynchronizationStatistics](V3SynchronizationStatistics) | Statistics of the synchronization. | [optional] |
| **error** | [ErrorBody](ErrorBody) | The error that occurred during the synchronization. | [optional] |
| **ingestion_status** | str | The status of the ingestion. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 256.0.0_

# V3SourceDetailedResponse

## V3SourceDetailedResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the source. | [optional] |
| **connection_id** | str | The connectionId of the source. | [optional] |
| **type** | str | The type of the source. | [optional] |
| **trigger_type** | str | The trigger type of the source. | [optional] |
| **status** | str | The current status of the source. | [optional] |
| **created_by** | [UserReference](UserReference) | The user who created the source. | [optional] |
| **modified_by** | [UserReference](UserReference) | The user who modified the document. | [optional] |
| **date_created** | datetime | Source creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Source last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **last_sync** | [V3SourceLastSynchronization](V3SourceLastSynchronization) | The last synchronization of the source. | [optional] |
| **schedule_settings** | [V3SourceScheduleSettings](V3SourceScheduleSettings) | Settings that determine when the source starts a sync. | [optional] |
| **filters** | [V3SourceFilter](V3SourceFilter) | Filters that determine what documents are synced. | [optional] |
| **filter_details** | [V3SourceFilterDetails](V3SourceFilterDetails) | Additional details to the source&#39;s filters. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 257.1.0_

# UserActivity

## UserActivity

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the user | |
| **routing_status** | [UserActivityRoutingStatus](UserActivityRoutingStatus) | The current routing status of the user | [optional] |
| **presence** | [UserActivityAdherencePresence](UserActivityAdherencePresence) | The current system presence of the user | [optional] |
| **out_of_office** | [UserActivityOutOfOffice](UserActivityOutOfOffice) | The current out of office state of the user | [optional] |
| **active_queue_ids** | list[str] | The IDs of the queues for which the user is active | |
| **date_active_queues_changed** | datetime | The date the activeQueueIds list was last modified. For reference only - subject to eventual consistency. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 268.0.0_

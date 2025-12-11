# QueueConversationVideoEventTopicCobrowse

## QueueConversationVideoEventTopicCobrowse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | str |  | [optional] |
| **initial_state** | str |  | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **pcSelf** | [QueueConversationVideoEventTopicAddress](QueueConversationVideoEventTopicAddress) | Address and name data for a call endpoint. | [optional] |
| **room_id** | str | The room id for the chat. | [optional] |
| **cobrowse_session_id** | str | The co-browse session ID. | [optional] |
| **cobrowse_role** | str | This value identifies the role of the co-browse client within the co-browse session (a client is a sharer or a viewer). | [optional] |
| **controlling** | list[str] | ID of co-browse participants for which this client has been granted control (list is empty if this client cannot control any shared pages). | [optional] |
| **viewer_url** | str | The URL that can be used to open co-browse session in web browser. | [optional] |
| **provider** | str | The source provider of the co-browse communication. | [optional] |
| **script_id** | str | The UUID of the script to use. | [optional] |
| **peer_id** | str | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **provider_event_time** | datetime | The time when the provider event which triggered this conversation update happened in the corrected provider clock (milliseconds since 1970-01-01 00:00:00 UTC). | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. | [optional] |
| **wrapup** | [QueueConversationVideoEventTopicWrapup](QueueConversationVideoEventTopicWrapup) | Call wrap up or disposition data. | [optional] |
| **after_call_work** | [QueueConversationVideoEventTopicAfterCallWork](QueueConversationVideoEventTopicAfterCallWork) | A communication&#39;s after-call work data. | [optional] |
| **after_call_work_required** | bool | Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested. | [optional] |
| **queue_media_settings** | [QueueConversationVideoEventTopicQueueMediaSettings](QueueConversationVideoEventTopicQueueMediaSettings) | Represents the queue setting for this media. | [optional] |



_PureCloudPlatformClientV2 246.0.0_

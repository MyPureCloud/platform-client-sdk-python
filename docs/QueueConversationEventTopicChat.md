# QueueConversationEventTopicChat

## QueueConversationEventTopicChat

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | str |  | [optional] |
| **initial_state** | str |  | [optional] |
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **provider** | str | The source provider of the chat. | [optional] |
| **script_id** | str | The UUID of the script to use. | [optional] |
| **peer_id** | str | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **room_id** | str | The room id for the chat. | [optional] |
| **avatar_image_url** | str | The avatar for the chat (if available). | [optional] |
| **held** | bool | True if this call is held and the person on this side hears silence. | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_hold_time** | datetime | The timestamp the chat was placed on hold in the cloud clock if the chat is currently on hold. | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. | [optional] |
| **journey_context** | [QueueConversationEventTopicJourneyContext](QueueConversationEventTopicJourneyContext) |  | [optional] |
| **wrapup** | [QueueConversationEventTopicWrapup](QueueConversationEventTopicWrapup) | Call wrap up or disposition data. | [optional] |
| **after_call_work** | [QueueConversationEventTopicAfterCallWork](QueueConversationEventTopicAfterCallWork) | A communication&#39;s after-call work data. | [optional] |
| **after_call_work_required** | bool | Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested. | [optional] |
| **queue_media_settings** | [QueueConversationEventTopicQueueMediaSettings](QueueConversationEventTopicQueueMediaSettings) | Represents the queue setting for this media. | [optional] |



_PureCloudPlatformClientV2 246.1.0_

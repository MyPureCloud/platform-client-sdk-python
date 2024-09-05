# QueueConversationVideoEventTopicCall

## QueueConversationVideoEventTopicCall

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **state** | str |  | [optional] |
| **initial_state** | str |  | [optional] |
| **recording** | bool | True if this call is being recorded. | [optional] |
| **recording_state** | str | State of recording on this call. | [optional] |
| **muted** | bool | True if this call is muted so that remote participants can&#39;t hear any audio from this end. | [optional] |
| **confined** | bool | True if this call is held and the person on this side hears hold music. | [optional] |
| **held** | bool | True if this call is held and the person on this side hears silence. | [optional] |
| **secure_pause** | bool | True when the recording of this call is in secure pause status. | [optional] |
| **error_info** | [QueueConversationVideoEventTopicErrorDetails](QueueConversationVideoEventTopicErrorDetails) |  | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_hold_time** | datetime | The timestamp the call was placed on hold in the cloud clock if the call is currently on hold. | [optional] |
| **direction** | str | Whether a call is inbound or outbound. | [optional] |
| **document_id** | str | If call is a fax of a document in content management, the id of the document in content management. | [optional] |
| **pcSelf** | [QueueConversationVideoEventTopicAddress](QueueConversationVideoEventTopicAddress) |  | [optional] |
| **other** | [QueueConversationVideoEventTopicAddress](QueueConversationVideoEventTopicAddress) | Address and name data for a call endpoint. | [optional] |
| **provider** | str | The source provider of the call. | [optional] |
| **script_id** | str | The UUID of the script to use. | [optional] |
| **peer_id** | str | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. | [optional] |
| **disconnect_reasons** | [list[QueueConversationVideoEventTopicDisconnectReason]](QueueConversationVideoEventTopicDisconnectReason) | List of reasons that this call was disconnected. This will be set once the call disconnects. | [optional] |
| **fax_status** | [QueueConversationVideoEventTopicFaxStatus](QueueConversationVideoEventTopicFaxStatus) |  | [optional] |
| **uui_data** | str | User to User Information (UUI) data managed by SIP session application. | [optional] |
| **barged_time** | datetime | The timestamp when this participant was connected to the barge conference in the provider clock. | [optional] |
| **wrapup** | [QueueConversationVideoEventTopicWrapup](QueueConversationVideoEventTopicWrapup) | Call wrap up or disposition data. | [optional] |
| **after_call_work** | [QueueConversationVideoEventTopicAfterCallWork](QueueConversationVideoEventTopicAfterCallWork) |  | [optional] |
| **after_call_work_required** | bool | Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested. | [optional] |
| **agent_assistant_id** | str | UUID of virtual agent assistant that provide suggestions to the agent participant during the conversation. | [optional] |
| **queue_media_settings** | [QueueConversationVideoEventTopicQueueMediaSettings](QueueConversationVideoEventTopicQueueMediaSettings) |  | [optional] |



_PureCloudPlatformClientV2 210.0.0_

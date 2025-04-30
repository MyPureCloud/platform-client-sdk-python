# QueueConversationVideoEventTopicEmail

## QueueConversationVideoEventTopicEmail

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **state** | str |  | [optional] |
| **initial_state** | str |  | [optional] |
| **held** | bool | True if this call is held and the person on this side hears silence. | [optional] |
| **auto_generated** | bool | Indicates that the email was auto-generated like an Out of Office reply. | [optional] |
| **subject** | str | The subject for the initial email that started this conversation. | [optional] |
| **provider** | str | The source provider of the email. | [optional] |
| **script_id** | str | The UUID of the script to use. | [optional] |
| **peer_id** | str | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **messages_sent** | int | The number of email messages sent by this participant. | [optional] |
| **error_info** | [QueueConversationVideoEventTopicErrorDetails](QueueConversationVideoEventTopicErrorDetails) | Detailed information about an error response. | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_hold_time** | datetime | The timestamp the email was placed on hold in the cloud clock if the email is currently on hold. | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. | [optional] |
| **message_id** | str | A globally unique identifier for the stored content of this communication. | [optional] |
| **direction** | str | Whether an email is inbound or outbound. | [optional] |
| **draft_attachments** | [list[QueueConversationVideoEventTopicAttachment]](QueueConversationVideoEventTopicAttachment) | A list of uploaded attachments on the email draft. | [optional] |
| **spam** | bool | Indicates if the inbound email was marked as spam. | [optional] |
| **wrapup** | [QueueConversationVideoEventTopicWrapup](QueueConversationVideoEventTopicWrapup) | Call wrap up or disposition data. | [optional] |
| **after_call_work** | [QueueConversationVideoEventTopicAfterCallWork](QueueConversationVideoEventTopicAfterCallWork) | A communication&#39;s after-call work data. | [optional] |
| **after_call_work_required** | bool | Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested. | [optional] |
| **queue_media_settings** | [QueueConversationVideoEventTopicQueueMediaSettings](QueueConversationVideoEventTopicQueueMediaSettings) | Represents the queue setting for this media. | [optional] |
| **resume_time** | datetime | The time when a parked email should resume. | [optional] |
| **park_time** | datetime | The time when an  parked email was parked. | [optional] |



_PureCloudPlatformClientV2 227.0.0_

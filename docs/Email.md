# Email

## Email

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | str | The connection state of this communication. | [optional] |
| **initial_state** | str | The initial connection state of this communication. | [optional] |
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **held** | bool | True if this call is held and the person on this side hears silence. | [optional] |
| **subject** | str | The subject for the initial email that started this conversation. | [optional] |
| **messages_sent** | int | The number of email messages sent by this participant. | [optional] |
| **segments** | [list[Segment]](Segment) | The time line of the participant&#39;s email, divided into activity segments. | [optional] |
| **direction** | str | The direction of the email | [optional] |
| **recording_id** | str | A globally unique identifier for the recording associated with this call. | [optional] |
| **error_info** | [ErrorBody](ErrorBody) |  | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_hold_time** | datetime | The timestamp the email was placed on hold in the cloud clock if the email is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **start_alerting_time** | datetime | The timestamp the communication has when it is first put into an alerting state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **auto_generated** | bool | Indicates that the email was auto-generated like an Out of Office reply. | [optional] |
| **provider** | str | The source provider for the email. | [optional] |
| **script_id** | str | The UUID of the script to use. | [optional] |
| **peer_id** | str | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **message_id** | str | A globally unique identifier for the stored content of this communication. | [optional] |
| **draft_attachments** | [list[Attachment]](Attachment) | A list of uploaded attachments on the email draft. | [optional] |
| **spam** | bool | Indicates if the inbound email was marked as spam. | [optional] |
| **wrapup** | [Wrapup](Wrapup) | Call wrap up or disposition data. | [optional] |
| **after_call_work** | [AfterCallWork](AfterCallWork) | After-call work for the communication. | [optional] |
| **after_call_work_required** | bool | Indicates if after-call work is required for a communication. Only used when the ACW Setting is Agent Requested. | [optional] |
| **queue_media_settings** | [ConversationQueueMediaSettings](ConversationQueueMediaSettings) | Represents the queue settings for this media type. | [optional] |
| **park_time** | datetime | Represents the time when an email was put into parked state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 210.0.0_

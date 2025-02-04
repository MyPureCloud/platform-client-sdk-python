# Call

## Call

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | str | The connection state of this communication. | [optional] |
| **initial_state** | str | The initial connection state of this communication. | [optional] |
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **direction** | str | The direction of the call | [optional] |
| **recording** | bool | True if this call is being recorded. | [optional] |
| **recording_state** | str | State of recording on this call. | [optional] |
| **muted** | bool | True if this call is muted so that remote participants can&#39;t hear any audio from this end. | [optional] |
| **confined** | bool | True if this call is held and the person on this side hears hold music. | [optional] |
| **held** | bool | True if this call is held and the person on this side hears silence. | [optional] |
| **secure_pause** | bool | True when the recording of this call is in secure pause status. | [optional] |
| **recording_id** | str | A globally unique identifier for the recording associated with this call. | [optional] |
| **segments** | [list[Segment]](Segment) | The time line of the participant&#39;s call, divided into activity segments. | [optional] |
| **error_info** | [ErrorInfo](ErrorInfo) |  | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_hold_time** | datetime | The timestamp the call was placed on hold in the cloud clock if the call is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **document_id** | str | If call is an outbound fax of a document from content management, then this is the id in content management. | [optional] |
| **start_alerting_time** | datetime | The timestamp the communication has when it is first put into an alerting state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **disconnect_reasons** | [list[DisconnectReason]](DisconnectReason) | List of reasons that this call was disconnected. This will be set once the call disconnects. | [optional] |
| **fax_status** | [FaxStatus](FaxStatus) | Extra information on fax transmission. | [optional] |
| **provider** | str | The source provider for the call. | [optional] |
| **script_id** | str | The UUID of the script to use. | [optional] |
| **peer_id** | str | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **uui_data** | str | User to User Information (UUI) data managed by SIP session application. | [optional] |
| **pcSelf** | [Address](Address) | Address and name data for a call endpoint. | [optional] |
| **other** | [Address](Address) | Address and name data for a call endpoint. | [optional] |
| **wrapup** | [Wrapup](Wrapup) | Call wrap up or disposition data. | [optional] |
| **after_call_work** | [AfterCallWork](AfterCallWork) | After-call work for the communication. | [optional] |
| **after_call_work_required** | bool | Indicates if after-call work is required for a communication. Only used when the ACW Setting is Agent Requested. | [optional] |
| **agent_assistant_id** | str | UUID of virtual agent assistant that provide suggestions to the agent participant during the conversation. | [optional] |
| **queue_media_settings** | [ConversationQueueMediaSettings](ConversationQueueMediaSettings) | Represents the queue settings for this media type. | [optional] |
| **disposition** | [Disposition](Disposition) | Call resolution data for Dialer bulk make calls commands. | [optional] |



_PureCloudPlatformClientV2 221.0.0_

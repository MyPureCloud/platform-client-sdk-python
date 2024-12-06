# Message

## Message

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | str | The connection state of this communication. | [optional] |
| **initial_state** | str | The initial connection state of this communication. | [optional] |
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **held** | bool | True if this call is held and the person on this side hears silence. | [optional] |
| **segments** | [list[Segment]](Segment) | The time line of the participant&#39;s message, divided into activity segments. | [optional] |
| **direction** | str | The direction of the message. | [optional] |
| **recording_id** | str | A globally unique identifier for the recording associated with this message. | [optional] |
| **error_info** | [ErrorBody](ErrorBody) |  | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_hold_time** | datetime | The timestamp the message was placed on hold in the cloud clock if the message is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **start_alerting_time** | datetime | The timestamp the communication has when it is first put into an alerting state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **provider** | str | The source provider for the message. | [optional] |
| **authenticated** | bool | If true, the participant member is authenticated. | [optional] |
| **type** | str | Indicates the type of message platform from which the message originated. | [optional] |
| **recipient_country** | str | Indicates the country where the recipient is associated in ISO 3166-1 alpha-2 format. | [optional] |
| **recipient_type** | str | The type of the recipient. Eg: Provisioned phoneNumber is the recipient for sms message type. | [optional] |
| **script_id** | str | The UUID of the script to use. | [optional] |
| **peer_id** | str | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **to_address** | [Address](Address) | Address and name data for a call endpoint. | [optional] |
| **from_address** | [Address](Address) | Address and name data for a call endpoint. | [optional] |
| **messages** | [list[MessageDetails]](MessageDetails) | The messages sent on this communication channel. | [optional] |
| **journey_context** | [JourneyContext](JourneyContext) | A subset of the Journey System&#39;s data relevant to a part of a conversation (for external linkage and internal usage/context). | [optional] |
| **wrapup** | [Wrapup](Wrapup) | Call wrap up or disposition data. | [optional] |
| **after_call_work** | [AfterCallWork](AfterCallWork) | After-call work for the communication. | [optional] |
| **after_call_work_required** | bool | Indicates if after-call work is required for a communication. Only used when the ACW Setting is Agent Requested. | [optional] |
| **agent_assistant_id** | str | UUID of virtual agent assistant that provide suggestions to the agent participant during the conversation. | [optional] |
| **byo_sms_integration_id** | str | The internal id representing the customer supplied sms integration message. | [optional] |
| **queue_media_settings** | [ConversationQueueMediaSettings](ConversationQueueMediaSettings) | Represents the queue settings for this media type. | [optional] |



_PureCloudPlatformClientV2 217.0.0_

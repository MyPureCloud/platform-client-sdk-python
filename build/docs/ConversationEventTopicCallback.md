# ConversationEventTopicCallback

## ConversationEventTopicCallback

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | str |  | [optional] |
| **initial_state** | str |  | [optional] |
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **direction** | str | The direction of the call | [optional] |
| **held** | bool | True if this call is held and the person on this side hears silence. | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_hold_time** | datetime | The timestamp the callback was placed on hold in the cloud clock if the callback is currently on hold. | [optional] |
| **dialer_preview** | [ConversationEventTopicDialerPreview](ConversationEventTopicDialerPreview) |  | [optional] |
| **voicemail** | [ConversationEventTopicVoicemail](ConversationEventTopicVoicemail) |  | [optional] |
| **callback_numbers** | list[str] | The phone number(s) to use to place the callback. | [optional] |
| **callback_user_name** | str | The name of the user requesting a callback. | [optional] |
| **script_id** | str | The UUID of the script to use. | [optional] |
| **peer_id** | str | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **external_campaign** | bool | True if the call for the callback uses external dialing. | [optional] |
| **skip_enabled** | bool | True if the ability to skip a callback should be enabled. | [optional] |
| **provider** | str | The source provider of the callback. | [optional] |
| **timeout_seconds** | int | The number of seconds before the system automatically places a call for a callback.  0 means the automatic placement is disabled. | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. | [optional] |
| **callback_scheduled_time** | datetime | The timestamp when this communication is scheduled in the provider clock. If this value is missing it indicates the callback will be placed immediately. | [optional] |
| **automated_callback_config_id** | str | The id of the config for automatically placing the callback (and handling the disposition). If null, the callback will not be placed automatically but routed to an agent as per normal. | [optional] |
| **wrapup** | [ConversationEventTopicWrapup](ConversationEventTopicWrapup) | Call wrap up or disposition data. | [optional] |
| **after_call_work** | [ConversationEventTopicAfterCallWork](ConversationEventTopicAfterCallWork) | A communication&#39;s after-call work data. | [optional] |
| **after_call_work_required** | bool | Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested. | [optional] |
| **caller_id** | str | The phone number displayed to recipients of the phone call. The value should conform to the E164 format. | [optional] |
| **caller_id_name** | str | The name displayed to recipients of the phone call. | [optional] |
| **queue_media_settings** | [ConversationEventTopicQueueMediaSettings](ConversationEventTopicQueueMediaSettings) | Represents the queue setting for this media. | [optional] |



_PureCloudPlatformClientV2 235.0.0_

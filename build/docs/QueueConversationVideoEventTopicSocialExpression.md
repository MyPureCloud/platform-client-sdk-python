# QueueConversationVideoEventTopicSocialExpression

## QueueConversationVideoEventTopicSocialExpression

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | str |  | [optional] |
| **initial_state** | str |  | [optional] |
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **social_media_id** | str | A globally unique identifier for the social media. | [optional] |
| **social_media_hub** | str | The social network of the communication | [optional] |
| **social_user_name** | str | The social media user name of the communication | [optional] |
| **preview_text** | str | The text preview of the communication contents | [optional] |
| **recording_id** | str | A globally unique identifier for the recording associated with this chat. | [optional] |
| **held** | bool | True if this call is held and the person on this side hears silence. | [optional] |
| **provider** | str | The source provider of the social expression. | [optional] |
| **script_id** | str | The UUID of the script to use. | [optional] |
| **peer_id** | str | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_hold_time** | datetime | The timestamp the chat was placed on hold in the cloud clock if the chat is currently on hold. | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. | [optional] |
| **wrapup** | [QueueConversationVideoEventTopicWrapup](QueueConversationVideoEventTopicWrapup) | Call wrap up or disposition data. | [optional] |
| **after_call_work** | [QueueConversationVideoEventTopicAfterCallWork](QueueConversationVideoEventTopicAfterCallWork) | A communication&#39;s after-call work data. | [optional] |
| **after_call_work_required** | bool | Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested. | [optional] |



_PureCloudPlatformClientV2 237.0.0_

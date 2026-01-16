# SocialExpression

## SocialExpression

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | str | The connection state of this communication. | [optional] |
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **social_media_id** | str | A globally unique identifier for the social media. | [optional] |
| **social_media_hub** | str | The social network of the communication | [optional] |
| **social_user_name** | str | The user name for the communication. | [optional] |
| **preview_text** | str | The text preview of the communication contents | [optional] |
| **recording_id** | str | A globally unique identifier for the recording associated with this chat. | [optional] |
| **segments** | [list[Segment]](Segment) | The time line of the participant&#39;s chat, divided into activity segments. | [optional] |
| **held** | bool | True if this call is held and the person on this side hears silence. | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_hold_time** | datetime | The timestamp the chat was placed on hold in the cloud clock if the chat is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **start_alerting_time** | datetime | The timestamp the communication has when it is first put into an alerting state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **provider** | str | The source provider for the social expression. | [optional] |
| **script_id** | str | The UUID of the script to use. | [optional] |
| **peer_id** | str | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **wrapup** | [Wrapup](Wrapup) | Call wrap up or disposition data. | [optional] |
| **after_call_work** | [AfterCallWork](AfterCallWork) | After-call work for the communication. | [optional] |
| **after_call_work_required** | bool | Indicates if after-call work is required for a communication. Only used when the ACW Setting is Agent Requested. | [optional] |



_PureCloudPlatformClientV2 248.0.0_

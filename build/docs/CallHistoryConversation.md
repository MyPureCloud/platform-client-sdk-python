# CallHistoryConversation

## CallHistoryConversation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **participants** | [list[CallHistoryParticipant]](CallHistoryParticipant) | The list of participants involved in the conversation. | [optional] |
| **direction** | str | The direction of the call relating to the current user | [optional] |
| **went_to_voicemail** | bool | Did the call end in the current user&#39;s voicemail | [optional] |
| **missed_call** | bool | Did the user not answer this conversation | [optional] |
| **start_time** | datetime | The time the user joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **was_conference** | bool | Was this conversation a conference | [optional] |
| **was_callback** | bool | Was this conversation a callback | [optional] |
| **had_screen_share** | bool | Did this conversation have a screen share session | [optional] |
| **had_cobrowse** | bool | Did this conversation have a cobrowse session | [optional] |
| **was_outbound_campaign** | bool | Was this conversation associated with an outbound campaign | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 241.0.0_

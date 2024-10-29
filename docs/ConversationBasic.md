# ConversationBasic

## ConversationBasic

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **external_tag** | str | The external tag associated with the conversation. | [optional] |
| **start_time** | datetime | The time when the conversation started. This will be the time when the first participant joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **end_time** | datetime | The time when the conversation ended. This will be the time when the last participant left the conversation, or null when the conversation is still active. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **divisions** | [list[ConversationDivisionMembership]](ConversationDivisionMembership) | Identifiers of divisions associated with this conversation | [optional] |
| **secure_pause** | bool | True when the recording of this conversation is in secure pause status. | [optional] |
| **utilization_label_id** | str | An optional label that categorizes the conversation.  Max-utilization settings can be configured at a per-label level | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **participants** | [list[ParticipantBasic]](ParticipantBasic) |  | [optional] |



_PureCloudPlatformClientV2 215.0.0_

# ChatConversation

## ChatConversation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **participants** | [list[ChatMediaParticipant]](ChatMediaParticipant) | The list of participants involved in the conversation. | [optional] |
| **other_media_uris** | list[str] | The list of other media channels involved in the conversation. | [optional] |
| **recent_transfers** | [list[TransferResponse]](TransferResponse) | The list of the most recent 20 transfer commands applied to this conversation. | [optional] |
| **utilization_label_id** | str | An optional label that categorizes the conversation.  Max-utilization settings can be configured at a per-label level | [optional] |
| **inactivity_timeout** | datetime | The time in the future, after which this conversation would be considered inactive. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **divisions** | [list[ConversationDivisionMembership]](ConversationDivisionMembership) | Identifiers of divisions associated with this conversation. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.1.0_

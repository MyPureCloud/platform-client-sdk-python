# CobrowseConversation

## CobrowseConversation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **participants** | [list[CobrowseMediaParticipant]](CobrowseMediaParticipant) | The list of participants involved in the conversation. | [optional] |
| **other_media_uris** | list[str] | The list of other media channels involved in the conversation. | [optional] |
| **recent_transfers** | [list[TransferResponse]](TransferResponse) | The list of the most recent 20 transfer commands applied to this conversation. | [optional] |
| **utilization_label_id** | str | An optional label that categorizes the conversation.  Max-utilization settings can be configured at a per-label level | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 221.0.0_

---
title: EmailConversation
---
## EmailConversation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **participants** | [**list[EmailMediaParticipant]**](EmailMediaParticipant.html) | The list of participants involved in the conversation. | [optional] |
| **other_media_uris** | **list[str]** | The list of other media channels involved in the conversation. | [optional] |
| **recent_transfers** | [**list[TransferResponse]**](TransferResponse.html) | The list of the most recent 20 transfer commands applied to this conversation. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



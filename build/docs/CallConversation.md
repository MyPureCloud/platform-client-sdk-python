---
title: CallConversation
---
## CallConversation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **participants** | [**list[CallMediaParticipant]**](CallMediaParticipant.html) | The list of participants involved in the conversation. | [optional] |
| **other_media_uris** | **list[str]** | The list of other media channels involved in the conversation. | [optional] |
| **recording_state** | **str** |  | [optional] |
| **max_participants** | **int** | If this is a conference conversation, then this field indicates the maximum number of participants allowed to participant in the conference. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



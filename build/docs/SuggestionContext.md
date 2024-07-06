---
title: SuggestionContext
---
## SuggestionContext

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [**AddressableEntityRef**](AddressableEntityRef.html) | The queue used to assign the interaction to the user, if any. | [optional] |
| **media_type** | **str** | The media type of the conversation in which the suggestion event was raised. | [optional] |
| **user** | [**UserReference**](UserReference.html) | The agent participant who received the raised suggestion, if any. | [optional] |
| **external_contact** | [**AddressableEntityRef**](AddressableEntityRef.html) | The external contact of the end-user participant, if any. | [optional] |
| **utterance** | [**Entity**](Entity.html) | The utterance in the voice conversation, after which the suggestion was raised, if any. | [optional] |
| **message** | [**AddressableEntityRef**](AddressableEntityRef.html) | The message in the digital conversation, after which the suggestion was raised, if any. | [optional] |
| **query_statement** | **str** | The query statement used when generating the suggestion, if any. | [optional] |
{: class="table table-striped"}



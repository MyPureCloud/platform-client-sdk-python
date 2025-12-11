# SuggestionContext

## SuggestionContext

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [AddressableEntityRef](AddressableEntityRef) | The queue used to assign the interaction to the user, if any. | [optional] |
| **media_type** | str | The media type of the conversation in which the suggestion event was raised. | [optional] |
| **user** | [UserReference](UserReference) | The agent participant who received the raised suggestion, if any. | [optional] |
| **external_contact** | [AddressableEntityRef](AddressableEntityRef) | The external contact of the end-user participant, if any. | [optional] |
| **utterance** | [Entity](Entity) | The utterance in the voice conversation, after which the suggestion was raised, if any. | [optional] |
| **message** | [AddressableEntityRef](AddressableEntityRef) | The message in the digital conversation, after which the suggestion was raised, if any. | [optional] |
| **query_statement** | str | The query statement used when generating the suggestion, if any. | [optional] |



_PureCloudPlatformClientV2 246.0.0_

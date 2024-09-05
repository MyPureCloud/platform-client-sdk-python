# DraftTopics

## DraftTopics

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Id for a topic. | |
| **name** | str | Topic name. | [optional] |
| **miner** | [Miner](Miner) | The miner to which the topic belongs. | [optional] |
| **conversation_count** | int | Number of conversations where a topic has occurred. | [optional] |
| **conversation_percent** | float | Percentage of conversations where a topic has occurred. | [optional] |
| **utterance_count** | int | Number of unique utterances where a topic has occurred. | [optional] |
| **phrase_count** | int | Number of unique phrases (sub-utterances) where a topic has occurred. | [optional] |
| **phrases** | list[str] | The phrases that are extracted for a topic. | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 210.0.0_

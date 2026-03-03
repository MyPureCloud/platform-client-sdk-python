# KnowledgeSearchPreviewRequest

## KnowledgeSearchPreviewRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **query** | str | Query to search content in the knowledge sources. | |
| **sources** | [list[V3SourceRef]](V3SourceRef) | Source information to search upon. | |
| **generation_setting** | [KnowledgeGenerationSetting](KnowledgeGenerationSetting) | Setting for answer generation. | |
| **stateful** | bool | Indicates if stateful search and generation is enabled for the knowledge setting. | [optional] |
| **conversation_turns** | [list[KnowledgeConversationTurn]](KnowledgeConversationTurn) | List of conversation turns to use for stateful search. | [optional] |



_PureCloudPlatformClientV2 252.1.0_

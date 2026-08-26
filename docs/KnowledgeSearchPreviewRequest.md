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
| **filter** | [V3SourceTagFilter](V3SourceTagFilter) | Composite tag filter applied to the search preview. | [optional] |
| **application** | [V3KnowledgeSearchPreviewClientApplication](V3KnowledgeSearchPreviewClientApplication) | The touchpoint application to simulate for the preview. | [optional] |
| **conversation_context** | [KnowledgeV3PreviewConversationContext](KnowledgeV3PreviewConversationContext) | The channel context to simulate for the preview. | [optional] |



_PureCloudPlatformClientV2 265.0.0_

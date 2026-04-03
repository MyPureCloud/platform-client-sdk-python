# KnowledgeSettingsRequest

## KnowledgeSettingsRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | Knowledge setting name. | |
| **description** | str | Knowledge setting description. | [optional] |
| **sources** | [list[V3SourceRef]](V3SourceRef) | Knowledge source information to search upon. | |
| **generation_setting** | [KnowledgeGenerationSetting](KnowledgeGenerationSetting) | Setting for answer generation. | [optional] |
| **stateful** | bool | Indicates if stateful search and generation is enabled for the knowledge setting. | [optional] |



_PureCloudPlatformClientV2 255.0.0_

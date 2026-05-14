# KnowledgeSettingsResponse

## KnowledgeSettingsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Knowledge Setting Id. | [optional] |
| **name** | str | Knowledge Setting Name. | [optional] |
| **description** | str | Knowledge setting description. | [optional] |
| **sources** | [list[V3SourceRef]](V3SourceRef) | Knowledge source information searched upon. | [optional] |
| **generation_setting** | [KnowledgeGenerationSetting](KnowledgeGenerationSetting) | Settings for answer generation. | [optional] |
| **stateful** | bool | Indicates if stateful search and generation is enabled for the knowledge setting. | [optional] |
| **date_created** | datetime | Knowledge setting created date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Knowledge setting last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [UserReference](UserReference) | The user who modified the knowledge setting. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 257.1.0_

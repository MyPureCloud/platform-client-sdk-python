# ConversationCobrowseEventTopicConversationRoutingData

## ConversationCobrowseEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [ConversationCobrowseEventTopicUriReference](ConversationCobrowseEventTopicUriReference) | A UriReference for a resource | [optional] |
| **language** | [ConversationCobrowseEventTopicUriReference](ConversationCobrowseEventTopicUriReference) | A UriReference for a resource | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[ConversationCobrowseEventTopicUriReference]](ConversationCobrowseEventTopicUriReference) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [list[ConversationCobrowseEventTopicScoredAgent]](ConversationCobrowseEventTopicScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |



_PureCloudPlatformClientV2 223.0.0_

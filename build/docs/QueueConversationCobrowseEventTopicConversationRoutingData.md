# QueueConversationCobrowseEventTopicConversationRoutingData

## QueueConversationCobrowseEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [QueueConversationCobrowseEventTopicUriReference](QueueConversationCobrowseEventTopicUriReference) | A UriReference for a resource | [optional] |
| **language** | [QueueConversationCobrowseEventTopicUriReference](QueueConversationCobrowseEventTopicUriReference) | A UriReference for a resource | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[QueueConversationCobrowseEventTopicUriReference]](QueueConversationCobrowseEventTopicUriReference) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [list[QueueConversationCobrowseEventTopicScoredAgent]](QueueConversationCobrowseEventTopicScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |



_PureCloudPlatformClientV2 212.0.0_

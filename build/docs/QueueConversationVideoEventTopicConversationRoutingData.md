# QueueConversationVideoEventTopicConversationRoutingData

## QueueConversationVideoEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [QueueConversationVideoEventTopicUriReference](QueueConversationVideoEventTopicUriReference) |  | [optional] |
| **language** | [QueueConversationVideoEventTopicUriReference](QueueConversationVideoEventTopicUriReference) | A UriReference for a resource | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[QueueConversationVideoEventTopicUriReference]](QueueConversationVideoEventTopicUriReference) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [list[QueueConversationVideoEventTopicScoredAgent]](QueueConversationVideoEventTopicScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |



_PureCloudPlatformClientV2 234.0.0_

# QueueConversationEventTopicConversationRoutingData

## QueueConversationEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [QueueConversationEventTopicUriReference](QueueConversationEventTopicUriReference) |  | [optional] |
| **language** | [QueueConversationEventTopicUriReference](QueueConversationEventTopicUriReference) | A UriReference for a resource | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[QueueConversationEventTopicUriReference]](QueueConversationEventTopicUriReference) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [list[QueueConversationEventTopicScoredAgent]](QueueConversationEventTopicScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |



_PureCloudPlatformClientV2 210.0.0_

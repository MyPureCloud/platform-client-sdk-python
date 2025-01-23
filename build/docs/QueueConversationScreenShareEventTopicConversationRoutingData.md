# QueueConversationScreenShareEventTopicConversationRoutingData

## QueueConversationScreenShareEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [QueueConversationScreenShareEventTopicUriReference](QueueConversationScreenShareEventTopicUriReference) | A UriReference for a resource | [optional] |
| **language** | [QueueConversationScreenShareEventTopicUriReference](QueueConversationScreenShareEventTopicUriReference) | A UriReference for a resource | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[QueueConversationScreenShareEventTopicUriReference]](QueueConversationScreenShareEventTopicUriReference) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [list[QueueConversationScreenShareEventTopicScoredAgent]](QueueConversationScreenShareEventTopicScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |



_PureCloudPlatformClientV2 220.0.0_

# QueueConversationMessageEventTopicConversationRoutingData

## QueueConversationMessageEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [QueueConversationMessageEventTopicUriReference](QueueConversationMessageEventTopicUriReference) | A UriReference for a resource | [optional] |
| **language** | [QueueConversationMessageEventTopicUriReference](QueueConversationMessageEventTopicUriReference) | A UriReference for a resource | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[QueueConversationMessageEventTopicUriReference]](QueueConversationMessageEventTopicUriReference) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [list[QueueConversationMessageEventTopicScoredAgent]](QueueConversationMessageEventTopicScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |



_PureCloudPlatformClientV2 246.0.0_

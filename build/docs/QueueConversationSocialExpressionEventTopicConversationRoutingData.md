# QueueConversationSocialExpressionEventTopicConversationRoutingData

## QueueConversationSocialExpressionEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [QueueConversationSocialExpressionEventTopicUriReference](QueueConversationSocialExpressionEventTopicUriReference) |  | [optional] |
| **language** | [QueueConversationSocialExpressionEventTopicUriReference](QueueConversationSocialExpressionEventTopicUriReference) | A UriReference for a resource | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[QueueConversationSocialExpressionEventTopicUriReference]](QueueConversationSocialExpressionEventTopicUriReference) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [list[QueueConversationSocialExpressionEventTopicScoredAgent]](QueueConversationSocialExpressionEventTopicScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |



_PureCloudPlatformClientV2 235.0.0_

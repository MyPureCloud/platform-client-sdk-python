# ConversationSocialExpressionEventTopicConversationRoutingData

## ConversationSocialExpressionEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [ConversationSocialExpressionEventTopicUriReference](ConversationSocialExpressionEventTopicUriReference) | A UriReference for a resource | [optional] |
| **language** | [ConversationSocialExpressionEventTopicUriReference](ConversationSocialExpressionEventTopicUriReference) | A UriReference for a resource | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[ConversationSocialExpressionEventTopicUriReference]](ConversationSocialExpressionEventTopicUriReference) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [list[ConversationSocialExpressionEventTopicScoredAgent]](ConversationSocialExpressionEventTopicScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |



_PureCloudPlatformClientV2 226.0.0_

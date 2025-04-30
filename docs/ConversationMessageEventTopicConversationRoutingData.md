# ConversationMessageEventTopicConversationRoutingData

## ConversationMessageEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [ConversationMessageEventTopicUriReference](ConversationMessageEventTopicUriReference) | A UriReference for a resource | [optional] |
| **language** | [ConversationMessageEventTopicUriReference](ConversationMessageEventTopicUriReference) | A UriReference for a resource | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[ConversationMessageEventTopicUriReference]](ConversationMessageEventTopicUriReference) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [list[ConversationMessageEventTopicScoredAgent]](ConversationMessageEventTopicScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |



_PureCloudPlatformClientV2 227.0.0_

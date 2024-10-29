# ConversationEventTopicConversationRoutingData

## ConversationEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [ConversationEventTopicUriReference](ConversationEventTopicUriReference) |  | [optional] |
| **language** | [ConversationEventTopicUriReference](ConversationEventTopicUriReference) | A UriReference for a resource | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[ConversationEventTopicUriReference]](ConversationEventTopicUriReference) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [list[ConversationEventTopicScoredAgent]](ConversationEventTopicScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |



_PureCloudPlatformClientV2 215.0.0_

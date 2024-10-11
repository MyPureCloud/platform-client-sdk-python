# ConversationVideoEventTopicConversationRoutingData

## ConversationVideoEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [ConversationVideoEventTopicUriReference](ConversationVideoEventTopicUriReference) | A UriReference for a resource | [optional] |
| **language** | [ConversationVideoEventTopicUriReference](ConversationVideoEventTopicUriReference) | A UriReference for a resource | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[ConversationVideoEventTopicUriReference]](ConversationVideoEventTopicUriReference) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [list[ConversationVideoEventTopicScoredAgent]](ConversationVideoEventTopicScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |



_PureCloudPlatformClientV2 213.0.0_

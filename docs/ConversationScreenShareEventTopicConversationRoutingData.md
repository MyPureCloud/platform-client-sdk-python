# ConversationScreenShareEventTopicConversationRoutingData

## ConversationScreenShareEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [ConversationScreenShareEventTopicUriReference](ConversationScreenShareEventTopicUriReference) | A UriReference for a resource | [optional] |
| **language** | [ConversationScreenShareEventTopicUriReference](ConversationScreenShareEventTopicUriReference) | A UriReference for a resource | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[ConversationScreenShareEventTopicUriReference]](ConversationScreenShareEventTopicUriReference) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [list[ConversationScreenShareEventTopicScoredAgent]](ConversationScreenShareEventTopicScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |



_PureCloudPlatformClientV2 236.0.0_

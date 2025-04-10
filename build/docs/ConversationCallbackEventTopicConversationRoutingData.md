# ConversationCallbackEventTopicConversationRoutingData

## ConversationCallbackEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [ConversationCallbackEventTopicUriReference](ConversationCallbackEventTopicUriReference) | A UriReference for a resource | [optional] |
| **language** | [ConversationCallbackEventTopicUriReference](ConversationCallbackEventTopicUriReference) | A UriReference for a resource | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[ConversationCallbackEventTopicUriReference]](ConversationCallbackEventTopicUriReference) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [list[ConversationCallbackEventTopicScoredAgent]](ConversationCallbackEventTopicScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |



_PureCloudPlatformClientV2 225.0.0_

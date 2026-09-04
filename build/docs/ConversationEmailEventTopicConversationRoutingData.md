# ConversationEmailEventTopicConversationRoutingData

## ConversationEmailEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [ConversationEmailEventTopicUriReference](ConversationEmailEventTopicUriReference) | A UriReference for a resource | [optional] |
| **language** | [ConversationEmailEventTopicUriReference](ConversationEmailEventTopicUriReference) | A UriReference for a resource | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[ConversationEmailEventTopicUriReference]](ConversationEmailEventTopicUriReference) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [list[ConversationEmailEventTopicScoredAgent]](ConversationEmailEventTopicScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |
| **skill_expression_id** | [ConversationEmailEventTopicUriReference](ConversationEmailEventTopicUriReference) | A UriReference for a resource | [optional] |



_PureCloudPlatformClientV2 266.0.0_

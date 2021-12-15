---
title: ConversationMessageEventTopicConversationRoutingData
---
## ConversationMessageEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [**ConversationMessageEventTopicUriReference**](ConversationMessageEventTopicUriReference.html) | A UriReference for a resource | [optional] |
| **language** | [**ConversationMessageEventTopicUriReference**](ConversationMessageEventTopicUriReference.html) | A UriReference for a resource | [optional] |
| **priority** | **int** | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [**list[ConversationMessageEventTopicUriReference]**](ConversationMessageEventTopicUriReference.html) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [**list[ConversationMessageEventTopicScoredAgent]**](ConversationMessageEventTopicScoredAgent.html) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |
{: class="table table-striped"}



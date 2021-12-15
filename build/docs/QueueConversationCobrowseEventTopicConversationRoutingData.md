---
title: QueueConversationCobrowseEventTopicConversationRoutingData
---
## QueueConversationCobrowseEventTopicConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [**QueueConversationCobrowseEventTopicUriReference**](QueueConversationCobrowseEventTopicUriReference.html) | A UriReference for a resource | [optional] |
| **language** | [**QueueConversationCobrowseEventTopicUriReference**](QueueConversationCobrowseEventTopicUriReference.html) | A UriReference for a resource | [optional] |
| **priority** | **int** | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [**list[QueueConversationCobrowseEventTopicUriReference]**](QueueConversationCobrowseEventTopicUriReference.html) | The skills to use for routing decisions | [optional] |
| **scored_agents** | [**list[QueueConversationCobrowseEventTopicScoredAgent]**](QueueConversationCobrowseEventTopicScoredAgent.html) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |
{: class="table table-striped"}



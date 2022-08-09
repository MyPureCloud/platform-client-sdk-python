---
title: RoutingData
---
## RoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue_id** | **str** | The identifier of the routing queue | |
| **language_id** | **str** | The identifier of a language to be considered in routing | [optional] |
| **priority** | **int** | The priority for routing | [optional] |
| **skill_ids** | **list[str]** | A list of skill identifiers to be considered in routing | [optional] |
| **preferred_agent_ids** | **list[str]** | A list of agents to be preferred in routing | [optional] |
| **scored_agents** | [**list[ScoredAgent]**](ScoredAgent.html) | A list of scored agents for routing decisions. For Agent Owned Callbacks use one scored agent with a score of 100. | [optional] |
| **routing_flags** | **list[str]** | An array of flags indicating how the conversation should be routed. Use \&quot;AGENT_OWNED_CALLBACK\&quot; when creating an Agent Owned Callback. | [optional] |
{: class="table table-striped"}



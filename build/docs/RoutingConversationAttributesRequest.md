---
title: RoutingConversationAttributesRequest
---
## RoutingConversationAttributesRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **priority** | **int** | Priority for the conversation.  Each point of priority is equivalent to one minute of time in queue.  Range:[-25000000, 25000000].  To reset, specify 0. | [optional] |
| **skill_ids** | **list[str]** | Skill requirements for the conversation.  To remove all skill requirements, specify an empty list, i.e. []. | [optional] |
| **language_id** | **str** | Language requirement for the conversation.  To remove the language requirement, specify an empty string, i.e., \&quot;\&quot;. | [optional] |
| **request_scored_agents** | [**list[RequestScoredAgent]**](RequestScoredAgent.html) |  | [optional] |
{: class="table table-striped"}



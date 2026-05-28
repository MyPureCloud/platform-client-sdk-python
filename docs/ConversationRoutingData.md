# ConversationRoutingData

## ConversationRoutingData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [AddressableEntityRef](AddressableEntityRef) | The queue to use for routing decisions | [optional] |
| **language** | [AddressableEntityRef](AddressableEntityRef) | The language to use for routing decisions | [optional] |
| **priority** | int | The priority of the conversation to use for routing decisions | [optional] |
| **skills** | [list[AddressableEntityRef]](AddressableEntityRef) | The skills to use for routing decisions | [optional] |
| **skill_expression** | str | The string with skill expression requested by the caller for routing decisions | [optional] |
| **skill_expression_id** | str | The internal id of the skill expression, if any, that is currently in use for routing decisions | [optional] |
| **scored_agents** | [list[ScoredAgent]](ScoredAgent) | A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents | [optional] |
| **label** | str | An optional label that categorizes the conversation.  Max-utilization settings can be configured at a per-label level | [optional] |



_PureCloudPlatformClientV2 258.0.0_

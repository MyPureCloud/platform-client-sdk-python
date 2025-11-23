# RoutingConversationAttributesResponse

## RoutingConversationAttributesResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **priority** | int | Current priority value on in-queue conversation. Range:[-25000000, 25000000] | [optional] |
| **skills** | [list[RoutingSkill]](RoutingSkill) | Current routing skills on in-queue conversation | [optional] |
| **language** | [Language](Language) | Current language on in-queue conversation | [optional] |
| **label** | [UtilizationLabel](UtilizationLabel) | Current label on in-queue conversation | [optional] |
| **scored_agents** | [list[ScoredAgent]](ScoredAgent) | Current scored agents on in-queue conversation | [optional] |



_PureCloudPlatformClientV2 244.0.0_

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
| **skill_expression** | str | Current skill expression on in-queue conversation | [optional] |
| **skill_expression_id** | str | Current skill expression ID on in-queue conversation | [optional] |



_PureCloudPlatformClientV2 263.0.0_

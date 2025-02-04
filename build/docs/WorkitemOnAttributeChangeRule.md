# WorkitemOnAttributeChangeRule

## WorkitemOnAttributeChangeRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **type** | str | The type of the rule. | [optional] |
| **action** | [WorkitemRuleAction](WorkitemRuleAction) | The rules action. If the condition criteria is met this action will be executed. | [optional] |
| **worktype** | [WorktypeReference](WorktypeReference) | The Worktype containing the rule. | [optional] |
| **condition** | [WorkitemOnAttributeChangeCondition](WorkitemOnAttributeChangeCondition) | The rules condition. If the condition criteria is met the rules action will be executed. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 221.0.0_

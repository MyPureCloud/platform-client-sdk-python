# WorkitemOnAttributeChangeRuleUpdate

## WorkitemOnAttributeChangeRuleUpdate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the rule. | [optional] |
| **condition** | [WorkitemOnAttributeChangeConditionUpdate](WorkitemOnAttributeChangeConditionUpdate) | The rules condition. If the condition criteria is met the rules action will be executed. Mutually exclusive with match; supplying either replaces the rule&#39;s existing match criteria in full. | [optional] |
| **match** | [WorkitemOnAttributeChangeMatch](WorkitemOnAttributeChangeMatch) | Grouped match criteria combined with logical operators. Mutually exclusive with condition; the supplied object replaces the rule&#39;s existing match criteria in full. | [optional] |



_PureCloudPlatformClientV2 270.0.0_

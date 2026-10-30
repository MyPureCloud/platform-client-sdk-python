# WorkitemOnAttributeChangeRuleCreate

## WorkitemOnAttributeChangeRuleCreate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the rule. | |
| **condition** | [WorkitemOnAttributeChangeCondition](WorkitemOnAttributeChangeCondition) | The rules condition. If the condition criteria is met the rules action will be executed. Mutually exclusive with match; exactly one of condition or match must be provided. | [optional] |
| **match** | [WorkitemOnAttributeChangeMatch](WorkitemOnAttributeChangeMatch) | Grouped match criteria combined with logical operators. Mutually exclusive with condition; exactly one of condition or match must be provided. | [optional] |



_PureCloudPlatformClientV2 270.0.0_

# CampaignRuleDayOfMonthParameters

## CampaignRuleDayOfMonthParameters

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **threshold_value** | str | The operand for the \&quot;before\&quot; and \&quot;after\&quot; operators, can be either exact day (1-31) or \&quot;LAST_DAY\&quot; | [optional] |
| **in_set** | list[str] | The operand for the \&quot;in\&quot; operator, each element can be either exact day (1,31) or \&quot;LAST_DAY\&quot;, \&quot;EVEN_DAY\&quot;, \&quot;ODD_DAY\&quot; | [optional] |
| **interval** | [CampaignRuleDayOfMonthInterval](CampaignRuleDayOfMonthInterval) | The interval operand for the \&quot;between\&quot; operator | [optional] |



_PureCloudPlatformClientV2 255.0.0_

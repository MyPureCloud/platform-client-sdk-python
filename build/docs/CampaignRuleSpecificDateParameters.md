# CampaignRuleSpecificDateParameters

## CampaignRuleSpecificDateParameters

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **include_year** | bool | If true, includes year in date comparison for specificDate type. When false, only month and day are compared. Default is true.  | [optional] |
| **threshold_value** | str | The operand for the \&quot;equals\&quot;, \&quot;after\&quot; and \&quot;before\&quot; operators in yyyy-MM-dd (if includeYear&#x3D;true) or MM-dd (if includeYear&#x3D;false) format. | [optional] |
| **interval** | [CampaignRuleSpecificDateInterval](CampaignRuleSpecificDateInterval) | The operand for the \&quot;between\&quot; operator | [optional] |



_PureCloudPlatformClientV2 256.0.0_

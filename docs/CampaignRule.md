# CampaignRule

## CampaignRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the CampaignRule. | |
| **date_created** | datetime | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **campaign_rule_entities** | [CampaignRuleEntities](CampaignRuleEntities) | The list of entities that this CampaignRule monitors. | |
| **campaign_rule_conditions** | [list[CampaignRuleCondition]](CampaignRuleCondition) | The list of conditions that are evaluated on the entities. | |
| **campaign_rule_actions** | [list[CampaignRuleAction]](CampaignRuleAction) | The list of actions that are executed if the conditions are satisfied. | |
| **match_any_conditions** | bool |  | [optional] |
| **enabled** | bool | Whether or not this CampaignRule is currently enabled. Required on updates. | [optional] |
| **campaign_rule_processing** | str | CampaignRule processing algorithm | [optional] |
| **condition_groups** | [list[CampaignRuleConditionGroup]](CampaignRuleConditionGroup) | List of condition groups that are evaluated, used only with campaignRuleProcessing&#x3D;\&quot;v2\&quot; | [optional] |
| **execution_settings** | [CampaignRuleExecutionSettings](CampaignRuleExecutionSettings) | CampaignRule execution settings | [optional] |
| **warnings** | [list[CampaignRuleWarning]](CampaignRuleWarning) | A list of current warning conditions associated with the campaign rule. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 230.0.0_

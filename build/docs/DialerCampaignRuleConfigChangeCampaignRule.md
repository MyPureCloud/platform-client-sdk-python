# DialerCampaignRuleConfigChangeCampaignRule

## DialerCampaignRuleConfigChangeCampaignRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **campaign_rule_entities** | [DialerCampaignRuleConfigChangeCampaignRuleEntities](DialerCampaignRuleConfigChangeCampaignRuleEntities) |  | [optional] |
| **campaign_rule_conditions** | [list[DialerCampaignRuleConfigChangeCampaignRuleCondition]](DialerCampaignRuleConfigChangeCampaignRuleCondition) | The list of conditions that will trigger this Campaign Rule | [optional] |
| **campaign_rule_actions** | [list[DialerCampaignRuleConfigChangeCampaignRuleAction]](DialerCampaignRuleConfigChangeCampaignRuleAction) | The list of actions that will be taken when this Campaign Rule&#39;s conditions are met | [optional] |
| **match_any_conditions** | bool | Whether this Campaign Rule should match any conditions (inclusive OR) or match all conditions (ALL) | [optional] |
| **enabled** | bool | Whether this campaign rule is enabled | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The UI-visible name of the object | [optional] |
| **date_created** | datetime | Creation time of the entity | [optional] |
| **date_modified** | datetime | Last modified time of the entity | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |



_PureCloudPlatformClientV2 223.0.0_

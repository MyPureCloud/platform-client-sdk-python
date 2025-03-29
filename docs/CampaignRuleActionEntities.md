# CampaignRuleActionEntities

## CampaignRuleActionEntities

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **campaigns** | [list[DomainEntityRef]](DomainEntityRef) | The list of campaigns for a CampaignRule to monitor. Required if the CampaignRule has any conditions that run on a campaign. | [optional] |
| **sequences** | [list[DomainEntityRef]](DomainEntityRef) | The list of sequences for a CampaignRule to monitor. Required if the CampaignRule has any conditions that run on a sequence. | [optional] |
| **email_campaigns** | [list[DomainEntityRef]](DomainEntityRef) | The list of Email campaigns for a CampaignRule to monitor. Required if the CampaignRule has any conditions that run on a Email campaign. | [optional] |
| **sms_campaigns** | [list[DomainEntityRef]](DomainEntityRef) | The list of SMS campaigns for a CampaignRule to monitor. Required if the CampaignRule has any conditions that run on a SMS campaign. | [optional] |
| **use_triggering_entity** | bool | If true, the CampaignRuleAction will apply to the same entity that triggered the CampaignRuleCondition. | [optional] |



_PureCloudPlatformClientV2 224.1.0_

# CampaignRuleEntities

## CampaignRuleEntities

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **campaigns** | [list[DomainEntityRef]](DomainEntityRef) | The list of campaigns for a CampaignRule to monitor. Required if the CampaignRule has any conditions that run on a campaign. | [optional] |
| **sequences** | [list[DomainEntityRef]](DomainEntityRef) | The list of sequences for a CampaignRule to monitor. Required if the CampaignRule has any conditions that run on a sequence. | [optional] |
| **email_campaigns** | [list[DomainEntityRef]](DomainEntityRef) | The list of Email campaigns for a CampaignRule to monitor. Required if the CampaignRule has any conditions that run on a Email campaign. | [optional] |
| **sms_campaigns** | [list[DomainEntityRef]](DomainEntityRef) | The list of SMS campaigns for a CampaignRule to monitor. Required if the CampaignRule has any conditions that run on a SMS campaign. | [optional] |



_PureCloudPlatformClientV2 233.0.0_

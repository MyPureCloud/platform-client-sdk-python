---
title: CampaignRuleActionEntities
---
## CampaignRuleActionEntities

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **campaigns** | [**list[UriReference]**](UriReference.html) | The list of campaigns for a CampaignRule to monitor. Required if the CampaignRule has any conditions that run on a campaign. | [optional] |
| **sequences** | [**list[UriReference]**](UriReference.html) | The list of sequences for a CampaignRule to monitor. Required if the CampaignRule has any conditions that run on a sequence. | [optional] |
| **use_triggering_entity** | **bool** | If true, the CampaignRuleAction will apply to the same entity that triggered the CampaignRuleCondition. | [optional] |
{: class="table table-striped"}



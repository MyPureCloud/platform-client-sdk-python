# CampaignRuleParameters

## CampaignRuleParameters

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **operator** | str | The operator for comparison. Required for a CampaignRuleCondition. | [optional] |
| **value** | str | The value for comparison. Required for a CampaignRuleCondition. | [optional] |
| **priority** | str | The priority to set a campaign to. Required for the &#39;setCampaignPriority&#39; action. | [optional] |
| **dialing_mode** | str | The dialing mode to set a campaign to. Required for the &#39;setCampaignDialingMode&#39; action. | [optional] |
| **abandon_rate** | float | The abandon rate to set a campaign to. Required for the &#39;setCampaignAbandonRate&#39; action. | [optional] |
| **outbound_line_count** | int | The  number of outbound lines to set a campaign to. Required for the &#39;setCampaignNumberOfLines&#39; action. | [optional] |
| **relative_weight** | int | The relative weight to set a campaign to. Required for the &#39;setCampaignWeight&#39; action. | [optional] |
| **max_calls_per_agent** | float | The maximum number of calls per agent to set a campaign to. Required for the &#39;setCampaignMaxCallsPerAgent&#39; action. | [optional] |
| **queue** | [DomainEntityRef](DomainEntityRef) | The queue a campaign to. Required for the &#39;changeCampaignQueue&#39; action. | [optional] |
| **messages_per_minute** | int | The number of messages per minute to set a messaging campaign to. | [optional] |
| **sms_messages_per_minute** | int | The number of messages per minute to set a SMS messaging campaign to. | [optional] |
| **email_messages_per_minute** | int | The number of messages per minute to set a Email messaging campaign to. | [optional] |
| **sms_content_template** | [DomainEntityRef](DomainEntityRef) | The content template to set a SMS campaign to. | [optional] |
| **email_content_template** | [DomainEntityRef](DomainEntityRef) | The content template to set a Email campaign to. | [optional] |



_PureCloudPlatformClientV2 241.0.0_

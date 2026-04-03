# CampaignRuleCondition

## CampaignRuleCondition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str |  | [optional] |
| **parameters** | [CampaignRuleParameters](CampaignRuleParameters) | The parameters for the CampaignRuleCondition. | |
| **condition_type** | str | The type of condition to evaluate. | |
| **date_time_parameters** | [CampaignRuleDateTimeConditionParameters](CampaignRuleDateTimeConditionParameters) | Parameters for conditions (timeOfDay, dayOfWeek, dayOfMonth, weekDayOfMonth and specificDate) | [optional] |
| **campaign_run_time_settings** | [CampaignRuleCampaignRunTimeSettings](CampaignRuleCampaignRunTimeSettings) | Settings for campaignRunTime conditions | [optional] |
| **campaign_wait_time_settings** | [CampaignRuleCampaignWaitTimeSettings](CampaignRuleCampaignWaitTimeSettings) | Settings for campaignWaitTime conditions | [optional] |



_PureCloudPlatformClientV2 255.0.0_

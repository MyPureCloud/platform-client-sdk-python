# CampaignDiagnostics

## CampaignDiagnostics

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **callable_contacts** | [CallableContactsDiagnostic](CallableContactsDiagnostic) | Campaign properties that can impact which contacts are callable | [optional] |
| **queue_utilization_diagnostic** | [QueueUtilizationDiagnostic](QueueUtilizationDiagnostic) | Information regarding the campaign&#39;s queue | [optional] |
| **rule_set_diagnostics** | [list[RuleSetDiagnostic]](RuleSetDiagnostic) | Information regarding the campaign&#39;s rule sets | [optional] |
| **outstanding_interactions_count** | int | Current number of outstanding interactions on the campaign | [optional] |
| **scheduled_interactions_count** | int | Current number of scheduled interactions on the campaign | [optional] |
| **time_zone_rescheduled_calls_count** | int | Current number of time zone rescheduled calls on the campaign | [optional] |
| **filtered_out_contacts_count** | int | Number of contacts that don&#39;t match filter. This is currently supported only for Campaigns with dynamic filter on. | [optional] |
| **campaign_skill_statistics** | [CampaignSkillStatistics](CampaignSkillStatistics) | Information regarding the campaign&#39;s skills | [optional] |



_PureCloudPlatformClientV2 220.0.0_

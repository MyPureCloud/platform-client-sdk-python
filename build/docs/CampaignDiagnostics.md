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
| **idle_agents** | int | Information regarding the campaign&#39;s available agents. | [optional] |
| **effective_idle_agents** | float | Information regarding the campaign&#39;s effective available agents. | [optional] |
| **lines_utilization** | [CampaignLinesUtilization](CampaignLinesUtilization) | Information on the campaign&#39;s lines utilization. | [optional] |
| **number_of_contacts_called** | int | Number of contacts called during the campaign. | [optional] |
| **total_number_of_contacts** | int | Total number of contacts in the campaign. | [optional] |
| **campaign_errors** | [list[RestErrorDetail]](RestErrorDetail) | A list of current error conditions associated with the campaign. | [optional] |
| **campaign_skill_statistics** | [CampaignSkillStatistics](CampaignSkillStatistics) | Information regarding the campaign&#39;s skills | [optional] |



_PureCloudPlatformClientV2 248.0.0_

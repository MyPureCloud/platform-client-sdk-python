# CampaignStats

## CampaignStats

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **contact_rate** | [ConnectRate](ConnectRate) | Information regarding the campaign&#39;s connect rate | [optional] |
| **idle_agents** | int | Number of available agents not currently being utilized | [optional] |
| **effective_idle_agents** | float | Number of effective available agents not currently being utilized | [optional] |
| **adjusted_calls_per_agent** | float | Calls per agent adjusted by pace | [optional] |
| **outstanding_calls** | int | Number of campaign calls currently ongoing | [optional] |
| **scheduled_calls** | int | Number of campaign calls currently scheduled | [optional] |
| **time_zone_rescheduled_calls** | int | Number of campaign calls currently timezone rescheduled | [optional] |
| **filtered_out_contacts_count** | int | Number of contacts that don&#39;t match filter. This is currently supported only for Campaigns with dynamic filter on. | [optional] |
| **right_party_contacts_count** | int | Information on the campaign&#39;s number of Right Party Contacts | [optional] |
| **valid_attempts** | int | Information on the campaign&#39;s valid attempts | [optional] |
| **lines_utilization** | [CampaignLinesUtilization](CampaignLinesUtilization) | Information on the campaign&#39;s lines utilization | [optional] |
| **business_category_metrics** | [CampaignBusinessCategoryMetrics](CampaignBusinessCategoryMetrics) | Information on the campaign&#39;s business category metrics | [optional] |



_PureCloudPlatformClientV2 224.1.0_

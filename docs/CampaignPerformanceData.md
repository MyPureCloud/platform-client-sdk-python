# CampaignPerformanceData

## CampaignPerformanceData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **campaign** | [DomainEntityRef](DomainEntityRef) | Identifier of the campaign | |
| **division** | [AddressableEntityRef](AddressableEntityRef) | The division the campaign belongs to | [optional] |
| **contact_rate** | [CampaignPerformanceDataContactRate](CampaignPerformanceDataContactRate) | Information regarding the campaign&#39;s connect rate | [optional] |
| **idle_agents** | int | Number of available agents not currently being utilized | [optional] |
| **effective_idle_agents** | float | Number of effective available agents not currently being utilized | [optional] |
| **adjusted_calls_per_agent** | float | Calls per agent adjusted by pace | [optional] |
| **outstanding_calls** | int | Number of campaign calls currently ongoing | [optional] |
| **scheduled_calls** | int | Number of campaign calls currently scheduled | [optional] |
| **right_party_contacts_count** | int | Information on the campaign&#39;s number of Right Party Contacts | [optional] |
| **campaign_status** | str | The status of the campaign | [optional] |
| **dialing_mode** | str | The strategy this Campaign will use for dialing | [optional] |
| **progress** | [CampaignPerformanceDataProgress](CampaignPerformanceDataProgress) | Information on the campaign&#39;s progress | [optional] |
| **lines_utilization** | [CampaignLinesUtilization](CampaignLinesUtilization) | Information on the campaign&#39;s lines utilization | [optional] |
| **business_category_metrics** | [CampaignBusinessCategoryMetrics](CampaignBusinessCategoryMetrics) | Information on the campaign&#39;s business category metrics | [optional] |



_PureCloudPlatformClientV2 246.1.0_

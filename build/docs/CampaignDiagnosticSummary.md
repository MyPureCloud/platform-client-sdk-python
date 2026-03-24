# CampaignDiagnosticSummary

## CampaignDiagnosticSummary

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **campaign_id** | str | Campaign ID | [optional] |
| **date_start** | datetime | Start of the interval. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_end** | datetime | End of the interval. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **campaign_states** | [list[CampaignDiagnosticCampaignState]](CampaignDiagnosticCampaignState) | Array of campaign states | [optional] |
| **campaign_info** | [list[CampaignDiagnosticWindow]](CampaignDiagnosticWindow) | Array of diagnostic windows | [optional] |
| **campaign_health_states** | [list[CampaignDiagnosticCampaignHealthState]](CampaignDiagnosticCampaignHealthState) | Array of campaign health states | [optional] |
| **config_changes** | [list[CampaignDiagnosticConfigChange]](CampaignDiagnosticConfigChange) | Configuration changes occurring within the time window | [optional] |



_PureCloudPlatformClientV2 254.0.0_

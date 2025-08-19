# CampaignPatchRequest

## CampaignPatchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **outbound_line_count** | int | The number of outbound lines to be concurrently dialed. | [optional] |
| **abandon_rate** | float | The targeted compliance abandon rate percentage | [optional] |
| **max_calls_per_agent** | float | The maximum number of calls that can be placed per agent on this campaign | [optional] |
| **dynamic_line_balancing_settings** | [DynamicLineBalancingSettingsPatchRequest](DynamicLineBalancingSettingsPatchRequest) | Dynamic line balancing settings | [optional] |
| **queue** | [AddressableEntityRef](AddressableEntityRef) | The Queue for this Campaign to route calls to. | [optional] |



_PureCloudPlatformClientV2 235.1.0_

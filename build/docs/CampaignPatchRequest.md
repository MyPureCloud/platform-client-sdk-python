---
title: CampaignPatchRequest
---
## CampaignPatchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **outbound_line_count** | **int** | The number of outbound lines to be concurrently dialed. | [optional] |
| **abandon_rate** | **float** | The targeted compliance abandon rate percentage | [optional] |
| **max_calls_per_agent** | **float** | The maximum number of calls that can be placed per agent on this campaign | [optional] |
| **dynamic_line_balancing_settings** | [**DynamicLineBalancingSettingsPatchRequest**](DynamicLineBalancingSettingsPatchRequest.html) | Dynamic line balancing settings | [optional] |
| **queue** | [**AddressableEntityRef**](AddressableEntityRef.html) | The Queue for this Campaign to route calls to. | [optional] |
{: class="table table-striped"}



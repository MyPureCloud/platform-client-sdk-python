---
title: ManagementUnitSettingsResponse
---
## ManagementUnitSettingsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **adherence** | [**AdherenceSettings**](AdherenceSettings.html) | Adherence settings for this management unit | [optional] |
| **short_term_forecasting** | [**ShortTermForecastingSettings**](ShortTermForecastingSettings.html) | Short term forecasting settings for this management unit | [optional] |
| **time_off** | [**TimeOffRequestSettings**](TimeOffRequestSettings.html) | Time off request settings for this management unit | [optional] |
| **scheduling** | [**SchedulingSettingsResponse**](SchedulingSettingsResponse.html) | Scheduling settings for this management unit. These settings are only available if you have the permission wfm:managementUnit:view | [optional] |
| **shift_trading** | [**ShiftTradeSettings**](ShiftTradeSettings.html) | Shift trade settings for this management unit | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Version info metadata for the associated management unit | |
{: class="table table-striped"}



# ManagementUnitSettingsResponse

## ManagementUnitSettingsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **adherence** | [AdherenceSettings](AdherenceSettings) | Adherence settings for this management unit | [optional] |
| **short_term_forecasting** | [ShortTermForecastingSettings](ShortTermForecastingSettings) | Short term forecasting settings for this management unit | [optional] |
| **time_off** | [TimeOffSettingsResponse](TimeOffSettingsResponse) | Time off request settings for this management unit | [optional] |
| **scheduling** | [SchedulingSettingsResponse](SchedulingSettingsResponse) | Scheduling settings for this management unit. These settings are only available if you have the permission wfm:managementUnit:view | [optional] |
| **shift_trading** | [ShiftTradeSettings](ShiftTradeSettings) | Shift trade settings for this management unit | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version info metadata for the associated management unit | |



_PureCloudPlatformClientV2 237.0.0_

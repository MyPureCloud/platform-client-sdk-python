# UpdateBusinessUnitSettingsRequest

## UpdateBusinessUnitSettingsRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_day_of_week** | str | The start day of week for this business unit | [optional] |
| **time_zone** | str | The time zone for this business unit, using the Olsen tz database format | [optional] |
| **short_term_forecasting** | [BuShortTermForecastingSettings](BuShortTermForecastingSettings) | Short term forecasting settings | [optional] |
| **scheduling** | [BuSchedulingSettingsRequest](BuSchedulingSettingsRequest) | Scheduling settings | [optional] |
| **notifications** | [BuNotificationSettingsRequest](BuNotificationSettingsRequest) | Notification settings | [optional] |
| **learning** | [BuActivitySettingsRequest](BuActivitySettingsRequest) | Learning settings | [optional] |
| **coaching** | [BuActivitySettingsRequest](BuActivitySettingsRequest) | Coaching settings | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for this business unit | |



_PureCloudPlatformClientV2 261.0.0_

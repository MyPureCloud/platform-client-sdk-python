# BusinessUnitSettingsResponse

## BusinessUnitSettingsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_day_of_week** | str | The start day of week for this business unit | |
| **time_zone** | str | The time zone for this business unit, using the Olsen tz database format | |
| **short_term_forecasting** | [BuShortTermForecastingSettings](BuShortTermForecastingSettings) | Short term forecasting settings | [optional] |
| **scheduling** | [BuSchedulingSettingsResponse](BuSchedulingSettingsResponse) | Scheduling settings | [optional] |
| **notifications** | [BuNotificationSettingsResponse](BuNotificationSettingsResponse) | Notification settings | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for this business unit | |



_PureCloudPlatformClientV2 248.0.0_

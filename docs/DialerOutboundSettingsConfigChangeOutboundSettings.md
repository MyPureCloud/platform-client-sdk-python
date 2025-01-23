# DialerOutboundSettingsConfigChangeOutboundSettings

## DialerOutboundSettingsConfigChangeOutboundSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **max_calls_per_agent** | int | The maximum number of calls that can be placed per agent on any campaign | [optional] |
| **max_line_utilization** | float | The maximum percentage of lines that should be used for Outbound, expressed as a decimal in the range [0.0, 1.0] | [optional] |
| **abandon_seconds** | float | The number of seconds used to determine if a call is abandoned | [optional] |
| **compliance_abandon_rate_denominator** | str | The denominator to be used in determining the compliance abandon rate | [optional] |
| **automatic_time_zone_mapping** | [DialerOutboundSettingsConfigChangeAutomaticTimeZoneMappingSettings](DialerOutboundSettingsConfigChangeAutomaticTimeZoneMappingSettings) |  | [optional] |
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The UI-visible name of the object | [optional] |
| **date_created** | datetime | Creation time of the entity | [optional] |
| **date_modified** | datetime | Last modified time of the entity | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |



_PureCloudPlatformClientV2 220.0.0_

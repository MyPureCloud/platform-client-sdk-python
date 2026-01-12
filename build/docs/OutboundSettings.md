# OutboundSettings

## OutboundSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **date_created** | datetime | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | int | Required for updates, must match the version number of the most recent update | [optional] |
| **max_calls_per_agent** | int | The maximum number of calls that can be placed per agent on any campaign | [optional] |
| **max_calls_per_agent_decimal** | float | The maximum number of calls that can be placed per agent on any campaign with decimal precision | [optional] |
| **max_configurable_calls_per_agent** | int | The maximum number of calls that can be configured to be placed per agent on any campaign | [optional] |
| **max_line_utilization** | float | The maximum percentage of lines that should be used for Outbound, expressed as a decimal in the range [0.0, 1.0] | [optional] |
| **abandon_seconds** | float | The number of seconds used to determine if a call is abandoned | [optional] |
| **compliance_abandon_rate_denominator** | str | The denominator to be used in determining the compliance abandon rate | [optional] |
| **automatic_time_zone_mapping** | [AutomaticTimeZoneMappingSettings](AutomaticTimeZoneMappingSettings) | The settings for automatic time zone mapping. Note that changing these settings will change them for both voice and messaging campaigns. | [optional] |
| **reschedule_time_zone_skipped_contacts** | bool | Whether or not to reschedule time-zone blocked contacts | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 247.0.0_

# AlternativeShiftBuSettingsResponse

## AlternativeShiftBuSettingsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enabled_granularities** | list[str] | The granularity at which alternative shifts is allowed. An empty list means Alternative Shifts is disabled | |
| **min_minutes_before_start_time** | int | The minimum number of minutes before the start of a shift that an alternative shift can be automatically approved | |
| **retained_activity_categories** | list[str] | Categories of activities that are required to remain at the same time slot for the alternative shifts offered. An empty list represents no retained activities | |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for this business unit&#39;s alternative shift settings | |



_PureCloudPlatformClientV2 219.0.0_

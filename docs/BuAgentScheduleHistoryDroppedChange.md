# BuAgentScheduleHistoryDroppedChange

## BuAgentScheduleHistoryDroppedChange

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **metadata** | [BuAgentScheduleHistoryChangeMetadata](BuAgentScheduleHistoryChangeMetadata) | The metadata of the change, including who and when the change was made | [optional] |
| **shift_ids** | list[str] | The IDs of deleted shifts | [optional] |
| **full_day_time_off_marker_dates** | list[date] | The dates of any deleted full day time off markers | [optional] |
| **deletes** | [BuAgentScheduleHistoryDeletedChange](BuAgentScheduleHistoryDeletedChange) | The deleted shifts, full day time off markers, or the entire agent schedule | [optional] |



_PureCloudPlatformClientV2 210.0.0_

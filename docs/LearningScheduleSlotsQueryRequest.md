# LearningScheduleSlotsQueryRequest

## LearningScheduleSlotsQueryRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **interval** | str | Range of time to get slots for scheduling learning activities. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **length_in_minutes** | int | The duration of Learning Assignment to schedule in 15 minutes granularity | |
| **user_ids** | list[str] | The user IDs for which to fetch schedules. Must be only 1. | |
| **interruptible_assignment_id** | str | Assignment ID to exclude from consideration when determining blocked slots | [optional] |



_PureCloudPlatformClientV2 238.0.0_

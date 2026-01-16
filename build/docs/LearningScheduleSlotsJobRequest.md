# LearningScheduleSlotsJobRequest

## LearningScheduleSlotsJobRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user_ids** | list[str] | The user IDs to fetch the slots for. | |
| **length_in_minutes** | int | The length in minutes of the slots, in 15 minutes granularity. | |
| **activity_code_id** | str | The Activity Code Id of the slots. | |
| **intervals** | list[str] | The intervals to fetch the slots for. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **slots_type** | str | The type of slots to fetch in the job. | |



_PureCloudPlatformClientV2 248.0.0_

# CoachingScheduleSlotsJobResult

## CoachingScheduleSlotsJobResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **interval** | str | The interval of the job. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional] |
| **status** | str | The status of the job | [optional] |
| **slot** | [CoachingScheduleSlotsJobSlot](CoachingScheduleSlotsJobSlot) | The slot found from the job | [optional] |
| **has_conflict** | bool | True if the slot conflicts with a Coaching Appointment | [optional] |



_PureCloudPlatformClientV2 248.0.0_

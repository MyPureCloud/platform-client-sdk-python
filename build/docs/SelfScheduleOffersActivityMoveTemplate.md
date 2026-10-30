# SelfScheduleOffersActivityMoveTemplate

## SelfScheduleOffersActivityMoveTemplate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **schedule** | [BuScheduleReference](BuScheduleReference) | The schedule associated with the shift the agent wants to edit. | |
| **shift_id** | str | The ID of the shift to which the self-schedule activity move is associated | |
| **reference_key** | str | The unique identifier for the offered shift edit that was used for this shift edit | |
| **start_date** | datetime | The start date/time for the shift in ISO-8601 format | |
| **length_minutes** | int | The duration of this shift in minutes | |
| **activity_code** | [ActivityCodeReference](ActivityCodeReference) | The activity related to this shift | |
| **alternate_start_dates** | list[datetime] | The alternative start dates for this shift | |



_PureCloudPlatformClientV2 270.0.0_

# ScheduleGenerationWarning

## ScheduleGenerationWarning

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user_id** | str | ID of the user in the warning | [optional] |
| **user_not_licensed** | bool | Whether the user does not have the appropriate license to be scheduled | [optional] |
| **unable_to_meet_max_days** | bool | Whether the number of scheduled days exceeded the maximum days to schedule defined in the agent work plan | [optional] |
| **unable_to_schedule_required_days** | list[str] | Days indicated as required to work in agent work plan where no viable shift was found to schedule | [optional] |
| **unable_to_meet_min_paid_for_the_week** | bool | Whether the schedule did not meet the minimum paid time for the week defined in the agent work plan | [optional] |
| **unable_to_meet_max_paid_for_the_week** | bool | Whether the schedule exceeded the maximum paid time for the week defined in the agent work plan | [optional] |
| **no_need_days** | list[str] | Days agent was scheduled but there was no need to meet. The scheduled days have no effect on service levels | [optional] |
| **shifts_too_close_together** | bool | Whether the schedule did not meet the minimum time between shifts defined in the agent work plan | [optional] |



_PureCloudPlatformClientV2 219.1.0_

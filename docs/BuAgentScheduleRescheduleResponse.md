# BuAgentScheduleRescheduleResponse

## BuAgentScheduleRescheduleResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user** | [UserReference](UserReference) | The user to whom this agent schedule applies | [optional] |
| **shifts** | [list[BuAgentScheduleShift]](BuAgentScheduleShift) | The shift definitions for this agent schedule | [optional] |
| **full_day_time_off_markers** | [list[BuFullDayTimeOffMarker]](BuFullDayTimeOffMarker) | Full day time off markers which apply to this agent schedule | [optional] |
| **work_plan** | [WorkPlanReference](WorkPlanReference) | The work plan for this user | [optional] |
| **work_plans_per_week** | [list[WorkPlanReference]](WorkPlanReference) | The work plans per week for this user from the work plan rotation. Null values in the list denotes that user is not part of any work plan for that week | [optional] |



_PureCloudPlatformClientV2 238.0.0_

# CreateActivityPlanRequest

## CreateActivityPlanRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the activity plan | |
| **management_unit_ids** | list[str] | The management units to which this activity plan applies. Empty list or null means this activity plan applies to the entire business unit | [optional] |
| **description** | str | The description of the activity plan | [optional] |
| **activity_code_id** | str | The activity code associated with the activity plan | |
| **type** | str | The type of the activity plan | |
| **length_minutes** | int | The length in minutes of the activity plan | |
| **initial_schedule_period** | [SchedulingPeriod](SchedulingPeriod) | The initial scheduling period for the activity plan | |
| **group_settings** | [GroupSettings](GroupSettings) | Group settings for the activity plan | [optional] |
| **recurrence_settings** | [RecurrenceSettings](RecurrenceSettings) | Settings controlling recurrence for the activity plan. If not set the activity plan will only occur once | [optional] |
| **attendees_search_rule** | [UserSearchRule](UserSearchRule) | Attendee search rule for this activity plan | [optional] |
| **facilitated** | bool | Whether the sessions created by this activity plan should be facilitated | [optional] |
| **facilitators_search_rule** | [UserSearchRule](UserSearchRule) | Facilitator search rule for this activity plan | [optional] |
| **transition_time_minutes** | int | Transition time in minutes between facilitated sessions | |
| **service_goal_impact_overrides** | [ActivityPlanServiceGoalImpactOverrides](ActivityPlanServiceGoalImpactOverrides) | Allowable service goal impact override settings for this activity plan. If not set the business unit setting will be used | [optional] |
| **optimization_objective** | str | The optimization objective of this activity plan | |
| **state** | str | The state of this activity plan | |
| **counts_as_paid_time** | bool | Whether the activity should count as paid time | |
| **fixed_availability** | [list[FixedAvailability]](FixedAvailability) | Fixed availability configuration for the activity plan | [optional] |



_PureCloudPlatformClientV2 227.1.0_

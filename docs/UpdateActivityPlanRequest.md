# UpdateActivityPlanRequest

## UpdateActivityPlanRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the activity plan | [optional] |
| **description** | str | The description of the activity plan | [optional] |
| **group_settings** | [ValueWrapperGroupSettings](ValueWrapperGroupSettings) | Group settings for the activity plan | [optional] |
| **attendees_search_rule** | [ValueWrapperUserSearchRule](ValueWrapperUserSearchRule) | Attendee search rule for this activity plan | [optional] |
| **facilitators_search_rule** | [ValueWrapperUserSearchRule](ValueWrapperUserSearchRule) | Facilitator search rule for this activity plan | [optional] |
| **transition_time_minutes** | int | Transition time in minutes between facilitated sessions | [optional] |
| **service_goal_impact_overrides** | [ValueWrapperActivityPlanServiceGoalImpactOverrides](ValueWrapperActivityPlanServiceGoalImpactOverrides) | Allowable service goal impact override settings for this activity plan | [optional] |
| **optimization_objective** | str | The optimization objective of this activity plan | [optional] |
| **state** | str | The state of this activity plan | [optional] |
| **fixed_availability** | [ListWrapperFixedAvailability](ListWrapperFixedAvailability) | Fixed availability configuration for the activity plan | [optional] |
| **activity_code_id** | str | The activity code associated with the activity plan | [optional] |
| **type** | str | The type of the activity plan | [optional] |
| **length_minutes** | int | The length in minutes of the activity plan | [optional] |
| **counts_as_paid_time** | bool | Whether the activity should count as paid time | [optional] |
| **recurrence_settings** | [RecurrenceSettingsBase](RecurrenceSettingsBase) | Settings controlling recurrence for the activity plan. If not set the activity plan will only occur once | [optional] |



_PureCloudPlatformClientV2 264.0.0_

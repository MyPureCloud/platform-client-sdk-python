# ActivityPlanResponse

## ActivityPlanResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the activity plan | |
| **management_units** | [list[ManagementUnitReference]](ManagementUnitReference) | The management units to which this activity plan applies. Empty list or null means this activity plan applies to the entire business unit | [optional] |
| **description** | str | The description of this activity plan | |
| **activity_code** | [ActivityCodeReference](ActivityCodeReference) | The activity code associated with this activity plan. It is recommended to load and cache the entire list of activity codes rather than look up individual codes | |
| **type** | str | The type of the activity plan | |
| **initial_schedule_period** | [SchedulingPeriod](SchedulingPeriod) | The initial schedule period of the activity plan | |
| **length_minutes** | int | The length of the activity in minutes | |
| **group_settings** | [GroupSettings](GroupSettings) | Group settings for this activity plan | [optional] |
| **recurrence_settings** | [RecurrenceSettings](RecurrenceSettings) | Recurrence settings for this activity plan | [optional] |
| **attendees_search_rule** | [UserSearchRule](UserSearchRule) | Attendee search rule for this activity plan | [optional] |
| **facilitated** | bool | Whether the sessions created by this activity plan should be facilitated | |
| **facilitators_search_rule** | [UserSearchRule](UserSearchRule) | Facilitator search rule for this activity plan | [optional] |
| **transition_time_minutes** | int | Transition time in minutes between facilitated sessions | |
| **service_goal_impact_overrides** | [ActivityPlanServiceGoalImpactOverrides](ActivityPlanServiceGoalImpactOverrides) | Allowable service goal impact override settings for this activity plan | [optional] |
| **optimization_objective** | str | The optimization objective of this activity plan | |
| **fixed_availability** | [list[FixedAvailability]](FixedAvailability) | Fixed availability configuration for this activity plan | [optional] |
| **state** | str | The state of this activity plan | |
| **counts_as_paid_time** | bool | Whether the activity should count as paid time | |
| **created_date** | datetime | The date the activity plan was created, in ISO-8601 format | |
| **created_by** | [UserReference](UserReference) | The user who created this activity plan | |
| **modified_date** | datetime | The date the activity plan was modified, in ISO-8601 format | |
| **modified_by** | [UserReference](UserReference) | The last user to modify this activity plan. The id may be &#39;System&#39; if it was an automated process | |
| **last_run_date** | datetime | The date on which the activity plan was last manually run, in ISO-8601 format | [optional] |
| **last_run_by** | [UserReference](UserReference) | The last user to run this activity plan | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 239.0.0_

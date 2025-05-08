# ActivityPlanListItem

## ActivityPlanListItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the activity plan | |
| **management_units** | [list[ManagementUnitReference]](ManagementUnitReference) | The management units to which this activity plan applies. Empty list or null means this activity plan applies to all management units in the business unit | [optional] |
| **description** | str | The description of this activity plan | |
| **activity_code** | [ActivityCodeReference](ActivityCodeReference) | The activity code to which this activity plan applies. Note: It is recommended to load and cache the entire list of activity codes rather than look up individual codes | |
| **type** | str | The type of the activity plan | |
| **optimization_objective** | str | The optimization objective of this activity plan | |
| **recurrence_settings** | [RecurrenceSettings](RecurrenceSettings) | Recurrence settings for this activity plan | [optional] |
| **state** | str | The state of this activity plan | |
| **last_run_date** | datetime | The date the activity plan was last run, in ISO-8601 format | [optional] |
| **last_run_by** | [UserReference](UserReference) | The last user to run this activity plan | [optional] |
| **created_date** | datetime | The date the activity plan was created, in ISO-8601 format | |
| **created_by** | [UserReference](UserReference) | The user who created this activity plan | |
| **modified_date** | datetime | The date the activity plan was modified, in ISO-8601 format | |
| **modified_by** | [UserReference](UserReference) | The last user to modify this activity plan. The id may be &#39;System&#39; if it was an automated process | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 227.1.0_

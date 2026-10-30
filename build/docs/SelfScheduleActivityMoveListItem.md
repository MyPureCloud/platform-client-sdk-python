# SelfScheduleActivityMoveListItem

## SelfScheduleActivityMoveListItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | |
| **schedule** | [BuScheduleReference](BuScheduleReference) | The schedule to which the shift and activity are associated | |
| **shift_id** | str | The ID of the shift to which this activity is associated | |
| **state** | str | The state of the self-schedule operation | |
| **workflow_status** | str | The processing status of this self-schedule operation | [optional] |
| **start_date** | datetime | The original start date of this activity in ISO-8601 format | |
| **new_date** | datetime | The new start date of this activity in ISO-8601 format | |
| **length_minutes** | int | The length of this activity in minutes | |
| **activity_code** | [ActivityCodeReference](ActivityCodeReference) | The activity code related to this shift | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 270.0.0_

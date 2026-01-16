# UpdateActivityCodeRequest

## UpdateActivityCodeRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the activity code | [optional] |
| **category** | str | The activity code&#39;s category. Attempting to change the category of a default activity code will return an error | [optional] |
| **length_in_minutes** | int | The default length of the activity in minutes | [optional] |
| **counts_as_paid_time** | bool | Whether an agent is paid while performing this activity | [optional] |
| **counts_as_work_time** | bool | Indicates whether or not the activity should be counted as work time | [optional] |
| **agent_time_off_selectable** | bool | Whether an agent can select this activity code when creating or editing a time off request | [optional] |
| **counts_toward_shrinkage** | bool | Whether or not this activity code counts toward shrinkage calculations | [optional] |
| **planned_shrinkage** | bool | Whether this activity code is considered planned or unplanned shrinkage | [optional] |
| **interruptible** | bool | Whether this activity code is considered interruptible | [optional] |
| **secondary_presences** | [ListWrapperSecondaryPresence](ListWrapperSecondaryPresence) | The secondary presences of this activity code | [optional] |
| **planning_group_ids** | [ListWrapperString](ListWrapperString) | The planning group IDs associated with this activity code | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for the associated business unit&#39;s list of activity codes | |



_PureCloudPlatformClientV2 248.0.0_

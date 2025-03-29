# BusinessUnitActivityCode

## BusinessUnitActivityCode

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **active** | bool | Whether this activity code is active or has been deleted | [optional] |
| **default_code** | bool | Whether this is a default activity code | [optional] |
| **category** | str | The category of the activity code | [optional] |
| **length_in_minutes** | int | The default length of the activity in minutes | [optional] |
| **counts_as_paid_time** | bool | Whether an agent is paid while performing this activity | [optional] |
| **counts_as_work_time** | bool | Indicates whether or not the activity should be counted as contiguous work time for calculating daily constraints | [optional] |
| **agent_time_off_selectable** | bool | Whether an agent can select this activity code when creating or editing a time off request. Null if the activity&#39;s category is not time off. | [optional] |
| **counts_toward_shrinkage** | bool | Whether or not this activity code counts toward shrinkage calculations | [optional] |
| **planned_shrinkage** | bool | Whether this activity code is considered planned or unplanned shrinkage | [optional] |
| **interruptible** | bool | Whether this activity code is considered interruptible | [optional] |
| **secondary_presences** | [list[SecondaryPresence]](SecondaryPresence) | The secondary presences of this activity code | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata of this activity code | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 224.1.0_

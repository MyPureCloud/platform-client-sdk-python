# BuQueryAgentSchedulesRequest

## BuQueryAgentSchedulesRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **management_unit_id** | str | The ID of the management unit to query | |
| **user_ids** | list[str] | The IDs of the users to query.  Omit to query all user schedules in the management unit. Note: If teamIds is also specified, only schedules for users in the requested teams will be returned | [optional] |
| **team_ids** | list[str] | The teamIds to request. If null or not set, results will be queried for requested users if applicable or otherwise all users in the management unit | [optional] |



_PureCloudPlatformClientV2 214.0.0_

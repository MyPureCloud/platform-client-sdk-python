# TimeOffRequestQueryBody

## TimeOffRequestQueryBody

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **ids** | list[str] | The set of ids to filter time off requests | [optional] |
| **user_ids** | list[str] | The set of user ids to filter time off requests. Omit to query all users in the management unit. Note: If teamIds is also specified, only time off requests for users in the requested teams will be returned | [optional] |
| **statuses** | list[str] | The set of statuses to filter time off requests | [optional] |
| **substatuses** | list[str] | The set of substatuses to filter time off requests | [optional] |
| **date_range** | [DateRange](DateRange) | The inclusive range of dates to filter time off requests | [optional] |
| **team_ids** | list[str] | The IDs of work teams to query. If null or not set, results will be queried for requested users if applicable or otherwise all users in the management unit | [optional] |



_PureCloudPlatformClientV2 268.0.0_

# BuManagementUnitScheduleSummary

## BuManagementUnitScheduleSummary

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **management_unit** | [ManagementUnitReference](ManagementUnitReference) | The management unit to which this summary applies | [optional] |
| **agent_count** | int | The number of agents from this management unit that are in the schedule | [optional] |
| **start_date** | datetime | The start of the schedule change in the management unit. Only populated in schedule update notifications. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **end_date** | datetime | The end of the schedule change in the management unit. Only populated in schedule update notifications. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **agents** | [list[UserReference]](UserReference) | The agents in the management unit who are part of this schedule, or in schedule change notifications, the agents that were changed. Note this will come back as an empty list unless the appropriate expand query parameter is passed | [optional] |



_PureCloudPlatformClientV2 249.0.0_

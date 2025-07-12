# MuAgentsWorkPlansResult

## MuAgentsWorkPlansResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **entities** | [list[AgentWorkPlans]](AgentWorkPlans) |  | [optional] |
| **reference_start_week_date** | date | The reference date in yyyy-MM-dd format rolled back to nearest BU start day of week. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **work_plan_lookup** | [dict(str, WorkPlanReference)](WorkPlanReference) | Map containing lookup values for agent work plans. The integer keys serves as lookup keys for effective work plan from workPlanLookupKeysPerWeek property | |



_PureCloudPlatformClientV2 233.0.0_

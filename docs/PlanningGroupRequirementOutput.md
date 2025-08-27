# PlanningGroupRequirementOutput

## PlanningGroupRequirementOutput

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the planning group to which this output applies | |
| **intervals** | list[int] | List of interval values that correspond with the requirements granularity that was requested | [optional] |
| **error_details** | [list[LongTermRequirementsErrorDetail]](LongTermRequirementsErrorDetail) | Error details if the intervals cannot be provided for this planning group because of missing data or internal error | [optional] |
| **service_goal_details** | [LongTermRequirementsServiceGoalDetail](LongTermRequirementsServiceGoalDetail) | The service goal details used to generate the requirements | [optional] |



_PureCloudPlatformClientV2 236.0.0_

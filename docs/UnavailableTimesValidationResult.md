# UnavailableTimesValidationResult

## UnavailableTimesValidationResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **valid** | bool | Indicates whether there are no violations in the given unavailable times | |
| **invalid_work_plans** | [list[WorkPlanReference]](WorkPlanReference) | Invalid work plans that were used when validating the agents unavailable times | |
| **work_plan_constraints_violation_message** | [WorkPlanConstraintsViolationMessage](WorkPlanConstraintsViolationMessage) | Message for set of agent unavailable times violating work plan constraints | [optional] |



_PureCloudPlatformClientV2 249.0.0_

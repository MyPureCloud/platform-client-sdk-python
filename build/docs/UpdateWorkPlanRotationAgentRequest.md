# UpdateWorkPlanRotationAgentRequest

## UpdateWorkPlanRotationAgentRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user_id** | str | The ID of an agent in this work plan rotation | |
| **date_range** | [DateRangeWithOptionalEnd](DateRangeWithOptionalEnd) | The date range to which this agent is effective in the work plan rotation | [optional] |
| **position** | int | Start position of the work plan in the pattern for this agent in the work plan rotation. Position value starts from 0 | [optional] |
| **delete** | bool | If marked true for this agent when updating, then this agent will be removed from this work plan rotation | [optional] |



_PureCloudPlatformClientV2 242.0.0_

# AddWorkPlanRotationRequest

## AddWorkPlanRotationRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | Name of this work plan rotation | |
| **date_range** | [DateRangeWithOptionalEnd](DateRangeWithOptionalEnd) | The date range to which this work plan rotation applies | |
| **agents** | [list[AddWorkPlanRotationAgentRequest]](AddWorkPlanRotationAgentRequest) | Agents in this work plan rotation | [optional] |
| **pattern** | [WorkPlanPatternRequest](WorkPlanPatternRequest) | Pattern with list of work plan IDs that rotate on a weekly basis | |



_PureCloudPlatformClientV2 220.0.0_

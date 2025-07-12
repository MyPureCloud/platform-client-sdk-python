# UpdateWorkPlanRotationRequest

## UpdateWorkPlanRotationRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | Name of this work plan rotation | [optional] |
| **enabled** | bool | Whether the work plan rotation is enabled for scheduling | [optional] |
| **date_range** | [DateRangeWithOptionalEnd](DateRangeWithOptionalEnd) | The date range to which this work plan rotation applies | [optional] |
| **agents** | [list[UpdateWorkPlanRotationAgentRequest]](UpdateWorkPlanRotationAgentRequest) | Agents in this work plan rotation | [optional] |
| **pattern** | [WorkPlanPatternRequest](WorkPlanPatternRequest) | Pattern with list of work plan IDs that rotate on a weekly basis | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for this work plan rotation | |



_PureCloudPlatformClientV2 233.0.0_

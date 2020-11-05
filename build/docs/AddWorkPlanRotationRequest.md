---
title: AddWorkPlanRotationRequest
---
## AddWorkPlanRotationRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | Name of this work plan rotation | |
| **date_range** | [**DateRangeWithOptionalEnd**](DateRangeWithOptionalEnd.html) | The date range to which this work plan rotation applies | |
| **agents** | [**list[AddWorkPlanRotationAgentRequest]**](AddWorkPlanRotationAgentRequest.html) | Agents in this work plan rotation | [optional] |
| **pattern** | [**WorkPlanPatternRequest**](WorkPlanPatternRequest.html) | Pattern with list of work plan IDs that rotate on a weekly basis | |
{: class="table table-striped"}



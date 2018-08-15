---
title: AnalyticsFlow
---
## AnalyticsFlow

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **flow_id** | **str** | The unique identifier of this flow | [optional] |
| **flow_name** | **str** | The name of this flow | [optional] |
| **flow_version** | **str** | The version of this flow | [optional] |
| **flow_type** | **str** | The type of this flow | [optional] |
| **exit_reason** | **str** | The exit reason for this flow, e.g. DISCONNECT | [optional] |
| **transfer_type** | **str** | The type of transfer for flows that ended with a transfer | [optional] |
| **transfer_target_name** | **str** | The name of a transfer target | [optional] |
| **transfer_target_address** | **str** | The address of a transfer target | [optional] |
| **issued_callback** | **bool** | Flag indicating whether the flow issued a callback | [optional] |
| **starting_language** | **str** | Flow starting language, e.g. en-us | [optional] |
| **ending_language** | **str** | Flow ending language, e.g. en-us | [optional] |
| **outcomes** | [**list[AnalyticsFlowOutcome]**](AnalyticsFlowOutcome.html) | Flow outcomes | [optional] |
{: class="table table-striped"}



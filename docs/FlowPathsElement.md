# FlowPathsElement

## FlowPathsElement

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **parent_id** | str | Unique identifier of the parent element. Will be null for the root element. | [optional] |
| **type** | str | Type of the element. | |
| **count** | int | Count of all journeys that include this element. | |
| **flows** | [list[FlowPathsFlowDetails]](FlowPathsFlowDetails) | Details of flows involved in journeys that include this element. | |
| **flow_outcome_value** | str | The value of the flow outcome, if the element type is Outcome. | [optional] |
| **flow_milestone** | [AddressableEntityRef](AddressableEntityRef) | The flow milestone, set if the element type is Milestone. | [optional] |
| **flow_outcome** | [AddressableEntityRef](AddressableEntityRef) | The flow outcome, set if the element type is Outcome or Milestone. | [optional] |



_PureCloudPlatformClientV2 242.0.0_

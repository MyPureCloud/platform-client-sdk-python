# AnalyticsFlow

## AnalyticsFlow

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **ending_language** | str | Flow ending language, e.g. en-us | [optional] |
| **entry_reason** | str | The particular entry reason for this flow, e.g. an address, userId, or flowId | [optional] |
| **entry_type** | str | The entry type for this flow, e.g. dnis, dialer, agent, flow, or direct | [optional] |
| **exit_reason** | str | The exit reason for this flow, e.g. DISCONNECT | [optional] |
| **flow_id** | str | The unique identifier of this flow | [optional] |
| **flow_name** | str | The name of this flow at the time of flow execution | [optional] |
| **flow_type** | str | The type of this flow | [optional] |
| **flow_version** | str | The version of this flow | [optional] |
| **issued_callback** | bool | Flag indicating whether the flow issued a callback | [optional] |
| **recognition_failure_reason** | str | The recognition failure reason causing to exit/disconnect | [optional] |
| **starting_language** | str | Flow starting language, e.g. en-us | [optional] |
| **transfer_target_address** | str | The address of a flow transfer target, e.g. a phone number, an email address, or a queueId | [optional] |
| **transfer_target_name** | str | The name of a flow transfer target | [optional] |
| **transfer_type** | str | The type of transfer for flows that ended with a transfer | [optional] |
| **outcomes** | [list[AnalyticsFlowOutcome]](AnalyticsFlowOutcome) | Flow outcomes | [optional] |



_PureCloudPlatformClientV2 235.0.0_

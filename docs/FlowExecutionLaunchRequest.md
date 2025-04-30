# FlowExecutionLaunchRequest

## FlowExecutionLaunchRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **flow_id** | str | ID of the flow to launch. | |
| **flow_version** | str | The version of the flow to launch. Omit this value (or supply null/empty) to use the latest published version. | [optional] |
| **input_data** | dict(str, object) | Input values to the flow. Valid values are defined by a flow&#39;s input JSON schema. | [optional] |
| **name** | str | A displayable name to assign to the new flow execution | [optional] |



_PureCloudPlatformClientV2 227.0.0_

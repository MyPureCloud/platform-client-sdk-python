# AgenticVirtualAgentToolInput

## AgenticVirtualAgentToolInput

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **target_name** | str | The unique name that identifies this input parameter within the tool | |
| **type** | str | Input type name. The valid referenced type depends on the input source. | |
| **source** | str | Source of the input value. | |
| **required** | bool | Whether this input must be supplied. | [optional] |
| **fallback_to_user** | bool | Whether the virtual agent should ask the user for this input value when it is not available from the configured source. | [optional] |
| **mapping** | list[object] | Path used to extract this input from a previous tool output. Only valid when source is &#39;ToolOutput&#39;. The path starts with a tool output type name, may contain only string property names or integer array indexes, and must resolve to a primitive value. | [optional] |



_PureCloudPlatformClientV2 269.0.0_

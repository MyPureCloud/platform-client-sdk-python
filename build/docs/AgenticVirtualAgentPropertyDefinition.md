# AgenticVirtualAgentPropertyDefinition

## AgenticVirtualAgentPropertyDefinition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | Property name. | |
| **type** | str | Property type name. The valid type depends on the containing type and related fields. | |
| **required** | bool | Whether this property must be supplied. | [optional] |
| **description** | str | Additional context that helps the virtual agent understand what this property means. | [optional] |
| **items** | str | Type of items in this array property. Applies when type is array. | [optional] |
| **mapping** | list[object] | Path used to extract this output data property from a tool output. Only valid for output data properties. The path starts with a tool output type name, may contain only string property names or integer array indexes, and must resolve to a primitive value. | [optional] |



_PureCloudPlatformClientV2 266.0.0_

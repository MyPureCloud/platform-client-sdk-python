# AgenticVirtualAgentTypeDefinition

## AgenticVirtualAgentTypeDefinition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | Type name. | |
| **description** | str | Additional context that helps the virtual agent understand what this type is used for. | [optional] |
| **direction** | str | Intended direction of use for this type. | [optional] |
| **type** | str | Type value. The applicable fields depend on this value and related fields. | [optional] |
| **user_utterance_substring** | bool | Whether values of this string type must be copied as a contiguous substring from recent user messages. | [optional] |
| **undisclosed** | bool | Whether values of this string type are hidden from the virtual agent and represented as opaque identifiers. Only valid when type is string. | [optional] |
| **properties** | [list[AgenticVirtualAgentPropertyDefinition]](AgenticVirtualAgentPropertyDefinition) | Properties of this object type. Applies when type is object. | [optional] |
| **items** | str | Type of items in this array type. Applies when type is array. | [optional] |
| **status_codes** | list[int] | HTTP 4xx or 5xx status codes this error type can handle. Applies when type is DataActionHttpError. | [optional] |
| **default_instruction** | str | Default instruction for how the virtual agent should handle this error type when a tool references it without its own error instruction. Applies when type is DataActionHttpError. | [optional] |
| **enum** | list[str] | Allowed enum values. Applies to enum types. | [optional] |



_PureCloudPlatformClientV2 266.0.0_

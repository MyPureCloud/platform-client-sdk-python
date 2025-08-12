# Flow

## Flow

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The flow identifier | [optional] |
| **name** | str | The flow name | |
| **division** | [WritableDivision](WritableDivision) | The division to which this entity belongs. | [optional] |
| **description** | str |  | [optional] |
| **type** | str |  | [optional] |
| **locked_user** | [User](User) | User that has the flow locked. | [optional] |
| **locked_client** | [DomainEntityRef](DomainEntityRef) | OAuth client that has the flow locked. | [optional] |
| **active** | bool |  | [optional] |
| **system** | bool |  | [optional] |
| **deleted** | bool |  | [optional] |
| **published_version** | [FlowVersion](FlowVersion) |  | [optional] |
| **saved_version** | [FlowVersion](FlowVersion) |  | [optional] |
| **input_schema** | object | json schema describing the inputs for the flow | [optional] |
| **output_schema** | object | json schema describing the outputs for the flow | [optional] |
| **checked_in_version** | [FlowVersion](FlowVersion) |  | [optional] |
| **debug_version** | [FlowVersion](FlowVersion) |  | [optional] |
| **published_by** | [User](User) |  | [optional] |
| **current_operation** | [Operation](Operation) |  | [optional] |
| **nlu_info** | [NluInfo](NluInfo) | Information about the natural language understanding configuration for the published version of the flow | [optional] |
| **supported_languages** | [list[SupportedLanguage]](SupportedLanguage) | List of supported languages for the published version of the flow. | [optional] |
| **compatible_flow_types** | list[str] | Compatible flow types designate which flow types are allowed to embed a flow’s configuration within their own flow configuration.  Currently the only flows that can be embedded are Common Module flows and the embedding flow can invoke them using the Call Common Module action. | [optional] |
| **worktype_id** | str |  | [optional] |
| **virtual_agent_enabled** | bool |  | [optional] |
| **agentic_virtual_agent_enabled** | bool |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.0.0_

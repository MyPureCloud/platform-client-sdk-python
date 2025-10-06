# FlowVersion

## FlowVersion

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The flow version identifier | [optional] |
| **name** | str |  | [optional] |
| **commit_version** | str |  | [optional] |
| **configuration_version** | str |  | [optional] |
| **type** | str |  | [optional] |
| **secure** | bool |  | [optional] |
| **debug** | bool |  | [optional] |
| **created_by** | [User](User) |  | [optional] |
| **created_by_client** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **configuration_uri** | str |  | [optional] |
| **date_created** | int |  | [optional] |
| **date_checked_in** | int |  | [optional] |
| **date_saved** | int |  | [optional] |
| **generation_id** | str |  | [optional] |
| **publish_result_uri** | str |  | [optional] |
| **input_schema** | [JsonSchemaDocument](JsonSchemaDocument) |  | [optional] |
| **output_schema** | [JsonSchemaDocument](JsonSchemaDocument) |  | [optional] |
| **virtual_agent_enabled** | bool |  | [optional] |
| **agentic_virtual_agent_enabled** | bool |  | [optional] |
| **date_published** | datetime | The date this version became the published version of the flow. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_published_end** | datetime | The date this version was no longer the published version of the flow. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **nlu_info** | [NluInfo](NluInfo) | Information about the natural language understanding configuration for the flow version | [optional] |
| **supported_languages** | [list[SupportedLanguage]](SupportedLanguage) | List of supported languages for this version of the flow | [optional] |
| **compatible_flow_types** | list[str] | Compatible flow types designate which flow types are allowed to embed a flow’s configuration within their own flow configuration.  Currently the only flows that can be embedded are Common Module flows and the embedding flow can invoke them using the Call Common Module action. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 240.0.0_

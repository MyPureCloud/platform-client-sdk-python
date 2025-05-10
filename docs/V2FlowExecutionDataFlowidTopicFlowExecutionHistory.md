# V2FlowExecutionDataFlowidTopicFlowExecutionHistory

## V2FlowExecutionDataFlowidTopicFlowExecutionHistory

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **execution_id** | str | The execution identifier which represents this unique instance of the flow that ran. | [optional] |
| **conversation_id** | str | The Genesys Cloud conversation identifier associated with this flow instance execution data. | [optional] |
| **division_id** | str | The division identifier for the division associated with the flow for this flow instance. | [optional] |
| **end_date_time** | datetime | The end date time for this flow instance execution data. | [optional] |
| **endpoint** | str | The public endpoint a user can use to retrieve the full historical log from the service. | [optional] |
| **errors** | [list[V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo]](V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo) | If the flow invoked error handling, an array of errors. | [optional] |
| **execution** | [list[V2FlowExecutionDataFlowidTopicFlowExecutionItem]](V2FlowExecutionDataFlowidTopicFlowExecutionItem) | An array of execution items that describe what happened when an Architect flow action container ran such as a flow, task, state or bot. | [optional] |
| **flow_exit_reason** | str | Provides information about why a flow ended. | [optional] |
| **flow_id** | str | The flow identifier for this flow instance execution data.  This is the identifier of the flow configuration that users load up in Architect. | [optional] |
| **flow_is_debug** | bool | Whether the flow that ran for this flow instance execution data was in debug mode. | [optional] |
| **execution_items_truncated** | bool | If true, the execution items in this event have been truncated to be deliverable. | [optional] |
| **flow_type** | str | The flow type of the Architect flow that was run. | [optional] |
| **flow_version** | str | The version of the flow for this flow instance execution data. Typically this is a numeric value like 1.0 represented as a string but can also be &#39;debug&#39; | [optional] |
| **message_type** | str | If applicable, the type of message platform from which the message originated. | [optional] |
| **invoking_context** | [V2FlowExecutionDataFlowidTopicInvokingContextInfo](V2FlowExecutionDataFlowidTopicInvokingContextInfo) |  | [optional] |
| **start_date_time** | datetime | The start date time for this flow instance execution data. | [optional] |
| **warnings** | [list[V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo]](V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo) | If the flow encountered a warning during execution, this is an array of the warnings. | [optional] |



_PureCloudPlatformClientV2 228.0.0_

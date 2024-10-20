# V2FlowExecutionDataFlowidTopicExecution

## V2FlowExecutionDataFlowidTopicExecution

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **object_type** | str | The type of executionItem that was executed. | [optional] |
| **object_id** | str | If applicable, the actionId, menuId or taskId for the executionItem. | [optional] |
| **output_path_id** | str | If applicable, the identifier of the OutputPath that was taken. | [optional] |
| **execution_id** | str | If applicable, the executionId for the executionItem. | [optional] |
| **start_date_time** | datetime | This is the starting time of the executionItem. | [optional] |
| **error** | [V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo](V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo) | Event generated when a Flow&#39;s Execution History is received and logged. | [optional] |
| **warning** | [V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo](V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo) | Event generated when a Flow&#39;s Execution History is received and logged. | [optional] |
| **language_tag** | str | If applicable, the language tag associated set by the execution. | [optional] |



_PureCloudPlatformClientV2 214.0.0_

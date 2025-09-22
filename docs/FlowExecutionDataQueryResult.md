# FlowExecutionDataQueryResult

## FlowExecutionDataQueryResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **start_date_time** | datetime | The start time for the execution of this flow. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **end_date_time** | datetime | The end time for the execution of this flow. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **flow_id** | str | The id of the flow that was executed. | [optional] |
| **flow_version** | str | The version of the flow that was executed. | [optional] |
| **conversation_id** | str | The id of the conversation that executed this flow. | [optional] |
| **workitem_id** | str | The id of the workitem that executed this flow. | [optional] |
| **flow_type** | str | The type of flow. | [optional] |
| **flow_error_reason** | str | If the flow errored out this is the reason. | [optional] |
| **flow_warning_reason** | str | If the flow had a warning, this is the reason. | [optional] |
| **flow_name** | str | The name of the flow. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 237.0.0_

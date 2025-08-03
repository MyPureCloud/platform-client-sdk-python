# FlowRuntimeExecution

## FlowRuntimeExecution

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The flow execution ID | [optional] |
| **name** | str | The flow execution name. | [optional] |
| **flow_version** | [FlowVersion](FlowVersion) | The Version of the flow definition of the flow execution. | |
| **date_launched** | datetime | The time the flow was launched. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **status** | str | The flow&#39;s running status, which indicates whether the flow is running normally or completed, etc. | |
| **date_completed** | datetime | The time the flow completed, if applicable. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **completion_reason** | str | The completion reason set at the flow completion time, if applicable. | [optional] |
| **flow_error_info** | [ErrorBody](ErrorBody) | Additional information if the flow is in error | [optional] |
| **output_data** | dict(str, object) | List of the flow&#39;s output variables, if any. Output variables are only supplied for Completed flows. | [optional] |
| **conversation** | [DomainEntityRef](DomainEntityRef) | The conversation to which this Flow execution is related | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 234.0.0_

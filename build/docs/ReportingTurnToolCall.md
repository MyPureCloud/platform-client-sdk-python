# ReportingTurnToolCall

## ReportingTurnToolCall

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **tool_id** | str | Represents the identifier of the tool called. | [optional] |
| **tool_name** | str | Represents the name of the tool used in the event. | [optional] |
| **tool_type** | str | Represents the type of tool used in the event. | [optional] |
| **target_id** | str | Represents the identifier of the target that the tool is using. | [optional] |
| **status** | str | Represents whether the tool call was successful or not. | [optional] |
| **error_text** | str | Represents the error returned by the tool in the event of a failure. | [optional] |
| **date_invoked** | datetime | Represents the starting time of the tool call. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **latency_ms** | int | Represents the time it took the tool call to execute. | [optional] |
| **origin** | str | Represents the origin of the tool call. | [optional] |
| **knowledge_metadata** | [ReportingTurnKnowledgeMetadata](ReportingTurnKnowledgeMetadata) | Represents various metadata of knowledge calls used by the tool if the tool is configured to use knowledge. | [optional] |



_PureCloudPlatformClientV2 266.0.0_

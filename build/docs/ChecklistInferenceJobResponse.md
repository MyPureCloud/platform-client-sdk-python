# ChecklistInferenceJobResponse

## ChecklistInferenceJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | ID of the inference job. | |
| **status** | str | Status of the checklist inference job. | |
| **error** | [ErrorInfo](ErrorInfo) | Error information associated with a job in case of any errors. | [optional] |
| **agent_checklist_info** | [AgentChecklistInfo](AgentChecklistInfo) | Agent checklist info. | [optional] |
| **job_start_time** | datetime | Date when the inference job started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **job_end_time** | datetime | Date when the inference job finished. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **language** | str | Language associated with the checklist. | [optional] |
| **agent_id** | str | Agent ID. | [optional] |
| **participant_id** | str | Participant ID. | [optional] |
| **queue_id** | str | Queue ID. | [optional] |
| **assistant_id** | str | Assistant ID. | [optional] |
| **media_type** | str | Media type. | [optional] |
| **direction** | str | Direction of the conversation. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 247.0.0_

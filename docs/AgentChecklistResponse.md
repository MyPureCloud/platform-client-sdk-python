# AgentChecklistResponse

## AgentChecklistResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | ID of the checklist. | |
| **name** | str | Name of the checklist. | |
| **checklist_items** | [list[ChecklistItem]](ChecklistItem) | List of individual Checklist Items. | |
| **activation_triggers** | [list[ActivationTrigger]](ActivationTrigger) | List of triggers that activated this checklist. | [optional] |
| **status** | str | The evaluation status of the checklist. | |
| **exit_reason** | str | Exit reason provided at the time of finalizing the checklist. | [optional] |
| **language** | str | Language associated with the checklist. | |
| **agent_id** | str | Agent ID. | [optional] |
| **participant_id** | str | Participant ID. | [optional] |
| **queue_id** | str | Queue ID. | [optional] |
| **assistant_id** | str | Assistant ID. | [optional] |
| **media_type** | str | Media type. | [optional] |
| **direction** | str | Direction of the conversation. | [optional] |
| **evaluation_start_date** | datetime | Date when the checklist evaluation began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **evaluation_last_modified_date** | datetime | Date when the checklist was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **evaluation_finalized_date** | datetime | Date when the checklist was finalized. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **evaluation_finalized_with_acw_date** | datetime | Date when the checklist was finalized with ACW. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 248.0.0_

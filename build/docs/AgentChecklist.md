# AgentChecklist

## AgentChecklist

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Agent Checklist ID. | [optional] |
| **name** | str | Agent Checklist Name. | |
| **language** | str | Agent Checklist Language. | |
| **checklist_items** | [list[AgentChecklistItem]](AgentChecklistItem) | Agent Checklist Items. | |
| **created_by** | [UserReference](UserReference) | The user who created the agent checklist. | [optional] |
| **modified_by** | [UserReference](UserReference) | The user who last modified the agent checklist. | [optional] |
| **date_created** | datetime | Date when the agent checklist was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date when the agent checklist was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 248.0.0_

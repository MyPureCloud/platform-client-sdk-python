# ChecklistItem

## ChecklistItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | ID of the checklist item. | |
| **name** | str | Name of the checklist item. | |
| **description** | str | Description of the checklist item. | [optional] |
| **automated_check_enabled** | bool | Flag to indicate whether automated check is enabled for this checklist item. | [optional] |
| **important** | bool | Flag to indicate whether this checklist item is marked as important. | [optional] |
| **state_from_model** | str | Checklist state as evaluated by the model. | [optional] |
| **state_from_agent** | str | Checklist state as evaluated by the agent. | [optional] |
| **date_last_modified_by_model** | datetime | Date when the checklist item was last modified by the model. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_last_modified_by_agent** | datetime | Date when the checklist item was last modified by the agent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **last_modified_in_acw** | bool | Flag to indicate whether this checklist item was modified in ACW. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 248.0.0_

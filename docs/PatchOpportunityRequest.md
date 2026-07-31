# PatchOpportunityRequest

## PatchOpportunityRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | datetime | The start date and time of the opportunity in ISO-8601 format | [optional] |
| **end_date** | datetime | The end date and time of the opportunity in ISO-8601 format | [optional] |
| **open_date** | [ValueWrapperInstant](ValueWrapperInstant) | The date and time when the opportunity opens for enrollment in ISO-8601 format. If not provided or in the past, it will be automatically updated to the current time when the opportunity is published | [optional] |
| **deadline_date** | datetime | The deadline date and time for enrollment in the opportunity in ISO-8601 format | [optional] |
| **name** | str | The name of the opportunity | [optional] |
| **description** | [ValueWrapperString](ValueWrapperString) | Additional details describing the purpose or context of this opportunity | [optional] |
| **activity_code_id** | str | The ID of the activity code associated with the opportunity | [optional] |
| **approval_type** | str | The approval type for enrollments | [optional] |
| **capacity** | int | The maximum capacity (enrollment slots) for this opportunity | [optional] |
| **agent_ids** | [ListWrapperString](ListWrapperString) | The IDs of the agents that are invited to the opportunity | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | The metadata for the opportunity | |



_PureCloudPlatformClientV2 263.0.0_

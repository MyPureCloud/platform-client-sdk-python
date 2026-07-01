# OpportunityResultWithAgentIds

## OpportunityResultWithAgentIds

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | |
| **start_date** | datetime | The start date and time of the opportunity in ISO-8601 format | |
| **end_date** | datetime | The end date and time of the opportunity in ISO-8601 format | |
| **status** | str | The current status of the opportunity | |
| **open_date** | datetime | The date and time when the opportunity opens for enrollment in ISO-8601 format. If not provided or in the past, it will be automatically updated to the current time when the opportunity is published | [optional] |
| **deadline_date** | datetime | The deadline date and time for enrollment in the opportunity in ISO-8601 format | |
| **name** | str | The name of the opportunity | |
| **description** | str | Additional details describing the purpose or context of this opportunity | [optional] |
| **activity_code_id** | str | The ID of the activity code associated with the opportunity | |
| **approval_type** | str | The approval type for enrollments | |
| **agent_count** | int | The total number of agents invited to this opportunity | |
| **capacity** | int | The maximum capacity (enrollment slots) for this opportunity | |
| **enrollment_processing_count** | int | The number of enrollments currently being processed | |
| **enrollment_counts** | [OpportunityEnrollmentCounts](OpportunityEnrollmentCounts) | The counts for enrollment statuses | |
| **published_date** | datetime | The date and time when the opportunity was published in ISO-8601 format | [optional] |
| **closed_date** | datetime | The date and time when the opportunity was closed in ISO-8601 format | [optional] |
| **system_message_code** | str | The system-generated message code about opportunity processing issues or validation failures | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | The metadata for the opportunity | |
| **agent_ids** | list[str] | The IDs of the agents that are invited to the opportunity | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 261.0.0_

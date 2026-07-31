# AgentQueryOpportunityResult

## AgentQueryOpportunityResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the opportunity | |
| **description** | str | Additional details describing the purpose or context of this opportunity | [optional] |
| **activity_code_id** | str | The ID of the activity code associated with the opportunity | |
| **start_date** | datetime | The start date and time of the opportunity in ISO-8601 format | |
| **end_date** | datetime | The end date and time of the opportunity in ISO-8601 format | |
| **deadline_date** | datetime | The deadline date and time for enrollment in the opportunity in ISO-8601 format | |
| **status** | str | The current status of the opportunity | |
| **capacity** | int | The maximum capacity for this opportunity | |
| **enrollment_counts** | [PendingAndApprovedOpportunityEnrollmentCounts](PendingAndApprovedOpportunityEnrollmentCounts) | Subset of enrollment counts which are relevant to the agent | |
| **enrollment** | [AgentOpportunityEnrollmentResult](AgentOpportunityEnrollmentResult) | The agent&#39;s enrollment in this opportunity, if enrolled | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | The metadata for the opportunity | |



_PureCloudPlatformClientV2 263.0.0_

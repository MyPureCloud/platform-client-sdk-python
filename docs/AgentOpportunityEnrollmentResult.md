# AgentOpportunityEnrollmentResult

## AgentOpportunityEnrollmentResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **status** | str | The current status of the enrollment | |
| **schedule** | [BuScheduleReference](BuScheduleReference) | The schedule on which the enrollment was added when this enrollment was approved | [optional] |
| **system_message_code** | str | The system-generated message code about enrollment processing results or failures | [optional] |
| **review_note** | str | Supervisor&#39;s note explaining the agent&#39;s enrollment status change | [optional] |
| **denial_code** | str | The denial code | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | The metadata for the enrollment | |



_PureCloudPlatformClientV2 265.0.0_

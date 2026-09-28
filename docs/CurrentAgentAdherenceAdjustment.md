# CurrentAgentAdherenceAdjustment

## CurrentAgentAdherenceAdjustment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | |
| **agent** | [UserReference](UserReference) | The agent to whom this adherence adjustment applies | |
| **management_unit** | [ManagementUnitReference](ManagementUnitReference) | The management unit to which the agent belonged when the adherence adjustment was submitted | |
| **business_unit** | [BusinessUnitReference](BusinessUnitReference) | The business unit to which the agent belonged when the adherence adjustment was submitted | |
| **start_date** | datetime | The start timestamp of the adherence adjustment in ISO-8601 format | |
| **length_minutes** | int | The length of the adherence adjustment in minutes | |
| **reason_code** | [AdherenceAdjustmentsReasonCodeReference](AdherenceAdjustmentsReasonCodeReference) | The reason code for this adherence adjustment | |
| **status** | str | The status of the adherence adjustment | |
| **expired** | bool | Indicates if the adherence adjustment is expired | |
| **submitter_notes** | str | Notes provided by the submitter for this adherence adjustment | [optional] |
| **reviewer_notes** | str | Notes provided by the reviewer for this adherence adjustment | [optional] |
| **reviewed_by** | [UserReference](UserReference) | The user who reviewed the adherence adjustment, if applicable. The id may be &#39;System&#39; if it was an automated process | [optional] |
| **reviewed_date** | datetime | The date the adherence adjustment was reviewed, if applicable. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for the adherence adjustment | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 268.0.0_

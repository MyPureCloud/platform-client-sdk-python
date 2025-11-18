# AlternativeShiftTradeResponse

## AlternativeShiftTradeResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **shift_offer_job_id** | str | The job ID of the alternative shift offer listing, from which the trade was chosen | |
| **existing_shifts** | [list[AlternativeShiftAgentScheduledShift]](AlternativeShiftAgentScheduledShift) | The existing shifts from the offer, may be empty | |
| **offered_shifts** | [list[AlternativeShiftAgentScheduledShift]](AlternativeShiftAgentScheduledShift) | The offered shifts from the offer, may be empty | |
| **schedule** | [AlternativeShiftScheduleLookup](AlternativeShiftScheduleLookup) | The existing schedule information associated with the trade | |
| **management_unit** | [ManagementUnitReference](ManagementUnitReference) | The management unit of this alternative shift trade request | |
| **user** | [UserReference](UserReference) | The user who submitted the trade request | |
| **week_date** | date | The start week date of the associated schedule in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **expiration_date** | datetime | The date when the trade will expire in ISO-8601 format. The trade cannot be approved after expiration | [optional] |
| **state** | str | The state of this alternative shift trade | |
| **processing_status** | str | The processing status of this alternative shift trade | [optional] |
| **system_date_reviewed** | datetime | The timestamp of when the trade request was reviewed by the system in ISO-8601 format | [optional] |
| **admin_date_reviewed** | datetime | The timestamp of when the trade request was reviewed by an admin in ISO-8601 format | [optional] |
| **admin_reviewed_by** | [UserReference](UserReference) | The admin who reviewed this alternative shift trade after system denial | [optional] |
| **violations** | list[str] | A list of trade match violations | |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for this alternative shift trade | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 243.0.0_

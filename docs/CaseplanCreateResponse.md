# CaseplanCreateResponse

## CaseplanCreateResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the Caseplan. | |
| **division** | [StarrableDivision](StarrableDivision) | The division to which this Caseplan belongs. | |
| **description** | str | The description of the Caseplan. | [optional] |
| **reference_prefix** | str | The prefix used when creating the reference for Cases from the Caseplan. | |
| **default_due_duration_in_seconds** | int | The default due duration in seconds for Cases created from the Caseplan. | |
| **default_ttl_seconds** | int | The default TTL in seconds for Cases created from the Caseplan. | |
| **default_case_owner** | [UserReference](UserReference) | The default Case owner for Cases created from the Caseplan. | [optional] |
| **latest** | int | The latest version of the Caseplan. | |
| **published** | int | The published version of the Caseplan. | [optional] |
| **date_created** | datetime | The Caseplan creation date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **date_modified** | datetime | The Caseplan modification date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **date_published** | datetime | The Caseplan publication date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [UserReference](UserReference) | The ID of the User who modified the Caseplan. | |
| **customer_intent** | [CustomerIntentReference](CustomerIntentReference) | The customer intent for Cases created from this Caseplan. | |
| **version_state** | str | The version state of the Caseplan. | [optional] |
| **data_schemas** | [list[CaseplanDataSchema]](CaseplanDataSchema) | The schemas that define all data for Cases from this Caseplan. | [optional] |
| **intake_settings** | [list[IntakeSetting]](IntakeSetting) | The intake format when collecting data for a Case from this Caseplan. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 261.0.0_

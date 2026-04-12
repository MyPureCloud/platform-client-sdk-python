# CaseplanCreate

## CaseplanCreate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the Caseplan. Valid length between 3 and 256 characters. | |
| **default_due_duration_in_seconds** | int | The default due duration in seconds for Cases created from the Caseplan. Valid range is between 1 and 31536000 seconds. | [optional] |
| **default_ttl_seconds** | int | The default TTL in seconds for Cases created from the Caseplan. Valid range is between 86400 and 31536000 seconds. | [optional] |
| **reference_prefix** | str | The prefix of the Caseplan reference. Valid length between 2 and 8 alphanumeric characters. | |
| **customer_intent_id** | str | The ID of the customer intent associated with this Caseplan. | |
| **description** | str | The description of the Caseplan. Maximum length of 512 characters. | [optional] |
| **default_case_owner_id** | str | The ID of the default owner of a Case created from the Caseplan. | [optional] |
| **division_id** | str | The ID of the division the Caseplan belongs to. Use &#39;*&#39; for divisionless caseplans. | |
| **data_schemas** | [list[CaseplanDataSchema]](CaseplanDataSchema) | The schemas that define all data for cases from this Caseplan. The schema must be defined in the TaskManagement namespace. | |
| **intake_settings** | [list[IntakeSetting]](IntakeSetting) | The intake format when collecting data for a case from this caseplan. There can be a maximum of 10 IntakeSettings defined for a Caseplan. | [optional] |



_PureCloudPlatformClientV2 256.0.0_

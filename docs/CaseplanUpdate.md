# CaseplanUpdate

## CaseplanUpdate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the Caseplan. Valid length between 3 and 256 characters. | [optional] |
| **default_due_duration_in_seconds** | int | The default due duration in seconds for Cases created from the Caseplan. Valid range is between 1 and 31536000 seconds. | [optional] |
| **default_ttl_seconds** | int | The default TTL in seconds for Cases created from the Caseplan. Valid range is between 86400 and 31536000 seconds. | [optional] |
| **reference_prefix** | str | The reference of the Caseplan. Valid length between 2 and 8 alphanumeric characters. | [optional] |
| **customer_intent_id** | str | The ID of the customer intent associated with this Caseplan. | [optional] |
| **description** | str | The description of the Caseplan. Maximum length of 512 characters. | [optional] |
| **default_case_owner_id** | str | The ID of the default owner of a Case created from the Caseplan. Must be a valid UUID. | [optional] |
| **division_id** | str | The ID of the division the Caseplan belongs to. If divisionId is null or &#39;*&#39;, the Caseplan will be divisionless. | [optional] |



_PureCloudPlatformClientV2 254.0.0_

# AdherenceExplanationResponse

## AdherenceExplanationResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **agent** | [UserReference](UserReference) | The agent to whom this adherence explanation applies | |
| **management_unit** | [ManagementUnitReference](ManagementUnitReference) | The management unit to which the agent belonged at the time the adherence explanation was submitted | |
| **business_unit** | [BusinessUnitReference](BusinessUnitReference) | The business unit to which the agent belonged at the time the adherence explanation was submitted | |
| **type** | str | The type of the adherence explanation | |
| **status** | str | The status of the adherence explanation | |
| **start_date** | datetime | The start timestamp of the adherence explanation in ISO-8601 format | |
| **length_minutes** | int | The length of the adherence explanation in minutes | |
| **notes** | str | Notes about the adherence explanation | [optional] |
| **reviewed_by** | [UserReference](UserReference) | The user who reviewed the adherence explanation, if applicable. The id may be &#39;System&#39; if it was an automated process | [optional] |
| **reviewed_date** | datetime | The timestamp for when the adherence explanation was reviewed, if applicable. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 247.0.0_

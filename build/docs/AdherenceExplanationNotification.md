# AdherenceExplanationNotification

## AdherenceExplanationNotification

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **agent** | [UserReference](UserReference) | The agent for whom the adherence explanation applies | [optional] |
| **management_unit** | [ManagementUnitReference](ManagementUnitReference) | The management unit to which the agent belonged at the time the adherence explanation was submitted | [optional] |
| **business_unit** | [BusinessUnitReference](BusinessUnitReference) | The business unit to which the agent belonged at the time the adherence explanation was submitted | [optional] |
| **start_date** | datetime | The start date of the adherence explanation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **length_minutes** | int | The length of the adherence explanation in minutes | [optional] |
| **status** | str | The status of the adherence explanation | [optional] |
| **type** | str | The type of the adherence explanation | [optional] |
| **notes** | str | Notes about the adherence explanation | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 243.0.0_

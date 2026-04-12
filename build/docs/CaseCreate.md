# CaseCreate

## CaseCreate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **caseplan_id** | str | The ID of the caseplan to create the case from. | |
| **owner_id** | str | The ID of the owner of the case. | [optional] |
| **summary** | str | Overview information for the Case. Valid length between 3 and 512 characters. | [optional] |
| **external_contact_id** | str | The ID of the External Contact associated with the Case. | |
| **conversation_id** | str | The ID of conversation associated with the Case. | [optional] |
| **workitem_id** | str | The ID of the workitem associated with the Case. | [optional] |
| **ttl_seconds** | int | The epoch timestamp in seconds specifying the time-to-live for the lifetime of the Case. Can not be greater than 365 days from the current time. | [optional] |
| **intake** | [list[Intake]](Intake) | The intake data for the Case. Maximum of 10 intake objects allowed. | [optional] |



_PureCloudPlatformClientV2 256.0.0_

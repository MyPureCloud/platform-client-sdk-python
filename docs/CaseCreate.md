# CaseCreate

## CaseCreate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **caseplan_id** | str | The ID of the Caseplan used to create the Case. | |
| **owner_id** | str | The ID of the owner of the Case. | [optional] |
| **summary** | str | Overview information for the Case. Valid length between 3 and 512 characters. | [optional] |
| **description** | str | The description of the Case. Maximum length of 512 characters. | [optional] |
| **external_id** | str | The identifier of the Case in an external system. Minimum length is 1 character. Maximum length of 64 characters. | [optional] |
| **external_contact_id** | str | The ID of the External Contact associated with the Case. | |
| **conversation_id** | str | The ID of the Conversation associated with the Case. | [optional] |
| **workitem_id** | str | The ID of the Workitem associated with the Case. | [optional] |
| **ttl_seconds** | int | Epoch timestamp in seconds for the Case time-to-live. Cannot be more than 365 days after the current time. | [optional] |
| **intake** | [list[Intake]](Intake) | The intake data for the Case. Maximum of 10 intake objects allowed. | [optional] |



_PureCloudPlatformClientV2 269.0.0_

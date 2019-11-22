---
title: LocationCreateDefinition
---
## LocationCreateDefinition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | The name of the Location. Required for creates, not required for updates | |
| **version** | **int** | Current version of the location | [optional] |
| **state** | **str** | Current activity status of the location. | [optional] |
| **path** | **list[str]** | A list of ancestor ids | [optional] |
| **notes** | **str** | Notes for the location | [optional] |
| **contact_user** | **str** | The user id of the location contact | [optional] |
| **emergency_number** | [**LocationEmergencyNumber**](LocationEmergencyNumber.html) | Emergency number for the location | [optional] |
| **address** | [**LocationAddress**](LocationAddress.html) | Address of the location | [optional] |
{: class="table table-striped"}



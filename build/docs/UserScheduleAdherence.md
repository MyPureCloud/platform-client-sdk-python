---
title: UserScheduleAdherence
---
## UserScheduleAdherence

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **user** | [**User**](User.html) | The user for whom this status applies | [optional] |
| **management_unit** | [**ManagementUnit**](ManagementUnit.html) | The management unit to which this user belongs | [optional] |
| **scheduled_activity_category** | **str** | Activity for which the user is scheduled | [optional] |
| **system_presence** | **str** | Actual underlying system presence value | [optional] |
| **organization_secondary_presence_id** | **str** | Organization Secondary Presence Id. | [optional] |
| **routing_status** | **str** | Actual underlying routing status, used to determine whether a user is actually in adherence when OnQueue | [optional] |
| **actual_activity_category** | **str** | Activity in which the user is actually engaged | [optional] |
| **is_out_of_office** | **bool** | Whether the user is marked OutOfOffice | [optional] |
| **adherence_state** | **str** | The user&#39;s current adherence state | [optional] |
| **impact** | **str** | The impact of the user&#39;s current adherenceState | [optional] |
| **time_of_adherence_change** | **str** | Time when the user entered the current adherenceState in ISO-8601 format | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



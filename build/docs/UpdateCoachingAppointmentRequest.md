---
title: UpdateCoachingAppointmentRequest
---
## UpdateCoachingAppointmentRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | The name of coaching appointment. | [optional] |
| **description** | **str** | The description of coaching appointment. | [optional] |
| **date_start** | **datetime** | The date/time the coaching appointment starts. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **length_in_minutes** | **int** | The duration of coaching appointment in minutes. | [optional] |
| **conversation_ids** | **list[str]** | IDs of conversations associated with this coaching appointment. | [optional] |
| **document_ids** | **list[str]** | IDs of documents associated with this coaching appointment. | [optional] |
{: class="table table-striped"}



---
title: CreateCoachingAppointmentRequest
---
## CreateCoachingAppointmentRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | The name of coaching appointment. | |
| **description** | **str** | The description of coaching appointment. | |
| **date_start** | **datetime** | The date/time the coaching appointment starts. Times will be rounded down to the minute. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **length_in_minutes** | **int** | The duration of coaching appointment in minutes. | |
| **facilitator_id** | **str** | The facilitator ID of coaching appointment. | [optional] |
| **attendee_ids** | **list[str]** | IDs of attendees in the coaching appointment. | |
| **conversation_ids** | **list[str]** | IDs of conversations associated with this coaching appointment. | |
| **document_ids** | **list[str]** | IDs of documents associated with this coaching appointment. | |
{: class="table table-striped"}



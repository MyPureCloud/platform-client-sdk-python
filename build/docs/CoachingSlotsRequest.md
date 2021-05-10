---
title: CoachingSlotsRequest
---
## CoachingSlotsRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **interval** | **str** | Range of time to get slots for scheduling coaching appointments. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **length_in_minutes** | **int** | The duration of coaching appointment to schedule in 15 minutes granularity up to maximum of 60 minutes | |
| **attendee_ids** | **list[str]** | List of attendees to determine coaching appointment slots | |
| **facilitator_ids** | **list[str]** | List of facilitators to determine coaching appointment slots | [optional] |
{: class="table table-striped"}



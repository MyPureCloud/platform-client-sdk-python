---
title: ObservationValue
---
## ObservationValue

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **observation_date** | **datetime** | The time at which the observation occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | |
| **conversation_id** | **str** | Unique identifier for the conversation | [optional] |
| **session_id** | **str** | The unique identifier of this session | [optional] |
| **requested_routing_skill_ids** | **list[str]** | Unique identifier for a skill requested for an interaction | [optional] |
| **requested_language_id** | **str** | Unique identifier for the language requested for an interaction | [optional] |
| **routing_priority** | **int** | Routing priority for the current interaction | [optional] |
| **participant_name** | **str** | A human readable name identifying the participant | [optional] |
| **user_id** | **str** | Unique identifier for the user | [optional] |
| **direction** | **str** | The direction of the communication | [optional] |
| **converted_from** | **str** | Session media type that was converted from in case of a media type conversion | [optional] |
| **converted_to** | **str** | Session media type that was converted to in case of a media type conversion | [optional] |
| **address_from** | **str** | The address that initiated an action | [optional] |
| **address_to** | **str** | The address receiving an action | [optional] |
| **ani** | **str** | Automatic Number Identification (caller&#39;s number) | [optional] |
| **dnis** | **str** | Dialed number identification service (number dialed by the calling party) | [optional] |
{: class="table table-striped"}



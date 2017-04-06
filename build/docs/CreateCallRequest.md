---
title: CreateCallRequest
---
## CreateCallRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **phone_number** | **str** | The phone number to dial. | [optional] |
| **call_from_queue_id** | **str** | The queue ID to call on behalf of. | [optional] |
| **call_queue_id** | **str** | The queue ID to call. | [optional] |
| **call_user_id** | **str** | The user ID to call. | [optional] |
| **priority** | **int** | The priority to assign to this call (if calling a queue). | [optional] |
| **language_id** | **str** | The language skill ID to use for routing this call (if calling a queue). | [optional] |
| **routing_skills_ids** | **list[str]** | The skill ID&#39;s to use for routing this call (if calling a queue). | [optional] |
| **conversation_ids** | **list[str]** | The list of existing call conversations to merge into a new ad-hoc conference. | [optional] |
| **participants** | [**list[Destination]**](Destination.html) | The list of participants to call to create a new ad-hoc conference. | [optional] |
{: class="table table-striped"}



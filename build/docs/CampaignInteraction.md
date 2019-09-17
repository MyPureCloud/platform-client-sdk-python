---
title: CampaignInteraction
---
## CampaignInteraction

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **campaign** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **agent** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **contact** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **destination_address** | **str** |  | [optional] |
| **active_preview_call** | **bool** | Boolean value if there is an active preview call on the interaction | [optional] |
| **last_active_preview_wrapup_time** | **datetime** | The time when the last preview of the interaction was wrapped up. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **creation_time** | **datetime** | The time when dialer created the interaction. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **call_placed_time** | **datetime** | The time when the agent or system places the call. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **call_routed_time** | **datetime** | The time when the agent was connected to the call. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **preview_connected_time** | **datetime** | The time when the customer and routing participant are connected. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **queue** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **script** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **disposition** | **str** | Describes what happened with call analysis for instance: disposition.classification.callable.person, disposition.classification.callable.noanswer | [optional] |
| **caller_name** | **str** |  | [optional] |
| **caller_address** | **str** |  | [optional] |
| **preview_pop_delivered_time** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **conversation** | [**ConversationBasic**](ConversationBasic.html) |  | [optional] |
| **dialer_system_participant_id** | **str** | conversation participant id that is the dialer system participant to monitor the call from dialer perspective | [optional] |
| **dialing_mode** | **str** |  | [optional] |
| **skills** | [**list[DomainEntityRef]**](DomainEntityRef.html) | Any skills that are attached to the call for routing | [optional] |
{: class="table table-striped"}



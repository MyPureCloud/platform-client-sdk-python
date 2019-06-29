---
title: AnalyticsConversationSegment
---
## AnalyticsConversationSegment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **segment_start** | **datetime** | The timestamp when this segment began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **segment_end** | **datetime** | The timestamp when this segment ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **queue_id** | **str** | Queue identifier | [optional] |
| **wrap_up_code** | **str** | Wrapup Code id | [optional] |
| **wrap_up_note** | **str** | Note entered by an agent during after-call work | [optional] |
| **wrap_up_tags** | **list[str]** |  | [optional] |
| **error_code** | **str** |  | [optional] |
| **disconnect_type** | **str** | A description of the event that disconnected the segment | [optional] |
| **segment_type** | **str** | The activity taking place for the participant in the segment | [optional] |
| **requested_routing_user_ids** | **list[str]** |  | [optional] |
| **requested_routing_skill_ids** | **list[str]** |  | [optional] |
| **requested_language_id** | **str** | A unique identifier for the language requested for an interaction. | [optional] |
| **scored_agents** | [**list[AnalyticsScoredAgent]**](AnalyticsScoredAgent.html) |  | [optional] |
| **properties** | [**list[AnalyticsProperty]**](AnalyticsProperty.html) |  | [optional] |
| **source_conversation_id** | **str** |  | [optional] |
| **destination_conversation_id** | **str** |  | [optional] |
| **source_session_id** | **str** |  | [optional] |
| **destination_session_id** | **str** |  | [optional] |
| **sip_response_codes** | **list[int]** |  | [optional] |
| **q850_response_codes** | **list[int]** |  | [optional] |
| **conference** | **bool** | Indicates whether the segment was a conference | [optional] |
| **group_id** | **str** |  | [optional] |
| **subject** | **str** |  | [optional] |
| **audio_muted** | **bool** |  | [optional] |
| **video_muted** | **bool** |  | [optional] |
{: class="table table-striped"}



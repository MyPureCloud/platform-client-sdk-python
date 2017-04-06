---
title: AnalyticsConversationSegment
---
## AnalyticsConversationSegment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **segment_start** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **segment_end** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **queue_id** | **str** |  | [optional] |
| **wrap_up_code** | **str** |  | [optional] |
| **wrap_up_note** | **str** |  | [optional] |
| **wrap_up_tags** | **list[str]** |  | [optional] |
| **error_code** | **str** |  | [optional] |
| **disconnect_type** | **str** |  | [optional] |
| **segment_type** | **str** |  | [optional] |
| **requested_routing_user_ids** | **list[str]** |  | [optional] |
| **requested_routing_skill_ids** | **list[str]** |  | [optional] |
| **requested_language_id** | **str** |  | [optional] |
| **properties** | [**list[AnalyticsProperty]**](AnalyticsProperty.html) |  | [optional] |
| **source_conversation_id** | **str** |  | [optional] |
| **destination_conversation_id** | **str** |  | [optional] |
| **source_session_id** | **str** |  | [optional] |
| **destination_session_id** | **str** |  | [optional] |
| **sip_response_codes** | **list[int]** |  | [optional] |
| **q850_response_codes** | **list[int]** |  | [optional] |
| **conference** | **bool** |  | [optional] |
| **group_id** | **str** |  | [optional] |
| **subject** | **str** |  | [optional] |
| **audio_muted** | **bool** |  | [optional] |
| **video_muted** | **bool** |  | [optional] |
{: class="table table-striped"}



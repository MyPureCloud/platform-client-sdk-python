---
title: QueueConversationEventTopicParticipant
---
## QueueConversationEventTopicParticipant

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **connected_time** | **datetime** |  | [optional] |
| **end_time** | **datetime** |  | [optional] |
| **user_id** | **str** |  | [optional] |
| **external_contact_id** | **str** |  | [optional] |
| **external_organization_id** | **str** |  | [optional] |
| **name** | **str** |  | [optional] |
| **queue_id** | **str** |  | [optional] |
| **group_id** | **str** |  | [optional] |
| **purpose** | **str** |  | [optional] |
| **consult_participant_id** | **str** |  | [optional] |
| **address** | **str** |  | [optional] |
| **wrapup_required** | **bool** |  | [optional] |
| **wrapup_expected** | **bool** |  | [optional] |
| **wrapup_prompt** | **str** |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup** | [**QueueConversationEventTopicWrapup**](QueueConversationEventTopicWrapup.html) |  | [optional] |
| **conversation_routing_data** | [**QueueConversationEventTopicConversationRoutingData**](QueueConversationEventTopicConversationRoutingData.html) |  | [optional] |
| **alerting_timeout_ms** | **int** |  | [optional] |
| **monitored_participant_id** | **str** |  | [optional] |
| **screen_recording_state** | **str** |  | [optional] |
| **flagged_reason** | **str** |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **calls** | [**list[QueueConversationEventTopicCall]**](QueueConversationEventTopicCall.html) |  | [optional] |
| **callbacks** | [**list[QueueConversationEventTopicCallback]**](QueueConversationEventTopicCallback.html) |  | [optional] |
| **chats** | [**list[QueueConversationEventTopicChat]**](QueueConversationEventTopicChat.html) |  | [optional] |
| **cobrowsesessions** | [**list[QueueConversationEventTopicCobrowse]**](QueueConversationEventTopicCobrowse.html) |  | [optional] |
| **emails** | [**list[QueueConversationEventTopicEmail]**](QueueConversationEventTopicEmail.html) |  | [optional] |
| **messages** | [**list[QueueConversationEventTopicMessage]**](QueueConversationEventTopicMessage.html) |  | [optional] |
| **screenshares** | [**list[QueueConversationEventTopicScreenshare]**](QueueConversationEventTopicScreenshare.html) |  | [optional] |
| **social_expressions** | [**list[QueueConversationEventTopicSocialExpression]**](QueueConversationEventTopicSocialExpression.html) |  | [optional] |
| **videos** | [**list[QueueConversationEventTopicVideo]**](QueueConversationEventTopicVideo.html) |  | [optional] |
| **additional_properties** | **object** |  | [optional] |
{: class="table table-striped"}



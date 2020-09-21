---
title: Queue
---
## Queue

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **division** | [**Division**](Division.html) | The division to which this entity belongs. | [optional] |
| **description** | **str** | The queue description. | [optional] |
| **date_created** | **datetime** | The date the queue was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | The date of the last modification to the queue. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | **str** | The ID of the user that last modified the queue. | [optional] |
| **created_by** | **str** | The ID of the user that created the queue. | [optional] |
| **member_count** | **int** | The number of users in the queue. | [optional] |
| **media_settings** | [**dict(str, MediaSetting)**](MediaSetting.html) | The media settings for the queue. Valid key values: CALL, CALLBACK, CHAT, EMAIL, MESSAGE, SOCIAL_EXPRESSION, VIDEO_COMM | [optional] |
| **routing_rules** | [**list[RoutingRule]**](RoutingRule.html) | The routing rules for the queue, used for routing to known or preferred agents. | [optional] |
| **bullseye** | [**Bullseye**](Bullseye.html) | The bulls-eye settings for the queue. | [optional] |
| **acw_settings** | [**AcwSettings**](AcwSettings.html) | The ACW settings for the queue. | [optional] |
| **skill_evaluation_method** | **str** | The skill evaluation method to use when routing conversations. | [optional] |
| **queue_flow** | [**DomainEntityRef**](DomainEntityRef.html) | The in-queue flow to use for conversations waiting in queue. | [optional] |
| **whisper_prompt** | [**DomainEntityRef**](DomainEntityRef.html) | The prompt used for whisper on the queue, if configured. | [optional] |
| **auto_answer_only** | **bool** | Specifies whether the configured whisper should play for all ACD calls, or only for those which are auto-answered. | [optional] |
| **enable_transcription** | **bool** | Indicates whether voice transcription is enabled for this queue. | [optional] |
| **enable_manual_assignment** | **bool** | Indicates whether manual assignment is enabled for this queue. | [optional] |
| **calling_party_name** | **str** | The name to use for caller identification for outbound calls from this queue. | [optional] |
| **calling_party_number** | **str** | The phone number to use for caller identification for outbound calls from this queue. | [optional] |
| **default_scripts** | [**dict(str, Script)**](Script.html) | The default script Ids for the communication types. | [optional] |
| **outbound_messaging_addresses** | [**QueueMessagingAddresses**](QueueMessagingAddresses.html) | The messaging addresses for the queue. | [optional] |
| **outbound_email_address** | [**QueueEmailAddress**](QueueEmailAddress.html) |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



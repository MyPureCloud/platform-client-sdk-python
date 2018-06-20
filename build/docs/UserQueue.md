---
title: UserQueue
---
## UserQueue

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **division** | [**Division**](Division.html) | The division to which this entity belongs. | [optional] |
| **description** | **str** | The queue description. | [optional] |
| **version** | **int** | The current version of the queue. | [optional] |
| **date_created** | **datetime** | The date the queue was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | The date of the last modification to the queue. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | **str** | The ID of the user that last modified the queue. | [optional] |
| **created_by** | **str** | The ID of the user that created the queue. | [optional] |
| **state** | **str** | Indicates if the queue is active, inactive, or deleted. | [optional] |
| **modified_by_app** | **str** | The application that last modified the queue. | [optional] |
| **created_by_app** | **str** | The application that created the queue. | [optional] |
| **media_settings** | [**dict(str, MediaSetting)**](MediaSetting.html) | The media settings for the queue. Valid Key Values: CALL, CALLBACK, CHAT, EMAIL, SOCIAL_EXPRESSION | |
| **bullseye** | [**Bullseye**](Bullseye.html) | The bulls-eye settings for the queue. | [optional] |
| **acw_settings** | [**AcwSettings**](AcwSettings.html) | The ACW settings for the queue. | |
| **skill_evaluation_method** | **str** | The skill evaluation method to use when routing conversations. | |
| **queue_flow** | [**UriReference**](UriReference.html) | The in-queue flow to use for conversations waiting in queue. | [optional] |
| **whisper_prompt** | [**UriReference**](UriReference.html) | The prompt used for whisper on the queue, if configured. | [optional] |
| **auto_answer_only** | **bool** | Specifies whether the configured whisper should play for all ACD calls, or only for those which are auto-answered. | [optional] |
| **calling_party_name** | **str** | The name to use for caller identification for outbound calls from this queue. | [optional] |
| **calling_party_number** | **str** | The phone number to use for caller identification for outbound calls from this queue. | [optional] |
| **default_scripts** | [**dict(str, Script)**](Script.html) | The default script Ids for the communication types. | [optional] |
| **outbound_email_address** | [**QueueEmailAddress**](QueueEmailAddress.html) |  | [optional] |
| **joined** | **bool** |  | [optional] |
| **member_count** | **int** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



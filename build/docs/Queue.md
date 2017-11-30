---
title: Queue
---
## Queue

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **description** | **str** | The resource&#39;s description. | [optional] |
| **version** | **int** | The current version of the resource. | [optional] |
| **date_created** | **datetime** | The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | **str** | The ID of the user that last modified the resource. | [optional] |
| **created_by** | **str** | The ID of the user that created the resource. | [optional] |
| **state** | **str** | Indicates if the resource is active, inactive, or deleted. | [optional] |
| **modified_by_app** | **str** | The application that last modified the resource. | [optional] |
| **created_by_app** | **str** | The application that created the resource. | [optional] |
| **media_settings** | [**dict(str, MediaSetting)**](MediaSetting.html) | The media settings for the queue. Valid Key Values: CALL, CALLBACK, CHAT, EMAIL, SOCIAL_EXPRESSION | |
| **bullseye** | [**Bullseye**](Bullseye.html) | The bulls-eye settings for the queue. | [optional] |
| **acw_settings** | [**AcwSettings**](AcwSettings.html) | The ACW settings for the queue. | |
| **skill_evaluation_method** | **str** | The skill evaluation method to use when routing conversations. | |
| **queue_flow** | [**UriReference**](UriReference.html) | The in-queue flow to use for conversations waiting in queue. | [optional] |
| **whisper** | [**UriReference**](UriReference.html) | The prompt used for whisper audio on the queue, if configured. | [optional] |
| **auto_answer_only** | **bool** | Specifies whether the configured whisper audio should play for all ACD calls, or only for those which are auto-answered. | [optional] |
| **calling_party_name** | **str** | The name to use for caller identification for outbound calls from this queue. | [optional] |
| **calling_party_number** | **str** | The phone number to use for caller identification for outbound calls from this queue. | [optional] |
| **default_scripts** | [**dict(str, Script)**](Script.html) | The default script Ids for the communication types. | [optional] |
| **outbound_email_address** | [**QueueEmailAddress**](QueueEmailAddress.html) |  | [optional] |
| **member_count** | **int** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



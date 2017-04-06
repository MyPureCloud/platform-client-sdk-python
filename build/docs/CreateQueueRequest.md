---
title: CreateQueueRequest
---
## CreateQueueRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **description** | **str** |  | [optional] |
| **version** | **int** |  | [optional] |
| **date_created** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | **str** |  | [optional] |
| **created_by** | **str** |  | [optional] |
| **state** | **str** |  | [optional] |
| **modified_by_app** | **str** |  | [optional] |
| **created_by_app** | **str** |  | [optional] |
| **media_settings** | [**dict(str, MediaSetting)**](MediaSetting.html) | The media settings for the queue. | |
| **bullseye** | [**Bullseye**](Bullseye.html) | The bulls-eye settings for the queue. | [optional] |
| **acw_settings** | [**AcwSettings**](AcwSettings.html) | The ACW settings for the queue. | |
| **skill_evaluation_method** | **str** | The skill evaluation method to use when routing conversations. | |
| **queue_flow** | [**UriReference**](UriReference.html) | The in-queue flow to use for conversations waiting in queue. | [optional] |
| **calling_party_name** | **str** | The name to use for caller identification for outbound calls from this queue. | [optional] |
| **calling_party_number** | **str** | The phone number to use for caller identification for outbound calls from this queue. | [optional] |
| **default_scripts** | [**dict(str, Script)**](Script.html) | The default script Ids for the communication types. | [optional] |
| **outbound_email_address** | [**QueueEmailAddress**](QueueEmailAddress.html) |  | [optional] |
| **source_queue_id** | **str** | The id of an existing queue to copy the settings from when creating a new queue. | [optional] |
| **member_count** | **int** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



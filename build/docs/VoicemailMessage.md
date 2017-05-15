---
title: VoicemailMessage
---
## VoicemailMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **conversation** | [**Conversation**](Conversation.html) | The conversation that the voicemail message is associated with | [optional] |
| **read** | **bool** | Whether the voicemail message is marked as read | [optional] |
| **audio_recording_duration_seconds** | **int** | The voicemail message&#39;s audio recording duration in seconds | [optional] |
| **audio_recording_size_bytes** | **int** | The voicemail message&#39;s audio recording size in bytes | [optional] |
| **created_date** | **datetime** | The date the voicemail message was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_date** | **datetime** | The date the voicemail message was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **caller_address** | **str** | The caller address | [optional] |
| **caller_name** | **str** | Optionally the name of the caller that left the voicemail message if the caller was a known user | [optional] |
| **caller_user** | [**User**](User.html) | Optionally the user that left the voicemail message if the caller was a known user | [optional] |
| **deleted** | **bool** | Whether the voicemail message has been marked as deleted | [optional] |
| **note** | **str** | An optional note | [optional] |
| **user** | [**User**](User.html) | The user that the voicemail message belongs to or null which means the voicemail message belongs to a group or queue | [optional] |
| **group** | [**Group**](Group.html) | The group that the voicemail message belongs to or null which means the voicemail message belongs to a user or queue | [optional] |
| **queue** | [**Queue**](Queue.html) | The queue that the voicemail message belongs to or null which means the voicemail message belongs to a user or group | [optional] |
| **copied_from** | [**VoicemailCopyRecord**](VoicemailCopyRecord.html) | Represents where this voicemail message was copied from | [optional] |
| **copied_to** | [**list[VoicemailCopyRecord]**](VoicemailCopyRecord.html) | Represents where this voicemail has been copied to | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



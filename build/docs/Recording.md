---
title: Recording
---
## Recording

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **conversation_id** | **str** |  | [optional] |
| **path** | **str** |  | [optional] |
| **start_time** | **str** |  | [optional] |
| **end_time** | **str** |  | [optional] |
| **media** | **str** | The type of media that the recording is. At the moment that could be audio, chat, or email. | [optional] |
| **annotations** | [**list[Annotation]**](Annotation.html) | Annotations that belong to the recording. | [optional] |
| **transcript** | [**list[ChatMessage]**](ChatMessage.html) | Represents a chat transcript | [optional] |
| **email_transcript** | [**list[RecordingEmailMessage]**](RecordingEmailMessage.html) | Represents an email transcript | [optional] |
| **messaging_transcript** | [**list[RecordingMessagingMessage]**](RecordingMessagingMessage.html) | Represents a messaging transcript | [optional] |
| **file_state** | **str** | Represents the current file state for a recording. Examples: Uploading, Archived, etc | [optional] |
| **restore_expiration_time** | **datetime** | The amount of time a restored recording will remain restored before being archived again. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **media_uris** | [**dict(str, MediaResult)**](MediaResult.html) | The different mediaUris for the recording. | [optional] |
| **estimated_transcode_time_ms** | **int** |  | [optional] |
| **actual_transcode_time_ms** | **int** |  | [optional] |
| **archive_date** | **datetime** | The date the recording will be archived. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **archive_medium** | **str** | The type of archive medium used. Example: CloudArchive | [optional] |
| **delete_date** | **datetime** | The date the recording will be deleted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **max_allowed_restorations_for_org** | **int** | How many archive restorations the organization is allowed to have. | [optional] |
| **remaining_restorations_allowed_for_org** | **int** | The remaining archive restorations the organization has. | [optional] |
| **session_id** | **str** | The session id represents an external resource id, such as email, call, chat, etc | [optional] |
| **users** | [**list[User]**](User.html) | The users participating in the conversation | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



# Recording

## Recording

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **conversation_id** | str |  | [optional] |
| **path** | str |  | [optional] |
| **start_time** | str | The start time of the recording. Null when there is no playable media. | [optional] |
| **end_time** | str | The end time of the recording. Null when there is no playable media. | [optional] |
| **media** | str | The media type of the recording. This could be audio, chat, messaging, email, or screen. | [optional] |
| **media_subtype** | str | The media subtype of the recording. | [optional] |
| **media_subject** | str | The media subject of the recording. | [optional] |
| **annotations** | [list[Annotation]](Annotation) | Annotations that belong to the recording. | [optional] |
| **transcript** | [list[ChatMessage]](ChatMessage) | Represents a chat transcript | [optional] |
| **email_transcript** | [list[RecordingEmailMessage]](RecordingEmailMessage) | Represents an email transcript | [optional] |
| **messaging_transcript** | [list[RecordingMessagingMessage]](RecordingMessagingMessage) | Represents a messaging transcript | [optional] |
| **file_state** | str | Represents the current file state for a recording. Examples: Uploading, Archived, etc | [optional] |
| **restore_expiration_time** | datetime | The amount of time a restored recording will remain restored before being archived again. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **media_uris** | [dict(str, MediaResult)](MediaResult) | The different mediaUris for the recording. Null when there is no playable media. | [optional] |
| **estimated_transcode_time_ms** | int |  | [optional] |
| **actual_transcode_time_ms** | int |  | [optional] |
| **archive_date** | datetime | The date the recording will be archived. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **archive_medium** | str | The type of archive medium used. Example: CloudArchive | [optional] |
| **delete_date** | datetime | The date the recording will be deleted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **export_date** | datetime | The date the recording will be exported. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **exported_date** | datetime | The date the recording was exported. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **output_duration_ms** | int | Duration of transcoded media in milliseconds | [optional] |
| **output_size_in_bytes** | int | Size of transcoded media in bytes. 0 if there is no transcoded media. | [optional] |
| **max_allowed_restorations_for_org** | int | How many archive restorations the organization is allowed to have. | [optional] |
| **remaining_restorations_allowed_for_org** | int | The remaining archive restorations the organization has. | [optional] |
| **session_id** | str | The session id represents an external resource id, such as email, call, chat, etc | [optional] |
| **users** | [list[User]](User) | The users participating in the conversation | [optional] |
| **recording_file_role** | str | Role of the file recording. It can be either customer_experience or adhoc. | [optional] |
| **recording_error_status** | str | Status of a recording that cannot be returned because of an error | [optional] |
| **original_recording_start_time** | datetime | The start time of the full recording, before any segment access restrictions are applied. Null when there is no playable media. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **creation_time** | datetime | The creation time of the recording. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.0.0_

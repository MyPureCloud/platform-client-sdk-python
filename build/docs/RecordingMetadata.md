# RecordingMetadata

## RecordingMetadata

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **conversation_id** | str |  | [optional] |
| **path** | str |  | [optional] |
| **start_time** | str | The start time of the recording for screen recordings. Null for other types. | [optional] |
| **end_time** | str |  | [optional] |
| **media** | str | The type of media that the recording is. At the moment that could be audio, chat, email, or message. | [optional] |
| **media_subtype** | str | The recording media subtype. | [optional] |
| **media_subject** | str | The recording media subject. | [optional] |
| **annotations** | [list[Annotation]](Annotation) | Annotations that belong to the recording. Populated when recording filestate is AVAILABLE. | [optional] |
| **file_state** | str | Represents the current file state for a recording. Examples: Uploading, Archived, etc | [optional] |
| **restore_expiration_time** | datetime | The amount of time a restored recording will remain restored before being archived again. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **archive_date** | datetime | The date the recording will be archived. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **archive_medium** | str | The type of archive medium used. Example: CloudArchive | [optional] |
| **delete_date** | datetime | The date the recording will be deleted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **export_date** | datetime | The date the recording will be exported. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **exported_date** | datetime | The date the recording was exported. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **max_allowed_restorations_for_org** | int | How many archive restorations the organization is allowed to have. | [optional] |
| **remaining_restorations_allowed_for_org** | int | The remaining archive restorations the organization has. | [optional] |
| **session_id** | str | The session id represents an external resource id, such as email, call, chat, etc | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 217.0.0_

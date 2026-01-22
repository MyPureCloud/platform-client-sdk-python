# VoicemailMessage

## VoicemailMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **conversation** | [Conversation](Conversation) | The conversation that the voicemail message is associated with | [optional] |
| **read** | bool | Whether the voicemail message is marked as read | [optional] |
| **audio_recording_duration_seconds** | int | The voicemail message&#39;s audio recording duration in seconds | [optional] |
| **audio_recording_size_bytes** | int | The voicemail message&#39;s audio recording size in bytes | [optional] |
| **transcription** | str | The transcription of the voicemail&#39;s audio | [optional] |
| **created_date** | datetime | The date the voicemail message was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_date** | datetime | The date the voicemail message was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **deleted_date** | datetime | The date the voicemail message deleted property was set to true. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **caller_address** | str | The caller address | [optional] |
| **caller_name** | str | Optionally the name of the caller that left the voicemail message if the caller was a known user | [optional] |
| **caller_user** | [User](User) | Optionally the user that left the voicemail message if the caller was a known user | [optional] |
| **deleted** | bool | Whether the voicemail message has been marked as deleted | [optional] |
| **note** | str | An optional note | [optional] |
| **user** | [User](User) | The user that the voicemail message belongs to or null which means the voicemail message belongs to a group or queue | [optional] |
| **group** | [Group](Group) | The group that the voicemail message belongs to or null which means the voicemail message belongs to a user or queue | [optional] |
| **queue** | [Queue](Queue) | The queue that the voicemail message belongs to or null which means the voicemail message belongs to a user or group | [optional] |
| **copied_from** | [VoicemailCopyRecord](VoicemailCopyRecord) | Represents where this voicemail message was copied from | [optional] |
| **copied_to** | [list[VoicemailCopyRecord]](VoicemailCopyRecord) | Represents where this voicemail has been copied to | [optional] |
| **delete_retention_policy** | [VoicemailRetentionPolicy](VoicemailRetentionPolicy) | The retention policy for this voicemail when deleted is set to true | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 249.0.0_

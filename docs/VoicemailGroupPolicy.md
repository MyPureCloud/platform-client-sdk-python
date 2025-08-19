# VoicemailGroupPolicy

## VoicemailGroupPolicy

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str |  | [optional] |
| **group** | [Group](Group) | The group associated with the policy | [optional] |
| **enabled** | bool | Whether voicemail is enabled for the group | [optional] |
| **send_email_notifications** | bool | Whether email notifications are sent to group members when a new voicemail is received | [optional] |
| **disable_email_pii** | bool | Removes any PII from group emails. This is overridden by the analogous organization configuration value. This is always true if HIPAA is enabled or unknown for an organization. | [optional] |
| **include_email_transcriptions** | bool | Whether to include the voicemail transcription in a group notification email | [optional] |
| **language_preference** | str | The language preference for the group.  Used for group voicemail transcription | [optional] |
| **email_policy** | [GroupEmailPolicy](GroupEmailPolicy) | The email policy for the group | [optional] |
| **rotate_calls_secs** | int | How many seconds to ring before rotating to the next member in the group | [optional] |
| **stop_ringing_after_rotations** | int | How many rotations to go through | [optional] |
| **overflow_group_id** | str | A fallback group to contact when all of the members in this group did not answer the call. | [optional] |
| **group_alert_type** | str | Specifies if the members in this group should be contacted randomly, in a specific order, or by round-robin. | [optional] |
| **interactive_response_prompt_id** | str | The prompt to use when connecting a user to a Group Ring call | [optional] |
| **interactive_response_required** | bool | Whether user should be prompted with a confirmation prompt when connecting to a Group Ring call | [optional] |



_PureCloudPlatformClientV2 235.1.0_

# VoicemailOrganizationPolicy

## VoicemailOrganizationPolicy

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enabled** | bool | Whether voicemail is enabled for this organization | [optional] |
| **alert_timeout_seconds** | int | The organization&#39;s default number of seconds to ring a user&#39;s phone before a call is transferred to voicemail | [optional] |
| **pin_configuration** | [PINConfiguration](PINConfiguration) | The configuration for user PINs to access their voicemail from a phone | [optional] |
| **voicemail_extension** | str | The extension for voicemail retrieval.  The default value is *86. | [optional] |
| **pin_required** | bool | If this is true, a PIN is required when accessing a user&#39;s voicemail from a phone. | [optional] |
| **interactive_response_required** | bool | Whether user should be prompted with a confirmation prompt when connecting to a Group Ring call | [optional] |
| **send_email_notifications** | bool | Whether email notifications are sent for new voicemails in the organization. If false, new voicemail email notifications are not be sent for the organization overriding any user or group setting. | [optional] |
| **include_email_transcriptions** | bool | Whether to include the voicemail transcription in the notification email | [optional] |
| **disable_email_pii** | bool | Removes any PII from emails. This overrides any analogous group configuration value. This is always true if HIPAA is enabled or unknown for an organization. | [optional] |
| **maximum_recording_time_seconds** | int | Default value for the maximum length of time in seconds of a recorded voicemail | [optional] |
| **modified_date** | datetime | The date the policy was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 218.0.0_

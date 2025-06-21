# VoicemailUserPolicy

## VoicemailUserPolicy

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enabled** | bool | Whether the user has voicemail enabled | [optional] |
| **alert_timeout_seconds** | int | The number of seconds to ring the user&#39;s phone before a call is transfered to voicemail | [optional] |
| **pin** | str | The user&#39;s PIN to access their voicemail. This property is only used for updates and never provided otherwise to ensure security | [optional] |
| **modified_date** | datetime | The date the policy was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **send_email_notifications** | bool | Whether email notifications are sent to the user when a new voicemail is received | [optional] |



_PureCloudPlatformClientV2 231.0.0_

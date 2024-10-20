# CallbackMediaSettings

## CallbackMediaSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enable_auto_answer** | bool | Indicates if auto-answer is enabled for the given media type or subtype (default is false).  Subtype settings take precedence over media type settings. | [optional] |
| **alerting_timeout_seconds** | int | The alerting timeout for the media type, in seconds | [optional] |
| **service_level** | [ServiceLevel](ServiceLevel) | The targeted service level for the media type | [optional] |
| **auto_answer_alert_tone_seconds** | float | How long to play the alerting tone for an auto-answer interaction | [optional] |
| **manual_answer_alert_tone_seconds** | float | How long to play the alerting tone for a manual-answer interaction | [optional] |
| **sub_type_settings** | [dict(str, BaseMediaSettings)](BaseMediaSettings) | Map of media subtype to media subtype specific settings. | [optional] |
| **enable_auto_dial_and_end** | bool | Flag to enable Auto-Dial and Auto-End automation for callbacks on this queue. | [optional] |
| **auto_dial_delay_seconds** | int | Time in seconds after agent connects to callback before outgoing call is auto-dialed. Allowable values in range 0 - 1200 seconds. Defaults to 300 seconds. | [optional] |
| **auto_end_delay_seconds** | int | Time in seconds after agent disconnects from the outgoing call before the encasing callback is auto-ended. Allowable values in range 0 - 1200 seconds. Defaults to 300 seconds. | [optional] |



_PureCloudPlatformClientV2 214.0.0_

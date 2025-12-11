# MessageMediaSettings

## MessageMediaSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enable_auto_answer** | bool | Indicates if auto-answer is enabled for the given media type or subtype (default is false).  Subtype settings take precedence over media type settings. | [optional] |
| **alerting_timeout_seconds** | int | The alerting timeout for the media type, in seconds | [optional] |
| **service_level** | [ServiceLevel](ServiceLevel) | The targeted service level for the media type | [optional] |
| **auto_answer_alert_tone_seconds** | float | How long to play the alerting tone for an auto-answer interaction | [optional] |
| **manual_answer_alert_tone_seconds** | float | How long to play the alerting tone for a manual-answer interaction | [optional] |
| **sub_type_settings** | [dict(str, MessageSubtypeSettings)](MessageSubtypeSettings) | Map of media subtype to media subtype specific settings. | [optional] |
| **enable_inactivity_timeout** | bool | Indicates if inactivity timeout is enabled for all subtypes. | [optional] |
| **inactivity_timeout_settings** | [InactivityTimeoutSettings](InactivityTimeoutSettings) | Inactivity timeout settings for messages | [optional] |



_PureCloudPlatformClientV2 246.0.0_

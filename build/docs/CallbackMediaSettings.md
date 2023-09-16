---
title: CallbackMediaSettings
---
## CallbackMediaSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enable_auto_answer** | **bool** | Indicates if auto-answer is enabled for the given media type or subtype (default is false).  Subtype settings take precedence over media type settings. | [optional] |
| **alerting_timeout_seconds** | **int** |  | [optional] |
| **service_level** | [**ServiceLevel**](ServiceLevel.html) |  | [optional] |
| **auto_answer_alert_tone_seconds** | **float** |  | [optional] |
| **manual_answer_alert_tone_seconds** | **float** |  | [optional] |
| **sub_type_settings** | [**dict(str, BaseMediaSettings)**](BaseMediaSettings.html) | Map of media subtype to media subtype specific settings. | [optional] |
{: class="table table-striped"}



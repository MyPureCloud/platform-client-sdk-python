# TtsEngineEntity

## TtsEngineEntity

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **languages** | list[str] | The set of languages the TTS engine supports | |
| **output_formats** | list[str] | The set of output formats the TTS engine can produce | |
| **voices** | [list[TtsVoiceEntity]](TtsVoiceEntity) | The set of voices the TTS engine supports | [optional] |
| **is_default** | bool | The TTS engine is the global default engine | [optional] |
| **is_secure** | bool | The TTS engine can be used in a secure call flow | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 216.0.0_

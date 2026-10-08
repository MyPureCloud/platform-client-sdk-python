# TtsVoiceEntity

## TtsVoiceEntity

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **display_name** | str | The display name of the TTS voice | [optional] |
| **gender** | str | The gender of the TTS voice | |
| **voice_type** | str | The type of the TTS voice | [optional] |
| **language** | str | The language supported by the TTS voice | |
| **engine** | [TtsEngineEntity](TtsEngineEntity) | Ths TTS engine this voice belongs to | |
| **is_default** | bool | The voice is the default voice for its language | [optional] |
| **supported_models** | list[str] | The models supported by the TTS voice | [optional] |
| **provider** | str | The provider of the TTS voice | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 269.0.0_

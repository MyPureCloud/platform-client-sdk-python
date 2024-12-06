# RecordingSettings

## RecordingSettings

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **max_simultaneous_streams** | int | Maximum number of simultaneous screen recording streams | [optional] |
| **max_configurable_screen_recording_streams** | int | Upper limit that maxSimultaneousStreams can be configured | [optional] |
| **regional_recording_storage_enabled** | bool | Store call recordings in the region where they are intended to be recorded, otherwise in the organization&#39;s home region | [optional] |
| **recording_playback_url_ttl** | int | The duration in minutes for which the generated URL for recording playback remains valid.The default duration is set to 60 minutes, with a minimum allowable duration of 2 minutes and a maximum of 60 minutes. | [optional] |
| **recording_batch_download_url_ttl** | int | The duration in minutes for which the generated URL for recording batch download remains valid.The default duration is set to 60 minutes, with a minimum allowable duration of 2 minutes and a maximum of 60 minutes. | [optional] |



_PureCloudPlatformClientV2 217.0.0_

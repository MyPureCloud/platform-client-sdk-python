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
| **mode** | str | The mode callbacks will use on this queue. | [optional] |
| **enable_auto_dial_and_end** | bool | Flag to enable Auto-Dial and Auto-End automation for callbacks on this queue. | [optional] |
| **auto_dial_delay_seconds** | int | Time in seconds after agent connects to callback before outgoing call is auto-dialed. Allowable values in range 0 - 1200 seconds. Defaults to 300 seconds. | [optional] |
| **auto_end_delay_seconds** | int | Time in seconds after agent disconnects from the outgoing call before the encasing callback is auto-ended. Allowable values in range 0 - 1200 seconds. Defaults to 300 seconds. | [optional] |
| **pacing_modifier** | float | Controls the maximum number of outbound calls at one time when mode is CustomerFirst. | [optional] |
| **max_retry_count** | int | Maximum number of retries that should be attempted to try and connect a customer first callback to a customer when the initial callback attempt did not connect. | [optional] |
| **retry_delay_seconds** | int | Delay in seconds between each retry of a customer first callback. | [optional] |
| **live_voice_reaction_type** | str | The action to take if a live voice is detected during the outbound call of a customer first callback. | [optional] |
| **live_voice_flow** | [DomainEntityRef](DomainEntityRef) | The inbound flow to transfer to if a live voice is detected during the outbound call of a customer first callback. | [optional] |
| **answering_machine_reaction_type** | str | The action to take if an answering machine is detected during the outbound call of a customer first callback. | [optional] |
| **answering_machine_flow** | [DomainEntityRef](DomainEntityRef) | The inbound flow to transfer to if an answering machine is detected during the outbound call of a customer first callback when answeringMachineReactionType is set to TransferToFlow. | [optional] |



_PureCloudPlatformClientV2 235.1.0_

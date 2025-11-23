# TransferToAgentRequest

## TransferToAgentRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **transfer_type** | str | The type of transfer to perform. Attended, where the initiating agent maintains ownership of the conversation until the intended recipient accepts the transfer, or Unattended, where the initiating agent immediately disconnects. Default is Unattended. | [optional] |
| **keep_internal_message_alive** | bool | If true, the digital internal message will NOT be terminated. | [optional] |
| **user_id** | str | The id of the internal user. | [optional] |
| **user_name** | str | The userName (like user’s email) of the internal user. | [optional] |
| **user_display_name** | str | The name of the internal user. | [optional] |
| **voicemail** | bool | If true, transfer to the voicemail inbox of the participant that is being replaced. | [optional] |



_PureCloudPlatformClientV2 244.0.0_

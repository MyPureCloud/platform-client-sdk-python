# TransferRequest

## TransferRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **transfer_type** | str | The type of transfer to perform. Attended, where the initiating agent maintains ownership of the conversation until the intended recipient accepts the transfer, or Unattended, where the initiating agent immediately disconnects. Default is Unattended. | [optional] |
| **keep_internal_message_alive** | bool | If true, the digital internal message will NOT be terminated. | [optional] |
| **user_id** | str | The user ID of the transfer target. | [optional] |
| **address** | str | The user ID or queue ID of the transfer target. Address like a phone number can not be used for callbacks, but they can be used for other forms of communication. | [optional] |
| **user_name** | str | The user name of the transfer target. | [optional] |
| **queue_id** | str | The queue ID of the transfer target. | [optional] |
| **voicemail** | bool | If true, transfer to the voicemail inbox of the participant that is being replaced. | [optional] |



_PureCloudPlatformClientV2 235.1.0_

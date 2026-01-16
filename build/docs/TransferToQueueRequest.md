# TransferToQueueRequest

## TransferToQueueRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **transfer_type** | str | The type of transfer to perform. Attended, where the initiating agent maintains ownership of the conversation until the intended recipient accepts the transfer, or Unattended, where the initiating agent immediately disconnects. Default is Unattended. | [optional] |
| **keep_internal_message_alive** | bool | If true, the digital internal message will NOT be terminated. | [optional] |
| **queue_id** | str | The id of the queue. | [optional] |
| **queue_name** | str | The name of the queue. | [optional] |



_PureCloudPlatformClientV2 248.0.0_

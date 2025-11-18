# TransferToExternalContactRequest

## TransferToExternalContactRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **transfer_type** | str | The type of transfer to perform. Attended, where the initiating agent maintains ownership of the conversation until the intended recipient accepts the transfer, or Unattended, where the initiating agent immediately disconnects. Default is Unattended. | [optional] |
| **keep_internal_message_alive** | bool | If true, the digital internal message will NOT be terminated. | [optional] |
| **contact_id** | str | The external contact id. | |
| **phone_type** | str | The external contact phone type. | |



_PureCloudPlatformClientV2 243.0.0_

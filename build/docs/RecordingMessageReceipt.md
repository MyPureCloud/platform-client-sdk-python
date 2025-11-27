# RecordingMessageReceipt

## RecordingMessageReceipt

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The id of the message receipt. Message receipts will have the same ID as the message they reference. | [optional] |
| **status** | str | The message receipt status | [optional] |
| **reasons** | [list[RecordingMessageReceiptReason]](RecordingMessageReceiptReason) | List of reasons for a message receipt that indicates the message has failed. Only used with Failed status. | [optional] |



_PureCloudPlatformClientV2 245.0.0_

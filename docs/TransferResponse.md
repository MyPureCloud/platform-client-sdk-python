# TransferResponse

## TransferResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The id of the command. | [optional] |
| **state** | str | The state of the command. | [optional] |
| **date_issued** | datetime | The date/time that this command was issued. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **initiator** | [TransferInitiator](TransferInitiator) | The initiator of the command. | [optional] |
| **modified_by** | [TransferResponseModifiedBy](TransferResponseModifiedBy) | The user or entity that modified the command. | [optional] |
| **destination** | [TransferDestination](TransferDestination) | The destination of the command. | [optional] |
| **transfer_type** | str | The type of transfer to perform. | [optional] |



_PureCloudPlatformClientV2 247.0.0_

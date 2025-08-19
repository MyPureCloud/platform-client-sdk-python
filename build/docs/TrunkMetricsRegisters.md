# TrunkMetricsRegisters

## TrunkMetricsRegisters

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **proxy_address** | str | Server proxy address that this registers array element represents. | [optional] |
| **register_state** | bool | True if last REGISTER message had positive response; false if error response or no response. | [optional] |
| **register_state_time** | datetime | ISO 8601 format UTC absolute date &amp; time of the last change of the register state. | [optional] |
| **error_info** | [TrunkErrorInfo](TrunkErrorInfo) |  | [optional] |



_PureCloudPlatformClientV2 235.1.0_

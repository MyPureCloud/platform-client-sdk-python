# FunctionConfig

## FunctionConfig

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Action identifier. | [optional] |
| **function** | [Function](Function) | Function configuration. | [optional] |
| **zip** | [FunctionZipConfig](FunctionZipConfig) | Zip file configuration and state. | [optional] |
| **upload_exception_history** | [list[FunctionZipConfig]](FunctionZipConfig) | History of failed zip upload file configuration including their state and error messages. Contains no more than last ten failures. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 247.0.0_

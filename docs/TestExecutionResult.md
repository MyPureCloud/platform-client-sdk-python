# TestExecutionResult

## TestExecutionResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **operations** | [list[TestExecutionOperationResult]](TestExecutionOperationResult) | Execution operations performed as part of the test | [optional] |
| **error** | [ErrorBody](ErrorBody) | The final error encountered during the test that resulted in test failure | [optional] |
| **final_result** | object | The final result of the test. This is the response that would be returned during normal action execution | [optional] |
| **success** | bool | Indicates whether or not the test was a success | [optional] |



_PureCloudPlatformClientV2 239.0.0_

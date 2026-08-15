# DecisionTableImportJobError

## DecisionTableImportJobError

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **error_code** | str | The error code for this job failure. | [optional] |
| **error_message** | str | A human-readable error message. | [optional] |
| **message_with_params** | str | Parameterized message template for the aggregate failure (when applicable) | [optional] |
| **message_params** | dict(str, str) | Parameters for messageWithParams | [optional] |
| **validation_errors** | [list[DecisionTableJobValidationError]](DecisionTableJobValidationError) | Validation failures for individual rows or the file structure | [optional] |



_PureCloudPlatformClientV2 264.0.0_

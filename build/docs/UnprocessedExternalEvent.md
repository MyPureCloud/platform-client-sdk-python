# UnprocessedExternalEvent

## UnprocessedExternalEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event** | [ExternalEvent](ExternalEvent) | The event that failed processing. | |
| **original_request_index** | int | The index of the event in the original request. | |
| **is_retryable** | bool | Whether the error is retryable. | |
| **error_message** | str | The error message. | |
| **status_code** | int | The HTTP status code associated with the error. | [optional] |



_PureCloudPlatformClientV2 257.1.0_

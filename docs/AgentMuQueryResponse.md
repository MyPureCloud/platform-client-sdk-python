# AgentMuQueryResponse

## AgentMuQueryResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **status** | str | The status of the operation | |
| **operation_id** | str | The ID for the operation | |
| **result** | [AgentMuScheduleResult](AgentMuScheduleResult) | The schema of the result of the operation. Null if downloadUrl is populated, but defines the schema of the data that will be returned from the downloadUrl | [optional] |
| **download_url** | str | The URL from which to download the result. The result will follow the schema documented by the result field | [optional] |
| **error** | [ErrorBody](ErrorBody) | Error details if status &#x3D;&#x3D; &#39;Error&#39;. Will always be null but the schema is documented in case of an error in an async notification | [optional] |



_PureCloudPlatformClientV2 244.0.0_

# BuAsyncAgentSchedulesSearchResponse

## BuAsyncAgentSchedulesSearchResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **status** | str | The status of the operation | [optional] |
| **operation_id** | str | The ID for the operation | [optional] |
| **result** | [BuAgentSchedulesSearchResponse](BuAgentSchedulesSearchResponse) | The result of the operation.  Null unless status &#x3D;&#x3D; Complete | [optional] |
| **progress** | int | Percent progress for the operation | [optional] |
| **download_url** | str | The URL from which to download the result if it is too large to pass directly | [optional] |



_PureCloudPlatformClientV2 227.1.0_

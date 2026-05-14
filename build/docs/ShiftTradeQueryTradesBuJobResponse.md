# ShiftTradeQueryTradesBuJobResponse

## ShiftTradeQueryTradesBuJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | |
| **status** | str | The status of the job | |
| **type** | str | The type of the job | |
| **download_url** | str | The URL where completed results might be available for download in case the result body for that job type is too large | [optional] |
| **error** | [ErrorBody](ErrorBody) | Any error information, only set if the status &#x3D;&#x3D; &#39;Error&#39; | [optional] |
| **query_trades_result** | [ShiftTradeListJobResponse](ShiftTradeListJobResponse) | Results for QueryTrades job type | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 257.1.0_

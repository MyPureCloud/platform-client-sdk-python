# WfmHistoricalShrinkageResponse

## WfmHistoricalShrinkageResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **operation_id** | str | The operationId for which to listen | [optional] |
| **download_urls** | list[str] | The url list to GET the results of the Historical Shrinkage query. This field is populated only if query state is Complete | [optional] |
| **download_result** | [HistoricalShrinkageResultListing](HistoricalShrinkageResultListing) | Result will always come via downloadUrls; however the schema is included for documentation | [optional] |
| **state** | str | The state of the shrinkage query | [optional] |



_PureCloudPlatformClientV2 211.1.0_

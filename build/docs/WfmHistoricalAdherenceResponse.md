# WfmHistoricalAdherenceResponse

## WfmHistoricalAdherenceResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The query ID to listen for | [optional] |
| **download_url** | str | Deprecated. Use downloadUrls instead. | [optional] |
| **download_result** | [WfmHistoricalAdherenceResultWrapper](WfmHistoricalAdherenceResultWrapper) | Result will always come via downloadUrls; however the schema is included for documentation | [optional] |
| **download_urls** | list[str] | The uri list to GET the results of the Historical Adherence query. For notification purposes only | [optional] |
| **query_state** | str | The state of the adherence query | [optional] |



_PureCloudPlatformClientV2 218.0.0_

# WfmAgentHistoricalAdherenceResponse

## WfmAgentHistoricalAdherenceResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **job** | [WfmAgentHistoricalAdherenceJobReference](WfmAgentHistoricalAdherenceJobReference) | A reference to the job that was started by the request | |
| **download_urls** | list[str] | The url list to GET the results of the agent adherence query. This field is populated only if query state is Complete | [optional] |
| **result** | [WfmAgentHistoricalAdherenceResult](WfmAgentHistoricalAdherenceResult) | Results will come via downloadUrls, however it may come inline if small enough | [optional] |



_PureCloudPlatformClientV2 247.0.0_

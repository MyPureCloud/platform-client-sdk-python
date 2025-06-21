# PerformancePredictionRecalculationResponse

## PerformancePredictionRecalculationResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **operation_id** | str | The operationId for which to listen | |
| **download_url** | str | The url to GET the results of the performance prediction. This field is populated only if query state is &#39;Complete&#39; | [optional] |
| **download_result** | [PerformancePredictionOutputs](PerformancePredictionOutputs) | Result will always come via downloadUrls; however the schema is included for documentation | [optional] |
| **state** | str | The state of the performance prediction | |



_PureCloudPlatformClientV2 231.0.0_

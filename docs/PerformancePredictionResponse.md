# PerformancePredictionResponse

## PerformancePredictionResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **week_date** | date | The weekDate of the short term forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **schedule_id** | str | The ID of the schedule this performance prediction is associated with | |
| **download_url** | str | The url to GET the results of the performance prediction. This field is populated only if query state is &#39;Complete&#39; | [optional] |
| **download_result** | [PerformancePredictionOutputs](PerformancePredictionOutputs) | Result will always come via downloadUrls; however the schema is included for documentation | [optional] |
| **state** | str | The state of the performance prediction | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.0.0_

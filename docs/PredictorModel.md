# PredictorModel

## PredictorModel

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **kpi** | str | The key performance indicator used in the model. | [optional] |
| **queues** | [list[AddressableEntityRef]](AddressableEntityRef) | The List of Queues that are assessed for Predictive Routing. | [optional] |
| **date_created** | datetime | DateTime indicating when the model was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_trained** | datetime | DateTime indicating when the model was last trained. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **media_type** | str | The media type of the model. | [optional] |
| **features** | [list[PredictorModelFeature]](PredictorModelFeature) |  | [optional] |



_PureCloudPlatformClientV2 211.0.0_

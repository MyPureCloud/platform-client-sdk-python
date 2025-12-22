# Predictor

## Predictor

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **queues** | [list[AddressableEntityRef]](AddressableEntityRef) | The queue IDs associated with the predictor. | |
| **kpi** | str | The KPI that the predictor attempts to maximize/minimize. | |
| **routing_timeout_seconds** | int | Number of seconds allocated to predictive routing before attempting a different routing method. This is a value between 12 and 900 seconds. | [optional] |
| **schedule** | [PredictorSchedule](PredictorSchedule) | The predictor schedule that determines when the predictor is used for routing interactions. | [optional] |
| **state** | str | The predictor state. | [optional] |
| **date_created** | datetime | DateTime indicating when the predictor was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | DateTime indicating when the predictor was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **workload_balancing_config** | [PredictorWorkloadBalancing](PredictorWorkloadBalancing) | The predictor balancing configuration to enable workload balancing. | [optional] |
| **error_code** | str | Predictor error code - optional details on why the predictor went into error state. | [optional] |
| **models** | [list[PredictorModelBrief]](PredictorModelBrief) | Predictor&#39;s models | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.1.0_

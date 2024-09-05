# PatchPredictorRequest

## PatchPredictorRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **routing_timeout_seconds** | int | Number of seconds allocated to predictive routing before attempting a different routing method. This is a value between 12 and 900 seconds. | [optional] |
| **schedule** | [PredictorSchedule](PredictorSchedule) | The predictor schedule that determines when the predictor is used for routing interactions. | [optional] |
| **workload_balancing_config** | [PredictorWorkloadBalancing](PredictorWorkloadBalancing) | The predictor balancing configuration to enable workload balancing | [optional] |



_PureCloudPlatformClientV2 210.0.0_

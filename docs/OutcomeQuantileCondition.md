# OutcomeQuantileCondition

## OutcomeQuantileCondition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **outcome_id** | str | The outcome ID. | |
| **max_quantile_threshold** | float | This Outcome Quantile Condition is met when sessionMaxQuantile of the OutcomeScore is above this value, (unless fallbackQuantile is set). Range 0.00-1.00 | |
| **fallback_quantile_threshold** | float | (Optional) If set, this Condition is met when maxQuantileThreshold is met, AND the current quantile of the OutcomeScore is below this fallbackQuantileThreshold. Range 0.00-1.00 | [optional] |



_PureCloudPlatformClientV2 245.0.0_

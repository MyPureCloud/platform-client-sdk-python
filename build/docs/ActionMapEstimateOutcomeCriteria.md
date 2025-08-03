# ActionMapEstimateOutcomeCriteria

## ActionMapEstimateOutcomeCriteria

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **outcome_id** | str | ID of outcome. | |
| **max_probability** | float | Probability value for the selected outcome at or above which the action map will trigger. | [optional] |
| **probability** | float | Additional probability condition, where if set, the action map will trigger if the current outcome probability is lower or equal to the value. | [optional] |
| **quantile** | float | Represents the quantity of sessions that have a maximum probability less than the predicted probability. | [optional] |
| **max_quantile** | float | Represents the quantity of sessions that have a maximum probability less than the predicted session max probability. | [optional] |



_PureCloudPlatformClientV2 234.0.0_

# OutcomeScore

## OutcomeScore

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **outcome** | [AddressableEntityRef](AddressableEntityRef) | The outcome that the score was calculated for. | [optional] |
| **session_max_probability** | float | Represents the max probability reached in the session. | [optional] |
| **probability** | float | Represents the likelihood of a customer reaching or achieving a given outcome. | [optional] |
| **percentile** | int | (Deprecated: use the &#39;quantile&#39; field instead) Represents the predicted probability&#39;s percentile score when compared with all other generated probabilities for a given outcome. | [optional] |
| **session_max_percentile** | int | (Deprecated: use the &#39;quantile&#39; field instead) Represents the maximum likelihood percentile score reached for a given outcome by the current session. | [optional] |
| **quantile** | float | Represents the quantity of sessions that have a maximum probability less than the predicted probability. | [optional] |
| **session_max_quantile** | float | Represents the quantity of sessions that have a maximum probability less than the predicted session max probability. | [optional] |



_PureCloudPlatformClientV2 232.0.0_

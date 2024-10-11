# FlowHealthIntentUtterance

## FlowHealthIntentUtterance

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **text** | str | Utterance Text. | [optional] |
| **issue_count** | int | Number of issues found for this utterance. | [optional] |
| **static_validation_results** | list[str] | Validation results for this utterance. | [optional] |
| **outlier_info** | [OutlierInfo](OutlierInfo) | Details about this utterance being an outlier or not. | [optional] |
| **confusion_info** | [ConfusionInfo](ConfusionInfo) | Confusion details with other utterances. | [optional] |



_PureCloudPlatformClientV2 213.0.0_

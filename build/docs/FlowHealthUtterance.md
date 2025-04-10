# FlowHealthUtterance

## FlowHealthUtterance

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **text** | str | Utterance Text. | [optional] |
| **issue_count** | int | Number of issues found for this utterance. | [optional] |
| **language** | str | Language provided for this utterance&#39;s health. | [optional] |
| **static_validation_results** | list[str] | Validation results for the utterance. | [optional] |
| **outlier_info** | [OutlierInfo](OutlierInfo) | Details about this utterance being an outlier or not. | [optional] |
| **confusion_info** | [ConfusionDetails](ConfusionDetails) | Confusion details with other utterances. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 225.0.0_

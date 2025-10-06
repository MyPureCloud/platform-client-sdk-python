# AssessmentFormQuestionGroup

## AssessmentFormQuestionGroup

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the question group, | [optional] |
| **name** | str | The question group name | |
| **type** | str | The question group type | |
| **context_id** | str | An identifier for this question group that stays the same across versions of the form. | [optional] |
| **default_answers_to_highest** | bool |  | [optional] |
| **default_answers_to_na** | bool |  | [optional] |
| **na_enabled** | bool |  | [optional] |
| **weight** | float |  | [optional] |
| **manual_weight** | bool |  | [optional] |
| **questions** | [list[AssessmentFormQuestion]](AssessmentFormQuestion) | The list of questions for this question group | |
| **visibility_condition** | [VisibilityCondition](VisibilityCondition) |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 240.0.0_

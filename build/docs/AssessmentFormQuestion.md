# AssessmentFormQuestion

## AssessmentFormQuestion

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str |  | [optional] |
| **type** | str |  | [optional] |
| **text** | str | The question text | |
| **help_text** | str |  | [optional] |
| **na_enabled** | bool |  | [optional] |
| **comments_required** | bool |  | [optional] |
| **visibility_condition** | [VisibilityCondition](VisibilityCondition) |  | [optional] |
| **answer_options** | [list[AnswerOption]](AnswerOption) | Options from which to choose an answer for this question. Only used by Multiple Choice type questions. | [optional] |
| **max_response_characters** | int | How many characters are allowed in the text response to this question. Used by Free Text question types. | [optional] |
| **is_kill** | bool | Does an incorrect answer to this question mark the form as having a failed kill question. Only used by Multiple Choice type questions. | [optional] |
| **is_critical** | bool | Does this question contribute to the critical score. Only used by Multiple Choice type questions. | [optional] |



_PureCloudPlatformClientV2 221.0.0_

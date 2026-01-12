# EvaluationQuestion

## EvaluationQuestion

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str |  | [optional] |
| **context_id** | str | An identifier for this question that stays the same across versions of the form. | [optional] |
| **text** | str |  | [optional] |
| **help_text** | str |  | [optional] |
| **type** | str |  | [optional] |
| **na_enabled** | bool |  | [optional] |
| **comments_required** | bool |  | [optional] |
| **visibility_condition** | [VisibilityCondition](VisibilityCondition) |  | [optional] |
| **answer_options** | [list[AnswerOption]](AnswerOption) | Options from which to choose an answer for this question. Only used by Multiple Choice type questions. | [optional] |
| **multiple_select_option_questions** | [list[EvaluationQuestion]](EvaluationQuestion) | Only used by Multiple Select type questions. A list of multiple choice questions representing selectable options. | [optional] |
| **default_answer** | [DefaultAnswer](DefaultAnswer) | The default selected answer for the question | [optional] |
| **is_kill** | bool |  | [optional] |
| **is_critical** | bool |  | [optional] |



_PureCloudPlatformClientV2 247.0.0_

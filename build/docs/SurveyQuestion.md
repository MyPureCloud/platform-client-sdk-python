---
title: SurveyQuestion
---
## SurveyQuestion

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **text** | **str** |  | [optional] |
| **help_text** | **str** |  | [optional] |
| **type** | **str** |  | [optional] |
| **na_enabled** | **bool** |  | [optional] |
| **visibility_condition** | [**VisibilityCondition**](VisibilityCondition.html) |  | [optional] |
| **answer_options** | [**list[AnswerOption]**](AnswerOption.html) | Options from which to choose an answer for this question. Only used by Multiple Choice type questions. | [optional] |
| **max_response_characters** | **int** | How many characters are allowed in the text response to this question. Used by NPS and Free Text question types. | [optional] |
| **explanation_prompt** | **str** | Prompt for details explaining the chosen NPS score. Used by NPS questions. | [optional] |
{: class="table table-striped"}



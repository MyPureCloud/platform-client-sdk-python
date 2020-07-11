---
title: SurveyForm
---
## SurveyForm

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The survey form name | |
| **modified_date** | **datetime** | Last modified date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **published** | **bool** | Is this form published | [optional] |
| **disabled** | **bool** | Is this form disabled | [optional] |
| **context_id** | **str** | Unique Id for all versions of this form | |
| **language** | **str** | Language for survey viewer localization. Currently localized languages: da, de, en-US, es, fi, fr, it, ja, ko, nl, no, pl, pt-BR, sv, th, tr, zh-CH, zh-TW | |
| **header** | **str** | Markdown text for the top of the form. | [optional] |
| **footer** | **str** | Markdown text for the bottom of the form. | [optional] |
| **question_groups** | [**list[SurveyQuestionGroup]**](SurveyQuestionGroup.html) | A list of question groups | |
| **published_versions** | [**DomainEntityListingSurveyForm**](DomainEntityListingSurveyForm.html) | List of published version of this form | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



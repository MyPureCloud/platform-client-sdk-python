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
| **header_image_id** | **str** | Id of the header image appearing at the top of the form. | [optional] |
| **header_image_url** | **str** | Temporary URL for accessing header image | [optional] |
| **header** | **str** | Markdown text for the top of the form. | [optional] |
| **footer** | **str** | Markdown text for the bottom of the form. | [optional] |
| **question_groups** | [**list[QuestionGroup]**](QuestionGroup.html) | A list of question groups | |
| **published_versions** | [**DomainEntityListingSurveyForm**](DomainEntityListingSurveyForm.html) | List of published version of this form | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



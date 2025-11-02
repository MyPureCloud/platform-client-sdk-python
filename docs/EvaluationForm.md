# EvaluationForm

## EvaluationForm

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The evaluation form name | |
| **modified_date** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **published** | bool |  | [optional] |
| **context_id** | str |  | [optional] |
| **question_groups** | [list[EvaluationQuestionGroup]](EvaluationQuestionGroup) | A list of question groups | |
| **published_versions** | [DomainEntityListingEvaluationForm](DomainEntityListingEvaluationForm) | A list of the published versions of this form. Not populated by default, its availability depends on the endpoint. Use the &#39;expand&#x3D;publishHistory&#39; query parameter to retrieve this data where applicable (refer to the endpoint description to see if it is applicable). | [optional] |
| **evaluation_settings** | [EvaluationSettings](EvaluationSettings) | Settings for evaluations associated with this form | [optional] |
| **ai_scoring** | [AiScoringSettings](AiScoringSettings) | AI scoring settings for the evaluation form. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 242.0.0_

# AssessmentForm

## AssessmentForm

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **date_modified** | datetime | Last modified date of the assessment form. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **context_id** | str | The unique Id for all versions of this assessment form | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **published** | bool | If true, assessment form is published | [optional] |
| **pass_percent** | int | The pass percent for the assessment form | |
| **question_groups** | [list[AssessmentFormQuestionGroup]](AssessmentFormQuestionGroup) | A list of question groups | |



_PureCloudPlatformClientV2 238.0.0_

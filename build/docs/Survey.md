---
title: Survey
---
## Survey

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **conversation** | [**Conversation**](Conversation.html) |  | [optional] |
| **survey_form** | [**SurveyForm**](SurveyForm.html) | Survey form used for this survey. | [optional] |
| **agent** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **status** | **str** |  | [optional] |
| **queue** | [**QueueReference**](QueueReference.html) |  | [optional] |
| **answers** | [**SurveyScoringSet**](SurveyScoringSet.html) |  | [optional] |
| **completed_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **survey_error_details** | [**SurveyErrorDetails**](SurveyErrorDetails.html) | Additional information about what happened when the survey is in Error status. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}



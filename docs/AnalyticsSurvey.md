# AnalyticsSurvey

## AnalyticsSurvey

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_time** | datetime | Specifies when an event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **queue_id** | str | The ID of the associated queue | [optional] |
| **survey_completed_date** | datetime | Completion datetime of the survey in ISO 8601 format | [optional] |
| **survey_form_context_id** | str | Unique identifier for the survey form, regardless of version | [optional] |
| **survey_form_id** | str | ID of the survey form used | [optional] |
| **survey_form_name** | str | Name of the survey form used | [optional] |
| **survey_id** | str | ID of the survey | [optional] |
| **survey_partial_response** | bool | Whether the survey was completed with any required questions unanswered. | [optional] |
| **survey_promoter_score** | int | Score of the survey used with NPS | [optional] |
| **survey_status** | str | The status of the survey | [optional] |
| **survey_type** | str | The type of the survey | [optional] |
| **user_id** | str | ID of the agent the survey was performed against | [optional] |
| **o_survey_total_score** | int |  | [optional] |



_PureCloudPlatformClientV2 227.1.0_
